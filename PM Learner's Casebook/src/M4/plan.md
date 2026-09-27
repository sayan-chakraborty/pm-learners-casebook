# M4 Mobility, maps & travel: session plan (25 Sep 2026, awaiting owner's "go")

## Cold open (top of the primer page)
Bengaluru, Friday 6:40 pm, heavy rain on Outer Ring Road. Ananya's cab app shows "finding your driver" for the fourth time; two drivers accepted and cancelled. The fare says 1.8× surge. Try it: "Drivers keep cancelling tonight. Is this a pricing problem, a matching problem or a driver problem, and how would you tell?"

## Outline
1. **Sector primer (~4–5 pp)**
   - The value chain: rider, platform, driver, vehicle owner or fleet, payments, maps; who pays whom
   - Commission vs subscription: Uber/Ola ~20–25% take vs Rapido and Namma Yatri's flat daily fee; Uber's move to subscriptions for autos (2025)
   - Unit economics, worked in ₹: one ₹300 cab ride from the driver's side (fuel/CNG, EMI, commission, earnings per hour) and the platform's side
   - Metrics: completed trips, ETA to pickup, acceptance and cancellation rates, driver utilisation, earnings per online hour, surge multiplier, trips per rider per month
   - Players and numbers: Uber India, Ola, Rapido, Namma Yatri, inDrive, BluSmart (collapse), Google Maps and Mappls, MakeMyTrip, ixigo, EaseMyTrip, IRCTC
   - Turning points: the Ola–Uber discount war (2015–17); zero-commission subscription models (2023–25); BluSmart's collapse and the 2025 aggregator guidelines (surge caps, driver share); state bike-taxi rules
   - Non-obvious mechanics: why drivers cancel (destination, cash vs UPI, short trips), surge as a supply signal, multi-apping, the airport and railway-station queue, maps as the hidden cost of every trip
   - Questions interviewers love
2. **Cases (4)**
   - 4.1 Ola for schoolkids (Design · A250–251)
   - 4.2 Improve Google Maps (Improvement · B114–115; B114 has a picture, which will be redrawn and labelled "redrawn from the original")
   - 4.3 Spike in Uber ride cancellations (RCA · A306)
   - 4.4 MakeMyTrip enters Dubai (GTM · B151–152)
   - **Dropped:**
     - Uber for kids (B39–40): the same design problem as 4.1, in the US
     - Improve Uber (B96): easy; HEART moves to 4.2
     - Google Maps ETA errors (B65): "a recent release broke it" repeats M1's Android DAU pattern
3. **Guesstimates (2)**
   - G4.1 Uber drivers in Bengaluru (B138): supply side, from peak-hour demand
   - G4.2 Bikes for a new bike-taxi firm (B140): demand forecast turned into fleet size
   - Short guesstimate-kit reminder only (the full kit is in M3). Each gets:
     - a kit-check line
     - a stronger answer following the six cards
     - an equation tree
     - a sanity check against a real figure
     - the reusable trick
4. **Teardowns (5):** Uber · Ola · Rapido (with Namma Yatri as the comparison) · Google Maps · MakeMyTrip. Then a comparison table and a positioning 2×2 (how drivers are paid, commission vs subscription, against how wide the service is).
5. **Technology (~8 pp)**
   - Cloud computing (IIM A p. 96): IaaS/PaaS/SaaS, serverless, pricing models (on-demand, reserved, spot)
   - System design III, detailed. Walkthrough: 6 pm Friday rain in Bengaluru and New Year's Eve at 10× normal load. Topics:
     - vertical vs horizontal scaling and autoscaling
     - load balancing
     - consistency vs availability (CAP) applied per feature
     - SLIs, SLOs and error budgets
     - graceful degradation
     - retries, timeouts and circuit breakers
     - microservices vs monolith
6. **Connect the dots (~1 p)**, with a sketch answer to the cold open

## Frameworks (new only; nothing already taught is repeated)
- **4.1:** MVP and build–measure–learn, plus the riskiest-assumption test (what to learn first and the smallest way to learn it)
- **4.2:**
  - Opportunity Solution Tree (Teresa Torres)
  - HEART metrics (Google): happiness, engagement, adoption, retention, task success
- **4.3:** Supply–demand balance and dynamic pricing (surge): why a price rise can shorten waits, and when it backfires
- **4.4:**
  - TAM/SAM/SOM
  - Porter's five forces
  - a Check box on why SWOT is weak
- **Dropped as gas:** Ansoff's matrix. It only names the move ("market development") and changes no decision.
- Every framework box follows the owner's rule from 25 Sep 2026: the five steps, "Using it, step by step", "Common slip", and the figure after the step list
- Every stronger answer carries:
  - a "Why this move" note on each turn
  - maths written out as a chain
  - a "How the answer hangs together" box

## Diagrams (~45; one line each)
- **Primer**
  - Money flow on one ride: rider, platform, driver, fleet owner
  - Commission vs subscription: the driver's monthly earnings side by side
  - Driver's ₹300 ride waterfall: fuel, EMI, commission, what's left per hour
  - Platform's side of the same ride
  - Players chart
  - Turning-points timeline
  - Why drivers cancel: the reasons, sized (illustrative)
- **Case 4.1:** move strip; riskiest-assumption ladder (parent trust → safety → route density → price); build–measure–learn loop with the school-run MVP
- **Case 4.2:**
  - move strip
  - B114 journey redraw
  - Opportunity Solution Tree for Maps engagement
  - HEART grid filled for one feature
- **Case 4.3:** move strip; supply–demand curves with and without surge; driver-cancellation issue split (rider side, driver side, pricing, matching)
- **Case 4.4:** move strip; TAM → SAM → SOM nested bars with ₹ numbers; five-forces diagram for Dubai online travel
- **Guesstimates:** two equation trees; a peak-hour demand curve for the Bengaluru fleet
- **Teardowns (×5)**
  - Behind-the-screens sequence flows: Uber ride with surge; Ola ride; Rapido bike ride on subscription; a Maps route with live traffic; MakeMyTrip flight + hotel booking with inventory from a GDS (global distribution system)
  - Loops and money waterfalls; comparison 2×2
- **Technology**
  - IaaS/PaaS/SaaS "pizza" analogy stack
  - On-demand vs reserved vs spot cost chart
  - Vertical vs horizontal scaling
  - Autoscaling with a traffic curve and the lag behind it
  - Load balancer spreading traffic
  - CAP choices per feature (driver assignment vs ETA display)
  - SLO and error-budget burn-down
  - Graceful degradation ladder
  - Retry storm and circuit breaker
  - Monolith vs microservices

## Light maths planned
- Commission vs subscription break-even (trips a day at which a ₹29 daily pass beats a 20% commission)
- Surge: the price that clears demand
- Driver earnings per online hour vs per trip hour (utilisation)
- TAM/SAM/SOM in ₹ Cr
- Autoscaling: servers = peak requests per second ÷ requests per server, plus headroom
- Error budget: 99.9% a month ≈ 43 minutes; how one bad release spends it
- Spot vs on-demand saving

## Research (one light batch)
- Uber India and Ola FY25/FY26 results
- Rapido FY25 and its valuation; Namma Yatri scale
- The 2025 Motor Vehicle Aggregator Guidelines (surge cap, driver share)
- BluSmart's collapse (2025)
- Karnataka's bike-taxi rules
- MakeMyTrip FY26 results (Nasdaq filing)
- ixigo/EaseMyTrip headline numbers
- Google Maps users; Mappls
- Dubai visitor numbers (DET, 2025), for 4.4's numbers
- Cloud pricing examples (spot discount)
- Reuse draft 205 (ride-hailing), 305 (cloud) and 303 (system design), and the research notes

## Numbering and build
- Figures 4.n; build copied from src/M3/build.py (with `post_case`, the duplicate-key check, and the tools/ scripts as patterns).
