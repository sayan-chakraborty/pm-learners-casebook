"""M9 primer figures; imported at the end of m9_figs.py."""
from m9_figs import FIGS, svg, T, lines, hbars, waterfall, loop, two_by_two, seq, strip  # noqa: F401
from figlib import *  # noqa: F401,F403
from figlib import box, MK, G, B, A, GR, R, P, I, vbars, arr


# ---------- where ₹15,900 of a smart speaker goes ----------
FIGS["speakerwf"] = waterfall([("Price on|the box (MRP)", 15900, "start"), ("GST|18%", 2425, "down"), ("Shop and|distributor", 1600, "down"),
                               ("Parts and|assembly", 5200, "down"), ("Freight,|warranty,|royalties", 1100, "down"), ("Left for|Apple", 5575, "total")],
                              h=236, note="One HomePod mini sold in India: where the ₹15,900 goes (illustrative split)")


# ---------- the ecosystem web ----------
def ecoweb():
    o = [MK]
    cx, cy = 340, 128
    o.append(box(cx - 78, cy - 30, 156, 60, *B, [("iPhone", "b t13"), ("the hub everyone owns", "s")], sw=2))
    nodes = [(92, 40, "AirPods", "switch between devices|without re-pairing", G),
             (588, 40, "Apple Watch", "works only with|an iPhone", G),
             (92, 216, "HomePod", "plays what the phone|plays; runs the home", A),
             (588, 216, "Mac, iPad", "copy on one,|paste on the other", G)]
    for x, y, t, sub, col in nodes:
        o.append(box(x - 82, y - 26, 164, 52, *col, [(t, "b"), (sub.split("|")[0], "s"), (sub.split("|")[1], "s")], lh=13))
        x2 = cx + (-78 if x < cx else 78); y2 = cy + (-18 if y < cy else 18)
        x1 = x + (82 if x < cx else -82)
        o.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y2}" stroke="#0b5d7a" stroke-width="1.6" stroke-dasharray="5 3"/>')
    o.append(box(250, 196, 180, 54, *P, [("Services on top", "b"), ("iCloud, Music, TV+, AppleCare", "s"), ("paid every month", "s")], lh=13))
    o.append(f'<line x1="340" y1="158" x2="340" y2="194" stroke="#127a64" stroke-width="3" marker-end="url(#pg)"/>')
    o.append(T(348, 180, "₹ every month", "b grn"))
    o.append(lines(340, 272, "Each extra device makes the others more useful, and leaving means replacing all of them at once.", "b acc", "middle"))
    return svg(282, o)
FIGS["ecoweb"] = ecoweb()


# ---------- the life of a loyalty point ----------
def pointlife():
    o = [MK, '<g class="c">']
    o.append(box(0, 40, 128, 70, *G, [("① Earn", "b"), ("₹1 lakh spent", ""), ("× 5% = ₹5,000", ""), ("of points", "")], lh=13))
    o.append(box(170, 40, 150, 70, *A, [("② Sit on the books", "b"), ("₹5,000 owed to the", ""), ("customer: a liability", ""), ("until used or expired", "")], lh=13))
    o.append(box(372, 4, 150, 62, *R, [("③ Burn (redeemed)", "b"), ("70% = ₹3,500", ""), ("real cost to the brands", "")], lh=13))
    o.append(box(372, 86, 150, 62, *GR, [("④ Expire (breakage)", "b"), ("30% = ₹1,500", ""), ("never costs anything", "")], lh=13))
    o.append(box(560, 40, 120, 70, *B, [("Net cost", "b"), ("₹3,500 on ₹1 lakh", ""), ("= 3.5% of sales,", ""), ("not 5%", "")], lh=13))
    o.append(arr(130, 75, 166, 75)); o.append(arr(322, 66, 368, 38)); o.append(arr(322, 84, 368, 112))
    o.append(arr(524, 38, 556, 64)); o.append(arr(524, 116, 556, 88))
    o.append("</g>")
    o.append(lines(0, 172, "A programme that is too stingy (little to spend points on) raises breakage and looks cheap on paper,|but customers notice that their points are worthless and stop caring.", "s", "start", 13))
    return svg(196, o)
FIGS["pointlife"] = pointlife()


# ---------- who pays when a point crosses brands ----------
FIGS["crossbrand"] = seq(
    [("Customer", "Priya", "user"), ("Titan store", "where she earns", "merchant"), ("Group loyalty", "the points bank", "app"),
     ("Starbucks café", "where she spends", "merchant")],
    [(0, 1, "buys a ₹20,000 watch", "money"), (1, 2, "“give Priya 1,000 points”", "msg"), (1, 2, "₹1,000 into the pool (Titan funds it)", "money"),
     (2, 0, "balance: 1,000 points = ₹1,000", "ret"), (0, 3, "pays for coffee with 400 points", "msg"), (3, 2, "“redeem 400 of Priya’s points”", "msg"),
     (2, 3, "₹400 settled to Starbucks, less a fee", "money"), (2, 2, "600 points still owed: stays a liability", "self")],
    note="The brand that issues the point pays for it; the brand that accepts it gets paid. Without that rule no brand will join.")


# ---------- India Stack layers ----------
def stack():
    rows = [("Commerce", "ONDC (2022)", "an open network any buyer app and seller app can join", A),
            ("Consent to share data", "Account Aggregator (2021)", "you approve which bank data a lender may read", P),
            ("Documents", "DigiLocker (2015)", "67.6 crore users; 950 crore+ documents issued", G),
            ("Payments", "UPI (2016)", "about 2,000 crore payments a month", B),
            ("Identity", "Aadhaar (2010)", "a number anyone can verify with a fingerprint or OTP", GR)]
    o = ['<g class="c">']
    for i, (layer, name, what, (fill, st)) in enumerate(rows):
        y = 6 + i * 40; w = 680 - i * 0  # same width
        o.append(f'<rect x="0" y="{y}" width="680" height="34" rx="5" fill="{fill}" stroke="{st}" stroke-width="1.3"/>')
        o.append(T(12, y + 21, layer, "b")); o.append(T(190, y + 21, name, "b acc")); o.append(T(360, y + 21, what, "s"))
    o.append("</g>")
    o.append(T(0, 222, "Each layer is built once by the state (or a non-profit), and any bank, app or shop can plug in.", "b acc"))
    o.append(T(0, 238, "Private companies compete on the apps built on top: PhonePe on UPI, Magicpin on ONDC, lenders on Account Aggregator.", "s"))
    return svg(246, o)
FIGS["stack"] = stack()


# ---------- enrolment vs use ----------
FIGS["enrol"] = hbars([("Downloaded the app", 100, "a campaign before the election"), ("Registered", 62, "gave a phone number, found their name"),
                       ("Used it once more", 30, "checked a booth or a candidate"), ("Opened it in voting week", 14, "the week that matters"),
                       ("Voted, and wouldn’t have", 2, "the only number the government hired you for")], 100,
                      lw=190, fmt="{}", unit=" of 100", colors=["#0b5d7a", "#0b5d7a", "#0b5d7a", "#c47f17", "#127a64"],
                      note="A public app, 100 people who downloaded it (illustrative)")


# ---------- turnout and Tata Digital (half-width) ----------
FIGS["turnout"] = vbars([("2009", 58.2, "58.2%"), ("2014", 66.4, "66.4%"), ("2019", 67.4, "67.4%"), ("2024", 65.8, "65.8%")], 75,
                        "Lok Sabha turnout", sub="share of registered voters who voted", colors=["#9aa3ad", "#0b5d7a", "#0b5d7a", "#c47f17"])
FIGS["tatadig"] = vbars([("Revenue|FY25", 32188, "₹32,188 Cr"), ("Revenue|FY26", 35990, "₹35,990 Cr"), ("Loss|FY25", 4610, "₹4,610 Cr"),
                         ("Loss|FY26", 4974, "₹4,974 Cr")], 36000, "Tata Digital: sales up, losses up",
                        sub="BigBasket, Neu, Croma online, 1mg, CLiQ", colors=["#0b5d7a", "#0b5d7a", "#b93a32", "#b93a32"])


# ---------- turning points ----------
def timeline():
    pts = [(46, "2007–08", "iPhone, App Store", ["One device runs", "any app; Apple", "earns on every", "app sold"], "#0b5d7a"),
           (130, "2010", "Aadhaar", ["A verifiable ID", "for everyone; 100", "crore numbers", "by 2016"], "#5b6470"),
           (214, "2014", "Amazon Echo", ["A speaker sold", "near cost to put", "Alexa in the", "home"], "#c47f17"),
           (298, "2015", "DigiLocker", ["Documents fetched", "from the issuer,", "not scanned", "copies"], "#127a64"),
           (382, "2016", "UPI", ["Free instant", "payments; later", "the rail for", "cashback"], "#0b5d7a"),
           (466, "Apr 2022", "Tata Neu", ["One app and one", "currency for", "Tata brands;", "NeuCoin = ₹1"], "#7c3aa6"),
           (550, "2022–25", "Voice stalls", ["Reports of big", "Alexa losses;", "Alexa+ rebuilt", "on GenAI, 2025"], "#b93a32"),
           (634, "2025–26", "Neu refocus", ["Card, loans and", "loyalty over", "shopping; loss", "₹4,974 Cr"], "#7c3aa6")]
    o = ['<line x1="8" y1="104" x2="674" y2="104" stroke="#4a5563" stroke-width="2"/><g class="c">']
    for i, (x, d, h, ls, col) in enumerate(pts):
        o.append(f'<circle cx="{x}" cy="104" r="6.5" fill="{col}"/>')
        if i % 2 == 0:
            o.append(T(x, 90, d, "b", "middle")); y0 = 126
        else:
            o.append(T(x, 124, d, "b", "middle")); y0 = 16
        o.append(T(x - 40, y0, h, "b", "start", fill=col))
        for j, l in enumerate(ls): o.append(T(x - 40, y0 + 14 + j * 13, l))
    o.append("</g>")
    return svg(192, o)
FIGS["timeline"] = timeline()


# ---------- two ways to earn from a device ----------
FIGS["devmodels"] = stacks([("HomePod mini|at ₹15,900", [5575, 3000], "₹8,575 over 3 years"),
                            ("Echo Dot|in a sale, ₹2,999", [100, 1500], "₹1,600, and ₹1,500 of it only if people shop by voice")],
                           ["profit on the device", "earned after the sale, 3 years"], ["#0b5d7a", "#127a64"], 11000,
                           title=None, lw=130, unit="")
