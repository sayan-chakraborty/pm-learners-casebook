"""Case and guesstimate figures for M7; imported at the end of m7_figs.py."""
from m7_figs import FIGS, svg, T, lines, strip, hbars, seq  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R, P, I  # noqa: F401


def curves(series, xs, L=46, R=520, Tp=14, Bt=170, h=196, ymax=100, notes=(), step=25):
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
        o.append(T(R + 8, Y(vals[-1]) + 4 + dy, f"{lab}: {vals[-1]}%", "b", fill=col))
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


# ================= Case 7.1 · AI assistant for doctors =================
FIGS["strip71"] = strip([("Clarify", "who pays, which clinic"), ("Size", "minutes, rupees"), ("Who", "Dr Kulkarni, 9–1"),
                         ("Design", "brief in 30 s"), ("Risk tiers", "alone, confirm, never"), ("Measure", "time and misses")])


def clinicmins():
    sc = 112  # units per minute
    x0 = 120
    rows = [("Today", [("Same 8 questions", 1.2, "#c47f17"), ("Reading the folder", 1.0, "#b93a32"), ("Examine and decide", 2.0, "#0b5d7a"), ("Write it up", 0.8, "#5b6470")]),
            ("With the brief", [("", 0.3, "#c47f17"), ("", 0.4, "#b93a32"), ("Examine and decide", 2.0, "#0b5d7a"), ("Write it up", 0.8, "#5b6470")])]
    o = [T(0, 12, "One consultation in a busy clinic, in minutes (illustrative)", "b")]
    for r, (lab, segs) in enumerate(rows):
        y = 26 + r * 58
        o.append(T(x0 - 8, y + 21, lab, "b", "end"))
        x = x0; tot = 0
        for name, m, col in segs:
            w = m * sc
            o.append(f'<rect x="{x:.1f}" y="{y}" width="{w - 2:.1f}" height="32" fill="{col}" rx="2"/>')
            if name: o.append(T(x + w / 2, y + 14, name, "b w", "middle")); o.append(T(x + w / 2, y + 27, f"{m:g} min", "w", "middle"))
            x += w; tot += m
        o.append(T(x + 6, y + 21, f"= {tot:g} min", "b"))
    o.append(T(x0 + 2, 26 + 58 + 46, "0.3 min: read the brief · 0.4 min: ask only what is missing", "s"))
    o.append(T(0, 160, "Saved: 1.5 min a patient. × 50 patients = 75 minutes a morning. × 25 clinic days = about 31 hours a month.", "b grn"))
    o.append(T(0, 175, "The doctor can see about 15 more patients a morning, or go home an hour earlier.", "b acc"))
    return svg(184, o)
FIGS["clinicmins"] = clinicmins()


FIGS["flow71"] = seq(
    [("Mrs Joshi", "patient, 58", "user"), ("Front desk", "tablet, QR code", "app"), ("Assistant", "reads, sorts, drafts", "app"),
     ("Dr Kulkarni", "40 patients a morning", "partner"), ("ABHA records", "labs linked by consent", "network")],
    [(0, 1, "answers 8 questions in Marathi, about a minute", "msg"),
     (0, 1, "photos of 6 old reports and prescriptions", "msg"),
     (0, 4, "scans the clinic QR: yes, share my lab records", "msg"),
     (4, 2, "two lab reports, already typed", "ret"),
     (1, 2, "answers and photos", "msg"),
     (2, 2, "sort by date, pull out values, translate", "self"),
     (2, 3, "one-page brief; every value linked to its photo", "ret"),
     (3, 3, "reads it in 30 s; taps a red value to see the report", "self"),
     (3, 0, "calls her in; asks only what is missing", "msg"),
     (3, 2, "correction: “allergy is sulfa, not penicillin”", "msg"),
     (2, 2, "correction saved as a new test case", "self")],
    note="The doctor is the check at ⑧: nothing from the assistant reaches the patient without him.")


def tiers():
    rows = [("Never", "the assistant must not do it", R,
             ["Say what the illness is", "Suggest a medicine or dose", "Explain a result to the patient", "Drop a report as irrelevant"]),
            ("Suggests; the doctor confirms", "shown with its source, one tap to check", A,
             ["Flag values out of range", "List current medicines", "Allergy alerts", "Two-line history summary"]),
            ("Does it alone", "easy to spot and undo if wrong", G,
             ["Sort reports by date", "Type up the questionnaire", "Translate Marathi to English", "Count pages, find duplicates"])]
    o = [MK]
    for i, (h, sub, (fill, st), items) in enumerate(rows):
        y = 6 + i * 62
        o.append(f'<rect x="46" y="{y}" width="634" height="54" rx="6" fill="{fill}" stroke="{st}" stroke-width="1.4"/>')
        o.append(T(58, y + 22, h, "b", fill=st)); o.append(T(58, y + 38, sub, "s"))
        for j, it in enumerate(items):
            cx = 290 + (j % 2) * 200; cy = y + 22 + (j // 2) * 18
            o.append(T(cx, cy, "• " + it, ""))
    o.append('<line x1="18" y1="186" x2="18" y2="10" stroke="#b93a32" stroke-width="2.4" marker-end="url(#pr)"/>')
    o.append(f'<text x="12" y="98" text-anchor="middle" class="b red" transform="rotate(-90 12 98)">more harm if wrong</text>')
    return svg(194, o)
FIGS["tiers"] = tiers()


# ================= Case 7.2 · HealthifyMe early drop-off =================
FIGS["strip72"] = strip([("Clarify", "since when, which step"), ("Find the step", "the funnel"), ("Who", "Neha, first week"),
                         ("Aha moment", "3 meals, 3 days"), ("Bets", "shorter, faster, nudged"), ("Measure", "day-7 and kg")])


def onb():
    steps = ["Installed", "Finished the questions", "Logged a first meal", "Came back on day 2", "Active on day 7"]
    before = [100, 55, 38, 20, 12]; after = [100, 85, 70, 40, 20]
    o = [T(0, 12, "Out of 100 installs (illustrative)", "b"),
         '<rect x="330" y="3" width="12" height="10" fill="#9aa3ad"/>', T(347, 12, "today: 22 questions first", "s"),
         '<rect x="500" y="3" width="12" height="10" fill="#127a64"/>', T(517, 12, "5 questions, photo first", "s")]
    for i, (s, b, a) in enumerate(zip(steps, before, after)):
        y = 24 + i * 34
        o.append(T(160, y + 18, s, "b", "end"))
        o.append(f'<rect x="170" y="{y + 2}" width="{3.9 * b:.1f}" height="13" fill="#9aa3ad" rx="2"/>')
        o.append(T(176 + 3.9 * b, y + 13, str(b), "b"))
        o.append(f'<rect x="170" y="{y + 16}" width="{3.9 * a:.1f}" height="13" fill="#127a64" rx="2"/>')
        o.append(T(176 + 3.9 * a, y + 27, str(a), "b grn"))
    o.append(T(0, 204, "Biggest loss today: the 45 who never finish the questions. Cutting them helps only if the first meal log is also quick.", "b acc"))
    return svg(212, o)
FIGS["onb"] = onb()


def fogg():
    L, Rr, Tp, Bt = 60, 520, 16, 196
    X = lambda a: L + (Rr - L) * a
    Y = lambda m: Bt - (Bt - Tp) * m
    o = [MK, f'<line x1="{L}" y1="{Bt}" x2="{Rr}" y2="{Bt}" stroke="#4a5563" marker-end="url(#pa)"/>',
         f'<line x1="{L}" y1="{Bt}" x2="{L}" y2="{Tp}" stroke="#4a5563" marker-end="url(#pa)"/>']
    pts = [(a / 100, min(1, 0.09 / (a / 100 + 0.02))) for a in range(8, 101, 2)]
    d = " ".join(f"{'M' if i == 0 else 'L'}{X(a):.1f},{Y(m):.1f}" for i, (a, m) in enumerate(pts))
    o.append(f'<path d="{d}" fill="none" stroke="#3e4fb8" stroke-width="2.6"/>')
    o.append(T(X(0.17), Y(0.62), "action line", "b fwc halo"))
    o.append(T(X(0.55), Y(0.75), "above the line: she does it,", "b grn")); o.append(T(X(0.55), Y(0.75) + 13, "if something prompts her", "grn"))
    o.append(T(X(0.42), Y(0.03), "below the line: she doesn’t", "b red"))
    o.append(f'<circle cx="{X(0.18):.1f}" cy="{Y(0.92):.1f}" r="6" fill="#0b5d7a"/>')
    o.append(T(X(0.18) + 10, Y(0.92) + 2, "Monday, week 1", "b halo", fill="#0b5d7a")); o.append(T(X(0.18) + 10, Y(0.92) + 16, "22 questions: just made it", "halo"))
    for a_, t1, t2, col, dy in [(0.25, "Wednesday", "typing every item: skips", "#b93a32", 20), (0.85, "Wednesday, photo log", "one tap at lunch: does it", "#127a64", -40)]:
        o.append(f'<circle cx="{X(a_):.1f}" cy="{Y(0.30):.1f}" r="6" fill="{col}"/>')
        o.append(T(X(a_), Y(0.30) + dy, t1, "b halo", "middle", fill=col)); o.append(T(X(a_), Y(0.30) + dy + 14, t2, "halo", "middle"))
    o.append(f'<path d="M{X(0.25) + 10:.1f},{Y(0.30):.1f} L{X(0.85) - 10:.1f},{Y(0.30):.1f}" class="msg" marker-end="url(#pa)"/>')
    o.append(T(X(0.55), Y(0.30) - 8, "make it easier", "b halo", "middle"))
    o.append(T((L + Rr) / 2, Bt + 16, "ability: hard → easy", "b", "middle"))
    o.append(f'<text x="30" y="{(Tp + Bt) / 2:.1f}" text-anchor="middle" class="b" transform="rotate(-90 30 {(Tp + Bt) / 2:.1f})">motivation: low → high</text>')
    # prompt panel
    o.append(f'<rect x="540" y="30" width="140" height="130" rx="6" fill="#e8eaf8" stroke="#3e4fb8"/>')
    for i, (s, c) in enumerate([("The prompt", "b fwc"), ("1:15 pm, her usual", ""), ("lunch time:", ""), ("“Snap your lunch”", "b"),
                                ("No prompt, no action,", "s"), ("even above the line.", "s")]):
        o.append(T(610, 52 + i * 17, s, c, "middle"))
    return svg(220, o)
FIGS["fogg"] = fogg()


FIGS["aha"] = curves(
    [("Logged 3 meals in first 3 days", [100, 78, 64, 55, 50, 47, 45], "#127a64", -4),
     ("Didn’t", [100, 42, 26, 19, 15, 13, 12], "#b93a32", 4)],
    ["day 0", "day 1", "day 3", "day 7", "day 14", "day 21", "day 30"], R=440,
    notes=[(140, 108, "same app, same month:", "b"), (140, 121, "the gap opens in the first 3 days", "")], h=190)


# ================= Case 7.3 · Duolingo engagement drop =================
FIGS["strip73"] = strip([("Clarify", "metric and scope"), ("Rule out", "season, rivals"), ("Find where", "US iOS, in-lesson"),
                         ("Add it up", "can one test do 15%?"), ("Stop it", "flag off today"), ("Fix and test", "read it properly")])


def tree73():
    o = [MK, '<g class="c">']
    o.append(box(4, 72, 170, 62, *B, [("Weekly learners", "b"), ("finishing ≥ 1 lesson", ""), ("100 → 85 (−15%)", "b red")]))
    kids = [(8, "Returning learners", "a week", "flat", G), (80, "× start a lesson", "90% → 90%", "flat", G),
            (152, "× finish it", "80% → 68%", "−15%: here", R)]
    for y, h, s, n, col in kids:
        o.append(f'<line x1="174" y1="103" x2="236" y2="{y + 24}" class="ln" marker-end="url(#pa)"/>')
        o.append(box(240, y, 180, 50, *col, [(h, "b"), (s + " · " + n, "")]))
    o.append(f'<line x1="420" y1="176" x2="468" y2="176" class="ln" marker-end="url(#pa)"/>')
    o.append(box(472, 146, 204, 60, *A, [("Where in the lesson?", "b"), ("exits jump on speaking", ""), ("screens after the flag", "")]))
    o.append(T(4, 14, "Illustrative. Returning × start × finish:", "s"))
    o.append(T(4, 28, "100 × 0.90 × 0.80 = 72 lessons done", "s"))
    o.append(T(4, 42, "100 × 0.90 × 0.68 = 61: the whole 15%", "b red"))
    o.append("</g>")
    return svg(212, o)
FIGS["tree73"] = tree73()


def exits73():
    cats = ["Translate", "Listen", "Speak", "Match pairs", "Other"]
    before = [24, 20, 22, 12, 22]; after = [12, 10, 60, 6, 12]
    o = [T(0, 12, "Where learners quit a lesson, share of all exits (%, illustrative)", "b"),
         '<rect x="440" y="3" width="12" height="10" fill="#9aa3ad"/>', T(457, 12, "before the flag", "s"),
         '<rect x="552" y="3" width="12" height="10" fill="#b93a32"/>', T(569, 12, "with the flag", "s")]
    for i, (c, b, a) in enumerate(zip(cats, before, after)):
        y = 24 + i * 30
        o.append(T(110, y + 16, c, "b", "end"))
        o.append(f'<rect x="120" y="{y}" width="{6 * b}" height="12" fill="#9aa3ad" rx="2"/>'); o.append(T(126 + 6 * b, y + 10, str(b), "s"))
        o.append(f'<rect x="120" y="{y + 13}" width="{6 * a}" height="12" fill="#b93a32" rx="2"/>'); o.append(T(126 + 6 * a, y + 23, str(a), "b red"))
    o.append(T(0, 184, "Six in ten exits now happen on a speaking screen. Next check: are those exits at commute and office hours?", "b acc"))
    return svg(192, o)
FIGS["exits73"] = exits73()


def abci():
    L, Rr = 250, 670
    lo, hi = -2, 9
    X = lambda v: L + (Rr - L) * (v - lo) / (hi - lo)
    rows = [("Lesson finish rate", "71.0% → 78.4%", 7.4, 6.9, 7.9, "#0b5d7a"),
            ("Weekly learners (the goal)", "64.1% → 66.0%", 1.9, 1.3, 2.5, "#127a64"),
            ("Still learning on day 28", "48.2% → 48.5%", 0.3, -0.3, 0.9, "#5b6470")]
    o = [T(0, 12, "Variant minus control, percentage points, with the 95% range (about 50,000 users in each group; illustrative)", "b")]
    for v in range(lo, hi + 1):
        o.append(f'<line x1="{X(v):.1f}" y1="24" x2="{X(v):.1f}" y2="118" stroke="{"#4a5563" if v == 0 else "#eef0f2"}" stroke-width="{1.4 if v == 0 else 1}"/>')
        o.append(T(X(v), 132, f"{v:+d}" if v else "0", "s", "middle"))
    for i, (lab, sub, m, a, b, col) in enumerate(rows):
        y = 40 + i * 30
        o.append(T(L - 12, y + 1, lab, "b", "end")); o.append(T(L - 12, y + 13, sub, "s", "end"))
        o.append(f'<line x1="{X(a):.1f}" y1="{y}" x2="{X(b):.1f}" y2="{y}" stroke="{col}" stroke-width="3"/>')
        o.append(f'<circle cx="{X(m):.1f}" cy="{y}" r="5.5" fill="{col}"/>')
        lab2 = f"{m:+.1f} ({a:+.1f} to {b:+.1f})"
        if X(b) + 150 > 680: o.append(T(X(a) - 8, y + 4, lab2, "b", "end", fill=col))
        else: o.append(T(X(b) + 8, y + 4, lab2, "b", fill=col))
    o.append(f'<rect x="0" y="142" width="680" height="30" rx="5" fill="#fcecea" stroke="#b93a32"/>')
    o.append(T(10, 161, "Safety check (guardrail) fails: speaking exercises done per learner a week 3.1 → 1.2 (−61%).", "b red"))
    o.append(T(0, 190, "The range for day 28 crosses zero: no proven change. Finish rate rose most, partly because skipping makes a lesson shorter.", "b acc"))
    return svg(198, o)
FIGS["abci"] = abci()


def novelty():
    L, Rr, Tp, Bt = 50, 520, 16, 150
    wk = [3.6, 2.5, 2.0, 1.9, 1.9, 1.8]
    X = lambda i: L + (Rr - L) * i / 5
    Y = lambda v: Bt - (Bt - Tp) * v / 4
    o = [f'<line x1="{L}" y1="{Bt}" x2="{Rr}" y2="{Bt}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{Bt}" stroke="#4a5563"/>']
    for v in range(0, 5):
        o.append(T(L - 6, Y(v) + 4, f"+{v}" if v else "0", "s", "end"))
        if v: o.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{Rr}" y2="{Y(v):.1f}" stroke="#eef0f2"/>')
    band = [(X(i), Y(v + 0.6)) for i, v in enumerate(wk)] + [(X(i), Y(v - 0.6)) for i, v in reversed(list(enumerate(wk)))]
    o.append('<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in band) + '" fill="#e1f2ec"/>')
    d = " ".join(f"{'M' if i == 0 else 'L'}{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(wk))
    o.append(f'<path d="{d}" fill="none" stroke="#127a64" stroke-width="2.6"/>')
    for i, v in enumerate(wk):
        o.append(f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="3" fill="#127a64"/>'); o.append(T(X(i), Bt + 15, f"week {i + 1}", "s", "middle"))
    o.append(T(X(0) + 10, Y(3.6) - 4, "week 1: +3.6 (new button, people try it)", "b halo"))
    o.append(T(X(3), Y(1.9) - 18, "settles near +1.9", "b grn halo", "middle"))
    o.append(T(Rr + 10, 40, "Reading after week 1", "b")); o.append(T(Rr + 10, 54, "promises nearly twice", "")); o.append(T(Rr + 10, 68, "the lasting effect.", ""))
    o.append(T(Rr + 10, 92, "Run 2–4 full weeks;", "b")); o.append(T(Rr + 10, 106, "look at the trend,", "")); o.append(T(Rr + 10, 120, "not one number.", ""))
    return svg(172, o)
FIGS["novelty"] = novelty()


# ================= Guesstimates =================
FIGS["stripg71"] = strip([("Unit", "data, both ways"), ("Approach", "people who call"), ("Tree", "users × hours × MB"),
                          ("Numbers", "a reason each"), ("Check", "Zoom’s own minutes"), ("Range", "users, share")])


def updown():
    o = [MK, '<g class="c">']
    o.append(box(250, 94, 180, 60, *A, [("Zoom server", "b"), ("receives each video once,", ""), ("sends it to everyone else", "s")]))
    people = [("Asha", 42), ("Ravi", 106), ("Meena", 170), ("Joseph", 234)]
    for i, (n, y) in enumerate(people):
        o.append(box(20, y - 20, 110, 40, *G, [(n, "b"), ("laptop", "s")]))
        o.append(f'<line x1="130" y1="{y - 8}" x2="246" y2="{110 + i * 9}" class="msg" marker-end="url(#pa)"/>')
        o.append(f'<line x1="250" y1="{118 + i * 9}" x2="134" y2="{y + 6}" stroke="#127a64" stroke-width="2.2" marker-end="url(#pg)"/>')
    o.append('<line x1="20" y1="10" x2="50" y2="10" class="msg"/>'); o.append(T(56, 14, "up: 1 video each, about 1 Mbps", "b"))
    o.append('<line x1="250" y1="10" x2="280" y2="10" stroke="#127a64" stroke-width="2.2"/>'); o.append(T(286, 14, "down: 3 small videos each, about 1.5 Mbps", "b grn"))
    o.append(f'<rect x="460" y="54" width="216" height="150" rx="6" fill="#f3f3ee" stroke="#6b6a52"/>')
    for i, (s, c) in enumerate([("A 4-person call, per hour", "b"), ("in: 4 × 1 Mbps = 4 Mbps", ""), ("out: 4 × 1.5 Mbps = 6 Mbps", ""),
                                ("total: 10 Mbps, 2.5 per person", "b"), ("", ""), ("per person-hour:", ""),
                                ("2.5 × 3,600 ÷ 8 ≈ 1.1 GB", "b grn"), ("The casebook counted 0.45 GB,", "red"), ("one direction only.", "red")]):
        o.append(T(470, 74 + i * 15, s, c))
    o.append("</g>")
    return svg(262, o)
FIGS["updown"] = updown()

FIGS["gtree71"] = etree([("≈ 3 Cr", "white-collar", "workers"), ("× 40% on", "a video call", "on a weekday"), ("× 30% Zoom", "(Teams, Meet", "lead offices)"),
                         ("= 36 lakh", "× 1.2 hours", "= 43 lakh hours"), ("× 1.1 GB", "per person-hour", "up + down"), ("≈ 4,800 TB", "a weekday", "range 2,000–8,000")],
                        [("Check (card 5)", "b"), ("Zoom’s 2020 peak: 3.3 trillion minutes a year", ""),
                         ("≈ 15 Cr hours a day, worldwide.", ""), ("Ours: 43 lakh ≈ 3% of that. Plausible.", "b grn"),
                         ("Casebook: 4.5 Cr hours ≈ 30%. Too high.", "red")],
                        [("Range (card 6): the swing factors", "b"), ("share on a call, and Zoom’s share", ""),
                         ("25% × 20% → about 2,000 TB", "b"), ("50% × 40% → about 8,000 TB", "b"), ("Webinars would add one-to-many load", "")],
                        h=172, swing=2)

FIGS["stripg72"] = strip([("Unit", "meetings, not joins"), ("Approach", "from Meet’s users"), ("Tree", "users × joins ÷ size"),
                          ("Numbers", "a reason each"), ("Check", "Google’s 2020 figure"), ("Range", "size of a meeting")])

FIGS["gtree72"] = etree([("30 Cr", "monthly", "Meet users"), ("× 35% use it", "on a weekday", "= 10.5 Cr"), ("× 2 joins", "each a day", "= 21 Cr joins"),
                         ("÷ 3.5 people", "per meeting", "on average"), ("≈ 6 Cr", "meetings", "a weekday"), ("3–11 Cr", "a weekday", "the range")],
                        [("Check (card 5)", "b"), ("Google, April 2020: 10 Cr daily", ""), ("meeting participants. Ours: 10.5 Cr.", "b grn"),
                         ("Casebook: 84 Cr users, 168 Cr meetings,", "red"), ("about 28 times too many.", "red")],
                        [("Range (card 6): the swing factor", "b"), ("people per meeting, and weekday use", ""),
                         ("5 people, 25% daily → about 3 Cr", "b"), ("2.5 people, 45% daily → about 11 Cr", "b")],
                        h=176, swing=3)
