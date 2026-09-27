"""M9 teardown figures (Intuit deep dive, Tata Neu, DigiLocker); imported at the end of m9_figs.py."""
from m9_figs import FIGS, svg, T, lines, hbars, waterfall, loop, two_by_two, seq, strip  # noqa: F401
from figlib import *  # noqa: F401,F403
from figlib import box, MK, G, B, A, GR, R, P, I, vbars, arr, curves, etree, stacks, ladder


# ================= Intuit: the company =================
def intu_timeline():
    pts = [(46, "1983", "Quicken", ["Scott Cook’s", "cheque-book app", "for households"], "#5b6470"),
           (130, "1992–93", "QuickBooks, TurboTax", ["Books for small", "firms; buys the", "maker of TurboTax"], "#0b5d7a"),
           (214, "2000s", "QuickBooks Online", ["Books in the", "cloud; later the", "main engine"], "#0b5d7a"),
           (298, "Dec 2020", "Credit Karma", ["$7.1 bn: free", "credit scores,", "paid by lenders"], "#7c3aa6"),
           (382, "2021", "Mailchimp", ["$12 bn: email", "marketing for", "small firms"], "#c47f17"),
           (466, "2023", "Intuit Assist", ["An AI assistant", "across TurboTax", "and QuickBooks"], "#3e4fb8"),
           (550, "Sep 2024", "Enterprise Suite", ["Moves up to firms", "with several", "companies"], "#127a64"),
           (634, "2025–26", "AI agents", ["Agents that chase", "invoices; $21.4 bn", "revenue in FY26"], "#3e4fb8")]
    o = ['<line x1="8" y1="92" x2="674" y2="92" stroke="#4a5563" stroke-width="2"/><g class="c">']
    for i, (x, d, h, ls, col) in enumerate(pts):
        o.append(f'<circle cx="{x}" cy="92" r="6.5" fill="{col}"/>')
        if i % 2 == 0:
            o.append(T(x, 78, d, "b", "middle")); y0 = 114
        else:
            o.append(T(x, 112, d, "b", "middle")); y0 = 16
        o.append(T(x - 40, y0, h, "b", "start", fill=col))
        for j, l in enumerate(ls): o.append(T(x - 40, y0 + 14 + j * 13, l))
    o.append("</g>")
    return svg(168, o)
FIGS["intu_timeline"] = intu_timeline()

FIGS["intu_rev"] = hbars([("QuickBooks online and IES", 8.6, "subscriptions, payments, payroll, loans (derived)"), ("TurboTax", 5.3, "+7%; the expert-help tiers are 53% of it"),
                          ("QuickBooks desktop and other", 3.0, "older installed software (derived)"), ("Credit Karma", 2.6, "+20%: loans, insurance, cards"),
                          ("Mailchimp", 1.26, "flat; its own segment from Aug 2026 (derived)"), ("ProTax", 0.65, "software for tax professionals")], 9,
                         lw=190, fmt="${}", unit=" bn", colors=["#0b5d7a", "#127a64", "#9aa3ad", "#7c3aa6", "#c47f17", "#9aa3ad"],
                         note="Intuit’s $21.4 bn of revenue in FY2026 (year to 31 Jul 2026), by product")


def intu_map():
    o = [MK, '<g class="c">']
    col = [(0, "Consumers", "filing taxes, checking credit", G), (230, "Small businesses", "1–50 staff", B), (460, "Mid-sized firms", "several companies, 50–500 staff", A)]
    for x, t, s, c in col:
        o.append(f'<rect x="{x}" y="0" width="220" height="30" rx="5" fill="{c[0]}" stroke="{c[1]}"/>')
        o.append(T(x + 110, 13, t, "b", "middle")); o.append(T(x + 110, 25, s, "s", "middle"))
    o.append(box(10, 48, 200, 46, *G, [("TurboTax", "b"), ("files the yearly tax return", "s")], lh=13))
    o.append(box(10, 128, 200, 46, *P, [("Credit Karma", "b"), ("free score; lenders pay", "s")], lh=13))
    o.append(box(240, 48, 200, 46, *B, [("QuickBooks", "b"), ("books, invoices, payments, payroll", "s")], lh=13))
    o.append(box(240, 128, 200, 46, *A, [("Mailchimp", "b"), ("email and SMS to customers", "s")], lh=13))
    o.append(box(470, 48, 200, 46, *I, [("Intuit Enterprise Suite", "b"), ("many companies, one set of books", "s")], lh=13))
    o.append(box(470, 128, 200, 46, *GR, [("Accountants (ProTax, QBOA)", "b"), ("recommend and run QuickBooks", "s")], lh=13))
    o.append(arr(110, 96, 110, 124, "#127a64")); o.append(T(116, 114, "refund into a Credit Karma", "s")); o.append(T(116, 125, "account", "s"))
    o.append(arr(340, 96, 340, 124)); o.append(T(346, 114, "customer lists", "s"))
    o.append(arr(442, 71, 466, 71)); o.append(T(454, 64, "grows", "s", "middle"))
    o.append(arr(470, 150, 444, 110)); o.append(T(452, 144, "sell", "s", "end"))
    o.append(box(90, 196, 500, 40, "#f3f3ee", "#6b6a52", [("One customer record and one data platform underneath:", "b"), ("each product’s data makes the others’ AI answers and offers better", "s")], lh=13))
    o.append("</g>")
    return svg(242, o)
FIGS["intu_map"] = intu_map()

FIGS["intu_fly"] = loop(["More customers|file, bill and borrow", "More financial data|incomes, invoices, bills", "Better AI|categories, answers, odds",
                         "More done for you|agents plus human experts", "More money products|payments, payroll, loans"],
                        "Intuit’s|data flywheel", h=236, ry=84, bw=164)


# ================= TurboTax =================
FIGS["flow_tt"] = seq(
    [("Rohan", "first US return", "user"), ("TurboTax", "app", "app"), ("Employer data", "W-2 import", "partner"), ("Tax expert", "TurboTax Live", "partner"),
     ("IRS", "tax authority", "bank"), ("His bank", "refund lands", "merchant")],
    [(0, 1, "photo of W-2 form", "msg"), (1, 2, "fetch W-2 details", "msg"), (2, 1, "salary, tax withheld", "ret"),
     (1, 0, "plain-words questions", "msg"), (0, 1, "adds $89 expert review", "money"), (1, 3, "return + his notes", "msg"),
     (3, 0, "video call: fixes a deduction", "msg"), (1, 4, "e-file the return", "msg"), (4, 1, "accepted in 24 hours", "ret"),
     (4, 5, "$1,240 refund, about 3 weeks", "money")],
    note="The expert step (⑤–⑦) is where TurboTax now earns most: 53% of its revenue in FY26.")

FIGS["tt_ladder"] = ladder([("Free Edition", "simple returns only:|salary, few credits", "$0", G), ("Do it yourself", "investments, rent,|self-employment", "≈ $60–130", B),
                            ("Expert Assist", "a tax expert checks|and signs off", "≈ $90–220", I), ("Full Service", "an expert does|the whole return", "≈ $130–400+", P)],
                           "TurboTax’s price ladder, federal return (illustrative US prices; state returns extra)")

FIGS["tt_season"] = vbars([("Aug–|Oct", 3, "3%"), ("Nov–|Jan", 22, "22%"), ("Feb–|Apr", 70, "70%"), ("May–|Jul", 5, "5%")], 75,
                          "TurboTax revenue by quarter", sub="share of the year (illustrative)", colors=["#9aa3ad", "#0b5d7a", "#127a64", "#9aa3ad"])

# ================= QuickBooks =================
FIGS["flow_qb"] = seq(
    [("Neha", "bakery owner", "user"), ("QuickBooks", "books + payments", "app"), ("Café chain", "her customer", "merchant"),
     ("Her bank", "business account", "bank"), ("Staff, tax office", "payroll", "partner")],
    [(0, 1, "sends a $2,400 invoice", "msg"), (1, 2, "invoice with a pay link", "msg"), (2, 1, "pays $2,400 by card", "money"),
     (1, 3, "$2,330 deposited (fee $70)", "money"), (3, 1, "bank feed: every transaction", "ret"), (1, 1, "AI files “flour” as cost of goods", "self"),
     (0, 1, "runs payroll for 6 staff", "msg"), (1, 4, "wages paid; payroll tax filed", "money"), (1, 0, "profit and loss, tax-ready", "ret")],
    note="The subscription is the door; payments (④) and payroll (⑧) earn as much again.")

FIGS["qb_money"] = stacks([("Plus plan only", [1380, 0, 0, 0], "$1,380 a year"), ("With payments,|payroll, a loan", [1380, 1100, 900, 400], "$3,780 a year")],
                          ["subscription", "payment fees", "payroll", "loan interest"], ["#0b5d7a", "#127a64", "#3e4fb8", "#c47f17"], 4200,
                          title=None, lw=130, unit="")

# ================= IES =================
FIGS["ies_cons"] = waterfall([("Bakery|company", 0.8, "start"), ("Café|company", 0.6, "up"), ("Central kitchen|company", 0.5, "up"),
                              ("Simple sum", 0, "total"), ("Kitchen’s sales|to the group", 0.2, "down"), ("Group|revenue", 0, "total")],
                             h=220, unit="$", suffix=" mn", note="A group of three companies: revenue for the year ($ million, illustrative)")

FIGS["ies_ladder"] = ladder([("Simple Start", "one user,|basic books", "$38", G), ("Essentials", "bills, more|users", "$75", G),
                             ("Plus", "stock, projects,|budgets", "$115", B), ("Advanced", "25 users, custom|reports, workflows", "$275", B),
                             ("Enterprise Suite", "many companies,|consolidation, AI", "quoted", I)],
                            "QuickBooks plans, price a month (US list prices, approximate, 2025–26)", h=206)

# ================= Credit Karma and Mailchimp =================
FIGS["flow_ck"] = seq(
    [("Maria", "member", "user"), ("Credit Karma", "free app", "app"), ("Credit bureau", "TransUnion", "partner"), ("Card issuer", "the lender", "bank")],
    [(0, 1, "signs up free", "msg"), (1, 2, "soft check (no effect on score)", "msg"), (2, 1, "score 712 + credit history", "ret"),
     (1, 1, "models approval odds per card", "self"), (1, 0, "“Approval odds: very good”", "msg"), (0, 3, "applies for the card", "msg"),
     (3, 0, "approved", "ret"), (3, 1, "fee for an approved customer", "money")],
    note="The member pays nothing; the lender pays when she is approved. Revenue swings with lenders’ appetite.")

# ================= Intuit Assist and agents =================
FIGS["flow_agent"] = seq(
    [("Neha", "owner", "user"), ("Payments agent", "Intuit Assist", "app"), ("QuickBooks data", "invoices, history", "partner"), ("Customer", "late payer", "merchant")],
    [(1, 2, "find overdue invoices", "msg"), (2, 1, "3 overdue; one always pays late", "ret"), (1, 1, "drafts polite reminders + pay link", "self"),
     (1, 0, "“Send these 3 reminders?”", "msg"), (0, 1, "approves (edits one)", "msg"), (1, 3, "reminder with pay link", "msg"),
     (3, 1, "pays $1,100 by card", "money"), (1, 2, "marks paid, matches bank deposit", "msg")],
    note="Intuit reports invoices chased this way are paid about 5 days sooner on average (2025).")


# ================= Tata Neu =================
FIGS["flow_neu"] = seq(
    [("Priya", "member", "user"), ("Neu app", "and NeuCoins", "app"), ("BigBasket", "groceries", "merchant"), ("HDFC Bank", "co-brand card", "bank"),
     ("Air India", "flight", "merchant")],
    [(0, 2, "₹4,000 groceries, Neu card", "money"), (3, 1, "5% as coins: 200 NeuCoins", "msg"), (2, 1, "brand offer: 40 more coins", "msg"),
     (1, 0, "balance 1,240 coins = ₹1,240", "ret"), (0, 4, "books a ₹6,500 flight", "msg"), (0, 1, "uses 1,240 coins at checkout", "msg"),
     (1, 4, "₹1,240 settled to Air India", "money"), (0, 4, "pays ₹5,260 balance", "money")],
    note="Most coins come from the card (②), which HDFC pays for; brands add offers (③).")

# ================= DigiLocker =================
FIGS["flow_dl"] = seq(
    [("Grandfather", "citizen", "user"), ("DigiLocker", "app", "app"), ("Transport dept", "the issuer", "bank"), ("Traffic police", "the verifier", "partner")],
    [(0, 1, "log in with Aadhaar OTP", "msg"), (1, 2, "fetch licence for this Aadhaar", "msg"), (2, 1, "licence record + digital signature", "ret"),
     (1, 1, "stores a link to the record", "self"), (3, 0, "“licence, please”", "msg"), (0, 3, "shows it; officer scans the QR", "msg"),
     (3, 2, "check the record live", "msg"), (2, 3, "valid, not suspended", "ret")],
    note="The issuer, not the citizen, vouches for the document; nothing is scanned or photocopied.")


def dl_issued():
    o = [MK, '<g class="c">']
    o.append(T(0, 12, "Uploaded copy", "b red")); o.append(T(350, 12, "Issued document", "b grn"))
    o.append(box(0, 24, 320, 118, *R, [("A photo of a paper licence", "b"), ("anyone can edit a photo", ""), ("may be out of date or suspended", ""),
                                       ("officer must trust the citizen", ""), ("like a photocopy: needs attestation", "s")], lh=16))
    o.append(box(350, 24, 330, 118, *G, [("A record fetched from the issuer", "b"), ("carries the issuer’s digital signature", ""), ("checked live: current status", ""),
                                         ("officer trusts the transport dept", ""), ("legally equal to the original", "s")], lh=16))
    o.append("</g>")
    return svg(148, o)
FIGS["dl_issued"] = dl_issued()


# ================= comparison =================
FIGS["pos2x2"] = two_by_two("How often people use it: once a year  →  every day", "Who pays: the user  →  someone else",
                            ["Rare, someone else pays", "Frequent, someone else pays", "Rare, the user pays", "Frequent, the user pays"],
                            [("DigiLocker (the state)", 0.07, 0.72, "#127a64", "start"), ("Credit Karma (lenders)", 0.3, 0.86, "#7c3aa6", "start"),
                             ("Tata Neu (card, brands)", 0.62, 0.7, "#7c3aa6", "start"), ("TurboTax", 0.06, 0.12, "#127a64", "start"),
                             ("Mailchimp", 0.5, 0.3, "#c47f17", "start"), ("QuickBooks", 0.8, 0.2, "#0b5d7a", "end"), ("IES", 0.86, 0.08, "#3e4fb8", "end")], h=290)
