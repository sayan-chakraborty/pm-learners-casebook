"""M9 build: parts/*.html -> one HTML (verbatim cases injected, figures numbered) -> PDF -> PNG previews.
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
import m9_figs  # noqa: E402

OUT_PDF = HERE.parents[1] / "M9 - Consumer hardware, loyalty & public services.pdf"
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

CASES = {
    "A245": ("iima", [245, 246], dict(fix=[("The remaining reason being busy on voting day I can", "The remaining reason – being busy on voting day – I can"),
        ("and closes the app a flow", "and closes the app – a flow")]), {}),
    "B93": ("iimb", [93], dict(), {}),
    "A285": ("iima", [285, 286], dict(fix=[("three parts: Reward structure Technical implementation Customer experience For the reward",
            "three parts:¶¶• Reward structure¶¶• Technical implementation¶¶• Customer experience¶¶For the reward"),
        ("three levels: Tata Group Points - ", "three levels:¶¶• Tata Group Points - "), ("brands. Brand Points - ", "brands.¶¶• Brand Points - "),
        ("programs. Store Points - ", "programs.¶¶• Store Points - "), ("promotions. A customer can", "promotions.¶¶A customer can"),
        ("inherit the applicable campaigns. This keeps", "inherit the applicable campaigns.¶¶This keeps"),
        ("unified customer profile One limitation", "unified customer profile¶¶One limitation"),
        ("I'd enable: Redemption within the same brand. Cross-brand", "I'd enable:¶¶• Redemption within the same brand.¶¶• Cross-brand"),
        ("possible. For example, points", "possible.¶¶For example, points"),
        ("before launch. This ensures", "before launch.¶¶This ensures")]), {}),
    "A239": ("iima", [239], dict(), {}),
    "B142": ("iimb", [142], dict(fix=[("= 20 million users For the top", "= 20 million users¶¶For the top"),
        ("Monthly : 40% Bi-monthly: 30%", "Monthly : 40%¶¶Bi-monthly: 30%"), ("= 3.3 Total number of orders per month:", "= 3.3¶¶Total number of orders per month:"),
        ("~ 3.5 million orders Assuming", "~ 3.5 million orders¶¶Assuming"), ("orders per day Number of Swiggy", "orders per day¶¶Number of Swiggy")]), {}),
}

A245_MET = ('<div class="turn a"><div class="who">A</div><div class="body"><p>The north-star metric is turnout lift – turnout among app users versus non-users, and overall turnout against the 55% baseline since that&#x27;s what the government actually hired for.</p>'
    '<p>Around it I&#x27;d track engagement (DAU/WAU, session duration, notification open rate), awareness (candidate-profile views per user, articles read, quiz completion), and conversion (voters registered through the app).</p></div></div>\n'
    '<p class="edit">[The casebook prints this answer across a layout table that splits its sentences; it is set out here in reading order, in the casebook’s words.]</p>\n')
A239_SEG = ('<div class="turn a"><div class="who">A</div><div class="body"><p>Thank you. Before I begin with the calculation, I’d like to outline my segmentation framework:</p>'
    '<p>1. <b>Urban vs rural:</b> given infrastructure and internet constraints in rural areas, adoption will concentrate in cities.</p>'
    '<p>2. <b>Age:</b> those aged 18-40 are the most likely users, given lifestyle and disposable income.</p>'
    '<p>3. <b>Income and digital access:</b> smartphone ownership, internet and digital payments as enablers.</p>'
    '<p>4. <b>Food-delivery propensity:</b> the share of the digitally-enabled group likely to use delivery.</p>'
    '<p>Are these factors exhaustive?</p></div></div>\n'
    '<p class="edit">[The casebook prints this list, and the note on the 41+ group, as layout tables that split the sentences; both are set out here in reading order, in the casebook’s words.]</p>\n')

def qa_case(key):
    src, pages, kw, kill, *who = CASES[key]
    return qa(src, pages, who=(who[0] if who else None), kill=kill, **kw)

TURN = lambda w, t: f'<div class="turn {w}"><div class="who">{w.upper()}</div><div class="body">{t}</div></div>'

def post_fix(key, h):
    h = re.sub(r"<p class=\"q2\"><p><span class='edit'>(.*?)</span></p></p>", r'<p class="edit">[\1]</p>', h, flags=re.S)
    if key == "A245":
        h = re.sub(r'<div class="turn a"><div class="who">A</div><div class="body"><p>The north-star metric.*?through the app\)\.</p></div></div>\n', lambda m: A245_MET, h, count=1, flags=re.S)
    if key == "A239":
        h = re.sub(r'<div class="turn a"><div class="who">A</div><div class="body"><p>Thank you\. Before I begin.*?Are these factors exhaustive\?</p></div></div>\n', lambda m: A239_SEG, h, count=1, flags=re.S)
        h = re.sub(r"So, 18-40 urban population = 50% of 70M = 35 million</p></div></div>\s*<table class='tbl'><tr><th>\(I&#x27;m treating 18.*?</table>\s*<div class=\"turn a\"><div class=\"who\">A</div><div class=\"body\"><p>this funnel is slightly conservative\.\)</p>",
                   "So, 18-40 urban population = 50% of 70M = 35 million</p><p>(I&#x27;m treating 18-40 as the core users; the 41+ group does order delivery too, at a lower rate, so this funnel is slightly conservative.)</p>", h, count=1, flags=re.S)
    return h

EXTRA = [r"\bunlock(s|ed|ing)?\s+(new|the (full |true )?potential|value|growth|opportunit|insight)", r"\bempower", r"game-changer", r"\bpivotal", r"plays a key role", r"worth noting", r"\bnot just\b",
         r"at its core", r"real magic", r"here's the thing", r"here’s the thing", r"\bnavigat(e|ing) the",
         r"below(?! the line)", r"that follows", r"above(?! zero| the line)"]

def post_case(key, h):
    """page-layout fixes that need moving whole blocks (visible notes where content moves)"""
    h = re.sub(r"<p>(\d)\.</p>\s*<p>(?:<b>)?", lambda m: f"<p>{m.group(1)}. <b>" if "<b>" in m.group(0) else f"<p>{m.group(1)}. ", h)
    h = post_fix(key, h)
    return h

HEAD = """<!DOCTYPE html><html lang="en-GB"><head><meta charset="utf-8"><title>Consumer hardware, loyalty &amp; public services</title>
<link rel="stylesheet" href="../common/style.css"><style>.opening{break-inside:avoid}.sw{break-inside:avoid}.prompts{display:flex;gap:8pt;margin:4pt 0 6pt;break-inside:avoid}.prompt{flex:1;font:8.2pt/1.4 Inter,sans-serif;padding:6pt 8pt;border-radius:4pt;border-left:3pt solid}.prompt.bad{background:#fcecea;border-color:#b93a32}.prompt.good{background:#e1f2ec;border-color:#127a64}.egcard{font:8pt/1.4 Inter,sans-serif}</style></head><body>
"""

def build():
    only = os.environ.get("PARTS")
    files = sorted((HERE / "parts").glob("*.html"))
    if only: files = [f for f in files if f.name.split("_")[0] in only.split(",")]
    body = ""; hits = 0
    for f in files:
        t = f.read_text(encoding="utf-8")
        hits += len(booklib.scan(t, f.name))
        plain = re.sub(r"<[^>]+>", " ", t)
        for pat in EXTRA:
            for m in re.finditer(pat, plain, re.I):
                hits += 1; print(f"  [{f.name}] {pat}: …{plain[max(0, m.start() - 40): m.end() + 40]}…")
        body += t + "\n"
    for key in CASES:
        if "{{CASE:%s}}" % key in body:
            body = body.replace("{{CASE:%s}}" % key, post_case(key, qa_case(key)))
    for k, svg in m9_figs.FIGS.items():
        body = body.replace("{{SVG:%s}}" % k, svg)
    import collections
    dup = [k for k, c in collections.Counter(re.findall(r"\{\{FIG:([\w-]+)\}\}", body)).items() if c > 1]
    if dup: print("!! duplicate figure keys:", dup)
    body = booklib.text_fill_to_style(body)
    body, nfig = booklib.number_figs(body, "9")
    out_html = HERE / "m9_built.html"
    out_html.write_text(HEAD + body + "</body></html>", encoding="utf-8")
    n = booklib.render(out_html, OUT_PDF, "PM Learner’s Casebook · Consumer hardware, loyalty &amp; public services", HERE / "png",
                       dpi=int(os.environ.get("DPI", 80)))
    print(f"{OUT_PDF.name}: {n} pages, {nfig} figures, {hits} style hits")

if __name__ == "__main__":
    build()
