# PROGRESS.md: PM Learner's Casebook

Claude Code: read this at the start of every session and update it at the end (see CLAUDE.md §2). Keep it short and factual.

## Status board

| Step | Part A: primer + cases | Part B: teardowns + technology | Final PDF | Pages | Notes |
|---|---|---|---|---|---|
| S0 Style check | n/a | n/a | ☑ approved 25 Sep 2026 | 8 | `S0 - Style sample.pdf` |
| M1 Payments & fintech | ☑ 25 Sep 2026 | ☑ 25 Sep 2026 | ☑ (awaiting owner review) | 43 | `M1 - Payments & fintech.pdf`, 50 figures |
| M2 Food delivery & quick commerce | ☑ 25 Sep 2026 | ☑ 25 Sep 2026 | ☑ (awaiting owner review) | 43 | `M2 - Food delivery & quick commerce.pdf`, 49 figures |
| M3 E-commerce & marketplaces | ☑ 25 Sep 2026 | ☑ 25 Sep 2026 | ☑ (awaiting owner review) | 40 | `M3 - E-commerce & marketplaces.pdf`, 44 figures |
| M4 Mobility, maps & travel | ☑ 26 Sep 2026 | ☑ 26 Sep 2026 | ☑ (awaiting owner review) | 46 | `M4 - Mobility, maps & travel.pdf`, 49 figures |
| M5 Social, creators & messaging | ☑ 26 Sep 2026 | ☑ 26 Sep 2026 | ☑ (awaiting owner review) | 42 | `M5 - Social, creators & messaging.pdf`, 52 figures |
| M6 Streaming, music & entertainment | ☑ 27 Sep 2026 | ☑ 27 Sep 2026 | ☑ (awaiting owner review) | 40 | `M6 - Streaming, music & entertainment.pdf`, 46 figures |
| M7 Health, fitness & learning | ☑ 27 Sep 2026 | ☑ 27 Sep 2026 | ☑ (awaiting owner review) | 43 | `M7 - Health, fitness & learning.pdf`, 50 figures |
| M8 SaaS, productivity & enterprise AI | ☑ 27 Sep 2026 | ☑ 27 Sep 2026 | ☑ (awaiting owner review) | 37 | `M8 - SaaS, productivity & enterprise AI.pdf`, 60 figures |
| M9 Consumer hardware, loyalty & public | ☑ 27 Sep 2026 | ☑ 27 Sep 2026 | ☑ (awaiting owner review) | 40 | `M9 - Consumer hardware, loyalty & public services.pdf`, 64 figures |
| F1 Guesstimates | n/a | n/a | dropped | | Owner, 25 Sep 2026: 2 guesstimates per module in M3–M9 instead |
| F2 Behavioural | n/a | n/a | ☑ 27 Sep 2026 (awaiting owner review) | 12 | `F2 - Behavioural.pdf`, 10 figures |
| F3 Merge into one book | n/a | n/a | ☑ 27 Sep 2026 | 392 | `PM Learner's Casebook (complete).pdf`: cover, preface, linked contents and index, bookmarks |

## Next step
F2 Behavioural: the plan is saved in `src/F2/plan.md`. At the start of that session, show the saved plan in chat and wait for the owner’s “go”. Reuse `src/M9/build.py` (EXTRA scan with pointer patterns) and `figlib.py` (shared helpers: box, vbars, curves, etree, stacks, ladder, arr) as the starting kit. After F2, F3 (optional merge) remains.

## Session log (newest first)

### 2026-09-27: F3 merged book complete
- Owner: merge all 10 PDFs; detailed index with page links; cover "Prepared for: Sayan Chakraborty" with the XLRI logo (`XLRI Logo.webp`); preface crediting Claude and the casebooks, saying the guide is exhaustive and for learning (curiosity about products, harm, second-order effects), explaining the case structure and asking readers to critique the stronger answers and build their own frameworks. Cover redone in an Economist style after "design is bad"; the title stays "PM Learner's Casebook".
- Built: `src/F3/extract.py` (headings, case/guesstimate/framework labels and section kickers from each chapter PDF → index.json; heading size relative to each chapter's title), `build_book.py` (cover + preface + contents + index, all linked; book-wide page numbers stamped over each chapter footer; 172 bookmarks). 392 pages; 36 cases, 14 guesstimates, 43 teardowns.
- Then: published to a public GitHub repo at the owner's request (everything in the folder, including the source casebook PDFs, the owner's explicit choice after a warning about redistribution). README says it is unverified, a work in progress, prepared in Sep 2026 (data will go stale), and that anyone may change it.

### 2026-09-27: F2 Behavioural complete
- Owner at start: "No AI" (confirmed = nothing reads as AI-written; no made-up answer presented as real), keep it simple, example answers from actual interviews, under 20 pages. Plan v2 in `src/F2/plan.md`. Mid-build: cold open removed ("looks bad"). All recorded in CLAUDE.md.
- Evidence: own count of ISB BTC Handbook 2026 interview reports (pp. 69–177): 285 of 585 rounds behavioural/HR/resume, 57 companies (`src/F2/btc_theme_counts.txt`). Real questions quoted with company and page; real candidate answers found in the reports (Practo CAC, Practo curiosity cues, Microsoft "why Microsoft", HiLabs one word and ChatGPT prep, Mastercard startup answer that ended the round, Salesforce founder/CFO) shown as summarised "From a real interview" boxes. Worked answers labelled "Example answer (written for this guide)". Published real answers online were paywalled or blocked (logged in research.md).
- Built: 12 pp, 10 figures, 0 style hits. How the round runs (real-data chart, scorecard) → story bank (sources table, six stories, filled story card, story × question grid) → STAR box → 11 questions (deep-dive, TMAY, why PM, why this company, prioritise/say no, conflict, strengths/weaknesses, failure/criticism, influence, 5 years, AI use) → stress rounds, curveballs, answer length, questions to ask → connect the dots.
- Output: PM Learner's Casebook/F2 - Behavioural.pdf. Build: `python "PM Learner's Casebook/src/F2/build.py"`.
- Short page: p8 (79%). Unverified: company attribution for a few quotes is by page only (cited as "2026 report, p. N").

### 2026-09-27: M9 complete
- Owner said “Start with M9. Refer to all the readme files and plans”, read as “go” on the revised plan in `src/M9/plan.md` (Intuit deep dive, Tata Neu, DigiLocker; no Apple, Alexa or Samsung teardowns).
- Built: 40 pp, 64 figures, 0 banned-word, extra-phrase, pointer or em-dash hits.
  - Primer (5 pp): Lucknow cold open (Ananya’s AirPods vs voting; NeuCoins; DigiLocker at a traffic check); HomePod mini ₹15,900 waterfall; two ways to earn from a device (Apple vs Echo); ecosystem web and attach rate; life of a loyalty point (₹1 lakh × 5%, 70% burn, 30% breakage); cross-brand settlement flow; India Stack layers; download-to-extra-vote funnel; metrics table; turnout and Tata Digital charts; loyalty Check (“points make customers loyal” Overstated, coffee-card goal gradient); timeline; mechanics; interview box.
  - Cases (about 12 pp): 9.1 voter turnout (A245–246; metrics tail set out from a layout table with a note; Check “users vs non-users” Doesn’t hold up; can’t / won’t / forgot; journey with leaks; 18,000 × 3% = 540 votes, holdout 4,300; **EAST nudges** box with vitamins analogy and evidence bars). 9.2 Apple speaker pricing (B93; Check “30% premium” Doesn’t hold up; iPhone homes; cost floor ₹8,450; profit at four prices, ₹12,900 ≈ ₹15,900 in 57% more homes; variants table; Key idea). 9.3 Tata loyalty (A285–286; bullets re-split; Check on the mobile number as ID Directionally right; Tata Neu already exists; flat 5% = ₹1,500 Cr needing +15% sales vs ₹340 Cr / +3.4%; settlement flows by brand; **PR-FAQ + pre-mortem** box with a wedding-toast analogy and a sample press release).
  - Guesstimates (about 4 pp, flowing on after the cases): reminder + key idea “users are not active users; an hour is not a day ÷ 24”; G9.1 food-delivery users (A239; segmentation list set out from a layout table; market 1.3 crore vs app ~50 lakh; checked against iFood orders per person); G9.2 Swiggy orders per hour (B142; 53,000 average, 1.6 lakh at 9–10 pm; checked against Swiggy’s 11.45 crore quarterly food orders; casebook ~40% high).
  - Teardowns (about 10 pp): Intuit deep dive (company page, timeline, product map, FY26 revenue by product, data flywheel; TurboTax flow, features, price ladder, season chart, “free” ads When-it-breaks; QuickBooks flow, money stack, India-exit example; IES consolidation waterfall and plan ladder; Credit Karma flow; Mailchimp; Intuit Assist payments-agent flow; strengths/weaknesses; build-next ideas); Tata Neu (earn-and-burn flow, card as what worked, refocus); DigiLocker (issuer-to-verifier flow, issued vs uploaded, ONDC comparison); side-by-side table; how-often × who-pays 2×2; interview box.
  - Technology (about 8 pp): restaurant analogy table; A. mobile releases (web vs mobile, version adoption curve, minimum version, server-driven screens); B. feature flags (flag flow, four kinds, kill-switch chart with 70 extra failures, Knight Capital); C. staged roll-outs (Apple 7-day phased release with gates, crash maths 2.1 lakh extra a day, CrowdStrike); D. observability (courier metrics/logs/traces, slow-payment trace, burn-rate alert); E. capstone Tatkal (temple-queue picture, 10 am demand, whole-system diagram, waiting room, seat hold with holds = rate × time, idempotent payment, async queue, degradation ladder, morning dashboard, PM trade-offs table). In-the-interview box per topic.
  - Connect the dots (1 p) with a sketch answer to the cold open and a numbers table.
- Output: PM Learner's Casebook/M9 - Consumer hardware, loyalty & public services.pdf (40 pages). Build: `python "PM Learner's Casebook/src/M9/build.py"` (PARTS=1,2 etc.; set PYTHONIOENCODING=utf-8 on Windows). Shared figure helpers now in `src/M9/figlib.py`.
- Dropped case (plan): Samsung Galaxy Buds (A264–266). Dropped teardowns (owner): Apple ecosystem, Amazon Alexa/Echo, Samsung Galaxy. IoT dropped (owner, 26 Sep). Named in one line only: holdouts, tiered and value-based pricing, North Star and guardrails, SLOs and error budgets, caching, idempotency, graceful degradation.
- Moved topics: none. The capstone names each earlier mechanism in one line and teaches only the new pieces (virtual waiting room, seat holds with timers).
- Scoping evidence: M9 patterns added (“what exists today” skipped again in A245 and A285; goal conflict share vs profit in 3 pricing cases, already an add-on; guesstimate card 5 skipped 14 of 14). No kit change.
- Unverified: see src/M9/research.md (iPhone 15 vs Pixel 8 launch prices; Apple FY25 services; election-experiment effect sizes; ECI figures; TurboTax $141 mn settlement and FTC ruling; Direct File status; DigiLocker legal rules; QuickBooks US prices; iPhone share in India). HomePod prices (₹15,900 / ₹44,900) are from Apple’s India store as fetched in Sep 2026 and are higher than earlier launch prices. All speaker costs, demand and profit curves, loyalty economics and settlement flows, turnout lifts, release, crash, latency and Tatkal numbers are labelled illustrative. Intuit’s QuickBooks online / desktop / Mailchimp split is derived from segment totals.
- Short pages (section ends only): p5 primer end (69%), p31 teardowns end (71%), p40 connect (80%).
- Next: F2 Behavioural (separate session; show the saved plan first).

### 2026-09-27: M9 planned
- Plan written to `PM Learner's Casebook/src/M9/plan.md` and shown in chat. Cases: 9.1 voter turnout (A245–246, EAST box), 9.2 Apple smart-speaker pricing (B93, no box), 9.3 Tata Group loyalty (A285–286, PR-FAQ + pre-mortem box). Dropped: Samsung Galaxy Buds (A264–266). Guesstimates A239 + B142. Case texts dumped to src/M9/cases_raw.txt. Nothing built yet.
- Owner, same day: **add an Intuit teardown with its products** (sixth teardown); recorded in CLAUDE.md → Design decisions.
- Owner, plan review: **Intuit as a deep dive, including Intuit Enterprise Suite (IES)**; **remove the Apple, Alexa/Echo and Samsung teardowns**. Teardowns now: Intuit (~10 pp, each product), Tata Neu, DigiLocker. Plan revised; recorded in CLAUDE.md.
- Next: owner’s “go” on the M9 plan, then build.
- F2 Behavioural also planned (owner asked; to be built in a separate session): `src/F2/plan.md`. How the round works → story bank (sources by background, story card, 7 × 10 story grid) → STAR box → the 10 questions (~2 pp each: what it tests, move strip, worked Q&A with follow-ups, where to find the story in any background, follow-ups, traps) → project deep-dive → company flavours → delivery and curveballs → 15 quick-fire questions → connect the dots. About 30–35 pp.

### 2026-09-27: M8 complete
- Owner said “M8 Start” (twice); read as “go” on the plan. Before building, the plan was re-checked against CLAUDE.md and four amendments appended to `src/M8/plan.md` (In-the-interview box per tech topic; real RAG and agent test cases with scores; no re-teaching of M1–M7 ideas; no pointers in print). The new PROGRESS note (“show the saved plan in chat before treating start as go”) was only seen at the end of the session: the amendments were shown in chat, the full plan was not.
- Built: 37 pp, 60 figures, 0 banned-word, extra-phrase, pointer or em-dash hits.
  - Primer (5 pp): Gurugram cold open (Karan’s 40 minutes of CRM notes, ₹1.2 Cr forecast miss, a ₹1,500-a-seat copilot, an AI bill that doubled); who buys, uses and can say no; seat economics with and without AI (₹1,000 → 80% vs 65% margin); CAC payback 15 vs 18.5 months; NRR worked (₹24 L → ₹30 L = 125%); metrics table (ARR, NRR, gross retention, logo churn, seat utilisation, expansion, CAC payback); cloud growth and Copilot seats; eight-date timeline; renewal cliff (₹9.6 L lost); seat vs use vs outcome pricing.
  - Cases (about 11 pp): 8.1 AI copilot (A267–268; MVP list, safeguards and metrics set out by hand from layout tables with a visible note; PM tip omitted with a note; Check on Brynjolfsson et al. “Directionally right”; 7,200 tickets × 1.2 min = 144 hours a day; minutes breakdown; grounded-draft flow; escalation threshold 90% vs 97% recall; Key idea “confidence from evidence”). 8.2 CRM adoption (A311–312; PM tip omitted with a note; Check on tenured reps “Overstated”; issue tree; 12 clicks → 3 taps; leading vs lagging panels; **buyer vs user** box with a school-uniform analogy and a value-flow figure). 8.3 AI sales assistant GTM (A283–284; Check on usage pricing “Directionally right”; India edges: phone and WhatsApp calls, Hinglish, DPDP consent; pilot with pass marks; ₹25 a call hour, break-even 48 hours, hybrid ₹1,200 + 30 hours; ~₹7.8 Cr add-on sizing; **sales-led vs product-led with seat vs usage pricing** box, gym and phone-plan analogy).
  - Guesstimates (about 4 pp, flowing on after the cases): reminder + key idea “stored is not the same as offered”; G8.1 Google Photos (B137; swapped file sizes ~2.4× too big; ~2,000 PB a year; checked against Google’s 28 bn items a week, 2020); G8.2 Drive Singapore (B139; skewed use ~16–20 GB not 60%; ×2 copies +20% headroom ≈ 280,000 TB vs casebook 580,800; checked against Photos’ ~9 GB a user); storage numbers table; author’s practice question (a year of UPI records ≈ 3 PB) with a tree.
  - Teardowns (about 7 pp): cloud trio (Diwali-sale autoscaling flow; revenue and margin charts), Amplitude (KYC-funnel flow; land-and-expand ladder), ThoughtSpot (plain-words query flow; words-to-columns figure), Gmail and Workspace (supplier-email flow; plan ladder), Microsoft 365 Copilot (Graph-grounded answer flow; seat arithmetic); side-by-side table; sold × priced 2×2; Zoho five-questions box.
  - Technology (about 11 pp): Priya analogy table; RAG (pipeline, chunking, embeddings and similarity, hybrid + re-rank 74% → 86%, grounded prompt before/after, freshness and permission filters, four failure cards, PM decisions); agents (loop, function calling with a ₹1,833 pro-rata trace and approval, stopping rules, permission ladder, one vs many agents, ₹6 → ₹90 retry loop); MCP (host/client/server, two-server trace, 100 → 25 connectors, risks, “ship an MCP server” decision); evals for RAG and agents (RAG test case, 17/7/4 failure split, agent test case, 50-task scorecard with unsafe action blocking launch, regression table for a cheaper model, five failure buckets); cost and latency (₹22 real cost per ticket, median vs p95, triangle with routed set-up at ₹1.11, levers). In-the-interview box per topic.
  - Connect the dots (2 pp) with a sketch answer to the cold open and a numbers table.
- Output: PM Learner's Casebook/M8 - SaaS, productivity & enterprise AI.pdf (37 pages). Build: `python "PM Learner's Casebook/src/M8/build.py"` (PARTS=1,2 etc. for subsets; set PYTHONIOENCODING=utf-8 on Windows).
- Dropped cases (plan): Improve PowerPoint (B128–129), AI email-summary metrics (A293), AI chatbot abandonment (A313–314; its five failure buckets are content in the evals section). Dropped framework boxes: JTBD for B2B, ICP and land-and-expand (named in answers), AI failure taxonomy (content). Low-code/no-code dropped (owner).
- Moved topics: none. Named in one line only: human-in-the-loop, precision/recall, cosine, unit economics/CAC, golden sets, rubrics, AI judges, prompt injection.
- Scoping evidence: M8 patterns added (what exists today now 13–14 cases; edges decided the target segment in A283; buyer vs user 2 cases; guesstimate card 5 weak in 12 of 12). No kit change.
- Unverified: see src/M8/research.md (Google Cloud margin and market shares from secondary coverage; Microsoft 365 seat total; Gmail 3 bn; ThoughtSpot ARR only from 2023). Amplitude NRR corrected to 103% (reported) from the 8-K. All deal sizes, margins, ticket volumes, timings, AI costs, eval scores, latency figures and pilot numbers are labelled illustrative.
- Short pages (section ends and one teardown page): p4 primer end (65%), p19 guesstimates end (74%), p22 Amplitude/ThoughtSpot (70%), p26 teardowns end (73%), p37 connect (71%).
- Next: M9 plan.

### 2026-09-27: M8 planned
- Plan written to `PM Learner's Casebook/src/M8/plan.md`. Cases: 8.1 AI copilot for support agents (A267–268), 8.2 Low CRM adoption (A311–312), 8.3 AI sales assistant GTM in India (A283–284). Dropped: Improve PowerPoint (B128–129), AI email-summary metrics (A293), AI chatbot abandonment (A313–314; its failure buckets go into the agent-evals section as content). Guesstimates B137 + B139. Case texts dumped to src/M8/cases_raw.txt. Nothing built yet.
- Framework placement: buyer vs user (8.2); sales-led vs product-led growth with seat vs usage pricing (8.3). 8.1 has no box; it is the running example for RAG, agents and their evals in the tech block.
- Owner, same day: technology should be **more detailed**, and **drop low-code and no-code** (IIM A p. 134). Plan revised (tech ~13–14 pp: RAG, agents, MCP, RAG/agent evals, cost and latency); recorded in CLAUDE.md → Design decisions.
- Next: owner’s “go” on the M8 plan, then build.

### 2026-09-27: M7 complete
- Owner said “Start with M7”, read as “go” on the plan written earlier the same day.
- Built: 43 pp, 50 figures, 0 banned-word, extra-phrase or em-dash hits.
  - Primer (5 pp): Indore cold open (22-question app vs a 212-day streak; the Nashik clinic folder); who pays whom; three-businesses table; ₹999 coaching plan waterfall (coach ₹400 a client); gym break-even (441 members vs ~520 capacity); test-prep funnel; metrics table; players chart; seven-date timeline; New Year cliff; outcome vs streak; the rules a PM designs around (telemedicine, DPDP, ABDM consent, coaching rules, pharmacy).
  - Cases (about 14 pp): 7.1 AI assistant for doctors (B50; Check “quiet helper, not influence” Overstated; 1.5 min × 50 patients = 75 min, ~₹6,000 a morning; ABHA Scan and Share flow; **human-in-the-loop and risk tiers** box, hospital-pharmacy analogy). 7.2 HealthifyMe early drop-off (B97; turns re-joined from a split page with a visible note; Check on Google Fit sync Overstated; funnel before/after; aha curves; **Fogg B = MAP** and **activation and the aha moment** boxes). 7.3 Duolingo 15% fall (A303–304; Check “can one US iOS test explain 15%?” Directionally right; driver tree; quit-screen chart; flag off first; **reading an A/B test** box with tea-stall analogy, SRM, CI chart, novelty curve).
  - Guesstimates (about 5 pp): reminder + key idea “count the right unit”; G7.1 Zoom India traffic (A237–238; both directions, ~4,800 TB vs casebook 20,000 TB; checked against Zoom’s 3.3 trillion minutes); G7.2 Meet calls a day (B143; joins ÷ people per meeting ≈ 6 Cr vs casebook 168 Cr; checked against Google’s 10 Cr daily participants); a “numbers worth remembering” table.
  - Teardowns (about 9 pp): Duolingo (Birdbrain + reminder flow, habit loop), HealthifyMe (photo-log flow, plan ladder), Cult.fit (waitlist flow, franchise vs own), Practo with Tata 1mg (appointment flow, four payers), PhysicsWallah (YouTube → batch → centre flow, FY25→FY26 chart); side-by-side table; how-often × who-delivers 2×2.
  - Technology (about 9 pp): LLMs and prompting (intern analogy table; tokens incl. Hindi tokenisers and a clinic cost chain ₹2,500 → ₹750 a month; next-word bars; attention; training stages; temperature; context window and lost-in-the-middle; hallucination with Mata v. Avianca and Air Canada; before/after prompt). Evals in depth (eval loop; golden-set test case; rubric with critical criteria; code checks, doctors and an AI judge with 88/100 agreement; offline vs online; regression table where −1.3 overall hides −13 on handwriting; red-team set). Guardrails (six layers on the metformin question; unsafe vs wrongly refused; prompt injection; personal data).
  - Connect the dots (1 p) with a sketch answer to the cold open.
- Output: PM Learner's Casebook/M7 - Health, fitness & learning.pdf (43 pages). Build: `python "PM Learner's Casebook/src/M7/build.py"` (PARTS=1,2 etc. for subsets; set PYTHONIOENCODING=utf-8 on Windows).
- Dropped cases (plan): Adobe LMS trial-to-paid (B78–79), Social fitness launch (A278–279). Launch phases not used. Named in one line only: RICE, North Star, guardrails, retention cohorts.
- Moved topics: none. A/B testing depth is the Case 7.3 framework (reading a test); the tech block names online A/B tests of AI features in one line. Human-in-the-loop taught in Case 7.1, only applied in guardrails.
- Scoping evidence: M7 patterns added (what exists today 11–12 cases; data trustworthiness now 3 cases, already an add-on; new “does the cause add up to the whole fall?”; guesstimate unit errors 6 cases). No kit change.
- Unverified: see src/M7/research.md (“Can’t speak now” pause length; GLP-1 launch dates; Healthify–Berry Street merger; Zoom/Meet current usage (2020 figures used and dated); Duolingo’s April 2025 AI-first memo and 148 AI-built courses, from memory; Zoom bandwidth ranges rounded). All clinic timings, funnels, retention splits, A/B results, eval scores, judge agreement, token counts and prices, gym economics and fees are labelled illustrative.
- Short pages (section ends only): p24 guesstimates end (63%), p33 teardowns end (73%), p43 connect (68%).
- Next: M8 plan.

### 2026-09-27: M7 planned
- Plan written to `PM Learner's Casebook/src/M7/plan.md`. Cases: 7.1 AI assistant for doctors (B50), 7.2 HealthifyMe early drop-off (B97), 7.3 Duolingo engagement drop (A303–304). Dropped: Adobe LMS trial-to-paid (B78–79, its lessons belong to M8’s B2B frameworks) and Social fitness launch (A278–279, GTM taught in M2). Guesstimates A237–238 (Zoom) + B143 (Meet). Case texts dumped to src/M7/cases_raw.txt. Nothing built yet.
- Framework placement: HITL and risk tiers (7.1); Fogg B = MAP and activation/aha (both 7.2); reading an A/B test (7.3). Evals in depth run on the Case 7.1 clinic assistant; M8’s evals should build on them (RAG and agent evals), not repeat them.
- Next: owner’s “go” on the M7 plan, then build.

### 2026-09-27: M6 complete
- Owner said “Start with M6”, read as “go” on the plan written 26 Sep (AR/VR already removed).
- Built: 40 pp, 46 figures, 0 banned-word, extra-phrase or em-dash hits.
  - Primer (5 pp): Ahmedabad IPL-final cold open; who pays whom (rights, app, viewers, advertisers, telcos, CDNs); five ways to charge; a ₹199 subscriber’s year (waterfall); fixed-cost curve (₹2,000 Cr budget, break-even ~1.3 Cr subscribers); IPL digital rights ₹23,758 Cr → ₹58 Cr a match → ~40 ads per viewer; reach vs subscriptions vs concurrency; metrics; players; five turning points; churn-and-return; music royalties (₹67 of ₹100); cost per hour watched.
  - Cases (about 12 pp): 6.1 Improve Hotstar (B105–106; RICE redone with numbers, forum drops to the bottom; retention curves and cohorts box; ₹105 Cr a quarter renewal sizing); 6.2 Prime Video views fall (B80–81; journey redrawn from the original; views = viewers × starts × finish-rate tree; “sachet pricing” Check “Doesn’t hold up”); 6.3 Netflix pricing (A299; key catch: no paid extra member in India since July 2023; WTP test; ₹149 own plan ₹37 Cr vs ₹99 slot ₹25 Cr net; tiered pricing box with a railway-class analogy, decoy, price discrimination, family-plan worked example).
  - Guesstimates (about 4 pp): short reminder + “ad money = minutes × ads per minute × price”; G6.1 YouTube US ad revenue a day (A236; minutes-based ~$48 mn vs casebook $20 mn; checked against Alphabet); G6.2 Bhojpuri app users (B144, set out verbatim in reading order from a two-column page; triers ~1 Cr vs 20–40 lakh monthly; Census 5.1 Cr check).
  - Teardowns (about 8 pp): Netflix (Open Connect flow, flywheel), JioHotstar (ad-break flow) + Prime Video loop, YouTube (upload-to-payout flow, creator shares) + Moj/Twitch, Spotify (stream-to-royalty flow, freemium loop) + JioSaavn, Zynga (near-miss flow, LTV vs CPI, Gaming Act box); side-by-side table; pay × keep 2×2; five money models table.
  - Technology (about 10 pp): blockchain in depth (bhishi analogy table; block with real SHA-256 fingerprints; tampered chain; proof of work with a 31,312-guess laptop demo vs proof of stake; wallets and custody incl. WazirX; escrow smart contract and The DAO; uses and failures table; public vs private chains; five-question test with scored proposals). System design V in detail (dairy analogy table with 10 ideas; ~100 Tbps load; bitrate ladder with MB-an-hour maths; segments and ABR trace; CDN tiers and hit-rate maths; glass-to-glass latency budget; toss-time spike and pre-warming; server-side ad insertion; degradation ladder; on-demand; DRM and watermarks; final-night plan table).
  - Connect the dots (1 p) with a sketch answer to the cold open.
- Output: PM Learner's Casebook/M6 - Streaming, music & entertainment.pdf (40 pages). Build: `python "PM Learner's Casebook/src/M6/build.py"` (PARTS=1,2 or t1 etc. for subsets).
- Dropped cases (plan): Podcasts on Spotify (A254–255), BookMyShow engagement (A317–318), Improve YouTube (B120–121), JioSaavn family plan (A298, B92; its lesson is the family-plan example inside the 6.3 box). Dropped frameworks: Double Diamond, ICE, DHM, seasonality as a box, Van Westendorp as its own box (a simple would-you-pay test sits inside tiered pricing). AR and VR dropped (owner, 26 Sep).
- Moved topics: none. Hashing, keys and signatures named in one line in blockchain (taught in M5), not re-taught.
- Scoping evidence: M6 patterns added; “what exists today?” skipped in all 3 cases (9 across M3–M6; already card 4); new RCA habit “split the metric into its parts” (1 case). No kit change.
- Unverified: see src/M6/research.md (JioHotstar 30 crore subscriptions claim; YouTube 2025 ads “about $40 bn”; Prime Video Store, miniTV and MX Player history; X-Ray in India; Hotstar scaling talks; rebuffering study; Coca-Cola 1999; creator revenue splits). All budgets, curves, cohorts, WTP answers and system loads are labelled illustrative.
- Short pages (section ends only): p29 teardowns end (71%), p34 blockchain end (67%), p39 technology end (76%), p40 connect (69%).
- Next: M7 plan.

### 2026-09-26: M6 planned
- Plan written to `PM Learner's Casebook/src/M6/plan.md`. Cases: 6.1 Improve Hotstar (B105–106), 6.2 Prime Video views fall (B80–81), 6.3 Netflix pricing and paid sharing (A299). Dropped: Podcasts on Spotify (A254–255), BookMyShow engagement (A317–318), Improve YouTube (B120–121), JioSaavn family plan (A298, B92). Guesstimates A236 + B144. Case texts dumped to src/M6/cases_raw.txt. Nothing built yet.
- Owner, same day: **drop AR and VR** (IIM A p. 91) from the technology topics; plan revised; recorded in CLAUDE.md → Design decisions.
- Next: owner's “go” on the M6 plan, then build.

### 2026-09-26: M5 complete
- Built: 42 pp, 52 figures, 0 banned-word, extra-phrase or em-dash hits.
  - Primer (5 pp): Lucknow family-group cold open; who pays whom; one hour of Reels in ₹ (₹1.44 India vs ₹16.80 US); Meta regional ARPU (Q4 2023); WhatsApp per-message pricing worked (₹66,000 a month); metrics; players chart and table; four turning points (Jio, TikTok ban, Jan 2021 privacy scare, IT and DPDP rules); 90-9-1 pyramid; feed-ranking score worked; five mechanics.
  - Cases (about 13 pp): 5.1 LinkedIn for blue-collar workers (B46–47; network effects and cold start box; density maths, 450 households; scam checkpoints; Aadhaar Check "Overstated"); 5.2 Instagram creator product tags (A288–289; no framework box; GMV Check "Overstated", attribution Check; ₹ funnel; who-wins grid as a Key idea); 5.3 WhatsApp → Telegram (B149–150; 3 of 4 proposed features already existed, Check table "Doesn't hold up"; Jan 2021 timeline; 0.9^47 ≈ 0.7% all-move maths; switching costs and multi-homing box).
  - Guesstimates (about 4 pp): kit reminder + "India's slice of a global number"; G5.1 Instagram posts a day (A235; 38 mn → about 2.5 crore; "a third of world posts" Check "Doesn't hold up"); G5.2 WhatsApp chats a day (B136; 11 bn → about 2.6 bn, checked against 100 bn messages a day × 18%); numbers-to-remember table.
  - Teardowns (about 9 pp): Instagram (+ Threads box), Facebook + Meta ad auction (bid × chance + quality, worked) + moderation pipeline, X (+ Community Notes bridging), Snapchat, WhatsApp (+ Telegram comparison table); side-by-side table; friends/strangers × private/public 2×2.
  - Technology (about 11 pp): System design IV in detail (post-office analogy table with 10 ideas; load maths; open connection vs polling; message journey and ticks; store and forward; order and duplicates; fan-out on write vs read; push notifications; media by reference; presence; forward limits; server failure and reconnect storms; Diwali-midnight plan). Encryption in detail (who can read; hashing with real SHA-256 outputs and password-cracking maths; AES; public/private keys, 4,99,500 vs 1,000; signatures; Diffie–Hellman with paint and small numbers; in transit vs end to end; WhatsApp's Signal protocol: pre-keys/X3DH, ratchet, security codes, sender keys, linked devices, backups; what E2E doesn't hide; PM trade-offs and the traceability case).
  - Connect the dots (1 p) with a sketch answer to the cold open.
- Output: PM Learner's Casebook/M5 - Social, creators & messaging.pdf (42 pages). Build: `python "PM Learner's Casebook/src/M5/build.py"` (PARTS=1,2 or t1 etc. for subsets).
- Owner instructions this session (recorded in CLAUDE.md → Design decisions): non-AI language everywhere, with an extra phrase scan; system design detailed (reinforced at "go").
- Dropped cases: Facebook Reactions (A316), WhatsApp in-app video (A295), Gmail success metrics (B154–155). Dropped frameworks: 7 Powers, multi-stakeholder metrics, GAME, Fogg (moves to M7), Hooked as a box (loop diagram only, Instagram teardown), trust and safety as a box (answer content in 5.1).
- Moved topics: IIM A p. 111 (platform economics) taught inside Cases 5.1 and 5.3; p. 137 (trust) inside Case 5.1, the teardowns and the encryption section. Hashing, signatures and public-key basics are now taught (M5 encryption), so M6's blockchain section should name them, not re-teach them.
- Scoping evidence: M5 patterns added; "what exists today?" skipped in all 3 cases (6 across M3–M5); no kit change (it is already card 4).
- Unverified: see src/M5/research.md (Meta regional ARPU Q4 2023 from memory; India user counts vary by source; X 2025 ad revenue conflict, written "about $2 bn"; Karnataka HC Sahyog ruling Sept 2025 and WhatsApp's April 2024 "would leave India" statement from memory; Telegram's ~7 crore sign-ups during the Oct 2021 outage, per its founder). All CPMs, funnels, densities, reviewer counts and server loads are labelled illustrative.
- Short pages (section ends only): p21 guesstimates end (60%), p30 teardowns end (67%), p41 technology end (71%), p42 connect (62%).
- Next: M6 plan.

### 2026-09-26: M4 complete
- Built: 46 pp, 49 figures, 0 banned-word or em-dash hits.
  - Primer (5 pp): Outer Ring Road rain cold open; who pays whom; driver and platform waterfalls on a ₹300 ride; utilisation maths; commission vs subscription chart (break-even ~1.2 trips); metrics table; share chart; players table; timeline; fare build-up with surge; five mechanics with cancellation reasons; OTA earnings; interview questions.
  - Cases (17 pp): 4.1 Ola for schoolchildren (A250–251; MVP, build–measure–learn, riskiest assumption; van break-even maths); 4.2 Improve Google Maps (B114–115; journey redrawn from the original; Opportunity Solution Tree + HEART); 4.3 Uber cancellations (A306; supply–demand and surge; driver's-maths ₹77 vs ₹128 an hour); 4.4 MakeMyTrip enters Dubai (B151–152; TAM/SAM/SOM ₹29,000 Cr → ₹110 Cr revenue; five forces; SWOT Check "Doesn't hold up"). Key catch: MMT already runs a UAE business.
  - Guesstimates (5 pp): short kit reminder + "a fleet is sized for its busiest hour"; G4.1 Uber drivers in Bengaluru (B138; casebook 1.7 lakh → ~31,000, checked by trips per driver); G4.2 bikes for a bike-taxi firm (B140; 2,200 → ~4,000–4,400 via the peak hour; B140 tables set side by side).
  - Teardowns (9 pp): Uber, Ola (flywheel in reverse), Rapido + Namma Yatri box, Google Maps, MakeMyTrip; comparison table; frequency vs money-per-use 2×2.
  - Technology (8 pp): cloud computing (utility idea, IaaS/PaaS/SaaS pizza grid, containers, serverless, on-demand/reserved/spot cost maths ₹14.4 → ₹5.1 lakh); System design III rewritten mid-session at the owner's request: running Diwali-restaurant analogy table, then for each of 8 mechanisms an everyday picture, how it works, a real example (OVHcloud fire, IRCTC Tatkal, BookMyShow seat lock, NPCI technical declines, Netflix fallbacks and Hystrix, Uber's 2,200 services, Prime Video's move back to one program) and the PM decision; New Year's Eve plan table.
  - Connect the dots (1 p) with a sketch answer to the cold open.
- Output: PM Learner's Casebook/M4 - Mobility, maps & travel.pdf (46 pages). Build: `python "PM Learner's Casebook/src/M4/build.py"` (PARTS=1,2 etc. for subsets).
- Owner instructions this session (recorded in CLAUDE.md → Design decisions): from M5 only 3 cases; IoT dropped; blockchain (M6) and evals (M7, M8) in depth with worked examples; system design explained with everyday pictures and real examples.
- Dropped cases: Uber for kids (B39–40), Improve Uber (B96), Google Maps ETA errors (B65). Dropped framework: Ansoff (gas). Frameworks taught: see list below.
- Scoping evidence: M4 patterns added; card 5 of the guesstimate kit now names two checks (per-unit ratio + published figure), as 4 of 4 guesstimates skipped it.
- Unverified: see src/M4/research.md (several facts logged "from memory": India domestic tourist visits 2023, Google address descriptors 2024, Ola Maps ₹100 Cr saving, GCC Indians ~90 lakh, BMTC ridership, AWS Oct 2025 outage, Uber 2,200 services, Prime Video 90%, OVHcloud fire). Ride-share splits are industry estimates. All ride economics, surge curves, cancellation splits and TAM multipliers are labelled illustrative.
- Short pages (section ends only): p28 guesstimates end (70%), p34 (79%), p46 connect (70%).
- Next: M5 plan.


### 2026-09-25 (late night, cont.): M4 planned
- Plan written to `PM Learner's Casebook/src/M4/plan.md` (outline, cases and drops, guesstimates, teardowns, tech topics, frameworks, ~45 diagrams, light maths, research list). Nothing built yet.
- Added M3's scoping patterns to `_pm_guide_toolkit/scoping_evidence.md` (skipped at the end of the M3 session). No kit change: no pattern has reached 3 cases yet; the guesstimate "external check" gap is at 2 of 2.
- CLAUDE.md and FEEDBACK.md: no change (no new owner instruction).
- Next: owner's "go" on the M4 plan, then build.

### 2026-09-25 (late night, cont.): M3 complete
- Built: 40 pp, 44 figures, 0 banned-word or em-dash hits.
  - Primer (4 pp): Jaipur sale-night cold open; who pays whom; FDI Press Notes; ₹1,299 kurta kept vs returned waterfalls (₹195 vs −₹250; 30% → 20% returns = +70% per order); Meesho placed vs delivered (36% gap); funnel; metrics; players; Myntra revenue mix; timeline; five mechanics; search-ranking shelf.
  - Cases (13 pp): 3.1 AI for Myntra (B107–108), 3.2 FB Marketplace (A290), 3.3 Amazon returns (B70–71), 3.4 Prime pricing two takes (A297 + B94, one slot).
  - Guesstimates (5 pp): primer + India numbers table + the guesstimate kit (wedding-caterer analogy, 6 cards); G3.1 Google searches/s (B141), G3.2 Ahmedabad dark stores (A240–241; coverage table moved up with an editorial note), and a side-by-side table.
  - Teardowns (10 pp): Amazon, Flipkart, Myntra, Google Search + ad auction, ad tech (InMobi, Media.net, RTB); comparison table, 2×2, interview box.
  - Technology (6 pp): ML/AI fundamentals (nesting, three learning types, train/val/test, overfitting, leakage, recommender pipeline with cosine maths, neural nets, GenAI, PM decision table); precision/recall/thresholds (confusion matrix, cost-based threshold table + chart); customer funnel and brand lift (worked lift and margin of error).
  - Connect the dots (1 p) with a sketch answer to the cold open.
- Owner instruction mid-session: more detailed, intuitive stronger answers and frameworks. Applied to all M3 cases and guesstimates; recorded in CLAUDE.md.
- Dropped cases: E-commerce for seniors (B30–31), cart-add decline (A309–310), vendor negotiation (A300–301), fake products on Instagram (B146). Dropped frameworks: fishbone (gas: the issue tree covers it); BATNA (its case dropped). Moved: Cagan's four risks to Case 3.1; trust and safety to M5.
- Output: PM Learner's Casebook/M3 - E-commerce & marketplaces.pdf (40 pages). Build: `python "PM Learner's Casebook/src/M3/build.py"`.
- Unverified: see src/M3/research.md (InMobi revenue; FB Marketplace MAU; fashion return and RTO rates are industry ranges; Myntra try-and-buy's current status unknown, described as launched in 2017).
- Short pages (section ends only): p4 primer end, p25 guesstimates end, p40 connect.
- Next: M4.


### 2026-09-25 (late night): M2 complete
- Built: 43 pp, 49 figures, 0 banned-word or em-dash hits.
  - Primer (5 pp): Mumbai monsoon cold open; three-sided money flow; 3P vs 1P; minutes timeline (30 vs 10 min); ₹450 food and ₹650 basket waterfalls; density; players table; order-value chart; turning points; metrics; five mechanics; rain-night example; rider-safety Check; platform-fee worked example.
  - Cases 2.1–2.7 (23 pp), each with verbatim Q&A, what worked/missing, scoping-kit check line, Checks, move strip, stronger answer, framework box. Redrawn originals: Swiggy journeys (B126–127), Zepto four-step breakdown (B82). Closing box: five scoping patterns from these openings.
  - Teardowns (8 pp): Zomato + Blinkit (two flows), Swiggy + Instamart, Zepto, BigBasket, magicpin + ONDC, comparison table + speed-vs-range 2×2.
  - Technology (6 pp): UX design (design thinking loop, affinity map, 5-user maths, prototype ladder, Nielsen's 10 on checkout, dark patterns/CCPA 2023); System design II, expanded at the owner's request (architecture, SQL vs NoSQL, indexes, order state machine, replicas and shards, caching and stampedes, queues and worker maths, live tracking at 75,000 pings/s, geohash rider search, batch matching, consistency table).
  - Connect the dots (1 p) with a sketch answer to the cold open.
- Output: PM Learner's Casebook/M2 - Food delivery & quick commerce.pdf (43 pages).
- Build: `python "PM Learner's Casebook/src/M2/build.py"` (PARTS=1,2 or 9a,… for subsets). Figures generated in src/M2/m2_figs.py.
- Owner instructions this session (all recorded in CLAUDE.md → Design decisions): light-touch research; record every standing instruction in CLAUDE.md; from M3, 4 cases + 2 guesstimates per module and no F1 file; guesstimate kit; drop gas frameworks; detailed system design; fill gaps with depth.
- Moved topics: Little's law taught once, in Case 2.7 (not repeated in the tech block). Design thinking (EDIPT) taught in the UX tech section, so M6's podcast case should add only the Double Diamond's diverge/converge idea, briefly, or drop it as gas.
- Unverified facts: see src/M2/research.md (Zepto FY26 revenue looks high; District NOV derived; BigBasket FY25 derived; Instamart margin −0.2% vs +0.2%; Blinkit "10 minutes" branding change not re-checked).
- Short pages (section ends only): p5 (56%), p28 (64%), p38 (78%), p43 (67%).
- Next: M3 under the new rules.

### 2026-09-25 (night): M1 complete
- Built: 43 pp, 50 figures, 0 banned-word or em-dash hits.
  - Primary sections:
    - Primer (5 pp): cold open with the Surat trader, rails, the UPI flow, card fee split, MDR, a loan waterfall, players, turning points, metrics, mechanics
    - Cases 1.1–1.6 (19 pp)
    - Teardowns (11 pp): PhonePe, Google Pay, Paytm + WeChat lens, Razorpay, Groww/Zerodha/smallcase, comparison table + 2×2
    - Technology (7 pp): SDLC/Agile/Scrum/Kanban; System design I, APIs, webhooks, UPI end to end; A/B testing basics
    - Connect the dots (1 p)
- Output: PM Learner's Casebook/M1 - Payments & fintech.pdf (43 pages).
- Build: `python "PM Learner's Casebook/src/M1/build.py"`.
  - Parts are in src/M1/parts/.
  - Generated SVGs (teardown sequence flows, tail chart) are in src/M1/m1_figs.py, made with src/common/svgkit.py (seq(), plus the unused phone() and browser() walkthrough helpers).
  - booklib now also moves SVG text fills into inline styles, because CSS was overriding the fill attributes.
- Owner decisions this session (recorded in CLAUDE.md design decisions and FEEDBACK.md lessons):
  1. no module codes or signposting
  2. no screenshots
  3. teardowns use behind-the-screens flow (sequence) diagrams, not screen mockups
  4. teardowns may run longer
  - The owner then withdrew a message asking for no flow diagrams ("ignore the previous prompt"). Flow diagrams stay.
- Moved topics: none. The frameworks were placed as CLAUDE.md suggested; the scoping kit's full intro moved to Case 1.1, and Case 1.6 has the RCA version of the cards.
- Unverified facts: see src/M1/research.md, "Unverified" section:
  - Zerodha PAT conflict
  - Razorpay take-rate estimate
  - app-level UPI success rates
  - illustrative loan terms
- Short pages (section ends only): p5 (66%), p24 (63%), p35 (53%), p42 (58%).
- Next: M2.

### 2026-09-25 (evening): M1 part A built (checkpoint)
- Built: primer (5 pp, 7 figures) + Cases 1.1–1.6 (19 pp, 15 figures) = 24 pp, 22 figures. `M1 - Payments & fintech.pdf` currently holds part A only.
- Build: `python "PM Learner's Casebook/src/M1/build.py"` (PARTS=1,2 builds a subset). Parts live in src/M1/parts/*.html; shared code in src/common/ (style.css, booklib.py, dump_case.py, sheet.py, fill.py).
- Owner feedback this session, both recorded in CLAUDE.md design decisions:
  - no real screenshots in teardowns
  - no module codes or signposting (no "M1", no module map, no "(Case 1.2)" pointers)
- Unverified facts: see src/M1/research.md, "Unverified" section.
- Resume from: part B (teardowns 8_*, tech 9_*, connect 10_*).


### 2026-09-25 (later): S0 approved
- The owner approved S0. The design system is recorded in CLAUDE.md → Design decisions.
- Next: M1 part A.

### 2026-09-25 (later): teardown screenshots rule
- The owner approved real app screenshots in teardowns, alongside the SVG diagrams. The rule is recorded in CLAUDE.md → Design decisions: sources, captions, permission via the session plan, and storage in `src/<step>/img/`. S0 not rebuilt (owner: no need to redo).

### 2026-09-25 (later): S0 revision, simplicity pass
- Owner feedback: the frameworks, scoping kit and stronger answers were weak for understanding and too complicated; they need to be simpler and more intuitive, with examples.
- Rewrote, in the case section:
  - **Scoping kit:** now opens with a doctor analogy and a birthday-party example, then five cards (plain question, why, this case, asked/skipped), one line of RCA add-ons and a rule of thumb.
  - **Stronger answer:** now opens with a six-move strip (Fig 1.4). Turns are tagged by move, with short plain sentences, "Why this move" notes, simple 70% × 60% maths, and metrics in plain words (Goal (North Star), Safety check (guardrail)).
  - **Framework box:** now has a scooter-vs-app analogy table, a plainer issue tree and 5 Whys (Fig 1.5), and a concrete "when it misleads" example (flat tyre plus empty tank).
  - "What was missing" and the rollback Check are reworded in plain language.
- Figures renumbered 1.1–1.11. Still 8 pages.
- Recorded the owner's simplicity rule in CLAUDE.md → Design decisions, at the owner's request. The design-system choices are still pending approval.
- Next: owner reviews the revised S0 sample.

### 2026-09-25: S0 style check
- Built: 8-page sample in the proposed design:
  - p1–2 primer "How UPI moves money": 3 diagrams (UPI message/money flow, the MDR fee curve from 15 Oct 2026, a turning-points timeline), a metrics table, a Check on the 30% cap, Key idea and In the interview boxes
  - p3–5 Case 1.6 (A308), verbatim Q&A → what worked/missing → Check → scoping-kit table → stronger answer (7 turns) → framework box (RCA sequence + 5 Whys, with the issue-tree diagram)
  - p6–7 tech "2 seconds inside a UPI payment": sequence diagram with a timing strip, p95/p99 tail chart, compounding success rates, nines table
  - p8 PhonePe teardown page: annotated home screen, core loop, FY26 revenue chart, metrics trio, moat, ideas
- The page count grew past 4 because the owner said not to aim for a page count; the aim was no half-empty pages.
- Setup done: pymupdf, playwright, markdown, pillow and Chromium installed; `cases2.py` extracts A308 correctly (speakers right; the console shows curly quotes as ? only because of cp1252 encoding; the build writes UTF-8).
- Output: PM Learner's Casebook/S0 - Style sample.pdf (8 pages). Sources: src/S0/ (s0.html template, style.css, build.py, research.md, png/ previews).
- Build: `python "PM Learner's Casebook/src/S0/build.py"`. It injects the verbatim case via cases2 (`qa_html`), prints the PDF with Chromium and renders PNGs at 80 dpi.
- Half-done / resume from: nothing half-done; waiting for approval.
- Unverified facts: see src/S0/research.md. Per-hop UPI latencies have no public source, so they're labelled illustrative. PhonePe FY26 "adjusted loss" and ESOP figures conflict between sources, so neither is used. How the new MDR is split between banks, app and NPCI is not published.
- New design decisions (PROPOSED, not yet approved):
  - Fonts: Source Serif 4 body at 9.9 pt; Inter headings, captions, tables and Q turns; A4; margins 13/15/14/15 mm; footer with book name + page number
  - Accent colour #0b5d7a; box colours: Example amber, When it breaks red, Framework indigo, Key idea green, Check grey-olive with a verdict pill, In the interview purple
  - Q&A: dark "A" badge + serif text for the candidate; grey "Q" badge + sans text on a tint for the interviewer; the opening question in a blue-bordered box; a yellow "Try it first" strip under a dark case header
  - Stronger answer uses green "A" badges; framework box steps numbered 1–5 (situation, everyday example, framework + diagram, when it misleads, in the interview)
  - Diagrams: hand-written inline SVG, viewBox width 680 = full text width (1 unit ≈ 0.75 pt), minimum text 10.3 units (~7.7 pt); consistent entity colours (app green, banks blue, NPCI/switch amber, problem red); dashed = message, solid green = money
  - Captions: "Figure M.n · Title." + what to notice + italic source and date
  - Each major section starts on a new page; h2 kept with its first paragraph
- Next: owner approval of S0, then M1 part A.
<!-- One entry per session:
### YYYY-MM-DD: <step>
- Built: …
- Output: PM Learner's Casebook/<file>.pdf (<n> pages)
- Half-done / resume from: …
- Unverified facts: …
- New design decisions (if any, approved by me): …
- Next: …
-->

## Frameworks introduced so far (so later modules can point back instead of re-teaching)
- Scoping kit (full cards, doctor analogy) → M1 Case 1.1; RCA add-ons → M1 Case 1.6
- RICE → M1 Case 1.1
- Two-sided users and personas; JTBD with the four forces → M1 Case 1.2
- CIRCLES; Kano → M1 Case 1.3
- Guardrails and counter-metrics → M1 Case 1.4
- North Star + input metrics + driver tree; holdouts and incrementality → M1 Case 1.5
- RCA sequence (four doors) + 5 Whys → M1 Case 1.6
- Impact–Effort; MoSCoW → M2 Case 2.1
- Customer journey map → M2 Case 2.2
- AARRR → M2 Case 2.3
- Unit economics: contribution margin, CAC, LTV, payback → M2 Case 2.4
- STP; the five GTM questions; Bullseye → M2 Case 2.5
- Issue trees and MECE → M2 Case 2.6
- Process decomposition; Little's law → M2 Case 2.7
- "Does this need AI?" test; Cagan's four risks → M3 Case 3.1
- Marketplace liquidity → M3 Case 3.2
- Mix vs rate decomposition (Simpson's paradox) → M3 Case 3.3
- Cost-plus / competitor / value-based pricing; elasticity; break-even for a price change → M3 Case 3.4
- Guesstimate primer + guesstimate kit (6 cards) → M3 Guesstimates
- MVP, build–measure–learn, riskiest-assumption map → M4 Case 4.1
- Opportunity Solution Tree; HEART → M4 Case 4.2
- Supply–demand balance and surge pricing → M4 Case 4.3
- TAM/SAM/SOM; Porter's five forces; SWOT (Check: doesn't hold up) → M4 Case 4.4
- Counter-positioning (one line, primer and Rapido teardown) → M4
- Network effects (direct, cross-side, local); cold start and the atomic network → M5 Case 5.1
- Who-wins, who-loses grid (Key idea, not a framework box) → M5 Case 5.2
- Switching costs (money, data, learning, people) and multi-homing → M5 Case 5.3
- Hooked loop (diagram only) → M5 Instagram teardown
- Retention curves and cohorts (three curve shapes, cohort table) → M6 Case 6.1
- Split the metric into its parts (views = viewers × starts × finish rate), a Key idea, not a box → M6 Case 6.2
- Tiered pricing (good–better–best), fences, price discrimination, decoy, simple willingness-to-pay test, family plans → M6 Case 6.3
- Cost per hour watched; LTV vs CPI for games (primer and Zynga teardown, not boxes) → M6

- Human-in-the-loop and risk tiers (harm if wrong × can a person catch it; rubber-stamping) → M7 Case 7.1
- Behaviour change, Fogg B = MAP (action line, prompts, tiny habits) → M7 Case 7.2
- Activation and the aha moment (time to value, activation rate, test the cause) → M7 Case 7.2
- Reading an A/B test (split/SRM, 95% range, size, guardrails, pre-named segments, novelty and learning effects, peeking, winner's curse, holdouts) → M7 Case 7.3
- "Does the cause add up to the whole fall?" (a Check, not a box) → M7 Case 7.3
- Buyer vs user in B2B (user, buyer, influencers, champion; value flow; one-way arrows) → M8 Case 8.2
- Sales-led vs product-led growth, with seat vs usage vs hybrid pricing (ICP and land-and-expand named inside) → M8 Case 8.3
- "Confidence should come from the evidence" (Key idea, not a box) → M8 Case 8.1
- B2B SaaS metrics: ARR, NRR, gross retention, logo churn, seat utilisation, expansion revenue (primer, not boxes) → M8
- Tearing down a B2B product in five questions (Real-life example box, Zoho) → M8 teardowns
- Nudges with EAST (Easy, Attractive, Social, Timely; can’t / won’t / forgot; evidence from turnout experiments) → M9 Case 9.1
- Working backwards: PR-FAQ with a pre-mortem → M9 Case 9.3
- Premium and ecosystem pricing (cost floor, whole-life value of a unit), loyalty economics (earn, burn, breakage, settlement) as answer content, not boxes → M9 Cases 9.2, 9.3 and primer

## Technology topics covered so far (IIM A curriculum slices; see CLAUDE.md §4)
- SDLC, Waterfall vs Agile, Scrum, Kanban, story points and velocity (IIM A pp. 70–74) → M1
- System design I: client/server, DNS, HTTPS/TLS, load balancer, tokens, REST APIs, status codes, webhooks vs polling, idempotency; UPI payment end to end, p95/p99, compounding success rates, nines → M1
- A/B testing basics (IIM A p. 54): control/variant, primary and guardrail metrics, significance, power, MDE, Lehr's sample-size rule, pitfalls → M1 (depth in M7)
- UX design (IIM A pp. 75–81): design thinking (EDIPT), research, affinity mapping (KJ), personas, prototype fidelity, usability testing (5 users), Nielsen's 10 heuristics, dark patterns (CCPA 2023) → M2
- ML and AI fundamentals (IIM A pp. 82–90): AI/ML/DL/GenAI, learning types, training splits, overfitting, leakage, recommender systems (collaborative, content, embeddings, cosine, retrieval → ranking → re-ranking, cold start), neural nets, GenAI basics, drift → M3
- Precision, recall, thresholds (IIM A p. 57): confusion matrix, accuracy trap, F1, cost-based threshold → M3
- Customer funnel and brand lift (IIM A pp. 121–124) → M3
- Cloud computing (IIM A p. 96): utility model, IaaS/PaaS/SaaS, containers, serverless, public/private/hybrid, on-demand/reserved/spot → M4
- System design III: scaling up vs out, stateless, load balancing, availability zones, autoscaling and warm pools, CAP per feature, SLI/SLO/error budgets, graceful degradation and kill switches, timeouts/backoff/circuit breakers, monolith vs microservices → M4
- System design IV: open connections vs polling, heartbeats, session directory, receipts and ticks, store and forward, message IDs and ordering, fan-out on write vs read, push (APNs/FCM), media by reference, presence, forward limits, failover and reconnect storms (jitter, backoff) → M5
- Encryption: salted slow hashes, AES, public/private keys, signatures, Diffie–Hellman, TLS vs end to end, Signal protocol (X3DH pre-keys, double ratchet, forward secrecy, security codes, key transparency, sender keys, multi-device, encrypted backups), metadata, PM trade-offs, traceability → M5
- Platform economics (IIM A p. 111) and building trust (p. 137): taught inside M5 cases, teardowns and encryption → M5
- Blockchain in depth (IIM A p. 101): ledger, blocks, SHA-256 chain, tamper-evidence, proof of work vs proof of stake, 51% attacks, wallets, seed phrases and custody, smart contracts and escrow, oracle problem, uses and failures (crypto, Walmart, TradeLens, e-rupee, NFTs), public vs private chains, five-question test → M6
- System design V: concurrency and bandwidth maths, bitrate ladder and codecs, segments, manifests, ABR and buffers, CDNs and hit-rate maths, origin shield, glass-to-glass latency and the low-latency trade-off, pre-warming vs autoscaling, server-side ad insertion, graceful degradation (start time, rebuffering ratio), on-demand pre-positioning, DRM and watermarking → M6
- AR and VR (IIM A p. 91): dropped (owner, 26 Sep 2026)
- System design II: SQL vs NoSQL, ACID, indexes, order state machine, replicas and sharding, caching (hit rate, TTL, stampede), queues and async workers, live tracking, geohash nearby search, batch matching, strong vs eventual consistency → M2
- LLMs and prompt engineering (IIM A p. 115): tokens and tokenisers (Indian scripts), cost-per-task chain, next-token prediction, attention and transformers, pre-training → instruction tuning → human feedback, training cut-off, temperature and top-p, context window and lost-in-the-middle, hallucination, prompt structure and system prompts → M7
- Evals in depth (IIM A pp. 54, 59): golden sets, rubrics with critical criteria, code checks vs expert graders vs AI judge (agreement check), offline vs online, regression evals by category, red-team sets, the eval loop → M7 (M8 adds RAG and agent evals)
- AI guardrails (IIM A p. 59): layered input, grounding, policy, output, hand-off and logging; unsafe vs wrongly refused rates; prompt injection; personal-data minimisation → M7
- IoT (IIM A p. 106): dropped (owner, 26 Sep 2026)
- RAG (IIM A pp. 125–128): chunking and overlap, embeddings and vector search, hybrid search, re-ranking, grounded prompts with citations, abstain threshold, freshness (re-index on publish), permission filters, four failure modes → M8
- Agents (IIM A pp. 129–131): the loop, tools and function calling, state and stopping rules, permissions by risk and least privilege, approvals, audit log, single vs multi-agent, loops, wrong inputs, injected instructions → M8
- MCP (IIM A pp. 132–133): host, client, server; tools, resources, prompts; 100 → 25 connectors; governance (Agentic AI Foundation, Dec 2025); risks; shipping an MCP server as distribution → M8
- Evals for RAG and agents: retrieval hit rate, faithfulness, correctness, agent task success, tool-call accuracy, unsafe-action rate, regression by stage, failure buckets from real chats → M8
- Cost per task and the quality–latency–cost triangle (IIM A p. 61): cost per resolved task with hand-offs, median vs p95, routing, caching, prompt caching, shorter context, batching → M8
- Low-code and no-code (IIM A p. 134): dropped (owner, 27 Sep 2026)
- Mobile releases (release trains, hotfixes, version tail, minimum supported version, server-driven screens) → M9
- Feature flags (kinds, targeting, kill switches, flag debt, Knight Capital) → M9
- Staged roll-outs (phased release, canaries, rings, gates and pause rules, crash maths, CrowdStrike) → M9
- Observability (metrics, logs, traces, crash reporting, real-user monitoring, burn-rate alerts) → M9
- Capstone system design: IRCTC Tatkal (waiting room, rate limits, seat holds with timers, strict seat count vs cached availability, idempotent payment, async tickets, degradation ladder, morning dashboard, PM trade-offs) → M9
