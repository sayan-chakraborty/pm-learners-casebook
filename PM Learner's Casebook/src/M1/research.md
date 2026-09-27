# M1 research log  (fact | number | date | source)

S0 facts reused (UPI Aug 2026 volume/value/share, MDR from 15 Oct 2026, PhonePe FY26, timeouts): see src/S0/research.md.

## Primer
UPI app share Aug 2026 | PhonePe 45.9%, Google Pay 32.4%, Paytm 8.1%, Navi 4.4%, super.money 1.7% | Aug 2026 | NPCI via Inc42 (inc42.com/buzz/upi-in-august-navis-market-share-climbs-to-4-4-phonepe-google-pay-slip/)
Credit cards outstanding | 12.29 crore (122.86 mn) Jul 2026; 12.16 crore Jun 2026; spends ₹2.01 lakh Cr in Jun 2026 | Jul 2026 | RBI data via Business Standard, 25 Aug 2026
Debit cards outstanding | ~100.5 crore | Jun 2025 | RBI data via Business Standard, Oct 2025
Card MDR split (typical, illustrative) | ~2% credit-card MDR; issuer interchange ~60–80% of fee pool; network ~5–15%; acquirer/aggregator ~10–25% | 2025 | GTM360 credit-card primer (2023); Terra Insight merchant-fees note — industry estimates, not regulated numbers
Contactless card limit without PIN | ₹5,000 per transaction | from 1 Jan 2021 | RBI via Moneylife/Enterslice
Card controls (on/off for online, contactless, international; set limits) | mandated for all cards | RBI circular 15 Jan 2020 | RBI via Business Standard
RuPay credit card on UPI | allowed since 2022 (only RuPay); UPI credit-card txns ~28–38% of card txns (estimate) | 2025–26 | coinlaw.io, TechCrunch Jan 2025 — estimate, labelled
Jan Dhan accounts | 59.04 crore accounts, ₹3.15 lakh Cr deposits | 12 Aug 2026 | PMJDY data via UNI / edunovations
Business correspondents | 17.36 lakh BCs; 1.81 lakh branches; 1.65 lakh IPPB centres; 99.92% of villages have a banking outlet within 5 km | 17 Jul 2026 | Govt reply via Policy Edge / The Hawk
Rural internet | 958 mn active internet users; rural 57% (~548 mn); 18% go online on someone else's phone, ~80% of them rural | 2025 (released Jan 2026) | IAMAI–Kantar Internet in India 2025 press release
UPI 123Pay | feature-phone UPI via IVR, missed call, app, sound; per-txn limit ₹10,000 (from ₹5,000) | RBI Dec 2024; compliance by 1 Jan 2025 | Business Standard 22 Nov 2024
UPI technical declines | ~8–10% in 2016 → roughly 0.3–0.8% by 2025; NPCI target < 0.25% | 2025 | D91 Labs, Paytm blog (NPCI data) — secondary, labelled approximate
UPI Circle | full delegation up to ₹15,000/month, ₹5,000/txn; partial = primary approves each; up to 5 secondary users | launched Aug 2024 | NPCI product page; Razorpay/Paytm explainers
Minors' accounts | minors 10+ may open and operate savings/term deposit accounts independently, limits set by bank; comply by 1 Jul 2025 | RBI circular 21 Apr 2025 | Business Standard 21 Apr 2025
PPI credit-line ban | PPIs may not be loaded from credit lines; hit Slice, Uni, LazyPay, teen cards | RBI 20 Jun 2022 | Inc42 / Business Standard Jun 2022
Minors cannot contract | agreement with a minor is void | Indian Contract Act 1872 s.11; Mohori Bibee v Dharmodas Ghose (1903) | general legal knowledge
RBI Digital Lending Directions 2025 | DLG capped at 5% of the portfolio disbursed; loans disbursed straight into the borrower's bank account; KFS; LSP rules | 8 May 2025 (RBI/2025-26/36) | ELP, Argus Partners summaries
Digital lending app economics (sourcing fee 2–3%, loss rates) | ILLUSTRATIVE only | — | author's worked example; no single public source
Paytm Payments Bank | licence cancelled, effective close of business 24 Apr 2026 | 24 Apr 2026 | RBI press release; Finextra
PhonePe IPO | SEBI observation 20 Jan 2026; UDRHP-I 21 Jan 2026; pure OFS ~₹12,000 Cr; paused Mar 2026; no date | Sep 2026 | Business Today 20 Jan 2026; TechCrunch Mar 2026
PhonePe Pincode | wound down | 5 Dec 2025 | TechCrunch
India age structure | 15–64 = 68.4%; under 15 = 24.2%; median age ~29.8 | 2025 | UNFPA / UN WPP 2024; the 15–39 share (~42%) is the author's estimate from WPP age bands

## Fraud (Case 1.4)
UPI frauds | FY24 13.42 lakh cases, ₹1,087 Cr; FY25 12.64 lakh, ₹981 Cr; FY26 (to Nov) 10.64 lakh, ₹805 Cr | Parliament answers Dec 2025 | YourStory Dec 2025; The420
Card + internet banking frauds | FY25: credit card 66,106 (₹336 Cr), internet banking 59,337 (₹413 Cr), debit/ATM 18,882 (₹68 Cr); total 1.45 lakh, ₹822 Cr | Lok Sabha USQ 2432, 3 Aug 2026 | taxguru.in
All bank frauds (RBI AR) | FY26 10,114 cases, ₹48,021 Cr (advances 85.5% by value) | RBI Annual Report 2025-26, 29 May 2026 | Business Standard
RBI discussion paper | "Exploring safeguards in digital payments to curb frauds": 1-hour delay for some authorised push payments, kill switch, account-level on/off controls, ₹25 lakh annual credit ceiling for unverified accounts | 9 Apr 2026 (comments to 8 May 2026) | Medianama 2026-04; RBI DP
Google Pay safety | ₹13,000 Cr fraud prevented "last year"; 4.1 crore scam warnings since Oct 2024; screen-share alerts on Android 11+ | 17 Dec 2025 | Google India blog

## Teardowns
PhonePe | see S0 log; merchant lending platform; SmartPOD (soundbox + card POS) | 2025–26 | phonepe.com press/product pages
Google Pay India entity | revenue ₹1,547 Cr FY25 (₹1,490 Cr FY24), profit ₹50 Cr (₹110 Cr) | FY25, reported 12 Feb 2026 | Storyboard18
Google Pay Flex | RuPay co-branded credit card with Axis Bank, rewards in "Stars" (1 Star = ₹1); Pocket Money on UPI Circle up to ₹15,000/month | 17 Dec 2025 | Google India blog; TechCrunch
Google Pay loans | personal loans via DMI Finance ₹30,000–₹9 lakh, 6–48 months, APR 12–27.9% | 2025–26 | paisasetu / Google Pay help (secondary)
Google Pay card convenience fee | 0.5–1% + GST on bill payments by card; free via UPI from bank | 2025 | secondary (paisasetu)
Paytm FY26 | revenue ₹8,437 Cr (+22%), PAT ₹552 Cr (FY25 loss ₹663 Cr), EBITDA ₹502 Cr | FY26 (6 May 2026) | Paytm investor relations; Business Standard
Paytm Q4 FY26 | revenue ₹2,264 Cr, PAT ₹184 Cr; merchant GMV ₹6.5 lakh Cr (+27%); 1.51 crore subscription merchants; financial services revenue ₹750 Cr (+38%) | Q4 FY26 | same
Paytm Q1 FY27 | revenue ₹2,448 Cr (+28%), PAT ₹220 Cr (+79%), EBITDA ₹203 Cr | Jul 2026 | Meyka / Open magazine
Paytm Intelligence (Pi) | AI agents for banks, lenders, insurers (India, UAE) | 9 Sep 2026 | Bloomberg; Business Standard
WeChat | Weixin + WeChat MAU > 1.4 bn | 30 Sep 2025 | Tencent 2025 annual results
Tencent FinTech & Business Services | RMB 229.4 bn revenue, +8% | 2025 | Tencent 2025 annual results
Alipay vs WeChat Pay | Alipay ~54% of mobile payments; the two together > 90% | 2025 | industry estimates (coinlaw / research reports) — labelled estimate
Razorpay | FY25 revenue ₹3,783 Cr (+65%), net loss ₹1,209 Cr (ESOP + reverse-flip tax) | FY25 | Inc42 / PL India
Razorpay IPO | confidential DRHP 12 Jun 2026 | Jun 2026 | Bajaj Broking / Moneyflow
Razorpay scale | TPV ~$180 bn annualised; RazorpayX 50,000+ businesses | 2026 | company-cited via digitalinasia, VFS — treat as company claims
Razorpay pricing | flat 2% standard fee on domestic cards, net banking, wallets, and UPI (as a "platform fee", since UPI MDR is zero); international up to 3% | Sep 2026 | razorpay.com/pricing
Razorpay agentic | UPI Reserve Pay on NPCI's single-block-multi-debit; ChatGPT UPI pilot with NPCI and OpenAI; June 2026 launches on Claude, Codex | 2025–26 | Razorpay blog; Sprint 2026
Groww FY26 | revenue from ops ₹4,645 Cr (+19%), PAT ₹2,083 Cr (+14%) | FY26 (20 Apr 2026) | Groww results PDF; IIFL
Groww Q1 FY27 | revenue ₹1,501 Cr (+66%), PAT ₹735 Cr | Jul 2026 | Entrackr
NSE active clients | Groww 1.335 crore (29.04%) Aug 2026; Angel One 67.2 lakh (14.79%); Zerodha 14.96% in Jun 2026 (~68 lakh) | Aug 2026 | NSE data via EquityBulls / knowyourbrokerage
Zerodha FY26 | PAT ₹4,283 Cr (+1.2%), revenue ~₹8,500 Cr flat; brokerage income −11% to ₹2,738 Cr; exchange-rebate income to zero; MTF ~10% of revenue | FY26 (26 Aug 2026) | Entrackr; BW Businessworld
smallcase | FY25 revenue ₹106 Cr (+57%), EBITDA loss ₹9 Cr, net loss ₹34 Cr | FY25 | Entrackr
smallcase fee | ₹100 + GST per buy (capped at 1.5%), ₹10 per SIP instalment | 2026 | smallcase.com fees page

Groww listing | NSE/BSE listing 12 Nov 2025; IPO ₹6,632 Cr, 17.6× subscribed | Nov 2025 | Business Standard 12 Nov 2025; BusinessToday
SEBI F&O study | 93% of 1 crore+ individual F&O traders lost money FY22–FY24; avg loss ~₹2 lakh; aggregate > ₹1.8 lakh Cr | 23 Sep 2024 | SEBI press release
SEBI F&O curbs, true-to-label charges | larger contracts, fewer weekly expiries (late 2024); uniform exchange charges ended broker rebates (Oct 2024) | 2024 | SEBI circulars (general knowledge; confirmed via Zerodha FY26 rebate income = 0, BW Businessworld)
NPCI API limits | balance enquiry capped at 50 per app per customer per day (2025) | 2025 | NPCI guidelines via D91 Labs / c4scourses (secondary)

## Tech
Agile Manifesto | 17 authors, Snowbird, Utah, Feb 2001 | 2001 | agilemanifesto.org (general knowledge)
Scrum | roles, events per Scrum Guide 2020 (Schwaber, Sutherland) | 2020 | scrumguides.org (general knowledge)
IIM A tech curriculum | SDLC p.70, Waterfall p.71, Agile p.72, Scrum/Kanban p.73, comparison p.74; A/B testing p.54 | 2026-27 | Product Mindset PDF
Razorpay Orders API | POST /v1/orders, amount in paise, returns order id; webhooks such as payment.captured signed with X-Razorpay-Signature (HMAC-SHA256) | current | razorpay.com/docs (general knowledge of public docs)
Sample size rule of thumb | n ≈ 16·p(1−p)/δ² per group for 80% power, 5% significance (Lehr's rule) | — | van Belle, Statistical Rules of Thumb (general knowledge)

## Unverified / conflicting (not published as fact)
- Razorpay revenue ÷ volume (~0.25%) mixes FY25 revenue with a 2026 annualised TPV claim; labelled rough.
- Paytm merchant-loan terms (₹310/day × 180 days) and PhonePe/Google Pay flow timings are illustrative.
- Zerodha FY26 PAT: ₹4,283 Cr (Entrackr, BW) vs ₹4,238 Cr (Inc42). Used "about ₹4,300 Cr".
- research_notes_sep2026.md profit per client (₹53.6k Zerodha, ₹14.1k Groww) is off by 10×; recomputed: ~₹6,300 and ~₹1,560 (FY26 PAT ÷ mid-2026 active clients).
- smallcase user count: sources say 3 mn+ and 10 mn+; not used.
- Google Pay "530 mn users transacted" appears in secondary sources only; not used.
- App-level UPI success rates (PhonePe vs Google Pay) are not published; the candidate's claim is marked unverifiable.
- The "~30% UPI failure rate in rural India" claim (Case 1.1) has no source.
- Razorpay pricing page wording on GST (included vs extra) is ambiguous; GST not mentioned in the text.
