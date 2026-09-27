"""System design V figures for M6; imported at the end of m6_figs.py."""
from m6_figs import FIGS, svg, T  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R, P  # noqa: F401


def ladder():
    rungs = [("240p", 0.4, "weak 4G, data saver"), ("360p", 0.8, "most phones on 4G"), ("480p", 1.2, "phone, good signal"),
             ("720p", 2.5, "phone on Wi-Fi, small TV"), ("1080p", 5.0, "TV on broadband"), ("4K", 15.0, "big TV on fibre")]
    o = [T(0, 12, "rung", "b"), T(84, 12, "megabits per second", "b"), T(462, 12, "data an hour", "b"), T(560, 12, "who gets it", "b")]
    for i, (r, mbps, who) in enumerate(rungs):
        y = 22 + i * 24
        w = 320 * mbps / 15
        col = "#7c3aa6" if r == "4K" else "#0b5d7a"
        o.append(T(0, y + 14, r, "b"))
        o.append(f'<rect x="84" y="{y + 3}" width="{max(w, 3):.1f}" height="15" rx="2" fill="{col}"/>')
        o.append(T(90 + w, y + 15, f"{mbps:g}", "b"))
        o.append(T(462, y + 15, f"{mbps * 3600 / 8:,.0f} MB", ""))
        o.append(T(560, y + 15, who, "s"))
    o.append(T(0, 172, "MB an hour = Mbps × 3,600 ÷ 8. A 3½-hour match at 1.5 Mbps ≈ 2.4 GB.", "b acc"))
    return svg(180, o)
FIGS["ladder"] = ladder()


def abr():
    L, R, Tp, Bt = 56, 670, 18, 120
    t = list(range(0, 61, 4))
    bw = [4, 4, 4, 3.5, 3, 0.6, 0.3, 0.4, 0.8, 2, 3, 4, 4, 4, 4, 4]
    rung = [1.2, 2.5, 2.5, 2.5, 2.5, 0.8, 0.4, 0.4, 0.4, 0.8, 1.2, 2.5, 2.5, 2.5, 2.5, 2.5]
    buf = [4, 8, 12, 14, 16, 12, 8, 6, 6, 9, 12, 14, 16, 16, 16, 16]
    X = lambda s: L + (R - L) * s / 64
    Y = lambda v: Bt - (Bt - Tp) * v / 4.5
    o = [f'<rect x="{X(18):.1f}" y="{Tp}" width="{X(32) - X(18):.1f}" height="{Bt - Tp}" fill="#fcecea"/>',
         T((X(18) + X(32)) / 2, Tp + 12, "train in a tunnel", "b red", "middle"),
         f'<line x1="{L}" y1="{Bt}" x2="{R}" y2="{Bt}" stroke="#4a5563"/>', T(L - 6, Tp - 4, "Mbps", "s", "end")]
    for v in (0, 1, 2, 3, 4): o.append(T(L - 6, Y(v) + 4, str(v), "s", "end"))
    for s in range(0, 61, 10): o.append(T(X(s), Bt + 14, f"{s} s", "s", "middle"))
    d = " ".join(f"{'M' if i == 0 else 'L'}{X(s):.1f},{Y(v):.1f}" for i, (s, v) in enumerate(zip(t, bw)))
    o.append(f'<path d="{d}" fill="none" stroke="#9aa3ad" stroke-width="2" stroke-dasharray="5 3"/>')
    d = "M" + " L".join(f"{X(s):.1f},{Y(v):.1f} {X(s + 4):.1f},{Y(v):.1f}" for s, v in zip(t, rung))
    o.append(f'<path d="{d}" fill="none" stroke="#0b5d7a" stroke-width="2.8"/>')
    o.append(T(X(1), Y(4) - 6, "network speed (dashed)", "s"))
    o.append(T(X(44), Y(2.5) - 8, "quality the player picks", "b acc"))
    yb = 144
    o.append(T(L - 6, yb + 12, "buffer", "s", "end"))
    for s, b in zip(t, buf):
        a = 0.15 + b / 20
        o.append(f'<rect x="{X(s) + 1:.1f}" y="{yb}" width="{X(4) - X(0) - 2:.1f}" height="16" fill="rgba(18,122,100,{a:.2f})"/>')
        o.append(T(X(s) + (X(4) - X(0)) / 2, yb + 12, f"{b}s", "b w" if a > 0.6 else "s", "middle"))
    o.append(T(L, yb + 34, "The buffer shrinks from 16 s to 6 s in the tunnel but never hits zero: blurry for a while, never frozen.", "b grn"))
    return svg(186, o)
FIGS["abr"] = abr()


def cdn():
    o = [MK, '<g class="c">']
    tiers = [(4, "Stadium feed", "one stream in", GR), (140, "Encoders, origin", "every rung, once", B),
             (276, "Origin shield", "collects misses", B), (412, "City edge, Nagpur", "most requests end", A), (548, "Viewers", "4 lakh in Nagpur", G)]
    for x, a, b, st in tiers:
        o.append(box(x, 22, 128, 50, *st, [(a, "b"), (b, "s")]))
    for x in (132, 268, 404, 540): o.append(f'<line x1="{x}" y1="47" x2="{x + 8}" y2="47" class="ln" marker-end="url(#pa)"/>')
    o.append(T(340, 12, "Video flows right; requests flow left and stop at the first layer that has a copy.", "s", "middle"))
    rows = [("6.5 Cr viewers × 1 request per 4 s", "= 1.6 Cr requests a second at the city edges", ""),
            ("At a 95% hit rate", "8 lakh a second go up to the shield", "b red"),
            ("At a 99% hit rate", "1.6 lakh a second go up: five times less", "b grn"),
            ("Shield hit rate ~99.9%", "the origin sees each segment only a handful of times", "")]
    for i, (a, b, c) in enumerate(rows):
        o.append(T(14, 98 + i * 18, a, "b")); o.append(T(270, 98 + i * 18, b, c))
    o.append("</g>")
    return svg(170, o)
FIGS["cdn"] = cdn()


def latency():
    parts = [("Camera, graphics", 3, "#9aa3ad"), ("Encoding", 4, "#0b5d7a"), ("Waiting for a whole segment", 6, "#3e4fb8"),
             ("CDN", 1, "#c47f17"), ("Player’s safety buffer (2–3 segments)", 15, "#b93a32")]
    L = 4; sc = 672 / 32
    o = [T(0, 12, "App with 6-second segments: about 29 seconds, glass to glass", "b")]
    x = L
    for i, (lab, s, col) in enumerate(parts):
        w = s * sc
        o.append(f'<rect x="{x:.1f}" y="20" width="{w - 2:.1f}" height="26" fill="{col}" rx="2"/>')
        o.append(T(x + w / 2, 38, f"{s} s", "b w", "middle"))
        if i == 3: o.append(T(x + w / 2, 76, lab, "s", "middle"))
        elif i == 0: o.append(T(x, 62, lab, "s", "start"))
        else: o.append(T(x + w / 2, 62, lab, "s", "middle"))
        x += w
    o.append(T(0, 104, "Satellite TV: about 7 seconds", "b"))
    o.append(f'<rect x="{L}" y="110" width="{7 * sc:.1f}" height="20" fill="#127a64" rx="2"/>')
    o.append(T(L + 7 * sc + 8, 125, "← Priya’s father sees the wicket about 20 seconds before she does", "b grn"))
    o.append(T(0, 152, "Low-latency mode (1-second parts, small buffer): about 6 seconds, but more freezes on weak networks", "b acc"))
    o.append(f'<rect x="{L}" y="158" width="{6 * sc:.1f}" height="20" fill="#3e4fb8" rx="2"/>')
    return svg(184, o)
FIGS["latency"] = latency()


def spike():
    L, R, Tp, Bt = 56, 670, 16, 150
    xs = [0, 15, 30, 40, 50, 55, 60, 70, 90, 120]
    vw = [0.4, 0.6, 1.2, 2.0, 3.5, 5.0, 6.0, 6.3, 6.4, 6.5]
    auto = [1.0, 1.0, 1.4, 1.9, 2.6, 3.2, 4.2, 5.4, 6.8, 7.0]
    pre = [7.2] * 10
    X = lambda m: L + (R - L) * m / 120
    Y = lambda v: Bt - (Bt - Tp) * v / 8
    o = [f'<line x1="{L}" y1="{Bt}" x2="{R}" y2="{Bt}" stroke="#4a5563"/>', T(L + 4, Tp - 4, "crore watching", "s", "start")]
    for v in (0, 2, 4, 6, 8): o.append(T(L - 6, Y(v) + 4, str(v), "s", "end"))
    for m, lab in [(0, "6:30"), (30, "7:00"), (60, "7:30"), (90, "8:00"), (120, "8:30")]:
        o.append(T(X(m), Bt + 14, lab + " pm", "s", "end" if m == 120 else "middle"))

    def path(vals, col, w, dash=""):
        d = " ".join(f"{'M' if i == 0 else 'L'}{X(m):.1f},{Y(v):.1f}" for i, (m, v) in enumerate(zip(xs, vals)))
        return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w}" {dash}/>'
    pts = [(X(m), Y(v)) for m, v in zip(xs, vw)][4:9]
    pts2 = [(X(m), Y(v)) for m, v in zip(xs, auto)][4:9]
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts + pts2[::-1])
    o.append(f'<polygon points="{poly}" fill="#fcecea"/>')
    o.append(path(pre, "#127a64", 2.4, 'stroke-dasharray="6 3"'))
    o.append(path(auto, "#b93a32", 2.4, 'stroke-dasharray="3 3"'))
    o.append(path(vw, "#0b5d7a", 3))
    o.append(f'<line x1="{X(58):.1f}" y1="{Tp + 12}" x2="{X(58):.1f}" y2="{Bt}" stroke="#c47f17" stroke-dasharray="2 2"/>')
    o.append(T(X(58) - 4, Tp + 26, "toss", "b amb", "end"))
    o.append(T(X(20), Y(7.2) - 6, "servers switched on before the match", "b grn"))
    o.append(T(X(4), Y(3.0), "autoscaling: follows the crowd", "b red"))
    o.append(T(X(72), Y(4.4), "short of servers", "b red"))
    o.append(T(X(96), Y(6.4) + 16, "viewers watching", "b acc"))
    return svg(174, o)
FIGS["spike"] = spike()


def degrade():
    steps = [("1", "Stop 4K and 1080p on phones", "saves the most bandwidth; few notice on a small screen", "#127a64"),
             ("2", "Pause animations, live polls, comments", "heavy on servers, light on value tonight", "#1d8a73"),
             ("3", "Show a fixed home page, not a personal one", "no recommendation calls for new arrivals", "#0b5d7a"),
             ("4", "Queue new sign-ups in a short waiting room", "protects viewers already watching", "#9a6310"),
             ("5", "Cap every stream at 480p", "last resort: blurrier for all, frozen for none", "#b93a32"),
             ("✗", "Never: stop the live match", "the one thing everyone came for", "#1c232b")]
    o = []
    for i, (n, a, b, col) in enumerate(steps):
        y = 4 + i * 30; x = i * 14
        o.append(f'<rect x="{x}" y="{y}" width="{680 - x}" height="26" rx="4" fill="{col}"/>')
        o.append(T(x + 12, y + 18, n, "b w t13"))
        o.append(T(x + 32, y + 17, a, "b w"))
        o.append(T(672, y + 17, b, "w", "end"))
    o.append(T(0, 198, "Load rising ↓ · Each step has a switch that works in seconds and was tested in rehearsal.", "b acc"))
    return svg(204, o)
FIGS["degrade"] = degrade()
