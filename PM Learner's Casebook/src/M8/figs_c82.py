"""Case 8.2 figures (low CRM adoption); imported at the end of m8_figs.py."""
from m8_figs import FIGS, svg, T, lines  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R, P, I  # noqa: F401
from figs_cases import curves


def tree82():
    o = [MK]
    o.append(box(0, 92, 150, 70, *R, [("Reps don’t update", "b"), ("70% log in daily;", "s"), ("only 40% update", "s"), ("deals each week", "s")]))
    br = [(22, "Too costly to update", "12 clicks, 4 min an update;", "fields that don’t fit the sale", "Data: time-on-task, where", "they abandon the form", "confirmed: 12 clicks, 4 min", "#b93a32"),
          (106, "Nothing comes back", "the rep types; managers", "get the forecast", "Data: which screens reps open;", "8 interviews, tenured reps", "confirmed: reps never open reports", "#b93a32"),
          (190, "Don’t trust the data", "duplicates, old contacts,", "other reps’ stale deals", "Data: duplicate rate,", "age of last update", "partly: 18% duplicate accounts", "#c47f17")]
    for y, h, a, b, c, d, v, col in br:
        o.append(f'<path d="M150,127 C175,127 180,{y + 32} 200,{y + 32}" fill="none" stroke="#4a5563" stroke-width="1.4" marker-end="url(#pa)"/>')
        o.append(f'<rect x="202" y="{y}" width="200" height="64" rx="6" fill="#fff" stroke="#5b6470" stroke-width="1.3"/>')
        o.append(T(212, y + 18, h, "b")); o.append(T(212, y + 34, a, "s")); o.append(T(212, y + 48, b, "s"))
        o.append(f'<line x1="402" y1="{y + 32}" x2="424" y2="{y + 32}" stroke="#4a5563" stroke-width="1.2" marker-end="url(#pa)"/>')
        o.append(f'<rect x="426" y="{y}" width="254" height="64" rx="6" fill="#f3f3ee" stroke="#6b6a52"/>')
        o.append(T(436, y + 18, c, "s")); o.append(T(436, y + 32, d, "s")); o.append(T(436, y + 52, v, "b", fill=col))
    o.append(T(0, 12, "Three causes, each tested with data the company already has before any interviews (results illustrative)", "s"))
    return svg(262, o)
FIGS["tree82"] = tree82()


def clicks82():
    o = [T(0, 12, "Updating one deal after a call", "b")]
    before = ["open deal", "edit", "stage ▾", "close date", "amount", "next step", "competitor", "contact role", "log call", "type notes", "save", "back"]
    after = ["call, email and meeting logged automatically", "“Move to Proposal?” one tap", "next step: pick 1 of 3", "done"]
    o.append(T(0, 34, "Today: 12 clicks, 7 fields, about 4 minutes", "b red"))
    x = 0
    for i, s in enumerate(before):
        w = 8 + len(s) * 5.9
        o.append(f'<rect x="{x:.1f}" y="42" width="{w:.1f}" height="22" rx="4" fill="#fcecea" stroke="#b93a32"/>')
        o.append(T(x + w / 2, 57, s, "s", "middle")); x += w + 3
    o.append(T(0, 90, "After: auto-capture and suggestions, 3 taps, about 30 seconds", "b grn"))
    x = 0
    for i, s in enumerate(after):
        w = 12 + len(s) * 5.9
        fill = ("#eef0f2", "#5b6470") if i == 0 else ("#e1f2ec", "#127a64")
        o.append(f'<rect x="{x:.1f}" y="98" width="{w:.1f}" height="22" rx="4" fill="{fill[0]}" stroke="{fill[1]}"/>')
        o.append(T(x + w / 2, 113, s, "s", "middle")); x += w + 6
    o.append(T(0, 140, "20 updates a week × 4 min = 80 minutes of typing; after: 20 × 0.5 min = 10 minutes. Grey = done by the system, not the rep.", "s"))
    return svg(148, o)
FIGS["clicks82"] = clicks82()


def valueflow():
    o = [MK,
         box(0, 70, 150, 64, *G, [("The rep (user)", "b"), ("types notes, stages,", "s"), ("next steps", "s")]),
         box(265, 70, 150, 64, *GR, [("The CRM", "b"), ("stores every deal", "s")]),
         box(530, 6, 150, 50, *B, [("Sales ops (buyer)", "b"), ("chose it, made it compulsory", "s")]),
         box(530, 76, 150, 50, *B, [("Sales head, CEO", "b"), ("the weekly forecast", "s")]),
         box(530, 146, 150, 50, *B, [("Finance", "b"), ("the revenue plan", "s")]),
         '<line x1="150" y1="92" x2="262" y2="92" stroke="#4a5563" stroke-width="2" marker-end="url(#pa)"/>',
         T(206, 60, "80 min of typing a week", "b", "middle"), f"<line x1=\"206\" y1=\"64\" x2=\"206\" y2=\"90\" stroke=\"#9aa3ad\" stroke-dasharray=\"2 2\"/>",
         '<line x1="415" y1="94" x2="527" y2="36" stroke="#0b5d7a" stroke-width="1.6" marker-end="url(#pa)"/>',
         '<line x1="415" y1="102" x2="527" y2="101" stroke="#0b5d7a" stroke-width="1.6" marker-end="url(#pa)"/>',
         '<line x1="415" y1="110" x2="527" y2="166" stroke="#0b5d7a" stroke-width="1.6" marker-end="url(#pa)"/>',
         T(470, 84, "reports", "s halo", "middle"),
         '<path d="M265,122 C220,160 190,160 152,124" fill="none" stroke="#b93a32" stroke-width="1.8" stroke-dasharray="5 4" marker-end="url(#pr)"/>',
         T(208, 110, "back to the rep", "b red", "middle"), T(208, 123, "today: nothing", "b red", "middle"),
         '<path d="M290,134 C250,220 120,220 80,136" fill="none" stroke="#127a64" stroke-width="2.2" marker-end="url(#pg)"/>',
         T(186, 214, "what should come back: follow-up reminders,", "b grn", "middle"),
         T(186, 228, "“deal at risk” alerts, commission so far", "grn", "middle"),
         ]
    return svg(236, o)
FIGS["valueflow"] = valueflow()

def lead82():
    o = []
    def panel(x0, title, vals, ymax, col, lab_fmt, note):
        L, Rr, Tp, Bt = x0 + 34, x0 + 318, 30, 150
        X = lambda i: L + (Rr - L) * i / (len(vals) - 1)
        Y = lambda v: Bt - (Bt - Tp) * v / ymax
        o.append(T(x0, 12, title, "b", fill=col))
        o.append(f'<line x1="{L}" y1="{Bt}" x2="{Rr}" y2="{Bt}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{Bt}" stroke="#4a5563"/>')
        for v in (0, ymax // 2, ymax):
            o.append(T(L - 5, Y(v) + 4, f"{v}%", "s", "end"))
            if v: o.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{Rr}" y2="{Y(v):.1f}" stroke="#eef0f2"/>')
        for i, m in enumerate(["launch", "wk 4", "wk 8", "wk 12", "wk 18", "wk 26"]):
            o.append(T(X(i), Bt + 14, m, "s", "middle"))
        d = " ".join(f"{'M' if i == 0 else 'L'}{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(vals))
        o.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2.6"/>')
        for i, v in enumerate(vals):
            o.append(f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="3" fill="{col}"/>')
        o.append(T(X(0) + 4, Y(vals[0]) - 8, lab_fmt.format(vals[0]), "b", "start", fill=col))
        o.append(T(X(5), Y(vals[-1]) - 8, lab_fmt.format(vals[-1]), "b", "end", fill=col))
        o.append(T(x0, 186, note, "s"))
    panel(0, "Leading: deals updated in the last 7 days", [40, 63, 71, 74, 75, 76], 100, "#127a64", "{}%", "moves in weeks: shows the fix is being used")
    panel(352, "Lagging: forecast error", [8.0, 7.6, 6.5, 5.4, 4.6, 4.2], 10, "#b93a32", "{}%", "moves over quarters: shows it mattered")
    return svg(194, o)
FIGS["lead82"] = lead82()
