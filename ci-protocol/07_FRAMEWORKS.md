# 07 — FRAMEWORKS & EXPERT REFERENCES
**The actual analytical tools the personas draw on. Applied form, not textbook.**

Read this alongside 04_PERSONA_DIALOGUE.md. Each persona section below maps to one persona in the dialogue and tells it what to actually DO when it challenges the analysis.

---

## PERSONA 1: SKEPTICAL INVESTOR

### Framework A: VC Due Diligence Question Set

This is what investors actually check when evaluating a consumer brand. Not everything applies at every stage — but the Skeptical Investor persona should be scanning for gaps in ANY of these.

**Market Questions:**
- Is the category growing? At what rate? (If shrinking or flat, the thesis weakens regardless of product quality)
- What's the realistic addressable market after filtering for ICP? (TAM numbers are meaningless without ICP-adjusted SAM)
- Is this a "vitamin" or a "painkiller"? (Vitamins are nice-to-have; painkillers solve a problem people are actively trying to solve. Investors fund painkillers.)

**Competitor Questions:**
- Who is the strongest incumbent, and why have they won so far? (If you can't explain why the leader leads, you can't explain why you'll beat them)
- Is anyone else trying to do exactly what we're doing? If not, why not? (An empty space is either an opportunity or a trap — the investor needs to know which)
- What would it take for the current leader to copy our approach? How long? (Defensibility window)

**Unit Economics Questions:**
- What's the LTV:CAC ratio at steady state? (Target: 3:1 minimum for DTC; below 2:1 is burning money)
- What's the payback period? (How many months of a customer's spend before we recoup acquisition cost)
- What's the margin stack? (Revenue → COGS → Gross Margin → Fulfillment → Marketing → Net. Every layer must be defensible)
- What does the margin look like at $1M, $10M, $100M revenue? (Margin compression is real — see LMNT benchmark: 56.7% GM at $206M vs. 65-75% category benchmark)

**Falsifiability Questions (the investor's core move):**
- "What would have to be true for this to fail?" (Every thesis has a kill condition. Name it explicitly.)
- "What's the single biggest assumption in this analysis, and how would we know if it's wrong?"
- "If this estimate is off by 2x in the wrong direction, does the business still work?"

**In this category, that means:**
- The Skeptical Investor should always ask: does the unit economics math actually close at the price point IonWave is targeting? At $1.57/serving vs. LMNT's $1.35 subscription price, the margin stack must justify the premium. If CAC is $35+ and retention drops below 50% at month 3, the LTV:CAC ratio collapses.
- When reviewing a competitor's revenue estimate, the investor asks: "What's the weakest input in this triangulation, and what happens to the conclusion if that input is wrong by 2x?"

---

### Framework B: Unit Economics Validation

The investor's primary quantitative lens. Apply this to ANY financial estimate in the analysis.

**Margin Stack (top to bottom):**
```
Revenue per serving:          $X.XX
- COGS (ingredients + packaging):  -$X.XX  → Gross Margin %
- Fulfillment (pick/pack/ship):    -$X.XX  → Fulfillment Margin %
- Marketing (CAC amortized):       -$X.XX  → Contribution Margin %
- G&A (allocated overhead):        -$X.XX  → Net Margin %
```

**Validation checks:**
- Gross margin should be 60%+ for supplements to have room for marketing spend
- Fulfillment cost typically $4-7 for a supplement box shipped DTC
- If marketing is >40% of revenue, the brand is acquisition-dependent (fragile)
- Net margin <10% at scale means the business requires constant capital infusion

**LTV:CAC calculation:**
```
CAC = Total marketing spend ÷ new customers acquired in period
LTV = AOV × purchase frequency × retention curve integral
      (simplified: AOV × avg purchases before churn)
LTV:CAC = LTV ÷ CAC  →  target 3:1+
```

**Payback period:**
```
Payback = CAC ÷ (contribution margin per order)
          Target: < 6 months for DTC supplement
```

**When to flag:** If any competitor's numbers imply a payback period > 12 months or LTV:CAC < 2:1, that's either a growth-stage burn strategy (acceptable if funded) or a structural problem (flag as intelligence gap).

---

## PERSONA 2: CUSTOMER ANTHROPOLOGIST

### Framework A: Jobs-to-Be-Done (Christensen)

The core insight: customers don't buy products. They hire products to do a job. Understanding the job — not the product — is what predicts switching behavior.

**The three layers of a job:**
1. **Functional job:** The practical task. ("I need to stay hydrated during long workouts without feeling bloated or crashing.")
2. **Emotional job:** How they want to feel. ("I want to feel like I'm optimizing my performance, not just surviving.")
3. **Social job:** How they want to be perceived. ("I want to signal that I take my health seriously — I'm not a Gatorade person.")

**How to apply it when reading customer reviews:**
- Don't just collect what customers SAY about the product. Collect what they say about WHY they bought it, what problem it solved, and what made them switch TO or FROM it.
- A review that says "tastes great" is surface-level. A review that says "I used to get afternoon crashes during fasting and this fixed it" reveals the functional job.
- A review that says "I bought this because my CrossFit coach recommended it" reveals the social job.

**In this category, that means:**
- The electrolyte market has at least 4 distinct jobs customers are hiring products for:
  1. **Fasting support** — "don't crash during intermittent fasting" (functional + emotional)
  2. **Workout recovery** — "bounce back faster after training" (functional)
  3. **Hangover recovery** — "feel human the morning after" (functional + emotional)
  4. **Health identity** — "I'm the kind of person who optimizes" (social + emotional)
- LMNT dominates jobs 1 and 2. The Customer Anthropologist should flag if customer voice evidence shows a job that LMNT is NOT serving well — that's where IonWave's opening lives.

---

### Framework B: Pain/Gain/Switch Map

Three questions that structure how to organize customer voice evidence:

**PAIN: What problem does the customer have BEFORE they find this product?**
- This is the "before" state. What were they doing instead? What was wrong with it?
- Example: "I was getting leg cramps at night during keto" → pain = electrolyte imbalance during low-carb eating

**GAIN: What positive outcome does the customer experience AFTER using the product?**
- This is the "after" state. What changed?
- Example: "Cramps stopped within a week" → gain = functional electrolyte replenishment

**SWITCH: What triggered them to change FROM one product/solution TO this one?**
- This is the decision moment. What tipped the scale?
- Example: "I tried Liquid IV first but it had sugar and I'm keto" → switch trigger = ingredient compatibility with dietary restriction

**Why this matters for competitive intelligence:**
- Pain analysis tells you what problem the market has (opportunity sizing)
- Gain analysis tells you what the incumbent is delivering (the bar to clear)
- Switch analysis tells you what makes customers actually change behavior (the lever to pull)

**Organizing quotes:**
When collecting customer voice, tag each quote with which layer it belongs to. A quote can hit multiple layers. The goal is to have evidence across all three for each major theme — if you have lots of Pain quotes but no Switch quotes, you have a gap.

---

### Framework C: Saturation Methodology (Why It Works)

The stopping rule in 04_PERSONA_DIALOGUE.md says "stop when 5 consecutive quotes don't add a new theme." Here's why that works and how to apply it:

**Principle:** Customer populations are not infinitely diverse. For any given product in a given category, there are typically 4-8 dominant themes in how customers talk about it. Once you've captured all the themes, additional quotes just restate what you already know.

**Application:**
- Start collecting quotes with no theme labels. Let the themes emerge from the data.
- After ~10 quotes, you'll see 3-4 themes forming. Label them.
- Keep collecting. Each new quote either: (a) reinforces an existing theme, or (b) reveals a new one.
- When you've gone 5 quotes in a row with only (a) outcomes, you've likely hit saturation.
- **Exception:** If you've only sampled ONE platform (e.g., only Amazon), you haven't hit real saturation — different platforms attract different customer segments. Saturation requires diversity of source, not just volume.

**Minimum for saturation claim:**
- 3+ source types (e.g., Amazon + Reddit + review site)
- 4+ themes identified
- 5 consecutive quotes adding no new theme

---

## PERSONA 3: COMPETITIVE STRATEGIST

### Framework A: Porter's Five Forces (Applied)

Not the textbook version. The version that actually produces useful competitive intelligence for a DTC supplement brand.

**Force 1: Threat of New Entrants**
*Question: How easy is it for someone new to enter this market and compete?*

What to look for in DTC supplements specifically:
- **Capital threshold:** What's the minimum ad spend to get meaningful customer acquisition? (In supplements, roughly $50K-100K/month to test; $500K+ to scale. This is the real barrier — not the product itself.)
- **Supplier access:** Can a new entrant get the same ingredients? (For synthetic electrolytes: yes, commodity. For marine plasma: more concentrated supplier base = higher barrier.)
- **Distribution:** DTC via Shopify = low barrier to distribution. The hard part is customer acquisition, not selling.
- **Brand/trust:** Health supplements require trust. First purchase is high-friction. Established brands have a trust advantage that takes 12-24 months to build.
- **Regulatory:** FDA supplement regulations are relatively light. Not a meaningful barrier.

**Verdict format:** Rate as LOW / MODERATE / HIGH. State which factor(s) dominate.

---

**Force 2: Bargaining Power of Buyers (Customers)**
*Question: How much power do customers have to demand better terms or switch?*

What to look for:
- **Switching costs:** Near zero in supplements. Customer can try a different brand next order with no penalty.
- **Price sensitivity:** If price is mentioned in >30% of reviews as a con, buyer power is HIGH.
- **Information availability:** Reviews, comparison articles, Reddit threads = customers are informed. HIGH information = HIGH buyer power.
- **Alternative availability:** How many substitutes exist? More substitutes = more buyer power.

**In this category:** Buyer power is consistently HIGH. Switching costs are zero, information is abundant, and substitutes are plentiful. This means: any brand that stops delivering value loses customers immediately. Retention is earned every single order.

---

**Force 3: Bargaining Power of Suppliers**
*Question: How much power do ingredient/material suppliers have over us?*

What to look for:
- **Number of suppliers:** If 10+ suppliers exist for the key ingredient, supplier power is LOW.
- **Switching costs:** Can we change suppliers without reformulating? (For commoditized minerals: yes. For proprietary or rare ingredients: no.)
- **Forward integration threat:** Could a supplier go direct-to-consumer and cut us out? (Rare in supplements — suppliers sell to many brands.)
- **Ingredient concentration:** The rarer the key ingredient, the more supplier power.

**In this category:** For synthetic electrolytes (Na, K, Mg), supplier power is LOW — these are commodity chemicals. For marine plasma specifically, supplier power is MODERATE — fewer suppliers, more specialized sourcing. This is a strategic risk IonWave should monitor.

---

**Force 4: Threat of Substitutes**
*Question: Can customers solve the same problem with a fundamentally different type of product?*

What to look for:
- **Functional equivalents:** Products that do the same job but aren't in the same category. (Food sources of electrolytes, IV drips, other supplement formats.)
- **Customer willingness to substitute:** Are customers actually using alternatives? (Check reviews for "I just eat a banana" or "I make my own with salt and lemon.")
- **Price differential:** If substitutes are dramatically cheaper, price-sensitive customers will migrate.

**In this category:** Substitutes are real and mentioned frequently. "Just eat a banana," homemade salt water, food-based electrolyte sources. The Competitive Strategist should flag any evidence that a significant customer segment is moving toward substitutes — that compresses the addressable market.

---

**Force 5: Rivalry Among Existing Competitors**
*Question: How intensely are current competitors fighting each other?*

What to look for:
- **Number of direct competitors:** More competitors = more rivalry = thinner margins.
- **Product differentiation:** If products are commoditized (hard to tell apart), rivalry intensifies into price competition.
- **Market growth rate:** Fast-growing markets have room for multiple winners. Slow-growth markets force zero-sum competition.
- **Ad spend escalation:** If competitors are increasing ad spend quarter-over-quarter, they're in an acquisition arms race. This drives up CAC for everyone.

**Verdict format:** Rate rivalry intensity as LOW / MODERATE / HIGH. Note whether the category is expanding (room for new entrants) or consolidating (incumbents locking out competitors).

---

### Framework B: Competitive Response Scenario

*Question: If we succeed, how will incumbents respond, and how long do we have before they do?*

**Structure (apply to each major incumbent):**

**Step 1: CAN they respond?**
- Do they have the capability? (Resources, distribution, brand)
- Do they have the motivation? (Is our success a threat to their core business?)
- Do they have the operational flexibility? (Can they launch a new product line without destroying existing business?)

**Step 2: What BARRIERS would they face?**
Categorize barriers by type:
- **Product barriers:** Reformulation, new ingredient sourcing, testing/validation
- **Brand barriers:** Would this product conflict with their existing positioning? (e.g., LMNT's "simple, 3 minerals" brand vs. marine plasma's "78 minerals")
- **Operational barriers:** New supply chain, new manufacturing, new SKU management
- **Strategic barriers:** Would this cannibalize their existing revenue? Would it confuse their customers?

**Step 3: TIMELINE estimation**
- Optimistic: assume they prioritize it and move fast. What's the minimum realistic timeline?
- Realistic: assume normal organizational speed. How long?
- Pessimistic: assume they decide not to do it at all. Why might that happen?

**Step 4: PROBABILITY assessment**
- What threshold of our success would trigger their response? (Usually: when we hit $2-5M revenue run rate, we become visible enough to act on)
- How confident are we in each timeline estimate? (Assign confidence grades)

**Step 5: OUR defensibility window**
- The gap between "when we launch" and "when they could respond" is our window.
- What do we need to accomplish in that window to make our position defensible? (Category ownership, customer loyalty, brand association)

---

### Framework C: Defensibility Stack

*What creates lasting competitive advantage? Not all advantages are equal.*

**Tier 1: Structural Advantages (hardest to copy)**
- **Network effects:** Does the product get better as more people use it? (Rare in supplements, but possible via community/social proof)
- **Data advantages:** Does using the product generate data that improves the experience? (Possible with personalization but not yet common in electrolytes)
- **Switching costs:** Once a customer is "locked in," how hard is it to leave? (Low in supplements generally — but loyalty programs, subscription inertia, and taste habituation create soft lock-in)

**Tier 2: Brand/Positioning Advantages (moderate difficulty to copy)**
- **Category ownership:** Being synonymous with a category. ("LMNT = electrolytes for keto" is category ownership. Once established, competitors can't easily claim the same space.)
- **Trust/credibility:** Built over time through consistent delivery. Can't be faked or shortcut.
- **Audience alignment:** Deep connection with a specific community (CrossFit, biohacking, keto). LMNT owns podcast audiences — that's a positioning moat.

**Tier 3: Operational Advantages (easiest to copy, but still real)**
- **Supply chain:** Better sourcing, lower COGS, faster fulfillment
- **Marketing efficiency:** Better creative, better targeting, better conversion
- **Distribution:** More retail/wholesale channels beyond DTC

**Application rule:** When assessing a competitor's strength, identify which tier(s) their advantage sits in. Tier 1 advantages are the ones that should make IonWave think hardest about differentiation strategy. Tier 3 advantages can be matched with execution.

---

### Framework D: Positioning Theory (Ries & Trout)

*How brands claim and defend mental real estate in customers' minds.*

**The core rules:**

1. **You can't be first in everything, but you can be first in a category.** If a category doesn't exist yet, create it. "Marine plasma electrolytes" is a category. Being first in it is more valuable than being second in "electrolytes."

2. **Repositioning the leader is harder than creating a new category.** Don't try to out-LMNT LMNT. Create a new box and own it.

3. **Perception IS reality.** It doesn't matter if marine plasma is objectively better. It matters what customers BELIEVE. Positioning is about shaping belief, not proving truth (though truth must underpin it or it collapses).

4. **The strongest position is the one tied to a specific, concrete benefit.** "Natural" is weak. "78 minerals your body actually uses, in the ratios nature intended" is stronger. "Tastes like water, works like medicine" is strongest (if true).

5. **Competitors' weaknesses are your positioning opportunities — but only if customers CARE about that weakness.** LMNT's saltiness is a weakness. But it only becomes IonWave's opportunity if customers are actively bothered by it (check customer voice evidence before positioning against it).

**Application in competitive analysis:**
- When mapping a competitor's position, identify: what category do they own? What benefit are they associated with? What weakness do customers notice?
- When assessing IonWave's positioning options, identify: what unclaimed category or benefit exists? Is there customer evidence that the gap is real (not just theoretical)?

---

## WORKED EXAMPLE: HOW FRAMEWORKS FIRED DURING LMNT ANALYSIS

This is the most important section. Abstract frameworks are useless without seeing how they actually played out.

**What happened when we ran LMNT:**

1. **Investor (Unit Economics)** flagged that v8's revenue estimate of $60-80M was based on podcast mentions and ad library inference. Pushed for SEC filing verification. Found Form C-AR showing $206.3M actual revenue — 3x the estimate. This immediately changed the threat assessment from "moderate competitor" to "dominant incumbent."

2. **Investor (Falsifiability)** asked: "What if their gross margin is lower than we assumed?" We assumed 70-80% (category benchmark). SEC filing showed 56.7%. This meant LMNT's margin stack is tighter than the category average — they're spending margin on the $7M sampling program and scale-related compression. This doesn't make them weaker, but it means IonWave shouldn't assume LMNT has unlimited margin to defend with.

3. **Anthropologist (JTBD)** identified that the dominant job LMNT customers are hiring the product for is "fasting support" — not workout recovery or general hydration. 60%+ of positive reviews mention fasting-related benefits. This means LMNT's strength is specifically in the fasting audience, and the workout/recovery audience might be underserved.

4. **Anthropologist (Pain/Gain/Switch)** found the key switch trigger: customers who LEFT other electrolytes for LMNT cited taste and simplicity (3 minerals, no sugar). Customers who were DISSATISFIED with LMNT cited saltiness and price. The switch map showed two distinct populations: loyalists (who love the salt) and churners (who find it too intense and leave).

5. **Strategist (Porter's)** assessed threat of new entrants as MODERATE — the real barrier isn't the product, it's the $500K+/month ad spend needed to compete at scale. This is a capital barrier, not a product barrier. Any well-funded entrant can replicate the product; they can't easily replicate LMNT's podcast distribution.

6. **Strategist (Competitive Response)** ran the scenario: could LMNT launch marine plasma? Assessed barriers: product reformulation (conflicts with "3 minerals" brand), supplier relationships (synthetic ≠ marine), brand identity risk. Estimated 12-18 month realistic timeline. But flagged: the $7M sampling program shows LMNT has operational flexibility to experiment. Probability adjusted upward from initial estimate.

7. **Strategist (Defensibility)** identified LMNT's advantage as Tier 2 (category ownership + audience alignment via podcasts). This is copyable in principle but takes 12-24 months to build. IonWave's window is real but narrow.

8. **Strategist (Positioning)** noted that "marine plasma" is an unclaimed category. IonWave doesn't need to beat LMNT at their game — it needs to own a different game. The positioning opportunity is category creation, not head-to-head competition.

---

## HOW TO USE THIS FILE

- **During persona dialogue:** When a persona needs to challenge something, look up the relevant framework section. The challenge should be grounded in a specific framework question, not just "show me evidence."
- **During research:** Use the "what to look for" sections to guide what data to collect. Don't just search for pricing — search for the specific evidence each framework needs.
- **During assembly:** The Strategic Notes section should reference which frameworks fired and what they revealed.
- **The worked example at the bottom is the most important section.** If you only read one thing, read that. It shows how abstract frameworks become concrete analytical moves.
