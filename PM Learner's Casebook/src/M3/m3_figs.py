"""Generated SVGs for M3 ({{SVG:name}} in parts): move strips, waterfalls, bar charts, teardown sequence flows."""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "common"))
from svgkit import seq as _seq  # noqa: E402
from html import escape as _E

def seq(*a, **k):
    k.setdefault("row", 24)
    return _seq(*a, **k)

FIGS = {}

def svg(h, body, w=680):
    return f'<svg class="d" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">' + "".join(body) + "</svg>"

def T(x, y, s, cls="", anchor="start", size=None, fill=None):
    st = []
    if size: st.append(f"font-size:{size}px")
    if fill: st.append(f"fill:{fill}")
    sa = f' style="{";".join(st)}"' if st else ""
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}"{sa}>{_E(s)}</text>'

def lines(x, y, s, cls="", anchor="middle", lh=13, size=None):
    return "".join(T(x, y + i * lh, t, cls, anchor, size) for i, t in enumerate(s.split("|")))

# ---------- move strip (stronger answers) ----------
STRIP_COLS = ["#127a64", "#1d8a73", "#2a9a82", "#0b5d7a", "#3e4fb8", "#7c3aa6", "#8a4fb0"]
def strip(moves):
    n = len(moves); w = (680 - 10) / n
    o = ['<g class="c">']
    for i, (a, b) in enumerate(moves):
        x0 = i * w; x1 = x0 + w + (10 if i < n - 1 else 0)
        tip = 10 if i < n - 1 else 0
        pts = f"{x0:.1f},4 {x0 + w:.1f},4 {x0 + w + tip:.1f},31 {x0 + w:.1f},58 {x0:.1f},58" + (f" {x0 + 10:.1f},31" if i else "")
        if i == n - 1: pts = f"{x0:.1f},4 680,4 680,58 {x0:.1f},58 {x0 + 10:.1f},31"
        o.append(f'<polygon points="{pts}" fill="{STRIP_COLS[i % len(STRIP_COLS)]}"/>')
        cx = x0 + w / 2 + (5 if i else 0)
        o.append(T(cx, 26, f"{'①②③④⑤⑥⑦⑧'[i]} {a}", "b w", "middle"))
        o.append(T(cx, 44, b, "w", "middle"))
    o.append("</g>")
    return svg(62, o)

FIGS["strip31"] = strip([("Clarify", "which engagement?"), ("Size it", "why users leave"), ("Need AI?", "rules vs model"),
                         ("Pick one", "four risks"), ("MVP", "wardrobe first"), ("Measure", "goal + safety")])
FIGS["strip32"] = strip([("Clarify", "what is healthy?"), ("Map", "buyers, sellers"), ("Liquidity", "does it match?"),
                         ("Goal", "one number"), ("Inputs", "levers per side"), ("Guardrails", "scams, spam")])
FIGS["strip33"] = strip([("Clarify", "which rate?"), ("Mix or rate?", "split the rise"), ("Reason codes", "where it shows"),
                         ("Size", "₹ per return"), ("Fix", "by root cause"), ("Measure", "net kept sales")])
FIGS["strip34"] = strip([("Clarify", "which Prime, goal"), ("Floor", "what it costs"), ("Ceiling", "what it’s worth"),
                         ("Break-even", "how many new?"), ("Test", "one market"), ("Decide", "with guardrails")])
FIGS["stripg1"] = strip([("Unit", "which queries?"), ("Approach", "top-down"), ("Tree", "users × rate"),
                         ("Numbers", "round, with reasons"), ("Check", "a second way"), ("Range", "and what moves it")])
FIGS["stripg2"] = strip([("Unit", "city, 10 min"), ("Approach", "two limits"), ("Tree", "area, peak orders"),
                         ("Numbers", "round, with reasons"), ("Check", "real store counts"), ("Range", "and headroom")])

# ---------- waterfall ----------
def waterfall(items, h=220, top=26, scale=None, unit="₹", label_w=0, note=None, upcol="#127a64", totcol="#127a64", vw=680, suffix=""):
    """items: (label, value, kind) kind: 'start' | 'up' | 'down' | 'total'. Bars left to right."""
    n = len(items); left = 4; right = vw - 2; bw = (right - left) / n
    vals = []; run = 0; hi = 0
    for lab, v, k in items:
        if k == "start": a, b = 0, v; run = v
        elif k == "total": a, b = 0, run
        elif k == "up": a, b = run, run + v; run += v
        else: a, b = run - v, run; run -= v
        vals.append((a, b)); hi = max(hi, a, b)
    base = h - 44; sc = scale or (base - top - 18) / hi
    Y = lambda v: base - v * sc
    o = [f'<line x1="{left}" y1="{base}" x2="{right}" y2="{base}" stroke="#4a5563"/>']
    for i, ((lab, v, k), (a, b)) in enumerate(zip(items, vals)):
        x = left + i * bw + 4; w = bw - 8
        col = {"start": "#0b5d7a", "total": totcol, "up": upcol, "down": "#b93a32"}[k]
        if k == "total" and b < 0: col = "#b93a32"
        y0, y1 = sorted((Y(a), Y(b)))
        o.append(f'<rect x="{x:.1f}" y="{y0:.1f}" width="{w:.1f}" height="{max(y1 - y0, 1.5):.1f}" fill="{col}" rx="2"/>')
        sign = "−" if k == "down" else ("+" if k == "up" else "")
        o.append(T(x + w / 2, y0 - 4, f"{sign}{unit}{abs(v) if k != 'total' else b:,}{suffix}", "b", "middle"))
        o.append(lines(x + w / 2, base + 14, lab, "s", "middle", 12))
        if i < n - 1 and k != "total":
            end = Y(b if k in ("start", "up") else a)
            o.append(f'<line x1="{x + w:.1f}" y1="{end:.1f}" x2="{x + bw:.1f}" y2="{end:.1f}" stroke="#9aa3ad" stroke-dasharray="2 2"/>')
    if note: o.append(lines(left, 12, note, "s", "start", 12))
    return svg(h, o, vw)

# platform view of one kept ₹1,299 kurta order (illustrative)
FIGS["wf_kept"] = waterfall([
    ("fees|from|seller", 380, "start"), ("forward|delivery", 85, "down"), ("sale|discount", 60, "down"),
    ("payment,|cash", 15, "down"), ("support,|tech", 25, "down"), ("left if|kept", 0, "total")],
    note="Platform’s side of one ₹1,299 kurta,|kept by the customer", vw=330, top=40, h=212, scale=0.27)
FIGS["wf_return"] = waterfall([
    ("forward|delivery", 85, "up"), ("reverse|pickup", 85, "up"),
    ("check,|repack", 20, "up"), ("resale|discount", 60, "up"), ("cost of|a return", 0, "total")],
    scale=0.27, upcol="#d9776f", totcol="#b93a32", note="The same kurta, returned: fees refunded,|and the system is out about ₹250", vw=330, top=40, h=212)

# ---------- horizontal bar chart ----------
def hbars(rows, maxv, h=None, lw=150, unit="", fmt="{:,}", colors=None, note=None, vw=680):
    """rows: (label, value, annotation)"""
    rh = 24; top = 18 if note else 4; h = h or top + rh * len(rows) + 6
    x0 = lw; W = vw - lw - 290
    o = []
    if note: o.append(T(0, 12, note, "s"))
    for i, (lab, v, ann) in enumerate(rows):
        y = top + i * rh
        col = (colors or ["#0b5d7a"])[i % len(colors or ["#0b5d7a"])]
        o.append(T(x0 - 6, y + 15, lab, "b", "end"))
        w = max(2, W * v / maxv)
        o.append(f'<rect x="{x0}" y="{y + 4}" width="{w:.1f}" height="15" fill="{col}" rx="2"/>')
        o.append(T(x0 + w + 5, y + 15, (fmt.format(v) + unit) + ("   " + ann if ann else ""), "s"))
    return svg(h, o, vw)

# ---------- teardown sequence flows ----------
FIGS["flow_amazon"] = seq(
    [("Neha", "Prime member", "user"), ("Amazon app", "search, Rufus, cart", "app"), ("Seller", "owns the stock", "merchant"),
     ("Amazon FC", "fulfilment centre", "network"), ("Delivery", "Amazon Logistics", "partner"), ("Bank / UPI", "payment", "bank")],
    [(0, 1, "“running shoes under ₹4,000, flat feet”", "msg"),
     (1, 1, "Rufus reads reviews + specs, suggests 3", "self"),
     (1, 0, "3 picks; top slot is a sponsored ad", "ret"),
     (0, 1, "buys ₹3,499 pair, Prime: free next-day", "msg"),
     (1, 5, "collect ₹3,499 by UPI", "msg"),
     (5, 1, "₹3,499 held by Amazon", "money"),
     (1, 3, "pick from the FC nearest Neha", "msg"),
     (3, 4, "packed, sorted, handed over by 6 pm", "msg"),
     (4, 0, "delivered next morning", "msg"),
     (1, 2, "remits ₹3,499 − fees (~₹600) in ~7 days", "money"),
     (2, 1, "pays for the sponsored slot, ₹45 a click", "money")],
    note="Amazon earns four ways on one order: seller fees, fulfilment, the ad click, and the Prime fee that made Neha buy here.")

FIGS["flow_flipkart"] = seq(
    [("Ramesh", "Indore, first phone EMI", "user"), ("Flipkart app", "sale, cart", "app"), ("Bank", "card EMI offer", "bank"),
     ("Seller", "phone stock", "merchant"), ("Ekart", "Flipkart logistics", "partner"), ("Old phone", "exchange partner", "network")],
    [(0, 1, "12:00 am: taps “Buy” on a ₹22,999 phone", "msg"),
     (1, 1, "checks exchange value of old phone: ₹4,000", "self"),
     (1, 2, "bank offer: ₹2,000 off on 6-month EMI", "msg"),
     (2, 1, "EMI approved, ₹16,999 on the card", "money"),
     (1, 3, "order to the seller’s stock in Ekart’s warehouse", "msg"),
     (3, 4, "packed within hours", "msg"),
     (4, 0, "delivered in 2 days; picks up the old phone", "msg"),
     (4, 5, "old phone handed to the refurbisher", "msg"),
     (5, 1, "₹4,000 credit settled", "money"),
     (1, 3, "₹22,999 − fees − ₹2,000 bank share, weekly", "money")],
    note="A sale-day phone is a bundle of four deals: the bank’s EMI discount, the exchange, the seller’s price and Flipkart’s delivery.")

FIGS["flow_myntra"] = seq(
    [("Aditi", "Pune, 24", "user"), ("Myntra app", "search, size, M-Now", "app"), ("Brand seller", "owns stock", "merchant"),
     ("M-Now store", "city fashion store", "network"), ("Rider", "delivery", "partner"), ("Bank / UPI", "payment", "bank")],
    [(0, 1, "photo of a kurta seen on Instagram", "msg"),
     (1, 1, "visual search: 40 similar kurtas", "self"),
     (1, 0, "size hint: “runs small, most chose one size up”", "ret"),
     (0, 1, "orders ₹1,299 in L, 30-minute delivery", "msg"),
     (1, 5, "collect ₹1,299 by UPI", "msg"),
     (1, 3, "pick from the nearest M-Now store", "msg"),
     (3, 4, "packed in minutes, handed over", "msg"),
     (4, 0, "delivered in 30 minutes; it fits", "msg"),
     (2, 1, "brand’s ad slot on the search page, paid per click", "money"),
     (1, 2, "₹1,299 − fees, after the return window closes", "money")],
    note="The size hint is the cheapest return-cutting tool Myntra has: it acts before the order, not after.")

FIGS["flow_search"] = seq(
    [("Karan", "types a query", "user"), ("Google Search", "results page", "app"), ("Ad auction", "in ~0.1 s", "network"),
     ("Advertisers", "3 shoe shops", "merchant"), ("Shop’s site", "landing page", "partner")],
    [(0, 1, "“buy running shoes online”", "msg"),
     (1, 2, "query + location + device", "msg"),
     (2, 3, "which ads bid on this keyword?", "msg"),
     (3, 2, "bids: ₹40, ₹30, ₹25 a click", "ret"),
     (2, 2, "rank = bid × quality; price = just enough", "self"),
     (2, 1, "2 ads above the links, 1 below", "ret"),
     (1, 0, "results page with AI Overview + ads", "ret"),
     (0, 4, "clicks the ad of shop B", "msg"),
     (3, 1, "shop B pays ₹25 for that click", "money")],
    note="Google is paid only when Karan clicks, so it wants the ad he is most likely to click, not only the highest bid.")

FIGS["flow_rtb"] = seq(
    [("Priya", "opens a news app", "user"), ("News app", "publisher", "app"), ("SSP / exchange", "e.g. InMobi Exchange", "network"),
     ("DSPs", "bid for brands", "merchant"), ("Brand", "a shoe maker", "bank")],
    [(0, 1, "opens an article; an ad slot is empty", "msg"),
     (1, 2, "bid request: slot size, app, city, device", "msg"),
     (2, 3, "request sent to 20 DSPs at once", "msg"),
     (3, 3, "does this person fit a brand’s target?", "self"),
     (3, 2, "bids: $1.20, $0.90, $0.40 per 1,000 views", "ret"),
     (2, 1, "winner’s ad, ~100 ms after the request", "ret"),
     (1, 0, "ad shown with the article", "msg"),
     (4, 3, "pays DSP for the view", "money"),
     (3, 2, "DSP pays exchange, keeps ~15%", "money"),
     (2, 1, "exchange pays app, keeps ~15%", "money")],
    note="Real-time bidding: an auction per ad slot, finished before the page has loaded. Middlemen keep a cut at every hop.")

FIGS["myntra_mix"] = hbars([("Logistics fees", 2919, "48%: storing and shipping for sellers"),
                            ("Marketplace fees", 2052, "34%: commission and listing"),
                            ("Advertising", 915, "15%, up 28% in a year"),
                            ("Other", 157, "3%")], 2919, lw=118, unit=" Cr", fmt="₹{:,}",
                           colors=["#2f6ea5", "#0b5d7a", "#127a64", "#9aa3ad"])

# ---------- loop (flywheel) ----------
def loop(nodes, centre, cx=340, cy=118, rx=250, ry=86, bw=150, bh=40, h=240, side=None, colors=None):
    """nodes: list of 'line1|line2' placed clockwise from the top; arrows between consecutive nodes."""
    n = len(nodes); o = ['<defs><marker id="lpa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#0b5d7a"/></marker></defs>']
    pts = [(cx + rx * math.sin(2 * math.pi * i / n), cy - ry * math.cos(2 * math.pi * i / n)) for i in range(n)]
    for i in range(n):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % n]
        a1 = 2 * math.pi * (i + 0.28) / n; a2 = 2 * math.pi * (i + 0.72) / n
        sx, sy = cx + rx * math.sin(a1), cy - ry * math.cos(a1); ex, ey = cx + rx * math.sin(a2), cy - ry * math.cos(a2)
        o.append(f'<path d="M{sx:.1f},{sy:.1f} A{rx},{ry} 0 0 1 {ex:.1f},{ey:.1f}" fill="none" stroke="#0b5d7a" stroke-width="2" marker-end="url(#lpa)"/>')
    for i, ((x, y), lab) in enumerate(zip(pts, nodes)):
        col = (colors or {}).get(i, ("#e3f0f5", "#0b5d7a"))
        o.append(f'<rect x="{x - bw/2:.1f}" y="{y - bh/2:.1f}" width="{bw}" height="{bh}" rx="6" fill="{col[0]}" stroke="{col[1]}" stroke-width="1.3"/>')
        ls = lab.split("|"); y0 = y - (len(ls) - 1) * 6.5 + 4
        for j, l in enumerate(ls): o.append(T(x, y0 + j * 13, l, "b" if j == 0 else "s", "middle"))
    for j, l in enumerate(centre.split("|")): o.append(T(cx, cy - (centre.count("|")) * 7 + 4 + j * 14, l, "b acc" if j == 0 else "s", "middle"))
    if side: o.append(lines(4, h - 26, side, "s", "start", 13))
    return svg(h, o)

FIGS["loop_amazon"] = loop(["More selection|sellers list more items", "Better experience|find it, next-day delivery",
                            "More shoppers|and more Prime members", "More sellers join|to reach those shoppers",
                            "Lower cost per order|fuller trucks, ads pay", "Lower prices|and more free delivery"],
                           "Amazon’s flywheel|each step feeds the next;|no single push needed", h=222, ry=82, cy=110)
FIGS["loop_flipkart"] = loop(["Sale-day big purchase|phone on EMI + exchange", "Good delivery|trust earned",
                              "Comes back|for fashion, home", "Credit and offers|Pay Later, co-branded card"],
                             "Flipkart’s loop|the sale buys the first|order; credit brings the next", h=206, rx=220, ry=74, cy=104, bw=168)
FIGS["loop_google"] = loop(["People search|14 bn times a day", "Better results|learned from clicks",
                            "Advertisers bid|on the intent", "Money for AI and|data centres, Android, Chrome"],
                           "Google’s loop|searches teach the ranking;|intent pays for everything", h=206, rx=220, ry=74, cy=104, bw=176)

# ---------- positioning 2x2 ----------
def two_by_two(xlab, ylab, quads, points, h=300):
    L, R, Tp, B = 70, 670, 14, h - 34
    mx, my = (L + R) / 2, (Tp + B) / 2
    o = [f'<rect x="{L}" y="{Tp}" width="{R-L}" height="{B-Tp}" fill="#fafbfc" stroke="#c3cad2"/>',
         f'<line x1="{mx}" y1="{Tp}" x2="{mx}" y2="{B}" stroke="#c3cad2"/><line x1="{L}" y1="{my}" x2="{R}" y2="{my}" stroke="#c3cad2"/>']
    for (qx, qy), txt in zip([(L + 8, Tp + 16), (mx + 8, Tp + 16), (L + 8, my + 16), (mx + 8, my + 16)], quads):
        o.append(T(qx, qy, txt, "s i"))
    for name, x, y, col, anchor in points:
        px, py = L + x * (R - L), B - y * (B - Tp)
        o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="6" fill="{col}"/>')
        o.append(T(px + (10 if anchor == "start" else -10), py + 4, name, "b halo", anchor))
    o.append(T((L + R) / 2, h - 12, xlab, "b", "middle"))
    o.append(f'<text x="18" y="{my:.1f}" text-anchor="middle" class="b" transform="rotate(-90 18 {my:.1f})">{_E(ylab)}</text>')
    o.append(T(L, h - 12, "low", "s")); o.append(T(R, h - 12, "high", "s", "end"))
    return svg(h, o)

FIGS["pos2x2"] = two_by_two("Share of profit that comes from ads (estimate)", "Breadth: how much people come for",
    ["everything, earns on goods and fees", "everything, ads pay the bills", "narrow, earns on goods", "narrow, ads pay the bills"],
    [("Flipkart", 0.30, 0.78, "#2f6ea5", "start"), ("Amazon India", 0.52, 0.86, "#c47f17", "start"),
     ("Meesho", 0.40, 0.62, "#7c3aa6", "start"), ("Myntra", 0.38, 0.24, "#b93a32", "start"),
     ("Google Search", 0.93, 0.92, "#127a64", "end"), ("InMobi", 0.90, 0.40, "#3e4fb8", "end"), ("Media.net", 0.86, 0.22, "#6b6a52", "end")], h=280)

FIGS["am_earn"] = hbars([("Referral fee", 420, "~12% of ₹3,499, paid by the seller"),
                         ("Fulfilment + closing", 120, "storing, packing, shipping the box"),
                         ("Prime fee share", 62, "₹1,499 ÷ ~24 orders a year"),
                         ("Ad click", 45, "the seller’s bid for the top slot")], 420, lw=150, fmt="₹{:,}",
                        colors=["#0b5d7a", "#2f6ea5", "#7c3aa6", "#127a64"])

FIGS["wf_adtax"] = waterfall([
    ("brand|spends", 100, "start"), ("agency,|DSP", 20, "down"), ("data,|checks", 10, "down"),
    ("exchange,|SSP", 15, "down"), ("unex-|plained", 4, "down"), ("app or|site gets", 0, "total")],
    unit="", suffix="¢", note="One dollar of open-web ad spend, in cents|(illustrative)", vw=330, top=40, h=212)
