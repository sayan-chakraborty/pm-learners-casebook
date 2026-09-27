"""M9 guesstimate figures; imported at the end of m9_figs.py."""
from m9_figs import FIGS, svg, T, lines, hbars, waterfall, loop, two_by_two, seq, strip  # noqa: F401
from figlib import *  # noqa: F401,F403
from figlib import box, MK, G, B, A, GR, R, P, I, vbars, arr, curves, etree, stacks

# ---------- G9.1 food-delivery users ----------
FIGS["stripg91"] = strip([("Unit", "monthly users, this app"), ("Approach", "people → orderers"), ("Tree", "5 steps"),
                          ("Numbers", "a reason each"), ("Check", "Brazil’s iFood"), ("Range", "3–8 million")])

FIGS["funnelg91"] = hbars([("Population", 100, "the interviewer’s country"), ("Urban, aged 15+", 55, "70% urban × 78% over 15"),
                           ("Smartphone + digital pay", 38, "about 7 in 10 urban adults"), ("Order delivery monthly", 13, "about a third of them: the whole market"),
                           ("Use this app monthly", 5, "if it has about 40% of orders (No. 2 of 3)")], 100,
                          lw=190, fmt="{}", unit=" mn", colors=["#9aa3ad", "#0b5d7a", "#0b5d7a", "#c47f17", "#127a64"],
                          note="From people to this app’s monthly users (illustrative)")

FIGS["gtreeg91"] = etree([("100 mn", "people", "(given)"), ("× 55%", "urban, 15+", "= 55 mn"), ("× 70%", "phone + digital", "pay = 38 mn"),
                          ("× 35%", "order monthly", "= 13 mn"), ("× 40%", "this app’s", "share"), ("≈ 5 mn", "monthly users", "of this app")],
                         [("Check against Brazil (iFood, 2025):", "b"), ("12 crore orders a month ÷ 21 crore people", ""), ("≈ 0.57 orders per person a month.", ""),
                          ("Ours: 13 mn × 2 orders ÷ 100 mn = 0.26,", ""), ("about half of Brazil’s, the most mature market.", "")],
                         [("Range: 3–8 mn monthly users of this app", "b"), ("Whole market: 10–20 mn monthly orderers.", ""), ("Swing factors: how often people order,", ""),
                          ("and whether this app leads or trails.", "")], h=172, swing=3)

# ---------- G9.2 Swiggy orders per hour ----------
FIGS["stripg92"] = strip([("Unit", "average and peak hour"), ("Approach", "users × orders"), ("Tree", "per day, then by hour"),
                          ("Numbers", "published users"), ("Check", "Swiggy’s results"), ("Range", "50k avg, 1.5L peak")])


def hourly92():
    share = [1.0, 0.5, 0.3, 0.2, 0.2, 0.3, 0.8, 1.8, 3.2, 3.8, 3.6, 4.2, 6.8, 8.0, 6.4, 3.6, 3.0, 3.4, 4.2, 6.0, 9.6, 12.6, 10.4, 5.6]
    tot = sum(share); share = [s / tot * 100 for s in share]
    day = 12.6  # lakh orders a day
    vals = [s / 100 * day * 100000 for s in share]
    L, R, Tp, Bt = 60, 670, 24, 164
    mx = 170000
    Y = lambda v: Bt - (Bt - Tp) * v / mx
    bw = (R - L) / 24
    o = [T(0, 12, "Swiggy food orders in each hour of an average day, India (hour-of-day split illustrative; daily total from results)", "b")]
    for v in (0, 50000, 100000, 150000):
        o.append(T(L - 6, Y(v) + 4, f"{v // 1000}k" if v else "0", "s", "end"))
        o.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{R}" y2="{Y(v):.1f}" stroke="#eef0f2"/>')
    for i, v in enumerate(vals):
        x = L + i * bw + 2
        col = "#b93a32" if v > 100000 else ("#0b5d7a" if v > 30000 else "#9aa3ad")
        o.append(f'<rect x="{x:.1f}" y="{Y(v):.1f}" width="{bw - 4:.1f}" height="{Bt - Y(v):.1f}" fill="{col}" rx="1.5"/>')
        if i % 3 == 0: o.append(T(x + bw / 2 - 2, Bt + 14, f"{i}:00", "s", "middle"))
    avg = day * 100000 / 24
    o.append(f'<line x1="{L}" y1="{Y(avg):.1f}" x2="{R}" y2="{Y(avg):.1f}" stroke="#127a64" stroke-width="2" stroke-dasharray="6 4"/>')
    o.append(T(L + 6, Y(avg) - 5, f"the day ÷ 24 ≈ {avg / 1000:.0f}k an hour", "b grn halo"))
    pk = max(vals); ip = vals.index(pk)
    o.append(T(L + ip * bw - 6, Y(pk) + 4, f"9–10 pm ≈ {pk / 1000:.0f}k, {pk / avg:.1f}× the average", "b red halo", "end"))
    o.append(f'<line x1="{L}" y1="{Bt}" x2="{R}" y2="{Bt}" stroke="#4a5563"/>')
    return svg(186, o)
FIGS["hourly92"] = hourly92()

FIGS["gtreeg92"] = etree([("1.9 crore", "food users a", "month (Swiggy)"), ("× 2 orders", "each a month", "= 3.8 crore"), ("÷ 30 days", "= 12.7 lakh", "a day"),
                          ("÷ 24 hours", "= 53,000", "average"), ("× 3 at 9 pm", "the dinner", "peak"), ("≈ 1.6 lakh", "orders in the", "peak hour")],
                         [("Check: Swiggy, Apr–Jun 2026", "b"), ("11.45 crore food orders ÷ 91 days", ""), ("= 12.6 lakh a day = 52,000 an hour.", ""),
                          ("Tree: 53,000. Casebook: 73,000 (too high).", "")],
                         [("Range: 45–60k an hour on average;", "b"), ("1.2–1.8 lakh in the dinner peak.", ""), ("Swing factors: orders per user,", ""),
                          ("and how sharp the peak is (rain, IPL).", "")], h=158, swing=4)
