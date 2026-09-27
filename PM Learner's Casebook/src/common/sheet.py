"""Contact sheet: python sheet.py <png_dir> <first> <last> <out> [scale]"""
import sys
from PIL import Image
d, a, b, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
sc = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0
ims = [Image.open(f"{d}/p{i:02d}.png") for i in range(a, b + 1)]
w = sum(i.width for i in ims); h = max(i.height for i in ims)
c = Image.new("RGB", (w, h), "white"); x = 0
for i in ims: c.paste(i, (x, 0)); x += i.width
if sc != 1: c = c.resize((int(w * sc), int(h * sc)))
c.save(out)
