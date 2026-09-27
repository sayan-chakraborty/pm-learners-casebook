"""SVG kit for teardown walkthroughs: simplified phone screens and browser windows, numbered markers,
and numbered notes. viewBox width 680 = text width; minimum text 10.3 units.

Screen item vocabulary (a trailing int on any item draws numbered marker n beside it):
  ("text", s [, cls])          ("center", s [, cls])        ("big", s [, fill])
  ("card", title [, sub])      ("icons", [labels] [, color]) ("banner", text [, fill, stroke])
  ("btn", text [, color])      ("row", left, right)          ("bubble", "line1|line2", "l"|"r")
  ("tick", text)               ("scratch", title, sub)       ("gap", n)
  ("cols", [(title, sub), ...])  small side-by-side tiles (browser screens)
"""
from html import escape as E
import textwrap

ACC = "#0b5d7a"

def _t(x, y, s, cls="", anchor="start", size=None, fill=None):
    st = f' style="font-size:{size}px"' if size else ""
    f = f' fill="{fill}"' if fill else ""
    c = f' class="{cls}"' if cls else ""
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}"{c}{f}{st}>{E(s)}</text>'

def _marker(n, x, y):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8.5" fill="{ACC}" stroke="#fff" stroke-width="1.5"/>' + _t(x, y + 3.8, str(n), "w b", "middle", size=10.3)

def _items(items, x, cx, cw, cy, color, center_x, mark_x=None):
    o = []
    for it in items:
        it = list(it); mark = it.pop() if isinstance(it[-1], int) and it[0] != "gap" else None
        k = it[0]; top = cy
        if k == "text":
            o.append(_t(cx + 2, cy + 11, it[1], it[2] if len(it) > 2 else "", size=10.3)); cy += 16
        elif k == "center":
            o.append(_t(center_x, cy + 11, it[1], it[2] if len(it) > 2 else "", "middle", size=10.3)); cy += 16
        elif k == "big":
            o.append(_t(center_x, cy + 20, it[1], "b", "middle", size=19, fill=it[2] if len(it) > 2 else "#1c232b")); cy += 28
        elif k == "card":
            o.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="38" rx="6" fill="#fff" stroke="#e1e4e8"/>')
            o.append(_t(cx + 7, cy + 15, it[1], "b", size=10.5))
            if len(it) > 2: o.append(_t(cx + 7, cy + 30, it[2], "s", size=10.3))
            cy += 44
        elif k == "icons":
            labels = it[1]; col = it[2] if len(it) > 2 else color; sx = cw / len(labels)
            o.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="46" rx="6" fill="#fff"/>')
            for i, lb in enumerate(labels):
                px = cx + sx * (i + .5)
                o.append(f'<circle cx="{px:.1f}" cy="{cy+15}" r="9" fill="{col}"/>' + _t(px, cy + 39, lb, "", "middle", size=10.3))
            cy += 52
        elif k == "banner":
            fill = it[2] if len(it) > 2 else "#ffe7c2"; st = it[3] if len(it) > 3 else "#e0a340"
            o.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="26" rx="6" fill="{fill}" stroke="{st}"/>')
            o.append(_t(center_x, cy + 17, it[1], "b", "middle", size=10.3)); cy += 32
        elif k == "btn":
            col = it[2] if len(it) > 2 else color
            o.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="28" rx="14" fill="{col}"/>')
            o.append(_t(center_x, cy + 18.5, it[1], "b w", "middle", size=10.8)); cy += 34
        elif k == "row":
            o.append(_t(cx + 2, cy + 11, it[1], "", size=10.3) + _t(cx + cw - 2, cy + 11, it[2], "b", "end", size=10.3)); cy += 16
        elif k == "bubble":
            side = it[2] if len(it) > 2 else "r"; bw = cw * .74; bx = cx + (cw - bw if side == "r" else 0)
            o.append(f'<rect x="{bx:.1f}" y="{cy}" width="{bw:.1f}" height="34" rx="8" fill="{"#fff" if side == "l" else "#e8f0fe"}" stroke="#d5dbe3"/>')
            for j, ln in enumerate(it[1].split("|")[:2]):
                o.append(_t(bx + 7, cy + 14 + j * 13, ln, "b" if j == 0 else "s", size=10.3))
            cy += 40
        elif k == "tick":
            o.append(f'<circle cx="{center_x}" cy="{cy + 20}" r="17" fill="#127a64"/>'
                     f'<path d="M{center_x-8},{cy+20} l6,6 l11,-12" stroke="#fff" stroke-width="3.2" fill="none"/>')
            o.append(_t(center_x, cy + 52, it[1], "b", "middle", size=11)); cy += 60
        elif k == "scratch":
            o.append(f'<rect x="{cx+12}" y="{cy}" width="{cw-24}" height="74" rx="8" fill="#fff3d6" stroke="#e0a340" stroke-width="1.4"/>')
            o.append(_t(center_x, cy + 30, it[1], "b", "middle", size=15, fill="#9a6310"))
            o.append(_t(center_x, cy + 52, it[2], "s", "middle", size=10.3)); cy += 80
        elif k == "cols":
            n = len(it[1]); g = 6; tw = (cw - g * (n - 1)) / n
            for i, (ti, su) in enumerate(it[1]):
                tx = cx + i * (tw + g)
                o.append(f'<rect x="{tx:.1f}" y="{cy}" width="{tw:.1f}" height="40" rx="6" fill="#fff" stroke="#e1e4e8"/>')
                o.append(_t(tx + 6, cy + 16, ti, "s", size=10.3) + _t(tx + 6, cy + 32, su, "b", size=11.5))
            cy += 46
        elif k == "gap":
            cy += it[1]
        if mark: o.append(_marker(mark, mark_x if mark_x else cx + cw + 4, (top + cy - 6) / 2))
    return o, cy

def phone(x, y, items, brand="", color="#5f259f", w=176, h=300, step=None, url=None):
    o = []
    if step: o.append(_t(x + w / 2, y - 8, step, "b", "middle"))
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="#fff" stroke="#2b3138" stroke-width="2.6"/>')
    o.append(f'<rect x="{x+7}" y="{y+12}" width="{w-14}" height="{h-24}" rx="11" fill="#f4f5f7"/>')
    top = y + 12
    if url:     # mobile browser: address bar above the site header
        o.append(f'<path d="M{x+7},{top+12} a12,12 0 0 1 12,-12 h{w-38} a12,12 0 0 1 12,12 v8 h{-(w-14)} z" fill="#e3e6ea"/>')
        o.append(f'<rect x="{x+14}" y="{top+3}" width="{w-28}" height="15" rx="7.5" fill="#fff"/>' + _t(x + 20, top + 14, url, "s", size=10.3))
        top += 20
        o.append(f'<rect x="{x+7}" y="{top}" width="{w-14}" height="28" fill="{color}"/>')
    else:
        o.append(f'<path d="M{x+7},{top+12} a12,12 0 0 1 12,-12 h{w-38} a12,12 0 0 1 12,12 v16 h{-(w-14)} z" fill="{color}"/>')
    o.append(_t(x + 16, top + 19, brand, "b w", size=11.5))
    body, _ = _items(items, x, x + 13, w - 26, top + 36, color, x + w / 2, mark_x=x + w + 1)
    return "\n".join(o + body)

def browser(x, y, items, url, brand="", color="#0b5d7a", w=360, h=300, step=None, side=None):
    """Laptop-style browser window. side: optional list of left-nav labels."""
    o = []
    if step: o.append(_t(x + w / 2, y - 8, step, "b", "middle"))
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#fff" stroke="#2b3138" stroke-width="2"/>')
    o.append(f'<path d="M{x},{y+8} a8,8 0 0 1 8,-8 h{w-16} a8,8 0 0 1 8,8 v18 h{-w} z" fill="#e3e6ea"/>')
    for i, c in enumerate(("#e0645c", "#e0b040", "#5cb85c")):
        o.append(f'<circle cx="{x+12+i*11}" cy="{y+13}" r="3.6" fill="{c}"/>')
    o.append(f'<rect x="{x+52}" y="{y+5}" width="{w-64}" height="16" rx="8" fill="#fff"/>' + _t(x + 60, y + 17, url, "s", size=10.3))
    o.append(f'<rect x="{x+1}" y="{y+26}" width="{w-2}" height="26" fill="{color}"/>' + _t(x + 12, y + 44, brand, "b w", size=11.5))
    cx = x + 12
    if side:
        o.append(f'<rect x="{x+1}" y="{y+52}" width="92" height="{h-53}" fill="#eef1f4"/>')
        for i, s in enumerate(side):
            o.append(_t(x + 10, y + 72 + i * 20, s, "b" if i == 0 else "s", size=10.3))
        cx = x + 104
    o.append(f'<rect x="{cx-4}" y="{y+52}" width="{x+w-cx+3}" height="{h-53}" fill="#f7f8fa"/>')
    body, _ = _items(items, x, cx, x + w - cx - 14, y + 60, color, (cx + x + w - 14) / 2, mark_x=x + w + 1)
    return "\n".join(o + body)

def notes(x, y, rows, width_px=176, lh=13.5):
    """numbered notes; titles and bodies both wrap inside width_px"""
    o = []
    tc, bc = max(12, int((width_px - 24) / 6.4)), max(14, int((width_px - 24) / 5.6))
    for n, title, body in rows:
        o.append(_marker(n, x + 9, y - 4))
        tl = textwrap.wrap(title, tc)
        for j, ln in enumerate(tl): o.append(_t(x + 24, y + j * lh, ln, "b"))
        yy = y + (len(tl) - 1) * lh
        for ln in textwrap.wrap(body, bc):
            yy += lh; o.append(_t(x + 24, yy, ln, "s"))
        y = yy + lh + 6
    return "\n".join(o), y

def arrow(x1, y, x2):
    return (f'<path d="M{x1},{y} L{x2-8},{y}" stroke="#7d8793" stroke-width="1.6" fill="none"/>'
            f'<path d="M{x2-8},{y-6} L{x2},{y} L{x2-8},{y+6} z" fill="#7d8793"/>')

def walkthrough(frames, note_rows, top=18, frame_h=300):
    """frames: list of dicts {kind:'phone'|'browser', w, step, items, brand, color, url, side}.
    Frames are laid out left to right with equal gaps; notes go under each frame."""
    widths = [f.get("w", 176 if f["kind"] == "phone" else 300) for f in frames]
    gap = (664 - sum(widths)) / max(1, len(frames) - 1)
    o, x, ends = [], 2, []
    for i, f in enumerate(frames):
        w = widths[i]
        kw = dict(brand=f.get("brand", ""), color=f.get("color", ACC), w=w, h=frame_h, step=f.get("step"))
        if f["kind"] == "phone": o.append(phone(x, top, f["items"], url=f.get("url"), **kw))
        else: o.append(browser(x, top, f["items"], f["url"], side=f.get("side"), **kw))
        nsvg, end = notes(x, top + frame_h + 26, note_rows[i], width_px=w + 10)
        o.append(nsvg); ends.append(end)
        if i < len(frames) - 1: o.append(arrow(x + w + 5, top + frame_h / 2, x + w + gap - 5))
        x += w + gap
    h = int(max(ends))
    return f'<svg class="d" viewBox="0 0 680 {h}" xmlns="http://www.w3.org/2000/svg">\n' + "\n".join(o) + "\n</svg>"

# ---------- behind-the-screens sequence diagrams (teardowns) ----------
KIND = {"user": ("#e1f2ec", "#127a64"), "app": ("#e3f0f5", "#0b5d7a"), "bank": ("#dbe8f5", "#2f6ea5"),
        "network": ("#fde7c8", "#c47f17"), "partner": ("#f1e6f8", "#7c3aa6"), "merchant": ("#eef0f2", "#5b6470"),
        "risk": ("#fcecea", "#b93a32")}
CIRC = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭"

def seq(actors, steps, row=27, top=52, note=None):
    """actors: [(name, sub, kind)]; steps: [(from, to, label, style)] with style in
    'msg' | 'ret' | 'money' | 'self'. For 'self', `to` is ignored and the label sits beside the lane.
    Returns an SVG string; steps are numbered automatically."""
    n = len(actors); lw = min(118, 660 / n - 8); span = (680 - lw) / (n - 1)
    X = [lw / 2 + i * span for i in range(n)]
    h = top + row * len(steps) + 16 + (18 if note else 0)
    o = ['<defs><marker id="sqa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#4a5563"/></marker>'
         '<marker id="sqr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#8a939e"/></marker>'
         '<marker id="sqg" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4.2" markerHeight="4.2" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#127a64"/></marker></defs>']
    for (name, sub, kind), x in zip(actors, X):
        fill, st = KIND[kind]
        o.append(f'<rect x="{x - lw/2:.1f}" y="2" width="{lw:.1f}" height="36" rx="5" fill="{fill}" stroke="{st}" stroke-width="1.3"/>')
        o.append(_t(x, 17, name, "b", "middle") + _t(x, 31, sub, "s", "middle"))
        o.append(f'<line x1="{x:.1f}" y1="38" x2="{x:.1f}" y2="{h - 8 - (18 if note else 0)}" stroke="#c3cad2" stroke-width="1.1" stroke-dasharray="3 3"/>')
    for i, (a, b, label, style) in enumerate(steps):
        y = top + i * row + 10; lab = f"{CIRC[i]} {label}"
        if style == "self":
            x = X[a]
            o.append(f'<rect x="{x-5:.1f}" y="{y-9}" width="10" height="16" fill="#fff3d6" stroke="#c47f17"/>')
            right = a < n - 1 and (a == 0 or len(label) * 5.6 < (680 - x - 12))
            o.append(_t(x + 10 if right else x - 10, y + 3, lab, "halo", "start" if right else "end"))
            continue
        x1, x2 = X[a], X[b]; d = 1 if x2 > x1 else -1
        cls = {"msg": 'stroke="#4a5563" stroke-width="1.4"', "ret": 'class="ret"', "money": 'stroke="#127a64" stroke-width="3"'}[style]
        mk = {"msg": "sqa", "ret": "sqr", "money": "sqg"}[style]
        o.append(f'<line x1="{x1:.1f}" y1="{y}" x2="{x2 - d*3:.1f}" y2="{y}" {cls} fill="none" marker-end="url(#{mk})"/>')
        tc = "halo b grn" if style == "money" else ("halo s" if style == "ret" else "halo")
        o.append(_t((x1 + x2) / 2, y - 5, lab, tc, "middle"))
    if note: o.append(_t(4, h - 6, note, "b acc"))
    return f'<svg class="d" viewBox="0 0 680 {h}" xmlns="http://www.w3.org/2000/svg">\n' + "\n".join(o) + "\n</svg>"
