"""Technology figures for M4 (cloud + System design III); imported at the end of m4_figs.py."""
from m4_figs import FIGS, svg, T, lines  # noqa: F401

YOU, PRO = ("#fbf4e6", "#c47f17"), ("#e3f0f5", "#0b5d7a")
ARW = ('<defs><marker id="ta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
       '<path d="M0,0 L10,5 L0,10 z" fill="#4a5563"/></marker>'
       '<marker id="tr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
       '<path d="M0,0 L10,5 L0,10 z" fill="#b93a32"/></marker></defs>')


def arrow(x1, y1, x2, y2, red=False, w=1.5, dash=False):
    d = ' stroke-dasharray="4 3"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{"#b93a32" if red else "#4a5563"}" stroke-width="{w}"{d} '
            f'marker-end="url(#{"tr" if red else "ta"})"/>')


def box(x, y, w, h, fill, st, txt, cls="b", sw=1.3, lh=13):
    ls = txt.split("|"); y0 = y + h / 2 - (len(ls) - 1) * lh / 2 + 4
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{st}" stroke-width="{sw}"/>'
            + "".join(T(x + w / 2, y0 + i * lh, l, cls if i == 0 else "", "middle") for i, l in enumerate(ls)))


# ---------- IaaS / PaaS / SaaS ----------
def pizza():
    cols = [("On-premises", "make it at home", 7, "own data centre"), ("IaaS", "take and bake", 4, "AWS EC2, Azure VMs"),
            ("PaaS", "delivered", 2, "App Engine, Heroku"), ("SaaS", "dine out", 0, "Gmail, Zoho, Slack")]
    layers = ["Your app’s features", "Your data", "Runtime, scaling", "Operating system", "Servers", "Storage, network", "Building, power, cooling"]
    o = ['<g class="c">']; x0 = 120; cw = 136
    for i, l in enumerate(layers): o.append(T(x0 - 8, 58 + i * 20, l, "", "end"))
    for j, (h, s, you, ex) in enumerate(cols):
        x = x0 + j * (cw + 4)
        o.append(T(x + cw / 2, 14, h, "b", "middle")); o.append(T(x + cw / 2, 28, s, "s", "middle"))
        for i in range(len(layers)):
            mine = i < you if j else True
            if j == 3: mine = False
            f, st = YOU if mine else PRO
            o.append(f'<rect x="{x}" y="{44 + i * 20}" width="{cw}" height="18" fill="{f}" stroke="{st}"/>')
        o.append(T(x + cw / 2, 200, ex, "s", "middle"))
    o.append(f'<rect x="{x0}" y="210" width="12" height="10" fill="{YOU[0]}" stroke="{YOU[1]}"/>'); o.append(T(x0 + 18, 219, "you run it", ""))
    o.append(f'<rect x="{x0 + 110}" y="210" width="12" height="10" fill="{PRO[0]}" stroke="{PRO[1]}"/>'); o.append(T(x0 + 128, 219, "the cloud provider runs it", ""))
    o.append("</g>")
    return svg(226, o)


FIGS["pizza"] = pizza()


# ---------- buying cloud: reserved + on-demand + spot ----------
def cost_mix():
    L, R, Tp, B = 44, 420, 20, 180
    X = lambda h: L + (R - L) * h / 24; Y = lambda s: B - (B - Tp) * s / 110
    demand = [30, 26, 24, 24, 26, 32, 45, 62, 80, 88, 76, 64, 60, 58, 56, 60, 70, 88, 100, 96, 80, 62, 48, 36, 30]
    o = [f'<line x1="{L}" y1="{B}" x2="{R}" y2="{B}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{B}" stroke="#4a5563"/>']
    o.append(f'<rect x="{L}" y="{Y(40):.1f}" width="{R-L}" height="{B-Y(40):.1f}" fill="#e3f0f5"/>')
    pts = " ".join(f"{X(h):.1f},{Y(max(d, 40)):.1f}" for h, d in enumerate(demand))
    o.append(f'<polygon points="{X(0):.1f},{Y(40):.1f} {pts} {X(24):.1f},{Y(40):.1f}" fill="#fbf4e6" stroke="none"/>')
    o.append(f'<polyline points="{" ".join(f"{X(h):.1f},{Y(d):.1f}" for h, d in enumerate(demand))}" fill="none" stroke="#1c232b" stroke-width="2"/>')
    o.append(f'<rect x="{X(1):.1f}" y="{Y(40) - 26:.1f}" width="{X(5) - X(1):.1f}" height="22" fill="#e7f4f0" stroke="#127a64" stroke-dasharray="3 2"/>')
    o.append(T(X(3), Y(40) - 11, "spot: retrain", "s", "middle"))
    for v in (0, 40, 100): o.append(T(L - 5, Y(v) + 4, str(v), "s", "end"))
    for h in (0, 6, 12, 18, 24): o.append(T(X(h), B + 14, f"{h:02d}:00", "s", "middle"))
    o.append(T(L, 12, "servers needed across a day", "s"))
    o.append(T(X(12), Y(20) + 4, "reserved: 40 servers, all day", "b acc", "middle"))
    o.append(T(X(12.5), Y(50), "on-demand for peaks", "b amb", "middle"))
    nx = 440
    rows = [("All on-demand, 100 servers 24×7", "b"), ("100 × ₹20 × 720 h = ₹14.4 lakh/month", ""), ("", ""),
            ("Mixed, as in the chart", "b grn"), ("Reserved 40 × ₹12 × 720 = ₹3.46 lakh", ""), ("On-demand peaks ≈ 60 × ₹20 × 4 h × 30", ""),
            ("                        = ₹1.44 lakh", ""), ("Spot retraining 100 h × ₹6 × 30 = ₹0.18 lakh", ""), ("Total ≈ ₹5.1 lakh: about 65% less", "b grn")]
    for i, (s, c) in enumerate(rows): o.append(T(nx, 24 + i * 15, s, c))
    return svg(196, o)


FIGS["costmix"] = cost_mix()


# ---------- vertical vs horizontal scaling ----------
def scaling():
    o = [ARW, '<g class="c">']
    o.append(T(0, 14, "Vertical: a bigger machine", "b"))
    o.append(box(10, 60, 60, 44, *PRO, "8 cores"))
    o.append(arrow(78, 82, 118, 82))
    o.append(box(126, 28, 120, 110, *PRO, "64 cores|one machine"))
    for i, s in enumerate(["+ simple: no code change", "− a ceiling: the biggest box", "− one failure takes all down", "− downtime to upgrade"]):
        o.append(T(10, 158 + i * 14, s, "grn" if s[0] == "+" else "red"))
    o.append(T(350, 14, "Horizontal: more machines", "b"))
    o.append(box(350, 60, 60, 44, *PRO, "8 cores"))
    o.append(arrow(418, 82, 458, 82))
    for r in range(3):
        for c in range(3):
            o.append(box(466 + c * 70, 26 + r * 40, 62, 34, *PRO, "8 cores"))
    for i, s in enumerate(["+ no ceiling; add or remove any time", "+ one box fails, the rest carry on", "− the service must be stateless", "− needs a load balancer, more to watch"]):
        o.append(T(350, 158 + i * 14, s, "grn" if s[0] == "+" else "red"))
    o.append("</g>")
    return svg(212, o)


FIGS["scaling"] = scaling()


# ---------- load balancer ----------
def lb():
    o = [ARW, '<g class="c">']
    o.append(box(0, 70, 120, 56, "#e1f2ec", "#127a64", "Riders’ phones|50,000 requests/s"))
    o.append(arrow(122, 98, 196, 98, w=2))
    o.append(box(200, 60, 140, 76, "#fde7c8", "#c47f17", "Load balancer|spreads requests;|checks health every 5 s"))
    ys = [6, 52, 98, 144]
    for i, y in enumerate(ys):
        bad = i == 2
        o.append(box(470, y, 150, 40, "#fcecea" if bad else PRO[0], "#b93a32" if bad else PRO[1], ("Server 3: not responding" if bad else f"Server {i + 1 if i < 2 else 4}") + ("|removed from rotation" if bad else "|~16,700 req/s")))
        o.append(arrow(342, 98, 466, y + 20, red=bad, dash=bad))
    o.append(T(350, 196, "Health check fails → no new traffic to server 3; the other three share its load.", "s"))
    o.append("</g>")
    return svg(204, o)


FIGS["lb"] = lb()


# ---------- autoscaling lag ----------
def autoscale():
    L, R, Tp, B = 50, 470, 18, 176
    X = lambda m: L + (R - L) * (m + 60) / 120; Y = lambda v: B - (B - Tp) * v / 150
    dem = [(-60, 20), (-30, 24), (-15, 30), (-5, 60), (0, 140), (10, 120), (25, 70), (40, 40), (60, 30)]
    cap = [(-60, 30), (-5, 30), (0, 30), (4, 30), (4, 60), (8, 60), (8, 110), (12, 110), (12, 150), (60, 150)]
    pre = [(-60, 30), (-40, 30), (-40, 150), (60, 150)]
    o = [f'<line x1="{L}" y1="{B}" x2="{R}" y2="{B}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{B}" stroke="#4a5563"/>']
    # gap shading between demand and reactive capacity from -5 to 12
    o.append(f'<polygon points="{X(-5):.1f},{Y(60):.1f} {X(0):.1f},{Y(140):.1f} {X(10):.1f},{Y(120):.1f} {X(12):.1f},{Y(113):.1f} {X(12):.1f},{Y(110):.1f} {X(8):.1f},{Y(110):.1f} {X(8):.1f},{Y(60):.1f} {X(4):.1f},{Y(60):.1f} {X(4):.1f},{Y(30):.1f} {X(-5):.1f},{Y(30):.1f}" fill="#fcecea"/>')
    o.append(f'<polyline points="{" ".join(f"{X(m):.1f},{Y(v):.1f}" for m, v in dem)}" fill="none" stroke="#1c232b" stroke-width="2.2"/>')
    o.append(f'<polyline points="{" ".join(f"{X(m):.1f},{Y(v):.1f}" for m, v in cap)}" fill="none" stroke="#b93a32" stroke-width="2"/>')
    o.append(f'<polyline points="{" ".join(f"{X(m):.1f},{Y(v):.1f}" for m, v in pre)}" fill="none" stroke="#127a64" stroke-width="2" stroke-dasharray="5 3"/>')
    for m, s in [(-60, "11:00"), (-30, "11:30"), (0, "midnight"), (30, "12:30"), (60, "1:00")]: o.append(T(X(m), B + 14, s, "s", "middle"))
    for v in (0, 50, 100, 150): o.append(T(L - 5, Y(v) + 4, str(v), "s", "end"))
    o.append(T(L, 11, "servers needed (black) vs servers running; New Year’s Eve", "s"))
    o.append(T(X(42), Y(52), "demand", "b halo"))
    o.append(T(X(14), Y(98), "reactive autoscaling", "b red halo"))
    o.append(T(X(14), Y(84), "adds servers in 4-min steps", "red halo"))
    o.append(T(X(-38) + 5, Y(150) + 14, "scheduled: scale up at 11:20 pm", "b grn halo"))
    o.append(T(X(-3), Y(42), "requests fail", "b red", "end"))
    nx = 488
    for i, (s, c) in enumerate([("Sizing the peak", "b"), ("50,000 req/s ÷ 500 per server", ""), ("= 100 servers", ""), ("× 1.3 headroom = 130", "b"),
                                ("", ""), ("Why react late?", "b red"), ("a new server takes 3–5 min", ""), ("to boot and warm up; the", ""), ("spike takes 5 min to arrive", ""),
                                ("", ""), ("Fix: scale on a schedule", "b grn"), ("for known peaks; keep a", ""), ("warm pool for surprises", "")]):
        o.append(T(nx, 24 + i * 13.5, s, c))
    return svg(198, o)


FIGS["autoscale"] = autoscale()


# ---------- CAP per feature ----------
def cap():
    o = ['<g class="c">']
    o.append(T(0, 14, "A network split: the Bengaluru and Chennai data centres can’t talk for 30 seconds. Each feature must choose:", "s"))
    o.append(f'<rect x="0" y="24" width="334" height="170" rx="8" fill="#eef0fb" stroke="#3e4fb8"/>')
    o.append(T(12, 44, "Stay correct (consistency)", "b fwc")); o.append(T(12, 58, "refuse or wait rather than give a wrong answer", "s"))
    for i, (a, b) in enumerate([("Assign a driver to a ride", "never two rides for one driver"), ("Charge the rider, pay the driver", "no double charge, no lost ₹"),
                                ("Apply a one-time coupon", "used once, not twice")]):
        o.append(f'<rect x="12" y="{68 + i * 40}" width="310" height="34" rx="5" fill="#fff" stroke="#c3cad2"/>')
        o.append(T(22, 82 + i * 40, a, "b")); o.append(T(22, 95 + i * 40, b, "s"))
    o.append(f'<rect x="346" y="24" width="334" height="170" rx="8" fill="#e7f4f0" stroke="#127a64"/>')
    o.append(T(358, 44, "Stay up (availability)", "b grn")); o.append(T(358, 58, "answer now, even if a few seconds out of date", "s"))
    for i, (a, b) in enumerate([("Cars near you on the map", "a 10-second-old position is fine"), ("ETA and fare estimate", "slightly stale beats a blank screen"),
                                ("Ratings, trip history, promos", "can catch up in a minute")]):
        o.append(f'<rect x="358" y="{68 + i * 40}" width="310" height="34" rx="5" fill="#fff" stroke="#c3cad2"/>')
        o.append(T(368, 82 + i * 40, a, "b")); o.append(T(368, 95 + i * 40, b, "s"))
    o.append("</g>")
    return svg(198, o)


FIGS["cap"] = cap()


# ---------- error budget burn-down ----------
def budget():
    L, R, Tp, B = 50, 450, 18, 170
    X = lambda d: L + (R - L) * d / 30; Y = lambda m: B - (B - Tp) * m / 45
    pts = [(0, 43.2), (6, 41), (6.1, 21), (18, 18), (18.1, 6), (22, 5), (30, 3)]
    o = [f'<line x1="{L}" y1="{B}" x2="{R}" y2="{B}" stroke="#4a5563"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{B}" stroke="#4a5563"/>']
    o.append(f'<rect x="{L}" y="{Y(10.8):.1f}" width="{R-L}" height="{B - Y(10.8):.1f}" fill="#fcecea"/>')
    o.append(T(R - 4, Y(10.8) + 13, "below 25% left: freeze feature releases", "b red", "end"))
    o.append(f'<polyline points="{" ".join(f"{X(d):.1f},{Y(m):.1f}" for d, m in pts)}" fill="none" stroke="#0b5d7a" stroke-width="2.5"/>')
    for d in (0, 10, 20, 30): o.append(T(X(d), B + 14, f"day {d}", "s", "middle"))
    for m in (0, 20, 43.2): o.append(T(L - 5, Y(m) + 4, f"{m:g}", "s", "end"))
    o.append(T(L, 11, "minutes of failure left this month (SLO 99.9%)", "s"))
    o.append(T(X(6.4), Y(30), "day 6: bad release,", "b halo")); o.append(T(X(6.4), Y(30) + 13, "20 min of failed bookings", "halo"))
    o.append(T(X(18.4), Y(22), "day 18: rain spike, 12 min", "b halo"))
    nx = 468
    for i, (s, c) in enumerate([("The arithmetic", "b"), ("30 days × 24 h × 60 min", ""), ("= 43,200 minutes", ""), ("0.1% of that = 43.2 min", "b"),
                                ("", ""), ("One bad release used", ""), ("20 ÷ 43.2 = 46%", "b red"), ("of the month’s budget", ""),
                                ("", ""), ("Budget left → ship fast;", "grn"), ("budget gone → fix first", "red")]):
        o.append(T(nx, 24 + i * 13.5, s, c))
    return svg(190, o)


FIGS["budget"] = budget()


# ---------- graceful degradation ladder ----------
def degrade():
    steps = [("Normal", "everything on", "#127a64"), ("Load 120%", "switch off promos,|recommendations", "#5b9c6e"),
             ("Load 150%", "cached ETAs|and fares,|≤ 60 s old", "#c47f17"), ("Load 200%", "simpler matching:|nearest driver only", "#d0782a"),
             ("Load 300%", "queue requests:|“about 3 min”", "#b93a32"), ("Last resort", "pause bookings in|the worst zones", "#8e2b25")]
    o = ['<g class="c">']; w = 108
    for i, (a, b, c) in enumerate(steps):
        x = i * (w + 6); y = 20 + i * 18; h = 150 - i * 18
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{c}"/>')
        o.append(T(x + w / 2, y + 18, a, "b w", "middle"))
        o.append(lines(x + w / 2, y + 36, b, "w", "middle", 13))
    o.append(T(0, 12, "Each step keeps the core job (get a rider a car) working by giving up something less important. Each is a switch built in advance.", "s"))
    o.append("</g>")
    return svg(176, o)


FIGS["degrade"] = degrade()


# ---------- retry storm and circuit breaker ----------
def breaker():
    o = [ARW, '<g class="c">']
    o.append(T(0, 14, "Retry storm: the pricing service slows down", "b"))
    bars = [("normal", 10, "#0b5d7a"), ("+ 1 retry", 20, "#c47f17"), ("+ 3 retries", 40, "#b93a32")]
    for i, (a, v, c) in enumerate(bars):
        y = 30 + i * 34
        o.append(T(80, y + 16, a, "b", "end"))
        o.append(f'<rect x="88" y="{y}" width="{v * 4.8}" height="22" fill="{c}" rx="2"/>')
        o.append(T(94 + v * 4.8, y + 16, f"{v},000 req/s", "b"))
    o.append(T(0, 148, "Every caller retrying 3 times turns 10,000 requests", "s")); o.append(T(0, 162, "into 40,000 at the moment the service is weakest.", "s"))
    o.append(T(0, 180, "Fix: back off (wait 1 s, 2 s, 4 s, plus randomness)", "b grn"))
    x0 = 350
    o.append(T(x0, 14, "Circuit breaker: stop calling a failing service", "b"))
    o.append(box(x0, 40, 120, 50, "#e7f4f0", "#127a64", "Closed|calls go through"))
    o.append(box(x0 + 180, 40, 120, 50, "#fcecea", "#b93a32", "Open|fail fast, use fallback"))
    o.append(box(x0 + 90, 130, 120, 50, "#fbf4e6", "#c47f17", "Half-open|try a few calls"))
    o.append(arrow(x0 + 122, 56, x0 + 178, 56)); o.append(T(x0 + 150, 50, "50% fail", "s halo", "middle"))
    o.append(arrow(x0 + 250, 92, x0 + 190, 128)); o.append(T(x0 + 226, 118, "after 30 s", "s halo"))
    o.append(arrow(x0 + 120, 128, x0 + 70, 92)); o.append(T(x0 + 104, 112, "they work", "s halo"))
    o.append(T(x0, 198, "Fallback while open: last known fare, marked “estimate”.", "s"))
    o.append("</g>")
    return svg(206, o)


FIGS["breaker"] = breaker()


# ---------- monolith vs microservices ----------
def micro():
    o = [ARW, '<g class="c">']
    o.append(T(0, 14, "Monolith: one program, one deploy", "b"))
    o.append(f'<rect x="0" y="24" width="300" height="118" rx="8" fill="{PRO[0]}" stroke="{PRO[1]}" stroke-width="1.5"/>')
    for i, s in enumerate(["riders", "drivers", "pricing", "matching", "payments", "trips", "support", "promos"]):
        o.append(f'<rect x="{12 + (i % 4) * 72}" y="{36 + (i // 4) * 50}" width="64" height="40" rx="4" fill="#fff" stroke="#c3cad2"/>')
        o.append(T(44 + (i % 4) * 72, 60 + (i // 4) * 50, s, "", "middle"))
    for i, s in enumerate(["+ simple to build, test and run at the start", "− one bug in promos can crash payments", "− 200 engineers queue for one release"]):
        o.append(T(0, 160 + i * 14, s, "grn" if s[0] == "+" else "red"))
    x0 = 360
    o.append(T(x0, 14, "Microservices: small services, each its own deploy", "b"))
    pos = [("riders", 0, 0), ("pricing", 1, 0), ("matching", 2, 0), ("drivers", 3, 0), ("payments", 0, 1), ("trips", 1, 1), ("support", 2, 1), ("promos", 3, 1)]
    for s, c, r in pos:
        o.append(box(x0 + c * 80, 30 + r * 64, 70, 36, *PRO, s, "", 1.2))
    for (a, b) in [((0, 0), (1, 0)), ((1, 0), (2, 0)), ((2, 0), (3, 0)), ((1, 0), (1, 1)), ((0, 1), (1, 1))]:
        x1 = x0 + a[0] * 80 + 35; y1 = 30 + a[1] * 64 + 18; x2 = x0 + b[0] * 80 + 35; y2 = 30 + b[1] * 64 + 18
        if a[1] == b[1]: o.append(arrow(x1 + 35, y1, x2 - 37, y2, w=1.1))
        else: o.append(arrow(x1, y1 + 18, x2, y2 - 20, w=1.1))
    for i, s in enumerate(["+ teams ship on their own; one crash stays local", "+ scale only the busy parts (matching at peak)", "− network calls fail; tracing a bug is harder", "− needs strong tooling and on-call discipline"]):
        o.append(T(x0, 160 + i * 14, s, "grn" if s[0] == "+" else "red"))
    o.append("</g>")
    return svg(214, o)


FIGS["micro"] = micro()
