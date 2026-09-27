"""Shared figure helpers for M9 (copied from M8: box, colours, vbars, curves, etree, stacks, ladder, arr)."""
from m9_figs import FIGS, svg, T, lines, hbars, waterfall, loop, two_by_two, seq, strip  # noqa: F401
MK = ('<defs><marker id="pa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
      '<path d="M0,0 L10,5 L0,10 z" fill="#4a5563"/></marker>'
      '<marker id="pg" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4.5" markerHeight="4.5" orient="auto">'
      '<path d="M0,0 L10,5 L0,10 z" fill="#127a64"/></marker>'
      '<marker id="pr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
      '<path d="M0,0 L10,5 L0,10 z" fill="#b93a32"/></marker></defs>')


def box(x, y, w, h, fill, st, rows, sw=1.4, lh=14):
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{st}" stroke-width="{sw}"/>']
    y0 = y + h / 2 - (len(rows) - 1) * lh / 2 + 4
    for i, (s, c) in enumerate(rows):
        o.append(T(x + w / 2, y0 + i * lh, s, c, "middle"))
    return "".join(o)


G, B, A, GR, R, P = (("#e1f2ec", "#127a64"), ("#e3f0f5", "#0b5d7a"), ("#fde7c8", "#c47f17"), ("#eef0f2", "#5b6470"),
                     ("#fcecea", "#b93a32"), ("#f1e6f8", "#7c3aa6"))
I = ("#e8eaf8", "#3e4fb8")


def vbars(rows, maxv, title, vw=330, h=190, fmt="{}", colors=None, sub=None):
    """small vertical bar chart. rows: (label 'a|b', value, value label or None)"""
    n = len(rows); L, Rr, Tp, Bt = 8, vw - 8, 40 if sub else 28, h - 34
    bw = (Rr - L) / n
    o = [T(0, 12, title, "b")]
    if sub: o.append(T(0, 26, sub, "s"))
    o.append(f'<line x1="{L}" y1="{Bt}" x2="{Rr}" y2="{Bt}" stroke="#4a5563"/>')
    for i, (lab, v, vl) in enumerate(rows):
        x = L + i * bw + bw * 0.2; w = bw * 0.6; y = Bt - (Bt - Tp - 14) * v / maxv
        col = (colors or ["#0b5d7a"])[i % len(colors or ["#0b5d7a"])]
        o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{Bt - y:.1f}" fill="{col}" rx="2"/>')
        o.append(T(x + w / 2, y - 5, vl if vl else fmt.format(v), "b", "middle"))
        o.append(lines(x + w / 2, Bt + 14, lab, "s", "middle", 12))
    return svg(h, o, vw)



def curves(series, xs, L=46, R=520, Tp=14, Bt=170, h=196, ymax=100, notes=(), step=25, unit="%"):
    X = lambda i: L + (R - L) * i / (len(xs) - 1)
    Y = lambda v: Bt - (Bt - Tp) * v / ymax
    o = [f'<line x1="{L}" y1="{Bt}" x2="{R}" y2="{Bt}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{Bt}" stroke="#4a5563"/>']
    for v in range(0, ymax + 1, step):
        o.append(T(L - 6, Y(v) + 4, str(v), "s", "end"))
        if v: o.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{R}" y2="{Y(v):.1f}" stroke="#eef0f2"/>')
    for i, m in enumerate(xs): o.append(T(X(i), Bt + 15, m, "s", "middle"))
    for lab, vals, col, dy in series:
        d = " ".join(f"{'M' if i == 0 else 'L'}{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(vals))
        o.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2.6"/>')
        for i, v in enumerate(vals): o.append(f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="2.8" fill="{col}"/>')
        o.append(T(R + 8, Y(vals[-1]) + 4 + dy, f"{lab}: {vals[-1]}{unit}", "b", fill=col))
    for x, y, s, c in notes: o.append(T(x, y, s, c))
    return svg(h, o)



def etree(boxes, check, rng, h=150, swing=None):
    """boxes: list of (title, sub1, sub2); last is the answer. swing: index of the orange box."""
    n = len(boxes); w = (680 - 18 * (n - 1)) / n
    o = ['<defs><marker id="gt5" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#4a5563"/></marker></defs><g class="c">']
    for i, (a, b, c) in enumerate(boxes):
        x = i * (w + 18)
        fill, st, sw = ("#e3f0f5", "#0b5d7a", 1)
        if i == swing: fill, st, sw = ("#fbf4e6", "#c47f17", 2)
        if i == n - 1: fill, st, sw = ("#e7f4f0", "#127a64", 2)
        o.append(f'<rect x="{x:.1f}" y="8" width="{w:.1f}" height="58" rx="6" fill="{fill}" stroke="{st}" stroke-width="{sw}"/>')
        o.append(T(x + w / 2, 27, a, "b grn" if i == n - 1 else "b", "middle")); o.append(T(x + w / 2, 42, b, "", "middle")); o.append(T(x + w / 2, 56, c, "", "middle"))
        if i < n - 1: o.append(f'<line x1="{x + w:.1f}" y1="37" x2="{x + w + 16:.1f}" y2="37" class="ln" marker-end="url(#gt5)"/>')
    o.append(f'<rect x="0" y="80" width="330" height="{h - 84}" rx="6" fill="#f3f3ee" stroke="#6b6a52"/>')
    for i, (s, c) in enumerate(check): o.append(T(10, 98 + i * 15, s, c))
    o.append(f'<rect x="350" y="80" width="330" height="{h - 84}" rx="6" fill="#fbf4e6" stroke="#c47f17"/>')
    for i, (s, c) in enumerate(rng): o.append(T(360, 98 + i * 15, s, c))
    o.append("</g>")
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



def ladder(steps, title, h=196):
    """steps: (name, sub, price, colours) rising left to right."""
    n = len(steps); w = (680 - 12 * (n - 1)) / n
    o = [MK, T(0, 12, title, "b")]
    for i, (name, sub, price, (fill, st)) in enumerate(steps):
        x = i * (w + 12); top = 96 - i * 24; hh = h - 16 - top
        o.append(f'<rect x="{x:.1f}" y="{top}" width="{w:.1f}" height="{hh}" rx="6" fill="{fill}" stroke="{st}" stroke-width="1.4"/>')
        o.append(T(x + w / 2, top + 18, name, "b", "middle"))
        for j, l in enumerate(sub.split("|")): o.append(T(x + w / 2, top + 34 + j * 13, l, "s", "middle"))
        o.append(T(x + w / 2, h - 28, price, "b grn", "middle"))
    return svg(h, o)


ARW = '<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#4a5563" stroke-width="1.4" marker-end="url(#pa)"/>'


def arr(x1, y1, x2, y2, col="#4a5563", dash=False):
    d = ' stroke-dasharray="4 3"' if dash else ""
    mk = "pr" if col == "#b93a32" else ("pg" if col == "#127a64" else "pa")
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="1.5"{d} marker-end="url(#{mk})"/>'


