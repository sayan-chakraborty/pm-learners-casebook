"""M5 build: parts/*.html -> one HTML (verbatim cases injected, figures numbered) -> PDF -> PNG previews.
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
import m5_figs  # noqa: E402

OUT_PDF = HERE.parents[1] / "M5 - Social, creators & messaging.pdf"
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
    "B46": ("iimb", [46, 47], {}),
    "A288": ("iima", [288, 289], dict(fix=[
        ("• Brand partner If that's okay", "• Brand partner¶¶If that's okay"),
        ("Sure. Creator Journey", "Sure.¶¶Creator Journey:"), ("results. Buyer Journey", "results.¶¶Buyer Journey:"),
        ("creators and buyers. Creator Metrics Awareness", "creators and buyers.¶¶Creator Metrics:¶¶Awareness:"),
        ("• Invite CTR Engagement", "• Invite CTR¶¶Engagement:"), ("tagging creators Conversion", "tagging creators¶¶Conversion:"),
        ("a similar funnel. Buyer Metrics Awareness", "a similar funnel.¶¶Buyer Metrics:¶¶Awareness:"),
        ("• Product tag CTR Engagement", "• Product tag CTR¶¶Engagement:"), ("on product pages Conversion", "on product pages¶¶Conversion:"),
        ("Operational Metrics", "Operational Metrics:"), ("accuracy Guardrail Metrics", "accuracy¶¶Guardrail Metrics:"),
        ("from Creator Content) To measure", "from Creator Content)¶¶To measure"), ("campaign IDs I'd also", "campaign IDs¶¶I'd also")])),
    "B149": ("iimb", [149, 150], dict(fix=[("self-destructing messages The following", "self-destructing messages¶¶The following"),
        ("leaving WhatsApp for", "leaving WhatsApp for Telegram"), ("File sharinglimits", "File sharing limits")])),
    "A235": ("iima", [235], dict(fix=[("= 490M accounts I’ll assume", "= 490M accounts¶¶I’ll assume"), ("= 400M So, we have", "= 400M¶¶So, we have"),
        ("= 20M users Therefore,", "= 20M users¶¶Therefore,")])),
    "B136": ("iimb", [136], dict(fix=[("70 million Does this", "70 million¶¶Does this"), ("7 per day Does this", "7 per day¶¶Does this"),
        ("1.06 billion Total Number", "1.06 billion¶¶Total Number")])),
}

def post_fix(key, h):
    if key == "A288": h = h.replace("<p>Operational Metrics:</p>", "<p><b>Operational Metrics:</b></p>")
    if key == "A235":   # the equations are printed as layout tables: turn them back into the candidate's lines
        h = re.sub(r"</p></div></div>\s*<table class='tbl'><tr><th>Instagram uploads per day.*?</table>\s*<div class=\"turn a\"><div class=\"who\">A</div><div class=\"body\">",
                   "</p><p>Instagram uploads per day = active personal Instagram users × average posts per user per day.</p>", h, flags=re.S)
        h = re.sub(r"</p></div></div>\s*<table class='tbl'><tr><th>active users = population.*?</table>",
                   "</p><p>active users = population × % with smartphone and internet × % on Instagram × % monthly active</p>"
                   "<p>India&#x27;s population is about 1.4 billion. Assuming 70% smartphone and internet penetration:</p>"
                   "<p>1.4 billion × 70% = 980 million smartphone users with internet.</p></div></div>", h, flags=re.S)
    return h

EXTRA = [r"\bunlock(s|ed|ing)?\s+(new|the (full |true )?potential|value|growth|opportunit|insight)", r"\bempower", r"game-changer", r"\bpivotal", r"plays a key role", r"worth noting", r"\bnot just\b",
         r"at its core", r"real magic", r"here's the thing", r"here’s the thing", r"\bnavigat(e|ing) the"]

def post_case(key, h):
    """page-layout fixes that need moving whole blocks (visible notes where content moves)"""
    h = re.sub(r"<p>(\d)\.</p>\s*<p>(?:<b>)?", lambda m: f"<p>{m.group(1)}. <b>" if "<b>" in m.group(0) else f"<p>{m.group(1)}. ", h)
    h = post_fix(key, h)
    return h

HEAD = """<!DOCTYPE html><html lang="en-GB"><head><meta charset="utf-8"><title>Social, creators &amp; messaging</title>
<link rel="stylesheet" href="../common/style.css"><style>.opening{break-inside:avoid}.sw{break-inside:avoid}</style></head><body>
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
    for key, (src, pages, kw) in CASES.items():
        if "{{CASE:%s}}" % key in body:
            body = body.replace("{{CASE:%s}}" % key, post_case(key, qa(src, pages, **kw)))
    for k, svg in m5_figs.FIGS.items():
        body = body.replace("{{SVG:%s}}" % k, svg)
    import collections
    dup = [k for k, c in collections.Counter(re.findall(r"\{\{FIG:([\w-]+)\}\}", body)).items() if c > 1]
    if dup: print("!! duplicate figure keys:", dup)
    body = booklib.text_fill_to_style(body)
    body, nfig = booklib.number_figs(body, "5")
    out_html = HERE / "m5_built.html"
    out_html.write_text(HEAD + body + "</body></html>", encoding="utf-8")
    n = booklib.render(out_html, OUT_PDF, "PM Learner’s Casebook · Social, creators &amp; messaging", HERE / "png",
                       dpi=int(os.environ.get("DPI", 80)))
    print(f"{OUT_PDF.name}: {n} pages, {nfig} figures, {hits} style hits")

if __name__ == "__main__":
    build()
