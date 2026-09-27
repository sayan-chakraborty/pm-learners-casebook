"""Generated SVGs for F2 (helpers copied from M8) ({{SVG:name}} in parts): move strips, waterfalls, bar charts, teardown sequence flows."""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "common"))
from svgkit import seq as _seq  # noqa: E402
from html import escape as _E

def seq(*a, **k):
    k.setdefault("row", 24)
    return _seq(*a, **k)

FIGS = {}

def svg(h, body, w=680):
    return f'<svg class="d" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">' + "".join(body) + "</svg>"

def T(x, y, s, cls="", anchor="start", size=None, fill=None):
    st = []
    if size: st.append(f"font-size:{size}px")
    if fill: st.append(f"fill:{fill}")
    sa = f' style="{";".join(st)}"' if st else ""
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}"{sa}>{_E(s)}</text>'

def lines(x, y, s, cls="", anchor="middle", lh=13, size=None):
    return "".join(T(x, y + i * lh, t, cls, anchor, size) for i, t in enumerate(s.split("|")))

# ---------- move strip (stronger answers) ----------
STRIP_COLS = ["#127a64", "#1d8a73", "#2a9a82", "#0b5d7a", "#3e4fb8", "#7c3aa6", "#8a4fb0"]
def strip(moves):
    n = len(moves); w = (680 - 10) / n
    o = ['<g class="c">']
    for i, (a, b) in enumerate(moves):
        x0 = i * w; x1 = x0 + w + (10 if i < n - 1 else 0)
        tip = 10 if i < n - 1 else 0
        pts = f"{x0:.1f},4 {x0 + w:.1f},4 {x0 + w + tip:.1f},31 {x0 + w:.1f},58 {x0:.1f},58" + (f" {x0 + 10:.1f},31" if i else "")
        if i == n - 1: pts = f"{x0:.1f},4 680,4 680,58 {x0:.1f},58 {x0 + 10:.1f},31"
        o.append(f'<polygon points="{pts}" fill="{STRIP_COLS[i % len(STRIP_COLS)]}"/>')
        cx = x0 + w / 2 + (5 if i else 0)
        o.append(T(cx, 26, f"{'①②③④⑤⑥⑦⑧'[i]} {a}", "b w", "middle"))
        o.append(T(cx, 44, b, "w", "middle"))
    o.append("</g>")
    return svg(62, o)


# ---------- waterfall ----------
def waterfall(items, h=220, top=26, scale=None, unit="₹", label_w=0, note=None, upcol="#127a64", totcol="#127a64", vw=680, suffix=""):
    """items: (label, value, kind) kind: 'start' | 'up' | 'down' | 'total'. Bars left to right."""
    n = len(items); left = 4; right = vw - 2; bw = (right - left) / n
    vals = []; run = 0; hi = 0
    for lab, v, k in items:
        if k == "start": a, b = 0, v; run = v
        elif k == "total": a, b = 0, run
        elif k == "up": a, b = run, run + v; run += v
        else: a, b = run - v, run; run -= v
        vals.append((a, b)); hi = max(hi, a, b)
    base = h - 44; sc = scale or (base - top - 18) / hi
    Y = lambda v: base - v * sc
    o = [f'<line x1="{left}" y1="{base}" x2="{right}" y2="{base}" stroke="#4a5563"/>']
    for i, ((lab, v, k), (a, b)) in enumerate(zip(items, vals)):
        x = left + i * bw + 4; w = bw - 8
        col = {"start": "#0b5d7a", "total": totcol, "up": upcol, "down": "#b93a32"}[k]
        if k == "total" and b < 0: col = "#b93a32"
        y0, y1 = sorted((Y(a), Y(b)))
        o.append(f'<rect x="{x:.1f}" y="{y0:.1f}" width="{w:.1f}" height="{max(y1 - y0, 1.5):.1f}" fill="{col}" rx="2"/>')
        sign = "−" if k == "down" else ("+" if k == "up" else "")
        o.append(T(x + w / 2, y0 - 4, f"{sign}{unit}{abs(v) if k != 'total' else b:,}{suffix}", "b", "middle"))
        o.append(lines(x + w / 2, base + 14, lab, "s", "middle", 12))
        if i < n - 1 and k != "total":
            end = Y(b if k in ("start", "up") else a)
            o.append(f'<line x1="{x + w:.1f}" y1="{end:.1f}" x2="{x + bw:.1f}" y2="{end:.1f}" stroke="#9aa3ad" stroke-dasharray="2 2"/>')
    if note: o.append(lines(left, 12, note, "s", "start", 12))
    return svg(h, o, vw)


# ---------- horizontal bar chart ----------
def hbars(rows, maxv, h=None, lw=150, unit="", fmt="{:,}", colors=None, note=None, vw=680):
    """rows: (label, value, annotation)"""
    rh = 24; top = 18 if note else 4; h = h or top + rh * len(rows) + 6
    x0 = lw; W = vw - lw - 290
    o = []
    if note: o.append(T(0, 12, note, "s"))
    for i, (lab, v, ann) in enumerate(rows):
        y = top + i * rh
        col = (colors or ["#0b5d7a"])[i % len(colors or ["#0b5d7a"])]
        o.append(T(x0 - 6, y + 15, lab, "b", "end"))
        w = max(2, W * v / maxv)
        o.append(f'<rect x="{x0}" y="{y + 4}" width="{w:.1f}" height="15" fill="{col}" rx="2"/>')
        o.append(T(x0 + w + 5, y + 15, (fmt.format(v) + unit) + ("   " + ann if ann else ""), "s"))
    return svg(h, o, vw)

# ---------- teardown sequence flows ----------






# ---------- loop (flywheel) ----------
def loop(nodes, centre, cx=340, cy=118, rx=250, ry=86, bw=150, bh=40, h=240, side=None, colors=None):
    """nodes: list of 'line1|line2' placed clockwise from the top; arrows between consecutive nodes."""
    n = len(nodes); o = ['<defs><marker id="lpa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#0b5d7a"/></marker></defs>']
    pts = [(cx + rx * math.sin(2 * math.pi * i / n), cy - ry * math.cos(2 * math.pi * i / n)) for i in range(n)]
    for i in range(n):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % n]
        a1 = 2 * math.pi * (i + 0.28) / n; a2 = 2 * math.pi * (i + 0.72) / n
        sx, sy = cx + rx * math.sin(a1), cy - ry * math.cos(a1); ex, ey = cx + rx * math.sin(a2), cy - ry * math.cos(a2)
        o.append(f'<path d="M{sx:.1f},{sy:.1f} A{rx},{ry} 0 0 1 {ex:.1f},{ey:.1f}" fill="none" stroke="#0b5d7a" stroke-width="2" marker-end="url(#lpa)"/>')
    for i, ((x, y), lab) in enumerate(zip(pts, nodes)):
        col = (colors or {}).get(i, ("#e3f0f5", "#0b5d7a"))
        o.append(f'<rect x="{x - bw/2:.1f}" y="{y - bh/2:.1f}" width="{bw}" height="{bh}" rx="6" fill="{col[0]}" stroke="{col[1]}" stroke-width="1.3"/>')
        ls = lab.split("|"); y0 = y - (len(ls) - 1) * 6.5 + 4
        for j, l in enumerate(ls): o.append(T(x, y0 + j * 13, l, "b" if j == 0 else "s", "middle"))
    for j, l in enumerate(centre.split("|")): o.append(T(cx, cy - (centre.count("|")) * 7 + 4 + j * 14, l, "b acc" if j == 0 else "s", "middle"))
    if side: o.append(lines(4, h - 26, side, "s", "start", 13))
    return svg(h, o)


# ---------- positioning 2x2 ----------
def two_by_two(xlab, ylab, quads, points, h=300):
    L, R, Tp, B = 70, 670, 14, h - 34
    mx, my = (L + R) / 2, (Tp + B) / 2
    o = [f'<rect x="{L}" y="{Tp}" width="{R-L}" height="{B-Tp}" fill="#fafbfc" stroke="#c3cad2"/>',
         f'<line x1="{mx}" y1="{Tp}" x2="{mx}" y2="{B}" stroke="#c3cad2"/><line x1="{L}" y1="{my}" x2="{R}" y2="{my}" stroke="#c3cad2"/>']
    for (qx, qy), txt in zip([(L + 8, Tp + 16), (mx + 8, Tp + 16), (L + 8, my + 16), (mx + 8, my + 16)], quads):
        o.append(T(qx, qy, txt, "s i"))
    for name, x, y, col, anchor in points:
        px, py = L + x * (R - L), B - y * (B - Tp)
        o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="6" fill="{col}"/>')
        o.append(T(px + (10 if anchor == "start" else -10), py + 4, name, "b halo", anchor))
    o.append(T((L + R) / 2, h - 12, xlab, "b", "middle"))
    o.append(f'<text x="18" y="{my:.1f}" text-anchor="middle" class="b" transform="rotate(-90 18 {my:.1f})">{_E(ylab)}</text>')
    o.append(T(L, h - 12, "low", "s")); o.append(T(R, h - 12, "high", "s", "end"))
    return svg(h, o)




def stacks(rows, segs, cols, total_max, title=None, lw=120, h=None, unit=" min", notes=()):
    """horizontal stacked bars. rows: (label, [values], total label); segs: segment names (legend)."""
    top = 34 if title else 26; rh = 38; h = h or top + rh * len(rows) + 30 + 14 * len(notes)
    W = 680 - lw - 70
    o = []
    if title: o.append(T(0, 12, title, "b"))
    lx = lw
    for s, c in zip(segs, cols):
        o.append(f'<rect x="{lx}" y="{top - 20}" width="10" height="10" fill="{c}"/>'); o.append(T(lx + 14, top - 11, s, "s"))
        lx += 16 + len(s) * 5.6 + 14
    for i, (lab, vals, tl) in enumerate(rows):
        y = top + i * rh
        o.append(lines(lw - 8, y + 16, lab, "b", "end", 12))
        x = lw
        for v, c in zip(vals, cols):
            w = W * v / total_max
            o.append(f'<rect x="{x:.1f}" y="{y + 4}" width="{w:.1f}" height="24" fill="{c}" stroke="#fff"/>')
            if w > 26: o.append(T(x + w / 2, y + 20, f"{v:g}", "b w", "middle"))
            x += w
        o.append(T(x + 6, y + 20, tl, "b"))
    for j, (s, c) in enumerate(notes): o.append(T(lw, top + rh * len(rows) + 14 + j * 14, s, c))
    return svg(h, o)
