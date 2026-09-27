"""Primer figures for M5; imported at the end of m5_figs.py (shares its helpers and FIGS)."""
from m5_figs import FIGS, svg, T, lines, hbars  # noqa: F401

MK = ('<defs><marker id="pa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
      '<path d="M0,0 L10,5 L0,10 z" fill="#4a5563"/></marker>'
      '<marker id="pg" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4.5" markerHeight="4.5" orient="auto">'
      '<path d="M0,0 L10,5 L0,10 z" fill="#127a64"/></marker>'
      '<marker id="pr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
      '<path d="M0,0 L10,5 L0,10 z" fill="#8a939e"/></marker></defs>')

def box(x, y, w, h, fill, st, rows, sw=1.4, lh=14):
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{st}" stroke-width="{sw}"/>']
    y0 = y + h / 2 - (len(rows) - 1) * lh / 2 + 4
    for i, (s, c) in enumerate(rows):
        o.append(T(x + w / 2, y0 + i * lh, s, c, "middle"))
    return "".join(o)

G, B, A, GR, R = ("#e1f2ec", "#127a64"), ("#e3f0f5", "#0b5d7a"), ("#fde7c8", "#c47f17"), ("#eef0f2", "#5b6470"), ("#fcecea", "#b93a32")


def money():
    o = [MK,
         '<line x1="470" y1="8" x2="500" y2="8" class="money"/>', T(506, 12, "money", "s"),
         '<line x1="552" y1="8" x2="582" y2="8" class="msg"/>', T(588, 12, "attention, posts", "s"),
         box(6, 30, 136, 60, *A, [("Creators", "b"), ("post Reels, videos", ""), ("1 in 100 users", "s")]),
         box(6, 168, 136, 60, *G, [("Users", "b"), ("scroll, react, chat", ""), ("pay ₹0", "s")]),
         box(262, 96, 156, 76, *B, [("Platform", "b"), ("ranks each feed,", ""), ("runs the ad auction,", ""), ("keeps chats ad-free", "s")]),
         box(538, 30, 136, 60, *GR, [("Advertisers, brands", "b"), ("Amazon to a", ""), ("Kochi bakery", "s")]),
         box(538, 168, 136, 60, *GR, [("Businesses", "b"), ("banks, shops, brands", ""), ("on WhatsApp", "s")]),
         # creators -> platform (posts)
         '<line x1="142" y1="76" x2="258" y2="112" class="msg" marker-end="url(#pa)"/>',
         T(196, 84, "① posts, Reels", "halo", "middle"),
         # users -> platform (attention)
         '<line x1="142" y1="186" x2="258" y2="160" class="msg" marker-end="url(#pa)"/>',
         T(206, 196, "② attention, data", "halo", "middle"),
         # platform -> users (feed)
         '<line x1="262" y1="170" x2="146" y2="214" class="ret" marker-end="url(#pr)"/>',
         T(214, 232, "③ a ranked feed", "halo s", "middle"),
         # advertisers -> platform (money)
         '<line x1="538" y1="78" x2="424" y2="112" class="money" marker-end="url(#pg)"/>',
         T(484, 116, "④ ₹ per 1,000", "b grn halo", "middle"), T(484, 130, "ad views", "grn halo", "middle"),
         # businesses -> platform (money)
         '<line x1="538" y1="194" x2="424" y2="160" class="money" marker-end="url(#pg)"/>',
         T(480, 206, "⑤ ₹0.12–0.86", "b grn halo", "middle"), T(480, 220, "per message", "grn halo", "middle"),
         # brands -> creators (money, direct)
         '<path d="M538,44 L146,44" class="money" marker-end="url(#pg)"/>',
         T(340, 36, "⑥ brand deals, paid directly: ₹20,000–1 lakh a post (illustrative)", "b grn halo", "middle"),
         ]
    return svg(240, o)
FIGS["money"] = money()


def hour():
    o = [MK, '<g class="c">']
    chain = [("60 minutes", "of Reels", ""), ("÷ 15 s a Reel", "= 240 Reels", "seen"), ("× 1 in 10", "is an ad", "= 24 ads")]
    for i, (a, b, c) in enumerate(chain):
        x = 4 + i * 150
        o.append(box(x, 30, 126, 64, *B, [(a, "b"), (b, ""), (c, "")]))
        o.append(f'<line x1="{x + 126}" y1="62" x2="{x + 146}" y2="62" class="ln" marker-end="url(#pa)"/>')
    o.append(f'<line x1="430" y1="62" x2="470" y2="30" class="ln" marker-end="url(#pa)"/>')
    o.append(f'<line x1="430" y1="62" x2="470" y2="96" class="ln" marker-end="url(#pa)"/>')
    o.append(box(474, 2, 206, 52, *A, [("India: × ₹60 per 1,000", "b"), ("24 × ₹60 ÷ 1,000 = ₹1.44", "")]))
    o.append(box(474, 70, 206, 52, *G, [("US: × ₹700 per 1,000", "b"), ("24 × ₹700 ÷ 1,000 = ₹16.80", "")]))
    o.append(T(4, 142, "Same app, same hour, same 24 ads: about 12× the money. India wins on users, not on revenue per user.", "b acc"))
    o.append("</g>")
    return svg(150, o)
FIGS["hour"] = hour()

FIGS["arpu"] = hbars([("US & Canada", 68.44, ""), ("Europe", 23.14, ""), ("Asia-Pacific", 5.52, "includes India, Japan, Australia"),
                      ("Rest of world", 4.50, "")], 68.44, lw=110, fmt="${:,.2f}",
                     colors=["#9aa3ad", "#9aa3ad", "#c47f17", "#9aa3ad"], note="Revenue per Facebook user, October–December 2023")

FIGS["players"] = hbars([("Facebook", 3.0, " monthly"), ("WhatsApp", 3.0, " monthly"), ("YouTube", 2.7, " users"),
                         ("Instagram", 2.0, " DAILY: the hardest measure"), ("Telegram", 1.0, " monthly"), ("Snapchat", 1.0, " monthly"),
                         ("X", 0.55, " monthly"), ("Threads", 0.5, " monthly")], 3.0, lw=90, unit=" bn", fmt="{:,.2g}",
                        colors=["#0b5d7a", "#0b5d7a", "#9aa3ad", "#127a64", "#9aa3ad", "#9aa3ad", "#9aa3ad", "#0b5d7a"],
                        note="Latest reported users, 2025–26 (blue = Meta; green = Meta, counted daily)")


def timeline():
    pts = [(58, "Sep 2016", "Cheap data", ["Jio’s free data;", "next 30 crore", "Indians come", "online via", "WhatsApp, YouTube"], "#0b5d7a"),
           (190, "Jun 2020", "TikTok ban", ["~20 crore users", "free; Moj, Josh", "race; Reels", "launches in July"], "#b93a32"),
           (322, "Jan–Feb 2021", "Privacy scare", ["Telegram +25 mn", "in 72 hours;", "WhatsApp delays", "policy; IT Rules"], "#c47f17"),
           (454, "2022–26", "Strangers’ posts", ["Feeds rebuilt on", "recommendations;", "Threads, Channels,", "AI ranking"], "#0b5d7a"),
           (590, "Nov 2025", "Data rules", ["DPDP Rules", "notified; consent", "duties apply", "from ~May 2027"], "#3e4fb8")]
    o = ['<line x1="10" y1="64" x2="670" y2="64" stroke="#4a5563" stroke-width="2"/><g class="c">']
    for x, d, h, ls, col in pts:
        o.append(f'<circle cx="{x}" cy="64" r="6.5" fill="{col}"/>')
        o.append(T(x, 50, d, "b", "middle"))
        o.append(T(x - 54, 84, h, "b", "start", fill=col))
        for i, l in enumerate(ls): o.append(T(x - 54, 98 + i * 13, l))
    o.append("</g>")
    o.append(T(10, 16, "Each turning point moved hundreds of millions of users, or changed what platforms must do for them.", "s"))
    return svg(162, o)
FIGS["timeline"] = timeline()


def pyramid():
    o = []
    cx, top, base, H = 170, 8, 158, 150
    bands = [(0.0, 0.18, "#c47f17", "1%", "create most posts"), (0.18, 0.42, "#0b5d7a", "9%", "comment, react, share"),
             (0.42, 1.0, "#9fb8c4", "90%", "only watch")]
    for a, b, col, pct, txt in bands:
        ya, yb = top + a * H, top + b * H
        wa, wb = a * 150, b * 150
        o.append(f'<polygon points="{cx - wa:.1f},{ya:.1f} {cx + wa:.1f},{ya:.1f} {cx + wb:.1f},{yb:.1f} {cx - wb:.1f},{yb:.1f}" fill="{col}" stroke="#fff" stroke-width="2"/>')
        ym = (ya + yb) / 2 + 5
        o.append(T(cx, ym, pct, "b w" if col != "#9fb8c4" else "b", "middle"))
        o.append(f'<line x1="{cx + (wa + wb) / 2 + 4:.1f}" y1="{ym - 4:.1f}" x2="350" y2="{ym - 4:.1f}" stroke="#c3cad2"/>')
        o.append(T(356, ym, txt, "b"))
    o.append(T(356, 36, "a creator losing interest hurts thousands", "s"))
    o.append(T(356, 76, "their shares bring friends back", "s"))
    o.append(T(356, 132, "the audience that ads are sold to", "s"))
    o.append(T(356, 156, "Farhan’s group: 4–5 of 47 send most messages", "b acc"))
    return svg(164, o)
FIGS["pyramid"] = pyramid()


def rank():
    rows = [("Watch to the end", 0.40, 1), ("Like", 0.10, 1), ("Comment", 0.03, 5), ("Share to a friend", 0.02, 20), ("“Not interested”", 0.01, -30)]
    o = [T(0, 12, "Reel A, for Priya, 22, Pune. The app predicts each action, multiplies by a weight, and adds up.", "s"),
         T(150, 34, "chance she does it", "b", "middle"), T(262, 34, "× weight", "b", "middle"), T(336, 34, "= points", "b", "middle"),
         f'<line x1="440" y1="40" x2="440" y2="176" stroke="#4a5563"/>']
    sc = 200
    for i, (lab, p, w) in enumerate(rows):
        y = 56 + i * 24; v = p * w
        o.append(T(4, y, lab, "b"))
        o.append(T(150, y, f"{p:.2f}", "", "middle")); o.append(T(262, y, f"× {w}".replace("-", "−"), "", "middle")); o.append(T(336, y, f"{v:+.2f}".replace("-", "−"), "b", "middle"))
        col = "#b93a32" if v < 0 else ("#127a64" if w >= 5 else "#0b5d7a")
        x = 440 if v >= 0 else 440 + v * sc
        o.append(f'<rect x="{x:.1f}" y="{y - 11}" width="{abs(v) * sc:.1f}" height="14" fill="{col}" rx="2"/>')
    o.append(f'<line x1="4" y1="176" x2="360" y2="176" stroke="#4a5563"/>')
    o.append(T(4, 192, "Score for Reel A", "b")); o.append(T(336, 192, "0.75", "b acc", "middle"))
    o.append(T(446, 192, "Reel B scores 0.60, so A goes first", "b acc"))
    o.append(T(530, 126, "← a rare share scores", "s")); o.append(T(530, 139, "as much as watching", "s")); o.append(T(530, 152, "to the end", "s"))
    return svg(200, o)
FIGS["rank"] = rank()
