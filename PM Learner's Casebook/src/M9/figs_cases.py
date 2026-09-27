"""M9 case figures (9.1 voter turnout, 9.2 Apple speaker pricing, 9.3 Tata loyalty); imported at the end of m9_figs.py."""
from m9_figs import FIGS, svg, T, lines, hbars, waterfall, loop, two_by_two, seq, strip  # noqa: F401
from figlib import *  # noqa: F401,F403
from figlib import box, MK, G, B, A, GR, R, P, I, vbars, arr, curves, etree, stacks

# ================= Case 9.1 voter turnout =================
FIGS["strip91"] = strip([("Clarify", "today, goal, limits"), ("Why", "can’t, won’t, forgot"), ("Journey", "where people drop"),
                         ("Nudge", "Easy, Attractive…"), ("Build first", "four features"), ("Measure", "lift vs a holdout")])

FIGS["why91"] = hbars([("Busy or forgot on the day", 34, "timing: fixable with a plan and a reminder"),
                       ("Don’t know the candidates", 24, "information: fixable, but carefully"),
                       ("Unsure how to register or where", 20, "friction: the easiest to remove"),
                       ("“My vote won’t count”", 14, "belief: the hardest to shift"),
                       ("Not interested", 8, "an app alone won’t change this")], 40,
                      lw=200, unit="%", colors=["#c47f17", "#0b5d7a", "#127a64", "#b93a32", "#9aa3ad"],
                      note="Why young people on the roll didn’t vote last time: share of reasons given (illustrative survey)")


def journey91():
    steps = [("On the roll?", "registered before|the deadline", 100, 82), ("Which booth?", "knows where|and when", 82, 70),
             ("Who’s standing?", "knows enough|to choose", 70, 62), ("A plan", "knows when|she will go", 62, 46),
             ("At the booth", "gets there|and votes", 46, 40)]
    o = [MK, '<g class="c">']
    w = 128; gap = 10
    for i, (t, sub, a, b) in enumerate(steps):
        x = i * (w + gap)
        o.append(f'<polygon points="{x},30 {x + w - 10},30 {x + w},52 {x + w - 10},74 {x},74 {x + 10 if i else x},52" fill="#e3f0f5" stroke="#0b5d7a" stroke-width="1.2"/>')
        o.append(T(x + w / 2 + 3, 49, t, "b", "middle"))
        o.append(T(x + w / 2 + 3, 63, sub.split("|")[0], "s", "middle"))
        hh = 90 * b / 100
        col = "#b93a32" if (a - b) >= 15 else "#0b5d7a"
        o.append(f'<rect x="{x + 30}" y="{190 - hh:.1f}" width="{w - 60}" height="{hh:.1f}" fill="{col if (a - b) >= 15 else "#0b5d7a"}" rx="2"/>')
        o.append(T(x + w / 2, 186 - hh, f"{b} left", "b", "middle"))
        o.append(T(x + w / 2, 206, f"−{a - b} here", "b red" if (a - b) >= 15 else "s", "middle"))
    o.append('<line x1="0" y1="190" x2="680" y2="190" stroke="#4a5563"/>')
    o.append(T(0, 14, "100 young people on the roll: how many are still on track after each step (illustrative)", "b"))
    o.append("</g>")
    o.append(T(0, 226, "Red bars mark the two biggest leaks: registering in time, and turning a vague intention into a plan.", "b acc"))
    return svg(234, o)
FIGS["journey91"] = journey91()


def east91():
    rows = [("E", "Easy", "Remove steps", "One tap: “Am I on the list? Which booth?”,|with the route and the booth’s opening hours", "#127a64", "#e1f2ec"),
            ("A", "Attractive", "Make it appealing", "A first-time-voter pledge card to share;|the inked-finger photo frame after voting", "#c47f17", "#fbf4e6"),
            ("S", "Social", "Show what others do", "“8 in 10 first-time voters in your ward|have checked their booth” (only if true)", "#7c3aa6", "#f1e6f8"),
            ("T", "Timely", "Ask at the right moment", "Three days before: “What time will you go?”|Polling morning: “Your booth opens at 7”", "#0b5d7a", "#e3f0f5")]
    o = ['<g class="c">']
    for i, (L, name, what, ex, col, bg) in enumerate(rows):
        y = 4 + i * 50
        o.append(f'<rect x="0" y="{y}" width="680" height="44" rx="6" fill="{bg}" stroke="{col}" stroke-width="1.3"/>')
        o.append(f'<circle cx="26" cy="{y + 22}" r="15" fill="{col}"/>' + T(26, y + 27, L, "b w t13", "middle"))
        o.append(T(52, y + 19, name, "b", fill=col)); o.append(T(52, y + 34, what, "s"))
        o.append(T(210, y + 19, ex.split("|")[0])); o.append(T(210, y + 34, ex.split("|")[1]))
    o.append("</g>")
    return svg(206, o)
FIGS["east91"] = east91()

FIGS["evid91"] = hbars([("“Your neighbours will see”", 8.1, "mailer listing who voted (US, 2006)"),
                        ("“Here is your voting record”", 4.9, "mailer showing your own past turnout"),
                        ("A call to make a plan", 4.1, "“when, from where, how?” (US, 2008)"),
                        ("“Voting is your duty”", 1.8, "a plain civic-duty letter"),
                        ("Friends who voted, on Facebook", 0.4, "tiny per person, but 6.1 crore people")], 9,
                       lw=200, fmt="+{}", unit=" points", colors=["#9aa3ad", "#9aa3ad", "#127a64", "#9aa3ad", "#0b5d7a"],
                       note="Extra turnout from famous experiments, in percentage points over a group that got nothing")


def lift91():
    o = []
    def panel(x0, title, sub, bars, verdict, vcol):
        o.append(T(x0, 12, title, "b")); o.append(T(x0, 26, sub, "s"))
        for i, (lab, v, col) in enumerate(bars):
            bx = x0 + 30 + i * 130; hh = v * 1.45
            o.append(f'<rect x="{bx}" y="{146 - hh:.1f}" width="80" height="{hh:.1f}" fill="{col}" rx="2"/>')
            o.append(T(bx + 40, 141 - hh, f"{v}%", "b", "middle"))
            o.append(lines(bx + 40, 160, lab, "s", "middle", 12))
        o.append(f'<line x1="{x0}" y1="146" x2="{x0 + 300}" y2="146" stroke="#4a5563"/>')
        o.append(lines(x0, 196, verdict, vcol, "start", 13))
    panel(0, "Misleading: app users vs everyone else", "keen voters are the ones who install it",
          [("Installed|the app", 70, "#9aa3ad"), ("Didn’t|install", 38, "#9aa3ad")], "Gap of 32 points, but most of it is|who installs, not what the app did", "b red")
    panel(360, "Fair: a random 10% get no reminders", "same kind of people in both groups",
          [("Got the|reminders", 43, "#127a64"), ("Held out|(10%)", 40, "#0b5d7a")], "Gap of 3 points: this is what|the reminders actually caused", "b grn")
    o.append('<line x1="340" y1="4" x2="340" y2="212" stroke="#d9dee4"/>')
    return svg(216, o)
FIGS["lift91"] = lift91()


# ================= Case 9.2 Apple smart-speaker pricing =================
FIGS["strip92"] = strip([("Clarify", "goal, market, iPhone?"), ("Who buys", "iPhone homes"), ("Cost floor", "below it, a loss"),
                         ("Value", "vs what they compare"), ("Price", "profit + services"), ("Measure", "homes, not share")])

FIGS["ladder92"] = hbars([("Google Nest Mini", 4499, "street price, 2026"), ("Amazon Echo Dot", 5499, "list price, 2026"),
                          ("Candidate’s “Home Mini”", 6500, "Nest × 1.3: under Apple’s cost floor"),
                          ("Google Nest (casebook)", 7000, "the interviewer’s figure"), ("Top Echo (casebook)", 10000, "the interviewer’s figure"),
                          ("Candidate’s “Home”", 13000, "Echo × 1.3"), ("Apple HomePod mini", 15900, "Apple India store, Sep 2026"),
                          ("Apple HomePod", 44900, "Apple India store, Sep 2026")], 44900,
                         lw=180, fmt="₹{:,}", colors=["#9aa3ad", "#9aa3ad", "#c47f17", "#9aa3ad", "#9aa3ad", "#c47f17", "#0b5d7a", "#0b5d7a"],
                         note="Smart speakers in India, by price (orange: the candidate’s proposal)")


def profit92():
    rows = [(6500, 120, -1453, "#b93a32"), (9900, 80, 1083, "#0b5d7a"), (12900, 55, 3320, "#127a64"), (15900, 35, 5558, "#0b5d7a")]
    svc = 1000
    L, Bt, Tp = 60, 176, 26
    o = [T(0, 12, "Mini speaker in India: profit to Apple over 3 years at four prices (₹ crore, illustrative)", "b")]
    zero = 112; sc = 3.2
    o.append(f'<line x1="{L}" y1="{zero}" x2="676" y2="{zero}" stroke="#4a5563"/>')
    o.append(T(L - 6, zero + 4, "0", "s", "end"))
    for i, (p, units, m, col) in enumerate(rows):
        x = L + 20 + i * 150
        dev = units * 1000 * m / 1e7; tot = units * 1000 * (m + svc) / 1e7
        h1 = dev * sc; h2 = tot * sc
        # device-only (hatched grey) and with services
        y1 = zero - max(h1, 0); o.append(f'<rect x="{x}" y="{y1:.1f}" width="46" height="{abs(h1):.1f}" fill="#9aa3ad" rx="2"/>')
        y2 = zero - max(h2, 0); o.append(f'<rect x="{x + 52}" y="{y2:.1f}" width="46" height="{abs(h2):.1f}" fill="{col}" rx="2"/>')
        o.append(T(x + 23, (y1 - 4) if dev >= 0 else (zero + abs(h1) + 12), f"{dev:+.1f}", "s", "middle"))
        o.append(T(x + 75, (y2 - 4) if tot >= 0 else (zero + abs(h2) + 12), f"{tot:+.1f}", "b", "middle"))
        o.append(T(x + 49, 200, f"₹{p:,}", "b", "middle"))
        o.append(T(x + 49, 214, f"{units}k homes a year", "s", "middle"))
    o.append('<rect x="60" y="226" width="10" height="10" fill="#9aa3ad"/>'); o.append(T(76, 235, "the device alone", "s"))
    o.append('<rect x="180" y="226" width="10" height="10" fill="#127a64"/>'); o.append(T(196, 235, "device + ₹1,000 of services", "s"))
    o.append(T(400, 235, "₹12,900 earns about what ₹15,900 does,", "b grn")); o.append(T(400, 249, "in 57% more homes", "b grn"))
    return svg(256, o)
FIGS["profit92"] = profit92()

FIGS["worth92"] = waterfall([("Price paid|by the buyer", 12900, "start"), ("GST|18%", 1968, "down"), ("Shop and|distributor", 1312, "down"),
                             ("Parts, assembly,|freight, warranty", 6300, "down"), ("Services over|3 years", 1000, "up"), ("What one speaker|is worth to Apple", 4320, "total")],
                            h=226, note="One mini speaker at ₹12,900, over three years (illustrative)")


# ================= Case 9.3 Tata Group loyalty =================
FIGS["strip93"] = strip([("Clarify", "Neu exists: what fails?"), ("Goal", "shop at a 2nd brand"), ("Economics", "what a point costs"),
                         ("Design", "earn, burn, fund"), ("Move over", "ID, consent, balances"), ("Measure", "cross-brand members")])


def cost93():
    o = [T(0, 12, "One year, 1 crore members spending ₹40,000 each = ₹40,000 crore of sales (illustrative)", "b")]
    rows = [("Flat 5% on everything", 1500, 6000, "15%", "#b93a32"), ("1% base + 5% bonus at a new brand", 340, 1360, "3.4%", "#127a64")]
    L = 250; sc = 380 / 6000
    for i, (lab, cost, be, pct, col) in enumerate(rows):
        y = 32 + i * 76
        o.append(T(L - 8, y + 14, lab, "b", "end"))
        o.append(f'<rect x="{L}" y="{y}" width="{cost * sc:.1f}" height="18" fill="{col}" rx="2"/>')
        o.append(T(L + cost * sc + 6, y + 13, f"cost of points ₹{cost:,} Cr", "s"))
        o.append(f'<rect x="{L}" y="{y + 24}" width="{be * sc:.1f}" height="18" fill="none" stroke="{col}" stroke-width="1.6" stroke-dasharray="4 3" rx="2"/>')
        o.append(T(L + 4, y + 57, f"extra sales needed to pay for it: ₹{be:,} Cr, a {pct} jump", "b", fill=col))
    o.append(T(0, 192, "Cost = sales × earn rate × 75% redeemed. Extra sales needed to pay for it = cost ÷ 25% gross margin.", "s"))
    return svg(198, o)
FIGS["cost93"] = cost93()


def settle93():
    rows = [("BigBasket", -40, "people earn on groceries every week…"), ("Croma", -12, ""), ("Titan, Tanishq", -15, ""),
            ("Westside", -6, ""), ("Starbucks", 10, ""), ("Taj hotels", 22, "…and spend on a holiday or a flight"), ("Air India", 41, "")]
    o = [T(0, 12, "Net settlement per brand in a year: pays into the pool (red) or is paid from it (green), ₹ crore (illustrative)", "b")]
    mid = 400; sc = 4.2
    o.append(f'<line x1="{mid}" y1="22" x2="{mid}" y2="{24 + 24 * len(rows)}" stroke="#4a5563"/>')
    for i, (lab, v, note) in enumerate(rows):
        y = 26 + i * 24
        col = "#b93a32" if v < 0 else "#127a64"
        x = mid + min(v, 0) * sc; w = abs(v) * sc
        o.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="16" fill="{col}" rx="2"/>')
        if v < 0:
            o.append(T(x - 6, y + 12, f"{lab}  −{abs(v)}", "b", "end"))
        else:
            o.append(T(mid - 8, y + 12, lab, "b", "end")); o.append(T(x + w + 6, y + 12, f"+{v}", "b"))
    o.append(T(0, 208, "Brands where points are earned pay the brands where they are spent. Set each brand’s earn rate from its own margin,", "s"))
    o.append(T(0, 222, "or the grocery business ends up paying for other people’s holidays and quits the programme.", "s"))
    return svg(228, o)
FIGS["settle93"] = settle93()

FIGS["loop93"] = loop(["Buy at one brand|earn NeuCoins", "Something to spend on|at another brand", "Try the second brand|with a bonus",
                       "Know the customer|across brands", "Better offers|with consent"], "More Tata brands|per customer", h=236, ry=84, bw=156)


FIGS["premortem93"] = hbars([("Points worth too little to notice", 9, "1% on groceries feels like nothing"), ("Few places people want to spend", 8, "most burn goes to a few brands"),
                             ("Brands refuse to fund it", 8, "BigBasket pays for Air India trips"), ("An app nobody opens", 6, "no weekly reason to come back"),
                             ("Data shared without clear consent", 5, "one complaint becomes news"), ("Old balances lost in the move", 4, "a one-time, avoidable anger")], 10,
                            lw=220, fmt="{}", unit="/10", colors=["#b93a32", "#b93a32", "#b93a32", "#c47f17", "#c47f17", "#9aa3ad"],
                            note="Pre-mortem, “It’s 2028 and the programme failed. Why?”: causes ranked by likelihood × damage (illustrative scores)")
