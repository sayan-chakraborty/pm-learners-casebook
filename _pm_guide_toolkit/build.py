import os
import re, sys, os, glob, html, json
import markdown
sys.path.insert(0, os.path.dirname(__file__))
import dia
import pymupdf as fitz

ROOT = os.path.dirname(os.path.abspath(__file__))
UP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..") + os.sep
SRC = {"iima": UP + "Product Mindset 2026-27.pdf", "iimb": UP + "Sigma PM Casebook 2026-27.pdf"}
SRCNAME = {"iima": "IIM Ahmedabad · Product Mindset 2026-27", "iimb": "IIM Bangalore · Sigma PM Casebook 2026-27"}
IMG = os.path.join(ROOT, "img"); os.makedirs(IMG, exist_ok=True)
_docs = {}
PH = {}; CASEN = [0]; FIGN = [0]; TOC = []

def ph(htmlstr):
    k = f"PHX{len(PH):05d}PHX"; PH[k] = htmlstr; return f"\n\n{k}\n\n"

def slide(src, p):
    fn = os.path.join(IMG, f"{src}_{p}.jpg")
    if not os.path.exists(fn):
        if src not in _docs: _docs[src] = fitz.open(SRC[src])
        pg = _docs[src][p - 1]; r = pg.rect
        clip = fitz.Rect(r.x0, r.y0, r.x1, r.y1 - r.height * (0.055 if src == "iima" else 0.06))
        pix = pg.get_pixmap(dpi=165, clip=clip)
        pix.save(fn, jpg_quality=80)
    return fn

def pages(spec):
    out = []
    for part in spec.split(","):
        if "-" in part: a, b = part.split("-"); out += list(range(int(a), int(b) + 1))
        else: out.append(int(part))
    return out

def md(text):
    return markdown.markdown(text, extensions=["tables", "md_in_html", "attr_list", "sane_lists"])

def fig_block(body):
    meta = {}; lines = body.strip("\n").split("\n"); i = 0
    while i < len(lines) and re.match(r"^(title|sub|src|wide|cls):", lines[i]):
        k, v = lines[i].split(":", 1); meta[k] = v.strip(); i += 1
    code = "\n".join(lines[i:])
    ns = {k: getattr(dia, k) for k in dir(dia) if not k.startswith("_")}
    dia.CURW[0] = 640
    try:
        s = eval(code, ns)
    except Exception as e:
        print("DIAGRAM ERROR:", meta.get("title"), e, file=sys.stderr); raise
    FIGN[0] += 1
    cls = "chart" + (" wide" if meta.get("wide") else "") + (" " + meta["cls"] if meta.get("cls") else "")
    h = f'<figure class="{cls}">'
    if meta.get("title"): h += f'<div class="ch-title">{html.escape(meta["title"])}</div>'
    if meta.get("sub"): h += f'<div class="ch-sub">{html.escape(meta["sub"])}</div>'
    h += f'<div class="ch-body">{s}</div>'
    if meta.get("src"): h += f'<div class="ch-src">Source: {html.escape(meta["src"])}</div>'
    return h + "</figure>"

def case_block(head, body):
    # head: src pages | title | type | level
    parts = [x.strip() for x in head.split("|")]
    src, pg = parts[0].split(); title = parts[1]; typ = parts[2] if len(parts) > 2 else ""; lvl = parts[3] if len(parts) > 3 else ""
    CASEN[0] += 1; n = CASEN[0]
    cid = f"case{n}"
    TOC.append(("case", n, title, typ, cid))
    imgs = "".join(f'<img class="slide {src}" src="file://{slide(src, p)}"/>' for p in pages(pg))
    h = f'''</div><section class="case" id="{cid}"><span class="mk">@@{cid}@@</span><div class="case-head"><div class="case-meta">Case {n} · {html.escape(typ)}{(" · " + html.escape(lvl)) if lvl else ""} · {SRCNAME[src]} (p. {pg})</div>
<div class="case-title">{html.escape(title)}</div><div class="case-try">Try it first: read only the question in the dark bar, close the page and give yourself five minutes to sketch your structure out loud. Then read the model answer.</div></div>
<div class="slides">{imgs}</div>'''
    if body.strip():
        h += f'<div class="ourtake"><div class="ot-label">Our take</div>{md(body)}</div>'
    return h + '</section><div class="body">'

def box_block(kind, title, body):
    return f'<aside class="box {kind}"><div class="box-title">{html.escape(title)}</div>{md(body)}</aside>'

def process(text):
    # figures
    text = re.sub(r"```dia\n(.*?)```", lambda m: ph(fig_block(m.group(1))), text, flags=re.S)
    # case blocks
    text = re.sub(r"^::: case (.*?)\n(.*?)^:::\s*$", lambda m: ph(case_block(m.group(1), m.group(2))), text, flags=re.S | re.M)
    # boxes
    text = re.sub(r"^::: (box|key|quiz|try|note|words) ?(.*?)\n(.*?)^:::\s*$", lambda m: ph(box_block(m.group(1), m.group(2), m.group(3))), text, flags=re.S | re.M)
    return text

def directive(line):
    parts = [p.strip() for p in line[2:].split("|")]
    kind = parts[0]
    if kind == "part":
        num, title, intro = parts[1], parts[2], parts[3] if len(parts) > 3 else ""
        pid = "part-" + re.sub(r"\W+", "-", num.lower())
        TOC.append(("part", num, title, intro, pid))
        return f'<section class="partpage" id="{pid}"><span class="mk">@@{pid}@@</span><div class="part-num">{num}</div><div class="part-title">{title}</div><div class="part-intro">{md(intro)}</div></section>'
    if kind in ("chapter", "article"):
        rub, title, stand = parts[1], parts[2], parts[3] if len(parts) > 3 else ""
        aid = "a" + str(len(TOC))
        TOC.append((kind, rub, title, stand, aid))
        cls = "art-head chapter" if kind == "chapter" else "art-head"
        return f'<header class="{cls}" id="{aid}"><span class="mk">@@{aid}@@</span><div class="rubric">{html.escape(rub)}</div><h1 class="headline">{html.escape(title)}</h1><div class="standfirst">{html.escape(stand)}</div></header>'
    if kind == "raw":
        return "|".join(parts[1:])
    return ""

def render_file(path):
    txt = open(path, encoding="utf-8").read()
    segs = re.split(r"^(%% .*)$", txt, flags=re.M)
    out = []; open_body = False
    for s in segs:
        if s.startswith("%% "):
            if open_body: out.append("</div>"); open_body = False
            d = directive(s)
            out.append(d)
            k = s[3:].split("|")[0].strip()
            if k in ("chapter", "article"):
                out.append('<div class="body">'); open_body = True
            elif k == "onecol":
                out.append('<div class="body one">'); open_body = True
        else:
            if not s.strip(): continue
            if not open_body: out.append('<div class="body">'); open_body = True
            h = md(process(s))
            for k, v in PH.items():
                h = h.replace(f"<p>{k}</p>", v).replace(k, v)
            out.append(h)
    if open_body: out.append("</div>")
    return "\n".join(out)

PAGES = {}
def pn(i): return f'<span class="pn">{PAGES.get(i, "")}</span>'
def toc_html():
    rows = []
    for t in TOC:
        if t[0] == "part":
            rows.append(f'<div class="toc-part"><a href="#{t[4]}">{t[1]} · {html.escape(t[2])}</a>{pn(t[4])}</div>')
        elif t[0] == "chapter":
            rows.append(f'<div class="toc-ch"><a href="#{t[4]}"><span class="toc-rub">{html.escape(t[1])}</span> {html.escape(t[2])}</a>{pn(t[4])}</div>')
    return '<section class="toc"><div class="rubric">Contents</div><h1 class="headline">What is inside</h1>' + "".join(rows) + "</section>"

def case_index():
    rows = [f'<tr><td>{n}</td><td><a href="#{cid}">{html.escape(t)}</a></td><td>{html.escape(ty)}</td><td>{PAGES.get(cid,"")}</td></tr>' for k, n, t, ty, cid in [x for x in TOC if x[0] == "case"]]
    return '<section class="caseidx"><div class="rubric">Index</div><h1 class="headline">Every case in this book</h1><table class="idx"><tr><th>#</th><th>Case</th><th>Type</th><th>Page</th></tr>' + "".join(rows) + "</table></section>"

def chrome_pdf(src, out):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        pg.goto("file://" + src, wait_until="load"); pg.wait_for_timeout(400)
        pg.pdf(path=out, prefer_css_page_size=True, print_background=True); br.close()

def build(files, out, cover_html=""):
    body = "".join(render_file(f) for f in files)
    css = open(os.path.join(ROOT, "style.css")).read().replace("FONTDIR", os.path.join(ROOT, "fonts"))
    hp = out.replace(".pdf", ".html")
    for it in range(2):
        full = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>The PM Casebook</title><style>{css}</style></head><body>{cover_html}{toc_html()}{body}{case_index()}</body></html>'
        open(hp, "w").write(full); chrome_pdf(hp, out)
        doc = fitz.open(out); PAGES.clear()
        for i, page in enumerate(doc):
            for m in re.findall(r"@@([\w-]+)@@", page.get_text()):
                PAGES.setdefault(m, i + 1)
        doc.close()
    # stamp running rubric + bookmarks
    doc = fitz.open(out); marks = sorted([(PAGES[t[4]], t) for t in TOC if t[0] in ("chapter", "part") and t[4] in PAGES], key=lambda x: x[0])
    ff = os.path.join(ROOT, "fonts", "SourceSans3-700-normal.ttf")
    for i, page in enumerate(doc):
        cur = None
        for pno, t in marks:
            if pno <= i + 1: cur = t
        if cur and cur[0] == "chapter" and PAGES.get(cur[4]) != i + 1 and page.rect.width > 0:
            txt = cur[1].upper()
            page.insert_text((31.2, 30), txt, fontsize=7, fontfile=ff, fontname="ssb", color=(0.0, 0.42, 0.64))
    toc = []
    for t in TOC:
        if t[4] not in PAGES: continue
        if t[0] == "part": toc.append([1, f"{t[1]} · {t[2]}", PAGES[t[4]]])
        elif t[0] == "chapter": toc.append([2, t[2], PAGES[t[4]]])
        elif t[0] == "article": toc.append([3, t[2], PAGES[t[4]]])
        elif t[0] == "case": toc.append([3, f"Case {t[1]}: {t[2]}", PAGES[t[4]]])
    fixed = []; lvl = 0
    for e in toc:
        e[0] = min(e[0], lvl + 1); lvl = e[0]; fixed.append(e)
    doc.set_toc(fixed)
    doc.save(out.replace(".pdf", "_f.pdf"), garbage=3, deflate=True); doc.close()
    os.replace(out.replace(".pdf", "_f.pdf"), out)
    print("built", out, "cases:", CASEN[0], "figs:", FIGN[0], "pages:", len(fitz.open(out)))

if __name__ == "__main__":
    files = sorted(glob.glob(os.path.join(ROOT, "content", "*.md")))
    if len(sys.argv) > 2: files = [f for f in files if any(a in os.path.basename(f) for a in sys.argv[2:])]
    cover = open(os.path.join(ROOT, "cover.html")).read() if os.path.exists(os.path.join(ROOT, "cover.html")) else ""
    build(files, sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "out.pdf"), cover)
