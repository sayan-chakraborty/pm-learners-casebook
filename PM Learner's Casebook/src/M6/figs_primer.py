"""Primer figures for M6; imported at the end of m6_figs.py (shares its helpers and FIGS)."""
from m6_figs import FIGS, svg, T, lines, hbars, waterfall  # noqa: F401

MK = ('<defs><marker id="pa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
      '<path d="M0,0 L10,5 L0,10 z" fill="#4a5563"/></marker>'
      '<marker id="pg" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4.5" markerHeight="4.5" orient="auto">'
      '<path d="M0,0 L10,5 L0,10 z" fill="#127a64"/></marker>'
      '<marker id="pr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
      '<path d="M0,0 L10,5 L0,10 z" fill="#8a939e"/></marker></defs>')

def box(x, y, w, h, fill, st, rows, sw=1.4, lh=14):
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{st}" stroke-width="{sw}"/>']
    y0 = y + h / 2 - (len(rows) - 1) * lh / 2 + 4
    for i, (s, c) in enumerate(rows):
        o.append(T(x + w / 2, y0 + i * lh, s, c, "middle"))
    return "".join(o)

G, B, A, GR, R, P = (("#e1f2ec", "#127a64"), ("#e3f0f5", "#0b5d7a"), ("#fde7c8", "#c47f17"), ("#eef0f2", "#5b6470"),
                     ("#fcecea", "#b93a32"), ("#f1e6f8", "#7c3aa6"))


def money():
    o = [MK,
         '<line x1="440" y1="10" x2="470" y2="10" class="money"/>', T(476, 14, "money", "s"),
         '<line x1="522" y1="10" x2="552" y2="10" class="msg"/>', T(558, 14, "content, streams", "s"),
         box(6, 28, 150, 62, *P, [("Rights owners", "b"), ("BCCI, studios,", ""), ("record labels", "s")]),
         box(262, 104, 156, 70, *B, [("Streaming app", "b"), ("buys rights, streams,", ""), ("sells ads and plans", "s")]),
         box(6, 196, 150, 58, *G, [("Viewers", "b"), ("watch, listen;", ""), ("pay ₹0 to ₹649 a month", "s")]),
         box(524, 28, 150, 58, *GR, [("Advertisers", "b"), ("brands buying", ""), ("seconds of attention", "s")]),
         box(524, 112, 150, 50, *GR, [("Delivery networks", "b"), ("CDNs, internet providers", "s")]),
         box(524, 200, 150, 58, *A, [("Telecom operators", "b"), ("Jio, Airtel: app", ""), ("inside a recharge", "s")]),
         '<line x1="156" y1="58" x2="258" y2="116" class="msg" marker-end="url(#pa)"/>',
         T(162, 46, "① matches, films, songs", "halo", "start"),
         '<path d="M262,128 L162,74" class="money" marker-end="url(#pg)"/>',
         T(194, 128, "② rights fee: ₹58 Cr", "b grn halo", "middle"), T(194, 141, "an IPL match (digital)", "grn halo", "middle"),
         '<line x1="262" y1="160" x2="160" y2="208" class="msg" marker-end="url(#pa)"/>',
         T(150, 180, "③ the stream", "halo", "end"),
         '<path d="M156,226 C230,226 300,200 318,178" class="money" marker-end="url(#pg)"/>',
         T(326, 196, "④ ₹79–649 a month", "b grn halo", "start"),
         '<line x1="524" y1="64" x2="422" y2="114" class="money" marker-end="url(#pg)"/>',
         T(468, 58, "⑤ ₹ per 1,000", "b grn halo", "middle"), T(468, 71, "ad views", "grn halo", "middle"),
         '<line x1="418" y1="140" x2="520" y2="138" class="money" marker-end="url(#pg)"/>',
         T(470, 131, "⑧ delivery", "b grn halo", "middle"),
         '<line x1="524" y1="218" x2="424" y2="166" class="money" marker-end="url(#pg)"/>',
         T(486, 178, "⑥ bundle fee", "b grn halo", "start"),
         '<path d="M156,244 C300,284 450,276 520,246" class="money" marker-end="url(#pg)"/>',
         T(340, 290, "⑦ a recharge that includes the app", "b grn halo", "middle"),
         ]
    return svg(298, o)
FIGS["money"] = money()

# one subscriber's year on a ₹199 plan (illustrative)
FIGS["subyear"] = waterfall([("Paid in a|year", 2388, "start"), ("GST|18%", 364, "down"), ("Payment|fees", 40, "down"),
                             ("Content|share", 900, "down"), ("Streaming,|delivery", 90, "down"), ("Marketing", 230, "down"),
                             ("Tech,|staff, other", 300, "down"), ("Left over", 0, "total")],
                            h=230, note="₹199 a month × 12 = ₹2,388. Where it goes (illustrative shares, modelled on Netflix’s global cost mix).")


def fixedcost():
    L, R, Tp, Bt = 70, 660, 24, 190
    xs = [(10, "10 L"), (50, "50 L"), (100, "1 Cr"), (200, "2 Cr"), (300, "3 Cr"), (500, "5 Cr")]
    X = lambda v: L + (R - L) * v / 500
    Y = lambda c: Bt - (Bt - Tp) * min(c, 8000) / 8000
    o = [f'<line x1="{L}" y1="{Bt}" x2="{R}" y2="{Bt}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{Bt}" stroke="#4a5563"/>']
    for v in (0, 2000, 4000, 6000, 8000):
        o.append(T(L - 6, Y(v) + 4, f"₹{v:,}", "s", "end"))
        o.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{R}" y2="{Y(v):.1f}" stroke="#eef0f2"/>')
    for v, lab in xs: o.append(T(X(v), Bt + 15, lab, "s", "middle"))
    pts = [(v, 200000 / v) for v in range(25, 501, 5)]
    d = " ".join(f"{'M' if i == 0 else 'L'}{X(v):.1f},{Y(c):.1f}" for i, (v, c) in enumerate(pts))
    o.append(f'<path d="{d}" fill="none" stroke="#0b5d7a" stroke-width="2.6"/>')
    o.append(f'<line x1="{L}" y1="{Y(1500):.1f}" x2="{R}" y2="{Y(1500):.1f}" stroke="#127a64" stroke-width="1.6" stroke-dasharray="6 3"/>')
    o.append(T(R, Y(1500) - 6, "what a subscriber pays in a year after GST: about ₹1,500", "b grn", "end"))
    for v in (50, 133, 400):
        c = 200000 / v
        o.append(f'<circle cx="{X(v):.1f}" cy="{Y(c):.1f}" r="4.5" fill="#0b5d7a"/>')
    o.append(T(X(50) + 8, Y(4000) - 4, "50 lakh subscribers: ₹4,000 each: a loss", "b red halo"))
    o.append(T(X(133) - 8, Y(1500) + 18, "1.33 Cr: content cost = what they pay", "b halo", "end"))
    o.append(T(X(400), Y(1000) + 2, "4 Cr: ₹500 each: a profit", "b grn halo", "middle"))
    o.append(T(L, 12, "Content cost per subscriber when the yearly content budget is ₹2,000 Cr (illustrative)", "b"))
    o.append(T((L + R) / 2, Bt + 30, "paying subscribers", "s", "middle"))
    return svg(226, o)
FIGS["fixedcost"] = fixedcost()


def iplmaths():
    o = [MK, '<g class="c">']
    chain = [("₹23,758 Cr", "digital rights,", "2023–27"), ("÷ 410 matches", "= ₹58 Cr", "a match"), ("÷ 20 Cr viewers", "= ₹2.90", "a viewer a match"),
             ("÷ ₹0.07 an ad", "(₹70 per", "1,000 views)"), ("≈ 40 ads", "per viewer", "per match")]
    w = 120
    for i, (a, b, c) in enumerate(chain):
        x = 4 + i * 138
        st = G if i == 4 else (B if i else P)
        o.append(box(x, 26, w, 64, *st, [(a, "b"), (b, ""), (c, "")]))
        if i < 4: o.append(f'<line x1="{x + w + 1}" y1="58" x2="{x + 136}" y2="58" class="ln" marker-end="url(#pa)"/>')
    o.append(T(4, 14, "What one IPL match must earn on phones, before a rupee of profit (viewers and ad price illustrative)", "s"))
    o.append(T(4, 112, "40 ads of 10–20 seconds is 7–13 minutes of ads per viewer. That is why every over-break, strategic time-out and", "b acc"))
    o.append(T(4, 127, "wicket is sold, and why the rights price sets the product: miss the ad target and the app must charge viewers instead.", "b acc"))
    o.append("</g>")
    return svg(136, o)
FIGS["iplmaths"] = iplmaths()


def reach():
    rows = [("Reached in the season", 70, "crore people watched some IPL 2026 on JioHotstar (company)", "#9fb8c4"),
            ("Subscriptions", 30, "crore claimed during IPL 2025, mostly bundled with recharges", "#0b5d7a"),
            ("Watching at one moment", 6.5, "crore: record, India–England T20 World Cup semi-final, Mar 2026", "#b93a32")]
    o = []
    for i, (lab, v, note, col) in enumerate(rows):
        y = 8 + i * 40
        o.append(T(0, y + 16, lab, "b"))
        w = 440 * v / 70
        o.append(f'<rect x="170" y="{y + 3}" width="{w:.1f}" height="20" rx="2" fill="{col}"/>')
        o.append(T(176 + w, y + 18, f"{v:g}", "b"))
        o.append(T(170, y + 36, note, "s"))
    return svg(128, o)
FIGS["reach"] = reach()


def timeline():
    pts = [(56, "Sep 2016", "Cheap data", ["Jio’s free, then", "cheap data makes", "video an all-day", "habit on phones"], "#0b5d7a"),
           (170, "2020", "Covid", ["Cinemas shut;", "films go straight", "to OTT; sign-ups", "jump"], "#c47f17"),
           (284, "Jun 2022", "IPL rights split", ["Digital rights sold", "separately:", "₹23,758 Cr to", "Viacom18"], "#3e4fb8"),
           (398, "2023", "Free IPL, no sharing", ["JioCinema streams", "IPL free; Netflix", "stops password", "sharing (July)"], "#b93a32"),
           (512, "Nov 2024–Feb 2025", "JioHotstar", ["Star + Viacom18", "merge; one app,", "cricket, Disney,", "HBO, serials"], "#0b5d7a"),
           (618, "Aug 2025", "Gaming Act", ["Real-money games", "banned from", "1 Oct 2025"], "#b93a32")]
    o = ['<line x1="10" y1="60" x2="672" y2="60" stroke="#4a5563" stroke-width="2"/><g class="c">']
    for x, d, h, ls, col in pts:
        o.append(f'<circle cx="{x}" cy="60" r="6.5" fill="{col}"/>')
        o.append(T(x, 46, d, "b", "middle"))
        o.append(T(x - 50, 80, h, "b", "start", fill=col))
        for i, l in enumerate(ls): o.append(T(x - 50, 94 + i * 13, l))
    o.append("</g>")
    o.append(T(10, 16, "Each turning point changed who pays, what they pay for, or how many people can watch at all.", "s"))
    return svg(152, o)
FIGS["timeline"] = timeline()


def churnyear():
    L, R, Tp, Bt = 48, 670, 22, 160
    m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    v = [100, 100, 150, 172, 178, 118, 110, 108, 109, 118, 116, 112]
    X = lambda i: L + (R - L) * i / 11
    Y = lambda s: Bt - (Bt - Tp) * (s - 60) / 130
    o = [f'<rect x="{X(2) - 20:.1f}" y="{Tp}" width="{X(4) - X(2) + 40:.1f}" height="{Bt - Tp}" fill="#e3f0f5"/>',
         T((X(2) + X(4)) / 2, Tp + 14, "IPL season", "b acc", "middle"),
         f'<line x1="{L}" y1="{Bt}" x2="{R}" y2="{Bt}" stroke="#4a5563"/>']
    for i, lab in enumerate(m): o.append(T(X(i), Bt + 15, lab, "s", "middle"))
    d = " ".join(f"{'M' if i == 0 else 'L'}{X(i):.1f},{Y(s):.1f}" for i, s in enumerate(v))
    o.append(f'<path d="{d}" fill="none" stroke="#0b5d7a" stroke-width="2.6"/>')
    for i, s in enumerate(v): o.append(f'<circle cx="{X(i):.1f}" cy="{Y(s):.1f}" r="3" fill="#0b5d7a"/>')
    o.append(T(X(0), Y(100) - 8, "100 paying", "b"))
    o.append(T(X(4) + 8, Y(178) + 4, "178: +78 joined for cricket", "b"))
    o.append(T(X(5) + 8, 134, "June: 60 of the 78 leave", "b red"))
    o.append(T(X(9), 66, "a big series or a World Cup", "s", "middle"))
    o.append(T(X(9), 79, "brings some back", "s", "middle"))
    return svg(184, o)
FIGS["churnyear"] = churnyear()

FIGS["royalty"] = waterfall([("Premium|payment", 100, "start"), ("Labels,|publishers", 67, "down"), ("Product,|engineering", 7, "down"),
                             ("Marketing", 9, "down"), ("Admin", 4, "down"), ("Spotify|keeps", 0, "total")],
                            h=210, note="Where ₹100 of a music subscription goes (Spotify’s cost mix, Q2 2026, rounded)")


def cph():
    rows = [("Big-budget series", 100, 2.0, "#b93a32"), ("Hollywood film licence", 30, 1.0, "#c47f17"),
            ("Small-town comedy", 12, 1.5, "#127a64"), ("IPL match (digital rights)", 58, 20, "#0b5d7a")]
    o = [T(0, 12, "title", "b"), T(200, 12, "cost", "b"), T(270, 12, "hours watched", "b"), T(400, 12, "cost per hour watched", "b")]
    for i, (lab, cost, hrs, col) in enumerate(rows):
        y = 22 + i * 26
        v = cost / hrs
        o.append(T(0, y + 15, lab, "b"))
        o.append(T(200, y + 15, f"₹{cost} Cr", ""))
        o.append(T(270, y + 15, f"{hrs:g} Cr hours", ""))
        w = 220 * v / 50
        o.append(f'<rect x="400" y="{y + 3}" width="{w:.1f}" height="16" fill="{col}" rx="2"/>')
        o.append(T(406 + w, y + 16, f"₹{v:,.0f}", "b"))
    o.append(T(0, 134, "IPL row: one match, 20 crore viewers × about 1 hour each = 20 crore hours (illustrative).", "s"))
    return svg(142, o)
FIGS["cph"] = cph()
