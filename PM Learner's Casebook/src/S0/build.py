"""S0 build: template -> HTML (verbatim case + generated chart) -> PDF (Chromium) -> PNG previews."""
import html, os, re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]                      # project folder
sys.path.insert(0, str(ROOT / "_pm_guide_toolkit"))
import cases2                                # noqa: E402

OUT_PDF = HERE.parents[1] / "S0 - Style sample.pdf"
PNG_DIR = HERE / "png"

def qa_html(src, pages):
    """Verbatim case as Q/A turns. First interviewer block -> highlighted opening box."""
    out, first = [], True
    for pno in pages:
        for k, lines, _ in cases2.segments(src, pno):
            if k == "T":
                rows = lines
                out.append("<table class='tbl'>" + "".join(
                    "<tr>" + "".join(f"<{'th' if i == 0 else 'td'}>{html.escape(c)}</{'th' if i == 0 else 'td'}>" for c in r) + "</tr>"
                    for i, r in enumerate(rows)) + "</table>")
                continue
            paras = [p for p in cases2.join(lines) if p]
            def fmt(p, i):
                p = html.escape(p)
                if i == 0: return p                     # first paragraph is speech: leave it as spoken
                return re.sub(r"^([A-Z][A-Za-z /&-]{0,28}:)", r"<b>\1</b>", p)   # list lead-ins like "Short term:"
            body = "".join(f"<p>{fmt(p, i)}</p>" for i, p in enumerate(paras))
            if k == "I" and first:
                out.append(f'<div class="opening"><span class="lbl">The question</span>{body}</div><div class="qa">')
                first = False
            elif k == "I":
                out.append(f'<div class="turn q"><div class="who">Q</div><div class="body">{body}</div></div>')
            elif k == "C":
                out.append(f'<div class="turn a"><div class="who">A</div><div class="body">{body}</div></div>')
            else:
                out.append(f'<p class="small muted">{body}</p>')
    out.append("</div>")
    return "\n".join(out)

def tail_chart():
    times = [1.2] * 90 + [3.0] * 8 + [15.0] * 2
    x0, bw, base, k = 60, 5.6, 128, 100 / 15
    col = {1.2: "#9fb3c8", 3.0: "#e0a340", 15.0: "#b93a32"}
    bars = "".join(f'<rect x="{x0 + i * bw:.1f}" y="{base - t * k:.1f}" width="{bw - .6:.1f}" height="{t * k:.1f}" fill="{col[t]}"/>'
                   for i, t in enumerate(times))
    grid = "".join(f'<line x1="56" y1="{base - s * k:.1f}" x2="622" y2="{base - s * k:.1f}" stroke="#e3e7eb"/>'
                   f'<text x="52" y="{base - s * k + 4:.1f}" text-anchor="end" class="s">{s} s</text>' for s in (0, 5, 10, 15))
    mean_y = base - 1.62 * k
    p95x = x0 + 94 * bw + (bw - .6) / 2
    p99x = x0 + 98 * bw + (bw - .6) / 2
    svg = f'''<figure><svg class="d" viewBox="0 0 680 150" xmlns="http://www.w3.org/2000/svg">
 {grid}{bars}
 <line x1="56" y1="{mean_y:.1f}" x2="622" y2="{mean_y:.1f}" stroke="#1c232b" stroke-width="1.4" stroke-dasharray="5 3"/>
 <text x="64" y="{mean_y - 6:.1f}" class="b">mean = 1.62 s: looks fine</text>
 <line x1="{p95x:.1f}" y1="{base - 3 * k - 4:.1f}" x2="{p95x:.1f}" y2="72" stroke="#c47f17" stroke-width="1.2"/>
 <text x="{p95x - 4:.1f}" y="70" text-anchor="end" class="b" fill="#9a6310">p95 = 3 s</text>
 <text x="{p99x - 12:.1f}" y="36" text-anchor="end" class="b red">p99 = 15 s: 2 in 100 hit the timeout</text>
 <text x="630" y="{base - 3:.1f}" class="s">90 × 1.2 s</text>
 <text x="340" y="146" text-anchor="middle" class="s">100 payments, sorted from fastest to slowest (illustrative)</text>
</svg>
<figcaption><b>Figure 1.7 · The same 100 payments, three summaries.</b> The mean hides the two payments that hang for 15 s; p95 and p99 show them. Payments teams set targets on p95/p99 and success rate for this reason. <span class="src">Illustrative numbers.</span></figcaption></figure>'''
    return svg

def build():
    t = (HERE / "s0.html").read_text(encoding="utf-8")
    t = t.replace("{{A308}}", qa_html("iima", [308])).replace("{{TAILCHART}}", tail_chart())
    out_html = HERE / "s0_built.html"
    out_html.write_text(t, encoding="utf-8")
    from playwright.sync_api import sync_playwright
    foot = ('<div style="width:100%;font-family:Inter,Segoe UI,Arial;font-size:7px;color:#7a838d;'
            'padding:0 15mm;display:flex;justify-content:space-between">'
            '<span>PM Learner’s Casebook · S0 style sample</span><span class="pageNumber"></span></div>')
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto(out_html.as_uri(), wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        pg.pdf(path=str(OUT_PDF), format="A4", print_background=True, display_header_footer=True,
               header_template="<span></span>", footer_template=foot,
               margin=dict(top="13mm", bottom="14mm", left="15mm", right="15mm"))
        b.close()
    import pymupdf as fitz
    PNG_DIR.mkdir(exist_ok=True)
    for f in PNG_DIR.glob("*.png"): f.unlink()
    d = fitz.open(OUT_PDF)
    for i, page in enumerate(d):
        page.get_pixmap(dpi=int(os.environ.get("DPI", 80))).save(PNG_DIR / f"p{i + 1}.png")
    print(f"{OUT_PDF.name}: {len(d)} pages")

if __name__ == "__main__":
    build()
