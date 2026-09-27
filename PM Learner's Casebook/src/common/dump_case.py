"""Print a case's joined paragraphs with ¶¶ separators, to write exact extraction fixes.
usage: python dump_case.py iimb 55 56"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import booklib  # noqa: F401  (sets up cases2 path)
import cases2
src, pages = sys.argv[1], [int(x) for x in sys.argv[2:]]
for pno in pages:
    for k, lines, _ in cases2.segments(src, pno):
        if k == "T": print(f"[T] {lines}"); continue
        print(f"[{k}] " + "¶¶".join(p for p in cases2.join(lines) if p))
