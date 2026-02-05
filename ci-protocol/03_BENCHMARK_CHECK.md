# 03 — BENCHMARK CHECK
**Reality check + anomaly detection. Two-pass audit structure.**

---

## WHY THIS EXISTS

Two functions, both important:

1. **Reality check:** Catches impossible or implausible estimates before they reach the output. If our revenue estimate for a $5M DTC brand comes back as $500M, something is wrong.

2. **Anomaly detection:** When a competitor deviates SIGNIFICANTLY from industry benchmarks, that deviation is often strategically meaningful. It's either an exploitable weakness or a competitive advantage worth understanding.

The key insight (from Danilo's framework): LLMs don't automatically flag when numbers are implausible. This step must be explicit.

---

## TWO-PASS STRUCTURE

### Pass 1: Narrative Audit (run first)
Check for INTERNAL CONSISTENCY across all estimates before checking against external benchmarks.

**Questions to answer:**
- Do the estimates tell a coherent story? (e.g., if revenue is $200M, does the estimated headcount / ad spend / market share make sense at that scale?)
- Are there mathematical impossibilities? (e.g., revenue per serving × estimated servings sold ≠ stated revenue)
- Do customer voice findings align with the strategic positioning claims?
- Are the competitive response scenarios plausible given the company's actual scale?

**If inconsistency found:** Flag it, resolve it (usually means one estimate is wrong), then proceed to Pass 2.

### Pass 2: Component Audit (run second)
Check each estimate individually against industry benchmarks.

**For each numeric estimate in the output:**
1. What is the relevant industry benchmark for this metric?
2. How does the competitor's value compare to the benchmark?
3. If deviation is >2x in either direction, flag as anomaly
4. Document the benchmark, the deviation, and what it might mean strategically

---

## INDUSTRY BENCHMARKS BY METRIC TYPE

### DTC Supplement / Health Product Benchmarks

| Metric | Benchmark Range | Source Notes |
|--------|----------------|--------------|
| **Gross Margin** | 65-75% | Healthy supplement DTC; drops with scale (shipping, fulfillment) |
| **Net Margin** | 10-20% | Mature DTC brands; startups often negative |
| **CAC (Customer Acquisition Cost)** | $25-45 | DTC supplement; varies hugely by channel |
| **LTV (Lifetime Value)** | $120-250 | Subscription-based supplement; depends on retention |
| **LTV:CAC Ratio** | 3:1 to 5:1 | Target for healthy DTC; <2:1 is unsustainable |
| **Subscription Rate** | 40-60% | % of customers on auto-ship |
| **Retention (Month 3)** | 50-65% | Subscription retention at 3 months |
| **Retention (Month 6)** | 35-50% | Subscription retention at 6 months |
| **Ad Spend as % Revenue** | 25-40% | S&M spend; higher = growth stage, lower = mature |
| **ROAS (Return on Ad Spend)** | 2.5x-4x | Revenue per $1 of ad spend |
| **Price per Serving** | $0.80-2.00 | Premium supplement range |
| **Revenue per Employee** | $2M-5M | Lean DTC operations |
| **Sampling/Free Product spend as % Revenue** | 1-5% | Customer acquisition via sampling |

### Electrolyte Category Specific

| Metric | Benchmark Range | Notes |
|--------|----------------|-------|
| **Category Growth Rate** | 8-15% YoY | Sports nutrition / electrolyte segment |
| **Average Serving Size** | 1-2g powder | Electrolyte drink mix |
| **Sodium per Serving** | 200-1000mg | Range across category (low to high) |
| **Price Premium vs. Mass Market** | 1.5x-3x | Premium vs. Gatorade/Pedialyte |

### General DTC E-Commerce

| Metric | Benchmark Range | Notes |
|--------|----------------|-------|
| **Website Conversion Rate** | 2-4% | E-commerce average |
| **AOV (Average Order Value)** | $40-80 | Supplement subscription box |
| **Email List as % Monthly Visitors** | 5-15% | Healthy conversion to email |
| **Social Media Followers to Revenue** | $50-200 per 1K followers | Very rough proxy |

---

## ANOMALY DETECTION LOGIC

After comparing each estimate to its benchmark:

### Anomaly = Deviation > 2x from benchmark (in either direction)

**When anomaly is detected, document:**

1. **The metric and value found**
2. **The benchmark it's being compared against**
3. **The deviation magnitude** (e.g., "3.2x above benchmark")
4. **Direction** (above or below benchmark)
5. **Strategic interpretation** — choose the most likely explanation:

### Interpretation Framework

**If ABOVE benchmark (competitor outperforms):**
- **Structural advantage:** They have something others don't (brand, distribution, channel)
  - Example: LMNT's podcast distribution gives them abnormally low CAC
- **Category leader premium:** First-mover or dominant brand commands premium metrics
- **Measurement artifact:** The benchmark doesn't apply to their specific sub-segment
- **Unsustainable:** They're burning cash to achieve this metric (check profitability)

**If BELOW benchmark (competitor underperforms):**
- **Exploitable weakness:** They're losing on this metric — potential opportunity
  - Example: If retention is 30% vs. 50% benchmark, retention is an attack vector
- **Growth stage investment:** They're spending margin to grow (intentional)
- **Category drag:** Something about their product/positioning structurally limits this metric
- **Data quality issue:** Our estimate might be wrong — flag for verification

### What to Do With Anomalies
- Document in the output as a **Strategic Note** in the relevant section
- If the anomaly is exploitable → flag for IonWave positioning discussion
- If the anomaly suggests our estimate is wrong → re-examine the source
- If the anomaly is a competitor advantage → document in competitive response scenario

---

## BENCHMARK CHECK COMPLETION CRITERIA

- [ ] Narrative audit complete (internal consistency verified)
- [ ] Every numeric estimate compared to relevant benchmark
- [ ] All anomalies (>2x deviation) documented with strategic interpretation
- [ ] No mathematical impossibilities remain in the output

---

## EXAMPLE

**Finding:** LMNT gross margin = 56.7% (from SEC filing)
**Benchmark:** DTC supplement gross margin = 65-75%
**Deviation:** 0.76x benchmark (below by 24%)
**Direction:** Below
**Interpretation:** At $206M revenue scale, margin compression from shipping costs and fulfillment is expected. But 56.7% is notably below the healthy benchmark range. This could mean: (a) they're investing margin into the $7M sampling program, (b) marine plasma brands with higher COGS might face even more compression, or (c) this sets a realistic ceiling for what IonWave should model at scale.
**Action:** Flag as strategic note — IonWave's margin projections should model compression to 55-60% at scale, not hold at startup margins.
