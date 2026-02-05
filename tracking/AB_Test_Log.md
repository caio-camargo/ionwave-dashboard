# AB Test Log

**Purpose:** Systematic tracking of all AB tests across the business  
**Updated:** When tests launch and when results are conclusive  
**Maintenance:** Document every test before launch, log results  
**Owner:** Operator + relevant domain owner

---

## WHY WE TEST

**We test because:**
- Assumptions are often wrong
- Small changes can have big impacts
- Data beats opinions
- Optimization compounds over time

**We don't test:**
- Things that don't matter (vanity metrics)
- Too many things at once (confounds results)
- Without clear hypotheses (fishing expeditions)
- When sample size is too small (inconclusive)

---

## TEST PROTOCOL

### Before Launching Any Test

1. **Hypothesis:** What do we believe will happen?
2. **Rationale:** Why do we believe this?
3. **Variables:** What exactly are we changing?
4. **Metrics:** How will we measure success?
5. **Sample Size:** How much traffic/volume needed?
6. **Timeline:** How long to run test?
7. **Success Criteria:** What result = winner?

### During Test

- Monitor for implementation errors
- Don't peek at results early (p-hacking)
- Let test run to statistical significance
- Document any anomalies

### After Test

- Analyze results objectively
- Implement winner
- Document learnings
- Share with team

---

## ACTIVE TESTS

### Test #001: Price Point Test

**Status:** ⏳ RUNNING  
**Launched:** 2026-02-15  
**Expected End:** 2026-03-01 (2 weeks)

**Hypothesis:**
$59 price point will convert better than $49, despite higher sticker price, because it signals quality and justifies marine plasma premium.

**Rationale:**
- Competitor LMNT is $45 (synthetic)
- Competitor Seaonic is $89 (ultra-premium)
- $59 positions us as premium but accessible
- Customer research shows willingness to pay for quality

**Variables:**
- Control: $49 price point
- Variant: $59 price point
- (Everything else identical)

**Metrics:**
- Primary: Revenue per visitor (RPV)
- Secondary: Conversion rate, AOV, ROAS

**Sample Size:** 
- Need 2,000 visitors per variant
- Current: 847 / 2,000 (control), 823 / 2,000 (variant)

**Timeline:** 2 weeks (adjust if traffic lower)

**Success Criteria:**
- $59 variant must have ≥5% higher RPV
- AND maintain ≥2.0% conversion rate
- Statistical significance p<0.05

**Current Results (Interim - DO NOT CONCLUDE YET):**
- Control ($49): 847 visitors, 2.4% CVR, $1.02 RPV
- Variant ($59): 823 visitors, 2.1% CVR, $1.26 RPV
- Variant ahead on RPV but needs full data

**Notes:** Don't peek! Let it run to full sample size.

---

### Test #002: VSL Length Test

**Status:** 📋 PLANNED  
**Launch Date:** TBD (after price test concludes)

**Hypothesis:**
Shorter VSL (3 min) will convert better than longer VSL (5 min) because attention spans are declining and we need to close faster.

**Rationale:**
- Industry trend toward shorter content
- Mobile traffic has limited patience
- Core value prop can be delivered in 3 min
- But: counter-view is longer = more trust built

**Variables:**
- Control: 5-minute VSL (current)
- Variant: 3-minute VSL (condensed)
- (Same script structure, just tighter)

**Metrics:**
- Primary: Conversion rate (VSL → Purchase)
- Secondary: Video completion rate, ROAS

**Sample Size:** 3,000 visitors per variant (6,000 total)

**Timeline:** 3 weeks

**Success Criteria:**
- 3-min must have ≥10% higher CVR
- OR maintain same CVR with higher completion rate
- Statistical significance p<0.05

**Pre-Work Needed:**
- [ ] Script 3-minute version
- [ ] Film and edit new VSL
- [ ] Set up split test in funnel
- [ ] Verify tracking works

---

## TEST HISTORY (COMPLETED)

### Test #000: Email Subject Line Test

**Status:** ✅ COMPLETED  
**Launched:** 2026-01-20  
**Concluded:** 2026-01-27  
**Duration:** 7 days

**Hypothesis:**
Curiosity-driven subject line will outperform benefit-driven subject line in open rates.

**Variables:**
- Control: "Get 78 Essential Minerals in One Serving"
- Variant: "Why Your Body Might Be Mineral Deficient"

**Results:**
- Control: 24.3% open rate (2,847 sends)
- Variant: 31.7% open rate (2,821 sends)
- Winner: Variant (+30% relative lift)
- Statistical significance: p<0.01 ✅

**Learnings:**
- Curiosity gap works better than feature listing
- "Why" questions engage better than "Get" statements
- Negative framing ("deficient") can work if followed by solution

**Action Taken:**
- Implemented curiosity-based subject lines as default
- Created subject line library with "Why" templates
- Tested pattern holds across multiple emails

---

## TEST CATEGORIES

### Pricing & Offer Tests
- Price point variations
- Bundle configurations
- Subscription vs one-time
- Discount levels
- Upsell sequencing

### Creative Tests
- Ad hooks
- Ad angles
- Visual styles
- Copy length
- CTA variations

### Landing Page Tests
- Headline variations
- VSL length
- Proof elements (testimonials, studies)
- Form fields (email only vs email+phone)
- Layout changes

### Email Tests
- Subject lines
- Send times
- Personalization
- Content structure
- CTA placement

### Funnel Tests
- Flow sequences
- Page order
- Exit intent offers
- Checkout optimization

---

## TESTING BEST PRACTICES

### DO

✅ Test one variable at a time  
✅ Run to statistical significance  
✅ Document hypothesis before launching  
✅ Calculate required sample size upfront  
✅ Wait for full duration before concluding  
✅ Implement winners immediately  
✅ Share learnings with team

### DON'T

❌ Test multiple variables simultaneously  
❌ Call winners early (p-hacking)  
❌ Test without hypothesis  
❌ Stop test when result looks good  
❌ Ignore neutral results (they teach too)  
❌ Test things that don't matter  
❌ Keep testing same thing repeatedly

---

## STATISTICAL SIGNIFICANCE

### Sample Size Calculator

**For Conversion Rate Tests:**
- Baseline CVR: 2.5%
- Minimum Detectable Effect: 20% (0.5% absolute)
- Confidence: 95%
- Power: 80%
- **Required Sample:** ~3,000 per variant

**For Revenue Tests:**
- Baseline RPV: $1.00
- Minimum Detectable Effect: 15% ($0.15)
- Confidence: 95%
- Power: 80%
- **Required Sample:** ~2,000 per variant

### When to Stop a Test

**Stop Early (Rare):**
- Implementation error discovered
- External event invalidates test (site outage, major news)
- Variant is massively worse (>50% decline, p<0.01)

**Normal Conclusion:**
- Reached required sample size
- OR 30 days elapsed (whichever first)
- AND statistical significance achieved

**Inconclusive:**
- Reached sample but no significance
- = No clear winner, keep control
- Log learnings anyway

---

## TEST PRIORITIZATION

### High Priority (Test First)
- Large traffic volume (affects many)
- High-impact variables (pricing, core offer)
- Clear hypothesis with strong rationale
- Easy to implement

### Medium Priority (Test When Capacity)
- Moderate traffic
- Moderate impact (page elements)
- Reasonable hypothesis
- Moderate implementation effort

### Low Priority (Nice to Have)
- Low traffic
- Low impact (cosmetic)
- Weak hypothesis
- High implementation effort

**Focus on:** High traffic × High impact = Biggest wins

---

## COMMON MISTAKES

### Mistake #1: Testing Too Early
**Problem:** Not enough traffic yet  
**Result:** Tests take months, waste time  
**Fix:** Wait until 2,000+ visitors/week

### Mistake #2: Too Many Variants
**Problem:** Split traffic 5 ways  
**Result:** Never reach significance  
**Fix:** Limit to 2-3 variants max

### Mistake #3: Peeking at Results
**Problem:** Call winner at 50% sample  
**Result:** False positive (p-hacking)  
**Fix:** Set sample size, don't peek until reached

### Mistake #4: Testing Wrong Things
**Problem:** Test button color instead of offer  
**Result:** Tiny gains on low-impact variables  
**Fix:** Prioritize high-impact tests

### Mistake #5: Ignoring Neutral Results
**Problem:** "No winner = wasted test"  
**Result:** Miss valuable learnings  
**Fix:** Document why hypothesis was wrong

---

## TESTING ROADMAP

### Q1 2026 Testing Plan

**February:**
- [ ] Test #001: Price point ($49 vs $59)
- [ ] Test #002: VSL length (3 min vs 5 min)

**March:**
- [ ] Test #003: Bundle offer (single vs 3-pack)
- [ ] Test #004: Ad hook variations (top 5 hooks)

**April:**
- [ ] Test #005: Landing page headline
- [ ] Test #006: Email sequence timing

**Success Metrics:**
- Run 6 tests in Q1
- Implement 4+ winners
- Achieve 20%+ cumulative lift in key metrics

---

## TEST TEMPLATE

```markdown
### Test #___: [Test Name]

**Status:** [📋 PLANNED | ⏳ RUNNING | ✅ COMPLETED]  
**Launched:** [Date]  
**Expected End:** [Date]

**Hypothesis:**
[What we believe will happen and why]

**Variables:**
- Control: [Current/baseline version]
- Variant: [What we're testing]

**Metrics:**
- Primary: [Key success metric]
- Secondary: [Supporting metrics]

**Sample Size:** [Number per variant]

**Timeline:** [Duration]

**Success Criteria:**
[Specific threshold for declaring winner]

**Results:**
[Fill in when complete]

**Learnings:**
[What we learned, even if inconclusive]

**Action Taken:**
[What we implemented based on results]
```

---

**Last Updated:** 2026-02-02  
**Active Tests:** 1  
**Completed Tests:** 1  
**Testing Queue:** 5  
**Owner:** [Name]
