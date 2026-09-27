"""Case and guesstimate figures for M5; imported at the end of m5_figs.py."""
import math
from m5_figs import FIGS, svg, T, lines, strip, hbars  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R  # noqa: F401

# ---------- Case 5.1 ----------
FIGS["strip51"] = strip([("Clarify", "goal, what exists"), ("Start small", "one trade, one area"), ("Trust", "checks both ways"),
                         ("Flow", "voice, map, deal"), ("Who pays", "households only"), ("Measure", "hires that last")])


def scam():
    steps = [["Fake “hotel” posts:", "₹22,000 a month,", "no experience needed"],
             ["Worker calls. “You’re", "selected! Pay ₹1,500", "for uniform and ID”"],
             ["Worker pays by UPI", "to a personal UPI ID;", "told to report Monday"],
             ["Number switched off.", "The job never existed.", "₹1,500 gone"]]
    checks = [["Employer verified:", "shop licence or", "society flat; pay far", "above area range flagged"],
              ["Calls go through", "masked numbers;", "chats scanned for", "“fee”, “deposit”"],
              ["First screen rule:", "a worker never pays.", "Any request = one-", "tap report"],
              ["One report hides", "the post and freezes", "the employer’s other", "postings"]]
    o = [MK, '<g class="c">', T(0, 12, "The scam", "b red"), T(0, 118, "Where the app stops it", "b grn")]
    for i, (s, c) in enumerate(zip(steps, checks)):
        x = i * 172
        o.append(box(x, 20, 160, 64, *R, [(l, "b" if j == 0 else "") for j, l in enumerate(s)], lh=13))
        if i < 3: o.append(f'<line x1="{x + 160}" y1="52" x2="{x + 170}" y2="52" class="ln" marker-end="url(#pa)"/>')
        o.append(f'<line x1="{x + 80}" y1="84" x2="{x + 80}" y2="120" stroke="#127a64" stroke-width="1.6" stroke-dasharray="3 2"/>')
        o.append(box(x, 124, 160, 70, *G, [(l, "b" if j == 0 else "") for j, l in enumerate(c)], lh=13))
    o.append("</g>")
    return svg(198, o)
FIGS["scam"] = scam()


def kinds():
    o = ['<g class="c">']
    # direct: 6 nodes all linked
    cx, cy, r = 110, 82, 48
    pts = [(cx + r * math.cos(2 * math.pi * k / 6), cy + r * math.sin(2 * math.pi * k / 6)) for k in range(6)]
    for a in range(6):
        for b in range(a + 1, 6):
            o.append(f'<line x1="{pts[a][0]:.1f}" y1="{pts[a][1]:.1f}" x2="{pts[b][0]:.1f}" y2="{pts[b][1]:.1f}" stroke="#9fb8c4"/>')
    for x, y in pts: o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="#127a64"/>')
    o += [T(110, 12, "Direct", "b t12", "middle"), T(110, 150, "Each friend who joins is", "", "middle"),
          T(110, 163, "someone more I can message", "", "middle"), T(110, 180, "WhatsApp, Snapchat", "b acc", "middle")]
    # cross-side
    hx = [258, 300, 342, 384]; wx = [258, 300, 342, 384]
    for a in hx:
        for b in wx: o.append(f'<line x1="{a}" y1="44" x2="{b}" y2="120" stroke="#9fb8c4"/>')
    for x in hx: o.append(f'<rect x="{x - 9}" y="35" width="18" height="18" rx="3" fill="#0b5d7a"/>')
    for x in wx: o.append(f'<circle cx="{x}" cy="120" r="9" fill="#c47f17"/>')
    o += [T(321, 12, "Cross-side", "b t12", "middle"), T(410, 48, "households", "s"), T(410, 124, "workers", "s"),
          T(321, 150, "More households help workers,", "", "middle"), T(321, 163, "and more workers help households", "", "middle"),
          T(321, 180, "jobs apps, Uber, Swiggy", "b acc", "middle")]
    # local
    for (cx2, name) in [(520, "Wakad"), (630, "Delhi")]:
        ps = [(cx2 - 22, 60), (cx2 + 22, 60), (cx2 - 22, 104), (cx2 + 22, 104)]
        for a in range(4):
            for b in range(a + 1, 4):
                o.append(f'<line x1="{ps[a][0]}" y1="{ps[a][1]}" x2="{ps[b][0]}" y2="{ps[b][1]}" stroke="#9fb8c4"/>')
        for i, (x, y) in enumerate(ps):
            o.append(f'<circle cx="{x}" cy="{y}" r="8" fill="{"#0b5d7a" if i < 2 else "#c47f17"}"/>')
        o.append(f'<circle cx="{cx2}" cy="82" r="44" fill="none" stroke="#5b6470" stroke-dasharray="3 3"/>')
        o.append(T(cx2, 140, name, "b", "middle"))
    o += ['<line x1="562" y1="82" x2="588" y2="82" stroke="#b93a32" stroke-width="2"/>', T(575, 76, "✗", "b red", "middle"),
          T(575, 12, "Local", "b t12", "middle"), T(575, 158, "Only users nearby count;", "", "middle"),
          T(575, 171, "win one area at a time", "", "middle"), T(575, 186, "this jobs app, Uber", "b acc", "middle")]
    o.append('<line x1="222" y1="20" x2="222" y2="186" stroke="#e1e5ea"/><line x1="462" y1="20" x2="462" y2="186" stroke="#e1e5ea"/>')
    o.append("</g>")
    return svg(192, o)
FIGS["kinds"] = kinds()


def atomic():
    L, Rr, Tp, Bt = 60, 660, 20, 170
    X = lambda h: L + (Rr - L) * h / 1000
    Y = lambda j: Bt - (Bt - Tp) * j / 7
    o = [f'<rect x="{L}" y="{Tp}" width="{X(450) - L:.1f}" height="{Bt - Tp}" fill="#fcecea"/>',
         f'<rect x="{X(450):.1f}" y="{Tp}" width="{Rr - X(450):.1f}" height="{Bt - Tp}" fill="#e7f4f0"/>',
         f'<line x1="{L}" y1="{Bt}" x2="{Rr}" y2="{Bt}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{Bt}" stroke="#4a5563"/>']
    for h in range(0, 1001, 200): o.append(T(X(h), Bt + 14, f"{h:,}", "s", "middle"))
    for j in range(0, 8, 1): o.append(T(L - 6, Y(j) + 4, f"{j}", "s", "end"))
    o.append(f'<line x1="{X(0):.1f}" y1="{Y(0):.1f}" x2="{X(1000):.1f}" y2="{Y(1000 / 150):.1f}" stroke="#0b5d7a" stroke-width="2.6"/>')
    o.append(f'<line x1="{L}" y1="{Y(3):.1f}" x2="{Rr}" y2="{Y(3):.1f}" stroke="#c47f17" stroke-width="1.5" stroke-dasharray="5 3"/>')
    o.append(f'<line x1="{X(450):.1f}" y1="{Tp}" x2="{X(450):.1f}" y2="{Bt}" stroke="#127a64" stroke-width="1.5" stroke-dasharray="5 3"/>')
    o.append(f'<circle cx="{X(450):.1f}" cy="{Y(3):.1f}" r="5" fill="#127a64"/>')
    o.append(T(X(450) + 8, Y(3) + 16, "450 households: 3 jobs a week", "b grn halo"))
    o.append(T(L + 8, Tp + 16, "Savita sees too few jobs;", "b red")); o.append(T(L + 8, Tp + 30, "she drifts back to her agent", "red"))
    o.append(T(Rr - 8, Tp + 16, "enough jobs: she comes back", "b grn", "end")); o.append(T(Rr - 8, Tp + 30, "without being asked", "grn", "end"))
    o.append(T(Rr - 8, Y(3) - 6, "worth-coming-back line: 3 a week", "s amb halo", "end"))
    o.append(T(X(760), Y(760 / 150) + 26, "jobs seen = households × 2% × ⅓", "b acc halo", "middle"))
    o.append(T((L + Rr) / 2, Bt + 30, "active households on the app within 3 km", "b", "middle"))
    o.append(f'<text x="16" y="{(Tp + Bt) / 2:.0f}" text-anchor="middle" class="b" transform="rotate(-90 16 {(Tp + Bt) / 2:.0f})">suitable jobs a week</text>')
    return svg(206, o)
FIGS["atomic"] = atomic()


# ---------- Case 5.2 ----------
FIGS["strip52"] = strip([("Clarify", "stage, decision"), ("Goal", "each side’s win"), ("One number", "creators earning"),
                         ("Inputs", "the ₹ funnel"), ("Guardrails", "feed quality"), ("Decide", "holdout + rule")])


def grid52():
    cols = ["Creator", "Viewer (buyer)", "Brand", "Instagram"]
    rows = [("Tags on every Reel", [("+", "more chances|to earn"), ("−", "feed feels|like a shop"), ("+", "more|exposure"), ("−", "watch time|may fall")]),
            ("Tagged Reels shown to", [("+", "new|buyers"), ("±", "useful finds, or|strangers’ ads"), ("+", "more|reach"), ("±", "good only if|relevant")]),
            ("Higher commission", [("+", "earns|more"), ("0", "no|change"), ("−", "pays more|per sale"), ("+", "creators|stay")]),
            ("Rank tagged Reels higher", [("+", "more|sales"), ("−", "worse|feed"), ("+", "more|sales"), ("−", "trust falls,|then ad money")])]
    sub = {1: "non-followers"}
    CW, X0, RH, Y0 = 128, 168, 42, 26
    col = {"+": ("#e1f2ec", "#127a64"), "−": ("#fcecea", "#b93a32"), "±": ("#fbf4e6", "#c47f17"), "0": ("#eef0f2", "#5b6470")}
    o = [T(0, 16, "Product choice", "b")]
    for j, c in enumerate(cols): o.append(T(X0 + j * CW + CW / 2 - 2, 16, c, "b", "middle"))
    for i, (lab, cells) in enumerate(rows):
        y = Y0 + i * RH
        o.append(T(0, y + 18, lab, "b"))
        if i in sub: o.append(T(0, y + 31, sub[i], "b"))
        for j, (sym, txt) in enumerate(cells):
            f, st = col[sym]; x = X0 + j * CW
            o.append(f'<rect x="{x}" y="{y + 2}" width="{CW - 4}" height="{RH - 5}" rx="4" fill="{f}" stroke="{st}"/>')
            o.append(T(x + 12, y + 25, sym, "b t13", "middle", fill=st))
            for k, l in enumerate(txt.split("|")): o.append(T(x + 24, y + 18 + k * 13, l, "s"))
    return svg(Y0 + len(rows) * RH + 2, o)
FIGS["grid52"] = grid52()


def funnel52():
    steps = [("10,00,000", "views of the", "tagged Reel"), ("20,000", "tap the", "product tag"), ("8,000", "view the", "product page"),
             ("2,400", "go to the", "brand’s site"), ("72", "orders", "× ₹1,200")]
    rates = ["× 2%", "× 40%", "× 30%", "× 3%"]
    o = [MK, '<g class="c">']
    w = 112; gap = 26
    for i, (a, b, c) in enumerate(steps):
        x = i * (w + gap)
        fill, st = (B if i < 3 else GR)
        o.append(box(x, 40, w, 58, fill, st, [(a, "b t12"), (b, ""), (c, "")], lh=13))
        if i < 4:
            o.append(f'<line x1="{x + w + 2}" y1="69" x2="{x + w + gap - 2}" y2="69" class="ln" marker-end="url(#pa)"/>')
            o.append(T(x + w + gap / 2, 62, rates[i], "b red halo", "middle"))
    o.append('<path d="M2,30 L2,24 L386,24 L386,30" fill="none" stroke="#0b5d7a" stroke-width="1.5"/>')
    o.append(T(194, 18, "Instagram controls these steps", "b acc", "middle"))
    o.append('<path d="M414,30 L414,24 L660,24 L660,30" fill="none" stroke="#5b6470" stroke-width="1.5"/>')
    o.append(T(537, 18, "the brand controls these", "b", "middle"))
    o.append(box(170, 116, 340, 44, *G, [("72 × ₹1,200 = ₹86,400 of sales", "b"), ("× 8% commission ≈ ₹6,900 for the creator", "")]))
    o.append(T(4, 140, "98% are lost at", "b red")); o.append(T(4, 153, "the first tap", "red"))
    o.append("</g>")
    return svg(166, o)
FIGS["funnel52"] = funnel52()


# ---------- Case 5.3 ----------
FIGS["strip53"] = strip([("Clarify", "what is “moving”?"), ("Size", "who, how many"), ("Why they go", "jobs each app does"),
                         ("What holds", "switching costs"), ("Moves", "defend new groups"), ("Measure", "weekly senders")])


def jan21():
    pts = [(52, "4 Jan", "New policy", ["“Accept by 8 Feb,", "or lose access”;", "rumours: WhatsApp", "will read chats"], "#b93a32"),
           (186, "6–10 Jan", "Signal rush", ["75 lakh Signal", "downloads in", "five days,", "worldwide"], "#c47f17"),
           (320, "12 Jan", "Telegram rush", ["+25 mn users in", "72 hours; India", "gives the most", "installs (24%)"], "#c47f17"),
           (454, "15 Jan", "WhatsApp replies", ["Deadline moved to", "15 May; Status", "posts: “we can’t", "read your chats”"], "#0b5d7a"),
           (592, "15 May", "Most people stay", ["Policy applies;", "family groups", "never moved; the", "new apps stay second"], "#127a64")]
    o = ['<line x1="10" y1="54" x2="670" y2="54" stroke="#4a5563" stroke-width="2"/><g class="c">']
    for x, d, h, ls, col in pts:
        o.append(f'<circle cx="{x}" cy="54" r="6.5" fill="{col}"/>')
        o.append(T(x, 40, d, "b", "middle"))
        o.append(T(x - 48, 74, h, "b", "start", fill=col))
        for i, l in enumerate(ls): o.append(T(x - 48, 88 + i * 13, l))
    o.append("</g>")
    o.append(T(10, 14, "January–May 2021: downloads spiked, but people added a second app rather than leaving.", "s"))
    return svg(146, o)
FIGS["jan21"] = jan21()


def allmove():
    L, Rr, Tp, Bt = 56, 470, 14, 164
    X = lambda n: L + (Rr - L) * (n - 1) / 49
    Y = lambda p: Bt - (Bt - Tp) * p
    o = [f'<line x1="{L}" y1="{Bt}" x2="{Rr}" y2="{Bt}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{Bt}" stroke="#4a5563"/>']
    for p in (0, 0.25, 0.5, 0.75, 1.0):
        o.append(f'<line x1="{L}" y1="{Y(p):.1f}" x2="{Rr}" y2="{Y(p):.1f}" stroke="#eef0f2"/>')
        o.append(T(L - 6, Y(p) + 4, f"{int(p * 100)}%", "s", "end"))
    for n in (1, 10, 20, 30, 40, 50): o.append(T(X(n), Bt + 14, str(n), "s", "middle"))
    for q, col, lab in ((0.97, "#127a64", "each member 97% likely"), (0.9, "#b93a32", "each member 90% likely")):
        pts = " ".join(f"{X(n):.1f},{Y(q ** n):.1f}" for n in range(1, 51))
        o.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2.4"/>')
    o.append(T(X(9), Y(0.97 ** 9) - 8, "each member 97% likely", "b grn halo"))
    o.append(T(X(4) + 10, Y(0.9 ** 4) + 30, "each member 90% likely", "b red halo"))
    for n, q, col in ((47, 0.97, "#127a64"), (47, 0.9, "#b93a32"), (5, 0.9, "#b93a32")):
        o.append(f'<circle cx="{X(n):.1f}" cy="{Y(q ** n):.1f}" r="4.5" fill="{col}"/>')
    o.append(f'<line x1="{X(47):.1f}" y1="{Tp}" x2="{X(47):.1f}" y2="{Bt}" stroke="#5b6470" stroke-dasharray="3 3"/>')
    o.append(T((L + Rr) / 2, Bt + 30, "members in the group", "b", "middle"))
    o.append(f'<text x="14" y="{(Tp + Bt) / 2:.0f}" text-anchor="middle" class="b" transform="rotate(-90 14 {(Tp + Bt) / 2:.0f})">chance everyone moves</text>')
    notes = [("Farhan’s group, 47 people:", "b"), ("at 90%: 0.9⁴⁷ ≈ 0.7%", "red"), ("at 97%: 0.97⁴⁷ ≈ 24%", "grn"),
             ("", ""), ("5 close friends at 90%:", "b"), ("0.9⁵ ≈ 59%", "red"), ("", ""), ("Small groups can move;", "b acc"), ("big ones almost never do.", "b acc")]
    for i, (t, c) in enumerate(notes): o.append(T(490, 30 + i * 14, t, c))
    return svg(198, o)
FIGS["allmove"] = allmove()


def stack():
    rows = [("People", "everyone must move together", 10, 2), ("History (data)", "photos, voice notes, chats", 6, 0),
            ("Learning", "new buttons, settings", 2, 2), ("Money", "both apps are free", 0.3, 0.3)]
    o = [T(196, 14, "switching cost, 0–10 (illustrative)", "s"),
         '<rect x="480" y="4" width="12" height="12" fill="#b93a32"/>', T(496, 14, "family group, 12 years old", "s"),
         '<rect x="480" y="20" width="12" height="12" fill="#127a64"/>', T(496, 30, "new college-batch group", "s")]
    for i, (lab, sub, a, b) in enumerate(rows):
        y = 40 + i * 38
        o.append(T(186, y + 10, lab, "b", "end")); o.append(T(186, y + 23, sub, "s", "end"))
        o.append(f'<rect x="196" y="{y}" width="{a * 26:.1f}" height="13" fill="#b93a32" rx="2"/>')
        o.append(f'<rect x="196" y="{y + 15}" width="{max(b * 26, 2):.1f}" height="13" fill="#127a64" rx="2"/>')
    o.append(T(480, 76, "For a new group of strangers", "b grn")); o.append(T(480, 90, "the costs are tiny, so it can", "grn"))
    o.append(T(480, 104, "start on whichever app does the", "grn")); o.append(T(480, 118, "job better. That is where", "grn"))
    o.append(T(480, 132, "Telegram wins.", "b grn"))
    return svg(194, o)
FIGS["stack"] = stack()



# ---------- Guesstimates ----------
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

FIGS["stripg51"] = strip([("Unit", "posts, not Stories"), ("Approach", "users × rate"), ("Tree", "split by behaviour"),
                          ("Numbers", "a reason each"), ("Check", "per person, world"), ("Range", "keen posters")])
FIGS["stripg52"] = strip([("Unit", "a chat = a thread"), ("Approach", "from WA users"), ("Tree", "openers → senders"),
                          ("Numbers", "8 chats a sender"), ("Check", "100 bn messages"), ("Range", "chats per sender")])

FIGS["gtree51"] = etree([("140 Cr people", "× 70% online", "= 98 Cr"), ("≈ 40 Cr", "monthly active", "on Instagram"),
                         ("70% watchers", "28 Cr × 1/60", "= 47 L a day"), ("25% regulars", "10 Cr × 0.1", "= 1 Cr a day"),
                         ("5% keen", "2 Cr × 0.5", "= 1 Cr a day"), ("≈ 2.5 Cr", "posts a day", "range 1.5–4 Cr")],
                        [("Check (card 5): two ways", "b"), ("Per person: 2.5 Cr ÷ 40 Cr = one post", ""),
                         ("every 16 days. Sounds right.", "b grn"), ("World: India ~13% of users → ~13–15%", ""),
                         ("of posts, not a third (casebook).", "red")],
                        [("Range (card 6): the swing factor", "b"), ("share of keen posters", ""),
                         ("3% → ~2 Cr · 8% → ~3 Cr a day", "b"), ("Add Stories and the number is", ""), ("several times higher.", "")],
                        h=172, swing=4)

FIGS["gtree52"] = etree([("55 Cr", "WhatsApp users", "in India, 2026"), ("× 80% open", "on a typical day", "= 44 Cr"),
                         ("× 75% send", "at least one", "message = 33 Cr"), ("× 8 chats", "5 personal", "+ 3 groups"),
                         ("≈ 2.6 bn", "chats a day", "range 2–4 bn")],
                        [("Check (card 5): WhatsApp’s own number", "b"), ("2.6 bn chats × ~6 messages ≈ 16 bn", ""),
                         ("100 bn+ a day worldwide × India’s 18%", ""), ("of users ≈ 18 bn. Holds up.", "b grn"),
                         ("Casebook 11 bn chats ≈ 66 bn messages.", "red")],
                        [("Range (card 6): the swing factor", "b"), ("chats per sender a day", ""),
                         ("6 → ~2 bn · 12 → ~4 bn", "b"), ("Diwali or New Year’s Eve: perhaps", ""), ("double, for one day.", "")],
                        h=172, swing=3)
