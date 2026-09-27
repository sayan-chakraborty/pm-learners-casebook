"""Pass 1: read headings, case/framework labels and section kickers from each chapter PDF -> index.json (slow; run once)."""
import json, re, pathlib, pymupdf as fitz
HERE = pathlib.Path(__file__).resolve().parent
BOOK = HERE.parents[1]
import os
FILES = os.environ.get("CODES", ",".join([f"M{i}" for i in range(1, 10)] + ["F2"])).split(",")
LAB = re.compile(r"^(CASE|GUESSTIMATE|FRAMEWORK|QUESTION) [\d.]*\s*·\s*(.+)$|^(FRAMEWORK) · (.+)$")
out = []
for code in FILES:
    fn = next(BOOK.glob(f"{code} - *.pdf"))
    d = fitz.open(fn)
    ch = {"code": code, "file": fn.name, "title": fn.stem.split(" - ", 1)[1], "pages": len(d), "h1": [], "labels": [], "kick": {}}
    banner = 0
    for i, pg in enumerate(d):
        prev = None
        for b in pg.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                t = "".join(s["text"] for s in l["spans"]).strip(); sz = max(s["size"] for s in l["spans"])
                if not t: continue
                if i == 0 and sz > 19: banner = sz; continue
                if i == 0 and not banner and sz > 17: banner = sz; continue
                if banner * 0.72 <= sz < banner - 0.5:
                    if prev and prev["p"] == i + 1 and abs(prev["sz"] - sz) < .2: prev["t"] += " " + t
                    else: prev = {"p": i + 1, "t": t, "sz": sz}; ch["h1"].append(prev)
                    continue
                prev = None
                if sz < 8.5 and t.upper() == t:
                    m = re.match(r"^(CASE|GUESSTIMATE|QUESTION) ([\d.]+) · (.+)$", t) or re.match(r"^(FRAMEWORK) ()· (.+)$", t)
                    if m: ch["labels"].append({"p": i + 1, "kind": m.group(1), "num": m.group(2), "t": m.group(3)}); continue
                    if "·" in t and len(t) < 70:
                        k = t.split("·")[-1].strip()
                        ch["kick"].setdefault(k, i + 1)
    out.append(ch); print(code, len(d), len(ch["h1"]), len(ch["labels"]), list(ch["kick"])[:8])
old = json.loads((HERE / "index.json").read_text(encoding="utf-8")) if (HERE / "index.json").exists() else []
new = {c["code"]: c for c in out}
out = [new.get(c["code"], c) for c in old] or out
(HERE / "index.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
