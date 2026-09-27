"""Technology figures for M7 (LLMs, evals, guardrails); imported at the end of m7_figs.py."""
from m7_figs import FIGS, svg, T, lines, hbars, loop, seq  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R, P, I  # noqa: F401


def chips(y, words, col, fill):
    o = []; x = 150
    for w in words:
        wd = max(18, 7.2 * len(w) + 10)
        o.append(f'<rect x="{x:.1f}" y="{y}" width="{wd:.1f}" height="22" rx="4" fill="{fill}" stroke="{col}"/>')
        o.append(T(x + wd / 2, y + 15, w, "", "middle"))
        x += wd + 4
    return "".join(o), x


def tokens():
    en = ["Drink", " eight", " glasses", " of", " water", " every", " day", "."]
    hi_old = ["ह", "र", " द", "िन", " आ", "ठ", " ग", "िल", "ास", " प", "ान", "ी", " प", "िए", "ँ"]
    hi_new = ["हर", " दिन", " आठ", " गिलास", " पानी", " पिएँ"]
    o = [T(0, 12, "The same advice, cut into tokens (illustrative; every model cuts text differently)", "b")]
    for i, (lab, sub, ws, col, fill) in enumerate([("English", "", en, "#0b5d7a", "#e3f0f5"),
                                                  ("Hindi,", "older tokeniser", hi_old, "#b93a32", "#fcecea"),
                                                  ("Hindi,", "built for Indian scripts", hi_new, "#127a64", "#e1f2ec")]):
        y = 24 + i * 36
        o.append(T(140, y + 11, lab, "b", "end")); o.append(T(140, y + 24, sub, "s", "end"))
        s, x = chips(y, ws, col, fill); o.append(s)
        o.append(T(x + 6, y + 15, f"{len(ws)} tokens", "b", fill=col))
    o.append(T(0, 134, "More tokens means a slower, costlier answer and less room in the model’s memory. Same meaning, 15 tokens against 6.", "b acc"))
    return svg(142, o)
FIGS["tokens"] = tokens()


def costchain():
    o = [MK, '<g class="c">']
    chain = [("6,000 tokens in", "six reports,", "typed up"), ("+ 400 out", "the one-page", "brief"), ("≈ ₹2", "a patient, at", "illustrative prices"),
             ("× 1,250 patients", "50 a day ×", "25 days"), ("≈ ₹2,500", "a month; the clinic", "pays ₹2,000")]
    w = 124
    for i, (a, b, c) in enumerate(chain):
        x = 4 + i * 136
        st = R if i == 4 else B
        o.append(box(x, 26, w, 64, *st, [(a, "b"), (b, ""), (c, "")]))
        if i < 4: o.append(f'<line x1="{x + w + 1}" y1="58" x2="{x + 134}" y2="58" class="ln" marker-end="url(#pa)"/>')
    o.append(T(4, 14, "Price used: ₹250 per million tokens read, ₹1,250 per million written (illustrative, near 2026 prices for a large model)", "s"))
    o.append(T(4, 112, "Fix: send only reports that are new since the last visit (2,000 tokens, not 6,000) and use a smaller model for typing up.", "b grn"))
    o.append(T(4, 127, "Cost falls to about ₹0.60 a patient, ₹750 a month: now the product can make money at ₹2,000.", "b grn"))
    o.append("</g>")
    return svg(136, o)
FIGS["costchain"] = costchain()


FIGS["nextword"] = hbars([("water", 86, "the pattern it has seen most often"), ("milk", 5, "plausible"), ("juice", 3, ""),
                          ("fluids", 2, ""), ("wine", 0.5, "rare in health advice, never exactly zero")], 100, lw=90, unit="%", fmt="{:g}",
                         colors=["#127a64", "#0b5d7a", "#0b5d7a", "#0b5d7a", "#b93a32"],
                         note="What comes next after “Drink eight glasses of …”? The model’s chances for each word (illustrative)")


def attention():
    words = ["The", "tablet", "didn’t", "fit", "in", "the", "box", "because", "it", "was", "too"]
    o = []
    for r, (last, target, col, wt) in enumerate([("big.", 1, "#127a64", "“it” = the tablet"), ("small.", 6, "#c47f17", "“it” = the box")]):
        y0 = 70 + r * 86
        xs = []; x = 10
        for w in words + [last]:
            wd = 7.0 * len(w) + 12
            xs.append(x + wd / 2)
            hl = w in (last, "it") or words.index(w) == target if w in words else True
            o.append(T(x + wd / 2, y0, w, "b" if hl else "", "middle"))
            x += wd + 6
        xi = xs[8]
        for j, strength in [(target, 3.6), (11, 2.6), (6 if target == 1 else 1, 0.8), (3, 0.8)]:
            xj = xs[j]; mid = (xi + xj) / 2; hgt = 18 + abs(xi - xj) * 0.12
            o.append(f'<path d="M{xi:.1f},{y0 - 14} Q{mid:.1f},{y0 - 14 - hgt:.1f} {xj:.1f},{y0 - 14}" fill="none" stroke="{col}" stroke-width="{strength}" opacity="{0.35 + 0.18 * strength:.2f}"/>')
        o.append(T(676, y0, wt, "b", "end", fill=col))
    o.append(T(0, 14, "Attention: when the model reads “it”, it weighs every other word. Thicker line = more weight (illustrative).", "b"))
    o.append(T(0, 184, "One word at the end changes what “it” means, and attention is how the model notices.", "b acc"))
    return svg(192, o)
FIGS["attention"] = attention()


def stages():
    o = [MK, '<g class="c">']
    st = [("1 · Pre-training", ["reads a huge share of", "public text and code;", "learns to predict", "the next token"], "a medical student", "reading the whole library", B),
          ("2 · Instruction tuning", ["trained on examples of", "good answers to", "requests, so it answers", "instead of rambling"], "an intern working", "through solved cases", I),
          ("3 · Feedback from people", ["people rank answers;", "the model is rewarded", "for helpful, honest,", "safe ones"], "senior doctors", "correcting the intern", G)]
    for i, (h, ls, a1, a2, (fill, stc)) in enumerate(st):
        x = 4 + i * 228
        o.append(f'<rect x="{x}" y="8" width="212" height="112" rx="6" fill="{fill}" stroke="{stc}" stroke-width="1.4"/>')
        o.append(T(x + 106, 28, h, "b", "middle"))
        for j, l in enumerate(ls): o.append(T(x + 106, 46 + j * 14, l, "", "middle"))
        o.append(T(x + 106, 140, a1, "b amb", "middle")); o.append(T(x + 106, 154, a2, "amb", "middle"))
        if i < 2: o.append(f'<line x1="{x + 213}" y1="64" x2="{x + 226}" y2="64" class="ln" marker-end="url(#pa)"/>')
    o.append(T(4, 178, "Its knowledge stops at a training cut-off date. It doesn’t know your clinic’s rules", "b acc"))
    o.append(T(4, 192, "or yesterday’s report unless you put them in the prompt.", "b acc"))
    o.append("</g>")
    return svg(200, o)
FIGS["stages"] = stages()


def tempdial():
    o = [T(0, 12, "Prompt: “Write a one-line reminder for Neha to drink water.” Three runs at three settings (illustrative)", "b")]
    rows = [("0", "very steady", "“Time for a glass of water, Neha.” · “Time for a glass of water, Neha.”", "#0b5d7a"),
            ("0.7", "varied, sensible", "“Neha, your 3 pm water break!” · “A glass of water now keeps the slump away.”", "#127a64"),
            ("1.5", "loose, drifting", "“Hydration is the river of focus, Neha.” · “Drink water like the monsoon: eight skies a day.”", "#b93a32")]
    for i, (t, d, s, col) in enumerate(rows):
        y = 26 + i * 40
        o.append(f'<rect x="0" y="{y}" width="120" height="32" rx="5" fill="#f5f6f8" stroke="{col}" stroke-width="1.4"/>')
        o.append(T(60, y + 14, f"temperature {t}", "b", "middle", fill=col)); o.append(T(60, y + 27, d, "s", "middle"))
        o.append(T(132, y + 21, s, ""))
    o.append(T(0, 152, "Low for summaries and anything medical: the same input should give the same output.", "b acc"))
    o.append(T(0, 166, "Higher for friendly nudges that shouldn’t repeat word for word every day.", "b acc"))
    return svg(174, o)
FIGS["tempdial"] = tempdial()


def desk():
    o = [T(0, 12, "A context window of 2,00,000 tokens (about 300 pages), filled for one patient (illustrative)", "b")]
    parts = [("Instructions", 3, "#3e4fb8"), ("Clinic rules", 2, "#7c3aa6"), ("Six reports", 6, "#0b5d7a"), ("Chat so far", 2, "#c47f17"), ("Answer", 1, "#127a64"), ("empty", 86, "#eef0f2")]
    x = 0
    for name, pct, col in parts:
        w = 680 * pct / 100
        o.append(f'<rect x="{x:.1f}" y="22" width="{w:.1f}" height="26" fill="{col}"/>')
        x += w
    o.append(T(4, 64, "instructions · rules · reports · chat · answer: 14% of the window", "s"))
    o.append(T(676, 40, "room left: but more isn’t better", "s", "end"))
    # lost in the middle curve
    L, Rr, Tp, Bt = 60, 400, 84, 170
    xs = [0, 0.1, 0.25, 0.5, 0.75, 0.9, 1]; ys = [0.92, 0.84, 0.72, 0.62, 0.70, 0.82, 0.90]
    X = lambda a: L + (Rr - L) * a; Y = lambda v: Bt - (Bt - Tp) * (v - 0.5) / 0.5
    o.append(f'<line x1="{L}" y1="{Bt}" x2="{Rr}" y2="{Bt}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{Bt}" stroke="#4a5563"/>')
    d = " ".join(f"{'M' if i == 0 else 'L'}{X(a):.1f},{Y(v):.1f}" for i, (a, v) in enumerate(zip(xs, ys)))
    o.append(f'<path d="{d}" fill="none" stroke="#b93a32" stroke-width="2.6"/>')
    o.append(T(L, Bt + 15, "fact at the start", "s")); o.append(T(Rr, Bt + 15, "at the end", "s", "end")); o.append(T((L + Rr) / 2, Bt + 15, "in the middle", "s", "middle"))
    o.append(f'<text x="30" y="{(Tp + Bt) / 2:.1f}" text-anchor="middle" class="s" transform="rotate(-90 30 {(Tp + Bt) / 2:.1f})">found</text>')
    o.append(T(420, 100, "Lost in the middle:", "b red"))
    o.append(T(420, 115, "facts buried in the middle of a long", ""))
    o.append(T(420, 130, "prompt are found less often than facts", ""))
    o.append(T(420, 145, "at the start or end (Liu et al., 2023).", ""))
    o.append(T(420, 164, "Send what matters, near the top.", "b acc"))
    return svg(194, o)
FIGS["desk"] = desk()


def halluc():
    o = [MK, '<g class="c">']
    o.append(box(4, 10, 200, 70, *GR, [("The question", "b"), ("“What dose of metformin", ""), ("is usual for a teenager?”", "")]))
    o.append(box(240, 10, 200, 70, *R, [("The fluent answer", "b red"), ("“The standard dose is", ""), ("1,500 mg at bedtime.”", "")]))
    o.append(box(476, 10, 200, 70, *A, [("Why it happens", "b"), ("it writes what sounds likely;", ""), ("nothing checks a source", "s")]))
    o.append('<line x1="204" y1="45" x2="236" y2="45" class="ln" marker-end="url(#pa)"/><line x1="440" y1="45" x2="472" y2="45" class="ln" marker-end="url(#pa)"/>')
    fixes = [("Ground it", "answer only from a", "trusted drug reference"), ("Cite it", "show the source line", "beside the number"),
             ("Refuse it", "doses are never the", "assistant’s job here"), ("Test it", "a set of dose questions", "in every eval run")]
    for i, (a, b, c) in enumerate(fixes):
        x = 4 + i * 170
        o.append(box(x, 104, 160, 58, *G, [(a, "b grn"), (b, ""), (c, "")]))
    o.append(T(4, 96, "What a product team does about it:", "b"))
    o.append("</g>")
    return svg(168, o)
FIGS["halluc"] = halluc()


# ---------- evals ----------
FIGS["evalloop"] = loop(["Collect real cases|60 folders, anonymised", "Write what good is|facts a doctor needs", "Change something|prompt, model, reader",
                         "Run every case|score with the rubric", "Gate the release|no category may fall", "Watch live use|edits, misses, audits"],
                        "The eval loop|every miss becomes a test", bw=160, h=236)


def agree():
    o = [T(0, 12, "100 briefs graded twice: by a doctor and by an AI judge using the same rubric (illustrative)", "b")]
    x0, y0, cw, ch = 150, 40, 150, 50
    o.append(T(x0 + cw, y0 - 8, "Doctor says", "b", "middle"))
    o.append(T(x0 + cw / 2, y0 + 8, "pass", "s", "middle")); o.append(T(x0 + 1.5 * cw, y0 + 8, "fail", "s", "middle"))
    o.append(T(x0 - 70, y0 + 20 + ch, "AI judge says", "b", "middle"))
    o.append(T(x0 - 10, y0 + 12 + ch / 2 + 4, "pass", "s", "end")); o.append(T(x0 - 10, y0 + 12 + 1.5 * ch + 4, "fail", "s", "end"))
    cells = [(0, 0, "72", "agree", "#e1f2ec", "#127a64"), (1, 0, "9", "judge too kind", "#fcecea", "#b93a32"),
             (0, 1, "3", "judge too strict", "#fbf4e6", "#c47f17"), (1, 1, "16", "agree", "#e1f2ec", "#127a64")]
    for cx, cy, n, lab, fill, st in cells:
        x = x0 + cx * cw; y = y0 + 12 + cy * ch
        o.append(f'<rect x="{x}" y="{y}" width="{cw - 4}" height="{ch - 4}" rx="5" fill="{fill}" stroke="{st}" stroke-width="1.4"/>')
        o.append(T(x + cw / 2 - 2, y + 22, n, "b t13", "middle", fill=st)); o.append(T(x + cw / 2 - 2, y + 37, lab, "s", "middle"))
    o.append(T(466, 60, "Agreement: 72 + 16 = 88 of 100.", "b"))
    o.append(T(466, 78, "The 9 matter most: the judge", ""))
    o.append(T(466, 92, "passed briefs with a wrong", ""))
    o.append(T(466, 106, "decimal (1.6 read as 16).", ""))
    o.append(T(466, 124, "Fix: a code check that every", "b grn"))
    o.append(T(466, 138, "number matches its source.", "b grn"))
    return svg(160, o)
FIGS["agree"] = agree()


def offon():
    o = []
    for x, h, (fill, st), rows in [(0, "Offline: before release", B, ["the 60-folder golden set", "+ the red-team set", "graded by rubric, judge, code checks",
                                                                    "fast, repeatable, safe", "misses what real clinics do"]),
                                   (346, "Online: after release", G, ["doctors’ edits: 8% of briefs", "“open the source” taps", "minutes saved per patient",
                                                                    "weekly audit: critical misses", "real, but slow and noisy"])]:
        o.append(f'<rect x="{x}" y="4" width="334" height="120" rx="6" fill="{fill}" stroke="{st}" stroke-width="1.4"/>')
        o.append(T(x + 14, 24, h, "b", fill=st))
        for i, r in enumerate(rows): o.append(T(x + 14, 44 + i * 16, ("✓ " if i < 3 else ("+ " if i == 3 else "− ")) + r, "b" if i == 4 else ""))
    o.append(T(0, 142, "Every doctor’s edit online is a candidate test case offline: that is how the golden set grows.", "b acc"))
    return svg(150, o)
FIGS["offon"] = offon()


# ---------- guardrails ----------
def layers():
    o = [MK, '<g class="c">']
    steps = [("Her message", "“Can I stop my", "metformin?”", GR), ("① Input check", "topic: changing a", "medicine: high risk", A), ("② Ground it", "her own records:", "on metformin", B),
             ("③ The model", "with a rule: never", "advise on stopping", I), ("④ Output check", "scan for “stop”,", "doses, diagnoses", A), ("⑤ Hand-off", "offer: message", "her doctor", G)]
    w = 104
    for i, (a, b, c, st) in enumerate(steps):
        x = 2 + i * 113
        o.append(box(x, 10, w, 66, *st, [(a, "b"), (b, ""), (c, "")]))
        if i < 5: o.append(f'<line x1="{x + w + 1}" y1="43" x2="{x + 111}" y2="43" class="ln" marker-end="url(#pa)"/>')
    o.append('<rect x="2" y="90" width="676" height="26" rx="5" fill="#f3f3ee" stroke="#6b6a52"/>')
    o.append(T(340, 107, "⑥ Log every step; a person reviews a sample of high-risk chats each week; rate limits stop floods and probing", "b", "middle"))
    o.append(T(2, 138, "Each layer catches what the one before misses. No single layer is trusted alone, including the model’s own rule.", "b acc"))
    o.append("</g>")
    return svg(146, o)
FIGS["layers"] = layers()


def refusal():
    o = [T(0, 12, "Two ways to fail, measured on two test sets (illustrative)", "b")]
    rows = [("Unsafe answers let through", "on 200 risky questions (stop a medicine, a dose)", 1, "#b93a32", "target: 0"),
            ("Safe questions refused", "on 200 ordinary ones (“Can I eat mango?”)", 14, "#c47f17", "target: under 2%")]
    for i, (a, b, v, col, tgt) in enumerate(rows):
        y = 26 + i * 44
        o.append(T(0, y + 12, a, "b")); o.append(T(0, y + 26, b, "s"))
        w = 10 * v
        o.append(f'<rect x="300" y="{y + 4}" width="{w}" height="20" rx="2" fill="{col}"/>')
        o.append(T(306 + w, y + 18, f"{v} of 200 ({v / 2:g}%) · {tgt}", "b", fill=col))
    o.append(T(0, 124, "Tightening the output check fixed the first row and broke the second: 14 people asked about mangoes and got a lecture.", "b acc"))
    return svg(132, o)
FIGS["refusal"] = refusal()
