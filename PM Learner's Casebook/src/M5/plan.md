# M5 Social, creators & messaging: session plan (26 Sep 2026, revised after owner feedback; awaiting "go")

**Owner feedback on the first plan (26 Sep 2026):** make encryption more detailed; don't repeat frameworks; then: keep only essential frameworks, no page budget. Changes: no separate platform-economics or trust sections in the tech block (both taught once, inside the cases); no framework box in 5.2 (multi-stakeholder metrics would re-teach two-sided users, North Star + guardrails and liquidity); one framework box per case idea, never twice; encryption becomes its own ~4-page section.

## Cold open (top of the primer page)
Lucknow, Sunday 9:15 pm. Farhan's family WhatsApp group (47 members) has sent 212 messages today: good-morning flowers, a wedding card, a forwarded "news" video. His cousin moves the family to a Telegram group "because WhatsApp is shutting down free groups". Three days later everyone is back on WhatsApp. Try it: "Why did the move fail, and what would it take for a rival to actually pull a family group away?"

## Outline
1. **Sector primer (~4 pp)**
   - Value chain: users (attention), creators (content), advertisers (money), the platform (ranking + ads), telcos and phone makers; who pays whom
   - Unit economics in ₹: revenue per user (ARPU) India vs world; one hour of scrolling, worked out (ads seen × price per 1,000 views); why a free messaging app is hard to monetise
   - Metrics: DAU/MAU (stickiness), time spent, sessions, ad load, CPM, ARPU, creator payouts, content per creator, reports per million
   - Players and numbers (dated): Instagram, Facebook, WhatsApp, YouTube Shorts, Snapchat, X, Threads, Telegram, ShareChat/Moj, Josh; India user counts
   - Turning points: TikTok ban (June 2020) and the short-video rush; WhatsApp privacy-policy update (Jan 2021) and the Telegram/Signal surge; feeds moving from friends to recommended content (2022–26); IT Rules 2021 and the DPDP Act 2023
   - Non-obvious mechanics: most users watch, few post (the 90-9-1 idea); ranking decides reach; ads pay for everything; forwarding limits; India is a volume market with low ARPU
   - Questions interviewers love
2. **Cases (3, owner's rule from M5)**
   - 5.1 LinkedIn for blue-collar workers (Design · B46–47)
   - 5.2 Instagram creator commerce (Metrics · A288–289)
   - 5.3 Users moving from WhatsApp to Telegram (Strategy · B149–150)
   - **Dropped:**
     - Facebook Reactions (A316): an engagement idea list; the Hooked loop is shown in the Instagram teardown instead, and Fogg's B = MAP moves to M7 (behaviour change)
     - WhatsApp in-app video (A295): its lesson (counter-metrics) was taught in M1 as guardrails
     - Gmail success metrics (B154–155): its framework (GAME) is gas next to North Star + HEART
3. **Guesstimates (2)**
   - G5.1 Instagram posts a day in India (A235)
   - G5.2 WhatsApp chats a day in India (B136)
   - Short kit reminder only; card 5 now names two checks (a per-person ratio and a published figure). Each gets the kit-check line, a stronger answer, an equation tree, a sanity check and the reusable trick.
4. **Teardowns (5):** Instagram (with Threads) · Facebook (with Meta's ad machine) · X · Snapchat · WhatsApp (with WhatsApp Pay, Business messaging, Messenger, and Telegram as the comparison). Then a comparison table and a 2×2: who you talk to (friends → strangers and interests) against how private it is (broadcast → private messages).
5. **Technology (~8–9 pp)**, following the owner's system-design rule (everyday-analogy table first; each mechanism: everyday picture → how it works → real example → PM decision)
   - **IIM A p. 111 (platform economics) and p. 137 (trust) are taught inside the cases, not repeated here:** network effects and tipping in 5.1, trust and safety in 5.1, switching costs and multi-homing in 5.3. The Facebook teardown carries the content-moderation pipeline as a flow.
   - **System design IV: one WhatsApp message, end to end (~4 pp).** Running analogy: India Post and a registered letter.
     - always-on connections vs polling (with requests and battery maths)
     - the message journey and the three ticks
     - store and forward while the phone is off
     - order and duplicates, kept short
     - group fan-out: 1 message to 1,023 members; messages a day converted to per second
     - push notifications through Apple's and Google's services
     - media uploaded once and shared as a link
   - **Encryption, in detail (~4–5 pp).** Each part gets an everyday picture, how it works, a real example and the PM decision:
     1. What can be seen on the way: café Wi-Fi, the telecom, the company's own server
     2. Hashing, the fingerprint: passwords stored as salted hashes; one changed letter changes the whole fingerprint; what a password leak exposes
     3. Symmetric encryption, one key for both sides (AES): fast, but how do you share the key? Maths: 2^128 keys, and how long guessing would take
     4. Public and private keys, the open padlocks you hand out: why they solve key sharing. Maths: keys needed for 1,000 people, 4,99,500 shared keys vs 2,000
     5. Digital signatures, the seal only you can make: signed app updates, Aadhaar e-sign
     6. Key exchange, the paint-mixing picture of Diffie–Hellman: agreeing a secret in public
     7. Encryption in transit vs end to end: the post office that opens and re-seals your letter vs a locked box only the receiver opens; what the server sees in each case
     8. How WhatsApp's end-to-end encryption works (Signal protocol):
        - keys made on the phone
        - pre-keys so you can message someone who is offline
        - a new key for every message ("ratchet"), so a stolen key can't read old messages (forward secrecy)
        - the security code / QR check against an eavesdropper in the middle
        - sender keys for groups
        - separate keys for each linked device
        - end-to-end encrypted backups (2021)
     9. What end-to-end encryption doesn't hide:
        - metadata (who, when, how often)
        - an unlocked phone, screenshots and forwards
        - unencrypted backups
        - messages a user reports
     10. The PM trade-offs:
        - features that stop working on content the server can't read (server-side search, spam filtering, AI summaries), and the on-device or opt-in alternatives
        - no recovery if a backup key is lost
        - forwarding limits as a design answer to misinformation
        - the traceability demand in India's IT Rules 2021 (WhatsApp's challenge in the Delhi High Court)
6. **Connect the dots (~1 p)**, with a sketch answer to the cold open

## Frameworks (owner, 26 Sep 2026: essential only, each taught once)
- **5.1:** **Network effects and cold start** (one box): direct, cross-side and local effects; when a market tips to one winner; the smallest network that works on its own, with density maths. Trust (fake jobs, deposit scams, verification) is handled inside the stronger answer, not as a box.
- **5.2:** **no framework box.** The who-wins, who-loses grid is a figure in the stronger answer; attribution is a Check.
- **5.3:** **Switching costs** (one box): data, learning, social ("my family is here") and money, plus multi-homing (people keep both apps). 7 Powers is dropped.
- **That's two framework boxes in M5.**
- **Dropped:** 7 Powers, trust and safety as a box, multi-stakeholder metrics, GAME, Fogg (to M7), Hooked (loop diagram only).

## Early catches to teach (from reading the cases)
- **5.3:** the candidate's first idea is "end-to-end encryption for all communication, including backups". WhatsApp has encrypted all chats end to end since 2016 and offered encrypted backups since 2021. This is the fourth case in a row where "what exists today?" was the costliest skip.
- **5.2:** the metrics have no North Star and no guardrail, and the case skips the brand side on the interviewer's instruction. The stronger answer adds the platform's goal and the conflicts between creators, buyers and brands.
- **5.1:** a good flow (voice intro, nearby jobs, digital agreement), but no cold-start plan (which city and trade first, and how many employers make the first workers stay) and thin scam protection. The metrics count profiles, not hires.

## Diagrams (~45; one line each)
- **Primer**
  - Money flow: users' attention → ads → platform → creators
  - ₹ per user: India vs world ARPU bars
  - One hour of scrolling, worked into ad revenue
  - Players chart (India users)
  - Turning-points timeline
  - The 90-9-1 pyramid (watch, react, create)
  - How a feed ranks one post (signals → score)
- **Case 5.1:**
  - move strip
  - three kinds of network effect
  - atomic network: one trade in one area, with the density maths
  - scam flow with the checkpoints that stop it (inside the stronger answer)
- **Case 5.2:**
  - move strip
  - three stakeholder journeys
  - who-wins, who-loses grid
  - tag funnel from views to purchases, with ₹
- **Case 5.3:**
  - move strip
  - Jan 2021 timeline: the policy update, the Telegram/Signal surge, and why most people stayed
  - switching-cost stack for one family group
  - multi-homing: how many people keep both apps, and what that means for “moving”
- **Guesstimates:** two strips; two equation trees
- **Teardowns (×5)**
  - Behind-the-screens flows: an Instagram Reel from upload to feed; Facebook's ad auction for one slot; an X post and reply; a disappearing Snap; a WhatsApp Business message with a UPI payment
  - Loops: Instagram's Hooked loop, creators' loop; money charts; the comparison 2×2
- **Technology**
  - India Post analogy table
  - Polling vs an always-on connection
  - Message journey with the three ticks
  - Store and forward
  - Group fan-out
  - Push notification path
  - Media sent once, as a link
  - Hash fingerprint (one letter changed)
  - Symmetric vs public-key padlocks
  - Keys needed: shared keys vs key pairs
  - Paint-mixing key exchange
  - Signature and verify
  - Encryption in transit vs end to end: what the server sees
  - WhatsApp's key ratchet and forward secrecy
  - Security-code check against an eavesdropper
  - What end-to-end does and doesn't hide
- **Removed:** platform vs pipeline, subsidy side, network-value curve, multi-homing, moderation (moved into cases/teardowns or dropped). **Total ~40 figures.**

## Light maths planned
- ARPU gap: revenue ÷ users, India vs US
- Ad revenue from one hour of scrolling (ads seen × CPM ÷ 1,000)
- Network value n(n−1)/2 for a 47-member family group (1,081 pairs), and why value doesn't keep growing that fast
- Cold-start density: jobs a worker must see nearby before they come back
- Creator-commerce funnel in ₹ (views → taps → purchases × order value × commission)
- Switching cost of one family group: people × effort to move
- Group fan-out: 1 message × 1,023 deliveries; messages a day converted to per second
- Polling vs push: requests saved and battery
- Encryption: 2^128 guesses in years; shared keys n(n−1)/2 vs key pairs 2n for 1,000 people
- Moderation reviewers: reports a day ÷ reviews per reviewer (in the Facebook teardown)

## Research (one light batch)
- Meta Q2 2026 (have), Instagram India users, WhatsApp India users, Threads (have)
- Telegram (have), plus its Jan 2021 surge figures
- X and Snap (have); ShareChat/Moj
- WhatsApp: Pay's UPI share and the NPCI user cap lifted (Dec 2024); usernames; Channels; Business messaging prices (have)
- Instagram product tags and shopping changes (Live Shopping ended 2023)
- Blue-collar jobs: Apna, WorkIndia, e-Shram registrations; job-scam data
- IT Rules 2021 traceability case (WhatsApp vs Government of India, Delhi HC) and the DPDP Rules status
- WhatsApp encryption facts: E2E default (2016), E2E backups (2021), multi-device keys, security codes; Signal protocol basics (WhatsApp's encryption white paper)
- Reuse drafts 207 (social), 211 (messaging and email), 310 (platform economics), 312 (trust) and the research notes

## Length
No page budget (owner, 26 Sep 2026). Length follows content, kept tight by cutting repetition.

## Numbering and build
- Figures 5.n
- Build copied from `src/M4/build.py`, with `m5_figs.py` helpers plus `figs_teardowns.py` and `figs_tech.py`
- Long figure code written with the Write tool
