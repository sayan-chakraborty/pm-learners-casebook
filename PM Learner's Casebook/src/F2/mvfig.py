"""usage: python mvfig.py part.html figkey 'anchor text'  -> moves <figure>{{SVG:figkey}}...</figure> to after the </p> that closes the paragraph starting with anchor"""
import pathlib, re, sys
p = pathlib.Path(sys.argv[1]); s = p.read_text(encoding="utf-8")
fig = re.search(r'<figure[^>]*>\{\{SVG:%s\}\}.*?</figure>\n' % re.escape(sys.argv[2]), s, re.S).group(0)
s = s.replace(fig, "", 1)
i = s.index(sys.argv[3]); j = s.index("</p>", i) + 4
s = s[:j] + "\n" + fig + s[j:].lstrip("\n")
p.write_text(s, encoding="utf-8")
print("moved", sys.argv[2])
