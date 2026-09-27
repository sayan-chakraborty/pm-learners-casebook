# CLAUDE.md: the PM Learner's Casebook

> Claude Code reads this file automatically at the start of every session in this folder. **You don't need to paste anything.** Just say which step to build (e.g. `Build M1`) or type `continue`, and follow §2 below.

---

## 1. What I want, and how the work is split

I'm an MBA student preparing for product manager (PM) roles in final placements, about two months away. I'm building a **personal learning guide** in small, finished pieces. I don't want to wait for one 300-page book: each piece should be useful the day it's finished. Keep everything **background-agnostic**.

**The plan: 1 style check + 9 sector modules + 3 finishing steps**

| Step | What gets built | Output PDF |
|---|---|---|
| **S0** | Style check: a 4-page sample in the final design, for my approval (§10) | `S0 - Style sample.pdf` |
| **M1–M9** | One module per sector. Each module contains: **(a)** the sector primer, **(b)** that sector's interview cases in Q&A form, with frameworks taught inside the cases, **(c)** ~5 product teardowns, **(d)** a technology block: the next slice of the IIM A technology curriculum plus one system-design topic. It doesn't have to match the sector. See §4 | `M<n> - <Sector>.pdf` |
| **F1** | Guesstimates: primer + 15 cases | `F1 - Guesstimates.pdf` |
| **F2** | Behavioural: the top 10 questions + story bank | `F2 - Behavioural.pdf` |
| **F3** | *(Optional)* Merge everything into one book with contents, case index, framework index and bookmarks | `PM Learner's Casebook (complete).pdf` |

Build modules in order M1 → M9, then F1, F2, F3, unless I ask otherwise. A module may take **two sessions**: part A covers the primer and cases, part B the teardowns and technology. That's fine, and PROGRESS.md tracks which parts are done. The module PDF is only final when both parts are in.

**Leave out:** case competitions, AI prototyping or vibe-coding, salary negotiation, resume building, any study plan, blank write-in spaces, a separate "frameworks at a glance" section, and ISB cases (ISB has no model answers).

## 2. Session protocol (follow every time)

**At the start of every session:**
1. Read `PROGRESS.md` and `FEEDBACK.md`. They are in this folder. FEEDBACK.md holds my reactions to earlier modules: apply every point to the new work.
2. If I say `continue` or `next`, propose the next unfinished step from PROGRESS.md.
3. **Show me a short plan and wait for my "go"** before building. The plan covers:
   - the outline (headings)
   - the diagrams (one line each)
   - the frameworks you'll introduce
   - the 5 teardowns
   - the tech topics
   - the research you'll do
4. Only read what the step needs. Don't read whole PDFs or drafts: extract only the pages you need, and `grep` the drafts for facts.

**At the end of every session (always, even if the work isn't finished):**
1. Update `PROGRESS.md`:
   - tick what's done
   - record page counts and the output file path
   - note what's half-done and exactly where to resume
   - list any facts you couldn't verify
   - add new design decisions
   - name the next step
2. Save sources to `PM Learner's Casebook/src/<step>/`.
3. Tell me in 3–4 lines what was built and what's next.

**Don't change this CLAUDE.md** except for the "Design decisions" section at the bottom, and only after I approve a change.

## 3. Files in this folder

| Path | Use |
|---|---|
| `Product Mindset 2026-27.pdf` | IIM A: worked cases (pp. 233–318), PM concepts (pp. 9–66), tech concepts (pp. 54–65, 69–144), sector primers (pp. 146–200) |
| `Sigma PM Casebook 2026-27.pdf` | IIM B: worked cases (pp. 10–155) |
| `BTC Handbook 2026.pdf` | ISB: approach chapters (pp. 39–61), behavioural chapter (pp. 39–44), "products to read up on" (p. 14). **Ideas only, never cases.** |
| `Lenny's Podcasts/…Field Guide.pdf` | A teaching style I liked (example boxes, "when it breaks"). Borrow ideas, don't copy the layout |
| `PM Learner's Casebook (drafts)/` | Old drafts of teardowns and technology (PDF plus a Markdown zip). **Research material only: rewrite, don't polish** |
| `_pm_guide_toolkit/` | Scripts and notes; read its `README.md`. `selection.py` holds the chosen cases and pages. `cases2.py` extracts the case text verbatim, with speakers labelled, and rebuilds tables. `research_notes_sep2026.md` has sourced facts. `scoping_evidence.md` has the opening questions of all cases. `dia.py`, `build.py` and `style.css` are reference only |
| `PROGRESS.md` / `FEEDBACK.md` | Progress tracker and my feedback log (see §2) |

Put all outputs in `PM Learner's Casebook/`.

## 4. What each module contains

| Module | Sector cases (type · source pages; A = IIM A, B = IIM B) | 5 product teardowns | Technology block (a slice of the IIM A tech curriculum + system design) |
|---|---|---|---|
| **M1 Payments & fintech** | Credit platform for teenagers (Design · B38) · Bank app for rural India (Design · B55–56) · Improve your favourite UPI app (Improvement · B116–117) · Fraud prevention in a banking app (Improvement · B110–111) · Google Pay tie-in promotions (Metrics · A294) · Android DAU drops 40% (RCA · A308) | PhonePe · Google Pay · Paytm (with a super-app lens and WeChat as the comparison) · Razorpay · Investing trio: Groww vs Zerodha vs smallcase | How software is built: SDLC, Waterfall vs Agile, Scrum, Kanban (IIM A p. 70) · System design I: how the internet and APIs work (client/server, DNS, HTTP/HTTPS, REST, webhooks), with **a UPI payment end to end** as the walkthrough · A/B testing basics (IIM A p. 54) |
| **M2 Food delivery & quick commerce** | Quick-commerce vendor management (Design · A269–271) · Improve Swiggy (Improvement · B126–127) · BigBasket metrics (Metrics · A291–292) · Swiggy metrics before an IPO (Metrics · B153) · Swiggy table reservations (GTM · A280–282) · Zomato cancellations (RCA · B86–87) · Zepto delivery-time breaches (RCA · B82–83) | Zomato (with Blinkit) · Swiggy (with Instamart) · Zepto · BigBasket · magicpin (with ONDC) | UX design: design thinking, personas, prototyping, Nielsen's heuristics (IIM A p. 75) · System design II: databases (SQL vs NoSQL, indexes), caching, queues and async processing, with **a food order and live tracking** as the walkthrough |
| **M3 E-commerce & marketplaces** | E-commerce for senior citizens (Design · B30–31) · AI for Myntra (Improvement · B107–108) · Facebook Marketplace metrics (Metrics · A290) · Decline in cart additions (RCA · A309–310) · Amazon return rate (RCA · B70–71) · Amazon Prime price-cut projection (Pricing · A297) · Pricing Amazon Prime (Pricing · B94) · Vendor price negotiation (Pricing · A300–301) · Fake products on Instagram (Strategy · B146) | Amazon (with Prime, Fresh/Now, Rufus) · Flipkart · Myntra · Google (search and ads) · Ad tech: InMobi and Media.net (plus how the ad-tech stack works) | Machine learning and AI fundamentals: types of learning, training, recommendations, neural nets, GenAI (IIM A p. 82) · precision, recall and thresholds (IIM A p. 57) · customer funnel and brand lift (IIM A p. 121) |
| **M4 Mobility, maps & travel** | Ola for schoolkids (Design · A250–251) · Uber for kids (Design · B39–40) · Improve Uber (Improvement · B96) · Improve Google Maps (Improvement · B114–115) · Spike in Uber cancellations (RCA · A306) · Google Maps ETA errors (RCA · B65) · MakeMyTrip enters Dubai (GTM · B151–152) | Uber · Ola · Rapido · Google Maps · MakeMyTrip | Cloud computing: IaaS/PaaS/SaaS, serverless, pricing models (IIM A p. 96) · System design III: scaling, load balancing, consistency vs availability (CAP), reliability (SLOs, the 'nines', graceful degradation) · microservices vs monolith |
| **M5 Social, creators & messaging** | LinkedIn for blue-collar workers (Design · B46–47) · Facebook Reactions (Improvement · A316) · Instagram creator commerce (Metrics · A288–289) · WhatsApp in-app video (Metrics · A295) · Gmail success metrics (Metrics · B154–155) · Users moving from WhatsApp to Telegram (Strategy · B149–150) | Instagram (with Threads) · Facebook (with Meta ads) · X (Twitter) · Snapchat · WhatsApp (with WhatsApp Pay, Messenger, and Telegram as the comparison) | Economics of digital platforms: network effects, differentiation, switching costs (IIM A p. 111) · building trust in products (IIM A p. 137) · System design IV: **messaging and notifications (WhatsApp delivery)**, encryption and security basics |
| **M6 Streaming, music & entertainment** | Podcasts on Spotify (Design · A254–255) · BookMyShow engagement (Improvement · A317–318) · Improve Hotstar (Improvement · B105–106) · Improve YouTube (Improvement · B120–121) · Prime Video views fall (RCA · B80–81) · JioSaavn family plan (Pricing · A298) · JioSaavn family plan, second take (Pricing · B92) · Netflix pricing (Pricing · A299) | Netflix · JioHotstar (with Prime Video as the comparison) · YouTube (with Moj and Twitch) · Spotify · Zynga (free-to-play game economics) | AR and VR (IIM A p. 91) · blockchain, and when it is *not* the answer (IIM A p. 101) · System design V: CDNs and video streaming, with **Hotstar at IPL scale** as the walkthrough |
| **M7 Health, fitness & learning** | AI assistant for doctors (Design · B50) · HealthifyMe engagement (Improvement · B97) · Duolingo engagement drop (RCA · A303–304) · Adobe LMS trial-to-paid (RCA · B78–79) · Social fitness product launch (GTM · A278–279) | Duolingo · HealthifyMe · Cult.fit · Practo (or Tata 1mg) · PhysicsWallah | LLMs and prompt engineering: tokens, transformers, temperature, prompting (IIM A p. 115) · A/B testing and evals in depth (IIM A p. 54) · AI guardrails and human-in-the-loop (IIM A p. 59) |
| **M8 SaaS, productivity & enterprise AI** | AI copilot for support agents (Design · A267–268) · Improve PowerPoint (Improvement · B128–129) · Measuring an AI email-summary feature (Metrics · A293) · Users abandoning an AI chatbot (RCA · A313–314) · Low CRM adoption (RCA · A311–312) · Launching an AI sales assistant (GTM · A283–284) | Cloud trio: AWS vs Google Cloud vs Azure · Amplitude · ThoughtSpot · Gmail and Google Workspace · Microsoft 365 Copilot | MCP, RAG and agentic AI (IIM A pp. 125–133) · cost per task and the quality–latency–cost triangle (IIM A p. 61) · low-code/no-code platforms (IIM A p. 134) |
| **M9 Consumer hardware, loyalty & public services** | Samsung Galaxy Buds (Design · A264–266) · Increasing voter turnout (Design · A245–246) · Pricing an Apple smart speaker (Pricing · B93) · Tata Group loyalty programme (GTM · A285–286) | Apple ecosystem (HomePod/AirPods) · Amazon Alexa/Echo · Samsung Galaxy ecosystem · Tata Neu · ONDC or DigiLocker (public digital infrastructure) | IoT (IIM A p. 106) · mobile app releases, feature flags, staged roll-outs and observability · capstone: design one system at PM level (e.g. IRCTC Tatkal booking rush), using everything from System design I–V |
| **F1 Guesstimates** | A235 Instagram uploads/day · A236 YouTube revenue/day · A237–238 Zoom server usage · A239 food-delivery users, S. America · A240–241 dark stores for Ahmedabad · B136 WhatsApp chats/day · B137 Google Photos storage · B138 Uber drivers, Bengaluru · B139 Google Drive storage, Singapore · B140 bikes for a bike-taxi firm · B141 Google searches/second · B142 Swiggy orders/hour · B143 Google Meet calls/day · B144 Bhojpuri short-movie app users · **+1**, sourced or written by you and clearly labelled (e.g. UPI payments/day, checked against NPCI) | n/a | n/a |

Coverage check: every product on the ISB list (p. 14) appears in M1–M6 or M8, either as a teardown or inside one as a comparison. The technology column works through the IIM A curriculum (pp. 54–65, 69–144) in a sensible learning order, foundations first, AI later. Every IIM A tech concept appears exactly once, and system design builds up across five parts (I–V) before the M9 capstone. **Technology topics don't need to match the module's sector.** Where a natural link to the module's products exists, use it for examples; otherwise use the best real-life example from anywhere. If you move a topic, note it in PROGRESS.md.

**Case pages with pictures or flowcharts** (text extraction alone loses them): B30, B31, B81, B82, B114, B126, B127. Crop the region as a sharp image, or redraw it as a clean diagram labelled "redrawn from the original".

**Page guide per module:** primer 4–6 pp · cases 8–12 pp · teardowns ~2–3 pp each · technology 6–10 pp. That's roughly 30–40 pages a module. Tight and useful beats long.

## 5. How the parts of a module are written

**Order inside a module:** cold open (½ page: a real scene plus one case question to try) → sector primer → cases (mixed by type) → product teardowns → technology → "Connect the dots" (½ page linking cases, products and tech).

### 5.1 Sector primer
Explain how the industry really works, for a learner:
- the value chain: who does what, and who pays whom
- unit economics with a worked ₹ example
- the metrics that matter, each explained the first time it appears
- players and current numbers, dated and sourced
- 2–3 turning points in the sector's history
- the non-obvious mechanics
- the questions interviewers love in this sector

Include at least 4–6 diagrams.

### 5.2 Cases in Q&A form
For each case:
- **Header:** case number, type, difficulty, source and page.
- **Try it first:** read only the question and spend 5 minutes structuring an answer out loud.
- **The case, verbatim, as Q&A turns:** **Q** = interviewer, **A** = candidate, with the opening question in a highlighted box. Use the casebook's exact words; fix only extraction glitches. Rebuild tables as real tables. Use `cases2.py`.
- **What worked / what was missing:** 3–5 bullets. Include fact-checks of shaky claims, and note which scoping-kit questions (§5.4) the candidate asked or skipped, and what it cost them.
- **Stronger answer:** a cleaner Q&A of 4–8 turns. It opens with the scoping kit applied to this case (3–5 questions plus one stated assumption), then gives concrete numbers, a North Star, a guardrail and the trade-off.
- **Framework box(es):** only where this case is the framework's natural first use (§5.3). Later cases get a one-line reminder that points back.

### 5.3 Frameworks, taught inside the cases
Every important PM framework must appear somewhere in M1–M9 or F1. Research canonical sources: Lenny's Newsletter, Exponent, SVPG, Product Talk, Reforge, and the original authors.

**How to introduce a framework (always):**
1. The situation from the case that needs it.
2. A second, everyday example.
3. The framework, explained simply with a diagram.
4. When it misleads or becomes decoration.
5. How to use it naturally in an interview without sounding like you're reciting.

**Suggested first placements** (adjust if a better case fits):
- **M1:**
  - two-sided users and personas; JTBD with the four forces (teen credit)
  - clarifying questions and the scoping kit; RICE with real numbers (rural bank)
  - CIRCLES; Kano (UPI app)
  - guardrail and counter-metrics (fraud)
  - metric formula / driver tree; North Star plus input metrics; holdouts and incrementality (Google Pay)
  - the RCA sequence (data → external → internal → segment); 5 Whys (Android DAU)
- **M2:**
  - Impact–Effort; MoSCoW (vendor management)
  - customer journey map (Swiggy)
  - AARRR (BigBasket)
  - unit economics: contribution margin, LTV/CAC, payback (Swiggy IPO)
  - STP; the five GTM questions; Bullseye channels (table reservations)
  - issue trees and MECE (Zomato)
  - process or funnel decomposition (Zepto)
- **M3:**
  - usability heuristics and accessibility (seniors)
  - the "does this need AI?" test (Myntra)
  - marketplace liquidity (FB Marketplace)
  - funnel analysis (cart)
  - fishbone (returns)
  - cost-plus, competitor and value-based pricing, plus elasticity (both Prime cases, side by side)
  - BATNA (vendor negotiation)
  - Cagan's four risks; trust and safety (fake products)
- **M4:**
  - contrasting cases: Ola for schoolkids vs Uber for kids; MVP and build–measure–learn
  - HEART (Uber)
  - Opportunity Solution Tree (Maps)
  - supply–demand balance (cancellations)
  - TAM/SAM/SOM, Ansoff, Porter's five forces, and why SWOT is weak (MakeMyTrip)
- **M5:**
  - network effects and cold start (LinkedIn blue-collar)
  - Hooked model; Fogg's B = MAP (Reactions)
  - multi-stakeholder metrics (creator commerce)
  - counter-metrics (WhatsApp video)
  - GAME (Gmail)
  - switching costs and Helmer's 7 Powers (WhatsApp → Telegram)
- **M6:**
  - design thinking and the Double Diamond (podcasts)
  - retention curves and cohorts (BookMyShow)
  - ICE (Hotstar)
  - Biddle's DHM (YouTube)
  - seasonality and segmentation (Prime Video)
  - good-better-best tiers, family plans, Van Westendorp (both JioSaavn cases)
  - price discrimination (Netflix)
- **M7:**
  - human-in-the-loop and risk tiers (doctors)
  - behaviour-change design (HealthifyMe)
  - reading an A/B test (Duolingo)
  - activation, the aha moment and PLG (Adobe)
  - alpha → beta → general-availability launch phases (social fitness)
- **M8:**
  - evals and precision/recall for AI (copilot)
  - JTBD for B2B (PowerPoint)
  - the quality–latency–cost triangle (AI summary)
  - AI failure taxonomy (chatbot)
  - buyer vs user; adoption vs activation (CRM)
  - ICP; sales-led vs product-led growth; land-and-expand; seat vs usage pricing (sales assistant)
- **M9:**
  - segmentation and a prioritisation matrix (Galaxy Buds)
  - problem framing and behavioural nudges, e.g. EAST (voter turnout)
  - premium and ecosystem pricing (Apple)
  - loyalty economics; Amazon's PR-FAQ; pre-mortem (Tata)
- **F1:**
  - top-down vs bottom-up; supply-side vs demand-side; proxies; sanity checks; "one number, three ways"
- **Also where natural:**
  - product life cycle; crossing the chasm; Blue Ocean/ERRC; Lean Canvas; STAR (point forward to F2)

### 5.4 The reusable scoping kit (introduce in S0/M1, reuse in every case)

**Why it matters.** The first two minutes decide the case, and interviewers grade them explicitly. The kit gives you:
- **Less to think about under stress:** you never have to invent your opening.
- **The right problem:** in the rural bank case, asking about the objective revealed that the real brief was crowded branches.
- **Visible structure:** the interviewer sees you lead the conversation.
- **Clarifying without stalling:** 3–5 questions, then an assumption. The ISB handbook (p. 39) warns about stalling.
- **Anchors for the whole answer:** the goal becomes the North Star, the user becomes the persona, the limits become the trade-offs.
- **Transfer to the job:** the same questions open every real PRD.

**The kit was built from the cases and checked against them.** It comes from the opening exchanges of all 72 selected cases; the evidence is in `_pm_guide_toolkit/scoping_evidence.md`. How often each clarification appeared:
- goal ~22/72
- restate and confirm ~14
- who ~14
- **today and the trigger ~14** (missing from the first draft of the kit)
- scope edges ~14
- constraints ~5 (it decided the case each time it came up)
- success metric asked up front in design cases only ~2, so it moves to the end of the answer
- RCA:
  - exact definition 8/12
  - size and timing 9/12
  - where it shows 8/12
  - recent changes 4/12
  - is the data trustworthy 1/12 (a differentiator)

Strong candidates ask 3–4 questions, not 8. When the interviewer says "your call", pick an option, justify it in one line, and move on.

**Five core questions:**
1. **Confirm the thing:** "We're talking about X, which does Y. Right?"
2. **Goal:** growth, engagement, revenue, cost or trust?
3. **Who:** which user or side, segment and market?
4. **Today and the trigger:** what exists now, and why now? New or mature?
5. **Edges:** geography, platform, timeline, regulation?

**Add-ons by case type (pick 1–3):**

| Case type | Add-ons |
|---|---|
| Design / improvement | Which journey stage? Which platform first? Eligibility or legal limits (minors, KYC)? State the success metric at the end |
| RCA | Exact definition · size vs baseline · since when, and sudden, gradual or seasonal · where it shows (platform, region, category, new vs existing, funnel stage) · recent releases or changes · is the data trustworthy? |
| Metrics | What job does the feature do, for which stakeholders? Product stage? What decision will the metric drive? |
| Guesstimate | Unit and definition · time frame (typical day, peak vs average) · boundary · what's in and out · uptake assumption · precision needed |
| Pricing | New or existing? Share or profit? Segment and market? Competitor prices · plan structure · cost floor |
| GTM / strategy | Objective and horizon · standalone or add-on (existing assets, right to win) · target market · competitors · budget |

Keep checking the kit against each module's cases. Add new patterns to `scoping_evidence.md`, and change the kit only if a pattern appears in 3 or more cases.

### 5.5 Product teardowns (~5 per module)
For each product:
- **Real user walkthrough:** a named persona does one real task, screen by screen, shown as annotated screens.
- **Key features explained properly:** what each does, the user problem behind it, why it's designed that way, and the metric it moves.
- **Core loop and growth loops.**
- **Business model with numbers** (a waterfall where it fits).
- **Moat in plain words.**
- **North Star, input and guardrail metrics.**
- **2025–26 moves.**
- **Strengths and weaknesses.**
- **"What I'd build next":** 2–3 ideas, each as problem → bet → metric.

End the teardown block with a **comparison table** and a **positioning 2×2**. Use the old drafts and `research_notes_sep2026.md` as a starting point, and verify and update every number.

### 5.6 Technology for PMs (the tech block of each module: IIM A curriculum order, not tied to the sector)
**Perspective:** what a PM needs to understand and decide. Go deep enough to hold a real conversation with engineers, but no deeper.

**Structure for every concept:**
1. A real-life situation: from this module's products if the link is natural, otherwise the best everyday or product example available.
2. How it actually works, intuitively and step by step, with a diagram.
3. Key terms.
4. Where it breaks.
5. The PM decisions it drives: cost, speed, reliability, user experience.
6. How it comes up in the interview.

**Use light maths when it builds intuition, explained with an example.** For instance:
- a confusion matrix with real counts
- why p95 latency matters more than the average
- cache hit-rate arithmetic
- A/B test sample size
- Little's law in a dark store
- token cost per task
- cosine similarity for recommendations
- retention compounding
- "nines" converted into minutes of downtime

### 5.7 Guesstimates (F1)
- Start with a 2-page primer: top-down vs bottom-up, supply vs demand side, proxies, round numbers, sanity checks, and a table of India numbers worth remembering (sourced and dated).
- Then, for each case: try it first → the verbatim Q&A → an equation-tree diagram with the numbers → a sanity check against a real published figure → "the reusable trick".

### 5.8 Behavioural (F2)
- Research the 10 most common PM behavioural questions (Exponent, Lenny, company guides, ISB pp. 39–44).
- For each question, cover:
  - what it really tests
  - a simple answer structure (STAR, used flexibly)
  - a background-agnostic worked example
  - likely follow-ups
  - traps
- Open with how to build a story bank of 5–7 stories.

## 6. Diagrams: descriptive and intuitive enough to teach on their own
- One idea per diagram, understandable from the diagram plus its caption alone.
- Descriptive labels: arrows say *what flows* ("₹20 debit instruction", "rider GPS every 4 s"), and boxes say what the thing *does*.
- Worked numbers flow through the picture wherever possible, real or clearly illustrative.
- Annotations point at the insight ("most failures happen here").
- Caption: **Title.** Then 1–2 sentences on what to notice, then the source and date.
- Types to use:
  - numbered mechanism flows
  - before/after comparisons
  - annotated app screens
  - waterfalls
  - driver trees
  - issue trees
  - 2×2s with real products placed on them
  - timelines
  - sequence diagrams
  - real-data charts
  - analogy mappings
  - trade-off dials
- Legibility: text ≥ ~8 pt printed, no overlaps, consistent colours.
- Density: about **one diagram per page** in primers, teardowns and technology; 1–2 per case.
- Draw bespoke SVGs for each diagram (hand-written or generated by small scripts). **After every build, render the pages to PNG and look at every diagram.** Fix anything cramped or unclear.

## 7. Writing style
- Case or example first, theory after. Explain like a sharp senior friend: short sentences, concrete nouns, real numbers. Define every term the first time it appears, in one line, with an example.
- Lots of real-life examples, Indian wherever a good one exists. Add a contrasting example for every big idea.
- **Never use:** "delve", "crucial", "landscape", "tapestry", "leverage" (as a verb), "robust", "seamless", "in today's fast-paced world", "it's not X, it's Y", rhetorical-question openers, triplets for rhythm, chains of em-dashes, "In conclusion", "genuinely/honestly/straightforward".
- Label anything illustrative. Never state an unverified number as fact. Date every current number (e.g. "Q2 2026"). British/Indian spelling; ₹ in lakh/crore for India.
- **Box types:**
  - **Real-life example**
  - **When it breaks**
  - **Framework**
  - **Key idea**
  - **Check** (a claim tested, with a verdict: Holds up / Directionally right / Overstated / Doesn't hold up)
  - **In the interview**

## 8. Layout and design
- Textbook style: single column, clean, **little wasted white space**. A4, about 15 mm margins.
- Body around 10 pt with a clear heading hierarchy, coloured callouts for the box types, and diagrams mostly full width.
- In cases, Q and A turns are clearly distinct and the opening question sits in a highlighted box.
- S0 sets the design system, and every later step reuses it exactly. Record the decisions in "Design decisions" below.

## 9. Research and quality
- **Research economically:**
  - batch your searches
  - fetch only the best source for each fact
  - ask fetched pages narrow questions
  - prefer primary sources: company results, regulator data, engineering blogs
- Log facts in `src/<step>/research.md` as `fact | number | date | source`.
- **Before delivering, run this checklist:**
  - every idea opens with an example
  - every framework has an example and a "when it breaks"
  - every case is verbatim Q&A, followed by what worked, what was missing, and a stronger answer
  - diagrams are descriptive, legible and show one idea each
  - numbers are sourced and dated
  - no banned words
  - length is within the page guide
- **Token discipline:** use scripts for extraction and builds; don't echo big files or web pages; view images at the lowest resolution that answers the question; make small targeted edits. Never trade quality for tokens; cut repetition instead.

## 10. S0: the style check (first session only)
1. **Set-up:** check and install Python packages (`pymupdf`, `playwright`, `markdown`, `pillow`) and Chromium (`python -m playwright install chromium`). Confirm `cases2.py` extracts A308 correctly.
2. **Build a 4-page sample in the proposed final design:**
   - a primer page ("How UPI moves money") with 2 diagrams
   - one full case in Q&A form ("Android DAU drops 40%", A308), with its stronger answer, the scoping kit and one framework box
   - one technology page ("2 seconds inside a UPI payment") with a sequence diagram and some light maths
   - one PhonePe teardown page with an annotated screen
3. Stop and wait for my approval, then record the approved choices under "Design decisions".

---

## Design decisions (filled in after S0; update only with my approval)

### Design system (S0 approved 25 Sep 2026)
Reference files: `PM Learner's Casebook/src/S0/`: `style.css`, `s0.html`, `build.py`. Every later step reuses them exactly; copy them to `src/common/` and import from there.
- **Page:** A4; margins 13 mm top, 15 mm sides, 14 mm bottom; footer with the book name on the left and the page number on the right (7 pt, grey). Each major section (primer, cases, teardowns, technology) starts on a new page. Headings stay with their first paragraph.
- **Type:**
  - body: Source Serif 4 at 9.9 pt, line height 1.37
  - headings, captions, tables, labels and interviewer turns: Inter
  - H1 18 pt / 800; H2 11.6 pt with a hairline rule; small uppercase kicker above the H1 (e.g. "M1 · Payments & fintech · Sector primer")
- **Colours:** accent #0b5d7a (deep teal-blue). Box types each get a left bar and a tint:
  - Real-life example: amber #c47f17
  - When it breaks: red #b93a32
  - Framework: indigo #3e4fb8
  - Key idea: green #127a64
  - Check: olive-grey #6b6a52, with a verdict pill (Holds up green · Directionally right blue · Overstated amber · Doesn't hold up red)
  - In the interview: purple #7c3aa6
- **Primer furniture:**
  - a 4-cell stats strip of big numbers, each with a dated one-line label
  - terms highlighted in accent sans the first time they're defined
  - tables in Inter 7.9 pt with grey header rows
- **Cases:**
  - dark case header: "Case M.n · Title" + type pill · difficulty · source and page
  - a yellow "Try it first" strip under the header
  - the opening question in a blue-bordered box
  - interviewer turns: grey "Q" badge + sans text on a light tint
  - candidate turns: teal "A" badge + serif text
  - "What worked · what was missing" in two columns with ✓ / ✗ markers
  - then the Check box(es), the scoping-kit cards, and the stronger answer with green "A" badges, the move strip and move tags
  - then the Framework box with steps 1–5
- **Diagrams:**
  - bespoke inline SVG, with viewBox width 680 = full text width (1 unit ≈ 0.75 pt)
  - text ≥ 10.3 units (~7.7 pt); Inter 11 for labels, 10.5 for notes
  - consistent entity colours: user app green, banks/partners blue, network/switch amber, problem/risk red, framework indigo
  - dashed arrows = messages/instructions; solid green = money; dotted grey = replies
  - white halo behind labels that cross lines; two half-width figures side by side where both are small
- **Captions:** "Figure M.n · Title." + 1–2 sentences on what to notice + italic source and date. Figures are numbered through each module.
- **Build:**
  - HTML template + Python build: case text injected verbatim via `cases2.segments` (bold only list lead-ins after the first paragraph of a turn)
  - Chromium via Playwright to PDF
  - PNG previews at 80 dpi (zoom crops at 110–130 dpi for dense diagrams), reviewed after every build
  - a banned-word and em-dash scan before delivery
- **No page-count target:** length follows content (the owner's instruction), but no half-empty pages. Fill with useful content the brief asks for, or tighten.

### Simplicity rule for frameworks, the scoping kit and stronger answers (approved 25 Sep 2026, after the first S0 draft)
My feedback on the first draft: these three felt weak for understanding and too complicated. They must be **simpler and more intuitive, with examples**. Apply this everywhere, M1 to F2:
- **Plain-language test:** a first-year undergraduate with no tech or business background should follow it on the first read. One idea per sentence. Explain any jargon in brackets where it appears ("a feature flag (an on/off switch the team controls from its servers)"), or replace it with everyday words ("daily users", not "DAU cohort").
- **Analogy first, formal version second.** Open every framework and the scoping kit with an everyday situation everyone knows: a doctor asking questions before prescribing, a scooter that won't start, planning a birthday party. Then show the same idea on the case.
- **Frameworks:** keep the five steps (situation → everyday example → framework + diagram → when it misleads → in the interview), and also include:
  - an **analogy-mapping table** (the everyday example and the case side by side, row by row)
  - a simple diagram with plain labels
  - a **concrete** "when it misleads" example (e.g. "a flat tyre *and* an empty tank: fix one and it still won't go"), never an abstract warning
  - a one-sentence script for the interview
- **Scoping kit:** show it as **five cards**. Each card has the plain question, a one-line "why ask it", what it sounds like in this case, and a tick for asked or skipped. Add-ons go in one line of chips, ending with a rule of thumb ("ask 3–4, state one assumption, begin").
- **Stronger answers:**
  - start with a **move strip** diagram of the answer's steps (e.g. RCA: Clarify → Rule out → Find where → Check size → Fix → Measure)
  - tag each candidate turn with its move
  - keep each turn to about 2–4 short sentences
  - after the key turns, add a one-line italic "Why this move:" note
  - give numbers as simple multiplication, labelled illustrative
  - name the metrics in plain words with the term in brackets: "Goal (North Star)", "Safety check (guardrail)", "Trade-off", "Next time"
  - 4–8 turns in total
- The design-system choices proposed in the S0 sample (fonts, colours, box styles, Q&A layout) are listed in PROGRESS.md and are **not yet approved**. Add them here only after my approval.

### No module codes or signposting (owner's instruction, 25 Sep 2026, during M1)
- Printed pages never say "M1", "Module 1 of 9", "this module", "this primer" or "the tech block". There's no "what this module covers" map and no summary blurbs about what the reader will learn.
- Kickers name only the sector and section, e.g. "Payments & fintech · Cases". The footer reads "PM Learner's Casebook · <Sector>".
- Don't send the reader elsewhere with pointers like "(Case 1.2)", "see below" or "covered in the teardowns". Give the useful content in place instead.
- Case numbers (Case 1.3) and figure numbers (Figure 1.4) stay as labels.
- The cold open sits at the top of the primer's first page, under a plain sector title banner, not on a page of its own.

### Teardowns: flow diagrams, not screen mockups (owner's instruction, 25 Sep 2026, during M1; overrides §5.5 "annotated screens")
- Don't draw app screens in teardowns: no phone or browser mockups, redrawn or real.
- Tell the persona walkthrough in words. Pair it with a **flow diagram of what happens behind the task**: numbered steps across the parties (user, app, bank, NPCI, lender, merchant, partner), labelled with what flows between them (message, money, data, fee).
- Other teardown diagrams should also explain a flow or mechanism: core and growth loops, money waterfalls, how the business earns, product ladders, the positioning 2×2.

### No real screenshots in product teardowns (owner's instruction, 25 Sep 2026, during M1; replaces the rule below)
- **Don't download or embed real app screenshots or product photos.** They cost too many tokens. Teardowns use **bespoke SVG redraws only**: simplified annotated screens labelled "Simplified redraw, not pixel-accurate", plus the other diagram types.
- The old rule below is kept for the record and is **no longer in force**.

### Light-touch research (owner's instruction, 25 Sep 2026, during M2; relaxes §9 "verify every number")
- Keep research short to save tokens: a small batch of searches for the headline numbers (latest quarterly results, major regulation), then reuse the old drafts and `research_notes_sep2026.md` without re-verifying every figure.
- Don't chase exact precision. Round numbers, say "about", and keep dating and sourcing them in captions and in `src/<step>/research.md`.
- Still label anything illustrative, and never invent a number and present it as fact.

### Four cases + two guesstimates per module, no separate F1 (owner's instruction, 25 Sep 2026, during M2; overrides §1 and §4 from M3 onwards)
- **M3 to M9: only 4 sector cases per module.** Pick the 4 that teach the most and cover different case types; list the dropped cases in the session plan and in PROGRESS.md.
- **M3 to M9: add 2 guesstimates per module**, taken from the F1 list in §4 (14 cases across 7 modules), matched to the sector where possible. Each follows §5.7: try it first → the verbatim Q&A → an equation-tree diagram → a sanity check against a real figure → the reusable trick. The guesstimate primer (§5.7) goes into M3, where the first guesstimates appear; later modules add only a short reminder.
- **Guesstimates get a reusable framework, like the cases' scoping kit** (owner's instruction, 25 Sep 2026). Introduce it once, in M3, built from the 14 guesstimate cases: an everyday analogy first, then a small set of cards covering the steps. The steps are:
  - clarify the unit, time frame and boundary
  - pick the approach (top-down or bottom-up, demand side or supply side)
  - build the equation tree
  - put in round numbers with a one-line reason each
  - sanity-check against a real figure or a second method
  - state the answer as a range, with what would change it

  Each later guesstimate applies the same cards, with a "Guesstimate kit check" line (✓ used / ✗ skipped, and what skipping cost) and a stronger answer that follows the cards. As with the scoping kit, change the cards only if a pattern shows up in 3 or more guesstimates.
- **No separate F1 Guesstimates file.** F2 (Behavioural) and F3 (merge) stay.
- **Drop frameworks that are pure gas.** If a framework adds jargon but no real insight or decision in an interview, leave it out entirely, even if §5.3 suggests it. Don't give a plain-words version of the idea either. Note the drop in PROGRESS.md. (Updated by the owner, 25 Sep 2026.)
- **Don't repeat covered frameworks.** If a framework has already been taught in an earlier module (see PROGRESS.md, "Frameworks introduced so far"), don't include it again: no re-teaching and no reminder box. This overrides §5.2's "one-line reminder that points back".
- M1 and M2 were built before this rule and keep their original case lists.

### Detailed system design (owner's instruction, 25 Sep 2026, during M2)
- System design sections should be detailed, not a light overview. Cover the mechanisms a PM will hear about in engineering reviews: data model and order states, replicas and sharding, geospatial lookup, caching strategies, queues, consistency choices. Each gets a diagram and light maths, and stays at PM depth (what it is, where it breaks, what the PM decides).
- When pages have gaps, fill them by deepening system design (or other useful content), never with filler.

### Recording the owner's instructions (owner's instruction, 25 Sep 2026)
- Whenever the owner gives a standing instruction during a session, add it to this "Design decisions" section straight away, dated. This standing permission covers additions only; any other change to this file still needs approval.

### More detailed, intuitive stronger answers and frameworks (owner's instruction, 25 Sep 2026, during M3)
- Explain stronger answers and frameworks **in a bit more detail**, in the same simple, intuitive language (the simplicity rule still applies: plain words, analogy first, one idea per sentence).
- **Stronger answers:**
  - every candidate turn gets a "Why this move:" note in plain words, not just the key turns
  - turns may run 3–5 short sentences so the reasoning is visible, not only the conclusion
  - show any maths as a spelled-out chain ("₹250 × 3 lakh returns = ₹7.5 Cr"), labelled illustrative where it is
  - close with a short "How the answer hangs together" note: how the goal, the numbers and the guardrail connect
- **Frameworks:** keep the five steps, and add inside step 3 a short **"Using it, step by step"** list that applies the framework to the case in 3–5 plain steps, plus one "common slip" line.

### Three cases per module from M5; no IoT; deep blockchain and evals (owner's instruction, 26 Sep 2026, during M4)
- **M5 to M9: only the 3 most important sector cases per module** (overrides the "4 sector cases" rule above for M5 onwards). Pick the 3 that teach the most and cover different case types; list the dropped cases in the session plan and in PROGRESS.md. The 2 guesstimates per module stay. M4 keeps its 4 cases.
- **Drop IoT from the technology topics** (IIM A p. 106, planned for M9). Note the drop in PROGRESS.md; M9's tech block keeps mobile releases, feature flags and staged roll-outs, observability and the capstone.
- **Blockchain (M6): explain in depth, with examples.** Cover how it actually works step by step (blocks, hashes, the chain, consensus, wallets and keys, smart contracts), each with a worked example and a diagram, plus real uses and failures (e.g. crypto payments, supply-chain pilots, CBDC / e-rupee, NFTs) and when it is *not* the answer.
- **Evals (M7 and M8): explain in depth, with examples.** Show real eval sets with sample test cases and scores (e.g. a golden set for a support copilot, LLM-as-judge with a rubric, offline vs online evals, regression evals before a model change), with worked numbers.

### System design with more everyday examples (owner's instruction, 26 Sep 2026, during M4)
- Explain every system-design mechanism (M4 onwards: System design III, IV, V and the M9 capstone) with **more examples, in simple, intuitive, human language**, never AI-generic phrasing.
- For each mechanism give: an **everyday picture** from ordinary life (a restaurant on Diwali night, a toll plaza, an inverter during a power cut, a mobile data pack), then how it works, then a **real example** from a named product or incident, then the PM decision it drives.
- Open the section with one running everyday analogy mapped to all the mechanisms (a small table), so the whole section can be understood without any tech background.

### No repeated frameworks, detailed encryption (owner's instruction, 26 Sep 2026, M5 plan review)
- ~~Target below 40 pages per module from M5.~~ Withdrawn the same day (see the next section): no page budget; length follows content, kept tight by cutting repetition.
- **No repeated frameworks, inside a module or across modules.** Teach each idea once:
  - If a case and a tech topic share an idea (e.g., network effects in a case and IIM A's platform-economics pages), teach it in the case and don't give it a separate tech section.
  - Don't add a framework box that re-teaches earlier ideas under a new name (e.g., "multi-stakeholder metrics" over two-sided users + North Star + guardrails + liquidity).
  - Show only the genuinely new element, as a figure inside the stronger answer.
  - Earlier frameworks may be named in one line, never re-explained.
- **Encryption (M5) in detail.** Each part gets an everyday picture, how it works, a real example and the PM decision:
  - hashing
  - symmetric keys
  - public and private keys
  - signatures
  - key exchange
  - in transit vs end to end
  - how WhatsApp's end-to-end encryption works (Signal protocol, forward secrecy, security codes, groups, multi-device, backups)
  - what end-to-end doesn't hide
  - the PM trade-offs, including the traceability debate in India

### Fewer frameworks: only the essential ones (owner's instruction, 26 Sep 2026; overrides the §5.3 suggestions for M5–M9 and F2)
- The owner doesn't want to be overloaded. Keep only frameworks that change a decision in an interview and are commonly expected. Everything else is dropped: no box, no plain-words version. Earlier frameworks may still be named in one line where they help.
- **No page budget.** Length follows content; keep it tight by cutting repetition and non-essential material.
- **Approved framework list for the remaining modules** (one framework box each, at most 2–3 per module):

| Module | Keep (one box each) | Dropped from §5.3 |
|---|---|---|
| M5 | Network effects and cold start (5.1) · Switching costs, incl. multi-homing (5.3) | Trust and safety as a box (kept as answer content) · Helmer's 7 Powers · multi-stakeholder metrics · Hooked (loop diagram only) · Fogg · GAME · counter-metrics |
| M6 | Retention curves and cohorts · Tiered pricing (good–better–best), incl. price discrimination and a simple willingness-to-pay test | Double Diamond · ICE · Biddle's DHM · seasonality as a box · Van Westendorp as a separate box |
| M7 | Human-in-the-loop and risk tiers · Behaviour change (Fogg B = MAP) · Reading an A/B test · Activation and the aha moment | Launch phases (one line at most) |
| M8 | Buyer vs user (B2B) · Sales-led vs product-led growth, with seat vs usage pricing | JTBD for B2B (taught in M1) · ICP and land-and-expand as boxes · AI failure taxonomy as a box (kept as answer content). Evals and the quality–latency–cost triangle live in the tech block |
| M9 | Nudges (EAST) · Working backwards: PR-FAQ with a pre-mortem | Segmentation and prioritisation matrix (taught before) · premium/ecosystem pricing and loyalty economics as boxes (kept as answer content) |
| F2 | STAR | n/a |
| Also dropped | | Product life cycle · crossing the chasm · Blue Ocean/ERRC · Lean Canvas |

### No AR and VR (owner's instruction, 26 Sep 2026, M6 plan review)
- Drop AR and VR (IIM A p. 91) from the technology topics; it was planned for M6. Note the drop in PROGRESS.md. M6's tech block keeps blockchain (in depth) and System design V (video streaming at IPL scale, detailed).

### Non-AI language (owner's instruction, 26 Sep 2026, at the start of M5)
- Every page must read as if a person wrote it: simple words, explained with examples and diagrams. No AI-sounding phrasing anywhere, not only in system design.
- Beyond the §7 banned list, avoid: "unlock", "empower", "game-changer", "pivotal", "plays a key role", "it's worth noting", "not just X but Y", "at its core", "the real magic", "here's the thing", "navigate" (figuratively), colon-reveal sentences ("The answer: …") used as a habit, and stacked adjectives. Add these to the pre-delivery scan.
- Prefer a concrete scene or number over a general claim; say what happens, to whom, with what result.

### More detailed technology blocks; no low-code/no-code (owner's instruction, 27 Sep 2026, M8 plan review)
- Technology sections in M8 and M9 must be **more detailed** than the first M8 plan: more mechanisms per topic, each with an everyday picture, how it works step by step, a worked example with numbers, where it breaks, and the PM decision. Deepen rather than add new topics.
- **Drop low-code and no-code** (IIM A p. 134), planned for M8. Note the drop in PROGRESS.md; its page space goes to deeper RAG, agents, MCP, evals and cost/latency.

### Intuit teardown in M9 (owner's instruction, 27 Sep 2026, M9 planning)
- M9 adds a sixth product teardown: **Intuit, with its products** (TurboTax, QuickBooks, Credit Karma, Mailchimp, and its AI assistant). It sits alongside the five M9 teardowns in §4 and joins the comparison table and 2×2.
- **Revised the same day (owner, M9 plan review):** make Intuit a **deep dive**, more detailed than a normal teardown, and include **Intuit Enterprise Suite (IES)**. **Remove the Apple ecosystem, Amazon Alexa/Echo and Samsung Galaxy ecosystem teardowns** from M9. M9's teardowns are now: Intuit (deep dive, with each product), Tata Neu, and DigiLocker (ONDC as the comparison).

### F2 Behavioural: simple, real, under 20 pages (owner's instruction, 27 Sep 2026, at the start of F2)
- **Below 20 pages.** Keep it simple: fewer diagrams, one example answer per question, no company-flavours section or long quick-fire list.
- **Example answers from actual interviews.** Questions are taken from real interview reports (ISB BTC Handbook 2026, pp. 69–177: what was asked and the follow-ups used, as evidence of what is common). Where a real candidate's answer has been published, summarise it with its source; any answer written for the guide is labelled as such.
- **"No AI" (confirmed by the owner, 27 Sep 2026):** nothing may read as AI-written, and no made-up answer may be presented as real. AI-usage questions ("How do you use AI tools?") stay in, as a short item.
- **No cold open in F2** (owner, 27 Sep 2026: the opening scene "looks bad"). F2 starts straight with how the round works.

### F3 merged book and publishing (owner's instructions, 27 Sep 2026)
- Merge all ten chapter PDFs into one book with a cover ("Prepared for: Sayan Chakraborty", XLRI logo from `XLRI Logo.webp`), a preface, a contents page and a detailed index; every contents and index entry links to its page.
- Cover in an Economist style (red masthead box, one strong illustration, big serif headline). The book title stays "PM Learner's Casebook".
- Preface: credits (Claude, the IIM A and IIM B casebooks, ISB, Lenny's guide, public sources); the guide is exhaustive and for learning: curiosity about products, how they help or harm people, and second-order consequences; the case structure explained; readers are expected to critique the stronger answers and build their own thinking frameworks.
- Publish to a public GitHub repo. README: anyone can make changes; not verified, a work in progress; prepared in September 2026, so data will go stale; clone and fix mistakes or inconsistencies.

### ~~Real app screenshots in product teardowns (approved 25 Sep 2026)~~ (superseded, see above)
- Product teardowns may include **real images of app screens** (and product photos where useful), alongside the bespoke annotated SVG diagrams. Use whichever tool suits: WebFetch, the built-in browser, or Claude in Chrome.
- **Use:**
  - the real screenshot shows what the user actually sees
  - the redrawn SVG explains the design logic (callouts, metrics)
  - pair them where both help, e.g. the screenshot on the left, the annotated redraw or callouts on the right
- **Where to get images, in order of preference:**
  1. official sources: the company's Play Store or App Store listing screenshots, press kits, newsroom and engineering blogs
  2. reputable coverage (news, product blogs) when no official image exists
  - never images behind a login, and never anything showing personal data
- **Caption every image** with its source and date, e.g. "Screenshot: PhonePe Play Store listing, Sep 2026". Note in the caption that the UI may have changed since.
- **Permission:**
  - list the images to fetch (what, source) in the session plan (§2), and my "go" covers those downloads
  - ask before any extra download not in the plan
- Save images to `PM Learner's Casebook/src/<step>/img/`, crop to the relevant part and compress. Keep them sharp at print size (≥ 150 dpi at the printed width).
- Log each image in `src/<step>/research.md` as `image | what it shows | date | source URL`.
