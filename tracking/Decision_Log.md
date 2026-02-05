# IonWave Decision Log

**Purpose:** Append-only history of decisions with full context, rationale, and impact  
**Format:** Each decision gets a unique ID: YYYY-MM-DD-###  
**Usage:** Reference decisions by ID in other tracking documents

---

## 2026-02-02-001: Gross Margin Discrepancy Discovered

**Status:** IN RESOLUTION (not yet decided)

**Context:**
During bootstrap improvement work on Market Landscape, discovered critical discrepancy:
- Unit Economics sheet assumes 70% gross margin
- Landed Cost Breakdown shows 40% gross margin (based on actual supplier quotes)
- This 30 percentage point gap has massive downstream impacts

**Investigation:**
- Loaded Landed Cost Breakdown sheet
- Supplier quotes show $12 COGS for 30-serving bottle
- At $59 retail price point = ($59 - $12) / $59 = 79.7% margin... wait
- Need to verify actual calculation in sheet
- **Root Cause:** Unit Economics used industry benchmark (supplements typically 70-80%)
- Landed Cost used actual supplier quotes (marine plasma more expensive than synthetic)

**Options Under Consideration:**
1. **Accept 40% margin reality:**
   - Pro: Based on real supplier data
   - Con: Much lower than industry standard
   - Con: May not support desired unit economics
   - Impact: Need higher price OR volume to hit targets

2. **Negotiate COGS down to enable 70% margin:**
   - Target COGS: ~$8 instead of $12 (33% reduction)
   - Pro: Aligns with industry benchmarks
   - Con: May not be achievable with marine plasma
   - Action: Need supplier negotiation or alternative sourcing

3. **Increase price point:**
   - Target: $79-89 retail (vs current $59)
   - Pro: Improves margin at current COGS
   - Con: May reduce conversion rate
   - Con: Positions above LMNT ($45 for 30 servings)

**Impact Analysis:**
- **Unit Economics:** Must be rebuilt with correct margin
- **Offer Strategy:** Pricing strategy may need complete revision
- **Financial Model:** Revenue projections could drop ~30%
- **W Formula Score:** May affect viability if margin kills profitability
- **Competitive Positioning:** Price point affects positioning vs LMNT/Seaonic

**Affected Sheets/Models:**
- Unit Economics (primary)
- Landed Cost Breakdown (source of truth)
- Offer Strategy
- Financial Model
- Pricing decisions

**Next Actions:**
- [ ] Verify exact COGS calculation in Landed Cost sheet
- [ ] Verify exact margin calculation in Unit Economics sheet
- [ ] Model all three scenarios (accept, negotiate, price up)
- [ ] Get Danilo's decision on path forward
- [ ] Update all affected sheets once decided
- [ ] Document decision rationale

**Owner:** Danilo (decision maker) + Caio (analysis support)  
**Due:** Within 48 hours (blocks multiple streams)  
**Logged By:** Claude  
**Date:** 2026-02-02

**Related:**
- Discrepancy_Register.md #D1
- Open_Questions.md #Q1
- MASTER_CONTROL.md (Critical Dependencies section)

---

## 2026-02-02-002: Bootstrap Methodology - Track A vs Track B

**Status:** DECIDED

**Context:**
Working on improving IonWave Market Landscape from 4-6/10 to 8-9/10 quality. Need to determine what work can be done immediately (Track A) vs what requires data collection tools (Track B).

**Decision:**
Split improvement work into two tracks:

**Track A (Strategic Analysis - No Tools):**
- Apply expert frameworks (Porter's Five Forces, Skeptical Investor lens)
- Mine customer voice from free web search (Reddit, Trustpilot, reviews)
- Competitive response scenario planning
- Strategic gap analysis
- Time: 4-6 hours
- Cost: $0
- Quality impact: 4/10 → 6-7/10

**Track B (Data Collection - Tools Required):**
- SEMrush traffic verification
- Paid market research reports
- Extensive competitor coverage (expand from 2 to 10-12)
- Time: 15-20 hours
- Cost: Tool subscriptions + labor
- Quality impact: 6-7/10 → 8-9/10

**Rationale:**
- Can make significant quality improvements without waiting for data
- Clear workflow choreography: Track A first, then decide if Track B needed
- Separates strategic thinking from data gathering
- Lets Operator (Caio) make immediate progress

**Impact:**
- Market Landscape improvement can start immediately
- Sets pattern for other deliverable improvements
- Informs OpKit development approach

**Next Actions:**
- [x] Execute Track A work on Market Landscape
- [ ] Document what worked for methodology extraction
- [ ] Decide if Track B needed after Track A complete

**Owner:** Caio + Claude  
**Date:** 2026-02-02  
**Logged By:** Claude

**Related:**
- Market_Landscape_Bootstrap_Plan.md
- 03_What_We_Did.md (Track A/B discovery)

---

## TEMPLATE FOR FUTURE DECISIONS

```
## YYYY-MM-DD-###: [Decision Title]

**Status:** [DECIDED | IN DISCUSSION | DEFERRED | REVERSED]

**Context:**
[What situation prompted this decision? What was happening?]

**Decision:**
[What was decided? Be specific and clear.]

**Options Considered:**
1. [Option 1 with pros/cons]
2. [Option 2 with pros/cons]
3. [Option 3 with pros/cons]

**Rationale:**
[Why this option? What factors tipped the decision?]

**Impact Analysis:**
[What does this affect? Downstream consequences?]

**Affected Sheets/Models:**
[List specific sheets/models that need updates]

**Next Actions:**
- [ ] [Action item 1]
- [ ] [Action item 2]

**Owner:** [Who owns execution]  
**Date:** [When decided]  
**Logged By:** [Who logged it]

**Related:**
[Links to other tracking documents]
```

---

**Log Maintenance:**
- Append new decisions to bottom (reverse chronological at top)
- Never delete entries (historical record)
- Update status as decisions evolve
- Reference by ID in other documents
