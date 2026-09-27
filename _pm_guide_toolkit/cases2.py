import pymupdf as fitz, re, html
from cases import doc, kind
def fixcell(c):
    if c is None: return ""
    parts = str(c).split("\n"); out = parts[0]
    for p in parts[1:]:
        if out.endswith("-") or p.startswith("-") or (len(p) <= 2 and p.islower()): out += p
        else: out += " " + p
    return out.strip()

def segments(src, pno):
    p = doc(src)[pno - 1]; W, H = p.rect.width, p.rect.height
    top = H * (0.085 if src == "iima" else 0.125); bot = H * 0.935
    tabs = []
    try:
        for t in p.find_tables().tables:
            x0, y0, x1, y1 = t.bbox
            if y1 < top or y0 > bot: continue
            tabs.append(t)
    except Exception: pass
    def intab(bb): return any(bb[0] >= t.bbox[0] - 2 and bb[1] >= t.bbox[1] - 2 and bb[2] <= t.bbox[2] + 2 and bb[3] <= t.bbox[3] + 2 for t in tabs)
    items = []
    for b in p.get_text("dict")["blocks"]:
        if b["type"] != 0: continue
        for l in b["lines"]:
            spans = [s for s in l["spans"] if s["text"].strip()]
            if not spans: continue
            bb = l["bbox"]
            if bb[3] < top or bb[1] > bot or intab(bb): continue
            txt = "".join(s["text"] for s in l["spans"]).strip()
            items.append(dict(t=txt, k=kind(spans[0]["color"]), x0=bb[0], y0=bb[1], y1=bb[3], sz=spans[0]["size"],
                              full=(bb[2] - bb[0]) > W * 0.62 and bb[1] < H * 0.3, col=0 if bb[0] < W * 0.47 else 1))
    for t in tabs:
        items.append(dict(t="", k="T", tab=t, x0=t.bbox[0], y0=t.bbox[1], y1=t.bbox[3], full=(t.bbox[2] - t.bbox[0]) > W * 0.62, col=0 if t.bbox[0] < W * 0.47 else 1, sz=9))
    items.sort(key=lambda it: (0 if it["full"] and it["y0"] < H * 0.3 else 1, it["col"], it["y0"]))
    # group into segments
    segs = []
    for it in items:
        if it["k"] == "T":
            rows = [[fixcell(c) for c in r] for r in it["tab"].extract()]
            segs.append(("T", rows, it)); continue
        if segs and segs[-1][0] == it["k"] and segs[-1][0] != "T":
            prev = segs[-1][2]
            gap = it["y0"] - prev["y1"]
            if gap < it["sz"] * 1.25 and prev["col"] == it["col"]:
                segs[-1][1].append(it["t"]); segs[-1] = (segs[-1][0], segs[-1][1], it); continue
            if gap < it["sz"] * 2.6 and prev["col"] == it["col"] and it["k"] != "I":
                segs[-1][1].append("\n" + it["t"]); segs[-1] = (segs[-1][0], segs[-1][1], it); continue
        segs.append((it["k"], [it["t"]], it))
    return segs

def join(lines):
    paras = []; cur = ""
    for t in lines:
        brk = t.startswith("\n"); t = t.strip()
        newitem = bool(re.match(r"^([•▪◦o]\s|[•▪◦\-–]|\d+[\.\)]\S?|[A-Z][A-Za-z /&]{0,28}:)", t))
        if cur and (brk or newitem): paras.append(cur); cur = t
        elif cur and re.search(r"[A-Za-z]-$", cur): cur += t
        else: cur = (cur + " " + t).strip()
    if cur: paras.append(cur)
    out = []
    for p in paras:
        if p in ("•", "o", "▪") and out is not None: out.append("•"); continue
        if out and out[-1] == "•": out[-1] = "• " + p
        else: out.append(p)
    return out

def render_pages(src, pages, notes=None):
    """notes: {segment index: html of a margin note to place before it}"""
    notes = notes or {}; out = []; idx = 0; first = True; qtext = None
    for pno in pages:
        for k, lines, _ in segments(src, pno):
            nh = notes.get(idx, "")
            if k == "T":
                rows = lines; h = "<table class='ctab'>" + "".join("<tr>" + "".join(f"<{'th' if i == 0 else 'td'}>{html.escape(c)}</{'th' if i == 0 else 'td'}>" for c in r) + "</tr>" for i, r in enumerate(rows)) + "</table>"
                out.append(nh + h); idx += 1; continue
            paras = join(lines)
            if k == "I" and first: qtext = " ".join(paras).strip()
            elif k == "I" and qtext and paras and paras[0].startswith(qtext):
                paras[0] = paras[0][len(qtext):].strip()
            body = "".join(f"<p>{html.escape(p)}</p>" for p in paras if p)
            if k == "I":
                cls, who = ("cq", "The question") if first else ("ci", "Interviewer")
            elif k == "X": cls, who = "cx", ""
            else: cls, who = "cc", "Candidate"
            if k != "X": first = False if k in ("I", "C") else first
            out.append(nh + f'<div class="dl {cls}">' + (f'<span class="who">{who}</span>' if who else "") + body + "</div>")
            idx += 1
    return "\n".join(out)

def dump(src, pages):
    i = 0
    for pno in pages:
        for k, lines, _ in segments(src, pno):
            if k == "T": print(f"[{i}T] table {len(lines)}x{len(lines[0])}: {lines[0]}")
            else: print(f"[{i}{k}] " + " / ".join(join(lines))[:260])
            i += 1
