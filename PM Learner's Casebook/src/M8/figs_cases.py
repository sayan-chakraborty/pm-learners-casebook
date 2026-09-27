"""Case and guesstimate figures for M8; imported at the end of m8_figs.py."""
from m8_figs import FIGS, svg, T, lines, strip, hbars, seq  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R, P, I  # noqa: F401


def curves(series, xs, L=46, R=520, Tp=14, Bt=170, h=196, ymax=100, notes=(), step=25, unit="%"):
    X = lambda i: L + (R - L) * i / (len(xs) - 1)
    Y = lambda v: Bt - (Bt - Tp) * v / ymax
    o = [f'<line x1="{L}" y1="{Bt}" x2="{R}" y2="{Bt}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{Bt}" stroke="#4a5563"/>']
    for v in range(0, ymax + 1, step):
        o.append(T(L - 6, Y(v) + 4, str(v), "s", "end"))
        if v: o.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{R}" y2="{Y(v):.1f}" stroke="#eef0f2"/>')
    for i, m in enumerate(xs): o.append(T(X(i), Bt + 15, m, "s", "middle"))
    for lab, vals, col, dy in series:
        d = " ".join(f"{'M' if i == 0 else 'L'}{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(vals))
        o.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2.6"/>')
        for i, v in enumerate(vals): o.append(f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="2.8" fill="{col}"/>')
        o.append(T(R + 8, Y(vals[-1]) + 4 + dy, f"{lab}: {vals[-1]}{unit}", "b", fill=col))
    for x, y, s, c in notes: o.append(T(x, y, s, c))
    return svg(h, o)


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


def stacks(rows, segs, cols, total_max, title=None, lw=120, h=None, unit=" min", notes=()):
    """horizontal stacked bars. rows: (label, [values], total label); segs: segment names (legend)."""
    top = 34 if title else 26; rh = 38; h = h or top + rh * len(rows) + 30 + 14 * len(notes)
    W = 680 - lw - 70
    o = []
    if title: o.append(T(0, 12, title, "b"))
    lx = lw
    for s, c in zip(segs, cols):
        o.append(f'<rect x="{lx}" y="{top - 20}" width="10" height="10" fill="{c}"/>'); o.append(T(lx + 14, top - 11, s, "s"))
        lx += 16 + len(s) * 5.6 + 14
    for i, (lab, vals, tl) in enumerate(rows):
        y = top + i * rh
        o.append(lines(lw - 8, y + 16, lab, "b", "end", 12))
        x = lw
        for v, c in zip(vals, cols):
            w = W * v / total_max
            o.append(f'<rect x="{x:.1f}" y="{y + 4}" width="{w:.1f}" height="24" fill="{c}" stroke="#fff"/>')
            if w > 26: o.append(T(x + w / 2, y + 20, f"{v:g}", "b w", "middle"))
            x += w
        o.append(T(x + 6, y + 20, tl, "b"))
    for j, (s, c) in enumerate(notes): o.append(T(lw, top + rh * len(rows) + 14 + j * 14, s, c))
    return svg(h, o)


# ================= Case 8.1 · AI copilot for support agents =================
FIGS["strip81"] = strip([("Clarify", "volume, tools, today"), ("Size", "minutes and rupees"), ("Find the minutes", "where time goes"),
                         ("Design", "grounded drafts"), ("Escalate", "set the threshold"), ("Measure", "gate on wrong answers")])

FIGS["mins81"] = stacks([("Today", [2.5, 2.0, 2.5, 1.0], "8.0 min"), ("With the|copilot", [1.8, 1.2, 2.6, 1.2], "6.8 min")],
                        ["Read ticket and history", "Find the answer", "Write or check the reply", "Decide the next step"],
                        ["#0b5d7a", "#3e4fb8", "#c47f17", "#7c3aa6"], 8.2,
                        notes=[("Saved: 1.2 min a ticket (15%), almost all from the summary and the search.", "b grn"),
                               ("Checking a draft takes about as long as writing a short reply, so drafting alone saves little.", "s")])

FIGS["flow81"] = seq(
    [("Customer", "a finance manager", "merchant"), ("Help desk + copilot", "Freshdesk, our app", "app"),
     ("Search index", "articles, past tickets", "app"), ("AI model", "writes the draft", "partner"), ("Agent", "Priya, new", "user")],
    [(0, 1, "ticket: “Why was GST charged twice on my invoice?”", "msg"),
     (1, 2, "search: this customer’s plan, invoices, similar tickets", "msg"),
     (2, 1, "5 closest passages; best match 0.82 (good)", "ret"),
     (1, 3, "ticket + 5 passages + “answer only from these, cite them”", "msg"),
     (3, 1, "draft reply citing article #214, “GST on upgrades”", "ret"),
     (1, 4, "3-line summary, draft, source link, “good match” tag", "msg"),
     (4, 1, "edits one line; approves", "msg"),
     (1, 0, "reply sent in the agent’s name", "msg"),
     (1, 1, "if best match is below 0.6: show “no suggestion”, not a guess", "self")],
    note="The tag comes from how close the search match was and simple checks, not from the model sounding sure.")


def esc81():
    o = [T(0, 12, "1,000 tickets, of which 30 truly need a senior (legal threat, cancellation, safety). Two settings for the escalation flag:", "s")]
    rows = [("Setting A|flags 60", 27, 33, 3, "catches 27 of 30 (90%); 33 false alarms"),
            ("Setting B|flags 140", 29, 111, 1, "catches 29 of 30 (97%); 111 false alarms")]
    L, W = 110, 330
    for i, (lab, tp, fp, miss, note) in enumerate(rows):
        y = 30 + i * 52
        o.append(lines(L - 8, y + 14, lab, "b", "end", 13))
        x = L
        for v, c in ((tp, "#127a64"), (fp, "#c47f17"), (miss, "#b93a32")):
            w = W * v / 145
            o.append(f'<rect x="{x:.1f}" y="{y}" width="{max(w, 3):.1f}" height="24" fill="{c}" stroke="#fff"/>')
            x += max(w, 3)
        o.append(T(x + 8, y + 16, note, "s"))
    y = 142
    for s, c, x in (("caught", "#127a64", L), ("false alarm: 5 min of a senior’s time", "#c47f17", L + 70), ("missed", "#b93a32", L + 300)):
        o.append(f'<rect x="{x}" y="{y - 9}" width="10" height="10" fill="{c}"/>'); o.append(T(x + 14, y, s, "s"))
    o.append(T(0, 166, "Per 1,000 tickets: B adds 78 false alarms × 5 min = 6.5 senior hours. A misses 2 more real threats.", "b"))
    o.append(T(0, 181, "One missed threat can lose a ₹24-lakh account, so B is cheaper; add keyword rules (“lawyer”, “cancel”) that always escalate.", ""))
    return svg(190, o)
FIGS["esc81"] = esc81()


# ================= Case 8.2 · Low CRM adoption =================
FIGS["strip82"] = strip([("Clarify", "log in vs update"), ("Segment", "tenured reps"), ("Who gains", "value flow"),
                         ("Test causes", "cheap data first"), ("Fix", "remove typing"), ("Measure", "leading, lagging")])
