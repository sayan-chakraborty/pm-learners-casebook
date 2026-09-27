"""Technology figures for M5 (System design IV + encryption); imported at the end of m5_figs.py."""
from m5_figs import FIGS, svg, T, lines, seq, hbars  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R  # noqa: F401

P = ("#f1e6f8", "#7c3aa6")


def arrow(x1, y1, x2, y2, col="#4a5563", w=1.4, dash=False, mk="pa"):
    d = ' stroke-dasharray="4 3"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}"{d} marker-end="url(#{mk})"/>'


# ---------- 1. polling vs open line ----------
def poll():
    L, Rr = 170, 670
    X = lambda t: L + (Rr - L) * t / 60
    o = [MK, '<g class="c">']
    for yy, title, sub in ((40, "Polling every 10 s", "“anything new?” all day"), (126, "One open line", "server pushes at once")):
        o.append(T(0, yy, title, "b t12")); o.append(T(0, yy + 14, sub, "s"))
        o.append(f'<line x1="{L}" y1="{yy + 4}" x2="{Rr}" y2="{yy + 4}" stroke="#9aa3ad"/>')
    for t in range(0, 61, 10):
        o.append(T(X(t), 182, f"{t} s", "s", "middle"))
    # polling requests
    for t in range(0, 51, 10):
        col = "#127a64" if t == 30 else "#9aa3ad"
        o.append(f'<line x1="{X(t):.1f}" y1="44" x2="{X(t):.1f}" y2="18" stroke="{col}" stroke-width="2"/>')
        o.append(T(X(t), 14, "new!" if t == 30 else "nothing", "b grn" if t == 30 else "s", "middle"))
    o.append(f'<circle cx="{X(23):.1f}" cy="44" r="5" fill="#c47f17"/>')
    o.append(T(X(23), 64, "message arrives 23 s", "amb", "middle"))
    o.append(f'<line x1="{X(23):.1f}" y1="72" x2="{X(30):.1f}" y2="72" stroke="#b93a32" stroke-width="2"/>')
    o.append(T(X(26.5), 86, "7 s late", "b red", "middle"))
    o.append(T(Rr, 100, "8,640 requests a day per phone, almost all “nothing”", "b red", "end"))
    # open line
    o.append(f'<rect x="{L}" y="126" width="{Rr - L}" height="8" rx="4" fill="#e1f2ec" stroke="#127a64"/>')
    o.append(f'<circle cx="{X(23):.1f}" cy="130" r="5" fill="#c47f17"/>')
    o.append(T(X(23), 150, "arrives 23 s → delivered at once", "b grn", "middle"))
    o.append(T(Rr, 166, "one heartbeat every 4 min = 360 a day", "b grn", "end"))
    o.append("</g>")
    return svg(190, o)
FIGS["poll"] = poll()

# ---------- 2. ticks ----------
FIGS["ticks"] = seq(
    [("Aunt’s phone", "sender", "user"), ("Chat server A", "holds her line", "app"), ("Session directory", "who is where", "network"),
     ("Chat server B", "holds his line", "app"), ("Farhan’s phone", "receiver", "user")],
    [(0, 1, "voice note, ID 7F3A, locked", "msg"),
     (1, 0, "saved → one grey tick ✓", "ret"),
     (1, 2, "where is Farhan connected?", "msg"),
     (2, 1, "on server B", "ret"),
     (1, 3, "pass on 7F3A", "msg"),
     (3, 4, "7F3A down his open line", "msg"),
     (4, 3, "delivered", "ret"),
     (3, 0, "two grey ticks ✓✓", "ret"),
     (4, 4, "Farhan opens the chat", "self"),
     (4, 0, "read → two blue ticks", "ret")],
    note="Every receipt is a tiny message of its own: one message sent creates about three.")


# ---------- 3. store and forward ----------
def store():
    L, Rr, Bt, Tp = 60, 560, 150, 40
    X = lambda h: L + (Rr - L) * (h - 21) / 4          # 9 pm .. 1 am
    Y = lambda q: Bt - (Bt - Tp) * q / 40
    o = [f'<rect x="{X(21.17):.1f}" y="{Tp - 8}" width="{X(24.33) - X(21.17):.1f}" height="{Bt - Tp + 8}" fill="#fcecea"/>',
         T((X(21.17) + X(24.33)) / 2, Tp + 6, "Zoya’s phone in flight mode: not connected", "b red", "middle"),
         f'<line x1="{L}" y1="{Bt}" x2="{Rr}" y2="{Bt}" stroke="#4a5563"/><line x1="{L}" y1="{Tp - 8}" x2="{L}" y2="{Bt}" stroke="#4a5563"/>']
    for h, lab in ((21, "9 pm"), (22, "10 pm"), (23, "11 pm"), (24, "midnight"), (25, "1 am")):
        o.append(T(X(h), Bt + 14, lab, "s", "middle"))
    for q in (0, 20, 40): o.append(T(L - 6, Y(q) + 4, str(q), "s", "end"))
    pts = [(21.17, 0)]; q = 0
    for i in range(40):
        h = 21.23 + i * (24.3 - 21.23) / 40; pts.append((h, q)); q += 1; pts.append((h, q))
    pts += [(24.33, q), (24.35, 0), (25, 0)]
    o.append('<polyline points="' + " ".join(f"{X(h):.1f},{Y(v):.1f}" for h, v in pts) + '" fill="none" stroke="#0b5d7a" stroke-width="2.2"/>')
    o.append(T(X(21.3), Y(34), "queue on the server grows;", "b acc halo"))
    o.append(T(X(21.3), Y(34) + 14, "aunt sees one tick ✓ each time", "acc halo"))
    for i, (t, c) in enumerate([("12:20 am: she lands.", "b grn"), ("40 messages delivered", "grn"), ("in order; ticks turn", "grn"),
                                ("✓✓; the queue is", "grn"), ("emptied and deleted", "grn")]):
        o.append(T(572, 52 + i * 14, t, c))
    o.append(f'<text x="16" y="{(Tp + Bt) / 2:.0f}" text-anchor="middle" class="b" transform="rotate(-90 16 {(Tp + Bt) / 2:.0f})">messages waiting</text>')
    return svg(170, o)
FIGS["store"] = store()


# ---------- 4. fan-out ----------
def fanout():
    o = [MK, '<g class="c">', T(0, 12, "Group: fan-out on write", "b t12"), T(360, 12, "Channel: fan-out on read", "b t12")]
    o.append(box(0, 70, 86, 44, *G, [("Aunt", "b"), ("1 message", "")]))
    o.append(box(118, 70, 90, 44, *B, [("Server", "b"), ("makes 46 copies", "s")]))
    o.append(arrow(86, 92, 114, 92))
    for i in range(6):
        y = 26 + i * 26
        lab = "…" if i == 3 else f"inbox {i + 1 if i < 3 else 46 - (5 - i)}"
        o.append(box(248, y, 76, 20, *GR, [(lab, "s")], sw=1))
        o.append(arrow(208, 92, 245, y + 10))
    o.append(T(0, 196, "212 messages × 46 members = 9,752", "b acc")); o.append(T(0, 210, "deliveries a day, from one family", "acc"))
    # channel
    o.append(box(360, 70, 100, 44, *A, [("Creator", "b"), ("1 post", "")]))
    o.append(box(498, 70, 100, 44, *B, [("Stored once", "b"), ("no copies made", "s")]))
    o.append(arrow(460, 92, 494, 92))
    for i, y in enumerate((26, 52, 132, 158)):
        o.append(box(620, y, 58, 20, *GR, [("phone" if i != 2 else "phone", "s")], sw=1))
        o.append(arrow(620, y + 10, 600, 92, col="#8a939e", dash=True, mk="pr"))
    o.append(T(649, 96, "…", "b", "middle"))
    o.append(T(360, 196, "1 crore followers: one stored post; only", "b acc")); o.append(T(360, 210, "phones that open the channel fetch it", "acc"))
    o.append('<line x1="340" y1="4" x2="340" y2="212" stroke="#e1e5ea"/>')
    o.append("</g>")
    return svg(218, o)
FIGS["fanout"] = fanout()

# ---------- 5. push ----------
FIGS["push"] = seq(
    [("WhatsApp server", "has a message", "app"), ("Apple / Google push", "APNs or FCM", "network"),
     ("Farhan’s phone", "operating system", "partner"), ("WhatsApp app", "asleep", "user")],
    [(0, 0, "Farhan’s line is closed: the app is asleep", "self"),
     (0, 1, "“wake WhatsApp on this phone” (nothing readable)", "msg"),
     (1, 2, "down the one line every app shares", "msg"),
     (2, 3, "wake up for a few seconds", "msg"),
     (3, 0, "reconnect and fetch", "msg"),
     (0, 3, "the locked voice note", "ret"),
     (3, 3, "unlock; show “Aunt: voice message”; buzz", "self")],
    note="One shared line to Apple or Google for all apps saves battery; WhatsApp only asks it to knock.")


# ---------- 6. media by reference ----------
def media():
    o = [MK, '<g class="c">',
         box(0, 20, 120, 60, *G, [("Aunt’s phone", "b"), ("shrinks the video,", ""), ("locks it with key K", "s")]),
         box(250, 0, 170, 50, *A, [("Media servers", "b"), ("store a locked 16 MB file", "s")]),
         box(250, 70, 170, 50, *B, [("Chat server", "b"), ("carries a tiny message", "s")]),
         box(540, 20, 140, 60, *GR, [("199 members", "b"), ("download, unlock", ""), ("with key K", "s")]),
         arrow(120, 38, 246, 25), T(182, 22, "① upload once, 16 MB", "b halo", "middle"),
         arrow(120, 64, 246, 94), T(182, 96, "② link + key K", "halo", "middle"), T(182, 109, "+ fingerprint, ~300 bytes", "s halo", "middle"),
         arrow(420, 95, 536, 62), T(478, 96, "③ 199 × the tiny message", "halo", "middle"),
         arrow(536, 36, 424, 25, col="#8a939e", dash=True, mk="pr"), T(482, 18, "④ each fetches the file", "s halo", "middle"),
         T(0, 142, "Uploads from the aunt’s phone:", "b"),
         f'<rect x="200" y="132" width="440" height="13" fill="#b93a32" rx="2"/>', T(646, 143, "3.2 GB", "b red"),
         T(0, 162, "   file inside every message (200 × 16 MB)", "s"),
         f'<rect x="200" y="152" width="2.2" height="13" fill="#127a64"/>', T(208, 163, "16 MB by link: 200 times less", "b grn"),
         "</g>"]
    return svg(172, o)
FIGS["media"] = media()


# ---------- 9. reconnect storm ----------
def storm():
    L, Rr, Tp, Bt = 70, 660, 20, 160
    X = lambda t: L + (Rr - L) * t / 70
    Y = lambda v: Bt - (Bt - Tp) * v / 2.0      # lakh per second, axis to 2
    o = [f'<line x1="{L}" y1="{Bt}" x2="{Rr}" y2="{Bt}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{Bt}" stroke="#4a5563"/>']
    for v in (0, 0.5, 1.0, 1.5, 2.0): o.append(T(L - 6, Y(v) + 4, f"{v:g} L", "s", "end"))
    for t in range(0, 71, 10): o.append(T(X(t), Bt + 14, f"{t} s", "s", "middle"))
    o.append(f'<rect x="{X(0):.1f}" y="{Tp - 10}" width="{X(1.2) - X(0):.1f}" height="{Bt - Tp + 10}" fill="#b93a32"/>')
    o.append(T(X(1.6), Tp, "all at once: 20 lakh in 1 second (off the scale)", "b red"))
    o.append(f'<rect x="{X(0):.1f}" y="{Y(0.33):.1f}" width="{X(60) - X(0):.1f}" height="{Bt - Y(0.33):.1f}" fill="#127a64" opacity="0.8"/>')
    o.append(T(X(30), Y(0.33) - 6, "random wait up to 60 s: about 33,000 a second", "b grn halo", "middle"))
    o.append(f'<line x1="{L}" y1="{Y(1.0):.1f}" x2="{Rr}" y2="{Y(1.0):.1f}" stroke="#c47f17" stroke-width="1.6" stroke-dasharray="6 3"/>')
    o.append(T(Rr, Y(1.0) - 6, "what the healthy servers can take: ~1 lakh a second", "b amb halo", "end"))
    o.append(f'<text x="16" y="{(Tp + Bt) / 2:.0f}" text-anchor="middle" class="b" transform="rotate(-90 16 {(Tp + Bt) / 2:.0f})">reconnects a second</text>')
    return svg(180, o)
FIGS["storm"] = storm()

import figs_crypto  # noqa: E402,F401
