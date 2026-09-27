# M7 Health, fitness & learning: session plan (27 Sep 2026; awaiting "go")

Rules applied: 3 cases + 2 guesstimates; only the approved M7 frameworks (human-in-the-loop and risk tiers; behaviour change, Fogg B = MAP; reading an A/B test; activation and the aha moment); retention curves and cohorts (M6), RICE, North Star and guardrails (M1) named in one line only; no page budget; non-AI language with the extra phrase scan; no cross-chapter pointers; evals in depth with real test cases and scores; blockchain-style depth for the tech topics.

## Cold open (top of the primer page)
Indore, the first Monday of January. Neha, 27, downloads a fitness app after a New Year resolution. It asks 22 questions before showing her anything: weight, goal weight, diet type, allergies, wake-up time. She logs breakfast on Monday and Tuesday, forgets Wednesday, and never opens it again. The same week, a green owl reminds her that her Duolingo Spanish streak is at 212 days; she does a two-minute lesson in the office lift to keep it alive. Her mother, 58, sits in a clinic in Nashik with a plastic folder of old reports while the doctor, on his fortieth patient of the morning, flips through them. Try it: "Why does one app keep Neha for 212 days and the other lose her in three? If you ran the fitness app, what would you change first?"

## Outline
1. **Sector primer (~5 pp)**
   - Three businesses under one roof: health (doctors, diagnostics, pharmacy, insurance), fitness (gyms, trackers, coaches) and learning (test prep, language, upskilling); who pays in each (patient, employer, insurer, parent)
   - Unit economics in ₹: a ₹999 coaching plan (coach cost per user); a gym centre's month (rent, trainers, members needed to break even); a ₹4,000 test-prep course (content fixed cost, YouTube as the free funnel)
   - Metrics: activation, day-1/7/30 return, streaks, completion rate, outcome metrics (kg lost, HbA1c, test ranks), paid conversion, refund rate
   - Players and numbers (dated): PhysicsWallah (listed Nov 2025), Byju's collapse, Unacademy; HealthifyMe, Cult.fit; Practo, Tata 1mg, PharmEasy, Apollo 24|7; Duolingo; ABDM (ABHA IDs)
   - Turning points: Covid telemedicine guidelines (Mar 2020) and online classes; the Byju's rise and fall (2022–24); ABDM and ABHA health IDs (2021 onwards); coaching-centre guidelines (Jan 2024); GLP-1 weight-loss drugs arriving in India (2025); DPDP Rules for health data (Nov 2025)
   - Non-obvious mechanics: the New Year cliff (motivation is seasonal); outcomes are slow, so apps sell progress signals; experts (doctors, coaches, teachers) are the scarce supply; free content (YouTube) is the biggest rival; trust and regulation (a wrong health answer is not like a wrong film pick)
   - Questions interviewers love
2. **Cases (3)**
   - 7.1 AI assistant for doctors in small clinics (Design · B50) → framework box: **human-in-the-loop and risk tiers** (what the AI may do alone, what a doctor must check, what it must never do)
   - 7.2 HealthifyMe: users dropping off early (Improvement · B97) → framework boxes: **behaviour change (Fogg B = MAP)** and **activation and the aha moment** (the case is about onboarding and first-week churn, the natural home for both)
   - 7.3 Duolingo engagement drop (RCA · A303–304) → framework box: **reading an A/B test** (the cause was itself a feature-flag test, and the fix is shipped as one); Fogg named in one line (ability fell in context)
   - **Dropped:** Adobe LMS trial-to-paid (B78–79: its buyer-vs-user and pricing lessons belong to M8’s approved B2B frameworks); Social fitness product launch (A278–279: GTM taught in M2; launch phases get one line at most)
3. **Guesstimates (2):** G7.1 Zoom’s daily server usage in India (A237–238); G7.2 Google Meet calls a day (B143). Short kit reminder + one key idea: **count the right unit** (a meeting is not a participant; data up is not data down).
4. **Teardowns (5):** Duolingo · HealthifyMe · Cult.fit · Practo (with Tata 1mg as the comparison) · PhysicsWallah. Then a comparison table and a 2×2: how often people use it (daily habit → occasional need) against who delivers the value (the app alone → a human expert).
5. **Technology (~10–11 pp)**
   - **LLMs and prompt engineering (IIM A p. 115), ~4 pp.** Running everyday picture: a very well-read new intern who finishes your sentences. Each mechanism gets an everyday picture → how it works → a real example → the PM decision:
     1. Tokens (worked: the same sentence in English and Hindi, token counts; why Indian languages cost more)
     2. Next-word prediction (worked probability table for “Drink eight glasses of …”)
     3. Transformers and attention, in plain words (“it” in a sentence finding what it refers to)
     4. How a model is made: pre-training → instruction tuning → feedback from people
     5. Temperature and top-p (the same prompt at three temperatures, worked)
     6. Context window and memory (what fits, what is forgotten)
     7. Hallucination: why a fluent answer can be false (worked: a made-up drug dose)
     8. Prompting that works: role, context, examples, steps, output format; a before/after prompt for a health coach
   - **Evals in depth (IIM A pp. 54, 59), ~4 pp.** One running example: the clinic briefing assistant from Case 7.1.
     1. Why AI features need evals (the same input, different outputs)
     2. A golden set: 60 anonymised patient folders with the facts a doctor needs (sample test cases shown)
     3. A rubric: accuracy, completeness, no invented facts, readable in 30 seconds; scored examples
     4. Who grades: doctors vs LLM-as-judge; agreement worked (e.g. 88 of 100 grades agree) and when a judge can’t be trusted
     5. Offline vs online evals (the golden set before launch; doctors’ edit rate and time saved after)
     6. Regression evals before a model or prompt change (a version-vs-version table where one category gets worse and blocks the release)
     7. Red-team sets: prompts designed to break it
     8. The eval loop: failure → new test case → fix → re-run
   - **AI guardrails (IIM A p. 59), ~2 pp.** Layers around the model: input checks (personal data, abuse, out-of-scope), grounding in the patient’s own records, output checks (doses, diagnoses, banned claims), refusal and hand-off to a person, rate limits and logging; worked example: a coach chatbot asked “Can I stop my metformin?”. Human-in-the-loop named in one line (taught in Case 7.1). A/B testing basics (M1) and reading a test (Case 7.3) not re-taught; online evals are described as A/B tests of AI features in one line.
   - Note for M8: its eval section should build on this (RAG and agent evals: retrieval quality, tool-call accuracy, task success), not repeat golden sets and rubrics.
6. **Connect the dots (~1 p)** with a sketch answer to the cold open

## Frameworks (approved list only)
- **7.1:** Human-in-the-loop and risk tiers (one box): everyday example (a hospital pharmacy: the machine counts tablets, the pharmacist checks the prescription, only the doctor prescribes); three tiers for the clinic assistant (do alone / suggest, a doctor confirms / never); how the tier changes with confidence and harm; when it misleads (rubber-stamping: a busy doctor clicking “approve” on everything)
- **7.2:** Behaviour change, Fogg B = MAP (one box): everyday example (a morning walk: motivation high on 1 January, ability low if shoes are hard to find, no prompt without an alarm); map each onboarding step to motivation, ability, prompt; tiny habits; when it misleads (nudges that become nagging; streak anxiety)
- **7.2:** Activation and the aha moment (one box): everyday example (a new gym member who gets a trainer’s plan in week one stays); how to find the aha moment from data (users who did X in week one stayed Y% more; correlation vs cause); time-to-value; activation rate worked; when it misleads (forcing the “aha” action without the value)
- **7.3:** Reading an A/B test (one box): everyday example (two tea stalls, one with a new sign); the reading checklist: did the split work (sample ratio), is the effect real (significance named in one line, not re-taught), is it big enough to matter, did guardrails hold, which segments, novelty and primacy effects, long-term effect; a worked result table for the “Can’t speak now” test; when it misleads (peeking, many metrics, winner’s curse)
- Named in one line only where useful: retention curves and cohorts (M6), RICE, North Star, guardrails (M1), MVP (M4)
- **Dropped:** launch phases as a box (one line at most, per the approved list); JTBD re-teach; any new prioritisation framework

## Early catches to teach (from reading the cases)
- **7.1:** the brief says “no diagnosis”, yet flagging “abnormal values” and summarising history is clinical content: exactly where risk tiers are needed. Never sized the prize (40–60 patients a morning × 1–2 minutes) or said who pays (the clinic owner). No success metric. Check what exists: AI scribes and clinic software in India (e.g. Eka Care, Practo’s clinic software) and ABDM health records that can replace photo uploads. Health data under the DPDP Act needs explicit consent. Questionnaire language (Hindi, Marathi) for Nashik-type clinics.
- **7.2:** good clarifying questions (when, which metrics), but “onboarding is too long” came from personal experience, not from the funnel data the interviewer offered. No aha moment defined, so “Skip & Start” may just move the drop-off to day 2. Fact-check: Google Fit’s APIs are being replaced by Health Connect on Android (verify dates), so “sync with Google Fit” needs updating. Check what HealthifyMe already does (photo calorie logging, AI coach Ria, wearable sync). No metric or guardrail named.
- **7.3:** a model RCA opening. Catches: Duolingo already has a “Can’t speak now” button that pauses speaking exercises (verify current behaviour), so solution 1 exists; the real questions are why the test that raised speaking exercises didn’t stop itself (its guardrails), and how to read the follow-up test properly (duration, novelty, sample ratio, segments). The candidate’s third check (did blocked users complete another lesson?) is excellent and worth praising.
- **G7.1 (Zoom):** “working population” was working-age population (60% of 140 crore), not workers; data per user counted one direction only (a Zoom server receives each person’s video once but sends several streams back); check against Zoom’s published meeting minutes.
- **G7.2 (Meet):** counted participant-joins, not meetings (a meeting with four people was counted four times); 84 crore professional users is far above Google’s published Meet users; check with meetings = joins ÷ people per meeting.

## Diagrams (~48; one line each)
- **Primer:** who pays whom across health, fitness and learning (patient, employer, insurer, parent); a ₹999 coaching plan waterfall; a gym centre’s break-even (members needed); test-prep money: YouTube free funnel → paid batch; the New Year cliff (sign-ups and activity by month); players chart; turning-points timeline; outcomes vs progress signals (weight loss curve vs daily streak)
- **Case 7.1:** move strip; a clinic morning timeline (where the 1–2 minutes go); risk-tier ladder (do alone / doctor confirms / never) placed on the assistant’s features; the briefing flow with the doctor’s check point
- **Case 7.2:** move strip; onboarding funnel with drop-off at each step (worked); B = MAP chart (motivation × ability with the action line and a prompt) with Neha plotted; aha-moment analysis (retention of users who did vs didn’t log 3 meals in week one)
- **Case 7.3:** move strip; driver tree (weekly learners = returning users × start rate × completion rate); funnel with the in-lesson drop; the A/B result table/figure with confidence intervals and a guardrail; novelty effect curve
- **Guesstimates:** two strips; two equation trees; Zoom up vs down data diagram (one sender, several receivers)
- **Teardowns (×5):** behind-the-screens flows: a Duolingo lesson and streak notification (Birdbrain picking exercises, the reminder timing); a HealthifyMe photo meal log (AI estimate, user correction, coach review); a Cult.fit class booking (slot, centre capacity, trainer, waitlist); a Practo appointment and teleconsult (doctor listing, booking, payment, prescription); a PhysicsWallah student from a free YouTube lecture to a paid batch and an offline centre; plus a loop or money chart per product; comparison 2×2
- **Technology:**
  - LLMs: intern analogy table; tokenisation of the same sentence in English and Hindi; next-word probability bars; attention lines on a sentence; the three training stages; temperature dial with three outputs; context-window “desk”; hallucination anatomy; before/after prompt
  - Evals: the eval loop; a golden-set test-case card; rubric scoring grid; judge-vs-doctor agreement table; offline vs online; regression table v1 vs v2 by category; red-team examples
  - Guardrails: layers around the model; the metformin question walked through the layers

## Light maths planned
- Clinic: 50 patients × 1.5 minutes saved = 75 minutes a morning; × 25 days = 31 hours a month; value at the doctor’s consult fee
- Onboarding funnel: 100 installs → 60 finish onboarding → 30 log a meal → 18 on day 7 (illustrative); cutting 22 questions to 5
- Aha moment: day-30 retention 45% vs 12% for users who logged 3 meals in week one, and why that is not proof of cause
- Duolingo: weekly learners = returning users × 0.9 start × completion; a 15% fall located in completion; A/B test sample size and a 95% interval on +3 points of completion
- Gym break-even: rent + trainers ÷ fee per member
- Tokens: words to tokens in English vs Hindi; context window in pages
- Evals: rubric scores (e.g. 4.1 vs 3.6 of 5), judge agreement 88%, regression blocking rule (no category may fall more than 2 points)
- Guesstimates: Zoom data both ways; Meet joins ÷ people per meeting

## Research (one light batch)
- Duolingo Q2 2026 results (DAUs, paid subscribers, revenue); “Can’t speak now” behaviour; AI-first 2025 memo and response
- HealthifyMe latest (revenue, GLP-1/metabolic programmes, Ria); Google Fit API deprecation and Health Connect dates
- Cult.fit latest revenue and IPO status; gym economics benchmarks
- Practo latest revenue; Tata 1mg; e-pharmacy rules status
- PhysicsWallah listing (Nov 2025) and FY26 results; Byju’s status; coaching guidelines (Jan 2024)
- ABDM (ABHA IDs, linked records); telemedicine guidelines 2020; DPDP Rules on health data
- Zoom, Google Meet, Teams published usage numbers (for the two guesstimate checks)
- LLM basics (tokenisers for Indian languages; context windows) from primary docs; eval practice from Anthropic, OpenAI and Google guides
- Reuse drafts 307 (LLMs), 309 (A/B tests, evals, guardrails and HITL) and the research notes

## Length
No page budget. Length follows content; kept tight by cutting repetition. Expect about 40 pages.

## Numbering and build
- Figures 7.n
- Build copied from `src/M6/build.py` (CASES with kill/who; EXTRA phrase scan; `.sw{break-inside:avoid}`), `m7_figs.py` helpers plus `figs_primer.py`, `figs_cases.py`, `figs_teardowns.py`, `figs_tech.py`; `crop.py` for zoom checks
- Figure code and patch scripts written with the Write tool
