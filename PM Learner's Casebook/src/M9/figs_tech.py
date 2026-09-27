"""M9 technology figures (releases, flags, staged roll-outs, observability, Tatkal capstone); imported at the end of m9_figs.py."""
from m9_figs import FIGS, svg, T, lines, hbars, waterfall, loop, two_by_two, seq, strip  # noqa: F401
from figlib import *  # noqa: F401,F403
from figlib import box, MK, G, B, A, GR, R, P, I, vbars, arr, curves, etree, stacks


# ================= A. mobile releases =================
def webmob():
    o = [MK, '<g class="c">']
    o.append(T(0, 12, "A website: one copy, on your servers", "b acc"))
    o.append(box(0, 22, 150, 40, *B, [("Engineer ships", "b"), ("a new version", "s")], lh=13))
    o.append(box(200, 22, 150, 40, *G, [("Every visitor", "b"), ("gets it on reload", "s")], lh=13))
    o.append(arr(152, 42, 196, 42)); o.append(T(174, 36, "minutes", "s", "middle"))
    o.append(box(390, 22, 290, 40, *G, [("A bug? Put the old version back", "b"), ("in minutes; everyone runs the same code", "s")], lh=13))
    o.append(T(0, 90, "A mobile app: a copy on every phone", "b red"))
    xs = [(0, "Build", "tested and signed", B), (130, "Store review", "Apple: hours to days", A), (260, "Phones update", "over days and weeks", B)]
    for i, (x, t, sub, c) in enumerate(xs):
        o.append(box(x, 100, 116, 40, *c, [(t, "b"), (sub, "s")], lh=13))
        o.append(arr(x + 117, 120, x + 128, 120))
    o.append(box(390, 100, 290, 40, *R, [("Old versions live for months; a bug", "b"), ("is fixed by a new version or a server switch", "s")], lh=13))
    o.append("</g>")
    return svg(146, o)
FIGS["webmob"] = webmob()

FIGS["adopt"] = curves([("New version 5.2", [0, 22, 40, 58, 68, 72, 75], "#127a64", 0), ("5.1 and older", [100, 78, 60, 42, 32, 28, 25], "#b93a32", 0)],
                       ["Day 0", "Day 3", "Week 1", "Week 2", "Week 4", "Week 8", "Week 12"],
                       h=200, R=500)


def sdui():
    o = [MK, '<g class="c">']
    o.append(box(0, 30, 150, 60, *G, [("App opens the", "b"), ("home screen", "b"), ("(version 5.1)", "s")], lh=14))
    o.append(box(250, 30, 170, 60, *B, [("Server decides", "b"), ("which blocks, in what", "s"), ("order, with what text", "s")], lh=13))
    o.append(box(510, 10, 170, 100, *GR, [("Screen description", "b"), ("1. Banner: Diwali sale", "s"), ("2. Tile row: 8 items", "s"), ("3. Card: “Pay rent”", "s"), ("4. Tile row: offers", "s")], lh=16))
    o.append(arr(152, 48, 246, 48)); o.append(T(199, 20, "“what should", "s", "middle")); o.append(T(199, 32, "I show?”", "s", "middle"))
    o.append(arr(422, 60, 506, 60))
    o.append(f'<path d="M595,112 L595,124 L75,124 L75,96" stroke="#127a64" stroke-width="1.5" fill="none" marker-end="url(#pg)"/>')
    o.append(T(340, 138, "the app draws blocks it already knows how to draw", "s", "middle"))
    o.append("</g>")
    o.append(T(0, 160, "Change the order or the text today, on every version; a brand-new kind of block still needs a new release.", "b acc"))
    return svg(166, o)
FIGS["sdui"] = sdui()


# ================= B. feature flags =================
FIGS["flagflow"] = seq(
    [("Riya", "Android, Pune", "user"), ("App", "version 5.2", "app"), ("Flag service", "the switches", "partner"), ("Payments", "new checkout", "bank")],
    [(1, 2, "flags for user 123, Android, Pune?", "msg"), (2, 1, "new_checkout: ON (in the 5%)", "ret"), (1, 1, "caches the answer for 60 s", "self"),
     (0, 1, "taps Pay ₹499", "msg"), (1, 3, "uses the new checkout", "msg"), (2, 2, "PM flips new_checkout to OFF", "self"),
     (1, 2, "next check, within 60 s", "msg"), (2, 1, "new_checkout: OFF", "ret"), (1, 3, "old checkout again, no new release", "msg")],
    note="The code for both checkouts is already on the phone; the flag only chooses which one runs.")


def killchart():
    L, R, Tp, Bt = 50, 660, 18, 150
    pts = [(0, 1.2), (2, 1.2), (4, 1.3), (5, 2.2), (6, 3.1), (7, 3.8), (8, 3.8), (8.5, 3.6), (9, 2.0), (10, 1.3), (12, 1.2), (14, 1.2)]
    X = lambda m: L + (R - L) * m / 14; Y = lambda v: Bt - (Bt - Tp) * v / 4.5
    o = [T(0, 12, "Payment failures (%) minute by minute after the new checkout is switched on for 20% of users (illustrative)", "b")]
    for v in (0, 1, 2, 3, 4):
        o.append(T(L - 6, Y(v) + 4, f"{v}%", "s", "end")); o.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{R}" y2="{Y(v):.1f}" stroke="#eef0f2"/>')
    d = " ".join(f"{'M' if i == 0 else 'L'}{X(m):.1f},{Y(v):.1f}" for i, (m, v) in enumerate(pts))
    o.append(f'<path d="{d}" fill="none" stroke="#b93a32" stroke-width="2.6"/>')
    for m, lab, y, c in [(4, "10:04 flag ON for 20%", 40, "b"), (7, "10:07 alert fires", 122, "b red"), (8.5, "10:08:30 flag OFF", 140, "b grn")]:
        o.append(f'<line x1="{X(m):.1f}" y1="{Tp}" x2="{X(m):.1f}" y2="{Bt}" stroke="#9aa3ad" stroke-dasharray="3 3"/>')
        o.append(T(X(m) - 4, y, lab, c + " halo", "end") if m == 4 else T(X(m) + 4, y, lab, c + " halo"))
    for m in range(0, 15, 2): o.append(T(X(m), Bt + 14, f"10:{m:02d}", "s", "middle"))
    o.append(f'<line x1="{L}" y1="{Bt}" x2="{R}" y2="{Bt}" stroke="#4a5563"/>')
    return svg(172, o)
FIGS["killchart"] = killchart()


# ================= C. staged roll-outs =================
def rollout():
    steps = [("Day 1", 1), ("Day 2", 2), ("Day 3", 5), ("Day 4", 10), ("Day 5", 20), ("Day 6", 50), ("Day 7", 100)]
    L, Bt = 20, 172; w = 88
    o = [T(0, 12, "Apple’s 7-day phased release: share of users who get the update (a gate before each step)", "b")]
    for i, (d, p) in enumerate(steps):
        x = L + i * w; hh = 8 + p * 1.1
        o.append(f'<rect x="{x}" y="{Bt - hh:.1f}" width="{w - 26}" height="{hh:.1f}" fill="#0b5d7a" rx="2"/>')
        o.append(T(x + (w - 26) / 2, Bt - hh - 5, f"{p}%", "b", "middle")); o.append(T(x + (w - 26) / 2, Bt + 14, d, "s", "middle"))
        if i < len(steps) - 1:
            gx = x + w - 13
            o.append(f'<circle cx="{gx}" cy="{Bt - 22}" r="8" fill="#fff" stroke="#c47f17" stroke-width="1.6"/>' + T(gx, Bt - 18, "?", "b amb", "middle"))
    o.append(f'<line x1="{L - 10}" y1="{Bt}" x2="{L + 7 * w}" y2="{Bt}" stroke="#4a5563"/>')
    o.append(T(0, Bt + 36, "At each gate (?): crash-free sessions, payment success, ratings and support tickets vs the old version. Any one fails: pause.", "b amb"))
    return svg(Bt + 44, o)
FIGS["rollout"] = rollout()

FIGS["crash"] = hbars([("Old version, all users", 60000, "0.2% of 3 crore sessions a day crash"), ("New version, if at 5%", 13500, "0.9% of its 15 lakh sessions (seen on day 3)"),
                       ("New version, if at 100%", 270000, "0.9% of 3 crore: 2.1 lakh extra crashes a day")], 270000,
                      lw=190, fmt="{:,}", colors=["#9aa3ad", "#c47f17", "#b93a32"], note="Crashes a day for an app with 1 crore users and 3 crore sessions (illustrative)")


# ================= D. observability =================
def three():
    cols = [("Metrics", "counts over time", "“12,400 parcels delivered|this hour; 3% late”", "Is something wrong?", B),
            ("Logs", "a diary of events", "“Hub 7, 14:02: parcel|8841 scanned, label torn”", "What exactly happened?", A),
            ("Traces", "one request’s journey", "“Parcel 8841: Pune 2 h,|Nagpur 19 h, Delhi 3 h”", "Where did the time go?", G)]
    o = ['<g class="c">']
    for i, (t, s, ex, q, (f, st)) in enumerate(cols):
        x = i * 232
        o.append(f'<rect x="{x}" y="0" width="216" height="120" rx="6" fill="{f}" stroke="{st}" stroke-width="1.3"/>')
        o.append(T(x + 10, 18, t, "b t13")); o.append(T(x + 10, 34, s, "s"))
        o.append(T(x + 10, 56, "Courier company:", "s")); o.append(T(x + 10, 71, ex.split("|")[0], "i")); o.append(T(x + 10, 85, ex.split("|")[1], "i"))
        o.append(T(x + 10, 108, q, "b acc"))
    o.append("</g>")
    return svg(124, o)
FIGS["three"] = three()


def trace():
    spans = [("Tap “Pay” → app sends request", 0, 0.1, "#0b5d7a"), ("Gateway: check login", 0.1, 0.3, "#0b5d7a"), ("Fetch offers for this user", 0.3, 0.6, "#0b5d7a"),
             ("Ask the bank to confirm (bank API)", 0.6, 3.8, "#b93a32"), ("Save result, draw the screen", 3.8, 4.0, "#0b5d7a")]
    L, R = 250, 670; sc = (R - L) / 4.0
    o = [T(0, 12, "One slow payment screen, as a trace: 4.0 seconds in total (illustrative)", "b")]
    for s in (0, 1, 2, 3, 4):
        x = L + s * sc; o.append(f'<line x1="{x:.1f}" y1="22" x2="{x:.1f}" y2="150" stroke="#eef0f2"/>'); o.append(T(x, 164, f"{s} s", "s", "middle"))
    for i, (lab, a, b, col) in enumerate(spans):
        y = 26 + i * 24
        o.append(T(L - 8, y + 13, lab, "b" if col == "#b93a32" else "", "end"))
        o.append(f'<rect x="{L + a * sc:.1f}" y="{y}" width="{max((b - a) * sc, 3):.1f}" height="17" fill="{col}" rx="2"/>')
    o.append(T(L + 2.2 * sc, 26 + 3 * 24 + 13, "3.2 s: 80% of the wait", "b w", "middle"))
    return svg(170, o)
FIGS["trace"] = trace()


def burn():
    L, R, Tp, Bt = 50, 660, 22, 150
    X = lambda d: L + (R - L) * d / 30; Y = lambda v: Bt - (Bt - Tp) * v / 43
    o = [T(0, 12, "Error budget: 43 minutes of slow payment screens allowed in a 30-day month (99.9% target)", "b")]
    for v in (0, 10, 20, 30, 43):
        o.append(T(L - 6, Y(v) + 4, f"{v}", "s", "end")); o.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{R}" y2="{Y(v):.1f}" stroke="#eef0f2"/>')
    o.append(f'<path d="M{X(0)},{Y(43)} L{X(30)},{Y(0)}" stroke="#9aa3ad" stroke-width="2" stroke-dasharray="6 4" fill="none"/>')
    o.append(T(X(21), Y(16) - 6, "steady use: lasts the month", "s halo"))
    o.append(f'<path d="M{X(0)},{Y(43)} L{X(10)},{Y(33)} L{X(11)},{Y(14)} L{X(11.5)},{Y(9)}" stroke="#b93a32" stroke-width="2.6" fill="none"/>')
    o.append(f'<circle cx="{X(10.2):.1f}" cy="{Y(30):.1f}" r="5" fill="#b93a32"/>')
    o.append(T(X(10.8), Y(31), "day 10: burning 14× too fast → page the on-call engineer", "b red halo"))
    for d in (0, 5, 10, 15, 20, 25, 30): o.append(T(X(d), Bt + 14, f"day {d}", "s", "middle"))
    o.append(f'<line x1="{L}" y1="{Bt}" x2="{R}" y2="{Bt}" stroke="#4a5563"/>')
    o.append(T(0, Bt + 32, "minutes of budget left", "s"))
    return svg(Bt + 38, o)
FIGS["burn"] = burn()


# ================= E. capstone: IRCTC Tatkal =================
def tatkal_demand():
    L, R, Tp, Bt = 60, 660, 22, 160
    xs = ["9:55", "9:58", "9:59", "10:00", "10:01", "10:02", "10:05", "10:10", "10:20"]
    vals = [3, 20, 60, 135, 120, 80, 35, 15, 6]
    X = lambda i: L + (R - L) * i / (len(xs) - 1); Y = lambda v: Bt - (Bt - Tp) * v / 150
    o = [T(0, 12, "Requests a second at the Tatkal booking system around 10 am (thousands, illustrative)", "b")]
    for v in (0, 50, 100, 150):
        o.append(T(L - 6, Y(v) + 4, f"{v}k", "s", "end")); o.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{R}" y2="{Y(v):.1f}" stroke="#eef0f2"/>')
    d = " ".join(f"{'M' if i == 0 else 'L'}{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(vals))
    o.append(f'<path d="{d} L{X(len(xs) - 1):.1f},{Bt} L{X(0):.1f},{Bt} z" fill="#fcecea" stroke="none"/>')
    o.append(f'<path d="{d}" fill="none" stroke="#b93a32" stroke-width="2.6"/>')
    o.append(f'<line x1="{L}" y1="{Y(8):.1f}" x2="{R}" y2="{Y(8):.1f}" stroke="#127a64" stroke-width="2" stroke-dasharray="6 4"/>')
    o.append(T(R, Y(8) - 6, "normal busy time ≈ 8k a second", "b grn halo", "end"))
    o.append(T(X(3) + 8, Y(135) + 4, "10:00:00 → about 17× normal, in seconds", "b red halo"))
    for i, x in enumerate(xs): o.append(T(X(i), Bt + 14, x, "s", "middle"))
    o.append(f'<line x1="{L}" y1="{Bt}" x2="{R}" y2="{Bt}" stroke="#4a5563"/>')
    return svg(Bt + 22, o)
FIGS["tatkal_demand"] = tatkal_demand()


def tatkal_arch():
    o = [MK, '<g class="c">']
    def bx(x, y, col, t, sub, tag, w=124, dash=False):
        o.append(box(x, y, w, 52, *col, [(t, "b"), (sub, "s"), (tag, "s i")], lh=14))
        if dash: o.append(f'<rect x="{x}" y="{y}" width="{w}" height="52" rx="6" fill="none" stroke="#fff" stroke-width="1.5" stroke-dasharray="4 4"/>')
    row1 = [(G, "Users", "app and website", "4 lakh at 10:00"), (A, "Front door", "CDN, bots, rate limits", "DNS, CDN"),
            (I, "Waiting room", "admits 25,000 a min", "the temple queue"), (B, "Load balancer", "spreads requests", "scale out"),
            (B, "Booking servers", "many; added at 9:45", "stateless")]
    for i, (c, t, sub, tag) in enumerate(row1):
        x = i * 139; bx(x, 8, c, t, sub, tag)
        if i < 4: o.append(arr(x + 125, 34, x + 137, 34))
    row2 = [(P, "Dashboards", "every box reports", "observability"), (A, "Queue", "ticket, SMS, email", "async workers"),
            (B, "Payment service", "one debit per booking", "idempotency"), (R, "Seat database", "one true count", "strong consistency"),
            (GR, "Availability cache", "seats left, seconds old", "caching")]
    o.append('<line x1="618" y1="62" x2="618" y2="84" stroke="#4a5563" stroke-width="1.4"/>')
    o.append('<line x1="201" y1="84" x2="618" y2="84" stroke="#4a5563" stroke-width="1.4"/>')
    for i, (c, t, sub, tag) in enumerate(row2):
        x = i * 139; bx(x, 108, c, t, sub, tag)
        if i >= 1: o.append(arr(x + 62, 84, x + 62, 104))
    o.append("</g>")
    o.append(T(0, 182, "Top row: controlling the crowd. Bottom row: keeping the count exact and the money safe. Italics: the mechanism at work.", "s"))
    return svg(188, o)
FIGS["tatkal_arch"] = tatkal_arch()

FIGS["wroom"] = seq(
    [("Suresh", "app, 9:59:40", "user"), ("Waiting room", "the queue", "app"), ("Booking", "servers", "bank"), ("Seat database", "true count", "risk")],
    [(0, 1, "opens Tatkal, logged in (Aadhaar-verified)", "msg"), (1, 0, "“You are 38,412th. About 90 s.”", "ret"), (1, 1, "admits 25,000 a minute, in order", "self"),
     (1, 0, "token: your turn, valid 10 min", "msg"), (0, 2, "search train 12951, 3A", "msg"), (2, 3, "“hold one berth for 5 min”", "msg"),
     (3, 2, "held: B2-34, timer starts", "ret"), (2, 0, "“Pay within 4:59”", "msg")],
    note="The queue protects the database: only as many people reach booking as it can serve.", row=21)


def seathold():
    o = [MK, '<g class="c">']
    st = [(0, 40, "Available", "counted in “seats left”", G), (190, 40, "Held (5 min)", "timer running; no one else", A),
          (400, 40, "Booked", "payment confirmed; ticket issued", B), (190, 130, "Released", "timer ran out or payment failed", R)]
    for x, y, t, s, c in st:
        o.append(box(x, y, 170 if x < 400 else 190, 50, *c, [(t, "b"), (s, "s")], lh=14))
    o.append(arr(172, 58, 186, 58)); o.append(T(179, 36, "user picks", "s", "middle"))
    o.append(arr(362, 58, 396, 58, "#127a64")); o.append(T(380, 36, "paid", "s grn", "middle"))
    o.append(arr(275, 92, 275, 126, "#b93a32")); o.append(T(282, 114, "5 min pass", "s red"))
    o.append(arr(188, 150, 90, 94)); o.append(T(14, 140, "back on sale", "s"))
    o.append("</g>")
    o.append(T(420, 140, "At 25,000 new holds a minute × 5 min,", "b")); o.append(T(420, 154, "about 1.25 lakh berths are held at", "b"))
    o.append(T(420, 168, "any moment (holds = rate × time).", "b")); o.append(T(420, 186, "If 30% never pay, those berths return", "s"))
    o.append(T(420, 199, "minutes later, to someone else.", "s"))
    return svg(206, o)
FIGS["seathold"] = seathold()

FIGS["payidem"] = seq(
    [("Suresh", "user", "user"), ("Booking", "servers", "app"), ("Payment", "service", "partner"), ("Bank", "via UPI", "bank")],
    [(1, 2, "pay ₹2,145 for booking B-7781 (the key)", "msg"), (2, 3, "debit request", "msg"), (3, 2, "debited (reply lost: timeout)", "ret"),
     (1, 2, "retry: pay for B-7781", "msg"), (2, 2, "B-7781 already paid: don’t debit again", "self"), (2, 1, "paid", "ret"),
     (1, 0, "ticket confirmed: PNR 4521…", "msg"), (2, 2, "nightly match: any debit with no ticket → refund", "self")],
    note="The booking ID travels with every retry, so a lost reply can’t turn into a second debit.", row=21)

FIGS["tdegrade"] = hbars([("Meals, hotel, tour offers", 1, "switched off at 9:45, back at 11:30"), ("Fare enquiry for other quotas", 2, "shown from a copy made at 9:30"),
                          ("PNR status checks", 3, "answered from a cache, up to 1 min old"), ("New sign-ups", 4, "paused 9:55–10:30; log-in stays open"),
                          ("Seat availability", 5, "cached, a few seconds old, marked “approx.”"), ("Hold a berth, pay, get the ticket", 6, "never switched off; strict count")], 6,
                         lw=210, fmt="", colors=["#9aa3ad", "#9aa3ad", "#c47f17", "#c47f17", "#0b5d7a", "#127a64"],
                         note="What gives way first on a Tatkal morning (top) and what never does (bottom): a degradation ladder")
