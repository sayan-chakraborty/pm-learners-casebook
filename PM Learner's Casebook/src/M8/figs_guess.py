"""Guesstimate figures for M8; imported at the end of m8_figs.py."""
from m8_figs import FIGS, svg, T, lines, strip  # noqa: F401
from figs_primer import box, MK, G, B, A, GR, R, P, I  # noqa: F401
from figs_cases import etree

# ---------- G8.1 Google Photos ----------
FIGS["stripg81"] = strip([("Unit", "new photos, one year"), ("Approach", "Photos users"), ("Tree", "users × photos × MB"),
                          ("Numbers", "clicked vs received"), ("Check", "Google’s own counts"), ("Range", "and what moves it")])


def split81():
    """casebook split vs corrected split, per 100 photos"""
    o = [T(0, 12, "What 100 photos weigh: 25 clicked on the phone, 75 received on chat apps", "b")]
    rows = [("Casebook", [(25, 0.2, "#9aa3ad", "25 clicked × 0.2 MB = 5 MB"), (75, 2.0, "#b93a32", "75 received × 2 MB = 150 MB")], "155 MB"),
            ("Corrected", [(25, 2.0, "#127a64", "25 clicked × 2 MB = 50 MB"), (75, 0.2, "#9aa3ad", "75 received × 0.2 MB = 15 MB")], "65 MB")]
    L, W = 90, 420
    for i, (lab, segs, tot) in enumerate(rows):
        y = 30 + i * 50
        o.append(T(L - 8, y + 17, lab, "b", "end"))
        x = L
        for n, mb, col, note in segs:
            w = W * n * mb / 160
            o.append(f'<rect x="{x:.1f}" y="{y}" width="{max(w, 3):.1f}" height="24" fill="{col}" stroke="#fff"/>')
            x += max(w, 3)
        o.append(T(x + 8, y + 17, tot, "b"))
        o.append(T(L, y + 38, segs[0][3] + "  +  " + segs[1][3], "s"))
    o.append(T(0, 138, "Giving the big file size to the many small forwarded images makes the answer about 2.4 times too large.", "b red"))
    return svg(146, o)
FIGS["split81"] = split81()

FIGS["gtree81"] = etree([("1.5 bn", "Photos users", "a month (2025)"), ("× 600 clicked", "photos a year", "(about 12 a week)"),
                         ("× 600 received", "backed up too", "(one per clicked)"), ("× 2 MB and", "0.2 MB each", "= 1.3 GB a user"),
                         ("≈ 2,000 PB", "new photos", "a year (2 EB)")],
                        [("Check: in Nov 2020 Google said 28 billion photos and", "b"), ("videos were added every week: 1.5 trillion a year.", ""),
                         ("Our tree: 1.5 bn × 1,200 = 1.8 trillion a year,", ""), ("a few years later. Consistent.", "b grn")],
                        [("Range: 1,000–4,000 PB a year.", "b"), ("Swing factors: how many received photos", ""),
                         ("are backed up, and whether photos are", ""), ("kept full size or compressed.", "")], h=158, swing=2)

# ---------- G8.2 Google Drive, Singapore ----------
FIGS["stripg82"] = strip([("Unit", "disk, not data"), ("Approach", "users × real use"), ("Tree", "use is skewed"),
                          ("Numbers", "copies, headroom"), ("Check", "Photos per user"), ("Range", "and what moves it")])


def skew82():
    o = [T(0, 12, "How 100 people use a free 200 GB quota (illustrative)", "b")]
    groups = [(70, 2, "70 people: under 5 GB", "#127a64"), (20, 20, "20 people: 5–50 GB", "#0b5d7a"),
              (8, 90, "8 people: 50–150 GB", "#c47f17"), (2, 180, "2 people: nearly full", "#b93a32")]
    L, Bt, Tp = 40, 150, 30
    x = L
    for n, gb, lab, col in groups:
        w = 3.6 * n; h = (Bt - Tp) * gb / 200
        o.append(f'<rect x="{x:.1f}" y="{Bt - h:.1f}" width="{w:.1f}" height="{max(h, 2):.1f}" fill="{col}" stroke="#fff"/>')
        x += w
    o.append(f'<line x1="{L}" y1="{Bt}" x2="{L + 360}" y2="{Bt}" stroke="#4a5563"/>')
    o.append(f'<line x1="{L}" y1="{Tp}" x2="{L + 360}" y2="{Tp}" stroke="#b93a32" stroke-dasharray="4 3"/>')
    o.append(T(L + 4, Tp - 5, "quota: 200 GB each", "s red"))
    o.append(T(L + 126, Bt - 10, "70 people, about 2 GB each: a sliver", "b grn", "middle"))
    o.append(T(L, Bt + 15, "each column is a group of people, as wide as its share", "s"))
    for i, (n, gb, lab, col) in enumerate(groups):
        o.append(f'<rect x="430" y="{36 + i * 20}" width="10" height="10" fill="{col}"/>'); o.append(T(446, 45 + i * 20, f"{lab}, avg {gb} GB", "s"))
    o.append(T(430, 136, "Average: 0.7×2 + 0.2×20 + 0.08×90 + 0.02×180", "b"))
    o.append(T(430, 150, "≈ 16 GB, about 8% of the quota, not 60%.", "b grn"))
    return svg(172, o)
FIGS["skew82"] = skew82()

FIGS["gtree82"] = etree([("5.8 mn", "internet users", "in Singapore"), ("× 20 GB", "average stored", "(skewed use)"),
                         ("= 116,000 TB", "of user data", "stored once"), ("× 2 copies", "+ 20% headroom", "for growth"),
                         ("≈ 280,000 TB", "of disk", "(about 280 PB)")],
                        [("Check: Google Photos holds about 9 trillion items for", "b"), ("1.5 bn users: 6,000 items × ~1.5 MB ≈ 9 GB each.", ""),
                         ("A 20 GB average with a 200 GB quota is in line.", "b grn")],
                        [("Range: 150,000–500,000 TB of disk.", "b"), ("Swing factors: average use (10–40 GB)", ""),
                         ("and how many copies Google keeps.", "")], h=144, swing=1)

FIGS["gtreeupi"] = etree([("20 bn", "UPI payments", "a month"), ("× 12", "= 240 bn", "a year"), ("× 1 KB", "= 240 TB", "one copy"),
                          ("× 4 keepers", "× 3 copies", "each"), ("≈ 3 PB", "of disk", "a year")],
                         [("Check: Google Photos adds about 2,000 PB a year.", "b"), ("UPI’s 3 PB is under 0.2% of that.", ""),
                          ("Money data is small; media is big.", "b grn")],
                         [("Range: 2–15 PB a year.", "b"), ("Swing factor: logs and fraud-check data", ""),
                          ("stored alongside each payment.", "")], h=144, swing=3)
