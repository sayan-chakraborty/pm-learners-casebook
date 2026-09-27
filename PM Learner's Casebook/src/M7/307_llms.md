%% chapter | Technology · Large language models | The world's most well-read autocomplete | How LLMs turn a prompt into an answer one token at a time, what the settings do, which kind of model to pick, and how to write prompts that work

Type "Happy birth" on your phone and the keyboard suggests "day". It has seen that pattern many times. Now imagine a keyboard that has read a large share of all the public text ever written, in dozens of languages, plus code, and that looks at your entire message, not just the last word, before suggesting what comes next. Keep accepting its suggestions and it will write the whole email for you. That, at its heart, is a **large language model (LLM)**.

An LLM is a very large neural network trained on huge amounts of text to do one thing: **predict the next piece of text**. Everything else, answering questions, summarising contracts, writing code, translating Tamil to Hindi, emerges from doing that one thing extraordinarily well.

## Prediction, one token at a time

Give a model the prompt "The first person to walk on the Moon was". It does not look up a fact. It calculates, for every possible next piece of text in its vocabulary, how likely it is to come next.

```dia
title: What the model 'sees' after 'The first person to walk on the Moon was'
sub: Probabilities for the next token (illustrative)
bars([("Neil", 0.82, "Overwhelmingly common in text it learned from"), ("Buzz", 0.09, "Plausible: Aldrin is often mentioned alongside"), ("an", 0.04, "'…was an American astronaut'"), ("Yuri", 0.01, "Wrong, but close in 'space' context"), ("Mickey", 0.00001, "Near zero, but never exactly zero")], fmt="{:.2f}", hl=[0])
```

It picks a token (usually one of the likely ones), adds it to the text, and repeats the whole calculation to predict the token after that, and so on until the answer is complete.

```dia
title: How an LLM generates an answer
sub: The loop runs once per token; a 300-word answer is roughly 400 loops
steps([("Tokenise", "Split the prompt into tokens (word pieces) and turn each into numbers", "Hindi and Tamil often need more tokens per word than English"), ("Embed", "Each token becomes a vector: a list of numbers that captures its meaning", "Similar meanings sit close together"), ("Transformer layers", "Attention lets every token look at every other token to understand context", "The expensive part"), ("Probabilities", "Score every possible next token", "Settings like temperature act here"), ("Pick and repeat", "Choose one token, append it, loop until done", "Output speed = tokens per second")], hl=[2])
```

**Tokens** are the unit of everything in LLM products: pricing, speed and limits. A token is a word or a piece of a word; in English, one token is roughly three-quarters of a word on average. Many Indian-language scripts are split into more tokens per word, which quietly makes the same answer in Hindi or Telugu slower and more expensive than in English, a real product consideration for Bharat-first apps.

The **context window** is the model's working memory: the maximum number of tokens (your prompt, any documents you paste, the conversation so far, and the answer) it can consider at once. It ranges from thousands to over a million tokens depending on the model. Anything outside the window, the model simply does not see.

**Embeddings** deserve a moment because they return in the RAG chapter. The model turns each token, and can turn whole sentences, into a long list of numbers, like coordinates on a map of meaning. "Refund" and "money back" land close together; "refund" and "biryani" land far apart. That is how an AI system can find the right help article even when the user's words do not match the article's words.

## The transformer and attention

Before 2017, language models read text roughly word by word and struggled to connect words far apart. In 2017, a team at Google published *Attention Is All You Need*, introducing the **transformer**. Its key idea, **attention**, lets every word look at every other word in the passage and decide which ones matter for understanding it.

Read this: "The robot picked up the heavy box because **it** was strong." You know "it" means the robot. Change one word: "…because **it** was light." Now "it" means the box. Attention is how the model makes the same leap: when processing "it", it weighs "strong" and "robot" heavily in the first sentence and "light" and "box" in the second.

```dia
title: Attention, as a highlighter
sub: Processing 'it', the model weighs other words by relevance (illustrative weights)
bars([("robot", 0.46, "Strongest link: a robot can be 'strong'"), ("strong", 0.31, "The clue that decides it"), ("box", 0.12, "Considered, then down-weighted"), ("heavy", 0.07, ""), ("picked", 0.04, "")], fmt="{:.2f}", hl=[0, 1])
```

The "GPT" in ChatGPT stands for **Generative Pre-trained Transformer**: it generates text, it was pre-trained on a large corpus, and it is built on the transformer. Most of today's major models use this architecture.

## How an LLM is made

```dia
title: From raw text to a helpful assistant
vsteps([("Pre-training", "The model reads trillions of tokens of text and code, learning to predict the next token (self-supervised). This takes months on thousands of chips and costs very large sums.", "Result: a knowledgeable but unruly 'base model'"), ("Instruction tuning", "Trained on curated examples of good answers to instructions, so it follows requests instead of just continuing text.", "Result: an assistant that answers"), ("Reinforcement learning from feedback", "People (and increasingly automated graders) compare answers; the model is rewarded for helpful, honest, harmless ones. Reasoning models are also trained with rewards on checkable tasks like maths and code.", "Shapes tone, safety and reasoning"), ("Deployment", "Served through an app or an API; companies may add their own instructions, data (RAG), tools and fine-tuning.", "Knowledge frozen at a training cutoff date")], hl=[0])
```

Two consequences matter for products. First, the model's knowledge stops at its **training cutoff**; it does not know yesterday's news or your company's refund policy unless you give it that information in the prompt (which is what RAG does). Second, because it generates the *likeliest-sounding* continuation, it can produce fluent, confident, **false** statements: **hallucinations**. The model is optimised to be plausible, and plausible is usually but not always true.

## Controlling the output: temperature, top-k and top-p

Remember that the model picks from a list of probabilities. Three settings change how it picks.

- **Temperature** controls randomness. Low (for example 0–0.3) makes the model almost always pick the most likely token: consistent, predictable, a little bland. High (0.8–1.0+) flattens the probabilities so less likely tokens get picked more often: more varied and creative, and more likely to drift or make things up.
- **Top-k** restricts the choice to the *k* most likely tokens. With k = 1, the model always takes the top option.
- **Top-p** ("nucleus sampling") restricts the choice to the smallest set of tokens whose probabilities add up to *p*, say 90%. When the model is confident, that set is tiny; when it is unsure, the set is wider.

```dia
title: Match the temperature to the task
scale("Low temperature: predictable", "High temperature: creative", [("Invoice extraction", 0.03, "Same input, same output"), ("Policy answers", 0.22, "Accurate and consistent"), ("Meeting summary", 0.42, ""), ("Draft a marketing email", 0.65, "Some variety helps"), ("Brainstorm 20 names", 0.92, "Surprise is the point")], lnote="Facts, data, compliance", rnote="Ideas, copy, variety")
```

Other controls you will meet: **maximum output tokens** (caps length and cost), **stop sequences** (where to stop), a **system prompt** (standing instructions the user does not see, such as tone, rules and persona), and **structured outputs** (forcing the answer into a fixed JSON format so software can use it reliably). Some providers fix or limit sampling settings on their reasoning models; there, the prompt and the choice of model matter more than the dials.

::: words LLM vocabulary
**Token:** a word or word-piece; the unit of pricing and limits. **Context window:** how many tokens the model can consider at once. **Embedding:** numbers representing meaning, used for semantic search. **Inference:** running the model to get an answer (as opposed to training it). **Latency:** often split into time-to-first-token (how soon text starts appearing) and tokens per second. **Hallucination:** a fluent but unsupported or false output. **Fine-tuning:** further training a model on your own examples to specialise it. **Open-weight model:** a model whose weights you can download and run yourself (Llama, Mistral, Qwen, Gemma, DeepSeek); **closed model:** used only through the provider's API (GPT, Claude, Gemini).
:::

## The model landscape: pick the right tool

"LLM" is used as a catch-all, but product teams choose among quite different kinds of models.

| Model type | What it is | Typical PM use |
|---|---|---|
| Frontier LLM | Largest general-purpose models; best quality, highest cost and latency | Complex assistants, research, hard writing and coding |
| Small language model (SLM) | Compact, fast, cheap; can run on-device or at huge volume | Classify tickets, extract fields, short summaries, autocomplete |
| Reasoning model | Spends extra tokens "thinking" step by step before answering | Multi-step analysis, maths, planning, tricky code; slower and costlier per answer |
| Multimodal model | Takes text, images, audio, sometimes video, together | Read a photo of a bill, understand a screenshot, voice conversations |
| Image / video generation | Creates visuals from prompts | Creatives, mock-ups, catalogue images |
| Speech models | Speech-to-text and text-to-speech | Voice bots, call-centre transcription, vernacular access |
| Domain or regional model | Tuned for a field (law, medicine, finance) or languages; for example, India's IndiaAI Mission backs home-grown models focused on Indian languages | Contract review, clinical notes, Indic-language assistants |

Note one common confusion: an **AI agent** is not a type of model. It is a *system* that uses one or more models together with tools, memory and a loop of actions. Agents get their own chapter.

**Choosing among them is a three-way trade** between quality, latency and cost, which the chapter on AI product quality covers in detail. The practical pattern is **routing**: send easy requests to a small, fast model and escalate only hard ones to a large or reasoning model.

```dia
title: Model choice is a quality–speed–cost trade
matrix("Cost and latency per request", "Quality on hard tasks", [("Rare sweet spot", "High quality, cheap; often a well-prompted mid-size model on a narrow task"), ("Frontier and reasoning models", "Best answers; slowest and most expensive; use when errors are costly"), ("Small models", "Fast and cheap; great for simple, high-volume tasks"), ("Avoid", "Paying more for no gain; common when teams default to the biggest model")], points=[("SLM on-device", 0.12, 0.18), ("Mid-size model", 0.36, 0.6), ("Frontier LLM", 0.6, 0.64), ("Reasoning model", 0.78, 0.56)])
```

## Prompt engineering: directing a brilliant improviser

If an LLM is a gifted improv actor, the prompt is the script and the director's notes. The same model can give a vague, generic answer or an excellent one depending on how it is asked. **Prompt engineering** is the craft of designing inputs that reliably produce useful, correctly formatted outputs.

```dia
title: The same request, prompted weakly and well
versus("Weak prompt", [("Prompt", "Summarise this customer feedback."), ("What you get", "A generic paragraph, different every time, mixing bugs with praise, no numbers.")], "Strong prompt", [("Role and goal", "You are a PM analyst. Goal: help the team prioritise fixes."), ("Context", "Here are 200 app reviews from the last week, between <reviews> tags."), ("Task and format", "Group into Bug, Feature request, UX issue. For each group: count, top 3 themes, one quote. Output as a table."), ("Example and rules", "One labelled example; 'If a review fits none, put it in Other. Do not invent quotes.'")], verdict="Clear role, context, task, format, examples and rules turn a party trick into a reliable tool.")
```

| Technique | What it means | Example |
|---|---|---|
| **Zero-, one-, few-shot** | Give no, one or a few worked examples so the model copies the pattern | "Here are 3 labelled reviews. Label these 20 the same way." |
| **Role prompting** | Ask the model to act as a persona to set expertise and tone | "Act as a PM. Summarise this idea for the CEO in five bullets." |
| **Chain-of-thought** | Ask it to reason step by step before answering | "Should we launch in Southeast Asia? Think through market size, competition, cost, then decide." |
| **ReAct (reason + act)** | Alternate reasoning with tool use, such as web search or a database lookup | "Search current iPhone prices in India, compare with last quarter, then recommend." |
| **Structured output** | Demand a fixed format, often JSON, so software can parse it | "Return {intent, urgency, order_id}." |
| **Prompt chaining** | Split a big task into steps, each its own prompt | Extract facts → check facts → write summary |

Practical rules that hold up: **start simple**, then add detail only where output falls short; **be explicit** about format, length, tone and audience; **say what to do** rather than only what to avoid; **show examples** of good output; **separate instructions from data** with clear markers; and **test and save**: keep prompts in version control and run them against an eval set whenever you change them or the model. Reasoning models do much of the step-by-step thinking on their own, so with them, clarity of goal and context matters more than "think step by step" tricks.

::: key The one-line rule
An LLM predicts plausible text, not truth. Control it with the right model, the right settings and a clear prompt, and give it the facts it needs rather than trusting what it remembers.
:::

**Contrasting case.** Prompting cannot fix missing knowledge or unreliable facts. If the model does not know your refund policy, the best prompt in the world will produce a confident guess. That problem needs retrieval (RAG), tools, or a narrower task, covered next.

**Why a PM cares.** Tokens are your unit cost: long prompts, long documents and long answers cost money on every request. Latency is time-to-first-token plus generation speed; streaming the answer word by word makes a 6-second answer feel fast. Temperature and model choice are product decisions tied to the job. And prompts are product assets that need owners, versions and tests, just like code.

**In the interview.** "Explain how ChatGPT works to your grandmother" (a super-autocomplete that has read a library and predicts the next word, very well), "Why does it hallucinate?" (it optimises for plausible, not true; no built-in fact-check; knowledge cutoff), "What would you set temperature to for a banking support bot?" (low, for consistency), "How would you reduce cost for an AI feature?" (smaller model for easy cases, shorter prompts, caching, limits on output length). A strong line: *"I'd treat the model as a component with a price per token and a quality score, and pick the smallest one that clears our eval bar."*

::: quiz Check yourself
1. In one sentence, what does an LLM actually do? Walk through the five-step generation loop.
2. What is a token, and why can the same answer cost more in Hindi than in English?
3. Explain attention using the 'robot and box' sentence.
4. What are pre-training and reinforcement learning from feedback for?
5. What do temperature, top-k and top-p change? Pick settings for invoice extraction and for brainstorming.
6. Why is an AI agent not a 'type of model'?
7. Rewrite "Analyse our churn" as a strong prompt using role, context, task, format and rules.
8. *(From the ML chapter)* How is the self-supervised pre-training of an LLM different from supervised learning for fraud detection?
:::
