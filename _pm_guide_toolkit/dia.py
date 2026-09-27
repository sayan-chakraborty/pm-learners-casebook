"""Economist-style *descriptive* diagram library (v2). Every primitive carries explanations, not just labels.
All functions return an SVG string. W is the viewBox width: 720 for full-width figures, 340 for one column."""
import math, subprocess, re, html

RED = "#E3120B"; B1 = "#006BA2"; B2 = "#3EBCD2"; TEAL = "#379A8B"; GOLD = "#EBB434"
OLIVE = "#B4BA39"; MAUVE = "#9A607F"; SAND = "#D1B07C"; GREY = "#758D99"; LG = "#EEF2F4"; INK = "#121212"; DG = "#3a4650"
NAVY = "#1F3A5F"
PAL = [B1, TEAL, GOLD, MAUVE, B2, OLIVE, SAND, GREY, RED]
F = "Sans"
CURW = [720]

def esc(s): return html.escape(str(s), quote=True)
def cw(size): return size * 0.50

def wrap(text, maxch):
    out = []
    for para in str(text).split("\n"):
        words = para.split(); cur = ""
        for w in words:
            if cur and len(cur) + 1 + len(w) > maxch: out.append(cur); cur = w
            else: cur = (cur + " " + w).strip()
        out.append(cur)
    return out or [""]

def nlines(text, width, size): return len(wrap(text, max(4, int(width / cw(size)))))

def T(x, y, text, size=11, weight=400, anchor="middle", fill=INK, width=None, lh=1.2, italic=False, valign="top"):
    lines = wrap(text, max(4, int(width / cw(size)))) if width else str(text).split("\n")
    h = size * lh; n = len(lines)
    if valign == "middle": y0 = y - n * h / 2 + size * 0.95
    elif valign == "bottom": y0 = y - n * h + size * 0.95
    else: y0 = y + size * 0.95
    st = ' font-style="italic"' if italic else ''
    o = [f'<text x="{x:.1f}" y="{y0:.1f}" font-family="{F}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}"{st}>']
    for i, l in enumerate(lines):
        o.append(f'<tspan x="{x:.1f}" dy="{0 if i == 0 else h:.1f}">{esc(l)}</tspan>')
    o.append('</text>')
    return "".join(o), n * h

def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="100%" preserveAspectRatio="xMidYMin meet">{defs()}{body}</svg>'

def defs():
    m = lambda i, c: f'<marker id="{i}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
    return f'<defs>{m("ag", GREY)}{m("ar", RED)}{m("ab", B1)}{m("ak", INK)}<filter id="sh" x="-5%" y="-5%" width="110%" height="120%"><feDropShadow dx="0" dy="1" stdDeviation="1.2" flood-color="#000" flood-opacity="0.12"/></filter></defs>'

def rect(x, y, w, h, fill="white", stroke="none", rx=4, sw=1, shadow=False, dash=None):
    f = ' filter="url(#sh)"' if shadow else ''
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{f}{d}/>'

def ln(x1, y1, x2, y2, c=GREY, w=1.4, arrow="ag", dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    m = f' marker-end="url(#{arrow})"' if arrow else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="{w}"{d}{m}/>'

def light(c, f=0.85):
    c = c.lstrip('#'); r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
    return '#%02x%02x%02x' % (int(r + (255 - r) * f), int(g + (255 - g) * f), int(b + (255 - b) * f))

def badge(x, y, n, c=RED, r=9):
    t, _ = T(x, y, str(n), 10.5 if r >= 8 else 9, 800, fill="white", valign="middle")
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{c}"/>' + t

def cardh(w, title, desc="", num=None, tsize=11.5, dsize=10):
    pad = 8; tw = w - 2 * pad - (18 if num is not None else 0)
    th = nlines(title, tw, tsize) * tsize * 1.2; dh = nlines(desc, w - 2 * pad, dsize) * dsize * 1.2 if desc else 0
    return pad + th + (5 + dh if desc else 0) + pad + 3

def card(x, y, w, title, desc="", c=B1, num=None, hl=False, tsize=11.5, dsize=10, minh=0, fill="white"):
    pad = 8; tw = w - 2 * pad - (18 if num is not None else 0)
    th = nlines(title, tw, tsize) * tsize * 1.2
    h = max(minh, cardh(w, title, desc, num, tsize, dsize)); col = RED if hl else c
    o = [rect(x, y, w, h, fill, "#cfd7dd", 3, 0.8), rect(x, y, w, 3, col, rx=0)]
    tx = x + pad + (18 if num is not None else 0)
    if num is not None: o.append(badge(x + pad + 7, y + pad + 8, num, col))
    t, _ = T(tx, y + pad + 1, title, tsize, 700, "start", col, tw); o.append(t)
    if desc:
        t, _ = T(x + pad, y + pad + th + 6, desc, dsize, 400, "start", DG, w - 2 * pad); o.append(t)
    return "".join(o), h

def _norm(it):
    if isinstance(it, str): return it, "", ""
    return (list(it) + ["", ""])[:3]

# ------------------------------------------------------------ processes
def steps(items, hl=None, c=B1, W=None, per_row=None, numbered=True, caption=None):
    """items: [(title, description, watch-out note)] → numbered cards joined by arrows (vertical if narrow)."""
    W = W or CURW[0]; items = [_norm(i) for i in items]; hl = hl or []
    if W < 500: return vsteps(items, hl, c, W, numbered)
    n = len(items); per_row = per_row or min(n, 5); rows = math.ceil(n / per_row); gap = 22
    bw = (W - 8 - gap * (per_row - 1)) / per_row; o = []; y = 4
    for r in range(rows):
        row = items[r * per_row:(r + 1) * per_row]
        ch = max(cardh(bw, t, d, 1) for t, d, _ in row)
        nh = max((nlines(nt, bw - 12, 9.5) * 11.4 + 8) if nt else 0 for _, _, nt in row)
        for j, (t, d, nt) in enumerate(row):
            i = r * per_row + j; x = 4 + j * (bw + gap)
            s, _ = card(x, y, bw, t, d, c, i + 1 if numbered else None, i in hl, minh=ch); o.append(s)
            if nt:
                h_ = nlines(nt, bw - 12, 9.5) * 11.4
                o.append(f'<line x1="{x + 5:.1f}" y1="{y + ch + 6:.1f}" x2="{x + 5:.1f}" y2="{y + ch + 6 + h_:.1f}" stroke="{RED}" stroke-width="2"/>')
                s, _ = T(x + 10, y + ch + 5, nt, 9.5, 400, "start", RED, bw - 12, italic=True); o.append(s)
            if j < len(row) - 1:
                o.append(ln(x + bw + 3, y + ch / 2, x + bw + gap - 3, y + ch / 2, GREY, 1.6))
        if r < rows - 1:
            xl = 4 + (len(row) - 1) * (bw + gap) + bw / 2; yb = y + ch + nh + 4
            o.append(f'<path d="M{xl:.1f},{y + ch:.1f} L{xl:.1f},{yb + 5:.1f} L{4 + bw / 2:.1f},{yb + 5:.1f} L{4 + bw / 2:.1f},{yb + 16:.1f}" fill="none" stroke="{GREY}" stroke-width="1.6" marker-end="url(#ag)"/>')
        y += ch + nh + (22 if r < rows - 1 else 0)
    if caption:
        s, h = T(4, y + 6, caption, 10, 400, "start", DG, W - 8, italic=True); o.append(s); y += h + 8
    return svg(W, y + 6, "".join(o))

def vsteps(items, hl=None, c=B1, W=None, numbered=True):
    W = W or CURW[0]; items = [_norm(i) for i in items]; hl = hl or []; o = []; y = 4; x0 = 26; ys = []
    for i, (t, d, nt) in enumerate(items):
        col = RED if i in hl else c
        s, th = T(x0 + 4, y, t, 11.5, 700, "start", col, W - x0 - 10); o.append(s)
        dh = 0
        if d: s, dh = T(x0 + 4, y + th + 2, d, 10, 400, "start", DG, W - x0 - 10); o.append(s)
        nh = 0
        if nt: s, nh = T(x0 + 4, y + th + dh + 5, "Watch out: " + nt, 9.5, 400, "start", RED, W - x0 - 10, italic=True); o.append(s); nh += 3
        ys.append((y, col)); y += th + dh + nh + 14
    for i, (yy, col) in enumerate(ys):
        if i < len(ys) - 1: o.insert(0, f'<line x1="11" y1="{yy + 10}" x2="11" y2="{ys[i + 1][0] + 2}" stroke="#c3ccd2" stroke-width="2"/>')
        o.append(badge(11, yy + 9, i + 1 if numbered else "•", col))
    return svg(W, y, "".join(o))

def journey(stages, rows, curve=None, W=None, c=B1):
    """Journey map. stages: [names]; rows: [(row label, [cell per stage])]; curve: feeling 1 (bad)–5 (good) per stage."""
    W = W or 720; n = len(stages); lw = 92; cwid = (W - lw - 8) / n; o = []; y = 4
    for j, s in enumerate(stages):
        x = lw + 4 + j * cwid
        o.append(f'<polygon points="{x:.1f},{y} {x + cwid - 8:.1f},{y} {x + cwid:.1f},{y + 15} {x + cwid - 8:.1f},{y + 30} {x:.1f},{y + 30} {x + 8:.1f},{y + 15}" fill="{c if j % 2 == 0 else NAVY}"/>')
        t, _ = T(x + cwid / 2 + 2, y + 15, s, 10.3, 700, fill="white", width=cwid - 20, valign="middle"); o.append(t)
    y += 36
    if curve:
        ch = 62; o.append(rect(4, y, W - 8, ch, "#f7f9fa", "none", 0)); t, _ = T(8, y + ch / 2, "How the user feels", 9.5, 700, "start", DG, lw - 10, valign="middle"); o.append(t)
        pts = [(lw + 4 + j * cwid + cwid / 2, y + ch - 9 - (v - 1) / 4 * (ch - 18)) for j, v in enumerate(curve)]
        o.append('<polyline fill="none" stroke="%s" stroke-width="2.2" points="%s"/>' % (GREY, " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)))
        for (a, b), v in zip(pts, curve): o.append(f'<circle cx="{a:.1f}" cy="{b:.1f}" r="5" fill="{RED if v <= 2 else (TEAL if v >= 4 else GOLD)}"/>')
        y += ch + 4
    for ri, (lab, cells) in enumerate(rows):
        pain = "pain" in lab.lower()
        rh = max([nlines(cl, cwid - 10, 9.6) * 9.6 * 1.2 for cl in cells] + [nlines(lab, lw - 10, 10) * 12]) + 12
        o.append(rect(4, y, W - 8, rh, light(RED, 0.92) if pain else (LG if ri % 2 == 0 else "white"), "none", 0))
        t, _ = T(8, y + 6, lab, 10, 700, "start", RED if pain else INK, lw - 10); o.append(t)
        for j, cl in enumerate(cells):
            t, _ = T(lw + 8 + j * cwid, y + 6, cl, 9.6, 400, "start", RED if pain else DG, cwid - 10); o.append(t)
        y += rh
    return svg(W, y + 4, "".join(o))

def funnel(stages, W=None, c=B1, hl=None):
    """stages: [(label, value text, share 0-1, note explaining the drop-off)]"""
    W = W or CURW[0]; hl = hl or []; o = []; y = 4; bw_max = W * (0.46 if W > 500 else 0.5); bh = 30
    cx = bw_max / 2 + 6; nx = bw_max + 20
    for i, st in enumerate(stages):
        lab, val, p = st[0], st[1], st[2]; note = st[3] if len(st) > 3 else ""
        w = max(bw_max * 0.2, bw_max * p); col = RED if i in hl else c
        o.append(rect(cx - w / 2, y, w, bh, col, rx=2))
        t, _ = T(cx, y + bh / 2, val, 11.5, 800, fill="white", valign="middle"); o.append(t)
        t, th = T(nx, y + 1, lab, 11, 700, "start", INK, W - nx - 4); o.append(t)
        nh = 0
        if note: t, nh = T(nx, y + 2 + th, note, 9.5, 400, "start", RED if i in hl else DG, W - nx - 4, italic=True); o.append(t)
        y += max(bh, th + nh + 4) + 8
    return svg(W, y, "".join(o))

# ------------------------------------------------------------ annotated charts
def bars(items, unit="", hl=None, W=None, c=B1, fmt="{:,.0f}", maxv=None, labelw=None, notes=True):
    """items: [(label, value, optional explanatory note)]"""
    W = W or CURW[0]; hl = hl or []; items = [tuple(i) + ("",) * (3 - len(i)) for i in items]
    labelw = labelw or (150 if W > 500 else 96); maxv = maxv or max(v for _, v, _ in items) * 1.12
    hasn = notes and any(n for _, _, n in items) and W > 500
    x0 = labelw + 8; aw = (W - x0 - 10) * (0.5 if hasn else 0.8); nx = x0 + aw + 60
    o = []; y = 16
    for k in range(5):
        gx = x0 + aw * k / 4
        o.append(f'<line x1="{gx:.1f}" y1="12" x2="{gx:.1f}" y2="{16 + len(items) * 30}" stroke="#dde3e7" stroke-width="0.8"/>')
        t, _ = T(gx, 0, fmt.format(maxv * k / 4) + unit, 8.8, 400, fill=GREY); o.append(t)
    for i, (lab, v, nt) in enumerate(items):
        col = RED if (lab in hl or i in hl) else c; w = aw * v / maxv
        t, _ = T(labelw, y + 11, lab, 10.3, 600, "end", INK, labelw - 4, valign="middle"); o.append(t)
        o.append(rect(x0, y + 2, max(w, 1.5), 18, col, rx=0))
        t, _ = T(x0 + w + 4, y + 11, fmt.format(v) + unit, 10.3, 800, "start", col, valign="middle"); o.append(t)
        if hasn and nt: t, _ = T(nx, y + 11, nt, 9.3, 400, "start", DG, W - nx - 4, italic=True, valign="middle"); o.append(t)
        y += 30
    return svg(W, y + 2, "".join(o))

def cols(items, unit="", hl=None, W=None, c=B1, fmt="{:,.0f}", H=210, notes=None):
    """Vertical columns. notes: [(index, annotation)] drawn as red callouts above the bar."""
    W = W or CURW[0]; hl = hl or []; maxv = max(v for _, v in items) * 1.35; n = len(items)
    x0 = 40; aw = W - 50; cwid = aw / n; o = []; base = H - 34
    for k in range(5):
        gy = base - (base - 18) * k / 4
        o.append(f'<line x1="{x0}" y1="{gy:.1f}" x2="{W - 6}" y2="{gy:.1f}" stroke="#dde3e7" stroke-width="0.8"/>')
        t, _ = T(x0 - 4, gy, fmt.format(maxv * k / 4), 8.8, 400, "end", GREY, valign="middle"); o.append(t)
    for i, (lab, v) in enumerate(items):
        h = (base - 18) * v / maxv; x = x0 + i * cwid + cwid * 0.18; col = RED if (lab in hl or i in hl) else c
        o.append(rect(x, base - h, cwid * 0.64, h, col, rx=0))
        t, _ = T(x + cwid * 0.32, base - h - 14, fmt.format(v) + unit, 10, 700, fill=col); o.append(t)
        t, _ = T(x + cwid * 0.32, base + 4, lab, 9.3, 400, fill=DG, width=cwid - 2); o.append(t)
    o.append(f'<line x1="{x0}" y1="{base}" x2="{W - 6}" y2="{base}" stroke="{INK}" stroke-width="1.2"/>')
    for (idx, txt) in (notes or []):
        x = x0 + idx * cwid + cwid * 0.5; v = items[idx][1]; yy = base - (base - 18) * v / maxv - 18
        tx = min(max(x, 80), W - 80)
        t, h = T(tx, 2, txt, 9.2, 600, fill=RED, width=150, italic=True); o.append(t)
        o.append(ln(tx, 4 + h, x, yy, RED, 1, "ar"))
    return svg(W, H + 12, "".join(o))

def linechart(series, xlabels, W=None, H=230, unit="", fmt="{:,.0f}", colors=None, ymin=None, notes=None):
    """notes: [(series name, x index, annotation)]"""
    W = W or CURW[0]; colors = colors or [B1, RED, TEAL, GOLD, MAUVE, GREY]
    allv = [v for s in series.values() for v in s if v is not None]
    mx = max(allv) * 1.15; mn = ymin if ymin is not None else min(0, min(allv))
    x0, x1, y0, y1 = 42, W - (110 if W > 500 else 64), 34 if notes else 14, H - 28; o = []
    for k in range(5):
        v = mn + (mx - mn) * k / 4; gy = y1 - (y1 - y0) * k / 4
        o.append(f'<line x1="{x0}" y1="{gy:.1f}" x2="{x1}" y2="{gy:.1f}" stroke="#dde3e7" stroke-width="0.8"/>')
        t, _ = T(x0 - 4, gy, fmt.format(v) + unit, 8.8, 400, "end", GREY, valign="middle"); o.append(t)
    n = len(xlabels); X = lambda i: x0 + (x1 - x0) * i / max(1, n - 1); Y = lambda v: y1 - (y1 - y0) * (v - mn) / (mx - mn)
    for i, l in enumerate(xlabels):
        t, _ = T(X(i), y1 + 5, l, 9, 400, fill=DG); o.append(t)
    for si, (name, vals) in enumerate(series.items()):
        c = colors[si % len(colors)]; pts = [(X(i), Y(v)) for i, v in enumerate(vals) if v is not None]
        o.append('<polyline fill="none" stroke="%s" stroke-width="2.4" points="%s"/>' % (c, " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)))
        t, _ = T(pts[-1][0] + 6, pts[-1][1], name, 10, 700, "start", c, (W - x1) - 8, valign="middle"); o.append(t)
    for (sname, i, txt) in (notes or []):
        v = series[sname][i]; px, py = X(i), Y(v); tx = min(max(px, 80), x1 - 80)
        t, h = T(tx, 0, txt, 9.2, 600, fill=RED, width=150, italic=True); o.append(t)
        o.append(ln(tx, h + 2, px, py - 5, RED, 0.9, "ar")); o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.5" fill="{RED}"/>')
    o.append(f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{INK}" stroke-width="1.2"/>')
    return svg(W, H, "".join(o))

def stack100(rows, W=None, colors=None, legend=True, note=None):
    W = W or CURW[0]; colors = colors or [B1, TEAL, GOLD, MAUVE, B2, GREY, OLIVE]; bh = 24; o = []; y = 4
    x0 = 130 if W > 500 else 80; aw = W - x0 - 8; segs = []
    for lab, parts in rows:
        tot = sum(v for _, v in parts); x = x0
        t, _ = T(x0 - 6, y + bh / 2, lab, 10.3, 600, "end", INK, x0 - 8, valign="middle"); o.append(t)
        for sname, v in parts:
            if sname not in segs: segs.append(sname)
            c = colors[segs.index(sname) % len(colors)]; w = aw * v / tot
            o.append(rect(x, y, w - 1, bh, c, rx=0))
            if w > 30: t, _ = T(x + w / 2, y + bh / 2, f"{v:g}%", 10, 700, fill="white", valign="middle"); o.append(t)
            x += w
        y += bh + 7
    if legend:
        lx = x0
        for j, s in enumerate(segs):
            if lx + 20 + len(s) * 5.3 > W: lx = x0; y += 15
            o.append(rect(lx, y + 3, 10, 10, colors[j % len(colors)], rx=0))
            t, _ = T(lx + 14, y + 8, s, 9.8, 400, "start", DG, valign="middle"); o.append(t); lx += 24 + len(s) * 5.3
        y += 18
    if note: t, h = T(4, y + 2, note, 9.6, 400, "start", DG, W - 8, italic=True); o.append(t); y += h + 4
    return svg(W, y + 2, "".join(o))

def waterfall(items, W=None, H=240, unit="", fmt="{:,.0f}", total="Result", takeaway=None):
    """items: [(label, value, explanation)]. Gains teal, costs red, result blue; notes under each bar."""
    W = W or CURW[0]; items = [tuple(i) + ("",) * (3 - len(i)) for i in items]
    run = 0; pts = []
    for lab, v, nt in items: pts.append((lab, run, run + v, nt)); run += v
    pts.append((total, 0, run, ""))
    vals = [p[1] for p in pts] + [p[2] for p in pts]; mx = max(vals) * 1.15; mn = min(0, min(vals)) * 1.15
    x0 = 6; aw = W - 12; n = len(pts); cwid = aw / n; y0 = 22; y1 = H - 20; o = []
    maxnote = max(nlines(p[0], cwid - 4, 9.3) * 11.2 + (nlines(p[3], cwid - 4, 8.7) * 10.5 + 3 if p[3] else 0) for p in pts)
    Y = lambda v: y1 - (y1 - y0) * (v - mn) / (mx - mn)
    o.append(f'<line x1="{x0}" y1="{Y(0):.1f}" x2="{W - 6}" y2="{Y(0):.1f}" stroke="{INK}" stroke-width="1.2"/>')
    for i, (lab, a, b, nt) in enumerate(pts):
        x = x0 + i * cwid + cwid * 0.15; last = i == n - 1; c = B1 if last else (TEAL if b >= a else RED)
        top, bot = Y(max(a, b)), Y(min(a, b)); o.append(rect(x, top, cwid * 0.7, max(bot - top, 1.5), c, rx=0))
        v = b - a if not last else b
        t, _ = T(x + cwid * 0.35, top - 15, ("+" if v > 0 and not last else "") + fmt.format(v) + unit, 10.3, 800, fill=c); o.append(t)
        t, th = T(x0 + i * cwid + cwid / 2, y1 + 6, lab, 9.3, 700, fill=INK, width=cwid - 4); o.append(t)
        if nt: t, _ = T(x0 + i * cwid + cwid / 2, y1 + 8 + th, nt, 8.7, 400, fill=DG, width=cwid - 4, italic=True); o.append(t)
        if not last:
            nxt = x0 + (i + 1) * cwid + cwid * 0.15
            o.append(f'<line x1="{x + cwid * 0.7:.1f}" y1="{Y(b):.1f}" x2="{nxt:.1f}" y2="{Y(b):.1f}" stroke="{GREY}" stroke-dasharray="3,2" stroke-width="0.9"/>')
    y = y1 + 10 + maxnote
    if takeaway:
        o.append(rect(4, y, W - 8, 3, RED, rx=0)); t, h = T(6, y + 7, takeaway, 10, 600, "start", INK, W - 12); o.append(t); y += h + 12
    return svg(W, y + 2, "".join(o))

# ------------------------------------------------------------ structures
def matrix(xlab, ylab, quads, points=None, xends=("Low", "High"), yends=("Low", "High"), W=None, hlq=None):
    """quads: [(title, description)] top-left, top-right, bottom-left, bottom-right; points: [(label, x, y)]"""
    W = W or CURW[0]; quads = [_norm(q) for q in quads]
    x0 = 40; x1 = W - 6; qw = (x1 - x0) / 2
    qh = max(cardh(qw - 4, t, d) for t, d, _ in quads) + (46 if points else 10)
    y0 = 8; y1 = y0 + qh * 2; o = []
    fills = [light(B1, 0.9), light(TEAL, 0.86), LG, light(GOLD, 0.85)]
    for i, (t, d, _) in enumerate(quads):
        qx = x0 + (i % 2) * qw; qy = y0 + (i // 2) * qh; f = light(RED, 0.86) if hlq == i else fills[i]
        o.append(rect(qx + 1.5, qy + 1.5, qw - 3, qh - 3, f, rx=2))
        s, th = T(qx + 9, qy + 8, t, 11, 800, "start", RED if hlq == i else NAVY, qw - 18); o.append(s)
        if d: s, _ = T(qx + 9, qy + 11 + th, d, 9.5, 400, "start", DG, qw - 18); o.append(s)
    o.append(ln(x0, y1, x1, y1, INK, 1.3, "ak")); o.append(ln(x0, y1, x0, y0 - 4, INK, 1.3, "ak"))
    t, _ = T((x0 + x1) / 2, y1 + 15, xlab, 10.5, 700); o.append(t)
    t, _ = T(x0 + 4, y1 + 3, xends[0], 9, 400, "start", GREY); o.append(t)
    t, _ = T(x1 - 8, y1 + 3, xends[1], 9, 400, "end", GREY); o.append(t)
    o.append(f'<text transform="translate(13,{(y0 + y1) / 2:.0f}) rotate(-90)" font-family="{F}" font-size="10.5" font-weight="700" text-anchor="middle">{esc(ylab)}</text>')
    o.append(f'<text transform="translate(31,{y1 - 3:.0f}) rotate(-90)" font-family="{F}" font-size="9" fill="{GREY}" text-anchor="start">{esc(yends[0])}</text>')
    o.append(f'<text transform="translate(31,{y0 + 3:.0f}) rotate(-90)" font-family="{F}" font-size="9" fill="{GREY}" text-anchor="end">{esc(yends[1])}</text>')
    for p in points or []:
        lab, px, py = p[:3]; c = p[3] if len(p) > 3 else RED
        cx = x0 + (x1 - x0) * px; cy = y1 - (y1 - y0) * py
        o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="5.5" fill="{c}" stroke="white" stroke-width="1.5"/>')
        anc = "start" if px < 0.72 else "end"; dx = 8 if px < 0.72 else -8
        s, _ = T(cx + dx, cy, lab, 9.6, 700, anc, c, 110, valign="middle"); o.append(s)
    return svg(W, y1 + 28, "".join(o))

def loop(nodes, center=None, center_desc=None, edges=None, W=None, c=B1, hl=None):
    """Reinforcing loop. nodes: [(title, description)]; edges: labels explaining each arrow (i → i+1)."""
    W = W or CURW[0]; nodes = [_norm(n) for n in nodes]; n = len(nodes); hl = hl or []
    if W < 500:
        its = []
        for i, (t, d, _) in enumerate(nodes):
            its.append((t, d, ("→ " + edges[i]) if edges and i < len(edges) and edges[i] else ""))
        return vsteps(its, hl, c, W) if not center else vsteps([(center, center_desc or "", "")] + its, [0] + [h + 1 for h in hl], c, W, numbered=True)
    bw = 172; hs = [cardh(bw, t, d, tsize=11, dsize=9.4) for t, d, _ in nodes]
    H = max(320, int(max(hs) * 2 + 170 + (40 if n > 4 else 0))); cx, cy = W / 2, H / 2
    Rx = (W - bw) / 2 - 6; Ry = H / 2 - max(hs) / 2 - 6; o = []
    ang = [-math.pi / 2 + 2 * math.pi * i / n for i in range(n)]
    pos = [(cx + Rx * math.cos(a), cy + Ry * math.sin(a)) for a in ang]
    for i in range(n):
        a1 = ang[i] + 2 * math.pi * 0.2 / n; a2 = ang[i] + 2 * math.pi * 0.8 / n; rx, ry = Rx * 0.8, Ry * 0.8
        p1 = (cx + rx * math.cos(a1), cy + ry * math.sin(a1)); p2 = (cx + rx * math.cos(a2), cy + ry * math.sin(a2))
        o.append(f'<path d="M{p1[0]:.1f},{p1[1]:.1f} A{rx:.1f},{ry:.1f} 0 0,1 {p2[0]:.1f},{p2[1]:.1f}" fill="none" stroke="{RED}" stroke-width="2" marker-end="url(#ar)"/>')
        if edges and i < len(edges) and edges[i]:
            am = (a1 + a2) / 2; ex, ey = cx + rx * 0.66 * math.cos(am), cy + ry * 0.66 * math.sin(am)
            s, _ = T(ex, ey, edges[i], 8.8, 600, fill=RED, width=96, italic=True, valign="middle"); o.append(s)
    for i, (x, y) in enumerate(pos):
        s, _ = card(x - bw / 2, y - hs[i] / 2, bw, nodes[i][0], nodes[i][1], c, None, i in hl, tsize=11, dsize=9.4); o.append(s)
    if center:
        s, h = T(cx, cy - 10, center, 13.5, 800, fill=RED, width=150, valign="middle"); o.append(s)
        if center_desc: s, _ = T(cx, cy - 10 + h / 2 + 3, center_desc, 9.2, 400, fill=DG, width=140, italic=True); o.append(s)
    return svg(W, H, "".join(o))

def layers(rows, W=None, colors=None, head=("Layer", "What it does", "Everyday example")):
    """rows: [(name, what it does, example)] — a stack, top row closest to the user."""
    W = W or CURW[0]; colors = colors or [B1, TEAL, GOLD, MAUVE, B2, OLIVE, SAND, GREY]; rows = [_norm(r) for r in rows]
    narrow = W < 500; lw = 92 if narrow else 140; ew = 0 if narrow else 190; dw = W - lw - ew - 12; o = []; y = 2
    if not narrow:
        for tx, xx in ((head[0], 6), (head[1], lw + 12), (head[2], lw + dw + 14)):
            t, _ = T(xx, y, tx, 9, 700, "start", GREY); o.append(t)
        y += 15
    for i, (name, d, ex) in enumerate(rows):
        c = colors[i % len(colors)]; body = d + ("\nE.g. " + ex if (narrow and ex) else "")
        h = max(nlines(name, lw - 12, 11) * 13.5, nlines(body, dw - 12, 9.7) * 11.7, (nlines(ex, ew - 12, 9.5) * 11.4 if ex and not narrow else 0)) + 14
        o.append(rect(4, y, lw, h, c, rx=2)); t, _ = T(4 + lw / 2, y + h / 2, name, 11, 800, fill="white", width=lw - 12, valign="middle"); o.append(t)
        o.append(rect(4 + lw + 2, y, dw + (ew if not narrow else 0) + 4, h, light(c, 0.88), rx=2))
        t, _ = T(lw + 12, y + 7, body, 9.7, 400, "start", INK, dw - 12); o.append(t)
        if ex and not narrow:
            o.append(f'<line x1="{lw + dw + 8:.1f}" y1="{y + 5}" x2="{lw + dw + 8:.1f}" y2="{y + h - 5}" stroke="white" stroke-width="2"/>')
            t, _ = T(lw + dw + 14, y + 7, ex, 9.5, 400, "start", DG, ew - 12, italic=True); o.append(t)
        y += h + 3
    return svg(W, y + 2, "".join(o))

def hub(center, spokes, center_desc=None, W=None, c=B1):
    """spokes: [(title, description)] around a central idea."""
    W = W or CURW[0]; spokes = [_norm(s) for s in spokes]; n = len(spokes)
    if W < 500: return cards([(t, d) for t, d, _ in spokes], 1, W, c, header=(center, center_desc))
    bw = 180; hs = [cardh(bw, t, d, tsize=11, dsize=9.4) for t, d, _ in spokes]
    H = max(330, int(max(hs) * 2.3 + 130)); cx, cy = W / 2, H / 2; Rx, Ry = W / 2 - bw / 2 - 6, H / 2 - max(hs) / 2 - 6; o = []
    for i in range(n):
        a = -math.pi / 2 + 2 * math.pi * i / n; x, y = cx + Rx * math.cos(a), cy + Ry * math.sin(a)
        o.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#c3ccd2" stroke-width="1.4"/>')
    for i, (t, d, _) in enumerate(spokes):
        a = -math.pi / 2 + 2 * math.pi * i / n; x, y = cx + Rx * math.cos(a), cy + Ry * math.sin(a)
        s, _ = card(x - bw / 2, y - hs[i] / 2, bw, t, d, c, None, tsize=11, dsize=9.4); o.append(s)
    o.append(f'<circle cx="{cx}" cy="{cy}" r="60" fill="{RED}"/>')
    s, h = T(cx, cy - (10 if center_desc else 0), center, 12.5, 800, fill="white", width=100, valign="middle"); o.append(s)
    if center_desc: s, _ = T(cx, cy + h / 2 - 5, center_desc, 8.6, 400, fill="white", width=96, italic=True); o.append(s)
    return svg(W, H, "".join(o))

def versus(lt, litems, rt, ritems, W=None, lc=GREY, rc=B1, verdict=None):
    """Two contrasting columns. Items: 'text' or (title, text). verdict: one-line conclusion under both."""
    W = W or CURW[0]; narrow = W < 500; o = []; cwid = (W - 12) if narrow else (W - 22) / 2
    def col(x, y, title, items, c):
        out = [rect(x, y, cwid, 26, c, rx=2)]; t, _ = T(x + cwid / 2, y + 13, title, 11.2, 800, fill="white", width=cwid - 10, valign="middle"); out.append(t)
        y += 30
        for it in items:
            tt, dd = (None, it) if isinstance(it, str) else it
            th = nlines(tt, cwid - 26, 10.3) * 12.4 if tt else 0; dh = nlines(dd, cwid - 26, 9.8) * 11.8; h = th + dh + 12
            out.append(rect(x, y, cwid, h, light(c, 0.88), rx=2)); out.append(f'<circle cx="{x + 10}" cy="{y + 11}" r="3.2" fill="{c}"/>')
            if tt: s, _ = T(x + 20, y + 5, tt, 10.3, 700, "start", INK, cwid - 26); out.append(s)
            s, _ = T(x + 20, y + 5 + th, dd, 9.8, 400, "start", DG, cwid - 26); out.append(s)
            y += h + 4
        return out, y
    a, ya = col(6, 2, lt, litems, lc)
    if narrow: b, yb = col(6, ya + 8, rt, ritems, rc); y = yb
    else: b, yb = col(16 + cwid, 2, rt, ritems, rc); y = max(ya, yb)
    o = a + b
    if verdict: o.append(rect(6, y + 4, W - 12, 3, RED, rx=0)); s, h = T(8, y + 11, verdict, 10.2, 600, "start", INK, W - 16); o.append(s); y += h + 16
    return svg(W, y + 4, "".join(o))

def cards(items, ncol=3, W=None, c=B1, header=None, numbered=False):
    """items: [(title, description, optional colour)]"""
    W = W or CURW[0]
    if W < 500: ncol = 1 if (ncol > 2 or W < 300) else ncol
    gw = (W - 8 * (ncol + 1)) / ncol; o = []; y = 4
    if header:
        hh = 30 if not header[1] else 30 + nlines(header[1], W - 20, 9.4) * 11.3
        o.append(rect(4, y, W - 8, hh, RED, rx=2)); s, h = T(W / 2, y + 7, header[0], 12, 800, fill="white", width=W - 20); o.append(s)
        if header[1]: s, _ = T(W / 2, y + 9 + h, header[1], 9.4, 400, fill="white", width=W - 20, italic=True); o.append(s)
        y += hh + 8
    k = 0
    for r in range(0, len(items), ncol):
        row = items[r:r + ncol]; rh = max(cardh(gw, it[0], it[1] if len(it) > 1 else "", (r + j + 1) if numbered else None) for j, it in enumerate(row))
        for j, it in enumerate(row):
            k += 1; col = it[2] if len(it) > 2 else c
            s, _ = card(8 + j * (gw + 8), y, gw, it[0], it[1] if len(it) > 1 else "", col, k if numbered else None, minh=rh); o.append(s)
        y += rh + 8
    return svg(W, y, "".join(o))

def pyramid(levels, W=None, colors=None):
    """levels top→bottom: [(title, description)]"""
    W = W or CURW[0]; levels = [_norm(l) for l in levels]; colors = colors or [RED, B1, TEAL, GOLD, MAUVE, GREY]
    pw = 210 if W > 500 else 110; o = []; y = 4
    hs = [max(36, nlines(d, W - pw - 30, 9.7) * 11.7 + nlines(t, W - pw - 30, 11) * 13.2 + 12) for t, d, _ in levels]
    tot = sum(hs); cx = pw / 2 + 4
    for i, (t, d, _) in enumerate(levels):
        wt = pw * (0.16 + 0.84 * sum(hs[:i]) / tot); wb = pw * (0.16 + 0.84 * sum(hs[:i + 1]) / tot); h = hs[i]
        o.append(f'<polygon points="{cx - wt / 2:.1f},{y} {cx + wt / 2:.1f},{y} {cx + wb / 2:.1f},{y + h - 3} {cx - wb / 2:.1f},{y + h - 3}" fill="{colors[i % len(colors)]}"/>')
        s, _ = T(cx, y + h / 2 - 1, str(i + 1), 13, 800, fill="white", valign="middle"); o.append(s)
        o.append(f'<line x1="{cx + wb / 2 + 3:.1f}" y1="{y + h / 2}" x2="{pw + 12}" y2="{y + h / 2}" stroke="#c3ccd2" stroke-dasharray="2,2"/>')
        s, th = T(pw + 16, y + 3, t, 11, 800, "start", colors[i % len(colors)], W - pw - 22); o.append(s)
        s, _ = T(pw + 16, y + 5 + th, d, 9.7, 400, "start", DG, W - pw - 22); o.append(s)
        y += h
    return svg(W, y + 4, "".join(o))

def timeline(events, W=None, c=B1):
    """events: [(date, title, description)] — vertical when narrow or long."""
    W = W or CURW[0]; events = [tuple(e) + ("",) * (3 - len(e)) for e in events]
    if W < 500 or len(events) > 6:
        o = []; y = 4; lx = 64
        for i, (dt, t, d) in enumerate(events):
            s, th = T(lx + 10, y, t, 10.8, 700, "start", INK, W - lx - 14); o.append(s)
            dh = 0
            if d: s, dh = T(lx + 10, y + th + 1, d, 9.5, 400, "start", DG, W - lx - 14); o.append(s)
            s, _ = T(lx - 8, y, dt, 10.3, 800, "end", RED, lx - 8); o.append(s)
            o.append(f'<circle cx="{lx}" cy="{y + 7}" r="4" fill="{RED}"/>'); h = th + dh + 10
            if i < len(events) - 1: o.insert(0, f'<line x1="{lx}" y1="{y + 7}" x2="{lx}" y2="{y + h + 7}" stroke="#c3ccd2" stroke-width="2"/>')
            y += h
        return svg(W, y + 2, "".join(o))
    n = len(events); gw = (W - 8) / n; o = [f'<line x1="4" y1="30" x2="{W - 4}" y2="30" stroke="{INK}" stroke-width="2"/>']; mh = 0
    for i, (dt, t, d) in enumerate(events):
        x = 4 + gw * i + gw / 2
        o.append(f'<circle cx="{x:.1f}" cy="30" r="5.5" fill="{RED}" stroke="white" stroke-width="1.5"/>')
        s, _ = T(x, 4, dt, 11, 800, fill=RED); o.append(s)
        s, th = T(x, 42, t, 10.5, 700, fill=INK, width=gw - 10); o.append(s)
        dh = 0
        if d: s, dh = T(x, 44 + th, d, 9.2, 400, fill=DG, width=gw - 10); o.append(s)
        mh = max(mh, th + dh)
    return svg(W, 52 + mh, "".join(o))

def seq(actors, msgs, W=None):
    """Sequence diagram. msgs: [(from, to, label, optional note)]"""
    W = W or CURW[0]; n = len(actors); gap = (W - 12) / n; xs = [6 + gap * (i + 0.5) for i in range(n)]; o = []
    y = 44; rows = []
    for m in msgs:
        a, b = actors.index(m[0]), actors.index(m[1]); lab = m[2]; nt = m[3] if len(m) > 3 else ""
        lw = max(abs(xs[b] - xs[a]) - 8, 80); lh = nlines(f"00. {lab}", lw, 9.5) * 11.4
        yy = y + lh + 2; nh = nlines(nt, max(lw, 150), 9) * 10.8 + 2 if nt else 0
        rows.append((a, b, lab, nt, yy, lw)); y = yy + nh + 12
    H = y + 4
    for i, a in enumerate(actors):
        o.append(rect(xs[i] - gap * 0.45, 4, gap * 0.9, 30, NAVY if i % 2 else B1, rx=3))
        s, _ = T(xs[i], 19, a, 10.2, 700, fill="white", width=gap * 0.86, valign="middle"); o.append(s)
        o.append(f'<line x1="{xs[i]:.1f}" y1="34" x2="{xs[i]:.1f}" y2="{H}" stroke="#b9c3ca" stroke-dasharray="4,3"/>')
    for k, (a, b, lab, nt, yy, lw) in enumerate(rows):
        o.append(ln(xs[a], yy, xs[b] + (-3 if b > a else 3), yy, B1, 1.5, "ab"))
        s, _ = T((xs[a] + xs[b]) / 2, yy - 3, f"{k + 1}. {lab}", 9.5, 600, fill=INK, width=lw, valign="bottom"); o.append(s)
        if nt: s, _ = T((xs[a] + xs[b]) / 2, yy + 3, nt, 9, 400, fill=RED, width=max(lw, 150), italic=True); o.append(s)
    return svg(W, H, "".join(o))

def analogy(rows, lt="Everyday world", rt="In technology", W=None):
    """rows: [(everyday thing, tech concept, what it means)]"""
    W = W or CURW[0]; rows = [_norm(r) for r in rows]; narrow = W < 500; o = []; y = 2
    if narrow:
        for a, b, d in rows:
            h1 = nlines(a, W - 20, 10) * 12; txt = b + (": " + d if d else ""); h2 = nlines(txt, W - 20, 9.7) * 11.7
            o.append(rect(4, y, W - 8, h1 + 8, light(GOLD, 0.78), rx=2)); s, _ = T(10, y + 4, a, 10, 700, "start", INK, W - 20); o.append(s)
            y += h1 + 8; o.append(rect(4, y, W - 8, h2 + 10, light(B1, 0.88), rx=2))
            s, _ = T(10, y + 5, txt, 9.7, 400, "start", INK, W - 20); o.append(s); y += h2 + 16
        return svg(W, y, "".join(o))
    lw = 225; rw = W - lw - 50
    for tx, xx, ww, bg, fg in ((lt, 4, lw, GOLD, "#222"), (rt, lw + 46, rw, B1, "white")):
        o.append(rect(xx, y, ww, 22, bg, rx=2)); s, _ = T(xx + 8, y + 11, tx, 10.5, 800, "start", fg, valign="middle"); o.append(s)
    y += 28
    for a, b, d in rows:
        h = max(nlines(a, lw - 16, 10.2) * 12.3, nlines(b, rw - 16, 10.5) * 12.6 + (nlines(d, rw - 16, 9.5) * 11.4 + 2 if d else 0)) + 12
        o.append(rect(4, y, lw, h, light(GOLD, 0.8), rx=2)); s, _ = T(12, y + 6, a, 10.2, 400, "start", INK, lw - 16); o.append(s)
        o.append(ln(lw + 8, y + h / 2, lw + 40, y + h / 2, RED, 1.8, "ar"))
        o.append(rect(lw + 46, y, rw, h, light(B1, 0.88), rx=2)); s, th = T(lw + 54, y + 6, b, 10.5, 700, "start", NAVY, rw - 16); o.append(s)
        if d: s, _ = T(lw + 54, y + 8 + th, d, 9.5, 400, "start", DG, rw - 16); o.append(s)
        y += h + 5
    return svg(W, y, "".join(o))

def formula(terms, result=None, ops=None, W=None, c=B1):
    """result = term × term …; terms: [(name, description, example value)]"""
    W = W or CURW[0]; terms = [_norm(t) for t in terms]; n = len(terms); o = []; y = 4
    if result:
        hh = nlines(result, W - 20, 12) * 14.4 + 12
        o.append(rect(4, y, W - 8, hh, RED, rx=3)); s, _ = T(W / 2, y + hh / 2, result, 12, 800, fill="white", width=W - 20, valign="middle"); o.append(s); y += hh + 8
    per = n if (W > 500 and n <= 5) else (2 if W < 500 else 3); gap = 20; gw = (W - 8 - gap * (per - 1)) / per; idx = 0
    for r in range(0, n, per):
        row = terms[r:r + per]; rh = max(cardh(gw, t, d) + (20 if e else 0) for t, d, e in row)
        for j, (t, d, e) in enumerate(row):
            x = 4 + j * (gw + gap); s, _ = card(x, y, gw, t, d, c, minh=rh); o.append(s)
            if e: o.append(rect(x, y + rh - 19, gw, 19, light(c, 0.78), rx=0)); s, _ = T(x + gw / 2, y + rh - 9.5, e, 10, 800, fill=NAVY, valign="middle"); o.append(s)
            if r + j < n - 1:
                op = ops[r + j] if ops and r + j < len(ops) else "×"
                if j < len(row) - 1: s, _ = T(x + gw + gap / 2, y + rh / 2, op, 17, 800, fill=RED, valign="middle"); o.append(s)
                else: s, _ = T(W - 6, y + rh + 1, op, 14, 800, "end", RED); o.append(s)
        y += rh + 12
    return svg(W, y, "".join(o))

def scale(left, right, marks, W=None, lnote="", rnote=""):
    """Trade-off spectrum. marks: [(label, position 0-1, note)]"""
    W = W or CURW[0]; marks = [tuple(m) + ("",) * (3 - len(m)) for m in marks]; o = []
    x0, x1 = 8, W - 8
    o.append(f'<defs><linearGradient id="gsc" x1="0" x2="1"><stop offset="0" stop-color="{B1}"/><stop offset="1" stop-color="{RED}"/></linearGradient></defs>')
    s, h1 = T(x0, 2, left, 10.8, 800, "start", B1, (x1 - x0) * 0.46); o.append(s)
    s, h2 = T(x1, 2, right, 10.8, 800, "end", RED, (x1 - x0) * 0.46); o.append(s)
    y = max(h1, h2) + 8; o.append(rect(x0, y, x1 - x0, 9, "url(#gsc)", rx=4.5)); maxh = 0
    ordered = sorted(enumerate(marks), key=lambda z: z[1][1]); tiers = []  # list of lists of (x0,x1)
    tw = min(150, max(90, (x1 - x0) / max(2, len(marks)) * 1.1)); th_est = 40
    for i, (lab, p, nt) in ordered:
        x = x0 + (x1 - x0) * p; xa = min(max(x, x0 + tw / 2), x1 - tw / 2)
        k = 0
        while k < len(tiers) and any(not (xa + tw / 2 + 4 < a or xa - tw / 2 - 4 > b) for a, b in tiers[k]): k += 1
        if k == len(tiers): tiers.append([])
        tiers[k].append((xa - tw / 2, xa + tw / 2)); base = y + 22 + k * th_est
        o.append(f'<polygon points="{x - 6:.1f},{y + 20} {x + 6:.1f},{y + 20} {x:.1f},{y + 11}" fill="{INK}"/>')
        if k: o.append(f'<line x1="{x:.1f}" y1="{y + 20}" x2="{xa:.1f}" y2="{base - 1:.1f}" stroke="{GREY}" stroke-width="0.7"/>')
        s_, th = T(xa, base, lab, 10, 800, fill=INK, width=tw); o.append(s_)
        nh = 0
        if nt: s_, nh = T(xa, base + th + 1, nt, 9, 400, fill=DG, width=tw, italic=True); o.append(s_)
        maxh = max(maxh, k * th_est + th + nh)
    y = y + 26 + maxh
    if lnote or rnote:
        s, a = T(x0, y + 4, lnote, 9.3, 400, "start", B1, (x1 - x0) * 0.47, italic=True); o.append(s)
        s, b = T(x1, y + 4, rnote, 9.3, 400, "end", RED, (x1 - x0) * 0.47, italic=True); o.append(s); y += max(a, b) + 6
    return svg(W, y + 4, "".join(o))

def phone(blocks, callouts, W=None):
    """Annotated app screen. blocks: [(label, relative height, optional colour)] top→bottom.
    callouts: [(block index, heading, explanation)] with numbered leader lines (alternating sides)."""
    W = W or CURW[0]; narrow = W < 500; pw = 150 if not narrow else 112; ph = 310 if not narrow else 250
    px = (W - pw) / 2 if not narrow else 6; py = 8; o = []
    o.append(rect(px - 6, py - 6, pw + 12, ph + 26, "#1d2327", rx=16)); o.append(rect(px, py + 8, pw, ph, "white", rx=4))
    o.append(rect(px + pw / 2 - 18, py - 1, 36, 4, "#3a4248", rx=2))
    tot = sum(b[1] for b in blocks); y = py + 10; mids = []
    pal = [light(B1, 0.8), light(TEAL, 0.78), LG, light(GOLD, 0.72), light(MAUVE, 0.8), light(B2, 0.7)]
    for i, b in enumerate(blocks):
        lab, hh = b[0], b[1]; col = b[2] if len(b) > 2 else pal[i % len(pal)]
        h = (ph - 4 - 2 * len(blocks)) * hh / tot
        o.append(rect(px + 3, y, pw - 6, h, col, rx=2)); s, _ = T(px + pw / 2, y + h / 2, lab, 8.5, 600, fill=DG, width=pw - 12, valign="middle"); o.append(s)
        mids.append(y + h / 2); y += h + 2
    if narrow:
        cx0 = px + pw + 22; cwid = W - cx0 - 4; yy = py
        for k, (bi, hd, ex) in enumerate(callouts):
            th = nlines(hd, cwid - 14, 10) * 12 + nlines(ex, cwid - 6, 9) * 10.8 + 8
            o.append(f'<path d="M{px + pw - 4:.1f},{mids[bi]:.1f} L{cx0 - 12:.1f},{yy + 8:.1f}" stroke="{RED}" stroke-width="0.9" fill="none"/>')
            o.append(badge(cx0 - 4, yy + 8, k + 1, RED, 7))
            s, h = T(cx0 + 8, yy + 1, hd, 10, 800, "start", INK, cwid - 12); o.append(s)
            s, _ = T(cx0 + 8, yy + 2 + h, ex, 9, 400, "start", DG, cwid - 12); o.append(s); yy += th + 4
        return svg(W, max(ph + 30, yy + 4), "".join(o))
    cwid = px - 30; out_h = ph + 30
    groups = [[(k, c) for k, c in enumerate(callouts) if k % 2 == 0], [(k, c) for k, c in enumerate(callouts) if k % 2 == 1]]
    for sidei, group in enumerate(groups):
        slots = []; yy = 0
        for k, (bi, hd, ex) in group:
            th = max(nlines(hd, cwid - 22, 10.4) * 12.5, 16) + nlines(ex, cwid - 6, 9.3) * 11.2 + 10
            slots.append((yy, th)); yy += th + 6
        off = max(py, (ph - yy) / 2 + py); out_h = max(out_h, yy + off + 6)
        for (k, (bi, hd, ex)), (ty, th) in zip(group, slots):
            ty += off
            if sidei == 0: tx = 2; ax = px + 6; bx = tx + cwid + 6
            else: tx = px + pw + 26; ax = px + pw - 6; bx = tx - 6
            o.append(f'<path d="M{ax:.1f},{mids[bi]:.1f} L{bx:.1f},{ty + 9:.1f}" stroke="{RED}" stroke-width="0.9" fill="none"/>')
            o.append(f'<circle cx="{ax:.1f}" cy="{mids[bi]:.1f}" r="2.6" fill="{RED}"/>')
            o.append(badge(tx + 8, ty + 9, k + 1, RED, 8))
            s, h = T(tx + 20, ty + 2, hd, 10.4, 800, "start", INK, cwid - 22); o.append(s)
            s, _ = T(tx + 2, ty + 4 + max(h, 16), ex, 9.3, 400, "start", DG, cwid - 6); o.append(s)
    return svg(W, out_h, "".join(o))

# ------------------------------------------------------------ graphviz (architecture, trees)
def _gvcolor(tag):
    return {"R": (RED, "white"), "L": ("white", NAVY), "T": (TEAL, "white"), "G": (GOLD, "#222222"), "Y": (GREY, "white"),
            "C": (light(B2, 0.55), "#0c2a3a"), "N": (NAVY, "white"), "B": (B1, "white"), "M": (MAUVE, "white")}.get(tag, (B1, "white"))

def gv(dot, rankdir="LR", W=None, nodesep=0.3, ranksep=0.5):
    src = f'''digraph G {{ rankdir={rankdir}; bgcolor="transparent"; nodesep={nodesep}; ranksep={ranksep}; pad=0.06; compound=true;
    node [shape=box style="rounded,filled" fillcolor="{B1}" color="{B1}" fontcolor="white" fontname="Source Sans 3" fontsize=11 margin="0.14,0.07"];
    edge [color="{GREY}" fontname="Source Sans 3" fontsize=9.5 fontcolor="#34424c" arrowsize=0.7 penwidth=1.2];
    {dot} }}'''
    for tag in "RLTGYCNBM":
        bg, fg = _gvcolor(tag); src = src.replace(f"[{tag}]", f'[fillcolor="{bg}" color="{NAVY if tag == "L" else bg}" fontcolor="{fg}"]')
    out = subprocess.run(["dot", "-Tsvg"], input=src.encode(), capture_output=True)
    if out.returncode != 0: raise RuntimeError(out.stderr.decode()[:800])
    s = out.stdout.decode(); s = s[s.find("<svg"):]
    m = re.search(r'width="([\d.]+)pt" height="([\d.]+)pt"', s); w, h = float(m.group(1)), float(m.group(2))
    maxpt = 533 if (W or CURW[0]) >= 600 else 262
    wpt = min(w * 0.85, maxpt)
    if wpt / w < 0.62: print(f"  [gv warning] graph shrunk to {wpt / w:.2f} — consider TB layout", flush=True)
    s = re.sub(r'width="[\d.]+pt" height="[\d.]+pt"', f'width="{wpt:.0f}pt" height="{wpt * h / w:.0f}pt"', s, count=1)
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r'font-family="Source Sans 3[^"]*"', f'font-family="{F}"', s)
    s = s.replace('<polygon fill="white" stroke="transparent"', '<polygon fill="none" stroke="none"')
    return s

def arch(nodes, edges, clusters=None, rankdir="LR", W=None, nodesep=0.3, ranksep=0.5, wrapch=24):
    """Descriptive architecture graph. nodes: {id: (title, description, tag)} tags: B blue, N navy, R red, T teal, G gold,
    C light, L outline, Y grey, M mauve. edges: [(a, b, label, style)] style 'd' dashed, 'r' red. clusters: {label: [ids]}."""
    W = W or CURW[0]
    def lab(t, d, fg):
        tt = "<BR/>".join(esc(x) for x in wrap(t, wrapch)); dd = "<BR/>".join(esc(x) for x in wrap(d, wrapch + 4)) if d else ""
        return f'<<FONT POINT-SIZE="11.5" COLOR="{fg}"><B>{tt}</B></FONT>' + (f'<BR/><FONT POINT-SIZE="9.3" COLOR="{fg}">{dd}</FONT>' if dd else "") + ">"
    L = []; inclu = set(i for ids in (clusters or {}).values() for i in ids)
    def nodeline(i):
        v = nodes[i]; t = v[0]; d = v[1] if len(v) > 1 else ""; tag = v[2] if len(v) > 2 else "B"
        bg, fg = _gvcolor(tag); border = NAVY if tag == "L" else bg
        return f'{i} [label={lab(t, d, fg)} fillcolor="{bg}" color="{border}"];'
    for ci, (cl, ids) in enumerate((clusters or {}).items()):
        L.append(f'subgraph cluster_{ci} {{ label=<<B>{esc(cl)}</B>>; fontname="Source Sans 3"; fontsize=10.5; fontcolor="{GREY}"; style="dashed,rounded"; color="#9fb0ba"; margin=10;')
        for i in ids: L.append(nodeline(i))
        L.append("}")
    for i in nodes:
        if i not in inclu: L.append(nodeline(i))
    for e in edges:
        a, b = e[0], e[1]; lb = e[2] if len(e) > 2 else ""; sty = e[3] if len(e) > 3 else ""
        extra = ' style="dashed"' if sty == "d" else (f' color="{RED}" fontcolor="{RED}" penwidth=1.7' if sty == "r" else "")
        lbl = "\\n".join(wrap(lb, 22)).replace('"', "'")
        L.append(f'{a} -> {b} [label="{lbl}"{extra}];')
    return gv("\n".join(L), rankdir, W, nodesep, ranksep)

def tree(spec, rankdir="TB", W=None, wrapch=20, **kw):
    """spec: ["Title|description", [children]]; prefix '!' marks the likely culprit in red."""
    nodes = {}; edges = []; cnt = [0]
    def walk(node, parent=None, depth=0):
        lab, kids = (node, []) if isinstance(node, str) else (node[0], node[1] if len(node) > 1 else [])
        cnt[0] += 1; nid = f"n{cnt[0]}"; hl = lab.startswith("!"); lab = lab.lstrip("!")
        t, d = (lab.split("|", 1) + [""])[:2]
        tag = "R" if hl else ("N" if depth == 0 else ("B" if depth == 1 else ("C" if depth == 2 else "L")))
        nodes[nid] = (t.strip(), d.strip(), tag)
        if parent: edges.append((parent, nid, ""))
        for k in kids: walk(k, nid, depth + 1)
    walk(spec)
    return arch(nodes, edges, None, rankdir, W, wrapch=wrapch, **kw)
