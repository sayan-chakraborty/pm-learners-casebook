"""Technology figures for M8 (RAG, agents, MCP, evals, cost and latency); imported at the end of m8_figs.py."""
import math
from m8_figs import FIGS, svg, T, lines, hbars, waterfall, loop, two_by_two, seq, strip  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R, P, I, vbars  # noqa: F401

ARW = '<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#4a5563" stroke-width="1.4" marker-end="url(#pa)"/>'


def arr(x1, y1, x2, y2, col="#4a5563", dash=False):
    d = ' stroke-dasharray="4 3"' if dash else ""
    mk = "pr" if col == "#b93a32" else ("pg" if col == "#127a64" else "pa")
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="1.5"{d} marker-end="url(#{mk})"/>'


# ================= A. RAG =================
def rag():
    o = [MK]
    o.append(f'<rect x="0" y="20" width="680" height="84" rx="8" fill="#f6f7f9" stroke="#c3cad2"/>')
    o.append(T(8, 14, "Before any question: prepare the library (runs when documents change)", "b acc"))
    steps1 = [("① Collect", "articles, policies,", "resolved tickets"), ("② Clean", "remove menus,", "old versions"), ("③ Chunk", "cut into pieces", "of ~250 words"),
              ("④ Embed", "each piece → a", "list of numbers"), ("⑤ Index", "store for fast", "search + filters")]
    for i, (a, b, c) in enumerate(steps1):
        x = 10 + i * 134
        o.append(box(x, 32, 118, 62, *B, [(a, "b"), (b, "s"), (c, "s")]))
        if i < 4: o.append(arr(x + 118, 63, x + 132, 63))
    o.append(f'<rect x="0" y="130" width="680" height="84" rx="8" fill="#f3f9f6" stroke="#b9d8cd"/>')
    o.append(T(8, 124, "For every question (runs in about a second)", "b grn"))
    steps2 = [("⑥ Question", "“Refund on my", "annual plan?”", G), ("⑦ Search", "meaning + keywords;", "top 20 pieces", B), ("⑧ Re-rank", "keep the best 5", "", B),
              ("⑨ Grounded prompt", "5 pieces + “answer", "only from these”", I), ("⑩ Answer", "with sources;", "or “not found”", G)]
    for i, (a, b, c, col) in enumerate(steps2):
        x = 10 + i * 134
        rows = [(a, "b"), (b, "s")] + ([(c, "s")] if c else [])
        o.append(box(x, 142, 118, 62, *col, rows))
        if i < 4: o.append(arr(x + 118, 173, x + 132, 173))
    o.append('<path d="M620,94 C620,114 330,112 330,138" fill="none" stroke="#0b5d7a" stroke-width="1.4" stroke-dasharray="4 3" marker-end="url(#pa)"/>')
    o.append(T(470, 118, "the index is what ⑦ searches", "s halo", "middle"))
    return svg(218, o)
FIGS["rag"] = rag()


def chunk():
    o = [T(0, 12, "One refund policy, 3,000 words, cut three ways. The question: “Refund if I cancel my annual plan after 10 days?”", "s")]
    cols = [("Too small: 50 words", R, ["“Refunds are possible", "within 14 days.”", "", "The condition “for annual", "plans only” sits in the", "next piece: lost."], "matches, but the answer is incomplete"),
            ("About right: 250 words", G, ["“Annual plans: full refund", "within 14 days of purchase.", "After that, no refund; the", "plan runs to the end of", "the term.” Overlap of 50", "words keeps sentences whole."], "12 pieces; the whole rule in one"),
            ("Too big: whole policy", A, ["All 3,000 words in", "one piece: refunds, GST,", "upgrades, payment failures.", "", "Matches everything a", "little, nothing well."], "weak match; costs 12× the words")]
    for i, (h, (fill, st), ls, note) in enumerate(cols):
        x = i * 230
        o.append(f'<rect x="{x}" y="24" width="216" height="126" rx="6" fill="{fill}" stroke="{st}" stroke-width="1.4"/>')
        o.append(T(x + 10, 42, h, "b"))
        for j, l in enumerate(ls): o.append(T(x + 10, 60 + j * 13, l, "s"))
        o.append(T(x + 108, 168, note, "b", "middle", fill=st))
    return svg(176, o)
FIGS["chunk"] = chunk()


def simmap():
    cx, cy, Rr = 40, 196, 190
    o = ['<defs><marker id="sm" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#4a5563"/></marker></defs>']
    o.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + Rr + 20}" y2="{cy}" stroke="#c3cad2"/><line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - Rr - 10}" stroke="#c3cad2"/>')
    pts = [("Question: refund, annual plan", 50, "#127a64", "b", -4), ("Refunds on annual plans", 43, "#0b5d7a", "", 10), ("Cancelling a monthly plan", 29, "#0b5d7a", "", 4),
           ("Upgrades and GST", 14, "#0b5d7a", "", 4), ("Resetting your password", 68, "#9aa3ad", "", 4)]
    for lab, ang, col, cls, dy in pts:
        a = math.radians(ang); x2 = cx + Rr * math.cos(a); y2 = cy - Rr * math.sin(a)
        w = 2.6 if cls else 1.6
        o.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}" marker-end="url(#sm)"/>')
        o.append(T(x2 + 6, y2 + dy, lab, ("b " if cls else "") + "halo", "start", fill=col))
    o.append(f'<path d="M{cx + 60 * math.cos(math.radians(50)):.1f},{cy - 60 * math.sin(math.radians(50)):.1f} A60,60 0 0 1 {cx + 60 * math.cos(math.radians(43)):.1f},{cy - 60 * math.sin(math.radians(43)):.1f}" fill="none" stroke="#c47f17" stroke-width="2"/>')
    o.append(T(cx - 6, cy + 16, "each arrow: a text turned into numbers (2 of ~1,000 directions shown)", "s"))
    rows = [("Refunds on annual plans", "0.86", "#127a64"), ("Cancelling a monthly plan", "0.71", "#0b5d7a"), ("Upgrades and GST", "0.52", "#0b5d7a"),
            ("Resetting your password", "0.12", "#9aa3ad"), ("Office holidays", "0.05", "#9aa3ad")]
    x0 = 450
    o.append(T(x0, 30, "Similarity to the question", "b")); o.append(T(x0, 44, "(small angle = close meaning = high score)", "s"))
    for i, (lab, v, col) in enumerate(rows):
        y = 64 + i * 22
        o.append(T(x0, y, lab, "", fill=col)); o.append(T(676, y, v, "b", "end", fill=col))
    o.append(T(x0, 186, "Top matches go to the model; the", "s")); o.append(T(x0, 199, "password page never does.", "s"))
    return svg(218, o)
FIGS["simmap"] = simmap()

FIGS["hybrid"] = hbars([("Meaning search only", 74, "misses codes like “GSTIN” and “ERR-4012”"), ("Keyword search only", 61, "misses rephrased questions"),
                        ("Both (hybrid)", 80, "each catches what the other misses"), ("Hybrid + re-ranker", 86, "the best 5 of 20 reordered by a second model")],
                       100, lw=150, unit="%", colors=["#0b5d7a", "#9aa3ad", "#3e4fb8", "#127a64"],
                       note="Right article in the top 5, out of 200 real test questions (illustrative)")


def fresh():
    o = [MK, T(0, 12, "Freshness: a policy changes; how long does the copilot keep quoting the old one?", "b")]
    o.append(box(0, 24, 150, 50, *A, [("1 Sep: refund window", "b"), ("changed 7 → 14 days", "s")]))
    o.append(box(200, 24, 200, 50, *R, [("Weekly re-index: until 7 Sep", "b red"), ("copilot still says 7 days", "s")]))
    o.append(box(450, 24, 230, 50, *G, [("Re-index on publish", "b grn"), ("new answer within 10 minutes", "s")]))
    o.append(arr(150, 49, 196, 49)); o.append(arr(400, 49, 446, 49, "#127a64"))
    o.append(T(300, 90, "6 days × 30 refund tickets a day = about 180 wrong answers", "b red", "middle"))
    o.append(T(0, 120, "Permissions: filter before the model sees anything", "b"))
    o.append(box(0, 132, 150, 52, *G, [("Agent asks about", "b"), ("customer C-2291", "s")]))
    o.append(box(200, 132, 200, 52, *B, [("Search with a filter", "b"), ("customer = C-2291; role = agent", "s")]))
    o.append(box(450, 132, 230, 52, *GR, [("Other customers’ tickets", "b"), ("and internal-only notes excluded", "s")]))
    o.append(arr(150, 158, 196, 158)); o.append(arr(400, 158, 446, 158))
    o.append(T(0, 204, "A line in the prompt such as “don’t reveal other customers’ data” is not a lock; the filter is.", "s"))
    return svg(212, o)
FIGS["fresh"] = fresh()


def ragfail():
    cards = [("Wrong piece found", "The question says “annual”;", "search returns the monthly", "plan’s rule.", "Fix: hybrid search, re-rank,", "a filter on plan type", R),
             ("Right piece, out of date", "The article was changed on", "1 Sep; the index still has", "the old 7-day window.", "Fix: re-index on publish;", "show the article’s date", A),
             ("Sources disagree", "The policy says 14 days; an", "old ticket reply said 7.", "The model picks one.", "Fix: rank official policy", "above past tickets", P),
             ("Answer spread out", "Refund amount needs the", "pro-rata rule, the GST rule", "and the processing time.", "Fix: bigger pieces or more", "of them; test such questions", B)]
    o = [T(0, 12, "Four ways a RAG answer goes wrong on the same refund question", "b")]
    for i, (h, a, b, c, f1, f2, (fill, st)) in enumerate(cards):
        x = i * 172
        o.append(f'<rect x="{x}" y="22" width="162" height="128" rx="6" fill="{fill}" stroke="{st}" stroke-width="1.4"/>')
        o.append(T(x + 8, 40, h, "b"))
        for j, l in enumerate((a, b, c)): o.append(T(x + 8, 58 + j * 13, l, "s"))
        o.append(T(x + 8, 122, f1, "b", fill=st)); o.append(T(x + 8, 136, f2, "s", fill=st))
    return svg(156, o)
FIGS["ragfail"] = ragfail()

# ================= B. Agents =================
FIGS["agentloop"] = loop(["Plan|what’s the next step?", "Pick a tool|and its inputs", "Call it|the app runs it",
                          "Read the result|did it work?", "Decide|go on, ask, or stop"],
                         "An agent|a model in a loop", bw=156, h=236)

FIGS["agenttrace"] = seq(
    [("Customer", "via Priya’s ticket", "merchant"), ("Agent (AI)", "plans each step", "app"), ("Billing system", "tools it may call", "bank"),
     ("Priya", "approves money moves", "user")],
    [(0, 1, "“Upgrade us from Basic to Pro today”", "msg"),
     (1, 2, "get_account(C-2291)", "msg"),
     (2, 1, "Basic, ₹2,000 a month, renews on 30th", "ret"),
     (1, 2, "get_plan_rules(Pro)", "msg"),
     (2, 1, "Pro ₹4,500 a month; upgrades charged pro rata", "ret"),
     (1, 2, "calc_proration(22 of 30 days left)", "msg"),
     (2, 1, "(₹4,500 − ₹2,000) × 22 ÷ 30 = ₹1,833", "ret"),
     (1, 3, "“Charge ₹1,833 and switch to Pro?” [Approve]", "msg"),
     (3, 1, "approved", "ret"),
     (1, 2, "change_plan(C-2291, Pro, today)", "msg"),
     (1, 0, "confirmation email, drafted for Priya to send", "msg")],
    note="Read steps run on their own; the step that moves money waits for a person. Six steps, well under the limit of eight.")


def permladder():
    rows = [("Read", "look up account, plan rules, tickets", "runs alone", G),
            ("Draft", "write a reply or a plan change, not sent", "runs alone; a person sends", B),
            ("Reversible write", "tag a ticket, change a setting that can be undone", "runs alone, logged", A),
            ("Money, deletion, messages out", "refunds, plan changes, emails to customers", "a person approves every time", R),
            ("Never", "change prices, delete accounts, edit another customer", "no tool exists for it", ("#2b2b2b", "#2b2b2b"))]
    o = [T(0, 12, "What an agent may do alone: give it tools by risk, and the fewest it needs (least privilege)", "b")]
    for i, (h, d, rule, (fill, st)) in enumerate(rows):
        y = 22 + i * 34; w = 200 + i * 40
        o.append(f'<rect x="0" y="{y}" width="{w}" height="28" rx="5" fill="{fill}" stroke="{st}" stroke-width="1.3"/>')
        o.append(T(8, y + 18, h, "b w" if i == 4 else "b"))
        o.append(T(w + 10, y + 12, d, "s")); o.append(T(w + 10, y + 25, rule, "b", fill=("#b93a32" if i >= 3 else "#127a64")))
    o.append(T(0, 200, "Every call, allowed or not, goes into an audit log: who asked, which tool, what inputs, what happened.", "s"))
    return svg(206, o)
FIGS["permladder"] = permladder()


def retry():
    o = [MK, T(0, 12, "One ticket, two runs. Each model call costs about ₹2 (illustrative).", "b")]
    o.append(T(0, 38, "Normal run", "b grn"))
    for i in range(3):
        o.append(f'<rect x="{110 + i * 38}" y="26" width="32" height="18" rx="3" fill="#127a64"/>')
    o.append(T(230, 40, "3 calls = ₹6, answer in 4 seconds", "b grn"))
    o.append(T(0, 76, "Stuck in a loop", "b red"))
    for i in range(45):
        x = 110 + (i % 15) * 38; y = 64 + (i // 15) * 22
        o.append(f'<rect x="{x}" y="{y}" width="32" height="18" rx="3" fill="#b93a32"/>')
    o.append(T(110, 146, "billing tool times out; the agent retries the same call 15 times, re-reading the whole history each time:", "s"))
    o.append(T(110, 160, "45 calls = ₹90 for one ticket, and still no answer. Fix: at most 8 steps, 2 retries, then hand to a person.", "b red"))
    return svg(168, o)
FIGS["retry"] = retry()

# ================= C. MCP =================
def mcp():
    o = [MK]
    o.append(f'<rect x="0" y="10" width="220" height="200" rx="8" fill="#e3f0f5" stroke="#0b5d7a" stroke-width="1.4"/>')
    o.append(T(110, 30, "Host: the AI app", "b", "middle")); o.append(T(110, 44, "the support copilot, a desktop", "s", "middle")); o.append(T(110, 57, "assistant, an IDE", "s", "middle"))
    for i, nm in enumerate(["client for help desk", "client for Jira", "client for Google Drive"]):
        o.append(box(20, 72 + i * 44, 180, 34, *G, [(nm, "")]))
    servers = [("MCP server: help desk", "tools: get_ticket, add_note", A), ("MCP server: Jira", "tools: create_issue, search", A),
               ("MCP server: Drive", "resources: files you may open", A)]
    for i, (h, d, col) in enumerate(servers):
        y = 64 + i * 50
        o.append(box(330, y, 190, 42, *col, [(h, "b"), (d, "s")]))
        o.append(f'<line x1="200" y1="{89 + i * 44}" x2="326" y2="{85 + i * 50}" stroke="#4a5563" stroke-width="1.4" stroke-dasharray="4 3"/>')
        o.append(box(580, y + 4, 100, 34, *GR, [(["Freshdesk", "Jira", "Drive"][i], "b")]))
        o.append(f'<line x1="520" y1="{y + 21}" x2="578" y2="{y + 21}" stroke="#4a5563" stroke-width="1.2"/>')
    o.append(T(263, 50, "one standard", "b halo", "middle")); o.append(T(263, 63, "“language” (MCP)", "s halo", "middle"))
    o.append(T(550, 50, "each service’s own API", "s", "middle"))
    o.append(T(0, 232, "A server offers tools (actions), resources (data to read) and prompts (ready-made instructions). Any MCP host can use any MCP server.", "s"))
    return svg(240, o)
FIGS["mcp"] = mcp()


def mcpmath():
    o = [T(0, 12, "Without a standard", "b red"), T(350, 12, "With MCP", "b grn")]
    apps = [30 + i * 30 for i in range(5)]; tools = [22 + i * 7.6 for i in range(20)]
    for y in apps:
        o.append(f'<rect x="0" y="{y - 8}" width="50" height="16" rx="3" fill="#e3f0f5" stroke="#0b5d7a"/>')
        for ty in tools: o.append(f'<line x1="50" y1="{y}" x2="250" y2="{ty + 4}" stroke="#b93a32" stroke-width="0.5" opacity="0.6"/>')
    for ty in tools: o.append(f'<rect x="250" y="{ty}" width="40" height="6" rx="1" fill="#fde7c8" stroke="#c47f17" stroke-width="0.6"/>')
    o.append(T(0, 188, "5 AI apps × 20 tools = 100 connectors to build", "b red"))
    o.append(T(0, 202, "and keep working when any of them changes", "s"))
    for y in apps:
        o.append(f'<rect x="350" y="{y - 8}" width="50" height="16" rx="3" fill="#e3f0f5" stroke="#0b5d7a"/>')
        o.append(f'<line x1="400" y1="{y}" x2="470" y2="{y}" stroke="#127a64" stroke-width="1.2"/>')
    o.append(f'<rect x="470" y="20" width="14" height="150" rx="3" fill="#127a64"/>')
    o.append(T(477, 14, "MCP", "b grn", "middle"))
    for ty in tools:
        o.append(f'<line x1="484" y1="{ty + 3}" x2="600" y2="{ty + 3}" stroke="#127a64" stroke-width="0.8"/>')
        o.append(f'<rect x="600" y="{ty}" width="40" height="6" rx="1" fill="#fde7c8" stroke="#c47f17" stroke-width="0.6"/>')
    o.append(T(350, 188, "5 clients + 20 servers = 25 pieces", "b grn"))
    o.append(T(350, 202, "each tool maker builds one server, once", "s"))
    return svg(210, o)
FIGS["mcpmath"] = mcpmath()

FIGS["mcptrace"] = seq(
    [("Priya", "support agent", "user"), ("Copilot (host)", "AI + MCP clients", "app"), ("Help-desk server", "MCP", "partner"),
     ("Jira server", "MCP", "partner"), ("Engineering", "sees the bug", "merchant")],
    [(0, 1, "“Summarise ticket #4821 and file a bug”", "msg"),
     (1, 2, "which tools do you offer? → get_ticket, add_note", "msg"),
     (1, 2, "get_ticket(4821)", "msg"),
     (2, 1, "ticket text + 6 replies + error log", "ret"),
     (1, 1, "summary: export fails above 10,000 rows", "self"),
     (1, 0, "“File in project BILL, priority high?” [Approve]", "msg"),
     (0, 1, "approve", "msg"),
     (1, 3, "create_issue(BILL, “CSV export fails >10k rows”, high)", "msg"),
     (3, 1, "BILL-912 created", "ret"),
     (1, 2, "add_note(4821, “Filed as BILL-912”)", "msg"),
     (3, 4, "new high-priority bug in the queue", "msg")],
    note="The copilot’s makers never wrote code for Jira; they connected Jira’s MCP server. Creating the issue still waits for Priya.")

# ================= D. Evals =================
FIGS["evalsplit"] = hbars([("Retrieval: wrong piece", 17, "the right article wasn’t in the top 5"), ("Generation: added or changed facts", 7, "right article, wrong answer"),
                           ("Stale source", 4, "right article, out of date")], 20, lw=210,
                          colors=["#b93a32", "#7c3aa6", "#c47f17"], note="200 labelled tickets; 172 answers correct, 28 wrong. Why the 28 failed:")

FIGS["failbuckets"] = hbars([("Accuracy", 34, "wrong or made-up answer"), ("Capability", 27, "asked for something it can’t do"),
                             ("Flow", 18, "loops, asks the same thing twice"), ("Hand-off", 13, "couldn’t reach a person"),
                             ("Tone", 8, "curt, robotic, or over-apologetic")], 40, lw=110, unit="%",
                            colors=["#b93a32", "#c47f17", "#3e4fb8", "#7c3aa6", "#9aa3ad"],
                            note="300 abandoned chat conversations, read and labelled by hand (illustrative)")

# ================= E. Cost and latency =================
def costchain():
    o = [T(0, 12, "What one ticket really costs: attempts, failures and hand-offs (illustrative)", "b")]
    steps = [("₹2", "per model call"), ("× 3 calls", "= ₹6 an attempt"), ("÷ 60% solved", "= ₹10 per solved ticket"),
             ("+ 40% to a person", "× ₹40 = ₹16"), ("= ₹22 a ticket", "vs ₹40 all-human")]
    w = 124
    for i, (a, b) in enumerate(steps):
        x = i * (w + 15)
        col = G if i == 4 else B
        o.append(box(x, 24, w, 52, *col, [(a, "b grn" if i == 4 else "b"), (b, "s")]))
        if i < 4: o.append(f'<line x1="{x + w + 1}" y1="50" x2="{x + w + 13}" y2="50" stroke="#4a5563" stroke-width="1.4"/>')
    o.append(T(0, 98, "Cost per attempt looks like ₹6; cost per solved ticket is ₹10; the real saving per ticket is ₹40 − ₹22 = ₹18.", "s"))
    return svg(106, o)
FIGS["costchain"] = costchain()


def latency():
    L, Rr, Tp, Bt = 40, 640, 20, 150
    X = lambda s: L + (Rr - L) * s / 8
    bins = [0, 3, 9, 16, 14, 10, 7, 5, 4, 3, 3, 2, 2, 2, 1.5, 1.2, 1, 1, 0.8, 0.6, 0.5, 0.4, 0.3, 0.2]
    step = 8 / len(bins); mx = max(bins)
    o = [f'<line x1="{L}" y1="{Bt}" x2="{Rr}" y2="{Bt}" stroke="#4a5563"/>']
    for i, v in enumerate(bins):
        h = (Bt - Tp - 14) * v / mx
        o.append(f'<rect x="{X(i * step) + 1:.1f}" y="{Bt - h:.1f}" width="{X(step) - L - 2:.1f}" height="{h:.1f}" fill="#9fc3d1"/>')
    for s in range(9): o.append(T(X(s), Bt + 14, f"{s} s", "s", "middle"))
    for s, lab, col in ((1.2, "median 1.2 s: half of answers are faster", "#127a64"), (6.0, "p95 6 s: 1 in 20 is slower", "#b93a32")):
        o.append(f'<line x1="{X(s):.1f}" y1="{Tp}" x2="{X(s):.1f}" y2="{Bt}" stroke="{col}" stroke-width="2" stroke-dasharray="5 3"/>')
        o.append(T(X(s) + 6, Tp + 10, lab, "b", fill=col))
    o.append(T(X(3.2), Bt - 52, "long tickets with many replies:", "s")); o.append(T(X(3.2), Bt - 39, "more words to read, slower answers", "s"))
    o.append(T(L, Bt + 30, "Time to a full answer for 1,000 copilot requests (illustrative). An agent handling 60 tickets a day meets the slow tail 3 times a day.", "s"))
    return svg(186, o)
FIGS["latency"] = latency()


def triangle():
    A_, B_, C_ = (170, 20), (20, 250), (320, 250)
    o = [f'<polygon points="{A_[0]},{A_[1]} {B_[0]},{B_[1]} {C_[0]},{C_[1]}" fill="#f6f7f9" stroke="#4a5563" stroke-width="1.6"/>',
         T(170, 12, "Quality", "b", "middle"), T(0, 268, "Speed (low latency)", "b", "start"), T(320, 268, "Low cost", "b", "middle")]
    pts = [("A", 170, 70, "#3e4fb8"), ("B", 250, 222, "#c47f17"), ("C", 190, 150, "#127a64")]
    for lab, x, y, col in pts:
        o.append(f'<circle cx="{x}" cy="{y}" r="11" fill="{col}"/>'); o.append(T(x, y + 4, lab, "b w", "middle"))
    rows = [("A · Large model + re-ranker", "92% correct · 4.5 s · ₹3.00 a ticket", "#3e4fb8", "best answers; slow and dear"),
            ("B · Small model", "81% correct · 0.9 s · ₹0.30 a ticket", "#c47f17", "fast and cheap; too many misses"),
            ("C · Routed: small first, large when unsure", "90% correct · 1.6 s average · ₹1.11", "#127a64", "70% × ₹0.30 + 30% × ₹3.00 = ₹1.11")]
    for i, (h, d, col, n) in enumerate(rows):
        y = 40 + i * 70
        o.append(f'<rect x="360" y="{y - 16}" width="320" height="58" rx="6" fill="#fff" stroke="{col}" stroke-width="1.6"/>')
        o.append(T(370, y, h, "b", fill=col)); o.append(T(370, y + 16, d, "")); o.append(T(370, y + 32, n, "s"))
    return svg(276, o)
FIGS["triangle"] = triangle()


def routing():
    o = [MK]
    o.append(box(0, 60, 120, 50, *G, [("100 tickets", "b"), ("come in", "s")]))
    o.append(box(170, 60, 130, 50, *B, [("Router", "b"), ("easy or hard?", "s")]))
    o.append(box(360, 6, 170, 50, *A, [("Small model: 70", "b"), ("70 × ₹0.30 = ₹21", "s")]))
    o.append(box(360, 114, 170, 50, *P, [("Large model: 30", "b"), ("30 × ₹3.00 = ₹90", "s")]))
    o.append(box(570, 60, 110, 50, *G, [("₹111 per 100", "b grn"), ("= ₹1.11 each", "s")]))
    o.append(arr(120, 85, 166, 85)); o.append(arr(300, 78, 356, 36)); o.append(arr(300, 92, 356, 134))
    o.append(arr(530, 34, 566, 76)); o.append(arr(530, 138, 566, 96))
    o.append('<path d="M445,56 L445,110" stroke="#b93a32" stroke-width="1.4" stroke-dasharray="4 3" marker-end="url(#pr)"/>')
    o.append(T(452, 88, "unsure? pass up", "s red"))
    o.append(T(0, 186, "Easy: password resets, invoice copies, plan questions. Hard: angry customers, several issues, legal words.", "s"))
    o.append(T(0, 200, "Sending all 100 to the large model would cost ₹300.", "b"))
    return svg(206, o)
FIGS["routing"] = routing()
