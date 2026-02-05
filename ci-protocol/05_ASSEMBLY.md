# 05 — ASSEMBLY
**How to build the integrated deliverable from all the pieces.**

---

## DELIVERABLE STRUCTURE: THREE VIEWS, ONE DOCUMENT

The output is a single integrated deliverable with three distinct views. Each section is self-contained but they reference each other where relevant.

---

## VIEW 1: ESTIMATES

The core intelligence — what we know (or think we know) about the competitor.

### Section Structure

```
# [Competitor Name] — Competitive Intelligence
**Protocol Run:** [ID]
**Date:** [date]
**Overall Confidence:** [aggregate grade — see grading rules below]

---

## PRODUCT PROFILE
[Basic facts: what they sell, formats, positioning]
Each fact tagged: [Confidence: X | Source: URL | Verified: date]

## PRICING
[All pricing tiers found]
Each price tagged: [Confidence: X | Source: URL | Verified: date]
[Per-serving calculation if available]
[Comparison to IonWave positioning]

## FINANCIAL SCALE
[Revenue estimate with full methodology]
[Each input to the estimate separately graded]
[Could be wrong if: scenarios]
[Benchmark comparison result — from 03_BENCHMARK_CHECK]
[Strategic note if anomaly detected]

## MARKET POSITION
[Where they sit in the competitive landscape]
[Distribution channels]
[Brand strength assessment]
[Target audience]

## CUSTOMER VOICE
[Organized by theme]
[Each theme: frequency, representative quotes, strategic implication]
[Saturation status noted]

## COMPETITIVE RESPONSE SCENARIO
[Could they enter our space? / Are we entering theirs?]
[Barriers, timeline, probability]
[Defensibility assessment]

## STRATEGIC NOTES
[Any anomalies flagged during benchmark check]
[Any tensions from persona dialogue that modified the analysis]
[Anything that surprised us]
```

### Confidence Tagging Rules
- Every factual claim gets a confidence tag inline
- Format: `[Confidence: A | Source: drinklmnt.com/shop | Verified: 2026-01-31]`
- Shortened format when space is tight: `[A — drinklmnt.com — 2026-01-31]`
- Analysis/interpretation gets: `[Analysis: Claude | Validated: pending/yes]`

---

## VIEW 2: INTELLIGENCE GAPS

What we DON'T know — and why it matters.

### Section Structure

```
# Intelligence Gaps — [Competitor Name]

## Gap [N]: [Title]

**What We Estimate:** [current best guess]
**Confidence:** [grade]
**Priority:** [CRITICAL / HIGH / MEDIUM / LOW]

**Why This Matters:**
[1-2 sentences on strategic importance]

**Impact If Wrong:**

*Scenario A: [optimistic scenario]*
- Implication: [what changes]
- Risk: [what breaks]

*Scenario B: [pessimistic scenario]*
- Implication: [what changes]  
- Risk: [what breaks]

**How to Validate:**
1. [Concrete action with timeline]
2. [Concrete action with timeline]

**Can We Proceed Without Knowing:** [Yes / No / Yes but with caveats]
```

### Gap Identification Sources
Gaps come from three places:
1. **Research phase:** Things we searched for but couldn't find
2. **Benchmark check:** Metrics where our estimate is D-grade (no real source)
3. **Persona dialogue:** UNRESOLVED tensions that represent genuine unknowns

### Gap Prioritization
Rank by: (impact if wrong) × (probability we're wrong)
- CRITICAL: High impact + likely wrong (e.g., revenue estimate based on D-grade source)
- HIGH: High impact + possibly wrong OR medium impact + likely wrong
- MEDIUM: Medium impact + possibly wrong
- LOW: Low impact regardless

---

## VIEW 3: SCORECARD

Executive summary. The first thing a reader sees.

### Section Structure

```
# Scorecard — [Competitor Name]

## Summary
[2-3 sentences: what this competitor is, how big a threat, confidence in our assessment]

## Confidence Overview

| Section | Grade | Key Limitation |
|---------|-------|----------------|
| Product Profile | [A/B/C/D] | [what's missing or uncertain] |
| Pricing | [A/B/C/D] | [what's missing or uncertain] |
| Financial Scale | [A/B/C/D] | [what's missing or uncertain] |
| Customer Voice | [A/B/C/D] | [what's missing or uncertain] |
| Competitive Response | [A/B/C/D] | [what's missing or uncertain] |
| **Overall** | **[aggregate]** | |

## Aggregate Grade Calculation
- All A → A
- Mostly A, some B → A-
- Mix of A and B → B+
- Mostly B → B
- Mix of B and C → B-
- Mostly C → C
- Any D without upgrade path → flag for attention

## Top Strategic Implications
1. [Most important takeaway for IonWave strategy]
2. [Second most important]
3. [Third]

## Upgrade Shopping List (Prioritized)
*What human legwork would elevate this from current grade to A-grade*

| Priority | What to Do | Time Estimate | Would Upgrade |
|----------|-----------|---------------|---------------|
| 1 | [most critical human task] | [hours] | [which section, from X to A] |
| 2 | [next most critical] | [hours] | [which section] |
| ... | ... | ... | ... |

## Upgrade Shopping List Rules
- Sorted by priority (highest-impact upgrades first)
- Each item is a concrete, actionable task (not "get better data" — "pull SEMrush traffic report for drinklmnt.com, export monthly visitors Jan-Dec 2025")
- Time estimate included for each task
- States exactly which section and which grade it would achieve
```

---

## ASSEMBLY CHECKLIST

Before finalizing, verify:
- [ ] Every factual claim has a confidence tag
- [ ] All three views are present and internally consistent
- [ ] Scorecard accurately reflects the grades in View 1
- [ ] All below-A items in View 1 have corresponding entries in the upgrade shopping list
- [ ] All gaps from View 2 are reflected in the scorecard's "Key Limitation" column
- [ ] Persona dialogue tensions are either resolved in the analysis or documented as gaps
- [ ] Benchmark anomalies are documented as strategic notes
- [ ] The upgrade shopping list is sorted by priority, not by section order
