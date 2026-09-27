"""M3 build: parts/*.html -> one HTML (verbatim cases injected, figures numbered) -> PDF -> PNG previews.
usage: python build.py            full module
       PARTS=1,2 python build.py  only parts whose file name starts with those prefixes (checkpoints)

segments2() extends cases2.segments for M2's casebook pages:
- bullet glyphs extracted after the first line of their item are moved back in front of it
- tables used as page layout (one filled cell per row) become turns; speakers come from `who`
- real tables lose empty columns and have continuation rows merged
- `kill`: segments whose text starts with a prefix are replaced (None = removed, str = editorial note)"""
import os, re, sys, html, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "common"))
import booklib  # noqa: E402
import cases2   # noqa: E402
sys.path.insert(0, str(HERE))
import m3_figs  # noqa: E402

OUT_PDF = HERE.parents[1] / "M3 - E-commerce & marketplaces.pdf"
_orig = cases2.segments
_ctx = {}

def _swap_bullets(lines):
    out = []
    for t in lines:
        if _ctx.get("swap") and t.strip() == "•" and out and not out[-1].lstrip("\n").startswith("•"):
            prev = out.pop(); nl = "\n" if prev.startswith("\n") else ""
            out.append(nl + "• " + prev.lstrip("\n"))
        else:
            out.append(t)
    return out

def _cell_lines(c):
    """a single layout cell -> lines, splitting inline bullets and numbered items"""
    c = re.sub(r"\s*•\s*", "\n• ", c)
    c = re.sub(r"\s(\d)\.\s+(?=[A-Z])", r"\n\1. ", c)
    return [("\n" + x if i else x) for i, x in enumerate(c.split("\n")) if x.strip()]

def segments2(src, pno):
    who = _ctx.get("who"); kill = _ctx.get("kill", {})
    segs = []; table = None
    def flush():
        nonlocal table
        if table:
            cols = [i for i in range(len(table[0])) if any(r[i] for r in table)]
            rows = []
            for r in table:
                r = [r[i] for i in cols]
                if rows and not r[0] and any(r): rows[-1] = [(a + " " + b).strip() for a, b in zip(rows[-1], r)]
                elif rows and r == rows[0]: continue             # header repeated on the next page
                elif any(r): rows.append(r)
            if segs and segs[-1][0] == "T" and segs[-1][1][0] == rows[0]: segs[-1][1].extend(rows[1:])
            else: segs.append(("T", rows, None))
        table = None
    for k, lines, it in _orig(src, pno):
        if k == "T":
            for r in lines:
                filled = [c for c in r if c]
                if not filled: continue
                if len(filled) == 1 and len(r) >= 2 and r[0] and not any(r[1:]):
                    flush()
                    sp = who.pop(0) if who else "C"
                    segs.append((sp, _cell_lines(filled[0]), None))
                else:
                    if table and len(r) != len(table[0]): flush()
                    table = (table or []) + [r]
            continue
        flush()
        segs.append((k, _swap_bullets(lines), it))
    flush()
    out = []
    for k, lines, it in segs:
        txt = " ".join(lines) if k != "T" else ""
        hit = next((p for p in kill if txt.startswith(p.split(":", 1)[1] if p[:3].isdigit() else p)
                    and (not p[:3].isdigit() or int(p[:3]) == pno)), None)
        if hit is not None:
            if kill[hit]: out.append(("N", ["[[" + kill[hit] + "]]"], None))
            continue
        out.append((k, lines, it))
    return out

cases2.segments = segments2

def qa(src, pages, who=None, kill=None, **kw):
    _ctx.clear(); _ctx.update(who=list(who or []), kill=kill or {}, swap=(src == "iima"))
    h = booklib.qa_html(src, pages, **kw)
    # inline bullets inside table cells -> line breaks
    h = re.sub(r"<td>(.*?)</td>", lambda m: "<td>" + re.sub(r"(?<=\S) ?• ", "<br>• ", m.group(1)) + "</td>", h, flags=re.S)
    # consecutive candidate turns (split by page layout) -> one turn
    A = '<div class="turn a"><div class="who">A</div><div class="body">'
    pat = re.compile("(" + re.escape(A) + r'(?:(?!<div class="turn).)*?)</div></div>\n' + re.escape(A), re.S)
    while pat.search(h): h = pat.sub(r"\1", h)
    # long turns may break across pages (short ones stay whole)
    h = re.sub(r'<div class="turn (a|q)">(<div class="who">.</div><div class="body">)((?:(?!<div class="turn).)*?)</div></div>',
               lambda m: f'<div class="turn {m.group(1)}{" long" if m.group(3).count("<p>") > 5 else ""}">{m.group(2)}{m.group(3)}</div></div>', h, flags=re.S)
    # a table continued on the next page (same header row) -> one table
    h = re.sub(r"(<tr><th>.*?</tr>)((?:(?!</table>).)*)</table>\s*<table class='tbl'>\1", r"\1\2", h, flags=re.S)
    return h

REDRAWN = "The original shows a diagram here; it is redrawn as {{REF:%s}}, labelled \"redrawn from the original\"."
CASES = {
    "B107": ("iimb", [107, 108], dict(
        kill={"108:You are a Product Manager at Myntra": None},
        fix=[("structure: User Personas", "structure:¶¶1. User Personas"), ("Pain Points AI-Driven", "Pain Points¶¶2. AI-Driven"),
             ("Solutions Prioritization", "Solutions¶¶3. Prioritization"), ("Feasibility) Success", "Feasibility)¶¶4. Success"),
             ("need AI can bridge", "need AI can bridge"),
             ("and \"experiencing\": The", "and \"experiencing\":¶¶The"),
             ("need a Stylist. The Trend", "need a Stylist.¶¶The Trend"), ("Discovery Friction. The Fit", "Discovery Friction.¶¶The Fit"),
             ("need Validation. I will", "need Validation.¶¶I will"),
             ("features: \"Myntra", "features:¶¶\"Myntra"), ("friend. \"Snap", "friend.¶¶\"Snap"),
             ("session time. \"StyleGPT\"", "session time.¶¶\"StyleGPT\""),
             ("North Star Metric: # of AI Interactions per DAU (How many users are actually talking to the stylist daily). L1 Metrics: Turn",
              "North Star Metric: # of AI Interactions per DAU (How many users are actually talking to the stylist daily).¶¶L1 Metrics:¶¶Turn")])),
    "A290": ("iima", [290], dict(fix=[("actions. Seller Journey", "actions.¶¶Seller Journey"), ("• Handover the product The last", "• Handover the product¶¶The last"),
             ("ecosystem. Buyer Journey", "ecosystem.¶¶Buyer Journey"), ("• Receive the product There", "• Receive the product¶¶There"),("Seller Journey Visit", "Seller Journey¶¶Visit"), ("Buyer Journey Visit", "Buyer Journey¶¶Visit"),
             ("1. Awareness Measures", "1. Awareness: Measures"), ("2. Activation Measures", "2. Activation: Measures"),
             ("3. Conversion Measures", "3. Conversion: Measures"), ("4. Retention Measures", "4. Retention: Measures"),
             ("Metric would be: Unique", "Metric would be:¶¶Unique"), ("the platform. As a counter", "the platform.¶¶As a counter"),
             ("I’d track: Purchases", "I’d track:¶¶Purchases"), ("I'd track: Purchases", "I'd track:¶¶Purchases")])),
    "B70": ("iimb", [70, 71], {}),
    "A297": ("iima", [297], dict(fix=[("1. Existing Prime Customers Reducing", "1. Existing Prime Customers¶¶Reducing"),
             ("2. New Prime Customers Next", "2. New Prime Customers¶¶Next"), ("40 million new members. Membership Revenue Incremental", "40 million new members.¶¶Membership Revenue: Incremental"),
             ("= $3.6B Incremental Shipping Cost Assume", "= $3.6B¶¶Incremental Shipping Cost: Assume"),
             ("= $0.8B Incremental Commerce Revenue Prime", "= $0.8B¶¶Incremental Commerce Revenue: Prime"),
             ("= +$1.2B Based", "= +$1.2B¶¶Based")])),
    "B94": ("iimb", [94], {}),
    "B141": ("iimb", [141], {}),
    "A240": ("iima", [240, 241], dict(fix=[("Path 1 - Coverage Of", "Path 1 - Coverage¶¶Of"), ("Path 2 - Throughput Now", "Path 2 - Throughput¶¶Now"),
             ("the evening rush. The busiest", "the evening rush. The busiest"), ("reconcile. Recommendation", "reconcile.¶¶Recommendation")])),
}

def post_case(key, h):
    """page-layout fixes that need moving whole blocks (visible notes where content moves)"""
    if key == "A240":
        # the casebook prints the coverage table in the right-hand column under 'Path 2'; move it back to the coverage path
        m = re.search(r"<table class='tbl'><tr><th>Coverage maths.*?</table>", h, re.S)
        if m:
            tbl = m.group(0); h = h.replace(tbl, "", 1)
            i = h.find('<div class="turn a"><div class="who">A</div><div class="body"><p>Path 2')
            if i > 0:
                h = h[:i] + tbl + '<p class="edit">The coverage table is printed beside \"Path 2\" in the casebook; it is moved up to follow the coverage path it belongs to.</p>' + h[i:]
        h = h.replace('<div class="turn a"><div class="who">A</div><div class="body"><p>Reconciling</p></div></div>', '<p class="q2">Reconciling</p>')
        h = h.replace("<p>Recommendation</p></div></div>", '</div></div><p class="q2">Recommendation</p>')
    if key == "B70":
        h = re.sub(r"<p>(\d)\.</p>\s*<p>(?:<b>)?", lambda m: f"<p>{m.group(1)}. <b>" if "<b>" in m.group(0) else f"<p>{m.group(1)}. ", h)
    return h

HEAD = """<!DOCTYPE html><html lang="en-GB"><head><meta charset="utf-8"><title>E-commerce &amp; marketplaces</title>
<link rel="stylesheet" href="../common/style.css"></head><body>
"""

def build():
    only = os.environ.get("PARTS")
    files = sorted((HERE / "parts").glob("*.html"))
    if only: files = [f for f in files if f.name.split("_")[0] in only.split(",")]
    body = ""; hits = 0
    for f in files:
        t = f.read_text(encoding="utf-8")
        hits += len(booklib.scan(t, f.name))
        body += t + "\n"
    for key, (src, pages, kw) in CASES.items():
        if "{{CASE:%s}}" % key in body:
            body = body.replace("{{CASE:%s}}" % key, post_case(key, qa(src, pages, **kw)))
    for k, svg in m3_figs.FIGS.items():
        body = body.replace("{{SVG:%s}}" % k, svg)
    import collections
    dup = [k for k, c in collections.Counter(re.findall(r"\{\{FIG:([\w-]+)\}\}", body)).items() if c > 1]
    if dup: print("!! duplicate figure keys:", dup)
    body = booklib.text_fill_to_style(body)
    body, nfig = booklib.number_figs(body, "3")
    out_html = HERE / "m3_built.html"
    out_html.write_text(HEAD + body + "</body></html>", encoding="utf-8")
    n = booklib.render(out_html, OUT_PDF, "PM Learner’s Casebook · E-commerce &amp; marketplaces", HERE / "png",
                       dpi=int(os.environ.get("DPI", 80)))
    print(f"{OUT_PDF.name}: {n} pages, {nfig} figures, {hits} style hits")

if __name__ == "__main__":
    build()
