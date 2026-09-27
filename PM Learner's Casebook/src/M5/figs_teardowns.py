"""Teardown figures for M5; imported at the end of m5_figs.py (shares its helpers and FIGS)."""
from m5_figs import FIGS, seq, hbars, loop, svg, T, two_by_two  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R  # noqa: F401

# ---------- Instagram ----------
FIGS["flow_ig"] = seq(
    [("Riya", "creator, Pune", "user"), ("Upload service", "stores, copies", "app"), ("Ranking", "who sees what", "app"),
     ("Test viewers", "~500 people", "partner"), ("Wider audience", "food lovers", "user"), ("Advertisers", "café, brands", "merchant")],
    [(0, 1, "30-s Reel + song, 25 MB", "msg"),
     (1, 1, "make 4 sizes; check song rights, nudity", "self"),
     (1, 2, "new Reel ready", "msg"),
     (2, 3, "show to some followers + some strangers", "msg"),
     (3, 2, "watched to the end, 3 shares, few skips", "ret"),
     (2, 2, "strong shares → push to a bigger pool", "self"),
     (2, 4, "40,000 views in 24 hours", "msg"),
     (4, 0, "200 new followers, 120 DM shares", "ret"),
     (5, 2, "₹ per 1,000 ad views", "money"),
     (2, 4, "about 1 ad every 10 Reels", "msg")],
    note="Riya earns from the café’s paid post, not from Instagram’s views.")

FIGS["loop_ig"] = loop(["① Trigger|a friend sends a Reel", "② Action|open, watch, swipe", "③ Uneven reward|1 in 5 is really funny",
                        "④ Investment|share, follow, post"], "The Hooked loop|④ becomes the next|person’s ①",
                       rx=230, ry=74, bw=170, bh=42, h=200, cy=100)

# ---------- Facebook ----------
FIGS["flow_fb"] = seq(
    [("Arun", "Kochi bakery", "merchant"), ("Meta ads", "campaigns", "app"), ("Auction", "per ad slot", "app"),
     ("Priya", "Facebook feed", "user"), ("WhatsApp", "chat", "app")],
    [(0, 1, "₹500 a day; 5 km; adults; goal: messages", "msg"),
     (1, 1, "check the ad against the rules", "self"),
     (3, 2, "Priya scrolls; next slot is an ad", "msg"),
     (2, 2, "gather every ad that wants someone like Priya", "self"),
     (2, 2, "score each: bid × chance + quality", "self"),
     (2, 3, "Arun’s cake ad wins (0.65 vs 0.60)", "ret"),
     (3, 4, "taps “Send message”", "msg"),
     (4, 0, "“Is the plum cake eggless?” → order", "msg"),
     (0, 1, "≈ ₹37 for this message", "money")],
    note="Arun pays for the action he chose (a message), not for the view.")


def auction():
    rows = [("Arun’s bakery", "₹40 a message", "1.5%", "0.60", "+0.05", "0.65", True),
            ("Phone brand", "₹8 a click", "5%", "0.40", "+0.10", "0.50", False),
            ("Loan app", "₹100 an install", "0.8%", "0.80", "−0.20", "0.60", False)]
    hdr = [(10, "Advertiser", "start"), (220, "Bid", "middle"), (320, "Chance Priya", "middle"), (420, "Bid × chance", "middle"),
           (510, "Quality", "middle"), (600, "Total value", "middle")]
    o = [T(x, 14, h, "b", a) for x, h, a in hdr]
    o.append(T(320, 27, "does it", "b", "middle"))
    for i, (n, b, p, v, q, t, win) in enumerate(rows):
        y = 36 + i * 30
        o.append(f'<rect x="2" y="{y}" width="676" height="26" rx="4" fill="{"#e1f2ec" if win else "#f5f6f8"}" stroke="{"#127a64" if win else "#dfe3e8"}"/>')
        o.append(T(10, y + 17, n, "b")); o.append(T(220, y + 17, b, "", "middle")); o.append(T(320, y + 17, p, "", "middle"))
        o.append(T(420, y + 17, v, "", "middle"))
        o.append(T(510, y + 17, q, "b red" if q.startswith("−") else "b grn", "middle"))
        o.append(T(600, y + 17, t + ("  wins" if win else ""), "b grn" if win else "b", "middle"))
    o.append(T(10, 146, "Arun pays just enough to beat 0.60: (0.60 − 0.05) ÷ 1.5% ≈ ₹37 per message, not his full ₹40 bid.", "b acc"))
    o.append(T(10, 161, "The loan app bids the most but loses: Priya is unlikely to install, and people report its ads.", "s"))
    return svg(170, o)
FIGS["auction"] = auction()


def moder():
    o = [MK, '<g class="c">',
         box(0, 44, 118, 56, *B, [("Post or report", "b"), ("billions a day", ""), ("worldwide", "s")]),
         box(150, 44, 130, 56, *A, [("Automatic check", "b"), ("classifiers score", ""), ("each post", "s")]),
         box(318, 0, 170, 44, *R, [("Clearly breaks rules", "b"), ("removed at once", "")]),
         box(318, 50, 170, 44, *A, [("Unsure (a few %)", "b"), ("→ human reviewers", "")]),
         box(318, 100, 170, 44, *G, [("Clearly fine", "b"), ("stays up", "")]),
         box(520, 50, 160, 44, *GR, [("Reviewer decides", "b"), ("in the post’s language", "")]),
         box(520, 102, 160, 44, *GR, [("Appeal", "b"), ("user can ask again", "")]),
         '<line x1="118" y1="72" x2="146" y2="72" class="ln" marker-end="url(#pa)"/>',
         '<line x1="280" y1="62" x2="314" y2="24" class="ln" marker-end="url(#pa)"/>',
         '<line x1="280" y1="72" x2="314" y2="72" class="ln" marker-end="url(#pa)"/>',
         '<line x1="280" y1="82" x2="314" y2="120" class="ln" marker-end="url(#pa)"/>',
         '<line x1="488" y1="72" x2="516" y2="72" class="ln" marker-end="url(#pa)"/>',
         '<line x1="600" y1="94" x2="600" y2="98" class="ln" marker-end="url(#pa)"/>',
         T(0, 164, "Team size (illustrative): 2 lakh posts a day need a human look in India ÷ 400 per reviewer a day = 500 on duty,", "b acc"),
         T(0, 178, "about 700 with shifts and leave. Tighten a rule, and posts move from “fine” to “unsure”: the team must grow.", "acc"),
         "</g>"]
    return svg(186, o)
FIGS["moder"] = moder()

# ---------- X ----------
FIGS["flow_x"] = seq(
    [("Meera", "reporter", "user"), ("X timelines", "Following", "app"), ("For You", "ranking", "app"),
     ("Followers", "80,000", "user"), ("Mumbai users", "non-followers", "user"), ("Note raters", "volunteers", "partner")],
    [(0, 1, "photo + 2 lines, 7:10 pm", "msg"),
     (1, 3, "into followers’ timelines, seconds", "msg"),
     (3, 2, "fast replies and reposts", "ret"),
     (2, 4, "shown to people nearby who don’t follow", "msg"),
     (4, 4, "old video posted as tonight’s", "self"),
     (4, 5, "note: “video is from 2019”", "msg"),
     (5, 5, "raters vote", "self"),
     (5, 2, "raters who usually disagree both say helpful", "ret"),
     (2, 4, "note shown under the false post", "msg")],
    note="Speed is X’s strength; a note arriving an hour late is its weakness.")


def bridge():
    o = ['<line x1="20" y1="44" x2="660" y2="44" stroke="#9aa3ad" stroke-width="1.5"/>',
         T(20, 34, "raters who usually lean one way", "s"), T(660, 34, "raters who usually lean the other way", "s", "end"),
         T(340, 14, "Each dot is a rater who marked the note helpful", "b", "middle")]
    # note A: all left
    o.append(T(20, 76, "Note A: 9 helpful votes", "b"))
    for i in range(9): o.append(f'<circle cx="{40 + i * 22}" cy="92" r="7" fill="#b93a32"/>')
    o.append(box(420, 70, 258, 40, *R, [("Hidden: all votes from one side", "b"), ("popular with one group only", "")]))
    o.append(T(20, 134, "Note B: 5 helpful votes", "b"))
    for i, x in enumerate([50, 90, 130, 560, 600]):
        o.append(f'<circle cx="{x}" cy="150" r="7" fill="#127a64"/>')
    o.append(box(200, 128, 258, 40, *G, [("Shown: helpful to both sides", "b"), ("people who usually disagree agree", "")]))
    return svg(176, o)
FIGS["bridge"] = bridge()

# ---------- Snapchat ----------
FIGS["flow_snap"] = seq(
    [("Kabir", "17, Delhi", "user"), ("Kabir’s phone", "camera, Lens", "app"), ("Snap servers", "hold, then delete", "app"),
     ("Aarav", "best friend", "user")],
    [(0, 1, "opens app: camera first", "msg"),
     (1, 1, "cricket-helmet Lens drawn on the phone", "self"),
     (1, 2, "Snap sent (photo, 400 KB)", "msg"),
     (2, 3, "“New Snap from Kabir” notification", "msg"),
     (3, 2, "opens it", "ret"),
     (2, 2, "all recipients opened → delete the Snap", "self"),
     (2, 1, "streak: 200 → 201 days", "ret"),
     (3, 0, "reply: photo of maths homework", "msg")],
    note="Unopened Snaps are deleted after 30 days; opened ones are gone from Snap’s servers.")

FIGS["snap_rev"] = hbars([("Total revenue", 1.6, " bn   April–June 2026, +19%"),
                          ("Advertising", 1.28, " bn   Lens, Stories, Spotlight ads (≈ total − other)"),
                          ("Other revenue", 0.316, " bn   mostly Snapchat+, +85%")], 1.6, lw=110, fmt="${:,.2f}",
                         colors=["#9aa3ad", "#0b5d7a", "#127a64"], note="Snap, one quarter")

# ---------- WhatsApp ----------
FIGS["flow_wa"] = seq(
    [("Neha", "Jaipur", "user"), ("Instagram", "Reel ad", "app"), ("WhatsApp", "encrypted chat", "app"),
     ("Saree shop", "+ AI assistant", "merchant"), ("UPI", "NPCI + banks", "bank"), ("Meta", "billing", "partner")],
    [(3, 5, "ad fee for the Reel ad", "money"),
     (1, 0, "Reel ad with “Send message”", "msg"),
     (0, 2, "chat opens: “Hi, I’m interested”", "msg"),
     (2, 3, "message, locked end to end", "msg"),
     (3, 0, "AI replies in Hindi: 3 colours, ₹2,400", "ret"),
     (0, 4, "pays ₹2,400 with UPI PIN, inside chat", "msg"),
     (4, 3, "₹2,400 to the shop’s bank", "money"),
     (3, 0, "“Order shipped” (utility message)", "msg"),
     (3, 5, "≈ ₹0.115 for that message", "money")],
    note="Meta earns twice from the shop, never from Neha; it can’t read the chat itself.")

FIGS["wa_price"] = hbars([("Marketing", 0.86, "   offers, new arrivals, “come back” messages"),
                          ("Utility", 0.115, "   order updates, bills, delivery alerts"),
                          ("Authentication", 0.115, "   one-time passwords"),
                          ("Service", 0.0, "   free: replies when the customer wrote first")], 0.86, lw=110, fmt="₹{:,.3g}",
                         colors=["#c47f17", "#0b5d7a", "#0b5d7a", "#127a64"], note="Price per message to a user in India, from January 2026 (approx.)")

FIGS["pos2x2"] = two_by_two("Whose posts you see: people you know → strangers picked by interest",
                            "Private → public broadcast",
                            ["public, people you know", "public, strangers: broadcast feeds", "private, close circles", "private-feeling, but strangers"],
                            [("WhatsApp", 0.12, 0.12, "#127a64", "start"), ("Snapchat", 0.2, 0.3, "#c47f17", "start"),
                             ("Facebook", 0.4, 0.56, "#0b5d7a", "start"), ("Instagram", 0.62, 0.64, "#0b5d7a", "start"),
                             ("Telegram", 0.72, 0.38, "#5b6470", "start"), ("Threads", 0.74, 0.8, "#0b5d7a", "end"),
                             ("X", 0.88, 0.9, "#1c232b", "end")], h=290)
