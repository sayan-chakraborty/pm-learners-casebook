"""F2 build: parts/*.html -> one HTML (figures numbered F.n) -> PDF -> PNG previews.
usage: python build.py            whole file
       PARTS=1,2 python build.py  only parts whose file name starts with those prefixes
No casebook text is injected here: the real questions are short quotes from the ISB interview reports, typed into the parts."""
import os, re, sys, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "common"))
import booklib  # noqa: E402
sys.path.insert(0, str(HERE))
import f2_figs  # noqa: E402
import figs     # noqa: E402,F401  (registers FIGS)

OUT_PDF = HERE.parents[1] / "F2 - Behavioural.pdf"

EXTRA = [r"\bunlock(s|ed|ing)?\b", r"\bempower", r"game-changer", r"\bpivotal", r"plays a key role", r"worth noting", r"\bnot just\b",
         r"at its core", r"real magic", r"here's the thing", r"here’s the thing", r"\bnavigat(e|ing)\b",
         r"below(?! the line)", r"that follows", r"above(?! zero| the line)", r"\bit'?s not .{1,40}, it'?s\b", r"it’s not .{1,40}, it’s"]

HEAD = """<!DOCTYPE html><html lang="en-GB"><head><meta charset="utf-8"><title>Behavioural interviews</title>
<link rel="stylesheet" href="../common/style.css"><style>
.prompts{display:flex;gap:8pt;margin:4pt 0 6pt;break-inside:avoid}.prompt{flex:1;font:8.2pt/1.4 Inter,sans-serif;padding:5pt 8pt;border-radius:4pt;border-left:3pt solid}
.prompt.bad{background:#fcecea;border-color:#b93a32}.prompt.good{background:#e1f2ec;border-color:#127a64}
.asked{font-family:Inter,sans-serif;font-size:8.2pt;line-height:1.4;border:1px solid #d9dee4;border-top:none;border-radius:0 0 4px 4px;padding:4pt 8pt;margin:0 0 5pt;background:#fafbfc}
.asked .l{font-size:7pt;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#0b5d7a;margin-right:4pt}
.asked q{font-style:italic;quotes:"“" "”"}.asked .co{color:#5b6470}
.qhead{margin-top:10pt;break-after:avoid}
.label{font-family:Inter,sans-serif;font-size:7.4pt;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:#5b6470;margin:5pt 0 2pt}
.label .bg{font-weight:600;letter-spacing:0;text-transform:none;color:#7a838d}
.card{display:grid;grid-template-columns:92pt 1fr;border:1px solid #cfd6dd;border-radius:5px;font-family:Inter,sans-serif;font-size:8pt;line-height:1.35;overflow:hidden;break-inside:avoid}
.card div{padding:2.6pt 6pt;border-bottom:1px solid #e6eaee}.card .k{background:#eef4f7;font-weight:700;color:#0b5d7a}
.card div:nth-last-child(-n+2){border-bottom:none}
.real{break-inside:avoid}
</style></head><body>
"""


def build():
    only = os.environ.get("PARTS")
    files = sorted((HERE / "parts").glob("*.html"))
    if only: files = [f for f in files if f.name.split("_")[0] in only.split(",")]
    body = ""; hits = 0
    for f in files:
        t = f.read_text(encoding="utf-8")
        # quoted interview questions are the reports' words: scan only author text
        mine = re.sub(r"<q>.*?</q>", " ", t, flags=re.S)
        hits += len(booklib.scan(mine, f.name))
        plain = re.sub(r"<[^>]+>", " ", mine)
        for pat in EXTRA:
            for m in re.finditer(pat, plain, re.I):
                hits += 1; print(f"  [{f.name}] {pat}: …{plain[max(0, m.start() - 40): m.end() + 40]}…")
        body += t + "\n"
    for k, svg in f2_figs.FIGS.items():
        body = body.replace("{{SVG:%s}}" % k, svg)
    left = re.findall(r"\{\{SVG:([\w-]+)\}\}", body)
    if left: print("!! missing SVGs:", left)
    dup = [k for k, c in collections.Counter(re.findall(r"\{\{FIG:([\w-]+)\}\}", body)).items() if c > 1]
    if dup: print("!! duplicate figure keys:", dup)
    body = booklib.text_fill_to_style(body)
    body, nfig = booklib.number_figs(body, "F")
    out_html = HERE / "f2_built.html"
    out_html.write_text(HEAD + body + "</body></html>", encoding="utf-8")
    n = booklib.render(out_html, OUT_PDF, "PM Learner’s Casebook · Behavioural", HERE / "png",
                       dpi=int(os.environ.get("DPI", 80)))
    print(f"{OUT_PDF.name}: {n} pages, {nfig} figures, {hits} style hits")


if __name__ == "__main__":
    build()
