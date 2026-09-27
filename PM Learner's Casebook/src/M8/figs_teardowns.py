"""Teardown figures for M8; imported at the end of m8_figs.py."""
from m8_figs import FIGS, svg, T, lines, hbars, waterfall, loop, two_by_two, seq, strip  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R, P, I, vbars  # noqa: F401


def ladder(steps, title, h=196):
    """steps: (name, sub, price, colours) rising left to right."""
    n = len(steps); w = (680 - 12 * (n - 1)) / n
    o = [MK, T(0, 12, title, "b")]
    for i, (name, sub, price, (fill, st)) in enumerate(steps):
        x = i * (w + 12); top = 96 - i * 24; hh = h - 16 - top
        o.append(f'<rect x="{x:.1f}" y="{top}" width="{w:.1f}" height="{hh}" rx="6" fill="{fill}" stroke="{st}" stroke-width="1.4"/>')
        o.append(T(x + w / 2, top + 18, name, "b", "middle"))
        for j, l in enumerate(sub.split("|")): o.append(T(x + w / 2, top + 34 + j * 13, l, "s", "middle"))
        o.append(T(x + w / 2, h - 28, price, "b grn", "middle"))
    return svg(h, o)


# ---------- Cloud trio ----------
FIGS["flow_cloud"] = seq(
    [("Shoppers", "Diwali sale, 8 pm", "merchant"), ("Load balancer", "spreads requests", "network"), ("App servers", "scale out and in", "app"),
     ("Managed database", "one writer, 3 readers", "bank"), ("Cloud bill", "per second used", "partner")],
    [(0, 1, "traffic jumps 10× in two minutes", "msg"),
     (1, 2, "requests shared across 10 servers", "msg"),
     (2, 2, "CPU above 70% for 1 min: add 30 servers", "self"),
     (2, 3, "product pages: reads go to the 3 read copies", "msg"),
     (2, 3, "orders: writes go to the one main copy", "msg"),
     (3, 2, "stock and order confirmed", "ret"),
     (2, 0, "page loads in under a second", "ret"),
     (2, 2, "midnight: traffic falls; remove 30 servers", "self"),
     (2, 4, "40 servers × 4 hours, billed by the second", "money")],
    note="The shop pays for 40 servers for four hours, not all year. Renting capacity by the second is the cloud’s core promise.")

FIGS["cloudmoney"] = vbars([("AWS", 42.2, "$42.2 bn"), ("Microsoft|Cloud*", 59.3, "$59.3 bn"), ("Google|Cloud", 24.8, "$24.8 bn")], 60,
                           "Revenue, Apr–Jun 2026", sub="* Microsoft Cloud includes Microsoft 365 and Azure", colors=["#c47f17", "#0b5d7a", "#127a64"], vw=330, h=196)
FIGS["cloudmargin"] = vbars([("AWS", 39, "39%"), ("Google|Cloud", 36, "about 36%")], 50,
                            "Operating margin, same quarter", sub="Microsoft does not report Azure’s margin", colors=["#c47f17", "#127a64"], vw=330, h=196)

# ---------- Amplitude ----------
FIGS["flow_amp"] = seq(
    [("Users", "KYC screen, Android", "user"), ("App + Amplitude SDK", "records events", "app"), ("Amplitude", "stores, counts", "partner"),
     ("Rohan (PM)", "Pune fintech", "user"), ("Experiment", "A/B tests", "partner")],
    [(0, 1, "taps “Upload PAN”, “Take selfie”, “Submit”", "msg"),
     (1, 2, "events sent in batches: name, time, device, user", "msg"),
     (3, 2, "funnel: install → PAN → selfie → submitted, last 30 days", "msg"),
     (2, 3, "selfie step: 71% → 52% since 4 Sep", "ret"),
     (3, 2, "split by device and app version", "msg"),
     (2, 3, "drop only on Android 14, app 6.2", "ret"),
     (3, 4, "test: old camera screen vs new, 50/50", "msg"),
     (4, 3, "old screen wins: +17 points; ship the fix", "ret")],
    note="Tracking plan first: if the team never named the “Take selfie” event, the funnel can’t show where people leave.")

FIGS["ladder_amp"] = ladder([("Starter", "free: events,|basic charts", "₹0", G), ("Plus", "a small team,|more events", "low monthly fee", B),
                             ("Growth", "funnels, cohorts,|more seats", "yearly contract", A),
                             ("Enterprise", "+ experiments, replays,|AI agents, governance", "$100k+ a year (824 firms)", P)],
                            "Amplitude’s ladder: priced mainly on data volume (events or tracked users), then add-on products")

# ---------- ThoughtSpot ----------
FIGS["flow_ts"] = seq(
    [("Anjali", "regional sales head", "user"), ("Spotter", "ThoughtSpot’s AI", "app"), ("Semantic model", "words → columns", "app"),
     ("Data warehouse", "the firm’s data", "bank")],
    [(0, 1, "“Sales by district last quarter vs target, Maharashtra”", "msg"),
     (1, 2, "which columns do these words mean?", "msg"),
     (2, 1, "sales = net_revenue; district = store.district; target table", "ret"),
     (1, 3, "SQL: sum, filter, join targets, group by district", "msg"),
     (3, 1, "36 rows, in 2 seconds", "ret"),
     (1, 0, "bar chart; Nashik 22% below target", "ret"),
     (0, 1, "“Why Nashik?”", "msg"),
     (1, 3, "breaks the gap down by product and store", "msg"),
     (1, 0, "two stores explain 70% of the gap", "ret")],
    note="The AI writes the query; the semantic model decides whether “sales” means net or gross. Most wrong answers start there.")


def semantic():
    rows = [("“sales”", "net_revenue (after returns)", "or gross? a company-wide definition", "#b93a32"),
            ("“district”", "store.district", "store address, not customer address", "#0b5d7a"),
            ("“last quarter”", "Apr–Jun (Indian financial year)", "not the calendar quarter", "#c47f17"),
            ("“vs target”", "join targets table on district", "only if the tables are linked", "#127a64")]
    o = [MK, T(0, 12, "What the semantic model does: turns everyday words into exact data", "b")]
    for i, (w, col, note, c) in enumerate(rows):
        y = 26 + i * 34
        o.append(f'<rect x="0" y="{y}" width="140" height="26" rx="5" fill="#e1f2ec" stroke="#127a64"/>'); o.append(T(70, y + 17, w, "b", "middle"))
        o.append(f'<line x1="142" y1="{y + 13}" x2="196" y2="{y + 13}" stroke="#4a5563" stroke-width="1.3" marker-end="url(#pa)"/>')
        o.append(f'<rect x="200" y="{y}" width="230" height="26" rx="5" fill="#e3f0f5" stroke="#0b5d7a"/>'); o.append(T(315, y + 17, col, "", "middle"))
        o.append(T(444, y + 17, note, "s", fill=c))
    return svg(166, o)
FIGS["semantic"] = semantic()

# ---------- Gmail and Workspace ----------
FIGS["flow_gm"] = seq(
    [("Supplier", "hotel in Udaipur", "merchant"), ("Gmail’s gate", "checks, filters", "network"), ("Sunita’s inbox", "ops head, Jaipur", "user"),
     ("Gemini", "inside Gmail", "app"), ("Admin console", "the owner’s rules", "bank")],
    [(0, 1, "rate sheet + PDF from @udaipurhotel.in", "msg"),
     (1, 1, "is the sender real? (SPF, DKIM, DMARC checks)", "self"),
     (1, 1, "spam and phishing models: safe; PDF scanned", "self"),
     (1, 2, "delivered to Primary", "msg"),
     (2, 3, "“Summarise this thread” (14 emails)", "msg"),
     (3, 2, "3 lines: new rates, deadline Friday, one open question", "ret"),
     (2, 3, "“Help me write”: accept, ask about child rates", "msg"),
     (3, 2, "draft reply; she edits and sends", "ret"),
     (2, 4, "shares the rate sheet: allowed inside the firm only", "msg")],
    note="Most of Gmail’s work happens before the email reaches her: checking the sender and blocking spam and phishing.")

FIGS["ladder_ws"] = ladder([("Starter", "30 GB, custom email,|Gemini in Gmail", "$7", G), ("Standard", "2 TB, recordings,|Gemini in all apps", "$14", B),
                            ("Plus", "5 TB, Vault,|stronger security", "$22", A), ("Enterprise", "data regions, advanced|security, AI controls", "quoted", P)],
                           "Google Workspace business plans, per user a month on a yearly plan (2025 list prices, Gemini included)")

# ---------- Microsoft 365 Copilot ----------
FIGS["flow_cop"] = seq(
    [("Arjun", "finance analyst", "user"), ("Copilot in Teams", "the assistant", "app"), ("Microsoft Graph", "mail, files, chats", "bank"),
     ("AI model", "in Microsoft’s cloud", "partner"), ("Word", "the draft", "app")],
    [(0, 1, "“What did we agree with the auditors?”", "msg"),
     (1, 2, "search only what Arjun is allowed to open", "msg"),
     (2, 1, "meeting transcript, 2 emails, 1 Excel file", "ret"),
     (1, 3, "his question + those passages + “cite sources”", "msg"),
     (3, 1, "4 agreed points with links to each source", "ret"),
     (1, 0, "answer in Teams, with citations", "ret"),
     (0, 1, "“Draft the email in Word”", "msg"),
     (1, 4, "draft created; Arjun checks the figures", "msg")],
    note="Copilot can see only what the user can already open. If old files were shared too widely, Copilot will find them.")


def copmoney():
    o = [T(0, 12, "What Copilot adds per user, list prices (illustrative; big customers get discounts)", "b")]
    bars = [("Microsoft 365 E3", 36, "#0b5d7a", "$36 a user a month"), ("+ Copilot", 30, "#3e4fb8", "+$30 a user a month")]
    x = 150
    for lab, v, c, note in bars:
        w = 7 * v
        o.append(f'<rect x="{x}" y="28" width="{w}" height="30" fill="{c}"/>'); o.append(T(x + w / 2, 47, note, "b w", "middle")); x += w
    o.append(T(142, 47, "per user", "b", "end"))
    o.append(T(x + 8, 47, "= $66", "b"))
    o.append(T(0, 88, "At 3 crore paid seats: 3 crore × $30 × 12 months ≈ $10.8 bn a year at list price.", "b"))
    o.append(T(0, 104, "Microsoft’s cost: model calls for every question, so heavy users earn less margin than light ones.", "s"))
    return svg(112, o)
FIGS["copmoney"] = copmoney()

# ---------- comparison 2x2 ----------
FIGS["pos2x2"] = two_by_two("How it is sold: through sales teams  →  users sign up themselves", "How it is priced: per seat  →  per use",
                            ["sales-led, per use", "self-serve, per use", "sales-led, per seat", "self-serve, per seat"],
                            [("AWS", 0.62, 0.9, "#c47f17", "start"), ("Google Cloud", 0.5, 0.8, "#127a64", "end"), ("Azure", 0.28, 0.86, "#0b5d7a", "end"),
                             ("Amplitude", 0.64, 0.52, "#7c3aa6", "start"), ("ThoughtSpot", 0.3, 0.36, "#3e4fb8", "start"),
                             ("Google Workspace", 0.84, 0.12, "#127a64", "end"), ("M365 Copilot", 0.2, 0.14, "#3e4fb8", "start"),
                             ("Intercom Fin (per resolution)", 0.92, 0.7, "#b93a32", "end")], h=300)
