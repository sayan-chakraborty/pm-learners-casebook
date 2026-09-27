"""Generated SVGs for M2 ({{SVG:name}} in parts): teardown behind-the-screens sequence diagrams."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "common"))
from svgkit import seq as _seq  # noqa: E402
def seq(*a, **k):
    k.setdefault("row", 24)
    return _seq(*a, **k)

FIGS = {}

from html import escape as _E

def _lines(x, y, s, cls="", size=10.3, lh=12.5, anchor="middle"):
    return "".join(f'<text x="{x:.1f}" y="{y + i*lh:.1f}" text-anchor="{anchor}" class="{cls}" style="font-size:{size}px">{_E(t)}</text>'
                   for i, t in enumerate(s.split("|")))

def journey_orig():
    rows = [("Know what|I want to eat", ["Open the|app", "Search food,|restaurant or|past order", "See the|list of|items", "Add to|cart", "Checkout", "Make|payment", "Check|order|status", "Ratings", "Resolve|issue if|any"]),
            ("Buy|groceries", ["Open the|app", "Tap in|Instamart", "Search|for item", "Explore|categories|for what’s|new", "Search|for item", "Add to|cart", "Checkout", "Make|payment", "Check|order|status", "Resolve|issue if|any"]),
            ("Explore new|dishes", ["Open the|app", "Explore|the feed", "Select a|restaurant|or food|item", "Add to|cart", "Checkout", "Make|payment", "Check|order|status", "Ratings", "Resolve|issue if|any"])]
    o = ['<text x="4" y="13" class="b">User intent</text><text x="100" y="13" class="b">User journey (steps in order)</text>']
    y = 22; bh = 60
    for intent, steps in rows:
        o.append(f'<rect x="0" y="{y}" width="88" height="{bh}" rx="4" fill="#fde7c8" stroke="#c47f17"/>')
        n = intent.count("|") + 1
        o.append(_lines(44, y + bh/2 - (n-1)*6.25 + 4, intent, "b"))
        w = (680 - 96 - 3 * 9) / 10
        for i, st in enumerate(steps):
            x = 96 + i * (w + 3)
            o.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{bh}" rx="4" fill="#dbe8f5" stroke="#9fb3c8"/>')
            n = st.count("|") + 1
            o.append(_lines(x + w/2, y + bh/2 - (n-1)*6.25 + 4, st))
        y += bh + 8
    return f'<svg class="d" viewBox="0 0 680 {y}" xmlns="http://www.w3.org/2000/svg">' + "".join(o) + "</svg>"

FIGS["swj_orig"] = journey_orig()

def payback():
    X = lambda m: 60 + m * 24.2
    Y = lambda v: 196 - v * 0.25
    A = [(0,0),(1,75),(2,120),(3,158),(4,191),(5,223),(6,253),(7,281),(8,308),(9,334),(10,359),(11,383),(12,406),(15,470),(18,530),(21,585),(24,640)]
    B = [(0,0),(1,75),(2,105),(3,125),(4,140),(6,170),(9,205),(12,230),(18,270),(24,300)]
    o = []
    for v in (0, 200, 400, 600):
        o.append(f'<line x1="60" y1="{Y(v):.1f}" x2="646" y2="{Y(v):.1f}" stroke="#e3e7eb"/><text x="54" y="{Y(v)+4:.1f}" text-anchor="end" class="s">₹{v}</text>')
    for m in (0, 6, 12, 18, 24):
        o.append(f'<text x="{X(m):.1f}" y="212" text-anchor="middle" class="s">{m}</text>')
    o.append('<text x="353" y="228" text-anchor="middle" class="s">months since the customer’s first order</text>')
    o.append(f'<line x1="60" y1="{Y(400):.1f}" x2="646" y2="{Y(400):.1f}" stroke="#b93a32" stroke-width="1.6" stroke-dasharray="6 4"/>')
    o.append(f'<text x="64" y="{Y(400)-6:.1f}" class="b red">cost to acquire (CAC): ₹400</text>')
    pa = " ".join(f"{X(m):.1f},{Y(v):.1f}" for m, v in A); pb = " ".join(f"{X(m):.1f},{Y(v):.1f}" for m, v in B)
    o.append(f'<polyline points="{pa}" fill="none" stroke="#127a64" stroke-width="2.6"/>')
    o.append(f'<polyline points="{pb}" fill="none" stroke="#c47f17" stroke-width="2.6"/>')
    o.append(f'<circle cx="{X(12):.1f}" cy="{Y(406):.1f}" r="5" fill="#127a64"/>')
    o.append(f'<text x="{X(12)+8:.1f}" y="{Y(406)+18:.1f}" class="b grn">pays back in month 12</text>')
    o.append(f'<text x="{X(24)-4:.1f}" y="{Y(640)+16:.1f}" text-anchor="end" class="b grn">organic customer: ₹640 by month 24</text>')
    o.append(f'<text x="{X(24)-4:.1f}" y="{Y(300)+18:.1f}" text-anchor="end" class="b amb">bought with a big discount: ₹300, never pays back</text>')
    o.append(f'<text x="64" y="16" class="s">cumulative contribution from one customer: ₹25 per order × 3 orders a month × the share still ordering</text>')
    return '<svg class="d" viewBox="0 0 680 234" xmlns="http://www.w3.org/2000/svg">' + "".join(o) + "</svg>"

FIGS["payback"] = payback()

# ---------- teardown sequence flows ----------
FIGS["flow_zomato"] = seq(
    [("Kavya", "Zomato app", "user"), ("Zomato", "orders + payments", "app"), ("Restaurant", "biryani kitchen", "merchant"),
     ("Dispatch", "matching engine", "network"), ("Rider", "delivery partner", "partner"), ("Banks", "UPI, settlement", "bank")],
    [(0, 1, "biryani ₹450, pays ₹490", "msg"),
     (1, 5, "collect ₹490 by UPI", "msg"),
     (5, 1, "₹490 held by Zomato", "money"),
     (1, 2, "new order on the tablet", "msg"),
     (2, 1, "accepted, ready in 13 min", "ret"),
     (1, 3, "rider needed at 8:58 pm", "msg"),
     (3, 3, "scores riders: distance, batching, rating", "self"),
     (3, 4, "offer: ₹85 for 4 km", "msg"),
     (4, 3, "accepts", "ret"),
     (4, 2, "arrives, collects the bag", "msg"),
     (4, 0, "hands over with a PIN, 9:31 pm", "msg"),
     (5, 2, "₹360 in the weekly payout", "money"),
     (5, 4, "₹85 in the rider payout", "money")],
    note="₹505 comes in (₹490 from Kavya, ₹15 of ads); ₹445 goes out. Zomato runs the whole relay but cooks and rides nothing.")

FIGS["flow_blinkit"] = seq(
    [("Rohan", "Blinkit app", "user"), ("Blinkit", "app + inventory", "app"), ("Dark store", "1.8 km away", "merchant"),
     ("Rider", "waiting at store", "partner"), ("Warehouse", "city mother hub", "network"), ("Brand", "e.g. Amul", "bank")],
    [(0, 1, "milk + charger, pays ₹1,340", "msg"),
     (1, 1, "picks the nearest store with both in stock", "self"),
     (1, 2, "pick list: bin A4, bin F12", "msg"),
     (2, 2, "picked + packed in 2 min", "self"),
     (2, 3, "bag handed over", "msg"),
     (3, 0, "delivered, 11 min after paying", "msg"),
     (1, 1, "stock of milk falls below 40 packs", "self"),
     (1, 4, "refill order for tomorrow 5 am", "msg"),
     (4, 2, "truck: 300 packs of milk", "msg"),
     (1, 5, "pays for the stock it bought", "money")],
    note="Since Blinkit owns the stock (1P), step ⑩ is its money at risk: unsold milk is its loss.")

FIGS["flow_swiggy"] = seq(
    [("Neha", "Swiggy One member", "user"), ("Swiggy", "one app, one fleet", "app"), ("Restaurant", "dinner", "merchant"),
     ("Instamart pod", "dark store", "merchant"), ("Rider", "shared fleet", "partner"), ("Banks", "UPI", "bank")],
    [(0, 1, "dinner ₹380 (free delivery: One)", "msg"),
     (1, 5, "collect ₹392", "msg"),
     (5, 1, "₹392", "money"),
     (1, 2, "order to kitchen", "msg"),
     (1, 4, "pickup at 8:20, 2 km", "msg"),
     (4, 0, "dinner delivered 8:34", "msg"),
     (0, 1, "adds eggs, bread: ₹240", "msg"),
     (1, 3, "pick list", "msg"),
     (1, 4, "same rider, pod is 600 m away", "msg"),
     (4, 0, "groceries at 8:47", "msg"),
     (0, 1, "membership fee (quarterly)", "money")],
    note="One rider, one member, two businesses: the shared fleet and the One membership are what tie food to Instamart.")

FIGS["flow_zepto"] = seq(
    [("Ira", "Zepto app", "user"), ("Zepto", "app + ads", "app"), ("Dark store", "picking", "merchant"),
     ("Café counter", "inside the store", "merchant"), ("Rider", "at store", "partner"), ("Brand", "snack maker", "bank")],
    [(1, 0, "sponsored: new chips, top row", "msg"),
     (0, 1, "chips + cold coffee, ₹310", "msg"),
     (1, 2, "pick chips, bin C3", "msg"),
     (1, 3, "brew cold coffee", "msg"),
     (3, 2, "coffee ready in 3 min", "ret"),
     (2, 4, "one bag, both items", "msg"),
     (4, 0, "delivered, 9 min", "msg"),
     (5, 1, "ad fee for the top row", "money")],
    note="The café adds a high-margin item to a small basket; the ad pays Zepto before anything is sold.")

FIGS["flow_bb"] = seq(
    [("Mrs Iyer", "BigBasket app", "user"), ("BigBasket", "app", "app"), ("Warehouse", "city fulfilment centre", "network"),
     ("Van", "20 homes per trip", "partner"), ("Farmers", "collection centre", "merchant"), ("Tata Neu", "loyalty", "bank")],
    [(0, 1, "weekly basket ₹2,150, slot 7–9 am", "msg"),
     (1, 4, "tomorrow’s veg demand", "msg"),
     (4, 2, "graded vegetables, 4 am", "msg"),
     (1, 2, "pick list (night shift)", "msg"),
     (2, 3, "crates loaded by route", "msg"),
     (3, 0, "delivered 7:40 am", "msg"),
     (1, 5, "NeuCoins earned: 5%", "msg"),
     (0, 1, "pays ₹2,150 (or cash on delivery)", "money")],
    note="Scheduled slots let BigBasket buy fresh produce against known demand and fill a van with 20 orders on one route.")

FIGS["flow_ondc"] = seq(
    [("Sameer", "magicpin app", "user"), ("magicpin", "buyer app", "app"), ("ONDC", "gateway + rules", "network"),
     ("Seller app", "restaurant’s tech", "partner"), ("Restaurant", "local kitchen", "merchant"), ("Logistics", "e.g. rider network", "bank")],
    [(0, 1, "search “paneer roll near me”", "msg"),
     (1, 2, "search request", "msg"),
     (2, 3, "broadcast to seller apps", "msg"),
     (3, 1, "menus + prices", "ret"),
     (0, 1, "orders ₹240, pays", "money"),
     (1, 3, "confirmed order (same protocol)", "msg"),
     (3, 4, "order to kitchen", "msg"),
     (3, 5, "book a rider", "msg"),
     (5, 0, "delivered", "msg"),
     (1, 4, "₹240 minus small fees, settled", "money")],
    note="No single company owns the customer, the restaurant and the rider: each role is a separate app speaking one open protocol.")

FIGS["flow_track"] = seq(
    [("Rider app", "phone GPS", "partner"), ("Location service", "receives pings", "app"), ("Queue", "event stream", "network"),
     ("Latest-location store", "in memory", "bank"), ("ETA service", "maps + history", "app"), ("Kavya’s app", "map screen", "user")],
    [(0, 1, "GPS point, every 4 s", "msg"),
     (1, 2, "location event", "msg"),
     (2, 3, "overwrite rider’s latest point", "msg"),
     (2, 4, "same event", "msg"),
     (4, 4, "recompute arrival: 7 min", "self"),
     (3, 5, "push new dot (open connection)", "msg"),
     (4, 5, "push “arrives 9:04 pm”", "msg"),
     (5, 5, "animates the dot between points", "self")],
    note="The order database is never touched: 75,000 pings a second go to a queue and a fast in-memory store instead.")
