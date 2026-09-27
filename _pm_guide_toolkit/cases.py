import os
import pymupdf as fitz, re, html
UP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..") + os.sep
SRC = {"iima": UP + "Product Mindset 2026-27.pdf", "iimb": UP + "Sigma PM Casebook 2026-27.pdf"}
_d = {}
def doc(src):
    if src not in _d: _d[src] = fitz.open(SRC[src])
    return _d[src]

def kind(color):
    if color == 0xffffff: return "I"
    r, g, b = color >> 16, (color >> 8) & 255, color & 255
    if max(r, g, b) < 70: return "C"
    return "X"   # coloured text: tips / labels

def page_items(src, pno):
    p = doc(src)[pno - 1]; W, H = p.rect.width, p.rect.height
    top = H * (0.085 if src == "iima" else 0.125); bot = H * 0.935
    blocks = []
    for b in p.get_text("dict")["blocks"]:
        if b["type"] != 0: continue
        x0, y0, x1, y1 = b["bbox"]
        if y1 < top or y0 > bot: continue
        lines = []
        for l in b["lines"]:
            spans = [s for s in l["spans"] if s["text"].strip() or s["text"] == " "]
            if not spans: continue
            txt = "".join(s["text"] for s in spans)
            bold = all((s["flags"] & 16) or "Bold" in s["font"] for s in spans if s["text"].strip())
            col = next((s["color"] for s in spans if s["text"].strip()), 0)
            lines.append((txt, bold, col, l["bbox"]))
        if not lines: continue
        k = kind(lines[0][2]); full = (x1 - x0) > W * 0.62
        colm = 0 if full else (0 if x0 < W * 0.47 else 1)
        blocks.append(dict(k=k, lines=lines, x0=x0, y0=y0, col=colm, full=full))
    blocks.sort(key=lambda b: (0 if b["full"] and b["y0"] < H * 0.3 else 1, b["col"], b["y0"]))
    return blocks

def join_lines(lines):
    out = []; cur = ""
    for txt, bold, col, bb in lines:
        t = txt.strip()
        if not t: continue
        newitem = bool(re.match(r"^([•▪◦\-–]|\d+[\.\)]\s|[a-z]\)\s|[A-Z][A-Za-z ]{0,30}:)", t))
        if cur and newitem: out.append(cur); cur = t
        elif cur and cur.endswith("-") and not cur.endswith(" -"): cur = cur + t
        else: cur = (cur + " " + t).strip()
    if cur: out.append(cur)
    return out

def is_complex(src, pno):
    """Pages with tables/diagrams: many short text blocks side by side, or many vector drawings."""
    p = doc(src)[pno - 1]; bl = page_items(src, pno)
    small = [b for b in bl if all(len(l[0].strip()) < 22 for l in b["lines"])]
    ndraw = len(p.get_drawings())
    return len(small) >= 9 or ndraw > (60 if src == "iima" else 40)

def render(src, pno):
    bl = page_items(src, pno); out = []; first = True
    for b in bl:
        paras = join_lines(b["lines"])
        if not paras: continue
        txt = "<br/>".join(html.escape(x) for x in paras)
        txt = re.sub(r"(^|<br/>)([•▪◦]\s*)", r"\1• ", txt)
        if b["k"] == "I":
            cls = "q" if first else "iv"; first = False
            out.append(f'<div class="dl {cls}"><span class="who">{"Question" if cls == "q" else "Interviewer"}</span>{txt}</div>')
        elif b["k"] == "X":
            out.append(f'<div class="dl tip">{txt}</div>')
        else:
            first = False
            out.append(f'<div class="dl cd"><span class="who">Candidate</span>{txt}</div>')
    # merge consecutive candidate blocks
    merged = []
    for h in out:
        if merged and h.startswith('<div class="dl cd">') and merged[-1].startswith('<div class="dl cd">'):
            merged[-1] = merged[-1][:-6] + "<br/>" + h.split('</span>', 1)[1][:-6] + "</div>"
        else: merged.append(h)
    return "\n".join(merged)
