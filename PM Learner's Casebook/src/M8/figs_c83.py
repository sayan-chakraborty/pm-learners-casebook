"""Case 8.3 figures (AI sales assistant GTM); imported at the end of m8_figs.py."""
from m8_figs import FIGS, svg, T, lines, strip, hbars  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R, P, I  # noqa: F401

FIGS["strip83"] = strip([("Clarify", "base, price, rivals"), ("Who", "users, buyer, India"), ("Pilot", "with a pass mark"),
                         ("Price", "cost per call hour"), ("Channels", "sales-led + a free door"), ("Measure", "and the risks")])

FIGS["pilot83"] = hbars([("Pilot accounts", 10, "picked: reps sell over video calls"), ("Reps invited", 400, "10 accounts × about 40 reps"),
                         ("Weekly active, week 4", 240, "pass mark: 60% of invited reps"), ("Accounts that pay", 6, "pass mark: 6 of 10 convert"),
                         ("Paid seats after pilot", 220, "then expand to other teams")],
                        400, lw=150, colors=["#0b5d7a", "#3e4fb8", "#127a64", "#c47f17", "#127a64"],
                        note="The pilot funnel, with the pass marks agreed with each buyer before the pilot starts (illustrative)")


def seatuse():
    L, Rr, Tp, Bt = 60, 520, 24, 206
    X = lambda hr: L + (Rr - L) * hr / 70
    Y = lambda v: Bt - (Bt - Tp) * v / 3000
    o = [f'<line x1="{L}" y1="{Bt}" x2="{Rr}" y2="{Bt}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{Bt}" stroke="#4a5563"/>']
    for v in (0, 500, 1000, 1500, 2000, 2500):
        o.append(T(L - 6, Y(v) + 4, f"₹{v:,}", "s", "end"))
        if v: o.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{Rr}" y2="{Y(v):.1f}" stroke="#eef0f2"/>')
    for hr in (0, 10, 20, 30, 40, 50, 60, 70): o.append(T(X(hr), Bt + 15, str(hr), "s", "middle"))
    o.append(T((L + Rr) / 2, Bt + 30, "call hours per rep per month", "s", "middle"))
    # cost
    o.append(f'<line x1="{X(0):.1f}" y1="{Y(0):.1f}" x2="{X(70):.1f}" y2="{Y(1750):.1f}" stroke="#b93a32" stroke-width="2.4"/>')
    # seat price
    o.append(f'<line x1="{X(0):.1f}" y1="{Y(1200):.1f}" x2="{X(70):.1f}" y2="{Y(1200):.1f}" stroke="#0b5d7a" stroke-width="2.4" stroke-dasharray="6 4"/>')
    # hybrid
    o.append(f'<path d="M{X(0):.1f},{Y(1200):.1f} L{X(30):.1f},{Y(1200):.1f} L{X(70):.1f},{Y(2800):.1f}" fill="none" stroke="#127a64" stroke-width="2.8"/>')
    o.append(f'<circle cx="{X(48):.1f}" cy="{Y(1200):.1f}" r="5" fill="#b93a32"/>')
    o.append(T(X(48) + 8, Y(1200) + 16, "break-even at 48 hours", "b red"))
    for hr, lab in ((10, "light rep"), (60, "heavy rep")):
        o.append(f'<line x1="{X(hr):.1f}" y1="{Tp + 10}" x2="{X(hr):.1f}" y2="{Bt}" stroke="#9aa3ad" stroke-dasharray="2 3"/>')
        o.append(T(X(hr), Tp + 4, lab, "b", "middle"))
    x0 = Rr + 14
    o += [T(x0, 40, "AI cost: ₹25 a call hour", "b red"), T(x0, 54, "(transcribe, summarise,", "s"), T(x0, 67, "update the CRM)", "s"),
          T(x0, 92, "Seat price: ₹1,200", "b acc"), T(x0, 106, "light rep: cost ₹250", "s"), T(x0, 119, "heavy rep: cost ₹1,500,", "s"), T(x0, 132, "a ₹300 loss", "b red"),
          T(x0, 158, "Hybrid: ₹1,200 with", "b grn"), T(x0, 172, "30 hours, then ₹40", "grn"), T(x0, 186, "an hour: heavy rep", "grn"), T(x0, 200, "pays ₹2,400", "b grn")]
    return svg(244, o)
FIGS["seatuse"] = seatuse()


def slgplg():
    o = ['<defs><marker id="sp" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#4a5563"/></marker></defs>']
    rows = [("Sales-led", "#0b5d7a", "#e3f0f5", ["Account manager|calls the sales head", "Demo, then|security review", "Paid pilot,|one team", "Contract:|300 seats", "Expand to|other teams"],
             "3–6 months to first money; ₹ lakhs per deal; works when the buyer must approve"),
            ("Product-led", "#127a64", "#e1f2ec", ["A rep signs up|free, on her calls", "Uses it daily;|invites her team", "Team hits the|free limit", "Manager pays|for the team", "Sales steps in|for the company"],
             "days to first use; small first payments; works when one user feels the value alone")]
    w = 124; gap = 15
    for r, (name, st, fill, steps, note) in enumerate(rows):
        y = 22 + r * 100
        o.append(T(0, y - 6, name, "b", fill=st))
        for i, s in enumerate(steps):
            x = i * (w + gap)
            o.append(f'<rect x="{x}" y="{y}" width="{w}" height="46" rx="6" fill="{fill}" stroke="{st}" stroke-width="1.3"/>')
            a, b = s.split("|")
            o.append(T(x + w / 2, y + 19, a, "b", "middle")); o.append(T(x + w / 2, y + 34, b, "s", "middle"))
            if i < len(steps) - 1:
                o.append(f'<line x1="{x + w + 1}" y1="{y + 23}" x2="{x + w + gap - 1}" y2="{y + 23}" stroke="#4a5563" stroke-width="1.4" marker-end="url(#sp)"/>')
        o.append(T(0, y + 64, note, "s"))
    return svg(214, o)
FIGS["slgplg"] = slgplg()
