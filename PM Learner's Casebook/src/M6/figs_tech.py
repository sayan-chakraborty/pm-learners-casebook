"""Technology figures for M6 (blockchain, System design V); imported at the end of m6_figs.py."""
from m6_figs import FIGS, svg, T, lines, hbars, seq  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R, P  # noqa: F401

MONO = "font-family:Consolas,'Courier New',monospace"

def mono(x, y, s, cls="", anchor="start", fill=None):
    st = MONO + (f";fill:{fill}" if fill else "")
    from html import escape
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}" style="{st}">{escape(s)}</text>'


# ---------- Blockchain ----------
def block():
    o = [f'<rect x="120" y="4" width="440" height="176" rx="8" fill="#fafbfc" stroke="#0b5d7a" stroke-width="1.6"/>',
         f'<rect x="120" y="4" width="440" height="30" rx="8" fill="#e3f0f5" stroke="#0b5d7a" stroke-width="1.6"/>',
         T(136, 24, "Block 101", "b t13"), T(250, 24, "time: 12 Mar, 10:41", "s"),
         T(400, 24, "previous fingerprint:", "s"), mono(544, 24, "0000…", "b", "end"),
         T(136, 56, "Transactions", "b acc")]
    rows = [("Asha → Ravi", "2 coins", True), ("Ravi → Meena", "1 coin", False), ("Meena → Kirana shop", "0.5 coin", False)]
    for i, (a, b, hl) in enumerate(rows):
        y = 78 + i * 22
        if hl: o.append(f'<rect x="130" y="{y - 15}" width="420" height="21" rx="3" fill="#fbf4e6" stroke="#c47f17"/>')
        o.append(T(146, y, a, "b")); o.append(T(420, y, b, "", "end"))
    o.append(f'<rect x="120" y="146" width="440" height="34" rx="8" fill="#e7f4f0" stroke="#127a64" stroke-width="1.6"/>')
    o.append(T(136, 168, "this block’s fingerprint (SHA-256):", "s")); o.append(mono(544, 168, "5bdfe69ac688…", "b grn", "end"))
    o.append(T(574, 82, "Edit “2” to “20”:", "b red")); o.append(T(574, 98, "fingerprint becomes", "red"))
    o.append(mono(574, 114, "8b31a0721103…", "b red"))
    o.append(T(6, 60, "Each block is", "s")); o.append(T(6, 74, "a page of", "s")); o.append(T(6, 88, "transactions,", "s"))
    o.append(T(6, 102, "sealed at the", "s")); o.append(T(6, 116, "bottom", "s"))
    return svg(186, o)
FIGS["block"] = block()


def chain():
    o = [MK, '<g class="c">']
    blocks = [(6, "Block 101 (edited)", "Asha → Ravi 20", "prev 0000…", "now 8b31a0721103…", True),
              (238, "Block 102", "Shop → Asha 0.2 …", "prev 5bdfe69ac688…", "own d4c446af2716…", False),
              (470, "Block 103", "Meena → Ravi 0.3", "prev d4c446af2716…", "own 8b20dacbeafe…", False)]
    for x, t, tx, prev, own, bad in blocks:
        st = R if bad else B
        o.append(f'<rect x="{x}" y="10" width="204" height="104" rx="7" fill="{st[0]}" stroke="{st[1]}" stroke-width="1.6"/>')
        o.append(T(x + 10, 30, t, "b")); o.append(T(x + 10, 50, tx, ""))
        o.append(mono(x + 10, 74, prev, "b" if not bad else "", fill=None))
        o.append(mono(x + 10, 98, own, "b red" if bad else "b grn"))
    o.append('<line x1="210" y1="94" x2="236" y2="72" stroke="#b93a32" stroke-width="2.2" stroke-dasharray="4 3"/>')
    o.append(T(223, 132, "✗ mismatch: 102 expects", "b red", "middle")); o.append(mono(223, 147, "5bdfe69ac688…", "red", "middle"))
    o.append('<line x1="442" y1="94" x2="468" y2="72" stroke="#127a64" stroke-width="2.2"/>')
    o.append(T(456, 132, "✓ still matches", "b grn", "middle"))
    o.append(T(340, 176, "To hide the edit, the cheat must redo 102, 103 and every later block, on over half of all copies.", "b acc", "middle"))
    o.append("</g>")
    return svg(186, o)
FIGS["chain"] = chain()


def consensus():
    o = ['<g class="c">',
         f'<rect x="4" y="4" width="330" height="200" rx="8" fill="#fbf4e6" stroke="#c47f17" stroke-width="1.4"/>',
         f'<rect x="346" y="4" width="330" height="200" rx="8" fill="#e7f4f0" stroke="#127a64" stroke-width="1.4"/>',
         T(16, 26, "Proof of work (Bitcoin)", "b t13"), T(358, 26, "Proof of stake (Ethereum since 2022)", "b t13")]
    left = [("Guess a number, hash the block, check:", ""), ("does the hash start with enough zeros?", ""),
            ("Laptop, 4 zeros: 31,312 guesses", "b"), ("Bitcoin network: ~10²³ guesses a block", "b"),
            ("One block about every 10 minutes", ""), ("Cheating: out-guess everyone (51%)", "red"),
            ("Cost: electricity, ~150 TWh a year", "b red"), ("Checking a winner: one hash", "grn")]
    right = [("Lock a deposit (32 ETH per validator)", ""), ("Network picks the next writer at", ""),
             ("random, weighted by deposit", ""), ("Others check and sign the block", ""),
             ("A new block every 12 seconds", "b"), ("Cheating: lose part of the deposit", "red"),
             ("Cost: tied-up money, not power", "b grn"), ("Energy: down more than 99.9%", "b grn")]
    for i, (s, c) in enumerate(left): o.append(T(16, 50 + i * 19, s, c))
    for i, (s, c) in enumerate(right): o.append(T(358, 50 + i * 19, s, c))
    o.append("</g>")
    return svg(210, o)
FIGS["consensus"] = consensus()


def custody():
    o = [MK, '<g class="c">']
    o.append(box(4, 6, 326, 30, *G, [("You hold the key (self-custody)", "b")]))
    o.append(box(350, 6, 326, 30, *A, [("An exchange holds the key", "b")]))
    o.append(box(20, 50, 110, 44, *G, [("You", "b"), ("seed phrase", "s")]))
    o.append(box(204, 50, 110, 44, *B, [("Blockchain", "b"), ("your address", "s")]))
    o.append('<line x1="130" y1="72" x2="200" y2="72" class="msg" marker-end="url(#pa)"/>')
    o.append(T(165, 64, "sign", "s", "middle"))
    o.append(box(366, 50, 90, 44, *G, [("You", "b"), ("password", "s")]))
    o.append(box(476, 50, 90, 44, *A, [("Exchange", "b"), ("holds keys", "s")]))
    o.append(box(586, 50, 86, 44, *B, [("Blockchain", "b"), ("its address", "s")]))
    o.append('<line x1="456" y1="72" x2="472" y2="72" class="msg" marker-end="url(#pa)"/>')
    o.append('<line x1="566" y1="72" x2="582" y2="72" class="msg" marker-end="url(#pa)"/>')
    for i, (s, c) in enumerate([("✓ no middleman can freeze or lose it", "grn"), ("✗ lose the 24 words: coins gone for ever", "red"),
                                ("✗ send to a wrong address: no reversal", "red"), ("~1 in 5 bitcoins thought lost (Chainalysis)", "b")]):
        o.append(T(14, 118 + i * 16, s, c))
    for i, (s, c) in enumerate([("✓ forgot password? customer care resets it", "grn"), ("✓ buy with UPI; easy for beginners", "grn"),
                                ("✗ exchange hacked or frozen: you wait", "red"), ("WazirX, July 2024: ~$230 mn taken", "b")]):
        o.append(T(360, 118 + i * 16, s, c))
    o.append("</g>")
    return svg(186, o)
FIGS["custody"] = custody()

FIGS["escrow"] = seq(
    [("Client", "Dubai", "merchant"), ("Escrow contract", "code on the chain", "app"), ("Nisha", "designer, Kochi", "user"),
     ("Arbitrator", "agreed in advance", "partner")],
    [(0, 1, "lock 500 dollar-tokens", "money"),
     (1, 2, "funds locked: start work", "msg"),
     (2, 0, "logo delivered (outside the chain)", "msg"),
     (0, 1, "“approve”: or silence for 14 days", "msg"),
     (1, 2, "500 tokens released", "money"),
     (0, 1, "or: “dispute”", "msg"),
     (1, 3, "wait for the arbitrator’s signed ruling", "msg"),
     (3, 1, "ruling: pay Nisha 400, refund 100", "ret")],
    note="The contract holds the money fairly, but it can’t judge the logo: that still needs a person.")


def bctree():
    o = [MK, '<g class="c">']
    qs = [("1 · Several parties", "must share one", "record?"), ("2 · Many of them", "write to it, not", "only read?"),
          ("3 · They distrust", "each other and any", "one keeper?"), ("4 · No trusted keeper", "is acceptable", "(a bank, the RBI)?"),
          ("5 · Data can be", "shared; slow and", "costly is fine?")]
    outs = ["Your own database", "One writer: database", "Shared database", "Use the keeper", "Database + signatures"]
    for i in range(5):
        x = 4 + i * 136
        o.append(box(x, 8, 124, 58, *B, [(qs[i][0], "b"), (qs[i][1], ""), (qs[i][2], "")], lh=15))
        o.append(f'<line x1="{x + 62}" y1="66" x2="{x + 62}" y2="92" class="ln" marker-end="url(#pa)"/>')
        o.append(T(x + 68, 83, "no", "b red"))
        o.append(box(x, 96, 124, 30, *GR, [(outs[i], "")]))
        if i < 4:
            o.append(f'<line x1="{x + 124}" y1="37" x2="{x + 134}" y2="37" class="ln" marker-end="url(#pa)"/>')
    o.append(box(460, 142, 216, 32, *G, [("All five yes: a blockchain may fit", "b")]))
    o.append(T(4, 150, "Each arrow to the right means “yes”.", "s"))
    o.append(T(4, 166, "Most proposals exit at question 2 or 3.", "b acc"))
    o.append("</g>")
    return svg(180, o)
FIGS["bctree"] = bctree()
