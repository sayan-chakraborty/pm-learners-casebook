"""Teardown figures for M6; imported at the end of m6_figs.py."""
from m6_figs import FIGS, svg, T, lines, hbars, loop, two_by_two, seq  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R, P  # noqa: F401

# ---------- Netflix ----------
FIGS["flow_nf"] = seq(
    [("Meera", "TV app, Bengaluru", "user"), ("Netflix servers", "in the cloud", "app"), ("Recommender", "picks rows", "app"),
     ("Licence server", "unlocks video", "network"), ("Cache box", "inside her ISP", "partner")],
    [(0, 1, "opens the app at 9:40 pm", "msg"),
     (1, 2, "who is this, what has she watched?", "msg"),
     (2, 1, "40 rows and the artwork for each, for Meera", "ret"),
     (1, 0, "home screen", "ret"),
     (0, 1, "presses play on a Korean series", "msg"),
     (1, 1, "Basic plan: 720p, one screen at a time", "self"),
     (1, 0, "address of the nearest copy: the cache box", "ret"),
     (0, 3, "ask for the key for this episode", "msg"),
     (3, 0, "key, valid for this device only", "ret"),
     (0, 4, "fetch 4-second chunks, low quality first", "msg"),
     (4, 0, "chunks from a box inside her ISP", "ret"),
     (0, 0, "buffer fills: switch up to 720p", "self"),
     (0, 1, "what she watched, every few seconds", "msg")],
    note="Nothing comes from America: the episode was copied to the box in her ISP overnight.")

FIGS["loop_nf"] = loop(["More members|worldwide", "More revenue|$51 bn in 2026", "Bigger content|budget", "More hits,|in more languages",
                        "More viewing|and data", "Better picks|less browsing"],
                       "Netflix’s flywheel|scale pays for content", bw=150, h=236)

# ---------- JioHotstar ----------
FIGS["flow_jh"] = seq(
    [("Stadium feed", "cameras, mixing", "partner"), ("Encoders", "cut 6-s chunks", "app"), ("CDN edges", "near viewers", "network"),
     ("Priya", "phone, Ahmedabad", "user"), ("Ad server", "picks ads", "app"), ("Advertisers", "brands", "merchant")],
    [(0, 1, "live picture, commentary in 12 languages", "msg"),
     (1, 2, "chunks in 5 qualities, every 6 seconds", "msg"),
     (3, 2, "next chunk, please (medium quality)", "msg"),
     (2, 3, "chunk, from a server in her city", "ret"),
     (1, 3, "over ends: an “ad break” marker in the stream", "msg"),
     (3, 4, "who is she: 24, Ahmedabad, Hindi, Android", "msg"),
     (4, 4, "pick 2 ads of 10 s for her", "self"),
     (4, 3, "ad chunks stitched into her stream", "ret"),
     (3, 4, "ad seen to the end", "msg"),
     (5, 4, "₹ per 1,000 views, for each ad shown", "money")],
    note="Crores of people see different ads in the same 30-second break.")

FIGS["loop_pv"] = loop(["A hit show|Panchayat, Mirzapur", "Prime feels|worth ₹1,499", "Prime renews", "More shopping|on Amazon",
                        "Retail and|ad profits"], "Prime Video’s job|keep Prime renewing", bw=150, h=230)

# ---------- YouTube ----------
FIGS["flow_yt"] = seq(
    [("Karthik", "creator, Coimbatore", "user"), ("YouTube", "upload, checks", "app"), ("Recommender", "home and search", "app"),
     ("Viewers", "bike owners", "user"), ("Advertisers", "tool brands", "merchant")],
    [(0, 1, "12-minute Tamil video on a carburettor", "msg"),
     (1, 1, "make 8 sizes; auto captions; dub to Hindi", "self"),
     (1, 1, "Content ID: any music owned by a label?", "self"),
     (1, 2, "new video, tagged: bikes, repair, Tamil", "msg"),
     (2, 3, "shown to people who watch bike repair", "msg"),
     (3, 2, "watched 9 of 12 minutes; 300 subscribe", "ret"),
     (4, 1, "₹80 per 1,000 ad views (illustrative)", "money"),
     (1, 0, "55% of the ad money, monthly", "money")],
    note="1 lakh views × 0.6 ads × ₹80 ÷ 1,000 × 55% ≈ ₹2,640 a month from ads (illustrative).")

FIGS["share_yt"] = hbars([("Kick subscriptions", 95, "to lure big streamers"), ("YouTube fan funding", 70, "memberships, Super Chat"),
                          ("Twitch Partner Plus", 70, "top streamers only"), ("YouTube long-form ads", 55, "the standard"),
                          ("Twitch standard subs", 50, "most streamers"), ("YouTube Shorts", 45, "share of a pooled fund")],
                         100, lw=150, unit="%", fmt="{:,}", colors=["#c47f17", "#0b5d7a", "#7c3aa6", "#0b5d7a", "#7c3aa6", "#0b5d7a"],
                         note="Creator’s share of each rupee (or dollar) earned, 2025–26")

# ---------- Spotify ----------
FIGS["flow_sp"] = seq(
    [("Ananya", "free plan, Pune", "user"), ("Spotify", "app, recommender", "app"), ("Cache", "near her", "network"),
     ("Advertiser", "a shoe brand", "merchant"), ("Labels, publishers", "rights owners", "partner")],
    [(0, 1, "Monday: opens Discover Weekly", "msg"),
     (1, 0, "30 songs picked from what she and similar people play", "ret"),
     (0, 2, "fetch the song file", "msg"),
     (2, 0, "audio, from a nearby server", "ret"),
     (1, 1, "past 30 seconds: counted as a stream", "self"),
     (1, 0, "an audio ad after a few songs", "msg"),
     (3, 1, "₹ per 1,000 ad plays", "money"),
     (1, 1, "month end: pool the revenue, split by share of streams", "self"),
     (1, 4, "about two-thirds of revenue", "money")],
    note="There is no fixed rate per play: each rights owner gets its share of all streams that month.")

FIGS["loop_sp"] = loop(["Listen free|with ads", "Spotify learns|your taste", "Discover Weekly,|Wrapped feel personal",
                        "Friends see|and join", "Ads and limits|start to annoy", "Upgrade|to Premium"],
                       "Free feeds Premium|30 crore pay of 77.7 crore", bw=150, h=236)

# ---------- Zynga ----------
FIGS["flow_zy"] = seq(
    [("Lakshmi", "Toon Blast player", "user"), ("Game app", "on her phone", "app"), ("Game server", "saves progress", "app"),
     ("Ad network", "sells ad slots", "merchant"), ("App store", "takes payment", "bank")],
    [(0, 1, "loses level 212 by two moves", "msg"),
     (1, 0, "offer: +5 moves for an ad, or 900 coins", "ret"),
     (0, 3, "chooses the 30-second ad", "msg"),
     (3, 1, "pays Zynga about ₹1 for that view", "money"),
     (1, 2, "level won: save stars and progress", "msg"),
     (0, 1, "a week later: stuck on a hard level", "msg"),
     (0, 4, "buys a coin pack for ₹89", "money"),
     (4, 1, "Zynga gets ₹89 minus the store’s cut (up to 30%)", "money"),
     (2, 0, "team chest opens; daily reward tomorrow", "ret")],
    note="Most players never pay. Ads earn from them; a few buyers earn most of the rest.")


def ltv_zy():
    o = [MK, '<g class="c">']
    chain = [("$0.12", "revenue per player", "per active day"), ("× 40 days", "active over the", "player’s life"),
             ("= $4.80", "lifetime value", "(LTV)"), ("vs $3.00", "cost to win one", "install (CPI)")]
    for i, (a, b, c) in enumerate(chain):
        x = 4 + i * 170
        st = G if i == 2 else (R if i == 3 else B)
        o.append(box(x, 26, 146, 64, *st, [(a, "b t13"), (b, ""), (c, "")]))
        if i < 3: o.append(f'<line x1="{x + 147}" y1="58" x2="{x + 168}" y2="58" class="ln" marker-end="url(#pa)"/>')
    o.append(T(4, 14, "Does buying a new player pay back? (illustrative casual-game numbers)", "s"))
    o.append(T(4, 112, "$4.80 > $3.00, so ads to win players pay back. Lift day-7 return and the 40 days grows: that is why games obsess over retention.", "b acc"))
    o.append("</g>")
    return svg(122, o)
FIGS["ltv_zy"] = ltv_zy()

# ---------- comparison ----------
FIGS["pos2x2"] = two_by_two("How people pay: mostly ads → mostly subscription", "What brings them back: live moments → a library",
                            ["Free, with a deep library", "Paid, with a deep library", "Free, built on live moments", "Paid, built on live moments"],
                            [("YouTube", 0.12, 0.84, "#b93a32", "start"), ("Spotify", 0.55, 0.78, "#127a64", "start"),
                             ("Netflix", 0.9, 0.72, "#b93a32", "end"), ("Prime Video", 0.72, 0.58, "#c47f17", "end"),
                             ("JioHotstar", 0.34, 0.2, "#0b5d7a", "start"), ("Zynga: a few buy extras", 0.5, 0.4, "#7c3aa6", "start")], h=290)
