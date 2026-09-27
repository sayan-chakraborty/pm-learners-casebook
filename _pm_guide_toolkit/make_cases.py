import os
import sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cases2

def note(kind, title, text):
    return f'<div class="note {kind}"><b>{title}</b>{text}</div>'

CASES = [
dict(src="iimb", pages=[38], ref="IIM Bangalore · Sigma casebook p. 38", typ="Product design", lvl="Hard",
 title="A credit platform for teenagers",
 notes={1: note("check", "The move that wins this case", "Spotting that a minor cannot sign a loan contract. Under the Indian Contract Act, 1872 (s.11), an agreement with someone under 18 is void. So a 'teen credit' product is really a <i>guardian-backed</i> product. Two users, not one."),
        5: note("term", "Is this credit?", "Pocket money loaded by a parent is a <strong>prepaid</strong> balance, not credit. Credit means someone lends money and carries the risk that it is not repaid. Always ask: who lends, and who eats the loss?"),
        9: note("metric", "Teen credit score", "Nice idea, but India's credit bureaus (CIBIL, Experian) score adults with loans or cards. A private 'score' would only be a badge unless a lender uses it."),
        13: note("metric", "Missing: a North Star", "Four metric buckets, but no single number that says 'this worked'. One candidate: <i>% of teen accounts that settle the monthly balance on time for 3 months running</i>. Guardrail: default rate.")},
 coach=[("What works", "Two-sided personas (teen and guardian), a sensible age split (13–15 vs 16–18), and honest trade-offs: freedom versus control, and default risk."),
        ("What's missing", "Who provides the money and under which licence. In 2022 the RBI stopped non-banks from loading credit lines into prepaid cards and wallets, which hit exactly this kind of product (Chapter 3). Also missing: how the business earns (interchange on spends? a parent subscription?)."),
        ("A stronger answer", "Reframes the goal as <b>credit-building</b>: a guardian-funded card with a spending limit that behaves like credit (monthly 'bill', on-time streaks), then graduates to a real secured card at 18. Real examples: FamPay and Junio in India, Greenlight and Step in the US."),
        ("Read next", "Chapter 3 (lending and regulation) and Chapter 4 (trust).")]),
dict(src="iimb", pages=[55, 56], ref="IIM Bangalore · Sigma casebook pp. 55–56", typ="Product design", lvl="Hard",
 title="A mobile banking app for rural India",
 notes={1: note("check", "Good opening", "Four clarifying questions, and the last one ('is there an objective?') unlocks the case: the interviewer says the real problem is crowded branches."),
        5: note("check", "Check the number", "The '~30% UPI failure rate in rural India' is not sourced. NPCI's published technical-decline rates are far lower nationally. In an interview, say 'I'd assume a high failure rate, say 1 in 10' and label it an assumption."),
        7: note("term", "Offline UPI already exists", "<strong>UPI 123PAY</strong> (2022) lets feature-phone users pay by IVR call or missed call, and <strong>UPI Lite X</strong> works offline over NFC. Name what exists, then improve it."),
        10: note("metric", "RICE with words", "RICE is Reach × Impact × Confidence ÷ Effort. Scoring with 'High-Moderate' hides the maths. Put rough numbers in, even if invented, so the ranking can be argued with."),
        13: note("metric", "L1 metric: tied to the goal", "'Average waiting time during a branch visit' measures the bank's actual problem. That is the right instinct: pick the metric that proves the objective, not generic DAU.")},
 coach=[("What works", "Clarifies the objective before designing; picks the larger segment (regular customers) with a reason; phases the roll-out; the headline metric matches the objective."),
        ("What's missing", "Rural India already has two systems built for this: <b>banking correspondents</b> (local agents who take deposits for a bank, the 'vendor partnership' idea) and <b>AePS</b>, where people withdraw government money at a micro-ATM using their fingerprint. A strong candidate designs around these. Also missing: voice and local-language design, and trust (family members often help)."),
        ("A stronger answer", "Starts from the most common reason people visit the branch (often checking whether a government payment arrived), solves it with an SMS or voice balance check and 'money arrived' alerts, and measures branch footfall per 1,000 customers."),
        ("Read next", "Chapter 2 (how money moves) and Chapter 5 (UPI 123PAY, UPI Lite).")]),
dict(src="iimb", pages=[116, 117], ref="IIM Bangalore · Sigma casebook pp. 116–117", typ="Product improvement", lvl="Medium",
 title="Improve your favourite UPI app",
 notes={1: note("check", "Keep the intro short", "A 30-second product summary is enough. This one runs long; interviewers often cut in."),
        3: note("check", "Claim: 'PhonePe has a higher success rate than GPay'", "<span class='verdict v-na'>Can't verify</span> Success rates depend mostly on the payer's bank, not the app. Avoid comparative claims you can't back."),
        5: note("check", "Asking for the goal", "Exactly right: improvement for what? Engagement, share, retention or revenue each lead to different features."),
        13: note("term", "The 'suspense wallet'", "Holding the customer's money in a middle wallet makes the app a <strong>PPI</strong> (prepaid instrument) issuer, which needs an RBI licence, and breaks UPI's direct bank-to-bank design. UPI already has a rule: failed debits are reversed by T+1, or the bank pays ₹100 a day."),
        17: note("metric", "Metrics the app can move", "Payment success rate is driven mainly by banks. Better app metrics: payments per monthly user, 30-day retention, and 'pending' payments cleared within 1 minute.")},
 coach=[("What works", "Asks for the goal, chooses retention with a reason, builds four clear personas and prioritises two."),
        ("What's missing", "Why retention is hard here: UPI is <b>interoperable</b>, so any app pays any QR and switching costs nothing. Features that competitors can copy in a week won't hold users."),
        ("A stronger answer", "Targets the moment of failure: a clear 'pending' screen with a countdown, automatic retry through UPI Lite for small amounts, and a message to the shop saying 'payment is on its way'. Measures repeat payments after a failure."),
        ("Read next", "Chapter 2 (interoperability) and Chapter 5 (why payments fail).")]),
dict(src="iimb", pages=[110, 111], ref="IIM Bangalore · Sigma casebook pp. 110–111", typ="Product improvement", lvl="Medium",
 title="Stopping fraud in a mobile banking app",
 notes={5: note("metric", "'Frauds prevented' is hard to count", "You never see the frauds you stopped. Use <i>fraud loss rate</i> (₹ lost per ₹1 lakh transacted) plus a <i>false-alarm rate</i> (genuine payments blocked). The second protects customers from friction."),
        13: note("check", "The strongest insight here", "Forwarding an OTP to a caller is the textbook social-engineering scam. Most fraud in India does not break the tech; it tricks the person."),
        15: note("check", "How big is tap-to-pay fraud?", "Contactless card payments up to ₹5,000 need no PIN (RBI, 2021). Skimming someone's pocket is possible but rare. Scams where the victim sends the money themselves are far more common (Chapter 4)."),
        17: note("term", "Auto-approve after 30 minutes", "Look closely: a suspicious payment <i>goes through</i> if the user doesn't respond. That default protects convenience, not the customer. Defaults are product decisions.")},
 coach=[("What works", "Clarifies scope, segments users, and follows the interviewer's steer to tech-savvy users; the toggle shows awareness of friction."),
        ("What's missing", "Data on where losses actually come from. Of ₹22,495 crore lost to cyber fraud in 2025, investment scams were about three-quarters (I4C). Also missing: the precision/recall trade-off every fraud feature faces."),
        ("A stronger answer", "Targets the riskiest moment: the first payment to a new payee after a phone call. It adds a cooling-off hold for large first-time transfers, shows the receiver's bank-registered name in big type, and measures fraud loss rate with a guardrail on false blocks."),
        ("Read next", "Chapter 4 (trust and fraud).")]),
dict(src="iima", pages=[294], ref="IIM Ahmedabad · Product Mindset p. 294", typ="Metrics", lvl="Medium",
 title="Metrics for tie-in promotions on Google Pay",
 notes={1: note("check", "Define the feature first", "Restating what a tie-in promotion is avoids solving the wrong problem. Takes 15 seconds."),
        7: note("metric", "A metric formula", "Breaking one number into factors (payments × share of cards that are tie-ins × redemption rate) shows exactly which lever moved. This is the most reusable move in metrics interviews."),
        12: note("metric", "Missing: incrementality", "Did the coupon make someone buy, or would they have bought anyway? Only a <strong>holdout</strong> group that never sees the promotion can answer that.")},
 coach=[("What works", "Two stakeholders (users and partner brands), goals before metrics, and a clean formula for each side."),
        ("What's missing", "A North Star, a guardrail and incrementality. Rewards can train users to pay only for cashback; Google Pay cut its famous scratch-card cashback after 2020, and usage held up because the habit had formed."),
        ("A stronger answer", "North Star: <i>payments made by users in the 30 days after redeeming a partner coupon</i> versus a holdout. Partner metric: cost per new customer compared with the brand's own ads. Guardrail: complaint rate about irrelevant coupons."),
        ("Read next", "Chapter 3 (how payment apps earn).")]),
dict(src="iima", pages=[308], ref="IIM Ahmedabad · Product Mindset p. 308", typ="Root cause analysis", lvl="Medium",
 title="Android users fall 40% in a banking app",
 notes={5: note("check", "Step 1: is the data real?", "Before hunting causes, rule out broken tracking. A logging change produces exactly the same graph as a real drop."),
        9: note("check", "Slice the data", "Android version, device maker, region, new vs existing users. The cut that concentrates the drop points to the cause."),
        13: note("term", "Staged rollout", "App stores let you release an update to 1%, then 5%, 20%… of users. If metrics break, you halt the rollout. That is why the drop showed first in one region."),
        21: note("metric", "Add: halt first, diagnose second", "The first action should be to pause the rollout in the Play Console within minutes, before the root cause is fully proven.")},
 coach=[("What works", "The textbook order: confirm the metric, check data quality, rule out external factors, segment, then look at internal changes. The staged-rollout reconciliation is excellent."),
        ("What's missing", "Size of the damage (how many customers are locked out of their money right now?), a customer-support plan and the regulator angle: banks must report major outages."),
        ("A stronger answer", "Adds a crash-free-sessions guardrail with an automatic rollout stop (for example, pause if crash-free sessions fall below 99.5%)."),
        ("Read next", "Chapter 5 (how releases and outages work).")]),
]

out = ['<section class="pb">', '<div class="chapter"><div class="num">1</div><div><div class="kicker">The interview room</div><h1>Six fintech cases, word for word</h1></div><div class="dek">Real case interviews from the IIM Ahmedabad and IIM Bangalore casebooks, reproduced verbatim. Try each one cold, then read the answer with the coach&#8217;s notes in the margin.</div></div>']
out.append('<p class="lead">Each case below is exactly as it appears in its casebook: a model answer written by students who went through PM interviews. The answers are good but not perfect. The margin notes show you where the candidate scored points and where they left points on the table. The box after each case says what a stronger answer would add, and which chapter explains the concept behind it.</p>')
for i, c in enumerate(CASES, 1):
    out.append(f'<div class="casehead"><div class="meta">Case {i} · {c["typ"]} · {c["lvl"]} · {c["ref"]}</div><h2>{c["title"]}</h2><div class="try">Try it first: read only the dark question box, cover the rest, and spend five minutes sketching your answer out loud.</div></div>')
    out.append(cases2.render_pages(c["src"], c["pages"], c["notes"]))
    dl = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in c["coach"])
    out.append(f'<div class="box coach clear"><h4>Coach&#8217;s verdict</h4><dl>{dl}</dl></div>')
out.append("</section>")
open("sample_fintech_cases.html", "w", encoding="utf-8").write("\n".join(out))
print("ok")
