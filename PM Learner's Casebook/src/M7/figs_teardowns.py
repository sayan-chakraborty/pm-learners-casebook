"""Teardown figures for M7; imported at the end of m7_figs.py."""
from m7_figs import FIGS, svg, T, lines, hbars, loop, two_by_two, seq  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R, P, I  # noqa: F401


def ladder(steps, title, h=196):
    """steps: (name, sub, price, colours) rising left to right."""
    n = len(steps); w = (680 - 12 * (n - 1)) / n
    o = [MK, T(0, 12, title, "b")]
    for i, (name, sub, price, (fill, st)) in enumerate(steps):
        x = i * (w + 12); top = 96 - i * 24; hh = h - 16 - top
        o.append(f'<rect x="{x:.1f}" y="{top}" width="{w:.1f}" height="{hh}" rx="6" fill="{fill}" stroke="{st}" stroke-width="1.4"/>')
        o.append(T(x + w / 2, top + 18, name, "b", "middle"))
        for j, l in enumerate(sub.split("|")): o.append(T(x + w / 2, top + 34 + j * 13, l, "s", "middle"))
        o.append(T(x + w / 2, h - 28, price, "b grn", "middle"))
    return svg(h, o)


# ---------- Duolingo ----------
FIGS["flow_duo"] = seq(
    [("Neha", "phone, office lift", "user"), ("Duolingo app", "lessons, streak", "app"), ("Birdbrain", "picks exercises", "app"),
     ("Reminder system", "learns what works", "app"), ("Her league", "30 learners", "partner")],
    [(3, 0, "8:50 am: “Your 212-day streak is waiting”", "msg"),
     (0, 1, "opens; taps today’s lesson", "msg"),
     (1, 2, "what does she know? 212 days of answers", "msg"),
     (2, 1, "15 exercises she’ll get right about 4 times in 5", "ret"),
     (0, 1, "answers; misses 2 past-tense verbs", "msg"),
     (1, 2, "update: past tense is fading for her", "msg"),
     (1, 0, "done in 3 minutes: +15 points, streak 213", "ret"),
     (1, 4, "her points added to this week’s table", "msg"),
     (4, 0, "“You moved up to 4th”", "ret"),
     (3, 3, "which message and time made her open today?", "self")],
    note="Each lesson is sized to be finished in a lift ride; the reminder is chosen to catch tomorrow’s lift ride.")

FIGS["loop_duo"] = loop(["A short lesson|2–5 minutes", "Streak and points|go up", "League and friends|a reason to compete",
                         "Reminder|at her usual time", "Opens again|tomorrow"],
                        "Duolingo’s habit loop|make tomorrow easy", bw=150, h=230)

# ---------- HealthifyMe ----------
FIGS["flow_hm"] = seq(
    [("Neha", "lunch at her desk", "user"), ("HealthifyMe app", "diary, plan", "app"), ("Photo AI", "dishes, portions", "app"),
     ("AI coach", "tips from the log", "app"), ("Dietitian", "150–250 clients", "partner")],
    [(0, 1, "photo of her lunch thali", "msg"),
     (1, 2, "the image", "msg"),
     (2, 1, "dal, 2 rotis, rice, sabzi: about 640 kcal", "ret"),
     (1, 0, "“Is this right?” with each portion shown", "ret"),
     (0, 1, "edits: 1 roti, not 2", "msg"),
     (1, 1, "today: 1,420 of her 1,600 kcal", "self"),
     (1, 3, "today’s log and her goal", "msg"),
     (3, 0, "“Low on protein today: add curd at dinner”", "ret"),
     (1, 4, "her week, summarised, for review", "msg"),
     (4, 0, "Saturday call: a plan for the wedding week", "msg"),
     (0, 1, "coaching plan, about ₹1,000 a month", "money")],
    note="The AI does the counting; the dietitian does the judgement and the checking-in.")

FIGS["ladder_hm"] = ladder([("Free", "calorie and step|tracking, photo log", "₹0", G), ("AI coach", "tips from your log,|chat any time", "low monthly fee", B),
                            ("Human coach", "a dietitian or trainer,|weekly calls", "about ₹1,000 a month", A),
                            ("Metabolic plans", "glucose sensor, doctors,|weight-loss drug support", "several thousand ₹", P)],
                           "HealthifyMe’s ladder: each step adds more human time, and costs more (price bands illustrative)")

# ---------- Cult.fit ----------
FIGS["flow_cult"] = seq(
    [("Arjun", "member, Bengaluru", "user"), ("cult app", "slots, waitlist", "app"), ("HSR centre", "franchise-run", "partner"),
     ("Trainer", "runs the class", "partner")],
    [(0, 1, "books tomorrow’s 7 am strength class", "msg"),
     (1, 1, "25 of 25 places taken: waitlist number 3", "self"),
     (1, 0, "“You’re number 3 on the waitlist”", "ret"),
     (1, 1, "two members cancel before 9 pm: he moves in", "self"),
     (1, 0, "“Confirmed” at 9:04 pm", "ret"),
     (0, 2, "6:55 am: checks in with a QR scan", "msg"),
     (2, 1, "attended: no no-show mark", "msg"),
     (3, 0, "45-minute class, his effort shown on a screen", "msg"),
     (1, 0, "rate it; book the next one", "ret"),
     (0, 1, "cultpass, a few thousand ₹ a month", "money"),
     (1, 2, "a share of fees to the centre’s owner", "money")],
    note="The scarce thing is a 7 am place: waitlists and no-show rules keep every one of them filled.")


def franchise():
    o = [MK]
    cols = [(6, "Cult runs the centre", B, [("Cult pays", "b"), ("rent, trainers, upkeep", ""), ("", ""), ("Cult keeps", "b"), ("all the fees", ""), ("", ""), ("Risk: an empty centre", "b red"), ("is Cult’s loss", "red")]),
            (352, "A franchisee runs it", G, [("The owner pays", "b"), ("rent, trainers, upkeep", ""), ("", ""), ("Cult gets", "b"), ("a platform and management fee", ""), ("", ""), ("Risk: shared; Cult grows", "b grn"), ("with less of its own money", "grn")])]
    for x, h, (fill, st), rows in cols:
        o.append(f'<rect x="{x}" y="6" width="322" height="160" rx="6" fill="{fill}" stroke="{st}" stroke-width="1.4"/>')
        o.append(T(x + 161, 26, h, "b", "middle"))
        for i, (s, c) in enumerate(rows): o.append(T(x + 161, 46 + i * 14, s, c, "middle"))
    o.append(T(0, 186, "About 76% of the centres Cult.fit added in FY26 were franchise-owned (DRHP, July 2026).", "b acc"))
    return svg(194, o)
FIGS["franchise"] = franchise()

# ---------- Practo ----------
FIGS["flow_practo"] = seq(
    [("Rahul", "patient, Hyderabad", "user"), ("Practo app", "search, booking", "app"), ("Clinic software", "calendar, records", "app"),
     ("Dr Rao", "dermatologist", "partner"), ("Lab, pharmacy", "tests, medicines", "network")],
    [(0, 1, "searches “skin doctor near me”", "msg"),
     (1, 0, "doctors with ratings, fees, next free slot", "ret"),
     (0, 1, "books 6:30 pm today", "msg"),
     (1, 2, "booking lands in the clinic’s calendar", "msg"),
     (2, 0, "reminder at 5 pm, with directions", "msg"),
     (0, 3, "sees Dr Rao in person", "msg"),
     (3, 2, "types the prescription into the software", "msg"),
     (2, 0, "prescription in his app", "ret"),
     (0, 4, "orders the cream and a blood test", "msg"),
     (0, 3, "consultation fee, about ₹600", "money"),
     (3, 1, "pays for the software and a better listing", "money")],
    note="Practo earns from both sides: patients bring doctors busy calendars; doctors pay for software and visibility.")


def practo_money():
    o = [MK]
    o.append(box(262, 70, 156, 56, *B, [("Practo", "b"), ("₹234 Cr revenue, FY25", "s")]))
    left = [(8, "Doctors and clinics", "software, listings, ads"), (100, "Patients", "online consults, tests")]
    right = [(8, "Employers, insurers", "health plans for staff"), (100, "Hospitals", "bookings, software")]
    for y, h, s in left:
        o.append(box(6, y, 170, 50, *G, [(h, "b"), (s, "s")]))
        o.append(f'<line x1="176" y1="{y + 25}" x2="258" y2="{90 + (y > 50) * 16}" class="money" marker-end="url(#pg)"/>')
    for y, h, s in right:
        o.append(box(504, y, 170, 50, *GR, [(h, "b"), (s, "s")]))
        o.append(f'<line x1="504" y1="{y + 25}" x2="422" y2="{90 + (y > 50) * 16}" class="money" marker-end="url(#pg)"/>')
    o.append(T(340, 176, "Many small streams, none of them large: the reason it took until FY25 to make an operating profit.", "b acc", "middle"))
    return svg(186, o)
FIGS["practo_money"] = practo_money()

# ---------- PhysicsWallah ----------
FIGS["flow_pw"] = seq(
    [("Aman", "Class 11, Patna", "user"), ("YouTube", "free lectures", "partner"), ("PW app", "batches, tests", "app"),
     ("Live batch", "teachers, doubts", "app"), ("Vidyapeeth", "offline centre", "network")],
    [(0, 1, "watches a free 2-hour physics lecture", "msg"),
     (1, 0, "teacher mentions the JEE batch; link below", "ret"),
     (0, 2, "installs; free notes and a mock test", "msg"),
     (2, 0, "score 42 of 120: weak in rotation", "ret"),
     (0, 2, "buys a JEE batch, about ₹4,000 a year", "money"),
     (2, 3, "adds him to live classes and weekly tests", "msg"),
     (3, 0, "all-India rank in the weekly test: 12,400", "ret"),
     (0, 3, "sends a photo of a doubt at 11 pm", "msg"),
     (3, 0, "answer by a doubt-solver, or AI first", "ret"),
     (0, 4, "visits the Patna centre with his parents", "msg"),
     (0, 4, "parents pay about ₹80,000 a year", "money")],
    note="Free video brings students in; tests show them where they stand; parents pay for the classroom.")


def pw_growth():
    o = [T(0, 12, "PhysicsWallah, FY25 → FY26", "b")]
    rows = [("Revenue", 2887, 3900, "₹{:,} Cr", 4000, "#0b5d7a"), ("Paying students (lakh)", 44.6, 53.4, "{:g} lakh", 60, "#127a64")]
    for i, (lab, a, b, fmt, mx, col) in enumerate(rows):
        y = 26 + i * 56
        o.append(T(0, y + 18, lab, "b"))
        for j, (v, yr) in enumerate([(a, "FY25"), (b, "FY26")]):
            w = 380 * v / mx
            o.append(f'<rect x="180" y="{y + j * 22}" width="{w:.1f}" height="18" rx="2" fill="{col}" opacity="{0.55 + 0.45 * j}"/>')
            o.append(T(186 + w, y + 14 + j * 22, f"{yr}: " + fmt.format(v), "b"))
    o.append(T(0, 148, "Net loss narrowed from ₹243 Cr to ₹24 Cr; operating profit rose to ₹549 Cr. Offline: 4.7 lakh of the 53.4 lakh.", "b acc"))
    return svg(156, o)
FIGS["pw_growth"] = pw_growth()

# ---------- comparison ----------
FIGS["pos2x2"] = two_by_two("how often people use it: an occasional need → a daily habit", "who delivers the value",
                            ["occasional, expert-led", "daily, expert-led", "occasional, the app alone", "daily, the app alone"],
                            [("Practo", 0.12, 0.88, "#0b5d7a", "start"), ("Tata 1mg", 0.22, 0.34, "#0b5d7a", "start"),
                             ("Cult.fit", 0.55, 0.82, "#c47f17", "start"), ("PhysicsWallah", 0.8, 0.66, "#127a64", "end"),
                             ("HealthifyMe", 0.70, 0.42, "#127a64", "start"), ("Duolingo", 0.9, 0.12, "#127a64", "end"),
                             ("YouTube workouts", 0.62, 0.06, "#9aa3ad", "end")], h=250)
