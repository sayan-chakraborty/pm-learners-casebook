"""Teardown figures for M4; imported at the end of m4_figs.py (shares its helpers and FIGS)."""
from m4_figs import FIGS, seq, hbars, loop, svg, T  # noqa: F401

FIGS["flow_uber"] = seq(
    [("Ananya", "rider app", "user"), ("Uber pricing", "fare, surge", "app"), ("Dispatch", "matching", "app"),
     ("Driver app", "Suresh, Dzire", "partner"), ("Maps", "route, ETA", "network"), ("UPI / bank", "payment", "bank")],
    [(0, 1, "Bellandur → Jayanagar, UberGo", "msg"),
     (1, 4, "route + traffic now?", "msg"),
     (4, 1, "14 km, 48 min", "ret"),
     (1, 1, "requests 2× free cars nearby → 1.8× surge", "self"),
     (1, 0, "upfront fare ₹610, fixed", "ret"),
     (0, 2, "confirm", "msg"),
     (2, 2, "rank drivers by pickup ETA, rating; 15 s to accept", "self"),
     (2, 3, "offer: pickup 1.2 km, drop area shown", "msg"),
     (3, 2, "accept", "ret"),
     (2, 0, "driver, plate, 4-digit PIN, ETA 6 min", "ret"),
     (3, 3, "arrives; Ananya says the PIN; trip starts", "self"),
     (0, 5, "₹610 by UPI at the end", "msg"),
     (5, 1, "₹610 to Uber", "money"),
     (1, 3, "₹488 (80%) in the weekly payout", "money")],
    note="Surge doubles as a message to drivers: “come to Bellandur”. The PIN stops wrong-car pickups.")

FIGS["uber_earn"] = hbars([("Gross bookings", 58.0, "   everything riders and eaters paid"),
                           ("Revenue", 14.2, "   Uber’s share, about 24%"),
                           ("Adjusted EBITDA", 2.8, "   profit before interest, tax, depreciation")], 58.0, lw=130, unit=" bn",
                          fmt="${:,.1f}", colors=["#9aa3ad", "#0b5d7a", "#127a64"], note="Uber worldwide, April–June 2026")

FIGS["loop_uber"] = loop(["More riders|demand in every area", "More drivers online|earnings per hour rise",
                          "Shorter pickup ETAs|a car is always near", "Higher utilisation|less empty driving",
                          "Steadier fares|fewer cancellations"],
                         "Liquidity loop|density makes every|trip cheaper to serve", h=214, rx=240, ry=76, cy=106, bw=168)

FIGS["flow_ola"] = seq(
    [("Ravi", "rider app", "user"), ("Ola app", "booking", "app"), ("Ola Maps", "own map, 2024", "network"),
     ("Auto driver", "on a daily plan", "partner"), ("UPI", "payment", "bank")],
    [(0, 1, "auto, Koramangala → MG Road", "msg"),
     (1, 2, "route, fare estimate", "msg"),
     (2, 1, "6 km, ₹120, 22 min", "ret"),
     (1, 3, "offer: pickup 800 m", "msg"),
     (3, 1, "accept", "ret"),
     (1, 0, "driver, OTP, ETA 4 min", "ret"),
     (0, 4, "pays ₹120 at the end", "msg"),
     (4, 3, "₹120 straight to the driver", "money"),
     (3, 1, "once a day: flat platform fee", "money")],
    note="Under zero commission Ola earns per driver-day, not per ride; its own map removed the per-call maps bill.")

FIGS["loop_ola"] = loop(["Drivers leave|payout complaints", "Longer ETAs|more cancellations",
                         "Riders leave|try Uber, Rapido", "Fewer trips|lower earnings per hour"],
                        "The flywheel in reverse|a two-sided market|shrinks as fast as it grows", h=204, rx=220, ry=72, cy=102, bw=168,
                        colors={i: ("#fcecea", "#b93a32") for i in range(4)})

FIGS["flow_rapido"] = seq(
    [("Priya", "commuter", "user"), ("Rapido app", "booking", "app"), ("Captain", "own bike", "partner"),
     ("UPI", "payment", "bank"), ("Rapido plan", "driver’s pass", "network")],
    [(0, 1, "bike, Silk Board → Koramangala, ₹85", "msg"),
     (1, 1, "nearest free captains within ~1 km", "self"),
     (1, 2, "offer: pickup 600 m, drop shown", "msg"),
     (2, 1, "accept", "ret"),
     (1, 0, "captain, plate, OTP, spare helmet", "ret"),
     (2, 0, "20-minute ride through traffic", "msg"),
     (0, 3, "scans captain’s UPI QR: ₹85", "msg"),
     (3, 2, "₹85, all of it", "money"),
     (2, 4, "flat daily pass, however many rides", "money")],
    note="A cab would take 50 minutes and ₹400. Time saved, not the fare, is why bike taxis win at Silk Board.")

_rungs = [("Bike taxi (2015)", "the wedge", "#c47f17"), ("Autos", "same riders", "#b8741a"),
          ("Cabs", "families, airports", "#0b5d7a"), ("Parcels", "off-peak work", "#2f6ea5"),
          ("Food (Ownly)", "vs Zomato, Swiggy", "#127a64")]
FIGS["ladder_rapido"] = svg(150, [T(8, 14, "Rapido’s product ladder: each step reuses the same app, riders and captains", "s"),
                                  T(8, 30, "Each rung raises trips per rider, or keeps captains busy in quiet hours.", "b acc")] + [
    f'<rect x="{8 + i*134}" y="{104 - i*16}" width="126" height="{42 + i*16}" rx="5" fill="{c}"/>'
    + T(8 + i*134 + 63, 104 - i*16 + 18, a, "b w", "middle") + T(8 + i*134 + 63, 104 - i*16 + 32, b, "w", "middle")
    for i, (a, b, c) in enumerate(_rungs)])

FIGS["flow_maps"] = seq(
    [("Other phones", "millions, anonymous", "user"), ("Traffic model", "live + history", "network"), ("Google Maps", "routing", "app"),
     ("Meera’s phone", "driving", "user"), ("Businesses", "places, ads", "merchant")],
    [(0, 1, "speed + location pings, anonymised", "msg"),
     (1, 1, "speed on each road segment: now, usual", "self"),
     (3, 2, "Indiranagar → airport, now", "msg"),
     (2, 1, "predicted speeds, next 60 min", "msg"),
     (1, 2, "segment speeds", "ret"),
     (2, 3, "3 routes; fastest 52 min via ORR", "ret"),
     (3, 2, "location every few seconds", "msg"),
     (0, 2, "crash reported on Hebbal flyover", "msg"),
     (2, 3, "reroute: saves 9 min", "ret"),
     (4, 2, "pays for a promoted pin", "money"),
     (2, 3, "café on the route, labelled Ad", "ret")],
    note="Every driver is both a user and a sensor: the ETA gets better as more people use it.")

FIGS["loop_maps"] = loop(["More people navigate|2 bn+ monthly users", "More traffic, place data|speeds, reviews, photos",
                          "Better ETAs and results|people trust it", "Businesses pay|ads, listings, API use"],
                         "Maps’ data loop|users are the sensors|that make it better", h=204, rx=220, ry=72, cy=102, bw=178)

FIGS["flow_mmt"] = seq(
    [("Rohit", "traveller", "user"), ("MakeMyTrip", "app", "app"), ("Airlines", "via GDS / APIs", "network"),
     ("Goa hotel", "via extranet", "partner"), ("Bank / UPI", "payment", "bank")],
    [(0, 1, "Mumbai → Goa, 12 Dec, 2 adults", "msg"),
     (1, 2, "fares and seats, 30+ flights", "msg"),
     (2, 1, "cheapest ₹5,400 each", "ret"),
     (0, 1, "picks IndiGo 7:10 am", "msg"),
     (1, 4, "₹10,800 + ₹400 convenience fee", "msg"),
     (4, 1, "₹11,200", "money"),
     (1, 2, "book: ticket issued, PNR", "msg"),
     (1, 0, "“Add a hotel? 2 nights, ₹8,000”", "ret"),
     (0, 1, "yes, pays ₹8,000", "money"),
     (1, 3, "booking via the hotel’s extranet", "msg"),
     (1, 2, "₹10,800 to IndiGo", "money"),
     (1, 3, "₹6,600 after ~17% commission", "money")],
    note="The flight earned MMT about ₹400; the hotel about ₹1,400. The flight brought Rohit in.")

FIGS["mmt_seg"] = hbars([("Air ticketing", 13.4, ""), ("Hotels and packages", 15.7, ""), ("Bus (redBus)", 29.3, ""), ("Other", 37.1, "")], 40,
                        lw=150, unit="%", fmt="+{:.1f}", colors=["#2f6ea5", "#127a64", "#c47f17", "#7c3aa6"],
                        note="Growth in adjusted margin by segment, FY26 (to March 2026), constant currency")


def _pos2x2():
    L, R, Tp, B = 70, 670, 14, 222
    o = [f'<rect x="{L}" y="{Tp}" width="{R-L}" height="{B-Tp}" fill="#fafbfc" stroke="#c3cad2"/>',
         f'<line x1="{(L+R)/2}" y1="{Tp}" x2="{(L+R)/2}" y2="{B}" stroke="#c3cad2"/><line x1="{L}" y1="{(Tp+B)/2}" x2="{R}" y2="{(Tp+B)/2}" stroke="#c3cad2"/>']
    for (qx, qy), s in zip([(L + 8, Tp + 16), ((L+R)/2 + 8, Tp + 16), (L + 8, B - 8), ((L+R)/2 + 8, B - 8)],
                           ["rare but valuable: win each booking", "frequent and valuable (rare)", "rare and low value: hard", "habit, little per use: needs ads or fees"]):
        o.append(T(qx, qy, s, "s i"))
    for n, x, y, c, a in [("MakeMyTrip", 0.10, 0.86, "#7c3aa6", "start"), ("Uber (cabs)", 0.42, 0.64, "#1c232b", "start"),
                          ("Ola", 0.34, 0.46, "#127a64", "start"), ("Rapido (bikes)", 0.66, 0.34, "#c47f17", "start"),
                          ("Namma Yatri", 0.58, 0.22, "#5b6470", "start"), ("Google Maps", 0.95, 0.16, "#2f6ea5", "end")]:
        px, py = L + x * (R - L), B - y * (B - Tp)
        o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="6" fill="{c}"/>')
        o.append(T(px + (10 if a == "start" else -10), py + 4, n, "b halo", a))
    o.append(T((L + R) / 2, B + 22, "How often a typical user uses it (a few times a year → every day)", "b", "middle"))
    o.append(f'<text x="18" y="{(Tp+B)/2}" text-anchor="middle" class="b" transform="rotate(-90 18 {(Tp+B)/2})">Money kept per use</text>')
    return svg(252, o)


FIGS["pos2x2"] = _pos2x2()
