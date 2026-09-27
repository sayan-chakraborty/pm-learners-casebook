"""Case and guesstimate figures for M6; imported at the end of m6_figs.py."""
from m6_figs import FIGS, svg, T, lines, strip, hbars  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R, P  # noqa: F401


def curves(series, months, L=46, R=520, Tp=14, Bt=170, h=196, ymax=100, notes=()):
    """series: (label, values, colour, label_y_offset); plotted 0..ymax."""
    X = lambda i: L + (R - L) * i / (len(months) - 1)
    Y = lambda v: Bt - (Bt - Tp) * v / ymax
    o = [f'<line x1="{L}" y1="{Bt}" x2="{R}" y2="{Bt}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{Bt}" stroke="#4a5563"/>']
    for v in range(0, ymax + 1, 25):
        o.append(T(L - 6, Y(v) + 4, str(v), "s", "end"))
        if v: o.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{R}" y2="{Y(v):.1f}" stroke="#eef0f2"/>')
    for i, m in enumerate(months): o.append(T(X(i), Bt + 15, m, "s", "middle"))
    for lab, vals, col, dy in series:
        d = " ".join(f"{'M' if i == 0 else 'L'}{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(vals))
        o.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2.6"/>')
        for i, v in enumerate(vals): o.append(f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="2.8" fill="{col}"/>')
        o.append(T(R + 8, Y(vals[-1]) + 4 + dy, f"{lab}: {vals[-1]}", "b", fill=col))
    for x, y, s, c in notes: o.append(T(x, y, s, c))
    return svg(h, o)


# ---------- Case 6.1 ----------
FIGS["strip61"] = strip([("Clarify", "loyalty = renewals"), ("Find the leak", "follow each cohort"), ("Size", "₹ at stake"),
                         ("Who", "the IPL joiner"), ("Bets", "scored with numbers"), ("Measure", "watching at day 60")])

FIGS["retcurves"] = curves(
    [("Joined in January", [100, 82, 74, 70, 68, 66, 65, 65, 65], "#127a64", -4),
     ("Joined for the IPL", [100, 94, 90, 42, 35, 31, 28, 27, 27], "#b93a32", 4),
     ("A failing product", [100, 55, 32, 20, 13, 8, 5, 3, 2], "#9aa3ad", -4)],
    ["start", "+1", "+2", "+3", "+4", "+5", "+6", "+7", "+8"],
    notes=[(226, 30, "June: the season ends and two in three", "b red"), (226, 43, "IPL joiners leave within a month", "red")], h=196)


def cohort():
    rows = [("Jan 2025", [100, 80, 72, 69, 67, 66], None), ("Mar 2025 (IPL)", [100, 93, 90, 40, 33, 30], 3),
            ("Jul 2025", [100, 78, 70, 66, 64, 63], None), ("Jan 2026", [100, 83, 76, 72, 70, 69], None),
            ("Mar 2026 (IPL)", [100, 94, 91, 55, 48, 45], 3)]
    o = [T(0, 14, "Share of each joining group still watching weekly (%)", "b")]
    x0, cw, rh, y0 = 150, 84, 26, 30
    for j in range(6): o.append(T(x0 + j * cw + cw / 2, y0 + 10, "start" if j == 0 else f"month {j}", "b", "middle"))
    for i, (lab, vals, jun) in enumerate(rows):
        y = y0 + 18 + i * rh
        o.append(T(x0 - 8, y + 17, lab, "b", "end"))
        for j, v in enumerate(vals):
            a = 0.12 + 0.88 * (v - 25) / 75
            col = f"rgba(11,93,122,{a:.2f})"
            o.append(f'<rect x="{x0 + j * cw + 1}" y="{y}" width="{cw - 2}" height="{rh - 2}" fill="{col}"/>')
            o.append(T(x0 + j * cw + cw / 2, y + 17, str(v), "b w" if a > 0.55 else "b", "middle"))
        if jun: o.append(f'<rect x="{x0 + jun * cw + 1}" y="{y}" width="{cw - 2}" height="{rh - 2}" fill="none" stroke="#b93a32" stroke-width="2.2"/>')
    yb = y0 + 18 + len(rows) * rh + 16
    o.append(T(x0, yb, "Red outline: June, when the season ends. 2026 IPL joiners: 55 kept, against 40 a year earlier.", "b red"))
    return svg(yb + 6, o)
FIGS["cohort"] = cohort()


# ---------- Case 6.2 ----------
FIGS["strip62"] = strip([("Clarify", "is counting same?"), ("Split", "into three parts"), ("Rule out", "season, catalogue"),
                         ("Find where", "light vs heavy"), ("Cause", "free rival"), ("Fix", "free, quick"), ("Measure", "weekly watchers")])


def journey62():
    o = [MK, '<g class="c">']
    o.append(box(10, 14, 120, 40, *B, [("Login", "b")]))
    o.append(box(10, 84, 120, 40, *B, [("Sign up", "b")]))
    o.append(box(250, 14, 130, 40, *B, [("Recommendations", "b")]))
    o.append(box(250, 84, 130, 40, *B, [("Search", "b")]))
    o.append(box(500, 44, 120, 50, *G, [("Watch video", "b")]))
    for y1 in (34, 104):
        for y2 in (34, 104):
            o.append(f'<line x1="130" y1="{y1}" x2="246" y2="{y2}" class="ln" marker-end="url(#pa)"/>')
    for y in (34, 104): o.append(f'<line x1="380" y1="{y}" x2="496" y2="69" class="ln" marker-end="url(#pa)"/>')
    for x, s in [(70, "log-in success, new sign-ups"), (315, "row clicks, searches with no result"), (560, "starts, share reaching 70%")]:
        o.append(T(x, 146, s, "s", "middle"))
    o.append("</g>")
    return svg(154, o)
FIGS["journey62"] = journey62()


def viewtree62():
    o = [MK, '<g class="c">']
    o.append(box(250, 6, 180, 46, *B, [("Views a day", "b"), ("90 lakh → 72 lakh (−20%)", "")]))
    parts = [(20, "People watching", "1 crore × 1.5 × 60%", "if 80 lakh watch:", "someone went elsewhere", R),
             (250, "Titles started each", "1.5 per viewer", "if 1.2 starts:", "catalogue or home screen", A),
             (480, "Share finished to 70%", "60% of starts", "if 48% finish:", "longer shows, autoplay", A)]
    for x, h, s, n1, n2, col in parts:
        o.append(f'<line x1="340" y1="52" x2="{x + 90}" y2="76" class="ln" marker-end="url(#pa)"/>')
        o.append(box(x, 78, 180, 44, "#e3f0f5", "#0b5d7a", [(h, "b"), (s, "")]))
        o.append(box(x, 132, 180, 44, *col, [(n1, "b"), (n2, "")]))
    o.append(T(340, 198, "The interviewer’s data: people watching −15%, starts slightly down, finish rate flat → people left.", "b acc", "middle"))
    o.append("</g>")
    return svg(206, o)
FIGS["viewtree62"] = viewtree62()


# ---------- Case 6.3 ----------
FIGS["strip63"] = strip([("Clarify", "what exists today"), ("Segments", "by what they’d pay"), ("Price ladder", "us vs rivals"),
                         ("Test", "would you pay ₹X?"), ("Count", "who moves down"), ("Decide", "and guard it")])


def ladder63():
    L, R = 150, 660
    X = lambda v: L + (R - L) * v / 700
    rows = [("Netflix", [(149, "Mobile"), (199, "Basic"), (499, "Standard"), (649, "Premium")], "#b93a32"),
            ("JioHotstar", [(79, "Mobile"), (149, "Super"), (299, "Premium")], "#0b5d7a"),
            ("Amazon Prime", [(125, "Prime, yearly ÷ 12"), (299, "Prime, monthly")], "#c47f17")]
    o = [f'<line x1="{L}" y1="176" x2="{R}" y2="176" stroke="#4a5563"/>']
    for v in range(0, 701, 100):
        o.append(T(X(v), 192, f"₹{v}", "s", "middle")); o.append(f'<line x1="{X(v):.1f}" y1="8" x2="{X(v):.1f}" y2="176" stroke="#eef0f2"/>')
    for i, (name, pts, col) in enumerate(rows):
        y = 28 + i * 56
        o.append(T(L - 10, y + 4, name, "b", "end"))
        o.append(f'<line x1="{X(pts[0][0]):.1f}" y1="{y}" x2="{X(pts[-1][0]):.1f}" y2="{y}" stroke="{col}" stroke-width="2"/>')
        for j, (v, lab) in enumerate(pts):
            o.append(f'<circle cx="{X(v):.1f}" cy="{y}" r="6" fill="{col}"/>')
            near_next = j + 1 < len(pts) and pts[j + 1][0] - v < 70
            near_prev = j > 0 and v - pts[j - 1][0] < 70
            anc, dx = ("end", -3) if near_next else (("start", 3) if near_prev else ("middle", 0))
            o.append(T(X(v) + dx, y - 11, f"₹{v}", "b", anc))
            o.append(T(X(v) + dx, y + 20, lab, "s", anc))
    return svg(198, o)
FIGS["ladder63"] = ladder63()


def share63():
    o = [MK, '<g class="c">']
    o.append(box(4, 4, 326, 30, *G, [("A · “Get your own plan” at ₹149", "b")]))
    o.append(box(350, 4, 326, 30, *A, [("B · Extra member at ₹99", "b")]))
    left = [("1 crore sharer households", ""), ("× 25% buy their own plan", ""), ("= 25 lakh × ₹149", ""), ("= ₹37 Cr a month", "b grn")]
    right = [("1 crore sharer households", ""), ("× 45% pay to stay: 45 lakh × ₹99 = ₹45 Cr", ""),
             ("− 10 lakh ₹499 households drop to ₹298:", "red"), ("   10 lakh × ₹201 = ₹20 Cr lost", "red"), ("= ₹25 Cr a month", "b red")]
    for i, (s, c) in enumerate(left): o.append(T(14, 56 + i * 17, s, c))
    for i, (s, c) in enumerate(right): o.append(T(360, 56 + i * 17, s, c))
    o.append(f'<line x1="340" y1="40" x2="340" y2="140" stroke="#c3cad2"/>')
    o.append(T(340, 158, "More people pay under B, but less money comes in: the cheaper option is also chosen by existing members.", "b acc", "middle"))
    o.append("</g>")
    return svg(166, o)
FIGS["share63"] = share63()


def wtp63():
    prices = [99, 149, 199, 249]; yes = [70, 45, 25, 12]
    L, R, Tp, Bt = 60, 520, 20, 150
    o = [f'<line x1="{L}" y1="{Bt}" x2="{R}" y2="{Bt}" stroke="#4a5563"/>']
    bw = 60; gap = (R - L) / 4
    Y = lambda v: Bt - (Bt - Tp) * v / 100
    Yr = lambda v: Bt - (Bt - Tp) * v / 8000
    pts = []
    for i, (p, s) in enumerate(zip(prices, yes)):
        cx = L + gap * (i + 0.5)
        o.append(f'<rect x="{cx - bw / 2:.1f}" y="{Y(s):.1f}" width="{bw}" height="{Bt - Y(s):.1f}" fill="#9fb8c4" rx="2"/>')
        o.append(T(cx, Bt - 5, f"{s}%", "b", "middle"))
        o.append(T(cx, Bt + 15, f"₹{p}", "b", "middle"))
        pts.append((cx, Yr(p * s), p * s))
    d = " ".join(f"{'M' if i == 0 else 'L'}{x:.1f},{y:.1f}" for i, (x, y, _) in enumerate(pts))
    o.append(f'<path d="{d}" fill="none" stroke="#127a64" stroke-width="2.6"/>')
    for x, y, r in pts:
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="#127a64"/>')
        o.append(T(x + 8, y - 6, f"₹{r:,}", "b grn halo"))
    o.append(T(536, 40, "green line: revenue", "b grn")); o.append(T(536, 54, "per 100 sharers", "grn"))
    o.append(T(536, 84, "grey bars: share who", "b")); o.append(T(536, 98, "would pay that price", ""))
    o.append(T(536, 128, "₹99 → ₹149: fewer", "b acc")); o.append(T(536, 142, "people, same money", "acc"))
    return svg(170, o)
FIGS["wtp63"] = wtp63()


# ---------- Guesstimates ----------
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


FIGS["stripg61"] = strip([("Unit", "ads only, US"), ("Approach", "from minutes"), ("Tree", "viewers × minutes"),
                          ("Numbers", "a reason each"), ("Check", "company, per person"), ("Range", "ads per minute")])
FIGS["stripg62"] = strip([("Unit", "triers vs monthly"), ("Approach", "speakers down"), ("Tree", "online → watch"),
                          ("Numbers", "free rival"), ("Check", "per language"), ("Range", "who stays")])

FIGS["gtree61"] = etree([("330 mn people", "× 75% watch", "= 250 mn"), ("× 60 min", "each a day", "= 15 bn min"),
                         ("× 85% with ads", "(not Premium)", "= 12.75 bn min"), ("× 1 ad / 4 min", "long + Shorts", "= 3.2 bn ads"),
                         ("× $15 per 1,000", "phone cheap,", "TV dear"), ("≈ $48 mn", "a day", "range $30–75 mn")],
                        [("Check (card 5): two ways", "b"), ("YouTube ads ≈ $40 bn (2025) × ~half US", ""),
                         ("÷ 365 ≈ $55 mn a day. Close.", "b grn"), ("Per viewer: 19¢ a day, ~$70 a year.", ""),
                         ("Casebook: $20 mn a day, too low.", "red")],
                        [("Range (card 6): the swing factors", "b"), ("ads per minute and price per 1,000", ""),
                         ("1 ad / 5 min, $12 → ~$31 mn", "b"), ("1 ad / 3 min, $18 → ~$77 mn", "b"), ("TV viewing pushes prices up", "")],
                        h=172, swing=4)

FIGS["gtree62"] = etree([("≈ 9 Cr", "understand", "Bhojpuri"), ("× 55% online", "= 5 Cr", ""), ("× 80% watch", "short videos", "= 4 Cr"),
                         ("× 25% try", "= 1 Cr", "triers"), ("× 5–10% stay", "vs YouTube,", "Moj (free)"), ("20–40 L", "monthly users", "in year 3")],
                        [("Check (card 5)", "b"), ("Census 2011: 5.1 Cr Bhojpuri mother tongue.", ""),
                         ("ShareChat + Moj ≈ 15 Cr across 15+", ""), ("languages ≈ 1 Cr a language. Below it.", "b grn")],
                        [("Range (card 6): the swing factor", "b"), ("share who stay after trying", ""),
                         ("5% → 20 L · 10% → 40 L", "b"), ("Exclusive films raise it.", "")],
                        h=152, swing=4)
