"""python crop.py <page> <y0 frac> <y1 frac> <out> [dpi]"""
import sys, pymupdf as fitz
d = fitz.open(__import__("os").path.dirname(__import__("os").path.abspath(__file__)) + "/../../F2 - Behavioural.pdf"); p = d[int(sys.argv[1]) - 1]; r = p.rect
a, b = float(sys.argv[2]), float(sys.argv[3])
p.get_pixmap(dpi=int(sys.argv[5]) if len(sys.argv) > 5 else 110, clip=fitz.Rect(0, r.height * a, r.width, r.height * b)).save(sys.argv[4])
