"""Report how full each page is (lowest non-white pixel row above the footer). usage: python fill.py <pdf>"""
import sys, pymupdf as fitz
from PIL import Image
d = fitz.open(sys.argv[1])
for i, p in enumerate(d):
    pix = p.get_pixmap(dpi=30); im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L")
    w, h = im.size; foot = int(h * 0.955); last = 0
    px = im.load()
    for y in range(foot):
        if any(px[x, y] < 235 for x in range(0, w, 2)): last = y
    fill = last / foot
    txt = p.get_text()
    locs = [k for k in ("Figure 1.",) if k in txt]
    print(f"p{i+1:02d} fill {fill:4.0%}" + ("   <-- short" if fill < 0.8 else ""))
