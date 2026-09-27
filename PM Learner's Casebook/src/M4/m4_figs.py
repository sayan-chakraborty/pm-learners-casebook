"""Generated SVGs for M4 ({{SVG:name}} in parts): move strips, waterfalls, bar charts, teardown sequence flows."""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "common"))
from svgkit import seq as _seq  # noqa: E402
from html import escape as _E

def seq(*a, **k):
    k.setdefault("row", 22)
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




# =====================================================================
# M4 figures
# =====================================================================
FIGS["strip41"] = strip([("Clarify", "who pays, who rides"), ("Pick", "which families"), ("Riskiest", "what must be true"),
                         ("MVP", "one school, 3 vans"), ("Learn", "what we measure"), ("Scale", "only if it holds")])
FIGS["strip42"] = strip([("Clarify", "which engagement"), ("Outcome", "one number"), ("Opportunities", "tourist pains"),
                         ("Solutions", "2–3 per pain"), ("Test", "cheapest first"), ("Measure", "HEART + guardrail")])
FIGS["strip43"] = strip([("Clarify", "who, where, when"), ("Rule out", "data, outside"), ("Find where", "which trips"),
                         ("Why", "driver’s maths"), ("Fix", "balance both"), ("Measure", "completed trips")])
FIGS["strip44"] = strip([("Clarify", "what exists today"), ("Size", "TAM → SOM"), ("Forces", "is it winnable?"),
                         ("Right to win", "what MMT has"), ("Entry", "wedge + phases"), ("Measure", "and kill rule")])
FIGS["stripg1"] = strip([("Unit", "drivers active when?"), ("Approach", "supply from demand"), ("Tree", "peak rides ÷ rate"),
                         ("Numbers", "round, with reasons"), ("Check", "per person, real data"), ("Range", "and what moves it")])
FIGS["stripg2"] = strip([("Unit", "bikes, one city"), ("Approach", "demand → fleet"), ("Tree", "rides ÷ rides per bike"),
                         ("Numbers", "peak, not average"), ("Check", "vs Rapido’s scale"), ("Range", "and spares")])

# ---------- primer: driver's ₹300 ride and the platform's side ----------
FIGS["wf_driver"] = waterfall([
    ("fare|paid", 300, "start"), ("commission|20%", 60, "down"), ("fuel, upkeep|15 km", 75, "down"),
    ("car EMI|per trip", 48, "down"), ("driver|keeps", 0, "total")],
    note="Driver’s side of one ₹300 cab ride|(12 km trip + 3 km to the pickup)", vw=330, top=40, h=212, scale=0.40)
FIGS["wf_platform"] = waterfall([
    ("commission", 60, "start"), ("driver|incentives", 22, "down"), ("rider|discount", 15, "down"),
    ("maps, cloud,|payments", 7, "down"), ("support,|insurance", 6, "down"), ("left", 0, "total")],
    note="Platform’s side of the same ride:|₹60 of commission shrinks fast", vw=330, top=40, h=212, scale=1.9)

def comm_vs_sub():
    L, R, Tp, B = 60, 660, 18, 190
    X = lambda t: L + (R - L) * t / 16; Y = lambda v: B - (B - Tp) * v / 400
    o = [f'<line x1="{L}" y1="{B}" x2="{R}" y2="{B}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{B}" stroke="#4a5563"/>']
    for v in (0, 100, 200, 300, 400):
        o.append(T(L - 6, Y(v) + 4, f"₹{v}", "s", "end"))
        if v: o.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{R}" y2="{Y(v):.1f}" stroke="#eceff2"/>')
    for t in range(0, 17, 2): o.append(T(X(t), B + 15, str(t), "s", "middle"))
    o.append(T((L + R) / 2, B + 30, "trips a driver completes in a day", "b", "middle"))
    o.append(f'<line x1="{X(0)}" y1="{Y(0)}" x2="{X(16)}" y2="{Y(384):.1f}" stroke="#b93a32" stroke-width="3"/>')
    o.append(f'<line x1="{X(0)}" y1="{Y(29):.1f}" x2="{X(16)}" y2="{Y(29):.1f}" stroke="#127a64" stroke-width="3"/>')
    o.append(T(X(9.3), Y(250), "Commission: 20% of a ₹120 auto fare", "b red halo", "end"))
    o.append(T(X(9.3), Y(250) + 14, "= ₹24 a trip, ₹288 at 12 trips", "red halo", "end"))
    o.append(T(X(16), Y(29) - 8, "Subscription: flat ₹29 a day, whatever the trips", "b grn halo", "end"))
    o.append(f'<circle cx="{X(1.2):.1f}" cy="{Y(29):.1f}" r="5" fill="#fff" stroke="#1c232b" stroke-width="1.5"/>')
    o.append(T(X(1.2) + 8, Y(29) - 26, "break-even at ~1.2 trips:", "s halo"))
    o.append(T(X(1.2) + 8, Y(29) - 13, "after that the pass is cheaper", "s halo"))
    o.append(f'<line x1="{X(12):.1f}" y1="{Y(288):.1f}" x2="{X(12):.1f}" y2="{Y(29):.1f}" stroke="#1c232b" stroke-dasharray="3 2"/>')
    o.append(T(X(12) + 6, Y(160), "₹259 a day stays", "b halo"))
    o.append(T(X(12) + 6, Y(160) + 14, "with the driver", "halo"))
    o.append(T(X(12) + 6, Y(160) + 28, "≈ ₹6,700 a month", "s halo"))
    return svg(226, o)
FIGS["comm_sub"] = comm_vs_sub()

FIGS["share"] = (lambda: svg(118, [
    T(0, 12, "Share of rides by vehicle type, India, 2025 (approximate)", "s"),
    *[x for i, (lab, parts) in enumerate([("Cabs", [("Uber", 50, "#1c232b"), ("Ola", 34, "#127a64"), ("Rapido", 14, "#c47f17"), ("", 2, "#c3cad2")]),
                                            ("Autos", [("Uber", 40, "#1c232b"), ("Rapido", 31, "#c47f17"), ("Ola", 26, "#127a64"), ("", 3, "#c3cad2")]),
                                            ("Bike taxis", [("Rapido", 56, "#c47f17"), ("Uber, Ola and others", 44, "#9aa3ad")])])
      for x in ([T(84, 40 + i * 28, lab, "b", "end")] + [
          f'<rect x="{92 + sum(p[1] for p in parts[:j]) * 5.8:.1f}" y="{27 + i * 28}" width="{v * 5.8:.1f}" height="19" fill="{c}"/>' +
          (T(92 + sum(p[1] for p in parts[:j]) * 5.8 + 5, 41 + i * 28, f"{n} {v}%", "b w") if n else "")
          for j, (n, v, c) in enumerate(parts)])]]))()

FIGS["cancel_why"] = hbars([
    ("Drop is far or dead-end", 34, "   long empty drive back"),
    ("Pickup too far away", 22, "   15 min unpaid to reach"),
    ("Rider wants cash (or UPI)", 16, "   payment mode mismatch"),
    ("Short, low-fare trip", 14, "   not worth the traffic"),
    ("Better trip on another app", 9, "   multi-apping"),
    ("Genuine problem", 5, "   breakdown, emergency")], 40, lw=176, unit="%",
    colors=["#b93a32", "#b93a32", "#c47f17", "#c47f17", "#5b6470", "#9aa3ad"],
    note="Why a driver cancels after accepting: illustrative split of 100 driver cancellations in a metro")

FIGS["ota_earn"] = hbars([
    ("₹10,000 domestic flight", 400, "  convenience fee + small airline incentive (~3–5%)"),
    ("₹10,000 of hotel nights", 1600, "  hotel commission (~15–20%)"),
    ("₹10,000 holiday package", 1200, "  margin on the bundle (~10–15%)"),
    ("₹10,000 of bus tickets", 900, "  operator commission (~8–10%)")], 2000, lw=170, unit="",
    fmt="₹{:,}", colors=["#2f6ea5", "#127a64", "#0b5d7a", "#c47f17"],
    note="What an online travel agency keeps on ₹10,000 of each kind of booking (illustrative ranges)")

def fare_build():
    o = [T(0, 12, "How a ₹300 fare is built (normal hour), and the same ride at 1.8× surge", "s")]
    def bar(y, parts, lab, cls):
        x = 120; o.append(T(112, y + 15, lab, cls, "end"))
        for l, v, c in parts:
            o.append(f'<rect x="{x}" y="{y}" width="{v}" height="22" fill="{c}" stroke="#fff"/>')
            o.append(lines(x + v / 2, y + 36, l, "s", "middle", 12)); x += v
    bar(24, [("base|₹50", 50, "#0b5d7a"), ("12 km × ₹14|= ₹168", 168, "#2f6ea5"), ("35 min × ₹1.5|= ₹52", 52, "#5b8fc0"), ("fee|₹30", 30, "#9aa3ad")], "Normal: ₹300", "b")
    bar(92, [("(base + km + minutes) × 1.8|= ₹270 × 1.8 = ₹486", 486, "#b93a32"), ("fee|₹30", 30, "#9aa3ad")], "Surge: ₹516", "b red")
    o.append(T(120, 166, "The 2025 guidelines let states cap the multiplier at 2× the base fare; here the fee sits outside the multiplier.", "s"))
    return svg(172, o)
FIGS["fare"] = fare_build()

# ---------- Case 4.1 ----------
def van_profit():
    ks = [4, 5, 6, 7, 8]; vals = [6000 * k - 40000 for k in ks]
    L, R, base = 70, 670, 104; sc = 0.0042
    o = [T(0, 12, "Monthly profit per van: 2 school runs a morning, ₹3,000 per child, costs ₹40,000 (illustrative)", "s"),
         f'<line x1="{L}" y1="{base}" x2="{R}" y2="{base}" stroke="#4a5563"/>']
    bw = (R - L) / len(ks)
    for i, (k, v) in enumerate(zip(ks, vals)):
        x = L + i * bw + 18; w = bw - 36; hh = abs(v) * sc
        y = base - hh if v > 0 else base
        o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{hh:.1f}" fill="{"#127a64" if v > 0 else "#b93a32"}" rx="2"/>')
        o.append(T(x + w / 2, (y - 5) if v > 0 else (base + hh + 13), ("+" if v > 0 else "−") + f"₹{abs(v):,}", "b", "middle"))
        o.append(T(x + w / 2, base - 6 if v < 0 else base + 14, f"{k} children a run", "s", "middle"))
    o.append(T(L - 6, base + 4, "₹0", "s", "end"))
    o.append(T(L, 36, "break-even ≈ 6.7 children per run", "b acc"))
    o.append(T(L, 50, "(₹40,000 ÷ ₹6,000 per extra child a run)", "s"))
    return svg(184, o)
FIGS["van"] = van_profit()

def risk_map():
    L, R, Tp, B = 40, 326, 22, 212
    o = [f'<rect x="{L}" y="{Tp}" width="{R-L}" height="{B-Tp}" fill="#fafbfc" stroke="#c3cad2"/>',
         f'<line x1="{(L+R)/2}" y1="{Tp}" x2="{(L+R)/2}" y2="{B}" stroke="#c3cad2"/><line x1="{L}" y1="{(Tp+B)/2}" x2="{R}" y2="{(Tp+B)/2}" stroke="#c3cad2"/>',
         f'<rect x="{(L+R)/2}" y="{Tp}" width="{(R-L)/2}" height="{(B-Tp)/2}" fill="#fcecea"/>',
         T(R - 6, (Tp+B)/2 - 8, "test these first", "b red", "end"),
         T(L + 6, Tp + 14, "fatal, but we know", "s"), T(L + 6, B - 8, "safe to assume", "s"), T(R - 6, B - 8, "cheap to check later", "s", "end")]
    pts = [("Parents pay ₹3,000", 0.78, 0.86, "#b93a32"), ("7+ children a run", 0.66, 0.70, "#b93a32"),
           ("Same driver daily", 0.40, 0.62, "#c47f17"), ("Kids like the ride", 0.72, 0.28, "#5b6470"), ("GPS tracking works", 0.14, 0.44, "#5b6470")]
    for n, x, y, c in pts:
        px, py = L + x * (R - L), B - y * (B - Tp)
        o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="{c}"/>')
        o.append(T(px + (8 if x < 0.7 else -8), py - 7, n, "b halo", "start" if x < 0.7 else "end"))
    o.append(T((L + R) / 2, B + 16, "how little we know →", "b", "middle"))
    o.append(f'<text x="16" y="{(Tp+B)/2:.1f}" text-anchor="middle" class="b" transform="rotate(-90 16 {(Tp+B)/2:.1f})">how fatal if wrong →</text>')
    return svg(234, o, 330)
FIGS["riskmap"] = risk_map()

def bml():
    o = ['<defs><marker id="bmA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#3e4fb8"/></marker></defs>']
    nodes = [(165, 34, "Build", "3 vans, 1 school,|routes by hand"), (282, 150, "Measure", "sign-ups, renewals,|on-time at the gate"),
             (48, 150, "Learn", "price? radius?|second school?")]
    for (x, y, h, s) in nodes:
        o.append(f'<rect x="{x-62}" y="{y-22}" width="124" height="50" rx="8" fill="#eef0fb" stroke="#3e4fb8" stroke-width="1.4"/>')
        o.append(T(x, y - 5, h, "b fwc", "middle")); o.append(lines(x, y + 9, s, "s", "middle", 12))
    for (x1, y1, x2, y2) in [(228, 50, 270, 124), (218, 162, 112, 162), (62, 124, 104, 50)]:
        o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#3e4fb8" stroke-width="2" marker-end="url(#bmA)"/>')
    o.append(T(165, 104, "one loop =", "s", "middle")); o.append(T(165, 117, "4 weeks, ~₹3 lakh", "b", "middle"))
    o.append(T(165, 206, "Ideas → code → data → lessons, then round again", "s", "middle"))
    o.append(T(165, 220, "Aim: make each loop faster, not bigger", "b acc", "middle"))
    return svg(234, o, 330)
FIGS["bml"] = bml()

# ---------- Case 4.2 ----------
def journey():
    stages = [("Find places", "(Entice)", "Want to know tourist|hotspots; information,|pictures, reviews"),
              ("Travel to place", "(Enter)", "Navigate using rented|cars, public transport,|cabs, or walk"),
              ("Explore", "(Engage)", "Make bookings; try local|restaurants, street|shopping, hire guides"),
              ("Feedback", "(Extend)", "Share reviews|and pictures")]
    pains = [("1 Trip planning", 0), ("2 Authentic experience", 2), ("3 Managing bookings", 2), ("4 Group travel", 1)]
    o = []; w = 170
    for i, (h, s, body) in enumerate(stages):
        x = i * w; tip = 12 if i < 3 else 0
        pts = f"{x},0 {x+w-2},0 {x+w-2+tip},30 {x+w-2},60 {x},60" + (f" {x+12},30" if i else "")
        o.append(f'<polygon points="{pts}" fill="{["#0b5d7a","#2f6ea5","#127a64","#7c3aa6"][i]}"/>')
        o.append(T(x + w / 2 + 4, 26, h, "b w", "middle")); o.append(T(x + w / 2 + 4, 42, s, "w", "middle"))
        o.append(f'<rect x="{x+4}" y="68" width="{w-12}" height="52" rx="5" fill="#f5f7f9" stroke="#c3cad2"/>')
        o.append(lines(x + w / 2 - 2, 84, body, "s", "middle", 13))
    o.append(T(0, 142, "Pain points the candidate names, placed on the stage where they bite:", "b"))
    for p, x, y, w_ in [("1 Trip planning", 6, 150, 130), ("4 Group travel", 176, 150, 120), ("2 Authentic experience", 346, 150, 170), ("3 Managing bookings", 346, 178, 160)]:
        o.append(f'<rect x="{x}" y="{y}" width="{w_}" height="22" rx="11" fill="#fcecea" stroke="#b93a32"/>')
        o.append(T(x + 10, y + 15, p, "b red"))
    o.append(T(0, 216, "Redrawn from the original (IIM B casebook, p. 114); pain-point placement added.", "s"))
    return svg(222, o)
FIGS["journey"] = journey()

def ost():
    o = ['<g class="c">']
    def box(x, y, w, h, fill, st, txt, cls="b"):
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{st}" stroke-width="1.3"/>')
        ls = txt.split("|"); y0 = y + h / 2 - (len(ls) - 1) * 6.5 + 4
        for i, l in enumerate(ls): o.append(T(x + w / 2, y0 + i * 13, l, cls if i == 0 else "", "middle"))
    def ln(x1, y1, x2, y2): o.append(f'<path d="M{x1},{y1} C{x1},{(y1+y2)/2} {x2},{(y1+y2)/2} {x2},{y2}" fill="none" stroke="#7d8793" stroke-width="1.2"/>')
    box(190, 2, 300, 38, "#e7f4f0", "#127a64", "Outcome: more trips planned in Maps|8% of trips today → 15% (illustrative)")
    X = [8, 178, 348, 518]
    opps = ["“I don’t know what’s|worth it in 2 days”", "“Is this a tourist trap?|Will I be overcharged?”", "“Queues and tickets|everywhere”", "“I can’t read the|menu or the signs”"]
    for t_, x in zip(opps, X):
        ln(340, 40, x + 77, 60); box(x, 60, 154, 40, "#e3f0f5", "#0b5d7a", t_, "b")
    sols = [("Plan my day, from saves", 0, 0), ("Ask Maps trip question", 0, 1), ("“Locals love this” badge", 1, 0), ("Price range from visitors", 1, 1)]
    for t_, c, k in sols:
        x = X[c]; y = 114 + k * 30
        if k == 0: ln(x + 77, 100, x + 77, y)
        box(x, y, 154, 24, "#eef0fb", "#3e4fb8", t_, "")
    o.append(f'<rect x="348" y="114" width="324" height="54" rx="6" fill="#fafbfc" stroke="#c3cad2" stroke-dasharray="3 3"/>')
    o.append(T(510, 136, "parked: real needs, but fewer tourists", "s", "middle")); o.append(T(510, 150, "feel them on a two-day trip", "s", "middle"))
    for t_, x in [("Fake door on new-city|searches; count taps", 8), ("Badge in 2 cities;|compare saves, visits", 178)]:
        ln(x + 77, 168, x + 77, 184); box(x, 184, 154, 38, "#fbf4e6", "#c47f17", t_, "")
    o.append(T(348, 196, "Rows, top to bottom: outcome → opportunities", "s")); o.append(T(348, 210, "(needs, in the user’s words) → solutions →", "s")); o.append(T(348, 224, "experiments that test the solution cheaply", "s"))
    o.append("</g>")
    return svg(230, o)
FIGS["ost"] = ost()

# ---------- Case 4.3 ----------
def cancel_zone():
    rows = [("Inside the city core", 8, 9), ("To busy suburbs", 9, 11), ("To the airport", 10, 24), ("To the city’s edge", 11, 31)]
    L = 170; sc = 11; o = [T(0, 12, "Driver cancellations after accepting, % of accepted rides, by where the trip ends (illustrative)", "s")]
    for i, (lab, a, b) in enumerate(rows):
        y = 26 + i * 34
        o.append(T(L - 8, y + 18, lab, "b", "end"))
        o.append(f'<rect x="{L}" y="{y}" width="{a*sc}" height="12" fill="#9aa3ad"/>'); o.append(T(L + a * sc + 5, y + 10, f"{a}% before", "s"))
        o.append(f'<rect x="{L}" y="{y+14}" width="{b*sc}" height="12" fill="{"#b93a32" if b > 15 else "#0b5d7a"}"/>'); o.append(T(L + b * sc + 5, y + 24, f"{b}% after the release", "b" if b > 15 else "s"))
    o.append(T(L, 170, "Overall: 8% → 14%. Almost all of the rise is on trips that end", "b acc"))
    o.append(T(L, 184, "where the driver won’t find a next ride.", "b acc"))
    return svg(190, o)
FIGS["czone"] = cancel_zone()

def surge_curves():
    L, R, Tp, B = 64, 410, 16, 206
    X = lambda q: L + (R - L) * q / 1200; Y = lambda p: B - (B - Tp) * (p - 0.6) / 1.6
    o = [f'<line x1="{L}" y1="{B}" x2="{R}" y2="{B}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{B}" stroke="#4a5563"/>']
    for p in (1.0, 1.5, 2.0): o.append(T(L - 6, Y(p) + 4, f"{p:.1f}×", "s", "end"))
    for q in (0, 400, 800, 1200): o.append(T(X(q), B + 14, str(q), "s", "middle"))
    o.append(T((L + R) / 2, B + 28, "rides per hour in one zone", "b", "middle"))
    o.append(f'<text x="18" y="{(Tp+B)/2}" text-anchor="middle" class="b" transform="rotate(-90 18 {(Tp+B)/2})">price multiplier</text>')
    # demand: q = 1000 at 1.0, 800 at 1.5 ; supply: q = 600 at 1.0, 800 at 1.5
    dem = lambda p: 1000 - 400 * (p - 1.0); sup = lambda p: 600 + 400 * (p - 1.0)
    o.append(f'<line x1="{X(dem(0.7)):.1f}" y1="{Y(0.7):.1f}" x2="{X(dem(2.1)):.1f}" y2="{Y(2.1):.1f}" stroke="#2f6ea5" stroke-width="3"/>')
    o.append(f'<line x1="{X(sup(0.7)):.1f}" y1="{Y(0.7):.1f}" x2="{X(sup(2.1)):.1f}" y2="{Y(2.1):.1f}" stroke="#127a64" stroke-width="3"/>')
    o.append(T(X(dem(2.05)) - 8, Y(2.05) + 4, "riders wanting", "b halo", "end"))
    o.append(T(X(dem(2.05)) - 8, Y(2.05) + 18, "a ride", "halo", "end"))
    o.append(T(X(sup(2.0)) - 8, Y(2.0) + 4, "drivers willing", "b grn halo", "end"))
    o.append(T(X(sup(2.0)) - 8, Y(2.0) + 18, "to drive here", "grn halo", "end"))
    o.append(f'<line x1="{X(600):.1f}" y1="{Y(1.0):.1f}" x2="{X(1000):.1f}" y2="{Y(1.0):.1f}" stroke="#b93a32" stroke-width="2.5"/>')
    o.append(T(X(800), Y(1.0) + 16, "gap at 1.0×: 400 rides", "b red halo", "middle"))
    o.append(f'<circle cx="{X(800):.1f}" cy="{Y(1.5):.1f}" r="6" fill="#fff" stroke="#1c232b" stroke-width="2"/>')
    o.append(T(X(800) + 10, Y(1.5) - 8, "1.5×: 800 = 800", "b halo"))
    o.append(f'<line x1="{L}" y1="{Y(1.5):.1f}" x2="{X(800):.1f}" y2="{Y(1.5):.1f}" stroke="#1c232b" stroke-dasharray="3 2"/>')
    nx = 448
    notes = [("At base price (1.0×)", "b red"), ("1,000 want a ride, 600 drivers", ""), ("nearby: 400 wait, cancel or", ""), ("leave. Drivers pick the best", ""), ("trips and cancel the rest.", ""),
             ("", ""), ("At 1.5× surge", "b"), ("200 riders take the metro or", ""), ("wait; 200 more drivers drive", ""), ("in or log on. Nobody waits long.", ""),
             ("", ""), ("Capped at 2× base (2025 rules):", "b acc"), ("if the gap needs more, it stays.", "")]
    for i, (s, c) in enumerate(notes): o.append(T(nx, 26 + i * 14, s, c))
    return svg(240, o)
FIGS["surge"] = surge_curves()

# ---------- Case 4.4 ----------
def tam():
    rows = [("TAM", "All travel booked by Dubai’s 39 lakh residents", "39 lakh × 1.5 trips × ₹50,000", 29000, "#0b5d7a"),
            ("SAM", "Trips where MMT has an edge: Indian-origin residents", "22 lakh × 1.2 trips × ₹45,000", 12000, "#2f6ea5"),
            ("Online", "… of which booked online", "₹12,000 Cr × 60%", 7200, "#3e4fb8"),
            ("SOM", "What MMT can win by year 5", "₹7,200 Cr × 15% share", 1080, "#127a64")]
    o = []; W = 290; L = 64
    for i, (k, lab, calc, v, c) in enumerate(rows):
        y = 6 + i * 44; w = max(W * v / 29000, 12)
        o.append(T(L - 8, y + 18, k, "b", "end"))
        o.append(f'<rect x="{L}" y="{y}" width="{w:.1f}" height="26" rx="3" fill="{c}"/>')
        o.append(T(L + w + 6 if w < 150 else L + 8, y + 17, f"₹{v:,} Cr", "b" if w < 150 else "b w"))
        o.append(T(L + W + 12, y + 11, lab, "s")); o.append(T(L + W + 12, y + 24, calc, "b"))
    o.append(T(L, 196, "Year-5 revenue ≈ ₹1,080 Cr × ~10% take ≈ ₹110 Cr a year: about 1% of MMT’s FY26 revenue (~₹9,000 Cr).", "b acc"))
    o.append(T(L, 210, "The prize grows only if Dubai becomes the base for all 90 lakh Indians across the Gulf.", "s"))
    return svg(216, o)
FIGS["tam"] = tam()

def forces():
    o = ['<defs><marker id="f5" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#4a5563"/></marker></defs>', '<g class="c">']
    def box(x, y, w, h, fill, st, title, lvl, lvlc, body):
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{st}" stroke-width="1.3"/>')
        o.append(T(x + 8, y + 16, title, "b")); o.append(T(x + w - 8, y + 16, lvl, "b", "end", fill=lvlc))
        for i, l in enumerate(body.split("|")): o.append(T(x + 8, y + 31 + i * 13, l))
    H, M, Lo = "#b93a32", "#c47f17", "#127a64"
    box(240, 96, 200, 74, "#e3f0f5", "#0b5d7a", "Rivalry", "HIGH", H, "Booking.com, Expedia, Agoda,|Almosafer, Wego; all well-|funded, all discounting")
    box(240, 2, 200, 74, "#f5f7f9", "#9aa3ad", "New entrants", "MEDIUM", M, "an app is cheap to launch;|trust and airline deals|are not")
    box(240, 190, 200, 60, "#f5f7f9", "#9aa3ad", "Substitutes", "HIGH", H, "airline apps (Emirates, IndiGo),|offline agents in Karama")
    box(2, 96, 200, 74, "#f5f7f9", "#9aa3ad", "Suppliers’ power", "HIGH / MED", H, "airlines sell direct and pay|little; hotels need help,|so they pay 15–20%")
    box(478, 96, 200, 74, "#f5f7f9", "#9aa3ad", "Buyers’ power", "HIGH", H, "compare prices in seconds;|no cost to switch apps")
    for (x1, y1, x2, y2) in [(340, 76, 340, 94), (340, 190, 340, 172), (202, 133, 238, 133), (478, 133, 442, 133)]:
        o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#4a5563" stroke-width="1.6" marker-end="url(#f5)"/>')
    o.append(T(2, 206, "Verdict for a generic OTA in Dubai:", "b red")); o.append(T(2, 220, "unattractive (four forces high).", "red"))
    o.append(T(478, 200, "In the India-corridor niche:", "b grn")); o.append(T(478, 214, "rivalry and buyer power fall;", "grn")); o.append(T(478, 228, "MMT has Indian hotels, packages", "grn")); o.append(T(478, 242, "and the brand Indians know.", "grn"))
    o.append("</g>")
    return svg(254, o)
FIGS["forces"] = forces()

# ---------- Guesstimates ----------
def etree(boxes, check, rng, h=150, swing=None):
    """boxes: list of (title, sub1, sub2); last is the answer. swing: index of the orange box."""
    n = len(boxes); w = (680 - 18 * (n - 1)) / n
    o = ['<defs><marker id="gt4" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#4a5563"/></marker></defs><g class="c">']
    for i, (a, b, c) in enumerate(boxes):
        x = i * (w + 18)
        fill, st, sw = ("#e3f0f5", "#0b5d7a", 1)
        if i == swing: fill, st, sw = ("#fbf4e6", "#c47f17", 2)
        if i == n - 1: fill, st, sw = ("#e7f4f0", "#127a64", 2)
        o.append(f'<rect x="{x:.1f}" y="8" width="{w:.1f}" height="58" rx="6" fill="{fill}" stroke="{st}" stroke-width="{sw}"/>')
        o.append(T(x + w / 2, 27, a, "b grn" if i == n - 1 else "b", "middle")); o.append(T(x + w / 2, 42, b, "", "middle")); o.append(T(x + w / 2, 56, c, "", "middle"))
        if i < n - 1: o.append(f'<line x1="{x + w:.1f}" y1="37" x2="{x + w + 16:.1f}" y2="37" class="ln" marker-end="url(#gt4)"/>')
    o.append(f'<rect x="0" y="80" width="330" height="{h - 84}" rx="6" fill="#f3f3ee" stroke="#6b6a52"/>')
    for i, (s, c) in enumerate(check): o.append(T(10, 98 + i * 15, s, c))
    o.append(f'<rect x="350" y="80" width="330" height="{h - 84}" rx="6" fill="#fbf4e6" stroke="#c47f17"/>')
    for i, (s, c) in enumerate(rng): o.append(T(360, 98 + i * 15, s, c))
    o.append("</g>")
    return svg(h, o)

FIGS["gtree1"] = etree([("1.4 Cr people", "Bengaluru,", "2025"), ("× 2% a day", "take an app cab;", "× 1.8 trips = 5 L"),
                        ("× 50% Uber", "cab share", "= 2.5 L trips"), ("× 10% at peak", "busiest hour", "= 25,000 trips"),
                        ("÷ 1.33 an hour", "45-min cycle,", "÷ 60% at peak"), ("≈ 31,000", "Uber cab drivers", "a weekday")],
                       [("Check (card 5): trips per driver", "b"), ("2.5 lakh trips ÷ 31,000 drivers ≈ 8 a day:", ""),
                        ("close to a full-timer’s 10–12, so it holds.", "b grn"), ("The candidate’s 1.7 lakh implies 1 trip per", ""), ("10 residents every day, far too many.", "red")],
                       [("Range (card 6): the swing factor", "b"), ("share taking an app cab each day", ""), ("1% → ~16,000 · 3% → ~47,000 drivers", "b"),
                        ("Add autos and bikes (Uber Auto, Moto)", ""), ("for the full Uber fleet: roughly double.", "")], h=172, swing=1)

FIGS["gtree2"] = etree([("40 L", "middle-income", "15–35s (case)"), ("× 1 trip a day", "× 10% by bike", "taxi = 4 L rides"),
                        ("× 10% share", "new firm", "= 40,000 a day"), ("× 15% at peak", "busiest hour", "= 6,000 rides"),
                        ("÷ 1.5 an hour", "20-min trips +", "pickup = 4,000"), ("≈ 4,000–4,400", "bikes (riders)", "incl. 10% spare")],
                       [("Check (card 5): the rider’s side", "b"), ("20 rides × ₹60 = ₹1,200 a day, before fuel,", ""),
                        ("only at full use. Real riders do ~12 a day:", ""), ("40,000 ÷ 12 ≈ 3,300 riders. Same range.", "b grn")],
                       [("Range (card 6): the swing factor", "b"), ("peak share of daily rides", ""), ("10% → ~2,700 · 20% → ~5,300 bikes", "b"),
                        ("Owned fleet or riders’ own bikes? Most", ""), ("Indian firms don’t own the bikes.", "")], h=172, swing=3)

def peak():
    hours = list(range(6, 24)); share = [1, 4, 9, 15, 8, 5, 4, 4, 4, 4, 5, 7, 10, 11, 6, 1, 1, 1]  # % of daily bike-taxi rides, illustrative
    L, R, B = 50, 670, 150; bw = (R - L) / len(hours)
    o = [T(0, 12, "Share of a day’s bike-taxi rides in each hour, Bengaluru weekday (illustrative)", "s"),
         f'<line x1="{L}" y1="{B}" x2="{R}" y2="{B}" stroke="#4a5563"/>']
    avg = 100 / 18
    for i, (hh, s) in enumerate(zip(hours, share)):
        x = L + i * bw + 3; hgt = s * 7.2
        o.append(f'<rect x="{x:.1f}" y="{B - hgt:.1f}" width="{bw - 6:.1f}" height="{hgt:.1f}" fill="{"#b93a32" if s >= 10 else "#0b5d7a"}" rx="2"/>')
        o.append(T(x + (bw - 6) / 2, B + 13, f"{hh}", "s", "middle"))
        if s >= 10: o.append(T(x + (bw - 6) / 2, B - hgt - 4, f"{s}%", "b", "middle"))
    ya = B - avg * 7.2
    o.append(f'<line x1="{L}" y1="{ya:.1f}" x2="{R}" y2="{ya:.1f}" stroke="#127a64" stroke-width="1.5" stroke-dasharray="5 3"/>')
    o.append(T(R, ya - 5, "flat average: 5.6% an hour", "b grn halo", "end"))
    o.append(T(L + 5 * bw, 30, "peaks carry 2–3× the average: size the fleet for 9 am, not for the day", "b acc"))
    o.append(T((L + R) / 2, B + 28, "hour of the day", "s", "middle"))
    return svg(182, o)
FIGS["peak"] = peak()

# teardown figures live in their own file
import figs_teardowns  # noqa: E402,F401
import figs_tech  # noqa: E402,F401
