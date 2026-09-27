# M8 SaaS, productivity & enterprise AI: session plan (27 Sep 2026; awaiting "go")

Rules applied: 3 cases + 2 guesstimates; only the approved M8 frameworks (buyer vs user in B2B; sales-led vs product-led growth with seat vs usage pricing); earlier frameworks named in one line only (JTBD M1, RICE M1, North Star and guardrails M1, human-in-the-loop M7, reading an A/B test M7, activation M7, unit economics M2); no page budget; non-AI language with the extra phrase scan; no cross-chapter pointers; evals build on M7 (RAG and agent evals only); everyday picture → how it works → real example → PM decision for every tech mechanism.

## Cold open (top of the primer page)
Gurugram, a Monday in March. Karan, 29, a sales rep at a mid-sized logistics-software company, spends 40 minutes after his last call typing notes into the CRM that his sales-ops head made compulsory. He skips two calls' notes; the Friday forecast is wrong by ₹1.2 crore. Upstairs, the head of support is deciding whether to pay ₹1,500 a seat a month for an AI copilot for 120 agents, and the finance head asks why the company's AI bill doubled while the number of seats stayed flat. Try it: "Who is the customer for a CRM: Karan or his boss? And if an AI tool does half an agent's work, should you still charge per agent?"

## Outline
1. **Sector primer (~5 pp)**
   - How B2B software is bought: users, the buyer (budget owner), influencers (IT, security, legal, finance); resellers, systems integrators, cloud marketplaces
   - Unit economics in ₹: a ₹1,000-a-seat-a-month tool sold to a 200-seat company (ARR, gross margin ~80% for classic SaaS); the same product with an AI feature that costs ₹150 a seat a month to run (margin falls); CAC payback worked
   - Metrics: ARR, net revenue retention (NRR), gross retention, logo churn, seat utilisation (paid vs active seats), CAC payback, expansion revenue; each defined once with an example
   - Players and numbers (dated): Microsoft 365, Google Workspace, Salesforce; Indian SaaS (Zoho, Freshworks, Postman, BrowserStack, LeadSquared); cloud trio shares
   - Turning points: subscriptions replace licences (Adobe Creative Cloud 2013); Covid remote work (Zoom, Teams, 2020); generative AI in office tools (ChatGPT Nov 2022, Microsoft 365 Copilot Nov 2023); agents and MCP (2024–26); per-seat pricing under pressure as AI does work (per-resolution pricing, e.g. Intercom Fin)
   - Non-obvious mechanics: the buyer isn't the user; land and expand (NRR above 100% means growth without new customers); renewal dates as cliffs; switching costs of data and workflows; long sales cycles; AI turns software's near-zero marginal cost into a real cost per use
   - Questions interviewers love
2. **Cases (3)**
   - 8.1 AI copilot for support agents (Design · A267–268): RAG-grounded drafts, confidence, escalation; human-in-the-loop named in one line (taught in M7). No framework box: the case feeds the tech block's running example (RAG, agents, their evals).
   - 8.2 Low CRM adoption (RCA · A311–312) → framework box: **buyer vs user** (sales ops mandates, reps don't get payback)
   - 8.3 Launching an AI sales assistant in India (GTM · A283–284) → framework box: **sales-led vs product-led growth, with seat vs usage pricing** (worked: per-rep price against per-call AI cost; a heavy-user rep costs more than he pays)
   - **Dropped:** Improve PowerPoint (B128–129: its JTBD and prioritisation lessons were taught in M1–M2; the answer is a generic feature list); AI email-summary metrics (A293: faithfulness, trust guardrails and "gate on a trust metric" were taught in M7's evals; its best line is reused in the tech block); users abandoning an AI chatbot (A313–314: RCA flow taught in M1 and applied in 8.2; its five failure buckets become answer content in the agent-evals section, as the approved list says)
3. **Guesstimates (2):** G8.1 Google Photos storage (B137); G8.2 storage for 200 GB free Google Drive in Singapore (B139). Short kit reminder + one key idea: **stored is not the same as offered** (people use a small, skewed share of any free quota; companies keep several copies of every file).
4. **Teardowns (5):** Cloud trio: AWS vs Google Cloud vs Azure · Amplitude · ThoughtSpot · Gmail and Google Workspace · Microsoft 365 Copilot. Then a comparison table and a 2×2: how it is sold (sales-led → product-led) against how it is priced (per seat → per use).
5. **Technology (~13–14 pp; revised after the owner's review: more detail, no low-code/no-code)**
   Running everyday picture for the whole block: Priya, a new support agent at a Pune SaaS company, with a library card (retrieval), a phone to call other departments (tools), a rule book (permissions) and a team lead who signs off refunds (approval). An analogy table maps every idea below to her day. Each mechanism gets: everyday picture → how it works, step by step → a worked example with numbers → where it breaks → the PM decision. Running product example: the support copilot from Case 8.1 (restated in one line where used, no pointers).
   - **A. RAG: answering from your own documents (IIM A pp. 125–128), ~4 pp**
     1. Why a model alone isn't enough: training cut-off, no access to the help centre, confident guesses (named in one line; taught in M7)
     2. Preparing the library: collecting sources (help articles, past resolved tickets, policy PDFs), cleaning, **chunking** (worked: a 3,000-word refund policy cut into 12 chunks of ~250 words with overlap; why too small loses context and too big dilutes the match)
     3. **Embeddings and vector search**: each chunk becomes a list of numbers; the question too; nearest chunks found by similarity (cosine named in one line, taught in M3); a worked 2-D picture with five chunks and one question; vector database and index refresh
     4. **Keyword + meaning search (hybrid)** and **re-ranking**: why "GSTIN" or an error code needs exact keyword match; a re-ranker reorders the top 20 to the best 5; worked hit-rate before/after (74% → 86% of 200 test questions)
     5. **The grounded prompt**: top chunks + instructions to answer only from them and cite; "no answer found" behaviour; worked prompt with two chunks and citations
     6. **Freshness and permissions**: re-indexing when an article changes (a stale refund window of 7 vs 14 days); access control so an agent never retrieves another customer's data or an internal-only document
     7. **Where RAG breaks** (four worked failure cards on one refund question): wrong chunk retrieved; right chunk but outdated; two sources disagree; answer spread across three chunks; plus each failure's fix
     8. PM decisions: what goes in the library and who owns each source; refresh cadence; answer-or-abstain threshold; showing sources to the user
   - **B. Agents: AI that takes actions (IIM A pp. 129–131), ~3 pp**
     1. From answering to doing: an **agent** is a model in a loop (plan → pick a tool → call it → read the result → decide again → stop)
     2. **Tools** and **function calling**: the model writes a structured request (tool name + inputs); the app runs it; worked trace for "move me from the Basic to the Pro plan from next month" (look up account → check plan rules → calculate pro-rated charge ₹1,833 → ask the agent/customer to approve → change plan → confirm), each step labelled with who acts
     3. **Memory and state** across steps; stopping rules (max 8 steps; timeouts)
     4. **Permissions and approvals**: read tools vs write tools; money, deletion and emails to customers need a human click (human-in-the-loop named in one line, M7); least privilege; audit log
     5. **Single agent vs several agents** (a planner that hands work to specialists), and why most teams should start with one agent and a few tools
     6. **Where agents break**: loops that repeat a failing call; wrong tool or wrong inputs (refunding the wrong invoice); acting on instructions hidden in a customer's email (prompt injection, named in one line, M7); cost blow-ups (worked: an agent that retries 15 times turns a ₹6 task into ₹90)
     7. PM decisions: which actions to automate first (reversible, high volume); approval thresholds (refunds above ₹5,000 need a lead); what the agent must never touch
   - **C. MCP: one standard plug for tools and data (IIM A pp. 132–133), ~2 pp**
     1. Everyday picture: before USB-C, every phone needed its own charger; MCP (Model Context Protocol, released by Anthropic in November 2024) is a common plug between AI apps and the tools and data they use
     2. How it works: **host** (the AI app, e.g. a desktop assistant or the copilot), **client** (the connector inside it), **server** (a small program that exposes a tool or data source: Jira, Google Drive, a database); what a server offers (tools, resources, prompts); a worked request from "summarise ticket #4821 and file a bug" through two MCP servers
     3. Before/after arithmetic: 5 AI apps × 20 tools = 100 custom connectors without a standard, 25 (5 clients + 20 servers) with one
     4. Who adopted it (OpenAI, Google, Microsoft in 2025) and governance (verify the 2025 move to a neutral foundation)
     5. Where it breaks: untrusted servers, over-broad permissions (a server that can delete as well as read), tool descriptions that inject instructions, authentication gaps
     6. PM decisions: build an MCP server for your product so customers' AI tools can use it (a distribution decision); which actions to expose; read-only first
   - **D. Evals for RAG and agents (building on M7; golden sets, rubrics, AI judges and regression evals not re-taught), ~2 pp**
     1. Split the pipeline so you know where it fails: **retrieval** (was the right chunk in the top 5? hit rate; did we fetch junk? precision), **generation** (faithfulness: does every claim appear in the retrieved text? answer correctness)
     2. Worked table: 200 labelled tickets; 28 wrong answers traced as 17 retrieval failures, 7 generation failures, 4 stale sources, so the fix is the search, not the model
     3. Agent evals: task success rate, tool-call accuracy (right tool, right inputs), steps per task, cost per task, unsafe-action rate; worked results for 50 plan-change tasks
     4. The five failure buckets from real chat logs (accuracy, capability, flow, tone, hand-off) as a labelled sample, worked bars; online signals (repeat questions, "talk to a human", abandonment by model version)
   - **E. Cost per task and the quality–latency–cost triangle (IIM A p. 61), ~2–3 pp**
     1. **Cost per resolved task** = cost per attempt ÷ success rate; worked (3 calls × ₹2) ÷ 0.6 = ₹10, not ₹6; including retries and hand-offs to humans
     2. **Latency**: time to first word vs full answer; median vs p95 (1.2 s median, 6 s p95 on long tickets); what users tolerate for a draft vs a live chat
     3. **The triangle**: three real configurations placed on it (large model + re-ranker: best, slow, dear; small model: fast, cheap, weaker; routed: small first, large when unsure) with worked numbers
     4. **Levers**: model routing (70% of tickets to a model costing one-tenth → blended cost), caching repeated answers and prompt caching, shorter context (send 5 chunks not 20), batching non-urgent work overnight
     5. Why this breaks per-seat pricing (one line; the pricing framework is in Case 8.3)
   - **Dropped (owner, 27 Sep 2026): low-code and no-code (IIM A p. 134).**
6. **Connect the dots (~1 p)** with a sketch answer to the cold open

## Frameworks (approved list only)
- **8.2: Buyer vs user (B2B).** Everyday example: a school uniform (the school picks it, parents pay, the child wears it). Map: CRM (sales ops and CRO choose and pay; reps use; finance and leadership consume the forecast). Using it: list each role, what they gain and lose, where value flows one way; design so the user gets payback (auto-captured activity, reminders, deal insight). When it misleads: treating "buyer vs user" as two people when one person is both (a founder-led startup), or ignoring influencers who can veto (IT security). Interview script.
- **8.3: Sales-led vs product-led growth, with seat vs usage pricing.** Everyday example: a gym sold through a corporate wellness deal (sales-led) vs a gym that gives a free week to anyone who walks in (product-led); a mobile plan per SIM (seat) vs per GB (usage). Worked numbers: per-rep price ₹1,200 a month; AI cost per call hour ₹25; a light rep (10 hours a month) costs ₹250, a heavy rep (60 hours) ₹1,500 → loss; hybrid (seat with an included allowance plus top-ups). When it misleads: PLG with no path to the buyer (lots of free users, no contract); usage pricing that frightens buyers with unpredictable bills. Land-and-expand and ICP appear in the answer, not as boxes.
- Named in one line only where useful: JTBD, RICE, North Star and guardrails (M1); unit economics (M2); MVP (M4); human-in-the-loop, reading an A/B test, activation (M7).
- **Dropped:** JTBD for B2B (taught M1); ICP and land-and-expand as boxes; AI failure taxonomy as a box (answer content in the tech block); value vs complexity matrix (taught M2 as Impact–Effort).

## Early catches to teach (from reading the cases)
- **8.1 copilot:** strong structure and safeguards. Catches: never sized the prize (tickets a day × minutes saved × agent cost against AI cost per ticket); "validate bottlenecks with analytics" said but no numbers; a model's own "confidence" is poorly calibrated, so confidence should come from retrieval (did we find a close match?) and simple checks; suggestion acceptance rate can be gamed by rubber-stamping (edit distance and audited quality instead); escalation precision vs recall has unequal costs (a missed legal threat vs an unnecessary hand-off); check what exists (Zendesk AI, Intercom, Salesforce, Freshworks Freddy AI).
- **8.2 CRM:** excellent diagnosis (segment first, cheap data before interviews, leading and lagging metric). Catches: never names the buyer–user split that the case is about (sales ops mandates, reps pay the cost); cutting to 3–4 fields removes fields someone upstream relies on, so it's a negotiation with the buyer; the strongest fix removes typing altogether (auto-capture from email, calendar and calls, which exists in major CRMs); tenured reps also hold the biggest accounts, so their stale data costs the most; forecast accuracy check holds up.
- **8.3 AI sales assistant:** clean GTM with user, buyer and influencer. Catches: per-user pricing ignores that AI cost scales with call hours (heavy reps lose money); a free pilot with no success criteria or budget owner often never converts (set exit criteria, or a paid pilot credited on conversion); India-specific gaps: Hinglish and regional-language calls, many sales calls on WhatsApp or mobile phones that a meeting bot never joins, recording consent under the DPDP Act; product-led option (free for individual reps, like Fireflies or Otter grew) not considered even to reject; no numbers on time saved or pilot targets.
- **G8.1 Google Photos:** the click-to-receive split is applied the wrong way round (2 MB given to the 75% received photos), which roughly doubles the answer; 5 photos a week for a heavy user is far too low; not every Android user backs up to Photos; counts one year only (stated, good); check against Google's published photo counts.
- **G8.2 Google Drive Singapore:** 60% average use of a 200 GB free quota is far too high (use is skewed: most use a few GB, a few fill it); "internet users 80%" is low for Singapore; forgets that stored data is kept in several copies, so disk needed is higher than data stored; the 10% "buffer" has no reason.

## Diagrams (~50; one line each)
- **Primer:** who buys, who uses, who can say no (buyer, users, IT, legal, finance around one deal); a 200-seat deal waterfall from list price to gross profit, with and without AI inference cost; NRR explained with a customer that grows from 200 to 260 seats; CAC payback curve; players chart (revenue, dated); turning-points timeline; seat vs usage vs outcome pricing ladder; the renewal calendar cliff
- **Case 8.1:** move strip; an agent's ticket timeline (where the minutes go, before and after); the copilot flow (ticket → retrieve → draft with source → agent edits → send; low-match → "no suggestion"); escalation threshold trade-off (missed vs unnecessary hand-offs)
- **Case 8.2:** move strip; issue tree (70% log in → 40% don't update → friction / no payback / low trust); rep's update flow, 12 clicks before and 3 after with auto-capture; value flow diagram (data goes up to sales ops, nothing comes back to the rep) → buyer vs user figure; leading vs lagging metric timeline
- **Case 8.3:** move strip; pilot funnel (10 pilot accounts → active reps → paid); SLG vs PLG paths side by side; seat vs usage worked chart (cost and revenue per rep by call hours, break-even line); hybrid price with allowance
- **Guesstimates:** two strips; two equation trees; the reversed-split correction bars (G8.1); the skewed-use curve for a free quota plus replication (G8.2)
- **Teardowns (×5):** behind-the-screens flows: a Diwali sale scaling on a cloud (autoscale, managed database, bill by the second); an Amplitude event from a tap to a funnel chart and an experiment; a ThoughtSpot question typed in plain words → SQL on the warehouse → chart; a Gmail message through spam filters and a Workspace seat's admin controls; Microsoft 365 Copilot answering in Teams (Microsoft Graph, permissions, the LLM, citations). Plus one loop or money chart each (cloud revenue and margin, Amplitude land-and-expand, ThoughtSpot pricing shift, Workspace tiers, Copilot's seat-price arithmetic); comparison 2×2
- **Technology (~20):** Priya analogy table (HTML); RAG pipeline end to end (collect → chunk → embed → index → search → re-rank → grounded prompt → answer with sources); chunking a refund policy (too small / right / too big); similarity map with five chunks and one question; hybrid search + re-rank hit-rate bars; grounded prompt with citations (HTML before/after box); freshness and permissions flow; where RAG breaks (four failure cards on one refund question); agent loop; agent trace for a plan change (sequence diagram with an approval step); read vs write tools permission ladder; cost blow-up from retries (chain); MCP host–client–server diagram; before/after connector arithmetic (100 vs 25); MCP request trace across two servers; retrieval vs generation failure split (bars from 200 tickets); agent eval scorecard; failure-bucket bars; cost per resolved task chain; latency distribution (median vs p95); quality–latency–cost triangle with three configurations; model-routing flow with blended cost

## Light maths planned
- Seat deal: 200 seats × ₹1,000 × 12 = ₹24 lakh ARR; gross margin 80% → ₹19.2 lakh; with AI at ₹150 a seat a month → margin 65%
- NRR: starts at ₹24 lakh, expands to ₹31.2 lakh, loses ₹1.2 lakh in downgrades → NRR = 30.0 ÷ 24 = 125%
- CAC payback: ₹6 lakh to win the deal ÷ ₹1.6 lakh gross profit a month ≈ 3.75 months (illustrative)
- Copilot: 120 agents × 60 tickets a day × 2 minutes saved = 240 hours a day; AI cost ₹4 a ticket × 7,200 tickets = ₹28,800 a day vs agent time saved
- Escalation threshold: 1,000 tickets, 30 truly risky; recall 90% vs 97% and the extra hand-offs it costs
- CRM: forecast error ₹1.2 Cr; stale-deal share; 12 clicks × 20 updates a week = 240 clicks
- Seat vs usage: ₹1,200 a rep vs ₹25 per call hour; break-even at 48 hours a month
- Cost per resolved task: (3 calls × ₹2) ÷ 0.6 = ₹10; routing 70% to a small model at ₹0.5
- p95 latency: 1.2 s median but 6 s p95 on long tickets
- Retrieval hit rate: right article in top 5 for 172 of 200 = 86%
- Guesstimates: photos per year both ways; corrected split; Drive skewed use × replication

## Research (one light batch)
- AWS, Azure (growth %), Google Cloud Q2 2026 revenue and operating income; cloud market shares (Synergy or Canalys, 2026)
- Microsoft 365 Copilot price and seat numbers; Microsoft 365 commercial seats
- Google Workspace paying customers / users, Gemini in Workspace pricing change (2025); Gmail users
- Amplitude Q2 2026 revenue, customers, NRR; ThoughtSpot latest (private: ARR, pricing, Spotter agent)
- Salesforce Agentforce pricing (per conversation → flex credits); Intercom Fin per-resolution price
- Zoho and Freshworks latest revenue (Indian SaaS)
- MCP: launch (Anthropic, Nov 2024), adoption by OpenAI, Google, Microsoft (2025), governance (Linux Foundation / Agentic AI Foundation, Dec 2025, verify)
- Google Photos users and photo counts (4 trillion photos, 28 billion a week: 2020; 1.5 billion monthly users: 2025, verify); Singapore population and internet use (2025–26)
- Reuse drafts 308 (RAG, MCP, agents), 309 (cost per task, triangle), 305 and 209 (cloud), 214 (analytics), 211 (email) and the research notes

## Length
No page budget. Length follows content; kept tight by cutting repetition. With the deeper technology block, expect about 44–46 pages.

## Numbering and build
- Figures 8.n
- Build copied from `src/M7/build.py` (CASES with kill/who; EXTRA phrase scan; `.prompts` styles), `m8_figs.py` helpers plus `figs_primer.py`, `figs_cases.py`, `figs_teardowns.py`, `figs_tech.py`; `crop.py` and `figcrops.py` for reviews
- Case-page glitches seen in the dump: A267–268 prints its MVP list and safeguards as layout tables with the numbers separated ("1. 2. 3. 4."), so they need setting out by hand in reading order with a visible note; A311–312 prints its "PM Tip" as an interviewer turn (drop it or mark it as the casebook's tip)
- Figure code and patch scripts written with the Write tool

## Amendments after re-checking CLAUDE.md (27 Sep 2026, at "M8 Start")
CLAUDE.md on disk is unchanged since the M8 plan review (last edit 03:01, 27 Sep). Plan checked against every rule; four gaps fixed:
1. **§5.6 steps 3 and 6 for every tech topic (A–E):** key terms highlighted and defined in one line where they first appear, and one "In the interview" box per topic (as in M7).
2. **Evals rule ("real eval sets with sample test cases and scores"):** section D shows a sample RAG golden-set test case (question, expected source chunk, expected answer; retrieval hit, faithfulness and correctness scores), a sample agent test case (task, expected tool calls and inputs, pass/fail per check), and a before/after table for a model or retriever change on RAG and agent metrics. Golden sets, rubrics and AI judges are named in one line, not re-taught. Section D grows to about 3 pp.
3. **No repeated frameworks:** unit economics, CAC and payback (M2), precision/recall (M3), cosine (M3), North Star and guardrails (M1), human-in-the-loop (M7) are defined in one line with a worked number only. New in M8 and fully explained: ARR, NRR, gross retention, logo churn, seat utilisation, expansion revenue.
4. **Printed text:** no "taught in M7"-style pointers (plan shorthand only); neutral wording for generic people ("the rep", not "he").
