"""F2 figures ({{SVG:key}} in parts)."""
from f2_figs import FIGS, svg, T, lines, strip, hbars, two_by_two, stacks

TEAL, IND, AMB, RED, GRN, PUR, GREY = "#0b5d7a", "#3e4fb8", "#c47f17", "#b93a32", "#127a64", "#7c3aa6", "#7d8793"


def rect(x, y, w, h, fill, stroke, rx=6, sw=1.3, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def arrow(x1, y1, x2, y2, col=GREY, w=1.5, mid="a"):
    return (f'<defs><marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{col}"/></marker></defs>'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}" marker-end="url(#{mid})"/>')


# ---------- F: what was actually asked (real data) ----------
FIGS["themes"] = hbars([
    ("Project / work deep-dive", 145, "the resume is the script"),
    ("Tell me about yourself", 28, ""),
    ("Why PM (why now)", 23, ""),
    ("Why this company", 21, ""),
    ("Prioritising, trade-offs", 19, ""),
    ("How you use AI", 16, "new in 2026"),
    ("Values and culture", 14, ""),
    ("Conflict, disagreement", 13, ""),
    ("Strengths, weaknesses", 12, ""),
    ("Stress, situational", 12, ""),
    ("Leading, persuading", 8, ""),
    ("Goals in 5 years", 7, ""),
    ("Failure, criticism", 5, "rare to be named, but asked"),
], 145, lw=170, colors=[TEAL, "#3f7f99", "#3f7f99", "#3f7f99", "#3f7f99", PUR] + ["#7fa9ba"] * 7,
    note="Behavioural, HR or resume rounds that touched each theme (285 such rounds, 57 companies; one round can touch several)")


# ---------- F: what the interviewer is scoring ----------
def score():
    cols = [("Ownership", "“I decided…”, “I built…”|clear about your part", "only “we”; can’t say|what you did yourself"),
            ("Judgement", "why this option|and not the other one", "“it just made sense”;|no alternatives named"),
            ("Working with|people", "names the other side’s|view fairly", "blames others;|“they didn’t get it”"),
            ("Self-|awareness", "a real mistake and|what changed after", "a fake weakness;|“I work too hard”"),
            ("Motivation", "a real moment that|led here; knows us", "a template line that|fits any company")]
    o = []; w = 128; gap = 10
    for i, (h, good, bad) in enumerate(cols):
        x = i * (w + gap)
        o.append(rect(x, 2, w, 44, TEAL, TEAL, 5))
        o.append(lines(x + w / 2, 20 if "|" in h else 28, h, "b w", "middle", 13))
        o.append(rect(x, 52, w, 52, "#e7f4f0", GRN, 5, 1))
        o.append(T(x + 7, 66, "Good sign", "b grn", "start", 9.5))
        o.append(lines(x + 7, 80, good, "s", "start", 12.5))
        o.append(rect(x, 110, w, 52, "#fcecea", RED, 5, 1))
        o.append(T(x + 7, 124, "Red flag", "b red", "start", 9.5))
        o.append(lines(x + 7, 138, bad, "s", "start", 12.5))
    return svg(166, o)
FIGS["score"] = score()


# ---------- F: STAR time budget ----------
FIGS["budget"] = stacks(
    [("Weak answer|(3 min)", [115, 25, 20, 20, 0], "180 s: the story, not the speaker’s part"),
     ("Stronger|(2 min)", [20, 10, 55, 20, 15], "120 s: half on what the speaker did")],
    ["Situation", "Task", "Action", "Result", "What I learned"],
    ["#7d8793", "#a3abb4", TEAL, GRN, PUR], 235, lw=110, unit=" s",
    notes=[("Bars are seconds (illustrative). The interviewer can only score what you did, so give that part half the time.", "s")])


# ---------- F: project deep-dive, the grilling tree ----------
def deep():
    o = []
    o.append(rect(250, 4, 180, 40, TEAL, TEAL))
    o.append(lines(340, 20, "Your project, 90 seconds|Why · What · How · Impact · Next", "b w", "middle", 14))
    kids = [("“Why that approach?”", "judgement: what else|you considered"),
            ("“What exactly did|you do?”", "ownership: your part,|not the team’s"),
            ("“What was the|number?”", "honesty: a real figure|or say you don’t know"),
            ("“What went wrong?”", "self-awareness: one|real problem"),
            ("“What would you|change now?”", "product sense: the|next version")]
    w = 128; gap = 10
    for i, (q, chk) in enumerate(kids):
        x = i * (w + gap); cx = x + w / 2
        o.append(f'<path d="M340,44 C340,60 {cx},56 {cx},72" fill="none" stroke="{GREY}" stroke-width="1.3"/>')
        o.append(rect(x, 72, w, 40, "#eef2f6", "#3d4b5c", 5, 1))
        o.append(lines(cx, 89 if "|" in q else 96, q, "b", "middle", 13))
        o.append(lines(cx, 128, chk, "s", "middle", 12.5))
    o.append(rect(0, 158, 680, 26, "#fcecea", RED, 4, 1))
    o.append(T(340, 175, "Every branch can go two or three levels deeper. A line you can’t defend for two minutes should come off the resume.", "b red", "middle", 10.5))
    return svg(188, o)
FIGS["deep"] = deep()


# ---------- F: tell me about yourself as a timeline ----------
def tmay():
    steps = [("Choice 1", "B.Tech, mechanical|(Pune, 2019)", "fixed machines|others gave up on", "#eef2f6", "#3d4b5c"),
             ("Choice 2", "Supply-chain analyst,|FMCG firm, 3 years", "built a tracker;|30 depots use it", "#eef2f6", "#3d4b5c"),
             ("Now", "MBA, XLRI;|summer at a fintech", "shipped a KYC fix:|6% more sign-ups", "#e3f0f5", TEAL),
             ("Why PM", "the tracker showed|I like the user side", "I want to own|the whole problem", "#e7f4f0", GRN),
             ("Why here", "your lending app|for small shops", "depot years: I know|how small shops think", "#f4edf9", PUR)]
    o = []; w = 124; gap = 15
    o.append(rect(0, 2, 680, 22, "#fbf4e6", AMB, 4, 1))
    o.append(T(340, 17, "The thread tying it together: “I keep building small tools that people with messy jobs actually use.”", "b amb", "middle", 10.5))
    for i, (h, a, b, f, s) in enumerate(steps):
        x = i * (w + gap)
        o.append(rect(x, 34, w, 96, f, s, 6))
        o.append(T(x + w / 2, 50, h, "b", "middle", 11.5))
        o.append(lines(x + w / 2, 68, a, "s", "middle", 12.5))
        o.append(lines(x + w / 2, 102, b, "s i", "middle", 12.5))
        if i < 4: o.append(arrow(x + w + 1, 82, x + w + gap - 1, 82, GREY, 1.5, f"tm{i}"))
    o.append(T(0, 148, "Grey = the past, told as choices with a reason. Blue = today. Green and purple = where you’re going and why this company fits.", "s"))
    o.append(T(0, 162, "About 20 seconds a box: 90 to 120 seconds in all. Example is illustrative.", "s"))
    return svg(166, o)
FIGS["tmay"] = tmay()


# ---------- F: conflict, two positions and the shared goal ----------
def conflict():
    o = []
    o.append(rect(0, 4, 250, 62, "#e3f0f5", TEAL))
    o.append(lines(125, 22, "My position (analyst)|“Launch the new pricing page in|all cities on 1 March”", "b", "middle", 13.5))
    o.append(rect(430, 4, 250, 62, "#fbf4e6", AMB))
    o.append(lines(555, 22, "Manager’s position|“Wait till April: sales team isn’t|trained, complaints will spike”", "b", "middle", 13.5))
    o.append(rect(215, 92, 250, 44, "#e7f4f0", GRN))
    o.append(lines(340, 110, "Shared goal both of us cared about|more paid sign-ups without angry customers", "b", "middle", 14))
    o.append(f'<path d="M125,66 C125,84 200,100 215,110" fill="none" stroke="{GREY}" stroke-width="1.4"/>')
    o.append(f'<path d="M555,66 C555,84 480,100 465,110" fill="none" stroke="{GREY}" stroke-width="1.4"/>')
    o.append(arrow(340, 136, 340, 156, GREEN := GRN, 1.8, "cf1"))
    o.append(rect(120, 158, 440, 44, "#fff", GRN, 6, 1.8))
    o.append(lines(340, 176, "Agreed: 2 cities on 1 March, a one-page FAQ for sales,|all cities in April if complaints stay under 2%", "b", "middle", 14))
    o.append(T(0, 222, "Step back from the two positions to the goal you share, then find a test that answers the worry. Illustrative example.", "s"))
    return svg(228, o)
FIGS["conflict"] = conflict()


# ---------- F: failure, the recovery arc ----------
def failarc():
    o = []
    pts = [(100, 44), (250, 118), (430, 88), (590, 34)]
    o.append(f'<path d="M20,32 C60,32 80,38 100,44 C160,76 200,120 250,118 C320,116 370,98 430,88 C500,76 540,44 590,34 C620,28 640,26 670,24" fill="none" stroke="{TEAL}" stroke-width="2.4"/>')
    labs = [("① What went wrong", "Sponsor deck sent 2 weeks|late; ₹1.5 L of ₹4 L lost", RED),
            ("② What I did that week", "Called 11 smaller sponsors;|recovered ₹90,000", AMB),
            ("③ What I changed for good", "A shared tracker with a|deadline owner per sponsor", TEAL),
            ("④ The next time", "Next fest: all 9 decks|out 3 weeks early", GRN)]
    for (x, y), (h, t, c) in zip(pts, labs):
        o.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{c}"/>')
        ty = y + 22 if y < 60 else y - 44
        o.append(T(x, ty, h, "b halo", "middle", 11))
        o.append(lines(x, ty + 14, t, "s halo", "middle", 12.5))
    o.append(T(0, 150, "Most weak answers stop at ①, or jump from ① to “it all worked out”. Points ③ and ④ are what the interviewer is scoring. Illustrative.", "s"))
    return svg(156, o)
FIGS["failarc"] = failarc()


# ---------- F: prioritising, requests on value vs effort ----------
FIGS["prio"] = two_by_two("Effort (team-weeks)", "Value to users and business",
    ["Do soon if there’s room", "Do first", "Say no, explain why", "Plan it properly"],
    [("Fix OTP failures on Jio (3%)", 0.18, 0.86, GRN, "start"),
     ("Dark mode", 0.30, 0.22, GREY, "start"),
     ("Sales head’s custom report", 0.62, 0.30, RED, "start"),
     ("New onboarding flow", 0.72, 0.78, TEAL, "start"),
     ("Referral banner tweak", 0.12, 0.55, AMB, "start")], h=250)


# ---------- F: answer length dial ----------
def dial():
    o = []
    L, R = 20, 660; sc = (R - L) / 300
    X = lambda s: L + s * sc
    zones = [(0, 45, "#fcecea", RED, "Too short", "thin; they must|drag it out"),
             (45, 90, "#fbf4e6", AMB, "A bit short", "fine for a|follow-up"),
             (90, 150, "#e7f4f0", GRN, "About right", "90 s to 2½ min, then|stop and let them ask"),
             (150, 210, "#fbf4e6", AMB, "Getting long", "cut the|situation"),
             (210, 300, "#fcecea", RED, "Rambling", "they stop listening|and plan to interrupt")]
    for a, b, f, s, h, t in zones:
        o.append(f'<rect x="{X(a):.1f}" y="10" width="{X(b) - X(a):.1f}" height="26" fill="{f}" stroke="{s}" stroke-width="1"/>')
        o.append(T((X(a) + X(b)) / 2, 27, h, "b", "middle", 10.5))
        o.append(lines((X(a) + X(b)) / 2, 54, t, "s", "middle", 12.5))
    for s in range(0, 301, 60):
        o.append(T(min(max(X(s), 22), 652), 96, f"{s // 60} min", "s", "middle"))
    return svg(100, o)
FIGS["dial"] = dial()


# ---------- move strips (unnumbered) ----------
FIGS["s_deep"] = strip([("Why", "whose problem"), ("What", "your part"), ("How", "choices, trade-offs"), ("Impact", "number or direction"), ("Next", "what you’d change")])
FIGS["s_tmay"] = strip([("Hook", "one line: who you are"), ("Choices", "2–3, with reasons"), ("Proof", "one result"), ("Why PM", "the thread"), ("Why here", "the fit")])
FIGS["s_whypm"] = strip([("Moment", "when you found it"), ("Evidence", "you’ve done PM-like work"), ("Gap", "what you still need"), ("Why now", "why this step, today")])
FIGS["s_whyco"] = strip([("Used it", "your own experience"), ("A view", "what they do well"), ("A question", "what you’d change"), ("Fit", "why you, over 40 others")])
FIGS["s_prio"] = strip([("The ask", "who wanted what"), ("The goal", "what mattered most"), ("Compare", "value vs effort"), ("Say no well", "reason plus an option"), ("Outcome", "what happened")])
FIGS["s_conf"] = strip([("Two views", "fairly stated"), ("Shared goal", "what both wanted"), ("Test", "data or a small trial"), ("Agree", "and commit"), ("Learn", "what you’d repeat")])
FIGS["s_sw"] = strip([("Strength", "one, with proof"), ("Weakness", "real and relevant"), ("Cost", "when it hurt"), ("Fix", "what you do now"), ("Progress", "evidence it works")])
FIGS["s_fail"] = strip([("Own it", "your part, early"), ("Size it", "what it cost"), ("Recover", "what you did"), ("Change", "the lasting fix"), ("Proof", "the next time")])
FIGS["s_infl"] = strip([("Need", "what had to happen"), ("Their view", "what they cared about"), ("Offer", "make it easy for them"), ("Result", "what moved")])
FIGS["s_five"] = strip([("Near term", "the skill to build"), ("3–5 years", "the scope you want"), ("Link", "why this job leads there")])
