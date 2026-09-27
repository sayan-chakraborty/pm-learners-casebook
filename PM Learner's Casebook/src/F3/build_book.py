"""F3: cover + preface + contents + detailed index (all linked) + the ten chapter PDFs -> one book with book-wide page numbers and bookmarks.
Run extract.py first (writes index.json). usage: python build_book.py"""
import json, re, html, pathlib, glob, sys
import pymupdf as fitz
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent; BOOK = HERE.parents[1]; ROOT = BOOK.parent
sys.path.insert(0, str(SRC / "common"))
OUT = ROOT / "PM Learner's Casebook (complete).pdf"
CH = json.loads((HERE / "index.json").read_text(encoding="utf-8"))
E = html.escape
norm = lambda s: re.sub(r"[^A-Z0-9]", "", s.upper())

# ---- original-case titles and case types from the chapter sources ----
SRCMAP, TYPES = {}, {}
for f in glob.glob(str(SRC / "M*/parts/*.html")) + glob.glob(str(SRC / "F2/parts/*.html")):
    s = open(f, encoding="utf-8").read()
    for m in re.finditer(r'class="t">(?:Case|Guesstimate|Question) ([\d.]+) · (.*?)</span>(.{0,500}?)class="pill">(.*?)<', s, re.S):
        t = re.sub(r"<[^>]+>", "", m.group(2)); SRCMAP[norm(t)] = html.unescape(t)
        if "Guesstimate" not in m.group(0)[:40]: TYPES[m.group(1)] = html.unescape(m.group(4))
    for m in re.finditer(r"Framework · (.*?)</span>", s, re.S):
        t = re.sub(r"<[^>]+>", "", m.group(1)).strip(); SRCMAP[norm(t)] = html.unescape(t)
def title(t):
    return SRCMAP.get(norm(t)) or t[:1] + t[1:].lower()

# ---- pages: cover (1) + front matter (n) + chapters ----
def plan(front_pages):
    start, p = {}, 1 + front_pages + 1
    for c in CH: start[c["code"]] = p; p += c["pages"]
    return start, p - 1

def link(page, text=None):
    return f'<a href="https://p/{page}">{E(str(text if text is not None else page))}</a>'

def pglink(p):
    return f'<a class="pg" href="https://p/{p}">{p}</a>'

def sections(c):
    k = c["kick"]; h = c["h1"]
    if c["code"] == "F2":
        return [("Behavioural interviews", 1)] + [(x["t"], x["p"]) for x in h]
    g = next((x["p"] for x in h if x["t"].startswith("Guesstimates")), k.get("GUESSTIMATES"))
    tech = k.get("TECHNOLOGY") or k.get("TECHNOLOGY FOR PMS")
    conn = next((x["p"] for x in h if x["t"].startswith("Connect the dots")), None)
    out = [("Sector primer", 1), ("Cases", k.get("CASES")), ("Guesstimates", g), ("Product teardowns", k.get("PRODUCT TEARDOWNS")),
           ("Technology", tech), ("Connect the dots", conn)]
    return [(a, b) for a, b in out if b]

def parts_of(c):
    k = c["kick"]; tech = k.get("TECHNOLOGY") or k.get("TECHNOLOGY FOR PMS") or 999
    tear = k.get("PRODUCT TEARDOWNS") or 999
    td = [x for x in c["h1"] if tear <= x["p"] < tech and not x["t"].startswith(("Guesstimates", "Connect"))]
    te = [x for x in c["h1"] if x["p"] >= tech and not x["t"].startswith("Connect")]
    return td, te

def front_html(front_pages):
    start, last = plan(front_pages)
    B = lambda c, p: start[c["code"]] + p - 1
    o = [f'<!DOCTYPE html><html lang="en-GB"><head><meta charset="utf-8"><link rel="stylesheet" href="{(SRC / "common/style.css").as_uri()}">'
         '<style>a{color:inherit;text-decoration:none}.toc{font-family:Inter,sans-serif;font-size:8.6pt}.toc .ch{display:flex;justify-content:space-between;font-weight:700;font-size:10.5pt;border-bottom:1px solid #d9dee4;padding:4pt 0 1pt;margin-top:4pt}'
         '.toc .ch a.pg,.ix a.pg{color:#0b5d7a;font-weight:700}.toc .sec{color:#4d5763;margin:1.5pt 0 0 0;line-height:1.5}.toc .sec a{color:#0b5d7a}'
         '.ix{font-family:Inter,sans-serif;font-size:7.9pt;column-count:2;column-gap:14pt}.ix .r{display:flex;justify-content:space-between;gap:6pt;break-inside:avoid;padding:.6pt 0;border-bottom:1px dotted #e1e5ea}'
         '.ix .h{font-weight:800;font-size:7.3pt;letter-spacing:.07em;text-transform:uppercase;color:#5b6470;margin:5pt 0 1pt;break-after:avoid}.ix .t{color:#7a838d}'
         '.pre p,.pre li{font-size:9.3pt;line-height:1.33}.pre .lede{font-size:9.6pt}.pre h2{margin-top:6pt}.parts{font-family:Inter,sans-serif;font-size:7.6pt}.parts td{padding:1.4pt 5pt}</style></head><body>']
    # preface
    o.append(PREFACE)
    # contents
    o.append('<section class="page"><div class="kicker">PM Learner’s Casebook</div><h1>Contents</h1><div class="toc">')
    o.append(f'<div class="ch"><span>{link(2, "Preface and how to read this book")}</span>{pglink(2)}</div>')
    for n, c in enumerate(CH):
        name = c["title"] if c["code"] != "F2" else "Behavioural interviews"
        lab = f"{n + 1}. {name}" if c["code"] != "F2" else f"10. {name}"
        o.append(f'<div class="ch"><span>{link(B(c, 1), lab)}</span><a class="pg" href="https://p/{B(c, 1)}">{B(c, 1)}</a></div>')
        o.append('<div class="sec">' + " · ".join(f'{E(a)} {link(B(c, p))}' for a, p in sections(c)[1 if c["code"] != "F2" else 1:]) + "</div>")
    o.append(f'<div class="ch"><span>{link(INDEX_PAGE[0], "Index: cases, guesstimates, frameworks, products, technology, behavioural questions")}</span>{pglink(INDEX_PAGE[0])}</div>')
    o.append("</div></section>")
    # index
    o.append('<section class="page" id="ix"><div class="kicker">PM Learner’s Casebook</div><h1>Index</h1><p class="small muted">Every entry links to its page. Page numbers are the book’s own, printed at the foot of every page.</p><div class="ix">')
    row = lambda t, p, tag="": f'<div class="r"><span>{t}{(" <span class=t>" + E(tag) + "</span>") if tag else ""}</span><a class="pg" href="https://p/{p}">{p}</a></div>'
    o.append('<div class="h">Cases, by sector</div>')
    for c in CH:
        for x in [l for l in c["labels"] if l["kind"] == "CASE"]:
            o.append(row(f'{x["num"]} {E(title(x["t"]))}', B(c, x["p"]), TYPES.get(x["num"], "")))
    o.append('<div class="h">Guesstimates</div>')
    for c in CH:
        for x in [l for l in c["labels"] if l["kind"] == "GUESSTIMATE"]:
            o.append(row(f'{x["num"]} {E(title(x["t"]))}', B(c, x["p"])))
    o.append('<div class="h">Frameworks, A to Z</div>')
    fw = sorted([(title(x["t"]), B(c, x["p"])) for c in CH for x in c["labels"] if x["kind"] == "FRAMEWORK"], key=lambda z: z[0].lower())
    for t, p in fw: o.append(row(E(t), p))
    o.append('<div class="h">Product teardowns, A to Z</div>')
    td = sorted([(x["t"], B(c, x["p"]), c["title"]) for c in CH if c["code"] != "F2" for x in parts_of(c)[0]], key=lambda z: z[0].lower())
    for t, p, s in td: o.append(row(E(t), p))
    o.append('<div class="h">Technology, in the order taught</div>')
    for c in CH:
        if c["code"] == "F2": continue
        for x in parts_of(c)[1]: o.append(row(E(x["t"]), B(c, x["p"])))
    o.append('<div class="h">Behavioural questions</div>')
    f2 = next(c for c in CH if c["code"] == "F2")
    for x in [l for l in f2["labels"] if l["kind"] == "QUESTION"]: o.append(row(f'{x["num"]} {E(title(x["t"]))}', B(f2, x["p"])))
    o.append("</div></section></body></html>")
    return "\n".join(o)

PREFACE = (HERE / "preface.html").read_text(encoding="utf-8")
INDEX_PAGE = [0]

def render(html_text, pdf, footer=True):
    from playwright.sync_api import sync_playwright
    tmp = HERE / "_tmp.html"; tmp.write_text(html_text, encoding="utf-8")
    foot = ('<div style="width:100%;font-family:Inter,Segoe UI,Arial;font-size:7px;color:#7a838d;padding:0 15mm;display:flex;justify-content:space-between">'
            '<span>PM Learner’s Casebook</span><span></span></div>') if footer else "<span></span>"
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        pg.goto(tmp.as_uri(), wait_until="networkidle"); pg.evaluate("document.fonts.ready")
        pg.pdf(path=str(pdf), format="A4", print_background=True, display_header_footer=footer, header_template="<span></span>",
               footer_template=foot, margin=dict(top="13mm", bottom="14mm", left="15mm", right="15mm") if footer else dict(top="0", bottom="0", left="0", right="0"))
        b.close()

def main():
    nc = sum(1 for c in CH for x in c["labels"] if x["kind"] == "CASE"); ng = sum(1 for c in CH for x in c["labels"] if x["kind"] == "GUESSTIMATE")
    nt = sum(len(parts_of(c)[0]) for c in CH if c["code"] != "F2")
    counts = f"{nc} real interview cases, {ng} guesstimates and {nt} product teardowns."
    print(counts)
    render((HERE / "cover.html").read_text(encoding="utf-8").replace("{{LOGO}}", (ROOT / "XLRI Logo.webp").as_uri()).replace("{{COUNTS}}", counts), HERE / "cover.pdf", footer=False)
    n = 4
    for _ in range(4):                                   # page count of the front matter settles in a pass or two
        render(front_html(n), HERE / "front.pdf")
        fr = fitz.open(HERE / "front.pdf"); got = len(fr)
        ix = next(i for i, pg in enumerate(fr) if "Every entry links to its page" in pg.get_text())
        fr.close()
        if got == n and INDEX_PAGE[0] == ix + 2: break
        n = got; INDEX_PAGE[0] = ix + 2
    start, last = plan(n)
    book = fitz.open(); book.insert_pdf(fitz.open(HERE / "cover.pdf")); book.insert_pdf(fitz.open(HERE / "front.pdf"))
    toc = [[1, "Cover", 1], [1, "Preface", 2], [1, "Contents", 2 + next(i for i, pg in enumerate(fitz.open(HERE / "front.pdf")) if "Contents" in pg.get_text()[:200])],
           [1, "Index", INDEX_PAGE[0]]]
    for c in CH:
        d = fitz.open(BOOK / c["file"]); s = start[c["code"]]
        book.insert_pdf(d)
        name = c["title"] if c["code"] != "F2" else "Behavioural interviews"
        toc.append([1, name, s])
        td, te = parts_of(c)
        for a, p in sections(c)[1:] if c["code"] != "F2" else sections(c)[1:]:
            toc.append([2, a, s + p - 1])
            if a == "Cases":
                for x in [l for l in c["labels"] if l["kind"] == "CASE"]: toc.append([3, f'{x["num"]} {title(x["t"])}', s + x["p"] - 1])
            if a == "Guesstimates":
                for x in [l for l in c["labels"] if l["kind"] == "GUESSTIMATE"]: toc.append([3, f'{x["num"]} {title(x["t"])}', s + x["p"] - 1])
            if a == "Product teardowns":
                for x in td: toc.append([3, x["t"], s + x["p"] - 1])
            if a == "Technology":
                for x in te: toc.append([3, x["t"], s + x["p"] - 1])
    # book-wide page numbers over each footer's right-hand number (cover unnumbered)
    for i in range(1, len(book)):
        pg = book[i]; r = pg.rect
        pg.draw_rect(fitz.Rect(r.width - 110, r.height - 26, r.width - 30, r.height - 10), color=None, fill=(1, 1, 1))
        pg.insert_textbox(fitz.Rect(r.width - 110, r.height - 22.2, r.width - 42.4, r.height - 10), str(i + 1), fontsize=7, fontname="helv",
                          color=(0.478, 0.514, 0.553), align=fitz.TEXT_ALIGN_RIGHT)
    # placeholder links (https://p/N) -> internal jumps
    nl = 0
    for i in range(len(book)):
        pg = book[i]
        for L in pg.get_links():
            u = L.get("uri") or ""
            m = re.match(r"https://p/(\d+)", u)
            if m:
                pg.delete_link(L); pg.insert_link({"kind": fitz.LINK_GOTO, "from": L["from"], "page": int(m.group(1)) - 1, "to": fitz.Point(0, 0)}); nl += 1
    book.set_toc(toc)
    book.set_metadata({"title": "PM Learner’s Casebook", "author": "Prepared for Sayan Chakraborty", "creator": "Claude Code"})
    book.save(OUT, garbage=3, deflate=True)
    print(f"{OUT.name}: {len(book)} pages, front matter {n}, {nl} links, {len(toc)} bookmarks")

if __name__ == "__main__":
    main()
