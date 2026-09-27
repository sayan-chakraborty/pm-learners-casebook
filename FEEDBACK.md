# FEEDBACK.md: my reactions after reading each module

Claude Code: read this before every session and apply every point to new work. Don't edit my notes, but you may add "Applied in M<n>" after an item.

## General (applies everywhere)
- Diagrams must be descriptive and intuitive enough to teach on their own.
- Simple, human language with lots of real-life examples, Indian where possible. Theory comes after the example.
- Technology explained from a PM's point of view, with light maths only where it builds intuition.
- Compact textbook layout with little wasted white space.

## After S0
- 

## After M1
- 

## Lessons learned while building (added by Claude at the owner's request; apply in every module)

### From the owner during M1 (25 Sep 2026)
- **No module codes or signposting.** Pages never say "M1", "Module 1 of 9", "this module/primer" or "the tech block". No "what this module covers" map, no framework-list blurbs, no "(Case 1.2)" or "see below" pointers. It reads as AI-generic. Put the useful content in place. Case and figure numbers stay as labels. Applied in M1.
- **No real screenshots in teardowns.** Downloading them costs too many tokens; use SVG redraws of screens only. Applied in M1.
- **Teardowns may run longer** than the ~2–3 pp guide when the content earns it.
- **No screen mockups in teardowns.** Tell the walkthrough in words, with a "behind the screens" flow diagram: numbered steps across user, app, bank, NPCI, lender and merchant, with what flows between them. Other teardown diagrams should also explain flows (loops, money, how it earns). Applied in M1.

### Build and layout
- Long boxes (framework boxes, scoping kit) must be allowed to break across pages (`.box.fw`, `.flowbox`), and long tables need `class="tbl flow"`. Otherwise a single unbreakable block jumps to the next page and leaves a half-empty page. Keep figures, tables and kit cards unbreakable.
- After every build, run `src/common/fill.py` on the PDF to catch short pages, then look at every page with a figure. Use a contact sheet (`sheet.py`) only for layout; zoom single pages to check labels.
- A figure inside a framework box can strand white space at the foot of a page. If the figure illustrates an answer turn, place it next to that turn and reference it from the box.
- The cold open goes at the top of the primer page, under a plain sector banner, never on a page of its own.

### Diagrams (SVG)
- SVG arrow markers scale with stroke width. For thick "force" arrows, draw polygon arrows by hand.
- Text budgets at 10.5 px:
  - a 120-unit box fits about 18 characters per line
  - a 106-unit chevron fits about 16 characters
  - right-edge axis labels need `text-anchor="end"`
- Two notes that share a row will collide. Stack them on two lines and enlarge the viewBox instead of shrinking the text.
- Label curves where they are far apart (usually the left ends), not where they converge.
- CSS `svg.d text{fill}` overrides a `fill=""` attribute on `<text>`, so coloured or white-on-dark labels silently turn black. The build now moves text fills into inline styles (`booklib.text_fill_to_style`). Always check dark boxes, such as code blocks, after a build.
- In Python heredocs, write regexes as raw strings. `` in a normal string becomes a backspace character and silently breaks the pattern.

### Cases
- Casebook pages sometimes repeat turns (A294) or reprint the question as a running header (B111). Remove repeats with a visible editorial note, and drop headers with `drop=`. Never silently rewrite the candidate's words.
- A recurring, high-value "what was missing" point: check whether the candidate's idea already exists in India. Examples: business correspondents, UPI 123Pay, RBI card controls, UPI Circle.
- Scoring the candidate's own ideas with real RICE numbers often flips their order. That is a strong teaching moment; reuse it.
- Size the problem before designing, using official data. In the fraud case, UPI fraud cases outnumbered card fraud cases about 9 to 1, and that one fact redirected the whole answer.

### From M3 (25 Sep 2026)
- **Owner: explain stronger answers and frameworks in more detail, simply.** Every candidate turn gets a "Why this move"; maths as a spelled-out chain; a closing "How the answer hangs together" box; every framework gets "Using it, step by step" + "Common slip". Applied in M3.
- Half-width figures (`.figrow`) need SVG viewBox width 330, or their text prints at half size.
- Never put HTML tags such as `<i>` inside SVG `<text>`: the SVG breaks and its text spills onto the page.
- Figure keys must be unique across parts (a primer `mix` and a case `mix` gave two figures the same number); the M3 build now warns.
- Place a framework's figure after its step list so text fills the page before a figure that won't fit.

### Research and numbers
- `research_notes_sep2026.md` contains arithmetic errors: profit per client was off by 10×. Recompute every derived number from its sources, and log conflicts under "Unverified" in research.md only if needed.
- For every company number, prefer company results or Parliament and RBI data over aggregator blogs. Where sources conflict (Zerodha FY26 PAT ₹4,283 Cr vs ₹4,238 Cr), round and say "about".

### From M6 (27 Sep 2026)
- A box that holds a figure (e.g. a comparison box with a loop diagram) must be `box ex flowbox`, or it jumps whole to the next page and leaves a gap.
- No cross-chapter pointers such as "the encryption chapter" or "the table above": restate the idea in one line where it is needed.
- Casebook pages printed in two columns (B144) can come out as one giant table; set the turns out by hand in reading order, in the casebook's words, with a visible editorial note.
- Check headline "viewers" numbers: press figures like "82 crore viewers" are reach, not concurrency; use the official peak-concurrency figure.

### From M8 (27 Sep 2026)
- `seq` diagrams: a long label on a step leaving the first lane is clipped at the left edge, and actor subtitles over about 20 characters overflow their box. Keep both short.
- Half-width `figrow` figures need viewBox 330 (the triangle at 680 printed at half size). Use `vbars(vw=330)` for small charts, or make the figure full width.
- When a tall figure jumps a page, move it after the next turn's "Why this move" note (`src/M8/mvfig.py`), not before its reference.
- Check company numbers against the company's own release: Amplitude's NRR was 103% reported, not the 105% pro forma quoted in coverage.
- The pointer scan (below / above / that follows) also flags ordinary uses such as "above ₹5,000"; reword them to "over" or "under" so real pointers stand out.

### From M9 (27 Sep 2026)
- `stacks(title=...)` draws its legend on top of the title; pass `title=None` and put the title in the caption.
- Tall `seq` flows can be tightened with `row=21` when a page is a few lines too long.
- Figure tags such as “part III” are cross-chapter pointers; label each box with the mechanism instead (“caching”, “idempotency”).
- Check a vendor’s own store for current prices before quoting launch prices: Apple’s India list prices for HomePod had risen well past their launch prices by Sep 2026.
