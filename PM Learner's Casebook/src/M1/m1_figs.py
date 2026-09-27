"""Generated SVGs for M1 teardowns ({{SVG:name}} in parts): behind-the-screens sequence diagrams.
No screen mockups (owner's rule, 25 Sep 2026)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "common"))
from svgkit import seq  # noqa: E402

FIGS = {}

# PhonePe: Meena pays her electricity bill, then sees a loan offer
FIGS["flow_phonepe"] = seq(
    [("Meena", "PhonePe app", "user"), ("PhonePe", "app + BBPS agent", "app"), ("NPCI", "BBPS + UPI", "network"),
     ("Meena’s bank", "issuer", "bank"), ("Electricity board", "the biller", "merchant"), ("Partner lender", "bank or NBFC", "partner")],
    [(0, 1, "consumer no. 4081…", "msg"),
     (1, 2, "fetch the bill", "msg"),
     (2, 4, "bill for this number?", "msg"),
     (4, 1, "₹1,240, due 10 Oct", "ret"),
     (0, 1, "UPI PIN (encrypted)", "msg"),
     (1, 2, "pay ₹1,240", "msg"),
     (2, 3, "debit ₹1,240", "msg"),
     (3, 4, "₹1,240 (banks settle later)", "money"),
     (4, 1, "paid ✓ + receipt", "ret"),
     (1, 5, "is Meena eligible? (her consent)", "msg"),
     (5, 1, "offer: up to ₹5 lakh", "ret"),
     (5, 3, "loan paid into her own account", "money"),
     (5, 1, "sourcing fee to PhonePe", "money")],
    note="PhonePe never holds the bill money or the loan: it earns only at step ⑬.")

# Google Pay: Aman requests ₹250, Rahul pays, a reward follows
FIGS["flow_gpay"] = seq(
    [("Rahul", "payer", "user"), ("Google Pay", "app + rewards", "app"), ("NPCI", "UPI switch", "network"),
     ("Banks", "Rahul’s and Aman’s", "bank"), ("Aman", "flatmate", "user"), ("Lenskart", "coupon partner", "partner")],
    [(4, 1, "request ₹250 · cab home", "msg"),
     (1, 0, "request shows in their chat", "msg"),
     (0, 1, "Pay + UPI PIN", "msg"),
     (1, 2, "pay ₹250 to aman@…", "msg"),
     (2, 3, "debit Rahul, credit Aman", "msg"),
     (3, 3, "₹250 moves bank to bank", "self"),
     (2, 1, "success", "ret"),
     (1, 4, "“₹250 received” in chat", "ret"),
     (1, 1, "rewards engine: eligible? which card?", "self"),
     (1, 0, "scratch card: ₹11 + coupon", "msg"),
     (0, 5, "uses coupon on an order", "msg"),
     (5, 1, "pays for placement", "money")],
    note="Google funds the ₹11; the coupon’s cost falls on Lenskart.")

# Paytm: a ₹10 chai payment, the evening settlement, a loan from takings
FIGS["flow_paytm"] = seq(
    [("Customer", "any UPI app", "user"), ("NPCI", "UPI switch", "network"), ("Paytm", "aggregator, escrow", "app"),
     ("Soundbox", "on the counter", "merchant"), ("Sunita’s bank", "SBI account", "bank"), ("Partner lender", "NBFC", "partner")],
    [(0, 1, "pay ₹10 to Sunita’s QR", "msg"),
     (1, 2, "₹10 into escrow", "money"),
     (2, 3, "“₹10 received”", "msg"),
     (3, 3, "speaks it aloud, in Hindi", "self"),
     (2, 4, "day’s ₹6,850 minus fees", "money"),
     (2, 2, "scores 6 months of takings", "self"),
     (2, 5, "Sunita pre-qualifies", "msg"),
     (5, 4, "₹50,000 loan", "money"),
     (2, 5, "₹310 a day, from settlements", "money"),
     (5, 2, "distribution fee", "money")],
    note="Money in escrow is the customers’ and Sunita’s, never Paytm’s own; Paytm earns device fees, card fees and step ⑩.")

# Razorpay: an online order with order API, UPI intent, webhook, settlement
FIGS["flow_razorpay"] = seq(
    [("Arjun", "phone browser", "user"), ("Neha’s site", "shop + server", "merchant"), ("Razorpay", "payment aggregator", "app"),
     ("UPI", "NPCI + Arjun’s bank", "network"), ("Escrow bank", "holds funds", "bank"), ("Neha’s bank", "current account", "bank")],
    [(0, 1, "Pay ₹899", "msg"),
     (1, 2, "create order: ₹899 (API)", "msg"),
     (2, 1, "order_id", "ret"),
     (2, 0, "checkout opens his UPI app", "msg"),
     (0, 3, "UPI PIN: pay ₹899", "msg"),
     (3, 4, "₹899", "money"),
     (3, 2, "success", "ret"),
     (2, 0, "“order placed” page", "ret"),
     (2, 1, "webhook: payment.captured", "msg"),
     (1, 1, "checks signature, packs order", "self"),
     (4, 5, "₹881 after the 2% fee, T+2", "money")],
    note="Razorpay keeps about ₹18 here; buyers’ money waits in an escrow account, not Razorpay’s own.")

# Groww: first SIP, from KYC to units
FIGS["flow_groww"] = seq(
    [("Priya", "first salary", "user"), ("Groww", "broker + fund platform", "app"), ("KYC checks", "PAN, DigiLocker, KRA", "network"),
     ("Priya’s bank", "salary account", "bank"), ("Fund house", "AMC + registrar", "partner")],
    [(0, 1, "PAN + Aadhaar consent", "msg"),
     (1, 2, "verify PAN, fetch address", "msg"),
     (2, 1, "KYC done, saved centrally", "ret"),
     (1, 3, "₹1 test deposit", "money"),
     (0, 1, "SIP ₹2,000 on the 5th", "msg"),
     (0, 3, "approve UPI Autopay once (PIN)", "msg"),
     (1, 3, "5th of month: collect ₹2,000", "msg"),
     (3, 4, "₹2,000 (via clearing)", "money"),
     (4, 4, "units at that day’s price (NAV)", "self"),
     (4, 0, "statement: units added", "ret")],
    note="Direct plan: the fund pays Groww no commission, so this SIP earns Groww almost nothing.")

# ---------- technology ----------
FIGS["flow_request"] = seq(
    [("Meena’s phone", "PhonePe app", "user"), ("DNS resolver", "phone book of the web", "network"),
     ("Load balancer", "spreads traffic", "app"), ("App server", "PhonePe’s code", "app"),
     ("Database", "her accounts", "merchant"), ("Her bank", "core banking", "bank")],
    [(0, 1, "where is api.phonepe.com?", "msg"),
     (1, 0, "IP address (then cached)", "ret"),
     (0, 2, "secure handshake (TLS)", "msg"),
     (0, 2, "HTTPS: GET /balance + token", "msg"),
     (2, 3, "to a healthy server", "msg"),
     (3, 3, "checks token: is this Meena?", "self"),
     (3, 4, "which bank account?", "msg"),
     (4, 3, "SBI ••4418", "ret"),
     (3, 5, "balance enquiry (via UPI)", "msg"),
     (5, 3, "₹18,240", "ret"),
     (3, 0, "200 OK + JSON {balance: 18240}", "ret")],
    note="Steps ①–⑤ take milliseconds; ⑨–⑩, the bank’s core system, usually take longest.")

def tail_chart():
    times = [1.2] * 90 + [3.0] * 8 + [15.0] * 2
    x0, bw, base, k = 60, 5.6, 128, 100 / 15
    col = {1.2: "#9fb3c8", 3.0: "#e0a340", 15.0: "#b93a32"}
    bars = "".join(f'<rect x="{x0 + i * bw:.1f}" y="{base - t * k:.1f}" width="{bw - .6:.1f}" height="{t * k:.1f}" fill="{col[t]}"/>'
                   for i, t in enumerate(times))
    grid = "".join(f'<line x1="56" y1="{base - s * k:.1f}" x2="622" y2="{base - s * k:.1f}" stroke="#e3e7eb"/>'
                   f'<text x="52" y="{base - s * k + 4:.1f}" text-anchor="end" class="s">{s} s</text>' for s in (0, 5, 10, 15))
    mean_y = base - 1.62 * k
    p95x = x0 + 94 * bw + (bw - .6) / 2
    p99x = x0 + 98 * bw + (bw - .6) / 2
    return f'''<svg class="d" viewBox="0 0 680 150" xmlns="http://www.w3.org/2000/svg">
 {grid}{bars}
 <line x1="56" y1="{mean_y:.1f}" x2="622" y2="{mean_y:.1f}" stroke="#1c232b" stroke-width="1.4" stroke-dasharray="5 3"/>
 <text x="64" y="{mean_y - 6:.1f}" class="b">mean = 1.62 s: looks fine</text>
 <line x1="{p95x:.1f}" y1="{base - 3 * k - 4:.1f}" x2="{p95x:.1f}" y2="72" stroke="#c47f17" stroke-width="1.2"/>
 <text x="{p95x - 4:.1f}" y="70" text-anchor="end" class="b" fill="#9a6310">p95 = 3 s</text>
 <text x="{p99x - 12:.1f}" y="36" text-anchor="end" class="b red">p99 = 15 s: 2 in 100 hit the timeout</text>
 <text x="630" y="{base - 3:.1f}" class="s">90 × 1.2 s</text>
 <text x="340" y="146" text-anchor="middle" class="s">100 payments, sorted from fastest to slowest (illustrative)</text>
</svg>'''

FIGS["tail"] = tail_chart()
