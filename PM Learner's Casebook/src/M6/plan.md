# M6 Streaming, music & entertainment: session plan (26 Sep 2026; revised: AR and VR removed at the owner's request; awaiting "go")

Rules applied: 3 cases + 2 guesstimates; only the approved frameworks (retention curves and cohorts; tiered pricing with price discrimination and a simple willingness-to-pay test); no page budget; non-AI language with the extra phrase scan; system design detailed with an everyday-analogy table and everyday picture → how it works → real example → PM decision per mechanism; blockchain in depth with worked examples; hashing, signatures and public/private keys named in one line (taught in M5), not re-taught.

## Cold open (top of the primer page)
Ahmedabad, IPL final, 7:28 pm. Two minutes before the first ball, crores of phones open JioHotstar at once. Priya, 24, gets a spinning wheel for eight seconds, then a blurry picture that sharpens as the over begins. Her father watches the same ball 30 seconds earlier on TV and phones her before she sees the wicket. The next morning, lakhs of people who subscribed for the IPL start deciding whether to keep paying. Try it: "If you ran JioHotstar, which would worry you more: the eight seconds of buffering on final night, or the people who cancel in June? Why?"

## Outline
1. **Sector primer (~5 pp)**
   - Value chain: studios and sports leagues (rights), platforms, telcos and TV makers (distribution and bundles), advertisers, viewers; who pays whom
   - Business models: subscription (SVOD), ads (AVOD), both (hybrid), pay per title (TVOD), free-to-play games (in-app purchases)
   - Unit economics in ₹: one subscriber's year (price − payment and telco-bundle cut − content cost per subscriber − streaming cost); why content is a fixed cost and why scale wins; IPL rights maths (cost per match per viewer)
   - Metrics: subscribers, ARPU, churn, watch time, completion rate, concurrency, rebuffering ratio, ad fill and CPM, royalty per stream
   - Players and numbers (dated): JioHotstar, Netflix, Prime Video, YouTube, Zee5, SonyLIV, Spotify, JioSaavn, Gaana, games (BGMI, real-money gaming ban)
   - Turning points: Jio's cheap data (2016); Covid and direct-to-OTT releases (2020); JioCinema's free IPL (2023); Jio–Disney merger into JioHotstar (Nov 2024 → Feb 2025); Netflix's paid sharing (2023); India's Online Gaming Act banning real-money games (Aug 2025)
   - Non-obvious mechanics: sports buys sign-ups, series keep them; subscription "churn and return" around big events; music royalties make streaming margins thin; piracy; the long tail
   - Questions interviewers love
2. **Cases (3)**
   - 6.1 Improve Hotstar (Improvement · B105–106) → framework box: **retention curves and cohorts** (the IPL cohort that joins in March and leaves in June)
   - 6.2 Prime Video views fall 20% (RCA · B80–81; B81's journey picture redrawn "from the original") → no box (RCA sequence taught in M1); one Key idea: a gradual fall across every segment points outside the product
   - 6.3 Netflix pricing and paid sharing in India (Pricing · A299) → framework box: **tiered pricing (good–better–best)**, with price discrimination and a simple willingness-to-pay test; family plans shown as one worked example (the lesson of the dropped JioSaavn cases)
   - **Dropped:** Podcasts on Spotify (A254–255: design thinking already taught in M2 UX; its Double Diamond is on the dropped list), BookMyShow engagement (A317–318: overlaps 6.1's retention lesson), Improve YouTube (B120–121: third improvement case; DHM dropped), JioSaavn family plan, both takes (A298, B92: family plans covered inside the 6.3 framework box)
3. **Guesstimates (2):** G6.1 YouTube revenue a day (A236); G6.2 users of a Bhojpuri short-movie app (B144). Short kit reminder; each with kit-check line, stronger answer, equation tree, sanity check, reusable trick.
4. **Teardowns (5):** Netflix · JioHotstar (with Prime Video as the comparison) · YouTube (with Moj and Twitch) · Spotify (with JioSaavn) · Zynga (free-to-play game economics). Then a comparison table and a 2×2: how the viewer pays (ads → subscription) against what keeps them (live events → a library).
5. **Technology (~10 pp)** (AR and VR dropped, owner, 26 Sep 2026)
   - **Blockchain, in depth (IIM A p. 101), ~4–5 pp.** Running everyday picture: a village's shared ledger book copied in every house.
     1. A block: a page of transactions (worked example with 3 payments)
     2. The chain: each page carries the previous page's fingerprint; change one entry and every later fingerprint breaks (worked with short real hashes)
     3. Consensus: who gets to write the next page; proof of work (the puzzle, energy maths) and proof of stake (a deposit you can lose); a 51% attack in plain words
     4. Wallets and keys: your address, your private key, "not your keys, not your coins"; lost keys (maths of coins lost for good)
     5. Smart contracts: a vending machine in code; a worked escrow example; the DAO hack (2016) as the failure
     6. Real uses and failures: crypto payments (India's 30% tax and 1% TDS), stablecoins; supply-chain pilots (Walmart's mango trace from 7 days to 2.2 seconds; TradeLens shut in 2022); the e-rupee (RBI CBDC pilots since Dec 2022, and why it doesn't need a public blockchain); NFTs (2021 boom, bust); music royalties on-chain
     7. When it is *not* the answer: a five-question test (many writers who don't trust each other? no trusted party? need for tamper evidence? tolerable speed and cost? data that can be public?), with a scored table for 5 proposals
   - **System design V: video streaming at IPL scale (detailed), ~5–6 pp.** Running everyday picture: milk distribution (dairy → chilling centres → neighbourhood booths → your door). Each mechanism: everyday picture → how it works → real example → PM decision, with a diagram and light maths:
     1. The load: concurrency (crores watching at once), bandwidth maths (viewers × bitrate = Tbps), why live is harder than on-demand
     2. Encoding and the bitrate ladder (one match cut into 6–8 qualities; codecs; storage and cost)
     3. Segments and adaptive bitrate (HLS/DASH, 4–6 s chunks, the player choosing quality every few seconds; buffer maths)
     4. CDNs and edge caching (hit rate arithmetic; origin shield; caches inside ISPs such as Netflix Open Connect)
     5. Live latency (glass-to-glass delay; why TV beats the app by 20–40 s; the spoiler problem; low-latency trade-offs)
     6. The toss-time spike: pre-warming, login and payment storms, autoscaling limits, waiting rooms
     7. Ads inside live sport (server-side ad insertion; personalised ads to crores in the same 30-second break)
     8. Graceful degradation on final night (drop 4K first, turn off extras, never the match); rebuffering ratio and start time as the SLIs
     9. On-demand is different: pre-positioning the next episode, download for offline, popular-at-night caching
     10. DRM and piracy (why a leak appears hours after a release; watermarking)
     - Closing: an "IPL final night plan" table
6. **Connect the dots (~1 p)** with a sketch answer to the cold open

## Frameworks (approved list only)
- **6.1:** Retention curves and cohorts (one box): everyday example (a gym's January joiners), cohort table, curve shapes (flattening vs falling to zero), "smile" curves after events, the IPL cohort maths, when averages mislead
- **6.3:** Tiered pricing (one box): good–better–best, the decoy, price discrimination (by device, by time, by bundle), a simple willingness-to-pay test (ask four price questions, plotted), family plans as a worked example
- Named in one line only where useful: RCA sequence (M1), North Star and guardrails (M1), RICE (M1), elasticity (M3)
- **Dropped:** Double Diamond, ICE, Biddle's DHM, seasonality as a box, Van Westendorp as its own box (its idea sits inside the tiered-pricing box as the "simple willingness-to-pay test")

## Early catches to teach (from reading the cases)
- **6.1:** the candidate's "RICE" is High/Medium/Low letters with no numbers, and the top pick (a Reddit-style forum) is rated High effort yet ranked first. No North Star; five metrics, none tied to loyalty. And the real loyalty problem for Hotstar is post-IPL churn, which none of the features touch. Also check what already existed (Hotstar's social and watch-along features during IPL).
- **6.2:** good clarifying questions (definition, size, timing, platform, region), but the external/internal checks were a list of guesses; the interviewer had to reveal the cause. "Sachet pricing" (pay per season) partly exists already: Prime Video's rental store (TVOD) in India. And a 70%-watched "view" can fall because of a product change (longer shows, autoplay) without anyone leaving.
- **6.3:** a strong 5 Cs opening, but "5 Cs" is recitation; the real insight is the new "converted sharer" segment. The ₹99 extra-member idea needs a check against what Netflix actually does in India, and the answer never tests willingness to pay or cannibalisation of the ₹199 plan.

## Diagrams (~50; one line each)
- **Primer:** who pays whom (rights → platform → viewers, advertisers, telcos); one subscriber's year as a ₹ waterfall; content cost as fixed cost (cost per subscriber falls with scale, chart); IPL rights per match per viewer chain; players chart; turning-points timeline; churn-and-return around IPL (subscriber line through a year); music royalty split of ₹1 per stream
- **Case 6.1:** move strip; retention curves (three shapes); cohort table heat map (IPL cohort vs non-IPL cohort); "what keeps an IPL joiner" driver tree
- **Case 6.2:** move strip; user journey redrawn from the original (B81); views = viewers × starts × completion driver tree with where a 20% fall could hide
- **Case 6.3:** move strip; Netflix and rivals' price ladder; good–better–best with a decoy; willingness-to-pay curves (four questions); paid-sharing conversion funnel in ₹
- **Guesstimates:** two strips; two equation trees
- **Teardowns (×5):** behind-the-screens flows: pressing play on Netflix (licence, CDN, ABR); an IPL ad break on JioHotstar; a YouTube creator's upload to payout; a Spotify stream to royalty; a Zynga player's first purchase; plus loops or money charts per product; comparison 2×2
- **Technology:**
  - Blockchain: village ledger analogy table; a block with 3 payments; chain of fingerprints with one tampered entry; proof of work puzzle and energy; proof of stake deposit; wallet/keys; escrow smart contract flow; e-rupee vs crypto vs UPI comparison; "do you need a blockchain?" decision tree; scored proposals table
  - System design V: milk-distribution analogy table; bitrate ladder; segments and the player buffer; ABR switching over time; CDN tiers (origin → shield → edge → ISP cache) with hit-rate maths; glass-to-glass latency bar; toss-time spike and pre-warming; server-side ad insertion flow; degradation ladder; DRM and watermark flow

## Light maths planned
- A subscriber's year: ₹1,499 − cuts − content cost share = margin (illustrative)
- IPL rights: rights ₹ per match ÷ viewers = paise per viewer per match
- Retention: 100 → 40 → 25 → 22 cohort; LTV from a flattening vs a falling curve
- Views = viewers × starts per viewer × share reaching 70%; which factor must fall 20%
- Paid sharing: sharers × conversion × fee vs lost subscribers
- Willingness to pay: share of people who'd pay at ₹99 / ₹149 / ₹199 → revenue at each price
- Blockchain: hash change on one edit; proof of work guesses (2^n); energy per transaction vs a UPI payment; lost-key coins
- Streaming: 5 crore viewers × 1.5 Mbps = 75 Tbps; CDN hit rate 95% vs 99% → origin load 5×; buffer seconds; latency budget; storage for a bitrate ladder

## Research (one light batch)
- JioHotstar subscribers and IPL 2025/2026 peak concurrency; Jio–Disney merger dates; IPL media-rights value (2023–27)
- Netflix India prices 2026 and paid-sharing status in India; Netflix Q2 2026 results
- Prime Video India (ads tier launch, rental store); YouTube India users, Shorts; YouTube ad revenue Q2 2026
- Spotify Q2 2026 (MAU, subscribers, profit); JioSaavn/Gaana status; music royalty rules
- Online Gaming Act 2025 (real-money ban); Zynga under Take-Two
- RBI e-rupee status; India crypto tax; TradeLens; Walmart mango trace
- Reuse drafts 210 (OTT video), 212 (ad-supported media), 213 (gaming), 311 (blockchain) and the research notes

## Length
No page budget. Length follows content; kept tight by cutting repetition.

## Numbering and build
- Figures 6.n
- Build copied from `src/M5/build.py` (with the EXTRA phrase scan and `.sw{break-inside:avoid}`), `m6_figs.py` helpers plus `figs_primer.py`, `figs_cases.py`, `figs_teardowns.py`, `figs_tech.py`
- Long figure code written with the Write tool; update scripts written to files
