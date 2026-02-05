# Deliverable Structure Standards
**New sheet to add to: 32_Quality_Standards.xlsx**

---

## PURPOSE

Defines mandatory structure for all Imagination Generation deliverables. This ensures consistency, quality documentation, and upgrade path visibility across all 38 domain files.

---

## STANDARD STRUCTURE

All Imagination deliverables must include THREE sections:

### SECTION 1: MAIN CONTENT
**Purpose:** The actual intelligence, analysis, or strategy

**Required Elements:**
- âœ… Every factual claim has confidence tag: `[Confidence: A/B/C/D | Source: URL | Verified: date]`
- âœ… Every estimate shows methodology (how calculated, what assumptions)
- âœ… Every analysis shows framework used: `[Analysis: Claude | Framework: X | Validated: pending/yes]`
- âœ… Strategic notes for key insights or anomalies
- âœ… Cross-references to dependent deliverables

**Format Examples:**

**Factual Claim:**
```
LMNT pricing: $45 for 30 servings = $1.50/serving 
[Confidence: A | Source: drinklmnt.com/shop | Verified: 2026-01-31]
```

**Estimate:**
```
LMNT revenue: $206M (FY2023) 
[Confidence: A | Source: SEC Form C-AR | Verified: 2026-01-31]
Methodology: Audited financial disclosure
Could be wrong if: They've contracted significantly since FY2023
```

**Analysis:**
```
Competitive threat assessment: HIGH
[Analysis: Claude | Framework: Porter's Five Forces + Response Scenarios | Validated: pending]
Rationale: Scale advantage ($206M vs our $0), brand recognition, distribution...
```

---

### SECTION 2: INTELLIGENCE GAPS
**Purpose:** Document what we DON'T know and why it matters

**Required Elements:**
For each significant gap:

```
## Gap [N]: [Descriptive Title]

**What We Estimate:** [current best guess with confidence grade]
**Source of Estimate:** [where it came from - benchmark, calculation, assumption]
**Confidence:** [A/B/C/D]

**Why This Matters:**
[1-2 sentences on strategic importance]

**Impact If Wrong:**
- **Optimistic scenario:** If actual is [better], then [implication]
- **Pessimistic scenario:** If actual is [worse], then [implication]

**How to Validate:**
1. [Specific actionable step with timeline]
2. [Specific actionable step with timeline]

**Timeline to Answer:** [when we could realistically know this]
**Can We Proceed Without Knowing:** [Yes / No / Yes but with caveats]
**Priority:** [CRITICAL / HIGH / MEDIUM / LOW]
```

**Prioritization Framework:**
- **CRITICAL:** High impact if wrong + likely wrong + blocks key decisions
- **HIGH:** High impact + possibly wrong OR medium impact + likely wrong
- **MEDIUM:** Medium impact + possibly wrong
- **LOW:** Low impact regardless of accuracy

---

### SECTION 3: SCORECARD
**Purpose:** Executive summary of quality and upgrade priorities

**Required Elements:**

```
# [Deliverable Name] Scorecard

## Summary
[2-3 sentences: what this deliverable covers, overall confidence, key takeaway]

## Confidence Overview

| Section | Grade | Key Limitation |
|---------|-------|----------------|
| [Section 1] | A/B/C/D | [what's missing or uncertain] |
| [Section 2] | A/B/C/D | [what's missing or uncertain] |
| [Section 3] | A/B/C/D | [what's missing or uncertain] |
| **Overall** | **[aggregate]** | |

**Aggregate Grade Rules:**
- All A → A
- Mostly A, some B → A-
- Mix of A and B → B+
- Mostly B → B
- Mix of B and C → B-
- Mostly C → C
- Any D without upgrade path → Flag for attention
- Critical section at D → Overall cannot be above C

## Top Strategic Implications
1. [Most important takeaway for business strategy]
2. [Second most important]
3. [Third most important]

[These should be ACTIONABLE insights, not just summaries]

## Upgrade Shopping List (Prioritized)

| Priority | Task | Time | Expected Outcome |
|----------|------|------|------------------|
| 1 | [Specific actionable task] | [hours/days] | [Section]: [current] → A |
| 2 | [Specific actionable task] | [hours/days] | [Section]: [current] → [target] |
| 3 | [Specific actionable task] | [hours/days] | [Section]: [current] → [target] |

**Shopping List Rules:**
- Sorted by IMPACT (highest-value upgrades first), not alphabetically
- Each task is CONCRETE ("Pull SEMrush traffic report", not "verify traffic")
- Time estimates included for planning
- Expected outcome specified (which grade, which section)
```

---

## CONFIDENCE GRADE SCALE

**A: Verified from Authoritative Source**
- SEC filings, audited financials
- Official company website (pricing, product info)
- 3+ independent sources that corroborate
- Recent (< 6 months) and verified

**B: Strong Single Source or Good Triangulation**
- Credible news article or industry report
- 2 independent sources that align
- Company blog or press release
- Recent analyst coverage
- Calculated from A-grade inputs with sound methodology

**C: Industry Benchmark or Derived Estimate**
- Industry average applied to specific competitor
- Calculated from B/C-grade inputs
- Single source > 1 year old
- Pattern from customer voice (10-20 quotes)
- Proxy metric with documented methodology

**D: Best Guess with No Solid Source**
- Blocked access to data
- Reasoning from category knowledge
- Assumption with no verification
- Pattern from limited customer voice (< 10 quotes)
- Older data (> 2 years) with unknown current accuracy

---

## UNACCEPTABLE DELIVERABLE PATTERNS

These indicate the deliverable is NOT ready:

âŒ **Claims without confidence tags**
"LMNT does $200M in revenue" ← No grade, no source

âŒ **Estimates without methodology**
"CAC is $30" ← How calculated? What assumptions?

âŒ **Below-A grades without upgrade paths**
"Traffic: 500K visits [C]" ← How to get to A-grade?

âŒ **Vague upgrade paths**
"Verify this data" ← Too vague. Verify HOW? From WHERE? How long?

âŒ **Optimistic scorecard**
Scorecard says "B+" but actual content is mostly C-grade

âŒ **Missing Gaps section**
Deliverable pretends everything is known (no honest gap documentation)

âŒ **No strategic implications**
Scorecard just summarizes without explaining "so what?"

---

## ACCEPTABLE DELIVERABLE PATTERNS

These indicate good process even if data quality is low:

✅ **Honest D-grade with upgrade path**
"Revenue: $2-5M [D - no sources found, category proxy]. Upgrade: Contact supplier for customer count, cross-check with social metrics (2 hours)"

✅ **Methodology documented for C-grade**
"CAC: $28 [C - DTC supplement benchmark]. Methodology: Shopify 2024 report shows $25-35 range for paid social. Could be wrong if: LMNT's podcast ROI is better. Validation: Test our own CAC (4 weeks, $5K)"

✅ **Gap prioritization is clear**
"Gap 1 (CRITICAL): Actual customer churn. Gap 2 (HIGH): Traffic verification. Gap 3 (MEDIUM): Partnership details..."

✅ **Shopping list is actionable**
"1. [2 hrs] Pull SEMrush traffic for top 5 competitors → Traffic C→A"

✅ **Scorecard matches reality**
Content is mostly C-grade → Scorecard honestly says C+ overall

---

## DELIVERABLE-SPECIFIC VARIATIONS

Some deliverables may need adapted structure:

**Research Deliverables** (Market Intelligence, Customer Research):
- Main Content: Heavily tagged with confidence
- Gaps: Many gaps expected (external data collection required)
- Scorecard: Shopping list is primary value

**Strategy Deliverables** (Thesis, ICP, Positioning):
- Main Content: More analysis, less factual claims
- Gaps: Fewer gaps (built from research layer)
- Scorecard: Strategic implications are primary value

**Financial Deliverables** (Unit Economics, Financial Model):
- Main Content: Input assumptions must be tagged with source deliverable
- Gaps: Focus on assumption risk scenarios
- Scorecard: Sensitivity to input changes is key metric

**Execution Deliverables** (Creative Strategy, Funnel, Media Plan):
- Main Content: Shows dependencies on upstream deliverables explicitly
- Gaps: Flag where upstream quality limits execution confidence
- Scorecard: Readiness assessment (can we execute with current confidence?)

---

## INTEGRATION WITH OTHER SYSTEMS

### Connection to Discrepancy Register
- Before finalizing deliverable, check for conflicts with other sheets
- Flag cross-sheet inconsistencies in Discrepancy Register
- Don't claim A-grade if dependent inputs are C/D-grade

### Connection to Definition of Done
- Definition of Done = execution milestones ("product ordered", "ads launched")
- Deliverable Structure = quality documentation ("confidence documented", "gaps identified")
- Both must be met for deliverable to be truly complete

### Connection to CM System
- CM can use Scorecard to quickly assess deliverable quality
- Upgrade Shopping List shows exactly what human work would improve grade
- Honest D-grade with upgrade path > Inflated B-grade without upgrade path

---

## IMPLEMENTATION CHECKLIST

When adding this standard to existing deliverables:

### Phase 1: Add Structure (Foundational)
- [ ] Add Scorecard sheet/section with confidence overview
- [ ] Add Intelligence Gaps sheet/section
- [ ] Start tagging new claims with confidence as they're added

### Phase 2: Backfill Quality Tags (Remediation)
- [ ] Review existing claims, add confidence tags
- [ ] Document methodology for existing estimates
- [ ] Identify and document gaps that were implicit

### Phase 3: Validate (Quality Check)
- [ ] Run self-grade checklist
- [ ] Verify scorecard matches actual content
- [ ] Verify all <A grades have upgrade paths
- [ ] Check for cross-sheet discrepancies

### Phase 4: Maintain (Ongoing)
- [ ] Update confidence tags when new data arrives
- [ ] Update gaps when questions are answered
- [ ] Update scorecard when sections improve
- [ ] Reference in Discrepancy Register when relevant

---

**Status:** Standard defined - ready for implementation  
**First Application:** Market Intelligence (02_Market_Intelligence.xlsx)  
**Rollout:** Apply to Research layer first, then Strategy, then Financial, then Execution  
**Owner:** Caio + Claude  
**Updated:** 2026-02-03
