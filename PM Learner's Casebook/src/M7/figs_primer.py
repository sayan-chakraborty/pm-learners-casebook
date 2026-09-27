"""Primer figures for M7; imported at the end of m7_figs.py (shares its helpers and FIGS)."""
from m7_figs import FIGS, svg, T, lines, hbars, waterfall  # noqa: F401

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


def money():
    o = [MK,
         '<line x1="444" y1="10" x2="474" y2="10" class="money"/>', T(480, 14, "money", "s"),
         '<line x1="526" y1="10" x2="556" y2="10" class="msg"/>', T(562, 14, "the service", "s"),
         box(6, 26, 150, 50, *G, [("The user", "b"), ("pays for herself", "s")]),
         box(6, 88, 150, 50, *G, [("Parents", "b"), ("pay for a child’s course", "s")]),
         box(6, 150, 150, 50, *GR, [("Employers", "b"), ("pay for staff wellness", "s")]),
         box(6, 212, 150, 50, *GR, [("Insurers", "b"), ("pay for treatment", "s")]),
         box(262, 104, 156, 86, *B, [("The app", "b"), ("Practo, Cult.fit,", ""), ("HealthifyMe, PW:", ""), ("books, delivers, bills", "s")]),
         box(524, 34, 150, 62, *P, [("Experts", "b"), ("doctors, coaches,", ""), ("teachers: scarce", "s")]),
         box(524, 118, 150, 62, *A, [("Places", "b"), ("clinics, gyms, labs,", ""), ("pharmacies, centres", "s")]),
         box(524, 202, 150, 58, *I, [("Content and AI", "b"), ("videos, plans, a bot", "s")]),
         # money in
         '<path d="M156,51 C210,51 230,112 258,120" class="money" marker-end="url(#pg)"/>',
         '<path d="M156,113 C205,113 230,136 258,138" class="money" marker-end="url(#pg)"/>',
         '<path d="M156,175 C205,175 230,158 258,156" class="money" marker-end="url(#pg)"/>',
         '<path d="M156,237 C210,237 232,184 258,174" class="money" marker-end="url(#pg)"/>',
         T(166, 44, "₹999 a month", "b grn halo"), T(166, 106, "₹4,000 a year", "b grn halo"),
         T(166, 170, "a yearly contract", "b grn halo"), T(166, 232, "a claim or cashless", "b grn halo"),
         # money out
         '<line x1="418" y1="122" x2="520" y2="72" class="money" marker-end="url(#pg)"/>',
         '<line x1="418" y1="148" x2="520" y2="148" class="money" marker-end="url(#pg)"/>',
         '<line x1="418" y1="176" x2="520" y2="222" class="money" marker-end="url(#pg)"/>',
         T(470, 86, "salary or fee", "b grn halo", "middle"), T(470, 99, "per consult", "grn halo", "middle"),
         T(470, 142, "rent, franchise", "b grn halo", "middle"),
         T(470, 214, "servers, AI", "b grn halo", "middle"), T(470, 227, "per use", "grn halo", "middle"),
         '<path d="M599,262 C560,290 120,292 60,264" class="msg" marker-end="url(#pa)"/>',
         T(340, 284, "a consult, a class, a lecture, a diet plan: delivered to the user", "b halo", "middle"),
         ]
    return svg(296, o)
FIGS["money"] = money()

FIGS["coachwf"] = waterfall([("Paid a|month", 999, "start"), ("GST|18% inside", 152, "down"), ("Payment|fee", 25, "down"),
                             ("Coach’s|time", 400, "down"), ("Tech|and AI", 60, "down"), ("Marketing|(spread)", 250, "down"),
                             ("Left over", 0, "total")],
                            note="A ₹999-a-month coaching plan, per user, per month (illustrative).|The coach earns ₹60,000 a month and looks after 150 clients: ₹60,000 ÷ 150 = ₹400 a client.", h=246, top=44)


def gym():
    L, R, Tp, Bt = 70, 660, 30, 196
    X = lambda m: L + (R - L) * m / 600
    Y = lambda r: Bt - (Bt - Tp) * r / 11
    o = [f'<line x1="{L}" y1="{Bt}" x2="{R}" y2="{Bt}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{Bt}" stroke="#4a5563"/>']
    for v in (0, 2, 4, 6, 8, 10):
        o.append(T(L - 6, Y(v) + 4, f"₹{v}L", "s", "end"))
        if v: o.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{R}" y2="{Y(v):.1f}" stroke="#eef0f2"/>')
    for m in (0, 100, 200, 300, 400, 500, 600): o.append(T(X(m), Bt + 15, str(m), "s", "middle"))
    o.append(f'<rect x="{X(500):.1f}" y="{Tp}" width="{X(600) - X(500):.1f}" height="{Bt - Tp}" fill="#fcecea"/>')
    o.append(T(X(550), Tp + 14, "no room:", "b red", "middle")); o.append(T(X(550), Tp + 27, "classes full", "red", "middle"))
    o.append(f'<line x1="{L}" y1="{Y(7.5):.1f}" x2="{R}" y2="{Y(7.5):.1f}" stroke="#b93a32" stroke-width="2.4"/>')
    o.append(T(X(20), Y(7.5) - 7, "monthly cost: rent ₹4L + 6 trainers ₹2.1L + upkeep ₹1.4L = ₹7.5L", "b red halo"))
    o.append(f'<line x1="{X(0):.1f}" y1="{Y(0):.1f}" x2="{X(600):.1f}" y2="{Y(600 * 0.017):.1f}" stroke="#127a64" stroke-width="2.6"/>')
    o.append(T(X(110), Y(110 * 0.017) + 20, "income: ₹1,700 a member a month (after GST)", "b grn halo", "start"))
    bx = 7.5 / 0.017
    o.append(f'<line x1="{X(bx):.1f}" y1="{Y(7.5):.1f}" x2="{X(bx):.1f}" y2="{Bt}" stroke="#0b5d7a" stroke-dasharray="4 3"/>')
    o.append(f'<circle cx="{X(bx):.1f}" cy="{Y(7.5):.1f}" r="5" fill="#0b5d7a"/>')
    o.append(T(X(bx) + 8, Y(4.6), "break-even:", "b acc halo"))
    o.append(T(X(bx) + 8, Y(4.6) + 13, "₹7.5L ÷ ₹1,700", "b acc halo"))
    o.append(T(X(bx) + 8, Y(4.6) + 26, "≈ 441 members", "b acc halo"))
    o.append(T(0, 14, "One centre, one month (illustrative). Room for about 520 members: 25 a class × 10 classes × 25 days ÷ 12 visits.", "b"))
    o.append(T((L + R) / 2, Bt + 30, "paying members", "s", "middle"))
    return svg(232, o)
FIGS["gym"] = gym()


def funnel():
    rows = [("Watch a free lecture", 100, "on YouTube, this month", "#9fb8c4"),
            ("Install the app", 20, "for notes, tests, doubts", "#5f8fa3"),
            ("Buy an online batch", 4, "₹4,000 a year each: ₹16,000", "#0b5d7a"),
            ("Join an offline centre", 0.4, "₹80,000 a year each: ₹32,000", "#127a64")]
    o = [T(0, 12, "Out of 100 students who watch a free lecture (illustrative)", "b")]
    for i, (lab, v, note, col) in enumerate(rows):
        y = 22 + i * 30
        o.append(T(170, y + 16, lab, "b", "end"))
        w = max(3, 300 * v / 100)
        o.append(f'<rect x="180" y="{y + 3}" width="{w:.1f}" height="19" rx="2" fill="{col}"/>')
        o.append(T(186 + w, y + 17, f"{v:g}", "b"))
        o.append(T(500, y + 17, note, "s"))
    o.append(T(0, 152, "The 0.4 offline students bring in twice the money of the 4 online ones. Free video is the shop window; the classroom is the till.", "b acc"))
    return svg(162, o)
FIGS["funnel"] = funnel()


def cliff():
    L, R, Tp, Bt = 40, 670, 30, 178
    m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    su = [100, 58, 46, 40, 38, 36, 35, 34, 38, 44, 40, 30]
    act = [100, 74, 55, 46, 42, 40, 39, 38, 40, 44, 43, 38]
    bw = (R - L) / 12
    X = lambda i: L + bw * i + bw / 2
    Y = lambda v: Bt - (Bt - Tp) * v / 110
    o = [f'<line x1="{L}" y1="{Bt}" x2="{R}" y2="{Bt}" stroke="#4a5563"/>']
    for i, (lab, v) in enumerate(zip(m, su)):
        col = "#c47f17" if i == 0 else "#f3d29a"
        o.append(f'<rect x="{X(i) - bw * 0.32:.1f}" y="{Y(v):.1f}" width="{bw * 0.64:.1f}" height="{Bt - Y(v):.1f}" fill="{col}"/>')
        o.append(T(X(i), Bt + 15, lab, "s", "middle"))
    d = " ".join(f"{'M' if i == 0 else 'L'}{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(act))
    o.append(f'<path d="{d}" fill="none" stroke="#0b5d7a" stroke-width="2.6"/>')
    for i, v in enumerate(act): o.append(f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="3" fill="#0b5d7a"/>')
    o.append(T(X(0) + 26, Y(100) + 4, "January sign-ups = 100", "b amb halo"))
    o.append(T(X(2) + 10, Y(55) - 10, "people logging in a week", "b acc halo"))
    o.append(T(X(3) - 6, Y(28), "by April, sign-ups are 40", "b halo"))
    o.append(T(X(3) - 6, Y(28) + 13, "and weekly users half of January", "halo"))
    o.append(T(X(9), Y(44) - 12, "a smaller wave: festive season", "s", "middle"))
    o.append(T(L, 14, "A fitness app’s year: bars are sign-ups by month, the line is people active in the week (index, January = 100; illustrative)", "b"))
    return svg(200, o)
FIGS["cliff"] = cliff()


FIGS["players"] = hbars([("PhysicsWallah", 3900, "FY26 · loss ₹24 Cr, operating profit ₹549 Cr"),
                         ("Tata 1mg", 2392, "FY25 · loss ₹276 Cr"),
                         ("Cult.fit", 1216, "FY25 · loss ₹481 Cr (FY26: ₹252 Cr)"),
                         ("Practo", 234, "FY25 · first full-year operating profit"),
                         ("HealthifyMe", 178, "FY25 · loss ₹4.7 Cr")], 3900, lw=110, unit=" Cr", fmt="₹{:,}",
                        colors=["#127a64", "#0b5d7a", "#c47f17", "#0b5d7a", "#127a64"],
                        note="Revenue from operations, latest full year (₹ crore)")


def timeline():
    pts = [(52, "Mar 2020", "Telemedicine", ["Doctors may", "consult on video", "and phone:", "guidelines issued"], "#0b5d7a"),
           (148, "2020–21", "Classes online", ["Schools shut;", "edtech sign-ups", "jump; Byju’s", "buys rivals"], "#c47f17"),
           (244, "Sep 2021", "ABDM", ["ABHA health IDs:", "97.8 crore by", "Sep 2026, 121", "crore records"], "#3e4fb8"),
           (340, "2022–24", "Byju’s falls", ["Schools reopen;", "refunds, unpaid", "loans; insolvency", "in July 2024"], "#b93a32"),
           (436, "Jan 2024", "Coaching rules", ["No coaching", "under 16; no", "rank-guarantee", "adverts"], "#b93a32"),
           (532, "Nov 2025", "PW lists; DPDP", ["PhysicsWallah’s", "IPO; data rules", "for health and", "children notified"], "#127a64"),
           (628, "2025–26", "GLP-1 drugs", ["Weight-loss jabs", "reach India;", "cheaper generics", "from 2026"], "#7c3aa6")]
    o = ['<line x1="8" y1="60" x2="674" y2="60" stroke="#4a5563" stroke-width="2"/><g class="c">']
    for x, d, h, ls, col in pts:
        o.append(f'<circle cx="{x}" cy="60" r="6.5" fill="{col}"/>')
        o.append(T(x, 46, d, "b", "middle"))
        o.append(T(x - 46, 80, h, "b", "start", fill=col))
        for i, l in enumerate(ls): o.append(T(x - 46, 94 + i * 13, l))
    o.append("</g>")
    o.append(T(8, 16, "Each turning point changed where care or teaching happens, who is allowed to sell it, or what the product can promise.", "s"))
    return svg(150, o)
FIGS["timeline"] = timeline()


def outcome():
    o = [T(0, 12, "What the user wants", "b"), T(360, 12, "What the app can show every day", "b")]
    # left: weight, slow and noisy
    L, Rr, Tp, Bt = 36, 320, 26, 150
    w = [78.0, 78.4, 77.6, 77.9, 77.1, 77.5, 76.6, 76.9, 76.2, 76.4, 75.8, 76.0, 75.4]
    X = lambda i: L + (Rr - L) * i / 12
    Y = lambda v: Bt - (Bt - Tp) * (v - 74.5) / 4.5
    o.append(f'<line x1="{L}" y1="{Bt}" x2="{Rr}" y2="{Bt}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{Bt}" stroke="#4a5563"/>')
    for v in (75, 77, 79):
        if v <= 79: o.append(T(L - 4, Y(v) + 4, f"{v}", "s", "end"))
    d = " ".join(f"{'M' if i == 0 else 'L'}{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(w))
    o.append(f'<path d="{d}" fill="none" stroke="#b93a32" stroke-width="2.4"/>')
    o.append(T(L, Bt + 15, "week 0", "s")); o.append(T(Rr, Bt + 15, "week 12", "s", "end"))
    o.append(T(L + 8, Bt - 22, "weight, kg: −2.6 kg in 12 weeks,", "b red"))
    o.append(T(L + 8, Bt - 9, "and up in 5 of those weeks", "red"))
    # right: streak and logged days
    L2, R2 = 380, 670
    X2 = lambda i: L2 + (R2 - L2) * i / 12
    Y2 = lambda v: Bt - (Bt - Tp) * v / 84
    o.append(f'<line x1="{L2}" y1="{Bt}" x2="{R2}" y2="{Bt}" stroke="#4a5563"/><line x1="{L2}" y1="{Tp}" x2="{L2}" y2="{Bt}" stroke="#4a5563"/>')
    for v in (0, 42, 84): o.append(T(L2 - 4, Y2(v) + 4, str(v), "s", "end"))
    d = " ".join(f"{'M' if i == 0 else 'L'}{X2(i):.1f},{Y2(i * 7):.1f}" for i in range(13))
    o.append(f'<path d="{d}" fill="none" stroke="#127a64" stroke-width="2.6"/>')
    for i in range(13): o.append(f'<circle cx="{X2(i):.1f}" cy="{Y2(i * 7):.1f}" r="2.6" fill="#127a64"/>')
    o.append(T(L2 + 8, Tp + 6, "days logged in a row: goes up", "b grn"))
    o.append(T(L2 + 8, Tp + 19, "every single day she shows up", "grn"))
    o.append(T(L2, Bt + 15, "week 0", "s")); o.append(T(R2, Bt + 15, "week 12", "s", "end"))
    return svg(172, o)
FIGS["outcome"] = outcome()
