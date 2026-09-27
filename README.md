# PM Learner's Casebook

A learner's guide for product-management interviews, built in September 2026 for PM placements at XLRI. Nine sectors, each with a sector primer, real interview cases in Q&A form, product teardowns and a technology block, plus a chapter on behavioural interviews.

**Start here:** [`PM Learner's Casebook/PM Learner's Casebook (complete).pdf`](PM%20Learner's%20Casebook/PM%20Learner's%20Casebook%20(complete).pdf) is the whole book in one file (392 pages), with a clickable contents page, a detailed index (cases, guesstimates, frameworks, products, technology, behavioural questions) and PDF bookmarks. Each chapter is also available as its own PDF in the same folder.

| # | Chapter |
|---|---|
| 1 | Payments & fintech |
| 2 | Food delivery & quick commerce |
| 3 | E-commerce & marketplaces |
| 4 | Mobility, maps & travel |
| 5 | Social, creators & messaging |
| 6 | Streaming, music & entertainment |
| 7 | Health, fitness & learning |
| 8 | SaaS, productivity & enterprise AI |
| 9 | Consumer hardware, loyalty & public services |
| 10 | Behavioural interviews |

## Please read this first

- **This is a work in progress and has not been verified.** It was written quickly, one chapter at a time. There will be mistakes, inconsistencies and numbers that are off.
- **It was prepared in September 2026.** Market shares, company results, prices and regulations change fast, so over time the data will go stale. Check any figure against a current source before you quote it.
- **Anyone can make changes here.** Clone it, fork it, fix what's wrong, update what's stale, add sectors or cases, and open a pull request. You don't need to ask first.
- It's for learning. The aim is to get curious about the products around you, how they help people (and sometimes make lives worse), and what their second-order effects are, not only to pass an interview.

## How to change and rebuild it

Each chapter is written as HTML parts plus small Python scripts that draw the diagrams, and is rendered to PDF with Chromium (Playwright).

```bash
pip install pymupdf playwright markdown pillow
python -m playwright install chromium
python "PM Learner's Casebook/src/M1/build.py"        # rebuild one chapter (M1 to M9, F2)
python "PM Learner's Casebook/src/F3/extract.py"      # re-read headings from the chapter PDFs
python "PM Learner's Casebook/src/F3/build_book.py"   # rebuild the complete book, contents and index
```

- `PM Learner's Casebook/src/<chapter>/parts/`: the text of each chapter.
- `PM Learner's Casebook/src/<chapter>/research.md`: the sources and dates behind the numbers.
- `PM Learner's Casebook/src/common/`: the shared stylesheet and build helpers.
- `CLAUDE.md`, `PROGRESS.md`, `FEEDBACK.md`: the brief, the build log (including facts that couldn't be verified) and the reviewer's feedback.
- `_pm_guide_toolkit/`: scripts that extract the casebook cases.

## Credits

- Researched, written, illustrated and typeset by **Claude** (Anthropic), working in Claude Code, under Sayan Chakraborty's direction and review.
- Interview cases reproduced from ***Product Mindset 2026–27*** (ProdMan Club, IIM Ahmedabad) and ***Sigma PM Casebook 2026–27*** (IIM Bangalore). The cases and candidates' answers belong to their authors and the clubs that published them.
- ***BTC Handbook 2026*** (ISB): approach chapters and 2026 interview reports, used for ideas and for counting the behavioural questions actually asked.
- **Lenny's Podcast**: the teaching style of example boxes and "when it breaks".
- Public sources (company results, NPCI, RBI and other regulators, engineering blogs, news) are cited and dated under each figure.

If you own any of the material above and want it changed or removed, please open an issue.
