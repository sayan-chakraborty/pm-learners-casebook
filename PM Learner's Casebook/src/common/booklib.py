"""Shared build helpers for every module (design system approved at S0).

qa_html()      verbatim case -> Q/A turns (opening question box first)
number_figs()  {{FIG:key}} / {{REF:key}} -> "Figure M.n"
render()       HTML -> PDF (Chromium via Playwright) -> PNG previews
scan()         banned words and em-dashes in author-written text
"""
import html, os, re, sys, pathlib
COMMON = pathlib.Path(__file__).resolve().parent
ROOT = COMMON.parents[2]                                     # project folder
sys.path.insert(0, str(ROOT / "_pm_guide_toolkit"))
import cases2                                                # noqa: E402

def qa_html(src, pages, fix=None, drop=()):
    """fix: list of (old, new) replacements on paragraph text (extraction glitches only).
    drop: substrings; a paragraph starting with one is removed (running headers)."""
    fix = fix or []
    out, first, pend = [], True, ""
    for pno in pages:
        for k, lines, _ in cases2.segments(src, pno):
            if k == "T":
                out.append("<table class='tbl'>" + "".join(
                    "<tr>" + "".join(f"<{'th' if i == 0 else 'td'}>{html.escape(c)}</{'th' if i == 0 else 'td'}>" for c in r) + "</tr>"
                    for i, r in enumerate(lines)) + "</table>")
                continue
            s = "¶¶".join(p for p in cases2.join(lines) if p)
            for a, b in fix: s = s.replace(a, b)
            s = re.sub(r"(^|¶¶)o ", r"\1◦ ", s)
            paras = []
            for p in s.split("¶¶"):
                for d in drop:
                    if p.startswith(d): p = p[len(d):].strip()
                if p.strip(): paras.append(p.strip())
            if not paras: continue
            if k == "X":                       # sub-heading inside a candidate answer: carry into the next turn
                pend += "".join(f"<p><b>{html.escape(p)}</b></p>" for p in paras); continue
            def fmt(p, i):
                p = html.escape(p).replace("[[", "<span class='edit'>").replace("]]", "</span>")
                if i == 0: return p
                return re.sub(r"^([A-Z][A-Za-z0-9 /&()-]{0,34}:)", r"<b>\1</b>", p)
            body = "".join(f"<p>{fmt(p, i)}</p>" for i, p in enumerate(paras))
            if k == "C" and pend: body, pend = pend + body, ""
            if k == "I" and first:
                out.append(f'<div class="opening"><span class="lbl">The question</span>{body}</div><div class="qa">')
                first = False
            elif k == "I":
                out.append(f'<div class="turn q"><div class="who">Q</div><div class="body">{body}</div></div>')
            elif k == "C":
                out.append(f'<div class="turn a"><div class="who">A</div><div class="body">{body}</div></div>')
            else:
                out.append(f'<p class="q2">{body}</p>')
    out.append("</div>")
    return "\n".join(out)

def text_fill_to_style(t):
    """CSS `svg.d text{fill}` beats a fill="" attribute, so move text fills into inline styles."""
    def fix(m):
        tag = m.group(0)
        fm = re.search(r' fill="(#[0-9a-fA-F]{3,6})"', tag)
        if not fm: return tag
        tag = tag.replace(fm.group(0), "")
        if ' style="' in tag: return tag.replace(' style="', f' style="fill:{fm.group(1)};', 1)
        return tag[:-1] + f' style="fill:{fm.group(1)}">'
    return re.sub(r"<text\s[^>]*>", fix, t)

def number_figs(t, module):
    keys = re.findall(r"\{\{FIG:([\w-]+)\}\}", t)
    num = {k: f"{module}.{i + 1}" for i, k in enumerate(keys)}
    missing = set(re.findall(r"\{\{REF:([\w-]+)\}\}", t)) - set(num)
    if missing: print("!! undefined figure refs:", missing)
    t = re.sub(r"\{\{FIG:([\w-]+)\}\}", lambda m: f"Figure {num[m.group(1)]}", t)
    t = re.sub(r"\{\{REF:([\w-]+)\}\}", lambda m: f"Figure {num.get(m.group(1), '?')}", t)
    return t, len(keys)

BANNED = [r"\bdelve", r"\bcrucial", r"\blandscape", r"\btapestry", r"\bleverag(e|es|ing|ed)\b(?! ratio)", r"\brobust",
          r"\bseamless", r"fast-paced world", r"\bin conclusion", r"\bgenuinely", r"\bhonestly", r"\bstraightforward"]

def scan(text, label=""):
    """Scan author-written text (case text excluded by the caller). Returns hit list."""
    plain = re.sub(r"<[^>]+>", " ", text)
    hits = []
    for pat in BANNED:
        for m in re.finditer(pat, plain, re.I):
            hits.append((pat, plain[max(0, m.start() - 40): m.end() + 40].replace("\n", " ")))
    for m in re.finditer("—", plain):
        hits.append(("em-dash", plain[max(0, m.start() - 40): m.end() + 40].replace("\n", " ")))
    for p, ctx in hits: print(f"  [{label}] {p}: …{ctx}…")
    return hits

def render(html_path, pdf_path, footer, png_dir=None, dpi=80):
    from playwright.sync_api import sync_playwright
    foot = ('<div style="width:100%;font-family:Inter,Segoe UI,Arial;font-size:7px;color:#7a838d;'
            f'padding:0 15mm;display:flex;justify-content:space-between"><span>{footer}</span>'
            '<span class="pageNumber"></span></div>')
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto(pathlib.Path(html_path).resolve().as_uri(), wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        pg.pdf(path=str(pdf_path), format="A4", print_background=True, display_header_footer=True,
               header_template="<span></span>", footer_template=foot,
               margin=dict(top="13mm", bottom="14mm", left="15mm", right="15mm"))
        b.close()
    import pymupdf as fitz
    d = fitz.open(pdf_path)
    if png_dir:
        png_dir = pathlib.Path(png_dir); png_dir.mkdir(exist_ok=True)
        for f in png_dir.glob("*.png"): f.unlink()
        for i, page in enumerate(d):
            page.get_pixmap(dpi=dpi).save(png_dir / f"p{i + 1:02d}.png")
    n = len(d); d.close()
    return n
