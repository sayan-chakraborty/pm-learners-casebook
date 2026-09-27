"""Rewrites the stronger-answer blocks of M3 case parts (owner instruction 25 Sep 2026:
more detail, every turn explained, a closing 'how it hangs together' note). Run once; idempotent."""
import pathlib
P = pathlib.Path(__file__).resolve().parent.parent / "parts"

def A(tag, body, why=None):
    ps = "".join(f"<p>{b}</p>" for b in body.split("\n\n"))
    h = f'<div class="turn a"><div class="who">A</div><div class="body"><div class="steptag">{tag}</div>{ps}</div></div>\n'
    if why: h += f'<p class="whynote">Why this move: {why}</p>\n'
    return h
def Q(body):
    return f'<div class="turn q"><div class="who">Q</div><div class="body"><p>{body}</p></div></div>\n'
def WHY(t):
    return f'<p class="whynote">Why this move: {t}</p>\n'
def HANG(t):
    return f'<div class="hang"><span class="l">How the answer hangs together</span>{t}</div>\n'

def splice(fname, start_pat, end_pat, new, nth=0):
    f = P / fname; t = f.read_text(encoding="utf-8")
    a = t.index(start_pat); b = t.index(end_pat, a)
    for _ in range(nth): b = t.index(end_pat, b + 1)
    # drop an older hang note that sits just before end_pat
    f.write_text(t[:a] + new + t[b:], encoding="utf-8")

# ---------------- Case 3.1 ----------------
s31 = '<div class="qa stronger">\n' + \
A("① Clarify", "“Engagement” can mean two things: people open Myntra on more days, or they stay longer each time. They lead to different ideas, so I’d ask which one matters. I’d also ask which users we care about, and what AI Myntra already has, such as visual search and MyFashionGPT, so I don’t propose something that exists. I’ll assume a mobile launch within six months.") + \
Q("More days a week. Focus on 18–30-year-olds. Assume visual search exists.") + \
WHY("“days a week” rules out ideas that only make each visit longer, such as a chat that keeps you typing. It also tells us what to measure at the end.") + \
A("② Size it", "Most people open a fashion app only when they need to buy something. Illustrative: of 100 monthly users, about 60 come only when buying, a few times a year. Short interviews would give three reasons they don’t come on other days: nothing new that suits me, I don’t know what goes with what, and I’m scared of ordering the wrong size.\n\nOnly the second reason can create a habit on days you are <i>not</i> buying, the way people check the weather every morning. The other two matter when you are already shopping.",
  "fixing the reason that creates a daily need moves “days a week”; fixing the others mostly moves sales.") + \
A("③ Does it need AI?", "Take each problem on its own. <b>Fear of size</b> doesn’t need a model: our returns data can say “runs small, most people chose one size up”, and that is a simple rule. <b>Styling</b> does: picking which bottoms and shoes go with a mustard kurta is a judgement nobody can write down as rules, we have millions of saved and bought outfits to learn from, and a bad suggestion costs the user only a swipe ({{REF:needai}}).",
  "it puts AI only where rules fail and mistakes are cheap, and ships the cheap fix for size straight away.") + \
A("④ Pick one, check four risks", "The idea: a daily “outfit of the day” built from what you own. Its four risks are in {{REF:risks}}. The biggest is <b>data</b>: most users own too few Myntra items to style, because they bought most of their clothes elsewhere. So the first version asks users to add photos of three favourite pieces.\n\nCost, illustrative: 10 lakh users a day × 3 outfits each × ₹0.20 of model cost per outfit = ₹6 lakh a day. ₹6 lakh × 365 days ≈ ₹22 Cr a year. The feature must bring in more than that in extra purchases.",
  "if the riskiest part fails, nothing else matters, so it is tested first and cheaply.") + \
A("⑤ MVP", "A morning card, not a chatbot: “Today: your blue jeans + this kurta + white sneakers”, with three buttons: Wear it, Swap, and Shop the missing piece. Launch it to 5% of users who own five or more Myntra items. Keep a similar group without it (a holdout) so we can see what the card really changes.",
  "a card needs no typing and costs one model call a day; a chat invites long, costly conversations. The holdout separates the card’s effect from everything else happening that month.") + \
A("⑥ Measure", "<b>Goal (North Star):</b> weekly users who save, wear or buy from a suggested outfit. <b>Inputs:</b> share of users with enough wardrobe items; outfits accepted per 100 shown. <b>Safety checks (guardrails):</b> return rate on items bought from suggestions; thumbs-down rate; model cost per active user. <b>Trade-off:</b> the card is cheap but narrow; chat is flexible but costly. <b>Next time:</b> open chat only to people who already use the card every week.",
  "the goal counts people who <i>act</i> on an outfit, so a confusing stylist can’t score well just by generating more chat.") + \
'</div>\n' + HANG("The goal (people acting on outfits each week) comes straight from the clarified meaning of engagement (more days a week). The biggest risk (too little wardrobe data) shaped the MVP (add three photos). The cost maths (₹22 Cr a year) set the bar the feature must clear. And the guardrail (returns on suggested items) stops an AI that sells clothes people send back.") + "\n"
splice("2_case31.html", '<div class="qa stronger">', '<div class="box fw">', s31)

# ---------------- Case 3.2 ----------------
s32 = '<div class="qa stronger">\n' + \
A("① Clarify", "Marketplace is mature, with about a billion monthly users, so this is about health, not launch. Two questions change the answer. What decision will these metrics drive: where to invest, or spotting problems early? And is the goal more time on Facebook, or Marketplace working as a place to buy and sell?") + \
Q("A monthly health review for the Marketplace team. Buying and selling that works; engagement follows.") + \
WHY("a monthly review needs a handful of numbers that point to action, not a list of eleven. And “buying and selling that works” tells us to measure deals, not clicks.") + \
A("② Map", "There are two sides, and each has one moment that decides whether they come back. For the seller: did my table sell, quickly, at a fair price? For the buyer: did I find a table near me, from someone I could trust? Every other metric is a cause of one of these two moments.",
  "naming the moment of truth for each side keeps the metrics tied to what users actually care about.") + \
A("③ Liquidity", "So the core question is whether listings find buyers. Illustrative, for 100 furniture listings in Pune in a week: 62 get a message within a day, 41 lead to an agreed meeting, and 30 are marked sold within 7 days ({{REF:liq}}). That 30% is the <b>sell-through rate</b>. I’d track it for each city and category, because a buyer in Pune can’t use a table in Patna.",
  "a marketplace is only as good as its chance of a match. Visits and messages are causes or side effects of that.") + \
A("④ Goal", "<b>Goal (North Star):</b> weekly successful local matches, meaning listings marked sold after a Marketplace conversation, or confirmed by the buyer’s rating. Payment happens off Facebook, so I pick signals we can actually see.",
  "one number that both sides’ success feeds into, and that Facebook can count.") + \
A("⑤ Inputs", "I’d split the levers by side so each team knows what to move. <b>Sellers:</b> new listings a week from active sellers; share of listings with a clear photo and a price close to similar items. <b>Buyers:</b> share of searches that show 10 or more nearby listings; share of searches that lead to a message. <b>Between them:</b> median time to first reply; share of first messages answered within an hour.",
  "when the goal drops, these tell you which side, and which step, to fix.") + \
A("⑥ Guardrails", "<b>Safety checks (guardrails):</b> scam reports per 1,000 conversations; share of listings removed for breaking rules; how often sellers block buyers. <b>Trade-off:</b> stricter checks on new sellers cut scams but also cut listings, which lowers liquidity. <b>Next time:</b> show “thin” cities separately from “thick” ones in every chart.",
  "scams and spam can inflate activity numbers, so the guardrails make sure growth is healthy growth.") + \
'</div>\n' + HANG("The decision (a monthly health review) told us to keep the list short. Mapping both sides gave two moments of truth, and liquidity joined them into one number: completed local matches. The inputs are split by side, so a drop points to a team. The guardrails stop scams from making the numbers look better than the marketplace really is.") + "\n"
splice("3_case32.html", '<div class="qa stronger">', '<div class="box fw">', s32)

# ---------------- Case 3.3 ----------------
s33 = '<div class="qa stronger">\n' + \
A("① Clarify", "I’d pin down three things. What exactly is the rate: returned units ÷ delivered units? From what level to what, over how long? And did anything change on our side: return rules, a new seller programme, a new delivery partner?") + \
Q("Units. Overall it went from 11% to about 15% over the festive quarter. No policy changes.") + \
WHY("“11% to 15% in a festive quarter, with no rule changes” already hints that the season, not a broken process, may be behind much of it.") + \
A("② Mix or rate?", "First I’d split the rise into two parts. Clothes are always returned more than other things, and in the wedding season we sell far more clothes. Illustrative: clothes went from 30% to 40% of orders. If every category kept its old return rate, that shift alone would add 2.1 of the 3.7 points. The rest comes from clothes’ own rate rising from 25% to 28% and electronics from 8% to 10% ({{REF:mix}}).",
  "more than half the “problem” is simply selling more clothes, which is good news. Only the smaller part is a real deterioration.") + \
A("③ Reason codes", "For the part that is a real rise inside clothes, I’d read the reason each customer chose when returning, and cut it by brand, seller, size, payment type, and new versus repeat buyers. I’d also count <b>bracketing</b>: one order with the same item in two sizes, like Pooja’s kurta. Illustrative split of clothing returns: size and fit 55%, “didn’t like it” 20%, damaged or wrong item 10%.",
  "the data ranks the causes in minutes; guessing them risks spending effort on a small one.") + \
A("④ Size it", "Each return loses about ₹250 (two trips, a check, a discounted resale). 3 extra points on, say, 1 crore clothing units a month = 3 lakh extra returns. 3 lakh × ₹250 = ₹7.5 Cr a month. Size and fit is 55% of that, about ₹4 Cr, so it gets most of the effort.",
  "rupees turn a list of causes into a priority order anyone in the room can agree on.") + \
A("⑤ Fix by root cause", "<b>Size and fit:</b> a fit hint on each product, built from its returns (“runs small: 60% chose one size up”), plus size advice based on what fitted the customer before. <b>Bracketing:</b> show that hint at the moment someone adds a second size. <b>Bad sellers:</b> sellers whose return rate is twice their category’s get flagged and drop in search results. <b>Wardrobing:</b> tamper tags only on high-value party and ethnic wear.",
  "each fix targets one measured cause, so we can tell later which one worked.") + \
A("⑥ Measure", "<b>Goal (North Star):</b> kept sales per visitor (NMV per visit), not the return rate on its own. <b>Safety checks (guardrails):</b> conversion rate; complaints about refused returns. <b>Trade-off:</b> anything that makes returns harder lowers the return rate but also lowers sales. <b>Next time:</b> report festive-season return rates with the category mix held fixed, so the season stops looking like a crisis.",
  "a return rate can be “improved” by scaring buyers away. Kept sales per visitor can only rise if customers buy and keep more.") + \
'</div>\n' + HANG("Clarifying the size of the rise (11% to 15%) made it worth splitting. The mix-or-rate split showed that only about a third is a real deterioration. Reason codes and rupees then ranked what is left, and the fixes follow those causes. The goal, kept sales per visitor, makes sure we cut returns without cutting sales.") + "\n"
splice("4_case33.html", '<div class="qa stronger">', '<div class="box fw">', s33)

# ---------------- Case 3.4 (keep the break-even figure between turns ④ and ⑤) ----------------
f = P / "5_case34.html"; t = f.read_text(encoding="utf-8")
fa = t.index('<figure style="margin:3pt 0 5pt">'); fb = t.index("</figure>", fa) + len("</figure>")
fig = t[fa:fb]
s34 = '<div class="qa stronger">\n' + \
A("① Clarify", "Why does the VP want a cut: are sign-ups slowing, is a competitor cheaper, or do we want members to shop more? Is the goal more members or more profit? And would the new price apply to everyone, or only to people who join from now on?") + \
Q("Sign-ups have slowed. The VP wants growth, but not at a loss. Assume the cut applies to everyone.") + \
WHY("“growth, but not at a loss” turns the question into a sum: does the cut bring in enough new money to cover what it gives away?") + \
A("② Floor", "Start with the least we could charge. Each new member costs about $20 a year in extra free shipping, plus a share of the video catalogue. $89.99 is far above that, so we won’t lose money on any single new member. Cost isn’t what decides this.",
  "checking the floor first rules out one worry quickly, so the rest of the answer can focus on the real risk.") + \
A("③ Ceiling", "Now the most members would pay. Existing members already pay $99.99 and stayed through two earlier price rises, so Prime is worth more than that to them. They don’t need a cut to stay. For them, the cut is simply money given away: $10 × 200 million members = $2 bn a year.",
  "it finds where the cost of the idea really sits: in the discount handed to people who would have paid anyway.") + \
A("④ Break-even", "How many new members pay back that $2 bn? Each new member brings the $90 fee, minus $20 of shipping, plus about $10 of margin on the extra shopping members do: $90 − $20 + $10 = $80 a year. $2 bn ÷ $80 = 25 million new members. On a base of 200 million, that is 12.5% growth ({{REF:be}}). So a 10% price cut must bring 12.5% more members: every 1% off the price must add 1.25% more members.",
  "it replaces a guess (“members grow 20%”) with a threshold (“we need 12.5%”) that a test can confirm or reject.") + \
fig + "\n" + \
A("⑤ Test", "Before any national change, show $89.99 to a random 5% of people who aren’t members, for six weeks, and compare sign-ups with everyone else. If sign-ups rise less than 12.5%, drop the idea. A cheaper test: a first-year price for new members only. It keeps most of the $2 bn, because existing members keep paying $99.99.",
  "six weeks of real behaviour is worth more than any assumption, and the new-member version limits the downside.") + \
A("⑥ Decide", "My recommendation: don’t cut the price for everyone; test a new-member price. <b>Goal (North Star):</b> Prime profit, from fees plus the extra shopping members do. <b>Safety checks (guardrails):</b> how many existing members cancel; how much new members shop (bargain joiners who never shop are a loss). <b>Trade-off:</b> a new-member deal can annoy loyal members who notice it.",
  "the decision follows the numbers: the only part of the idea that can pay is the new-member part, so that is the part to test.") + \
'</div>\n' + HANG("The floor showed each member is profitable at either price. The ceiling showed existing members don’t need the cut, so it costs $2 bn. Break-even turned that into a target (25 million new members, 12.5%), and the test checks the target cheaply. The recommendation keeps the upside (new members) and drops the costly part (discounting loyal ones).") + "\n"
a = t.index('<div class="qa stronger">'); b = t.index('<div class="box fw">', a)
f.write_text(t[:a] + s34 + t[b:], encoding="utf-8")

# ---------------- Guesstimate 3.1 ----------------
g1 = '<div class="qa stronger">\n' + \
A("1 · Unit", "I’ll count every query Google answers, typed, spoken or through Lens, worldwide, averaged over a typical day. Then I’ll say what the busiest hour looks like, because servers are built for the peak.",
  "“per second” can mean average or peak; saying which avoids a mismatch with what the interviewer had in mind.") + \
A("2 · Approach", "Top-down, from the demand side: the number of people who use Google, × searches each person makes a day, ÷ the seconds in a day.",
  "people and habits are easier to estimate than Google’s servers, and a published figure exists to check against.") + \
A("3–4 · Tree and numbers", "About 6 billion people are online (ITU, 2025). About 1.1 billion of them are in China, where Google is blocked: 6 − 1.1 = 4.9 billion. Google has about 90% of search: 4.9 × 90% ≈ 4.4 billion searchers. On average each searches about 3 times a day: heavy users do 10 or more, many do one or none. 4.4 billion × 3 = 13 billion searches a day. 13 billion ÷ 86,400 seconds ≈ <b>150,000 a second</b> ({{REF:gtree}}).",
  "three multiplications, each with a one-line reason, are easy for the interviewer to follow and to challenge.") + \
A("5 · Check", "Google said in 2025 that it handles more than 5 trillion searches a year. 5 trillion ÷ 365 ≈ 13.7 billion a day; ÷ 86,400 ≈ 158,000 a second. My 150,000 is within 5% of that.",
  "a second route to the answer turns a guess into an estimate you can defend.") + \
A("6 · Range", "The number I’m least sure of is searches per person. At 2 a day the answer is about 100,000 a second; at 5 a day, about 250,000. At the busiest hour traffic runs roughly 1.5–2× the average, so Google must be built for about 250,000–300,000 a second. AI chat tools push the per-person number down; AI Overviews and Lens push it up.",
  "a range with its main driver shows judgement, and tells the listener what to watch.") + \
'</div>\n' + HANG("The unit (average, all query types, worldwide) set up a simple demand-side tree. Each number has a reason, the check against Google’s own figure confirms the scale, and the range names the one input that moves it.") + "\n"
splice("6b_g31.html", '<div class="qa stronger">', '<figure>', g1)

# ---------------- Guesstimate 3.2 ----------------
g2 = '<div class="qa stronger">\n' + \
A("1–2 · Unit and approach", "Stores for one leading player, covering the dense 250 sq km of the city, with order-to-door in 10 minutes. Two things limit a store: how far its riders can reach in time, and how many orders its pickers can pack in the busiest hour. I’ll work out both and take the larger number.",
  "a store count must satisfy every limit at once, so the answer is the tighter of the two.") + \
A("3–4 · Reach, at the peak", "Picking and packing take about 3 minutes, which leaves 7 minutes to ride. In evening traffic a scooter averages about 15 km/h: 7 minutes × 15 km/h ≈ 1.75 km of road. Roads bend, so the straight-line reach is about 1.75 ÷ 1.3 ≈ 1.35 km. Each store’s circle is π × 1.35² ≈ 5.7 sq km, but circles must overlap to leave no gaps, so each store really covers about 83% of that: ≈ 4.7 sq km. 250 ÷ 4.7 ≈ <b>53 stores</b> ({{REF:hex}}).",
  "the slowest traffic and the most orders arrive in the same hour, so reach must be tested at the peak, not at noon.") + \
A("3–4 · Capacity", "At the peak, 8 pickers × 15 orders an hour = 120 orders an hour per store. The busiest hour carries about 15% of the day, so a store handles about 120 ÷ 0.15 = 800 orders a day. Demand: 23 lakh households × 17% who order × 0.3 orders a day × 35% share ≈ 42,000 orders a day. 42,000 ÷ 800 ≈ <b>53 stores</b>.",
  "the peak hour, not the whole day, is what a fixed team of pickers can handle.") + \
A("5 · Check", "Mapped data from mid-2025 shows Blinkit with 44 stores in Ahmedabad and all players with about 122. So the leader runs about 36% of the city’s stores, close to my 35% share. My 53–65 for a player at full maturity sits sensibly above today’s 44.",
  "a real count confirms the scale and catches any assumption that is badly off.") + \
A("6 · Range", "I’d plan about 65 stores, so each store runs at about 80% of its peak capacity rather than 99%. The range is 45–70, and orders per household is the number that swings it most. I’d open about 30 for coverage first, then add stores in the busiest neighbourhoods as orders grow.",
  "headroom absorbs rainy evenings and festivals; phasing avoids paying for half-empty stores up front.") + \
'</div>\n' + HANG("Both limits were worked out at the same moment, the evening peak, and both land near 53. The real count (Blinkit’s 44) confirms the scale, headroom lifts the plan to about 65, and the range names the one input to watch.") + "\n"
splice("6c_g32.html", '<div class="qa stronger">', '<figure>', g2)
print("stronger answers rewritten")
