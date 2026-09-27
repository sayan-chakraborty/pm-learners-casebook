"""Encryption figures for M5; imported at the end of figs_tech.py."""
import math
from m5_figs import FIGS, svg, T, lines, seq  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R  # noqa: F401
from figs_tech import arrow  # noqa: F401


def pill(x, y, w, ok, txt=None):
    f, st = (("#e1f2ec", "#127a64") if ok else ("#fcecea", "#b93a32"))
    return (f'<rect x="{x}" y="{y}" width="{w}" height="18" rx="9" fill="{f}" stroke="{st}"/>'
            + T(x + w / 2, y + 13, txt or ("locked" if ok else "can read"), "b", "middle", fill=st))


# ---------- who can read ----------
def path():
    nodes = ["Farhan’s|phone", "Café|Wi-Fi", "Telecom|(his)", "Internet|links", "WhatsApp|server", "Telecom|(hers)", "Sana’s|phone"]
    X0, W, GAP = 110, 70, 11
    o = [MK, '<g class="c">']
    for i, n in enumerate(nodes):
        x = X0 + i * (W + GAP)
        fill, st = G if i in (0, 6) else (B if i == 4 else GR)
        a, b = n.split("|")
        o.append(box(x, 2, W, 38, fill, st, [(a, "b"), (b, "")], lh=13))
        if i < 6: o.append(arrow(x + W, 21, x + W + GAP - 1, 21))
    rows = [("No encryption", [False] * 7), ("In transit (HTTPS)", [False, True, True, True, False, True, False]),
            ("End to end", [False, True, True, True, True, True, False])]
    for r, (lab, cells) in enumerate(rows):
        y = 54 + r * 26
        o.append(T(0, y + 13, lab, "b"))
        for i, ok in enumerate(cells):
            x = X0 + i * (W + GAP)
            if i in (0, 6): o.append(pill(x + 2, y, W - 4, False, "reads"))
            else: o.append(pill(x + 2, y, W - 4, ok))
    o.append(T(0, 144, "The ends must read the message. The question is who else can: everyone, the company, or nobody.", "b acc"))
    o.append("</g>")
    return svg(150, o)
FIGS["path"] = path()


# ---------- hashing ----------
def hash_fig():
    o = [MK, '<g class="c">']
    for i, (inp, out) in enumerate((("Meet me at 5 pm", "dad1adbc78eaadd7c4fbf296…"), ("Meet me at 6 pm", "6cb7f423ddccccf18fe403e6…"))):
        y = 6 + i * 52
        o.append(box(0, y, 150, 38, *G, [(inp, "b")]))
        o.append(arrow(150, y + 19, 196, y + 19))
        o.append(box(200, y, 120, 38, *A, [("SHA-256", "b"), ("the grinder", "s")]))
        o.append(arrow(320, y + 19, 366, y + 19))
        o.append(box(370, y, 250, 38, *GR, [(out, "b")]))
    o.append(T(378, 116, "one character changed → nothing in common", "b red"))
    o.append(T(0, 116, "Always 64 characters, for a word or a film.", "s"))
    o.append(T(0, 132, "No way back: the code can be checked, never reversed.", "b acc"))
    o.append("</g>")
    return svg(138, o)
FIGS["hash"] = hash_fig()


def keyicon(x, y, col="#c47f17"):
    return (f'<circle cx="{x}" cy="{y}" r="6" fill="none" stroke="{col}" stroke-width="2.4"/>'
            f'<line x1="{x + 6}" y1="{y}" x2="{x + 22}" y2="{y}" stroke="{col}" stroke-width="2.4"/>'
            f'<line x1="{x + 18}" y1="{y}" x2="{x + 18}" y2="{y + 6}" stroke="{col}" stroke-width="2.4"/>')


def padlock(x, y, open_=False, col="#127a64"):
    arc = (f'<path d="M{x + 3},{y} L{x + 3},{y - 7} A6,6 0 0 1 {x + 15},{y - 7} L{x + 15},{y - 3}" fill="none" stroke="{col}" stroke-width="2.2"/>'
           if open_ else f'<path d="M{x + 3},{y} L{x + 3},{y - 6} A6,6 0 0 1 {x + 15},{y - 6} L{x + 15},{y}" fill="none" stroke="{col}" stroke-width="2.2"/>')
    return arc + f'<rect x="{x}" y="{y}" width="18" height="14" rx="2" fill="{col}"/>'


# ---------- two kinds of lock ----------
def locks():
    o = [MK, '<g class="c">', T(0, 12, "One shared key (AES)", "b t12"), T(356, 12, "Open padlocks (public and private keys)", "b t12")]
    o.append(box(0, 30, 100, 44, *G, [("Farhan", "b"), ("has key K", "s")]))
    o.append(box(230, 30, 100, 44, *G, [("Sana", "b"), ("needs key K", "s")]))
    o.append(keyicon(30, 90)); o.append(keyicon(262, 90))
    o.append(arrow(100, 52, 226, 52, col="#b93a32", dash=True, mk="pa"))
    o.append(T(165, 44, "send K… how?", "b red halo", "middle"))
    o.append(box(115, 98, 100, 40, *R, [("Eavesdropper", "b"), ("copies K on the way", "s")]))
    o.append(f'<line x1="165" y1="56" x2="165" y2="96" stroke="#b93a32" stroke-dasharray="3 3"/>')
    o.append(T(0, 160, "Fast, but the key must travel, and a", "s")); o.append(T(0, 173, "copied key opens everything.", "b red"))
    # padlocks
    o.append(box(356, 30, 110, 50, *G, [("Sana", "b"), ("keeps the only key", "s"), ("(private)", "s")]))
    o.append(box(570, 30, 110, 50, *G, [("Farhan", "b"), ("snaps her padlock", "s"), ("on his box", "s")]))
    o.append(arrow(466, 40, 566, 40)); o.append(T(516, 30, "open padlocks (public)", "s halo", "middle"))
    o.append(arrow(566, 72, 470, 72, col="#127a64")); o.append(T(516, 88, "locked box", "b grn halo", "middle"))
    o.append(box(446, 104, 140, 40, *R, [("Eavesdropper", "b"), ("sees only a locked box", "s")]))
    o.append(T(356, 160, "Padlocks can be handed out freely: only", "s")); o.append(T(356, 173, "Sana can open what they lock.", "b grn"))
    o.append('<line x1="340" y1="4" x2="340" y2="176" stroke="#e1e5ea"/>')
    o.append("</g>")
    return svg(180, o)
FIGS["locks"] = locks()


# ---------- keys needed ----------
def keys():
    rows = [(10, 45, 10), (100, 4950, 100), (1000, 499500, 1000)]
    L = 150; W = 380; mx = math.log10(499500)
    o = [T(0, 12, "Keys needed for everyone to talk privately in pairs (bar length on a log scale)", "s")]
    for i, (n, sh, pr) in enumerate(rows):
        y = 28 + i * 44
        o.append(T(L - 10, y + 20, f"{n:,} people", "b", "end"))
        w1 = W * math.log10(sh) / mx; w2 = W * math.log10(pr) / mx
        o.append(f'<rect x="{L}" y="{y + 4}" width="{w1:.1f}" height="14" fill="#b93a32" rx="2"/>')
        o.append(T(L + w1 + 6, y + 15, f"{sh:,} shared keys".replace("499,500", "4,99,500"), "b red"))
        o.append(f'<rect x="{L}" y="{y + 21}" width="{w2:.1f}" height="14" fill="#127a64" rx="2"/>')
        o.append(T(L + w2 + 6, y + 32, f"{pr:,} key pairs", "b grn"))
    o.append(T(0, 170, "n × (n − 1) ÷ 2 against n: for WhatsApp’s 3 bn users, shared keys would be about 4.5 × 10¹⁸.", "b acc"))
    return svg(178, o)
FIGS["keys"] = keys()


# ---------- signature ----------
def sign():
    o = [MK, '<g class="c">', T(0, 12, "At WhatsApp", "b t12"), T(0, 104, "On your phone", "b t12")]
    o.append(box(0, 22, 120, 44, *GR, [("App update", "b"), ("the file", "s")]))
    o.append(arrow(120, 44, 150, 44)); o.append(box(154, 22, 110, 44, *A, [("Hash it", "b"), ("fingerprint", "s")]))
    o.append(arrow(264, 44, 294, 44)); o.append(box(298, 22, 150, 44, *B, [("Lock with private key", "b"), ("= the signature", "s")]))
    o.append(arrow(448, 44, 478, 44)); o.append(box(482, 22, 198, 44, *GR, [("Ship: file + signature", "b"), ("via the app store", "s")]))
    o.append(arrow(580, 66, 580, 110))
    o.append(box(482, 114, 198, 44, *B, [("Open signature with", "b"), ("WhatsApp’s public key", "s")]))
    o.append(box(250, 114, 200, 44, *A, [("Hash the file you got", "b"), ("your own fingerprint", "s")]))
    o.append(arrow(482, 136, 454, 136))
    o.append(box(0, 114, 214, 44, *G, [("Match → install ✓", "b"), ("Fake “WhatsApp Gold” → refuse ✗", "s")]))
    o.append(arrow(250, 136, 218, 136))
    o.append(T(0, 176, "Only the private key can make the signature; anyone with the public key can check it.", "b acc"))
    o.append("</g>")
    return svg(182, o)
FIGS["sign"] = sign()


# ---------- paint mixing ----------
def paint():
    Y, Rd, Bl, Or, Gr, Br = "#f2c94c", "#d64541", "#3b6fb6", "#e8883a", "#5aa469", "#8b5a2b"
    def blob(x, y, col, lab, sub=""):
        return (f'<circle cx="{x}" cy="{y}" r="16" fill="{col}" stroke="#4a5563"/>' + T(x, y + 30, lab, "b", "middle")
                + (T(x, y + 43, sub, "s", "middle") if sub else ""))
    o = [MK, '<g class="c">']
    for (y, who, sec, seccol, secsub, mix, mixcol, mixsub, got, gotcol) in (
            (40, "Riya", "secret red", Rd, "secret 6", "orange", Or, "5⁶ mod 23 = 8", "gets green", Gr),
            (164, "Farhan", "secret blue", Bl, "secret 15", "green", Gr, "5¹⁵ mod 23 = 19", "gets orange", Or)):
        o.append(T(0, y + 5, who, "b t12"))
        o.append(blob(80, y, Y, "public yellow", "5 and 23")); o.append(T(112, y + 5, "+", "b t13", "middle"))
        o.append(blob(144, y, seccol, sec, secsub)); o.append(arrow(162, y, 212, y))
        o.append(blob(232, y, mixcol, mix, mixsub))
        o.append(blob(452, y, gotcol, got, "from the other")); o.append(T(484, y + 5, "+", "b t13", "middle"))
        o.append(blob(516, y, seccol, "own secret", "")); o.append(arrow(534, y, 584, y))
        o.append(blob(604, y, Br, "brown", "19⁶ or 8¹⁵ mod 23 = 2"))
    o.append(arrow(250, 50, 434, 154, col="#8a939e", dash=True, mk="pr")); o.append(arrow(250, 154, 434, 50, col="#8a939e", dash=True, mk="pr"))
    o.append(T(342, 88, "swapped in public", "s halo", "middle"))
    o.append(T(340, 234, "An eavesdropper sees yellow, orange and green, but can’t unmix them to make the brown.", "b acc", "middle"))
    o.append("</g>")
    return svg(242, o)
FIGS["paint"] = paint()


# ---------- in transit vs end to end ----------
def e2e():
    o = [MK, '<g class="c">']
    for r, (title, srv, sub, ok) in enumerate((("In transit (HTTPS)", "“Meet me at 5 pm”", "server unlocks, can read, relocks", False),
                                              ("End to end", "locked box", "to: Sana · 9:14 pm · 1 KB", True))):
        y = 10 + r * 78
        o.append(T(0, y + 26, title, "b t12"))
        o.append(box(150, y, 96, 44, *G, [("Farhan", "b"), ("locks", "s")]))
        o.append(box(344, y, 170, 44, *(G if ok else R), [(srv if not ok else "a locked box", "b"), (sub, "s")]))
        o.append(box(590, y, 90, 44, *G, [("Sana", "b"), ("unlocks", "s")]))
        o.append(arrow(246, y + 22, 340, y + 22, col="#127a64")); o.append(arrow(514, y + 22, 586, y + 22, col="#127a64"))
        o.append(T(293, y + 16, "locked", "s halo", "middle")); o.append(T(550, y + 16, "locked", "s halo", "middle"))
    o.append(T(150, 160, "Server can: search, filter spam, run AI, hand content to police.", "red"))
    o.append(T(150, 174, "End to end, it can only deliver, and see the label.", "b grn"))
    o.append("</g>")
    return svg(180, o)
FIGS["e2e"] = e2e()


# ---------- pre-keys (X3DH) ----------
FIGS["prekey"] = seq(
    [("Sana’s phone", "switched off", "user"), ("WhatsApp server", "key directory", "app"), ("Farhan’s phone", "starts a chat", "user")],
    [(0, 1, "earlier: public keys + 100 one-time pre-keys", "msg"),
     (0, 0, "phone switched off", "self"),
     (2, 1, "“I want to message Sana”", "msg"),
     (1, 2, "her public keys + one-time pre-key #57", "ret"),
     (1, 1, "delete #57: each is used once", "self"),
     (2, 2, "check signature; 3–4 key exchanges → shared secret", "self"),
     (2, 1, "first message, locked; “I used #57”", "msg"),
     (1, 0, "delivered when she’s back online", "msg"),
     (0, 0, "same exchanges with her private keys → same secret; reads", "self")],
    note="Pre-keys let a conversation start safely even when the other phone is off.")


# ---------- ratchet ----------
def ratchet():
    o = [MK, '<g class="c">']
    o.append(box(0, 40, 80, 40, *B, [("Shared", "b"), ("secret", "s")]))
    xs = [110, 210, 310, 410]
    for i, x in enumerate(xs):
        dead = i < 2; stolen = i == 2
        fill, st = (("#eef0f2", "#9aa3ad") if dead else (R if stolen else A))
        o.append(box(x, 40, 76, 40, fill, st, [(f"key {i + 1}", "b"), ("deleted" if dead else ("stolen!" if stolen else "in use"), "s")]))
        o.append(arrow(x - 24 if i == 0 else x - 24, 60, x - 2, 60))
        o.append(box(x, 104, 76, 30, *GR, [(f"message {i + 1}", "")], sw=1))
        o.append(f'<line x1="{x + 38}" y1="80" x2="{x + 38}" y2="102" stroke="#9aa3ad"/>')
    o.append(T(348, 152, "thief reads message 3 only", "b red", "middle"))
    o.append(f'<line x1="300" y1="20" x2="200" y2="20" stroke="#b93a32" stroke-width="1.6" marker-end="url(#pa)"/>')
    o.append(T(250, 14, "can’t go back ✗", "b red", "middle"))
    o.append(box(520, 20, 160, 52, *G, [("Sana replies:", "b"), ("new key exchange mixed", "s"), ("in → fresh chain", "s")]))
    o.append(arrow(486, 60, 516, 50))
    o.append(box(520, 90, 160, 44, *G, [("key 3 no longer", "b"), ("opens anything new", "s")]))
    o.append(T(0, 176, "Each step is one-way, like a car jack: forward secrecy (the past stays locked) and self-healing (the future re-locks).", "b acc"))
    o.append("</g>")
    return svg(184, o)
FIGS["ratchet"] = ratchet()


# ---------- man in the middle and the security code ----------
def mitm():
    o = [MK, '<g class="c">', T(0, 12, "With someone in the middle", "b t12 red"), T(0, 112, "Nobody in the middle", "b t12 grn")]
    o.append(box(0, 22, 110, 42, *G, [("Farhan", "b"), ("holds padlock M", "s")]))
    o.append(box(285, 22, 110, 42, *R, [("Attacker", "b"), ("opens, reads, relocks", "s")]))
    o.append(box(570, 22, 110, 42, *G, [("Sana", "b"), ("holds padlock F′", "s")]))
    o.append(arrow(110, 43, 281, 43, col="#b93a32")); o.append(arrow(395, 43, 566, 43, col="#b93a32"))
    o.append(T(0, 82, "Farhan’s code: 12093 44817 …", "b")); o.append(T(680, 82, "Sana’s code: 90552 18302 …", "b", "end"))
    o.append(T(340, 96, "codes don’t match → someone swapped the padlocks", "b red", "middle"))
    o.append(box(0, 122, 110, 42, *G, [("Farhan", "b"), ("holds Sana’s padlock", "s")]))
    o.append(box(570, 122, 110, 42, *G, [("Sana", "b"), ("holds Farhan’s", "s")]))
    o.append(arrow(110, 143, 566, 143, col="#127a64"))
    o.append(T(0, 182, "Farhan’s code: 20931 44012 …", "b grn")); o.append(T(680, 182, "Sana’s code: 20931 44012 …", "b grn", "end"))
    o.append(T(340, 196, "same 60 digits on both phones → safe", "b grn", "middle"))
    o.append("</g>")
    return svg(202, o)
FIGS["mitm"] = mitm()


# ---------- what E2E hides ----------
def hides():
    left = ["Message text", "Photos, videos, documents", "Voice notes and calls", "Status updates", "Backups, if the user turns on encryption"]
    right = ["Who messages whom, and when (metadata)", "How often; your phone number, IP, phone model", "Who is in which group",
             "Anything on an unlocked or hacked phone", "Screenshots and forwards by the receiver", "Backups left unencrypted; reported messages"]
    o = [f'<rect x="0" y="0" width="330" height="{24 + 18 * 6 + 8}" rx="6" fill="#e7f4f0" stroke="#127a64"/>',
         f'<rect x="350" y="0" width="330" height="{24 + 18 * 6 + 8}" rx="6" fill="#fbf4e6" stroke="#c47f17"/>',
         T(12, 18, "Locked: only the two phones can read", "b grn"), T(362, 18, "Not locked by end to end", "b amb")]
    for i, t in enumerate(left): o.append(T(12, 40 + i * 18, "✓ " + t))
    for i, t in enumerate(right): o.append(T(362, 40 + i * 18, "• " + t))
    return svg(24 + 18 * 6 + 10, o)
FIGS["hides"] = hides()
