"""Primer figures for M8; imported at the end of m8_figs.py (shares its helpers and FIGS)."""
from m8_figs import FIGS, svg, T, lines, hbars, waterfall  # noqa: F401

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


# ---------- who buys, who uses, who can say no ----------
def deal():
    o = [MK,
         box(250, 104, 180, 64, *A, [("One deal", "b"), ("200 seats × ₹1,000 a month", ""), ("= ₹24 lakh a year", "b")]),
         box(6, 18, 172, 58, *G, [("Users: 200 agents", "b"), ("work in the tool all day", "s")]),
         box(255, 8, 170, 50, *B, [("Buyer: Head of Support", "b"), ("owns the budget", "s")]),
         box(502, 18, 172, 58, *R, [("IT and security", "b"), ("can say no: login, data", "s"), ("location, access rights", "s")]),
         box(502, 194, 172, 58, *R, [("Legal", "b"), ("contract and data terms", "s")]),
         box(255, 208, 170, 50, *GR, [("Finance, procurement", "b"), ("discount, payment terms", "s")]),
         box(6, 194, 172, 58, *P, [("The vendor’s team", "b"), ("sales rep, engineer,", "s"), ("customer success", "s")]),
         '<line x1="178" y1="70" x2="248" y2="112" stroke="#4a5563" stroke-width="1.4" marker-end="url(#pa)"/>',
         '<line x1="502" y1="70" x2="432" y2="112" stroke="#b93a32" stroke-width="1.4" marker-end="url(#pr)"/>',
         '<line x1="502" y1="200" x2="432" y2="160" stroke="#b93a32" stroke-width="1.4" marker-end="url(#pr)"/>',
         '<line x1="178" y1="200" x2="248" y2="160" stroke="#7c3aa6" stroke-width="1.4" marker-end="url(#pa)"/>',
         '<line x1="340" y1="58" x2="340" y2="102" class="money" marker-end="url(#pg)"/>',
         '<line x1="340" y1="206" x2="340" y2="170" stroke="#4a5563" stroke-width="1.4" marker-end="url(#pa)"/>',
         T(10, 94, "try it in a pilot, then", "s"), T(10, 107, "use it, or quietly ignore it", "s"),
         T(670, 94, "security review, 4–8 weeks;", "s", "end"), T(670, 107, "one “no” stops the deal", "b red", "end"),
         T(10, 172, "demos, a pilot,", "s"), T(10, 185, "a price quote", "s"),
         T(670, 172, "data-processing terms,", "s", "end"), T(670, 185, "limits on liability", "s", "end"),
         T(348, 84, "signs; pays ₹24 lakh a year", "b grn halo"),
         T(348, 192, "asks 15% off; pays yearly", "halo"),
         ]
    return svg(262, o)
FIGS["deal"] = deal()

# ---------- one seat, one month ----------
FIGS["seatwf"] = waterfall([("List price|a seat a month", 1000, "start"), ("Hosting,|support", 200, "down"),
                            ("Gross profit|classic SaaS", 0, "total"), ("AI model|calls", 150, "down"),
                            ("Gross profit|with AI", 0, "total")],
                           note="One seat for one month (illustrative). Classic SaaS keeps about 80 paise of each rupee;|an AI feature adds a bill that grows with use and takes it to 65 paise.", h=236, top=40)

# ---------- NRR ----------
FIGS["nrr"] = waterfall([("Last January:|what they paid", 24.0, "start"), ("More seats|200 → 260", 7.2, "up"),
                         ("Downgrades|and cuts", 1.2, "down"), ("This January:|same customers", 0, "total")],
                        suffix=" L", note="Customers who were already paying a year ago, ₹ lakh a year (illustrative).|NRR = ₹30 lakh ÷ ₹24 lakh = 125%: 25% growth without a single new customer.", h=228, top=40)


# ---------- CAC payback ----------
def payback():
    L, Rr, Tp, Bt = 54, 640, 30, 196
    X = lambda m: L + (Rr - L) * m / 24
    Y = lambda v: Bt - (Bt - Tp) * v / 40
    o = [f'<line x1="{L}" y1="{Bt}" x2="{Rr}" y2="{Bt}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{Bt}" stroke="#4a5563"/>']
    for v in (0, 10, 20, 30, 40):
        o.append(T(L - 6, Y(v) + 4, f"₹{v}L", "s", "end"))
        if v: o.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{Rr}" y2="{Y(v):.1f}" stroke="#eef0f2"/>')
    for m in (0, 6, 12, 18, 24): o.append(T(X(m), Bt + 15, f"month {m}", "s", "middle"))
    o.append(f'<line x1="{L}" y1="{Y(24):.1f}" x2="{Rr}" y2="{Y(24):.1f}" stroke="#b93a32" stroke-width="2.2"/>')
    o.append(T(L + 6, Y(24) - 6, "cost to win the deal (CAC): ₹24 lakh of sales time, demos, a pilot", "b red halo"))
    for rate, col, lab, dy in ((1.6, "#127a64", "classic: ₹1.6 lakh gross profit a month", -8), (1.3, "#c47f17", "with AI: ₹1.3 lakh a month", 16)):
        o.append(f'<line x1="{X(0):.1f}" y1="{Y(0):.1f}" x2="{X(24):.1f}" y2="{Y(24 * rate):.1f}" stroke="{col}" stroke-width="2.6"/>')
        m = 24 / rate
        o.append(f'<line x1="{X(m):.1f}" y1="{Y(24):.1f}" x2="{X(m):.1f}" y2="{Bt}" stroke="{col}" stroke-dasharray="4 3"/>')
        o.append(f'<circle cx="{X(m):.1f}" cy="{Y(24):.1f}" r="5" fill="{col}"/>')
    o.append(T(X(15) - 6, Bt - 8, "15 months", "b grn", "end"))
    o.append(T(X(18.5) + 6, Bt - 8, "18.5 months", "b", "start", fill="#c47f17"))
    o.append(T(X(19.3), Y(13), "classic: ₹1.6 lakh", "b grn")); o.append(T(X(19.3), Y(13) + 13, "gross profit a month", "grn"))
    o.append(T(X(19.3), Y(5), "with AI: ₹1.3 lakh", "b", "start", fill="#c47f17"))
    o.append(T(L, 14, "Cumulative gross profit from the 200-seat customer against what it cost to win them (illustrative)", "s"))
    return svg(218, o)
FIGS["payback"] = payback()

# ---------- players ----------
FIGS["cloudgrowth"] = vbars([("AWS", 37, "+37%"), ("Microsoft|Azure", 43, "+43%"), ("Google|Cloud", 82, "+82%")], 82,
                            "Cloud growth, Apr–Jun 2026", sub="revenue: AWS $42.2 bn, Google Cloud $24.8 bn", colors=["#c47f17", "#0b5d7a", "#127a64"])
FIGS["copilotseats"] = vbars([("Jan|2026", 15, "1.5 Cr"), ("Apr|2026", 20, "2 Cr"), ("Jul|2026", 30, "3 Cr+")], 30,
                             "Microsoft 365 Copilot paid seats", sub="out of about 45 crore Microsoft 365 office seats", colors=["#3e4fb8"])


# ---------- timeline ----------
def timeline():
    pts = [(46, "1999", "Salesforce", ["Software over the", "internet, paid", "by the month:", "“no software”"], "#0b5d7a"),
           (130, "2006", "AWS", ["Rent servers by", "the hour; start-", "ups need no", "data centre"], "#c47f17"),
           (214, "2013", "Adobe CC", ["Boxed software", "ends: ₹ a month", "replaces one", "big payment"], "#0b5d7a"),
           (298, "2020", "Covid", ["Zoom, Teams,", "Slack, cloud", "tools become", "daily habits"], "#7c3aa6"),
           (382, "Nov 2022", "ChatGPT", ["Anyone can", "talk to an AI;", "every office", "tool adds one"], "#3e4fb8"),
           (466, "Nov 2023", "M365 Copilot", ["AI sold per seat", "at $30 a user", "a month; 3 Cr+", "seats by 2026"], "#3e4fb8"),
           (550, "Nov 2024", "MCP", ["A common plug", "for AI tools; to", "the Linux Found-", "ation, Dec 2025"], "#127a64"),
           (634, "2025–26", "Pay per result", ["Intercom $0.99 a", "resolution; Sales-", "force per action;", "seats questioned"], "#b93a32")]
    o = ['<line x1="8" y1="104" x2="674" y2="104" stroke="#4a5563" stroke-width="2"/><g class="c">']
    for i, (x, d, h, ls, col) in enumerate(pts):
        o.append(f'<circle cx="{x}" cy="104" r="6.5" fill="{col}"/>')
        if i % 2 == 0:
            o.append(T(x, 90, d, "b", "middle")); y0 = 126
        else:
            o.append(T(x, 124, d, "b", "middle")); y0 = 16
        o.append(T(x - 40, y0, h, "b", "start", fill=col))
        for j, l in enumerate(ls): o.append(T(x - 40, y0 + 14 + j * 13, l))
    o.append("</g>")
    return svg(192, o)
FIGS["timeline"] = timeline()


# ---------- pricing ladder ----------
def priceladder():
    cols = [("Per seat", "a fee per person", "M365 Copilot: $30 a user a month", "exactly", "the vendor: heavy users cost more", B),
            ("Per use", "a fee per action or credit", "Agentforce: about $0.10 an action", "roughly, with a cap", "shared: the bill grows with use", A),
            ("Per outcome", "a fee per job done", "Intercom Fin: $0.99 a resolution", "only after the fact", "the vendor, if the AI can’t finish", G)]
    o = ['<defs><marker id="plr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#4a5563"/></marker></defs>']
    w = 212
    for i, (h, sub, eg, know, risk, (fill, st)) in enumerate(cols):
        x = i * (w + 22)
        o.append(f'<rect x="{x}" y="4" width="{w}" height="150" rx="6" fill="{fill}" stroke="{st}" stroke-width="1.4"/>')
        o.append(T(x + w / 2, 24, h, "b", "middle")); o.append(T(x + w / 2, 39, sub, "s", "middle"))
        o.append(T(x + 10, 62, "Example", "b")); o.append(T(x + 10, 76, eg, "s"))
        o.append(T(x + 10, 98, "Does the buyer know the bill?", "b")); o.append(T(x + 10, 112, know, "s"))
        o.append(T(x + 10, 134, "Who loses if costs jump?", "b")); o.append(T(x + 10, 148, risk, "s"))
    o.append('<line x1="10" y1="176" x2="668" y2="176" stroke="#4a5563" stroke-width="1.6" marker-end="url(#plr)"/>')
    o.append(T(10, 194, "Left to right: the price follows the value more closely, and the buyer’s bill becomes harder to predict.", "s"))
    return svg(202, o)
FIGS["priceladder"] = priceladder()


# ---------- renewal cliff ----------
def renewal():
    L, Rr, Tp, Bt = 50, 520, 26, 176
    X = lambda m: L + (Rr - L) * (m - 1) / 11
    Y = lambda v: Bt - (Bt - Tp) * v / 220
    act = [40, 90, 130, 150, 148, 140, 132, 124, 118, 114, 112, 110]
    o = [f'<line x1="{L}" y1="{Bt}" x2="{Rr}" y2="{Bt}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{Bt}" stroke="#4a5563"/>']
    for v in (0, 50, 100, 150, 200):
        o.append(T(L - 6, Y(v) + 4, str(v), "s", "end"))
        if v: o.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{Rr}" y2="{Y(v):.1f}" stroke="#eef0f2"/>')
    for m in (1, 3, 6, 9, 12): o.append(T(X(m), Bt + 15, f"month {m}", "s", "middle"))
    o.append(f'<line x1="{L}" y1="{Y(200):.1f}" x2="{Rr}" y2="{Y(200):.1f}" stroke="#0b5d7a" stroke-width="2.6"/>')
    o.append(T(L + 6, Y(200) - 6, "seats paid for: 200", "b acc"))
    d = " ".join(f"{'M' if i == 0 else 'L'}{X(i + 1):.1f},{Y(v):.1f}" for i, v in enumerate(act))
    o.append(f'<path d="{d}" fill="none" stroke="#127a64" stroke-width="2.6"/>')
    o.append(T(X(4), Y(150) + 18, "people who used it that month", "b grn halo", "middle"))
    o.append(f'<line x1="{X(12):.1f}" y1="{Tp}" x2="{X(12):.1f}" y2="{Bt}" stroke="#b93a32" stroke-dasharray="4 3"/>')
    o.append(T(X(12), Tp - 8, "renewal", "b red", "middle"))
    x0 = Rr + 18
    o.append(T(x0, 60, "At renewal the buyer", "b red")); o.append(T(x0, 74, "counts active users:", "red"))
    o.append(T(x0, 92, "110 of 200.", "b")); o.append(T(x0, 110, "Cuts to 120 seats:", "")); o.append(T(x0, 124, "80 × ₹1,000 × 12", ""))
    o.append(T(x0, 138, "= ₹9.6 lakh a year", "b red")); o.append(T(x0, 152, "gone in one email.", ""))
    return svg(196, o)
FIGS["renewal"] = renewal()
