"""Adds a 'Using it, step by step' list and a 'common slip' line inside step 3 of each M3 framework box
(owner instruction 25 Sep 2026). Inserted just before that box's step 4. Idempotent."""
import pathlib
P = pathlib.Path(__file__).resolve().parent.parent / "parts"
MARK = '<p><span class="step">4 · When it misleads.</span>'

def block(steps, slip):
    li = "".join(f"<li>{s}</li>" for s in steps)
    return (f'<p style="margin-bottom:1pt"><b>Using it, step by step</b> (on this case):</p><ol class="usesteps">{li}</ol>'
            f'<p class="slip"><b>Common slip</b> · {slip}</p>\n')

ADD = {
 ("2_case31.html", 0): block([
   "List the user problems separately: fear of the wrong size, not knowing what goes together, nothing new that suits me.",
   "For each one, try to write the logic as a single rule. “Tell people when a kurta runs small” fits in one sentence, so ship the rule.",
   "Where no rule fits (styling), check you have past examples with known right answers: outfits people saved, bought and kept.",
   "Ask what a wrong answer costs the user. A bad outfit costs a swipe, so AI can decide alone; blocking a seller costs a livelihood, so a person checks.",
   "Test the model against the simple version on a small group. Keep it only if it wins by more than its running cost."],
   "judging the whole idea (“an AI stylist”) instead of each problem inside it. Most ideas contain one part that needs AI and two that don’t."),
 ("2_case31.html", 1): block([
   "Write the idea in one line: a daily outfit card built from what the user owns.",
   "For each of the four risks, write the one thing that would kill it. Value: nobody opens it. Usability: people don’t get the buttons. Feasibility: too few wardrobe items. Viability: model cost beats extra sales.",
   "Mark the riskiest: the one you know least about <i>and</i> that would hurt most. Here, wardrobe data.",
   "Design the cheapest test for that one: run the model on 1,000 real wardrobes and have stylists rate the outfits.",
   "Only when that passes, move to the next risk, and only then design the screens."],
   "testing usability first because designing screens is the fun part, while the real unknown is whether the data or the demand exists."),
 ("3_case32.html", 0): block([
   "Name each side and what success means for it: a seller’s table sells; a buyer finds a table nearby.",
   "Pick one event you can see that proves a match happened: a listing marked sold after a Marketplace chat.",
   "Build the funnel from listing to match (100 → 62 → 41 → 30) and find the biggest leak.",
   "Cut the same funnel by city and category to find “thin” markets where few matches happen.",
   "Invest in the harder side (usually listings) in the thinnest markets first."],
   "counting activity (visits, messages) as if it were matches. A busy market where nothing sells is a failing market."),
 ("4_case33.html", 0): block([
   "Pick the groups (categories) and write down each group’s share of orders and return rate, before and after.",
   "Mix effect: for each group, change in share × <i>old</i> rate. Add them up (+2.5 − 0.4 = +2.1).",
   "Rate effect: for each group, <i>old</i> share × change in rate. Add them up (+0.9 + 0.4 = +1.3).",
   "The small remainder is both moving at once (+0.3). Check the three parts add to the total change (3.7).",
   "Explain the mix part as a business change (more clothes sold); investigate only the rate part."],
   "mixing old and new numbers inconsistently, which double counts. Always use old rates for the mix effect and old shares for the rate effect."),
 ("5_case34.html", 0): block([
   "Floor: work out what one customer costs to serve (free deliveries, content). Never price below it.",
   "Anchor: find the price of the nearest alternative the customer would compare with (a streaming plan alone).",
   "Ceiling: estimate the value to a <i>typical</i> customer, counting only the benefits they actually use.",
   "Set the price between anchor and ceiling: nearer the ceiling if you are clearly better, nearer the anchor if you want share.",
   "For a change: revenue lost on existing customers ÷ profit per new customer = new customers needed. Then test whether you can get them."],
   "adding up every benefit as if each customer uses all of them. That inflates the ceiling and makes almost any price look cheap."),
}

for (fname, nth), html in ADD.items():
    f = P / fname; t = f.read_text(encoding="utf-8")
    if "Using it, step by step" in t and t.count("Using it, step by step") > nth: continue
    i = -1
    for _ in range(nth + 1): i = t.index(MARK, i + 1)
    t = t[:i] + html + t[i:]
    f.write_text(t, encoding="utf-8")
print("use-steps added")
