"""Crop each figure (caption y minus figure height) and stack them into sheets for review."""
import re, sys, pymupdf as fitz
from PIL import Image
d = fitz.open(__import__("os").path.dirname(__import__("os").path.abspath(__file__)) + "/../../F2 - Behavioural.pdf")
crops = []
for pno, p in enumerate(d):
    blocks = sorted(p.get_text("blocks"), key=lambda b: b[1])
    draws = [dr["rect"] for dr in p.get_drawings()]
    for b in blocks:
        m = re.match(r"Figure F\.(\d+)", b[4])
        if not m: continue
        cy = b[1]
        above = [r for r in draws if r.y1 <= cy + 1 and r.y0 > cy - 520 and r.height < 500]
        top = min([r.y0 for r in above], default=cy - 200)
        # walk up only through contiguous drawings
        clip = fitz.Rect(0, max(0, top - 6), p.rect.width, cy + 2)
        pix = p.get_pixmap(dpi=int(sys.argv[1]) if len(sys.argv) > 1 else 75, clip=clip)
        fn = f"fc_{int(m.group(1)):02d}.png"; pix.save(fn); crops.append((int(m.group(1)), pno + 1, fn))
print(len(crops))
groups = [crops[i:i + 5] for i in range(0, len(crops), 5)]
for gi, g in enumerate(groups):
    ims = [Image.open(f) for _, _, f in g]
    W = max(i.width for i in ims); H = sum(i.height for i in ims)
    c = Image.new("RGB", (W, H), "white"); y = 0
    for i in ims: c.paste(i, (0, y)); y += i.height
    c.save(f"fsheet_{gi}.png")
print([(n, p) for n, p, _ in crops])
