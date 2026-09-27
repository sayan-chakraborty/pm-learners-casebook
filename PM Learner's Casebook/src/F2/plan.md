# F2 Behavioural: session plan v2 (27 Sep 2026; awaiting "go")

Owner's instructions at the start of F2: "No AI"; keep it simple; example answers from actual interviews; below 20 pages. This replaces plan v1 (30–35 pp, 25 diagrams, company flavours, 15 quick-fire, 7 × 10 story grid).

Output: `PM Learner's Casebook/F2 - Behavioural.pdf`, **18–19 pages**. Kickers "Behavioural interviews · <section>", footer "PM Learner's Casebook · Behavioural". One framework box: STAR. Non-AI language, extra and pointer scans, no signposting.

## Evidence: what was actually asked (ISB BTC Handbook 2026, interview reports pp. 69–177)
585 interview rounds reported, 285 of them behavioural, HR or resume rounds, across 57 companies. Themes counted by round (lower bounds: many reports only say "some behavioural questions"). Raw counts in `btc_theme_counts.txt`.

| Theme | Rounds | Real phrasing (company) |
|---|---|---|
| Project / work-ex deep-dive | 145 | "Detailed deep-dive into a project … What component were you responsible for?"; "drilled down on each line of my answer" |
| Intro / walk me through your resume | 28 | "Walk me through the work you have done, in one line for each role" |
| Why PM (why now, what is PM in one word) | 23 | "Why PM? Why now? … What is PM in one word?" (HiLabs) |
| Why this company / domain | 21 | "Why do you want to join Acko?"; "Why move from e-commerce to fintech?" |
| Prioritise / trade-offs (often situational) | 19 | "How would you prioritise features … present a case to senior leadership" |
| AI use / favourite AI product | 16 | "How do you use vibe coding tools … in your daily life?" (Affinity Global) |
| Values, culture, fit | 14 | "Questions on values and expectations" |
| Conflict / disagreement | 13 | "A time you disagreed with your manager: one where you were right, one where your manager was right" |
| Strengths / weaknesses / superpower | 12 | "Weaknesses and what you are doing to improve them" (CXO stress round) |
| Stress and situational rounds | 12 | "How will you handle a conflict situation with your colleague?" |
| Leadership / influence | 8 | "Leadership skills, evidence of proactiveness" |
| Long-term goals | 7 | "Where do you see yourself in 5 years?" (Flipkart) |
| Failure / criticism | 5 | "What was a time when you failed as a team?"; "a time when you were criticised" (Atlassian) |

Candidates' own advice from the same reports (used as tips, paraphrased): know every line of your resume; show genuine interest by using the company's product and having a view on its strategy; stay calm and structured in stress rounds; keep it conversational.

## How "example answers from actual interviews" will work
The ISB reports record the questions and follow-ups, not the answers. So each question gets:
1. **The question as actually asked** (2–3 real phrasings, company named, ISB 2026 reports).
2. **A real answer**, where a real candidate or PM has published the answer they gave (public mock-interview transcripts, candidates' write-ups of their own interviews). Summarised in my words, short, sourced and dated. Where no good real answer exists, the example is written for this guide and **labelled "Example answer (written for this guide)"**. Nothing invented is presented as real.
3. **The answer as Q&A**, with the follow-ups the ISB reports show interviewers actually use ("why that?", "what exactly did *you* do?", "what would you change?").
4. **Why it works** (3 short bullets) and **one trap** (weak line vs better line).

Backgrounds rotate across examples (fresher, engineer/analyst, business role, career switcher) so the guide stays background-agnostic.

## Outline (18–19 pp)
1. **Cold open + how the round works (~1.5 pp).** Riya at XLRI, "Tell me about a time you failed", no answer to "what did *you* do differently?" Then: what interviewers grade (ownership, judgement, working with people, self-awareness, motivation); how a round moves; red flags ("we" with no "I", no numbers, blame, a fake failure). Real-data chart of the themes above.
2. **Build a story bank (~1.5 pp).** Where stories come from in any background (one small table). Six stories cover almost everything: a project you drove, a conflict, a setback, a time you led or persuaded, a hard trade-off, a time data changed your mind. One filled story card (bullets, not a script). A small table: which story answers which question.
3. **Framework box: STAR, used flexibly (~1.5 pp).** Five steps as in every module: Riya's answer → explaining to parents why you came home late → STAR with a time-budget figure (Action ~half the time), analogy table, "Using it, step by step", common slip → when it misleads (a four-box recital that breaks when interrupted; results with no learning) → one-line script.
4. **The questions (~12 pp), ordered by how often they were asked:**
   1. The project deep-dive (~2 pp): Why → What → How → Impact → Next, then the line-by-line grilling tree
   2. Tell me about yourself / walk me through your resume
   3. Why PM? Why now?
   4. Why this company?
   5. How do you prioritise / a time you said no
   6. A conflict or disagreement (incl. "one where your manager was right")
   7. Strengths and weaknesses
   8. A failure, or a time you were criticised
   9. A time you led or persuaded people without authority
   10. Where do you see yourself in 5 years?
   *(If "No AI" does not mean dropping AI questions, 5–10 shift and "How do you use AI in your daily work?" joins as a short item.)*
5. **Stress rounds, curveballs and the end of the interview (~1 p).** Stress and situational rounds (from the reports: CXO and founder rounds); no example to hand; hostile follow-ups; answer length (about 2 minutes, then stop); three good questions to ask them, three to avoid.
6. **Connect the dots (~½ p).** The case habits carry over: clarify what is really being asked, give numbers, name the trade-off. Sketch answer to the cold open.

## Diagrams (about 10)
- Real-data bar chart: behavioural themes in 285 real rounds
- What the interviewer is scoring (five signals, with a red-flag for each)
- Story card, filled
- STAR time budget: weak vs strong answer (stacked bars)
- Project deep-dive: Why → What → How → Impact → Next, and the grilling tree
- Tell me about yourself: past → present → why PM → why here (timeline)
- Conflict: two positions, the shared goal, the agreed outcome
- Failure: what went wrong → what I did → what I changed → the next time
- Prioritising: requests placed on value vs effort (named in one line)
- Answer-length dial
Small move strips per question are CSS strips, not figures.

## Research (one light batch)
- Real published answers: public mock-interview transcripts with real PMs (e.g. Exponent), candidates' write-ups of answers they gave (PM blogs, Medium, LinkedIn posts), Lenny's Newsletter/Podcast pieces on behavioural interviews. Paraphrase only; at most one short quote per answer.
- Amazon Leadership Principles page (one line in section 5, as a common "values" set).
- Log in `src/F2/research.md`.

## Build
Copy `src/M8/build.py` minus the casebook CASES, plus `m8_figs.py` helpers, `figcrops.py`, `crop.py`, `mvfig.py`. Q&A uses the case styles (Q grey, A teal). "Why this move" notes only on 2–3 key lines per answer, to keep it simple. Figures numbered F.1, F.2 …
