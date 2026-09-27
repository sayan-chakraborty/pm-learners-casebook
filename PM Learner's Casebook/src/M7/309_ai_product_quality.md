%% chapter | Technology · Measuring what works | A/B tests: letting users settle the argument | How controlled experiments work, how big they need to be, and the traps that make a winning test lie

The design team at an e-commerce company is split. Half believe a "Buy Now" button on the cart page will cut drop-offs; the other half think it will confuse users who want to keep shopping. The meeting could go on for weeks. Instead, the PM proposes a test: for two weeks, half of shoppers (chosen at random) see the current cart, and half see the cart with "Buy Now". At the end, the variant's checkout completion is 14% higher than the control's, and the difference is far too large to be chance. The button ships to everyone. Nobody had to win the argument; the users settled it.

An **A/B test** is a controlled experiment: you randomly split users into a **control** group (A, the current experience) and a **variant** group (B, the change), and compare them on a metric you chose in advance. Because the split is random, the only systematic difference between the groups is the change, so any significant difference in outcomes can be credited to it. It is the product world's version of a randomised controlled trial in medicine.

```dia
title: Running an A/B test, step by step
steps([("Hypothesis", "'A Buy Now button on the cart will raise checkout completion by 10%, because users want fewer steps.'", "Write it before you see data"), ("Metrics", "One primary metric (checkout completion) + guardrails (returns, average order value, app crashes)", "Decide what would stop a launch"), ("Sample size", "Calculate users needed to detect the effect; run full weeks", "Too small = noise"), ("Randomise and run", "Split users at random, 50/50, via a feature flag; don't change anything else", "Check the split is really 50/50"), ("Analyse and decide", "Is the difference significant and large enough to matter? Guardrails OK? Ship, iterate or drop", "Don't stop early when it 'looks good'")], hl=[1])
```

## How big must the test be?

Flip a coin ten times and getting seven heads is not surprising. Flip it ten thousand times and 70% heads would be astonishing. Tests work the same way: small differences in small samples are often just noise. **Statistical significance** is the check that a difference is unlikely to be a fluke. By convention teams accept a result when there is less than a 5% chance that a difference this large would appear if the change actually did nothing (the "p-value below 0.05"). **Statistical power** (usually 80%) is the chance of detecting a real effect of the size you care about.

A handy rule of thumb for comparing conversion rates at those standard settings:

```dia
title: Rough sample size per group
sub: Lehr's rule of thumb for 5% significance and 80% power
src: Standard approximation; use a proper calculator for real tests
formula([("16", "A constant from the chosen significance and power", "16"), ("p × (1 − p)", "Variability of the baseline rate; for 20% conversion: 0.2 × 0.8", "0.16"), ("δ²", "Square of the smallest change worth detecting; 2 percentage points = 0.02²", "0.0004")], result="Users per group ≈ 16 × p(1 − p) ÷ δ² = 16 × 0.16 ÷ 0.0004 ≈ 6,400", ops=["×", "÷"])
```

The key intuition: **halving the effect you want to detect needs four times the users.** That is why small apps cannot test tiny tweaks, and why big apps such as Flipkart or Swiggy run hundreds of experiments at once.

## The traps that make a winning test lie

- **Peeking.** Checking every day and stopping the moment the result looks significant inflates false wins dramatically. Fix the duration in advance.
- **Novelty and learning effects.** A new design gets clicks because it is new; the lift fades after two weeks. Or the reverse: users need time to learn a better flow. Run long enough, and look at the trend.
- **Too many metrics.** Test twenty metrics and one will look significant by chance. Name one primary metric beforehand.
- **Weekday effects.** Shopping on Sunday differs from Tuesday. Run whole weeks.
- **Broken randomisation.** If the split is 50.0/50.0 by design but 52/48 in practice (a **sample ratio mismatch**), something is wrong with assignment; the result cannot be trusted.
- **Network effects and interference.** In a marketplace, treating one group changes the other. If variant riders get priority orders, control riders get fewer, and both groups are affected. Delivery and ride-hailing companies use **switchback tests** (whole cities alternate between A and B by time slot) or **geo tests** (compare matched cities) instead.
- **Winning the metric, losing the business.** A bigger "Buy Now" button may raise conversion and also raise returns. Guardrail metrics catch this.

**Contrasting cases.** A/B testing is the wrong tool when you have too little traffic, when the change is a big strategic bet whose effect takes months (a new pricing model, a brand repositioning), when it would be unethical or illegal to give some users a worse experience (safety features, regulatory disclosures), or when the change must be tested one variable at a time but you want to compare several elements together (use **multivariate testing**, which needs much more traffic).

::: key The one-line rule
Randomise, decide the metric and the sample size before you start, don't peek, and watch guardrails. A test that is too small or stopped early is worse than no test, because it gives false confidence.
:::

**In the interview.** "How would you test X?" wants hypothesis → primary and guardrail metrics → unit of randomisation (user, session, city) → sample size and duration → how you would decide. Strong line: *"For a rider-incentive change I wouldn't split riders within a city, because treated riders take orders from control riders. I'd run a switchback by city and hour and compare delivery time and cost per order."* Also be ready for: "The test shows +3% conversion but -2% revenue per user. Ship?" (depends on which is the goal metric and the long-term effect; dig into which segment drove each).

%% article | Technology · AI product quality | Evals: the PRD of an AI feature | How to define and test 'good enough' for a system whose outputs you cannot fully predict

For a normal feature, a tester can check that the "Cancel order" button cancels the order. For an AI support assistant, there are thousands of ways a customer can ask about a refund and many acceptable answers, and the same question can get slightly different answers each time. You cannot write down every correct output in advance. So how do you know it is good enough to launch, and how do you know a new model is better rather than just different?

An **eval** (evaluation) is a test for an AI system: you give it an input, grade the output with some grading logic, and measure how often it succeeds. A set of evals is how a team turns "good enough" into a number that can gate a launch.

## Two kinds, and you need both

| | Offline evals | Online metrics |
|---|---|---|
| When | During development, before shipping | In production, with real users |
| Data | A fixed, labelled set of test cases | Live traffic |
| Question answered | "Is the system good at the task?" | "Are users better off?" |
| Examples | Correct-answer rate on 300 real support conversations; hallucination rate on a labelled sample | Resolution rate, escalations to humans, CSAT, repeat contacts, A/B test results |

A model can pass offline evals and still disappoint users (the test set did not reflect real questions), or look popular online while quietly giving wrong answers (users do not know the answer is wrong). Hence both.

## Where the test cases come from

Build the eval set from **real failures**: your support queue, logged sessions, bug reports and complaints, not imagined scenarios. You do not need thousands to start. Anthropic's guidance on evaluating agents (January 2026) is that **20 to 50 tasks drawn from real failures** is a strong start. Every new failure you find becomes a new test case, so the set grows into a safety net that stops old mistakes from coming back.

```dia
title: The eval flywheel
loop([("Collect failures", "Support tickets, bad ratings, logged sessions"), ("Add to eval set", "Input + what a good answer must contain"), ("Change the system", "New prompt, model, retrieval or tool"), ("Run evals", "Score every version on the same set"), ("Gate the launch", "Ship only if the bar is met on every key slice"), ("Monitor online", "New failures surface in production")], center="Evals", center_desc="The set only grows; old bugs cannot return unnoticed", edges=["", "", "", "", "", ""])
```

## Who grades the output?

```dia
title: Three kinds of grader
cards([("Code-based checks", "Exact match, valid JSON, required fields present, test cases pass, cited source exists. Fast, cheap, objective; only works where 'correct' can be checked mechanically."), ("Human graders", "Experts label outputs against a rubric. Most accurate for nuanced quality; slow and costly. A few hundred well-labelled examples go a long way."), ("Model as judge", "Another LLM grades against a rubric. Cheap and scalable. Needs a clear rubric, an 'unknown' option so it does not invent a verdict, and regular checks against human labels.")], ncol=3)
```

A worked example. Before switching the model behind a support chatbot, the team runs 300 labelled conversations covering the top ten intents. The bar was set in advance: hallucination rate under 2%, and **no drop against the current model on any single intent**. The new model scores better overall but 8% worse on refunds. It does not ship for refunds; those failed conversations join the eval set so the same regression cannot slip through again.

**Why a PM cares.** The eval set is the closest thing an AI feature has to a PRD: it is where the quality bar actually lives. Without one you cannot tell an improvement from a regression. The rule of thumb in good AI teams: **no eval set, no launch**; if you cannot say which score would stop a launch, you do not have a bar. And **gate launches on quality metrics, never on engagement**: a chatbot that confidently gives wrong refund information can have excellent engagement.

%% article | Technology · AI product quality | Precision, recall and the threshold dial | Two ways to measure a model's mistakes, and why choosing between them is a product decision, not an ML one

A marketplace uses a model to flag fake listings. Every decision the model makes lands in one of four boxes.

```dia
title: The four outcomes of every yes/no prediction
sub: Example: a model that flags listings as fake
cards([("True positive (TP)", "Flagged, and it really was fake. A catch.", "#379A8B"), ("False positive (FP)", "Flagged, but it was genuine. A false alarm: a real seller wrongly punished.", "#E3120B"), ("False negative (FN)", "Let through, but it was fake. A miss: a buyer may get cheated.", "#E3120B"), ("True negative (TN)", "Let through, and it was genuine. Business as usual.", "#379A8B")], ncol=2)
```

Two metrics are built from these boxes:

- **Precision = TP ÷ (TP + FP).** Of everything the model flagged, how much was right? Flag 100 listings as fake, 80 truly are: precision is 80%.
- **Recall = TP ÷ (TP + FN).** Of everything that was actually fake, how much did the model catch? If 200 fake listings exist and the model catches 80: recall is 40%.

Why not just use **accuracy** (share of all decisions that were right)? Because when the thing you are looking for is rare, accuracy lies. If 1 in 100 payments is fraud, a "model" that never flags anything is 99% accurate and completely useless: its recall is zero.

## The threshold: one dial, two metrics

Most models do not output "fake" or "genuine"; they output a score, such as 0.73. The **threshold** is the cut-off above which the product acts. Raise it and the model only flags cases it is very sure about: fewer false alarms (precision up) but more misses (recall down). Lower it and it catches more, but also flags more genuine cases. **Precision and recall trade off against each other** as you move the dial.

```dia
title: Moving the threshold trades precision for recall
sub: Fake-listing model, illustrative
linechart({"Precision": [52, 64, 75, 84, 91, 96], "Recall": [95, 88, 76, 60, 41, 22]}, ["0.3", "0.4", "0.5", "0.6", "0.7", "0.8"], unit="%", notes=[("Precision", 4, "Seller moderation: few wrongful bans"), ("Recall", 1, "Payment fraud: catch most")])
```

**Calibration** matters too: a score of 0.9 means "90% likely" only if the model is calibrated, and many are not. Check before you build rules like "auto-ban above 0.9".

## Same maths, opposite answers

```dia
title: Which mistake hurts more?
versus("Seller moderation: protect precision", [("False positive", "Bans a real seller and takes away their income; damages trust with the supply side."), ("False negative", "A fake listing stays up a bit longer; can be caught by buyer reports."), ("Choice", "High threshold; send borderline cases to human review.")], "Payment fraud: protect recall", [("False positive", "One genuine payment is blocked; the user verifies and retries."), ("False negative", "Real money is lost; the fraudster tries again."), ("Choice", "Lower threshold; use step-up checks (OTP) instead of hard blocks.")], verdict="The engineer can set the threshold anywhere; only the PM can say which mistake hurts the user and the business more.")
```

**Why a PM cares.** "Improve accuracy" tells the team nothing. "Protect precision: we cannot ban genuine sellers; route anything between 0.6 and 0.85 to human review" tells them exactly what to build. Moving the threshold is also the cheapest lever you have: it needs no retraining. A related single number, **F1**, balances precision and recall, but a PM should usually say which one matters more rather than hide the choice in an average.

::: words Words to know
**Confusion matrix:** the 2×2 table of TP, FP, FN, TN. **Precision:** of flagged, share correct. **Recall (sensitivity):** of actual positives, share caught. **False positive rate:** of actual negatives, share wrongly flagged. **Threshold:** the score cut-off for acting. **Calibration:** whether a score of 0.8 really means 80%. **F1:** the harmonic mean of precision and recall.
:::

%% article | Technology · AI product quality | Guardrails and human-in-the-loop | Deciding what an AI system may say and do on its own, and where a person must step in

Air Canada learned in 2024 that a chatbot's words are the company's words: a Canadian tribunal ordered it to compensate a passenger whom its website chatbot had misinformed about bereavement-fare refunds, rejecting the airline's argument that the chatbot was responsible for its own words (Moffatt v. Air Canada, February 2024). Users forgive "I don't know". They do not forgive being confidently misled, and neither do regulators.

**Guardrails** are the controls that decide what an AI system may send to a user or do in the world. **Human-in-the-loop (HITL)** design decides where a person must step in.

## Guardrails: stopping confident-but-wrong output

```dia
title: The main guardrails, and what each costs
cards([("Grounding", "Answer only from retrieved sources, not from the model's memory. Costs: fewer questions answered."), ("Citations", "Show the source beside the claim so users can check. Costs: UI space; sources must be good."), ("Abstention", "If nothing relevant is retrieved, say 'I don't have that information' and offer a human. Costs: lower coverage."), ("Topic gates", "Route legal, medical, financial and other high-risk topics to a human whatever the confidence score. Costs: human time."), ("Input and output filters", "Block abuse, PII leaks, unsafe content and prompt-injection attempts. Costs: some false blocks."), ("Action limits", "Caps and allow-lists on what tools may do: refund ≤ ₹1,000, no deletes. Costs: more escalations.")], ncol=3)
```

The launch gate for a generative feature is usually the **hallucination rate**: the share of outputs containing a claim not supported by the sources, measured on a labelled sample. It must be measured directly, never inferred from complaint volume, because most users who are misled never realise it.

Guardrails cost **coverage**: fewer questions get answers, but the answers given can be trusted. Where to draw that line is the PM's call.

## Human-in-the-loop: how much does the machine do alone?

```dia
title: The automation spectrum
scale("Human only", "Fully automated", [("Human only", 0.03, "AI not involved: e.g. final medical diagnosis"), ("Human assisted", 0.35, "AI drafts or suggests; human decides and acts"), ("Human approves", 0.65, "AI prepares the action; one click to confirm"), ("Fully automated", 0.97, "AI acts; humans audit samples")], lnote="Slow and costly, maximum control", rnote="Fast and cheap, errors reach users directly")
```

Place the human gate on two axes: **confidence** (low-confidence cases go to a person) and **risk** (sensitive or irreversible actions go to a person regardless of confidence). The deciding variable is **reversibility: automate what can be undone; gate what cannot.**

```dia
title: Where to put the human
matrix("Cost of a mistake / irreversibility", "Model confidence", [("Automate", "Confident and cheap to fix: auto-tag tickets, fill CRM fields"), ("Human approves", "Confident but costly: refunds, account bans, payouts"), ("Automate with easy undo", "Unsure but harmless: suggest, let the user correct"), ("Human decides", "Unsure and costly: legal, medical, large money")], points=[("CRM auto-fill", 0.15, 0.8), ("Draft reply", 0.3, 0.3), ("Refund ₹8,000", 0.8, 0.75), ("Account ban", 0.85, 0.3)])
```

A worked example: an AI copilot for customer-support agents, with three automation levels chosen by reversibility. It **drafts replies**; the agent edits and sends, staying accountable for every message. It **auto-fills internal CRM fields** with no approval, because they are internal and easily corrected. It **never issues refunds on its own**, because refunds move money and cannot easily be undone. Same product, same model, three different answers, because the cost of being wrong differs.

One trap to design against is **automation bias**: when the model is usually right, people stop checking and start rubber-stamping. Countermeasures include showing the evidence behind a suggestion, occasionally sampling decisions for review, requiring edits on some cases, and tracking how often humans override the AI (an override rate near zero is a warning sign, not a success).

**Why a PM cares.** HITL design decides who is accountable when the system is wrong, a question that always comes up and is always a PM question. Raising it unprompted in an interview signals that you treat AI as **decision support with clear responsibility**, not as magic.

%% article | Technology · AI product quality | Cost per task: the unit economics of AI | Why AI features have a real cost every time they are used, how to count it honestly, and how it changes pricing

Traditional software is expensive to build and almost free to run for one more user. AI features are different: **every use costs money**, in model calls, retrieval and compute, and that cost never falls to zero.

**Cost per task** is the full cost of an AI system delivering one completed unit of user value, not the price of one API call. The honest version is **cost per resolved task**, which counts retries, escalations and failures.

```dia
title: Cost per resolved task
sub: Worked example from a support assistant
formula([("Calls per attempt", "Model calls for one attempt: understand, retrieve, answer", "3 calls"), ("Cost per call", "Tokens in and out × price", "₹2"), ("Success rate", "Share of attempts that actually resolve the issue", "60%")], result="Cost per resolved task = (3 × ₹2) ÷ 0.6 = ₹10, not ₹6", ops=["×", "÷"])
```

## The quality–latency–cost triangle

Every AI feature trades three things against each other, and you cannot set all three independently.

| Corner | What it means | How to measure |
|---|---|---|
| **Quality** | How good the output is | Your eval score, not user opinion |
| **Latency** | How long the user waits | p95, not the average; time-to-first-token for chat |
| **Cost** | What each completed task costs | Cost per resolved task, including retries and escalations |

Why they move together: a bigger model has more parameters, so every token it produces takes more computation; more computation costs more and takes longer. Reasoning models add "thinking" tokens on top. Pushing quality up drags latency and cost with it, unless you get clever.

```dia
title: The levers for bringing cost down without losing quality
cards([("Model routing", "Send easy requests to a small, cheap model; escalate only hard ones to a large or reasoning model."), ("Caching", "Never pay twice for the same work: cache repeated answers and reuse long, fixed prompt prefixes (prompt caching)."), ("Narrow the scope", "A focused feature ('track my order') costs far less per task than an open-ended 'ask me anything'."), ("Trim the tokens", "Shorter prompts, fewer retrieved chunks, capped output length."), ("Batch and defer", "Non-urgent jobs (overnight summaries) can run in cheaper batch mode."), ("Distil", "Train a small model on a big model's outputs for one narrow, high-volume task.")], ncol=3)
```

## Why this breaks per-seat pricing

Andreessen Horowitz found in 2020 that AI companies often spent a quarter or more of revenue on cloud resources, with gross margins materially below comparable software businesses (a16z, *The New Business of AI*). Usage-linked costs create a new pricing problem.

```dia
title: Same price, very different cost to serve
sub: An AI assistant at ₹500 per seat per month; monthly cost to serve by user type (illustrative)
bars([("Light user", 40, "Margin ₹460"), ("Typical user", 180, "Margin ₹320"), ("Power user", 520, "Loses ₹20"), ("Heaviest 10%", 900, "Loses ₹400 each")], fmt="₹{:,.0f}", hl=[3])
```

A flat fee against usage-linked cost means **the more successful the feature, the worse the margin can get**, and your heaviest, most enthusiastic users can be your least profitable. The average margin hides this. Every fix is a product decision: route simple queries to a cheaper model; cache repeated answers; cap usage in the base tier; or move from seat pricing to **usage-based** or **credit-based** pricing, or to **outcome-based** pricing (charge per resolved ticket), which aligns price with the value delivered.

::: key The one-line rule
Measure AI features by cost per *resolved* task and by quality on your evals, watch p95 latency, and price so that revenue rises with usage. Cost is a product constraint that shapes what you build, not a finance footnote.
:::

**In the interview.** "If there is an AI product and a non-AI product, how does your pricing strategy differ?" is asked directly. A strong answer: *"Non-AI software has near-zero marginal cost, so seat or flat pricing works. AI has a real cost per use that varies ten-fold between users, so I'd combine a base subscription with included usage and pay-as-you-go or credits beyond it, route easy work to small models, and track cost per resolved task by segment so we see loss-making power users early."* Other forms: "Our AI feature is popular but losing money; what do you do?", "Should we use the best model available?" (only where the eval gain justifies the cost and latency), "How would you launch an AI refund assistant?" (evals from real refund tickets, hallucination gate, abstention, human approval above a limit, cost per resolved refund).

::: quiz Check yourself
1. Walk through the five steps of an A/B test for a new checkout button. What is a guardrail metric?
2. Using the rule of thumb, roughly how many users per group do you need to detect a 1-point change from a 10% baseline?
3. Why are switchback tests used in delivery marketplaces?
4. What is the difference between offline evals and online metrics? Why do you need both?
5. Define precision and recall with the fake-listing example. Why is accuracy misleading for fraud?
6. For seller moderation and for payment fraud, which way would you move the threshold, and why?
7. Place four actions of a support copilot on the confidence–reversibility matrix.
8. Three calls at ₹1.50 each and a 50% success rate: what is the cost per resolved task?
9. *(From the RAG chapter)* How would you build an eval that separates retrieval failures from generation failures?
:::
