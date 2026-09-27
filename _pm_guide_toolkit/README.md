# _pm_guide_toolkit: what each file is

These are tools and notes from the first attempt at the guide (Claude Cowork session, 24 Sep 2026). Reuse whatever helps, and improve or replace what doesn't. The source PDFs sit one folder up.

| File | What it is | Status |
|---|---|---|
| `../CLAUDE.md` | The brief for Claude Code, read automatically each session (with `../PROGRESS.md` and `../FEEDBACK.md`) | Current |
| `MASTER_PROMPT.md` | Old brief; now only points to CLAUDE.md | Superseded |
| `scoping_evidence.md` | Opening questions from all 72 cases, used to validate the scoping kit | Current |
| `research_notes_sep2026.md` | Researched facts (Sep 2026) on all ISB-listed products, PM resources and learning science, with sources | Useful; re-verify any number you publish |
| `selection.py` | The chosen cases: sector, type, source PDF, page numbers, title, level. Also the 14 guesstimates | Current (12 per type max) |
| `cases2.py` (+ `cases.py`) | Pulls case text out of the IIM A / IIM B PDFs in the right reading order and labels who is speaking (white text = interviewer, black = candidate). Rebuilds tables with `find_tables()` | Works well; see note below |
| `make_cases.py` | Example of turning 6 fintech cases into HTML with margin notes and a "coach's verdict" | Reference only |
| `dia.py` | First-attempt SVG diagram library (steps, loops, matrices, waterfalls, phone screens, graphviz architecture…) | The user found these too generic. Improve heavily or draw bespoke SVGs |
| `build.py` + `style.css` | Markdown → HTML → PDF pipeline (Chromium via Playwright; two passes for contents page numbers) | Reference; the design must change (see prompt) |
| `../PM Learner's Casebook (drafts)/` | Draft Part II (product teardowns) and Part III (technology) as PDFs and Markdown (zip) | Research material only; rewrite |

Needs: Python 3.10+, `pip install pymupdf playwright markdown pillow`, then `python -m playwright install chromium`. Graphviz is optional.

Note on case extraction: a few IIM B pages mix diagrams with text. `cases2.segments()` handles text and tables. For the pages listed in CLAUDE.md §4 as having pictures or flowcharts, crop that region as an image, or redraw it as a clean diagram.
