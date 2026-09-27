"""M1 build: parts/*.html -> one HTML (verbatim cases injected, figures numbered) -> PDF -> PNG previews.
usage: python build.py            full module
       PARTS=0,1,2 python build.py   only parts whose file name starts with those digits (checkpoints)"""
import os, re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "common"))
import booklib  # noqa: E402
sys.path.insert(0, str(HERE))
import m1_figs  # noqa: E402

OUT_PDF = HERE.parents[1] / "M1 - Payments & fintech.pdf"
CASES = {
    "B55": ("iimb", [55, 56], dict(fix=[
        ("• Regular Customers Is there", "• Regular Customers¶¶Is there"),
        ("etc. These are all the issues", "etc.¶¶These are all the issues")])),
    "B38": ("iimb", [38], dict(fix=[
        ("tuition, and leisure. Since 16", "tuition, and leisure.¶¶Since 16"),
        ("efforts. To tackle these", "efforts.¶¶To tackle these")])),
    "B116": ("iimb", [116, 117], dict(fix=[
        ("The personas¶¶I can think of are:", "The personas I can think of are:")])),
    "B110": ("iimb", [110, 111], dict(fix=[
        ("1.¶¶General Stores", "1. General Stores"), ("2.¶¶Large Stores", "2. Large Stores"),
        ("1.¶¶Tech Savvy", "1. Tech Savvy"), ("like the elderly I would like", "like the elderly.¶¶I would like")],
        drop=("Can you improve the IDFC Bank mobile app for preventing frauds ",))),
    "A294": ("iima", [294], dict(fix=[
        ("Great. The metrics should align with the business goals. Users should find the promotions useful enough to continue using Google Pay.¶¶• Promotion partners should benefit through customer acquisition and revenue.¶¶• Accordingly, I'd define metrics from the perspective of users and promotion partners. The business goals seem accurate. Please proceed with the metrics.¶¶",
         "[[The casebook prints the previous two turns a second time here; the repeat is removed.]]¶¶"),
        ("business goals. Users should find", "business goals.¶¶• Users should find"),
        ("• Accordingly, I'd define", "Accordingly, I'd define"),
        ("Number of payments / payment frequency", "• Number of payments / payment frequency"),
        ("• Promotion Partner Metrics :", "Promotion Partner Metrics :"),
        ("Key metrics: Number of tie-in promotion partners", "Key metrics:¶¶• Number of tie-in promotion partners"),
        ("• These metrics help identify", "These metrics help identify")])),
    "A308": ("iima", [308], {}),
}

HEAD = """<!DOCTYPE html><html lang="en-GB"><head><meta charset="utf-8"><title>M1 Payments &amp; fintech</title>
<link rel="stylesheet" href="../common/style.css"></head><body>
"""

def build():
    only = os.environ.get("PARTS")
    files = sorted((HERE / "parts").glob("*.html"))
    if only: files = [f for f in files if f.name.split("_")[0] in only.split(",")]
    body = ""
    hits = 0
    for f in files:
        t = f.read_text(encoding="utf-8")
        hits += len(booklib.scan(t, f.name))          # author text only; cases are injected after the scan
        body += t + "\n"
    for key, (src, pages, kw) in CASES.items():
        if "{{CASE:%s}}" % key in body:
            body = body.replace("{{CASE:%s}}" % key, booklib.qa_html(src, pages, **kw))
    for k, svg in m1_figs.FIGS.items():
        body = body.replace("{{SVG:%s}}" % k, svg)
    body = booklib.text_fill_to_style(body)
    body, nfig = booklib.number_figs(body, "1")
    out_html = HERE / "m1_built.html"
    out_html.write_text(HEAD + body + "</body></html>", encoding="utf-8")
    n = booklib.render(out_html, OUT_PDF, "PM Learner’s Casebook · Payments &amp; fintech", HERE / "png",
                       dpi=int(os.environ.get("DPI", 80)))
    print(f"{OUT_PDF.name}: {n} pages, {nfig} figures, {hits} style hits")

if __name__ == "__main__":
    build()
