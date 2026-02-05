# IonWave Discrepancy Register

**Purpose:** Track conflicts between sheets/models where data doesn't match  
**Maintenance:** Claude updates when discovering or resolving conflicts  
**Critical Rule:** Don't finalize conflicting sheets until discrepancy resolved

---

## ðŸ”´ ACTIVE DISCREPANCIES (Require Resolution)

### D1: Gross Margin Mismatch (CRITICAL)

**Status:** IN RESOLUTION  
**Severity:** ðŸ”´ CRITICAL - blocks multiple work streams  
**Discovered:** 2026-02-02 during bootstrap analysis  

**The Conflict:**
- **Sheet 1:** Unit Economics - assumes 70% gross margin
- **Sheet 2:** Landed Cost Breakdown - calculates 40% gross margin
- **Gap:** 30 percentage points (massive difference)

**Details:**
```
Unit Economics assumption:
- Retail Price: $59
- COGS: ~$18 (implied by 70% margin)
- Gross Margin: 70%

Landed Cost reality:
- Retail Price: $59  
- COGS: $12 (actual supplier quotes)
- Gross Margin: ~79.7%... 
[WAIT - need to verify if Landed Cost sheet shows 40% or different calc]

ACTION: Verify exact numbers in both sheets before proceeding
```

**Root Cause:**
- Unit Economics used industry benchmark for supplements (70-80% typical)
- Landed Cost used actual supplier quotes
- Supplier quotes show marine plasma is more expensive than synthetic alternatives
- No cross-validation process existed between sheets

**Impact:**
- Pricing strategy may be wrong
- Offer Strategy built on wrong margin assumptions
- Financial Model projections may be off by 30%
- May affect Trade viability (W Formula score)

**Resolution Options:**
1. **Update Unit Economics to match Landed Cost reality** (accept lower margin)
2. **Negotiate COGS down** to match Unit Economics assumption (target 70%)
3. **Increase price point** to achieve desired margin at actual COGS

**Resolution Protocol:**
1. [ ] Verify exact COGS in Landed Cost Breakdown
2. [ ] Verify exact margin calculation in Unit Economics
3. [ ] Document which is correct (Landed Cost = source of truth)
4. [ ] Model impact of each resolution option
5. [ ] Get Danilo's decision on path forward
6. [ ] Update ALL affected sheets
7. [ ] Verify updates with cross-check
8. [ ] Mark discrepancy as RESOLVED

**Affected Sheets:**
- Unit Economics (primary)
- Landed Cost Breakdown (source of truth)
- Offer Strategy (depends on margin)
- Financial Model (uses margin in projections)
- Pricing decisions (across multiple sheets)

**Validation Rule Created:**
```
Rule: Gross Margin Consistency
- Source of Truth: Landed Cost Breakdown (actual data)
- Must Match: Unit Economics, Offer Strategy, Financial Model
- Auto-Check: Compare gross margin % across all sheets
- Trigger: Any change to COGS or pricing must update all sheets
```

**Owner:** Danilo (decision) + Caio (execution)  
**Due:** Within 48 hours (critical blocker)  
**Related:** 
- Decision_Log.md #2026-02-02-001
- Open_Questions.md #Q1
- MASTER_CONTROL.md (Active Discrepancies section)

---

### D2: Traffic Assumption Variance (MEDIUM)

**Status:** NEEDS DATA  
**Severity:** ðŸŸ¡ MEDIUM - affects planning but not critical  
**Discovered:** 2026-02-02 during dependency mapping  

**The Conflict:**
- **Sheet 1:** Market Data - estimates LMNT at 500K visits/month
- **Sheet 2:** Media Buying Plan - assumes 750K visits/month for CPM calculations
- **Gap:** 50% variance (500K vs 750K)

**Details:**
Market Data source: [Need to check - web research? estimate?]
Media Buying source: [Need to check - industry benchmark? assumption?]

**Root Cause:**
- Different research sources
- Different research dates (market growing rapidly)
- No single source of truth designated

**Impact:**
- CPM assumptions in Media Buying may be wrong
- Market share calculations may be off
- Competitive positioning estimates affected
- Not critical but creates uncertainty

**Resolution Options:**
1. **SEMrush verification** (Track B work - paid tool)
2. **Use more conservative estimate** (500K) until verified
3. **Document as range** (500K-750K) with confidence levels

**Resolution Protocol:**
1. [ ] Check what source Market Data used
2. [ ] Check what source Media Buying used
3. [ ] Determine if SEMrush verification needed
4. [ ] If yes: Add to Track B work queue
5. [ ] If no: Use conservative estimate and document assumption
6. [ ] Update both sheets to match
7. [ ] Mark discrepancy as RESOLVED

**Affected Sheets:**
- Market Data (market intelligence)
- Media Buying Plan (CPM assumptions)
- Market share calculations
- Competitive analysis

**Validation Rule Created:**
```
Rule: Traffic/Market Size Consistency
- Source of Truth: Market Data (with confidence levels)
- Must Match: Media Buying assumptions, Market share calcs
- Note: Document confidence level (HIGH if verified, MEDIUM if estimated)
```

**Owner:** Caio (research) + Danilo (prioritization)  
**Due:** Before finalizing Media Buying Plan  
**Priority:** Can proceed with conservative estimate, verify when doing Track B work  
**Related:** Market_Landscape_Bootstrap_Plan.md (Track B work)

---

## ðŸŸ¢ MONITORING (Potential Issues, Not Yet Critical)

### D3: AOV Assumptions Not Yet Validated

**Status:** MONITORING - not yet conflict but watch closely  
**Severity:** ðŸŸ¢ LOW - not critical yet but could become so  

**The Situation:**
Multiple sheets reference Average Order Value (AOV) but Offer Strategy not finalized yet:
- Unit Economics assumes certain AOV for calculations
- Financial Model projects revenue based on AOV
- Media Buying calculates ROAS based on AOV

**Why Not Critical Yet:**
- Offer Strategy is still in development
- Once finalized, will cascade to other sheets
- Currently using placeholder/assumption values

**What to Watch:**
- When Offer Strategy is finalized, must update all sheets
- Potential circular dependency: Offer Strategy needs margin from Unit Econ, Unit Econ needs AOV from Offer
- Resolution: Joint optimization (iterate both together)

**Action Items:**
- [ ] Mark as ACTIVE discrepancy when Offer Strategy near complete
- [ ] Set up joint optimization session for Unit Econ + Offer Strategy
- [ ] Document final AOV in all affected sheets
- [ ] Verify consistency across all sheets

**Affected Sheets:**
- Offer Strategy (determines AOV)
- Unit Economics (uses AOV)
- Financial Model (projects from AOV)
- Media Buying (ROAS calculations)

---

## âœ… RESOLVED DISCREPANCIES (Historical Record)

### D0: Example Template (Never Had Real Conflict)

**Status:** RESOLVED  
**Resolved Date:** 2026-02-02  

**The Conflict:**
[Description of what didn't match]

**Resolution:**
[How it was resolved]

**What Changed:**
[Which sheets were updated]

**Lesson Learned:**
[What process improvement came from this]

---

## DISCREPANCY DETECTION PROTOCOL

### How Claude Should Detect Discrepancies

**During Sheet Analysis:**
1. Note all numerical values and assumptions
2. Check if same value appears in other sheets
3. Compare values - do they match?
4. If mismatch, determine which is "source of truth"
5. Document in this register

**Common Discrepancy Patterns:**
- **Cascade failures:** Upstream value changed, downstream not updated
- **Circular dependencies:** Two sheets each depend on the other
- **Different sources:** Same data point from different research sources
- **Different dates:** Data valid at different times
- **Different assumptions:** Using different scenarios/cases

**What Qualifies as Discrepancy:**
- Same data point shows different values
- Calculations that should match don't
- Assumptions that should align are inconsistent
- Cross-references that should work are broken

**What's NOT a Discrepancy:**
- Different scenarios (Base case vs Upside case)
- Different time periods (Q1 vs Q2)
- Different segments (ICP 1 vs ICP 2)
- Intentional variations

### Quality Consistency Checks

**In addition to numerical discrepancies, also check for quality documentation issues:**

**Confidence Grade Consistency:**
- If Sheet A says data is "verified A-grade", does Sheet B using that data also show A-grade confidence?
- If Sheet A shows "C-grade estimate", are dependent sheets acknowledging the uncertainty?
- Are confidence levels honest or inflated?

**Example discrepancy:**
```
Sheet: Market Data
Claim: "LMNT traffic: 500K visits/month [Confidence: A | Source: SEMrush]"

Sheet: Media Buying Plan
Claim: "LMNT traffic: 500K visits/month [no confidence tag]"

Issue: Media Buying is using the number but not documenting its source/confidence
Resolution: Add confidence tag to Media Buying with reference to Market Data
```

**Methodology Consistency:**
- Is the same metric calculated differently in different sheets?
- Are assumptions documented in one place but missing in another?
- Is the "source of truth" designation clear?

**Example discrepancy:**
```
Sheet: Unit Economics
AOV calculation: Subscription price × subscription rate = $47 × 60% = $28.20

Sheet: Financial Model
AOV used: $35

Issue: Different AOV values, no documentation of which is correct
Resolution: Determine source of truth (probably Offer Strategy), update both sheets
```

**Upgrade Path Conflicts:**
- Does one sheet say "verified and complete" while another says "needs validation"?
- Are gaps documented in one place but ignored in dependent sheets?
- Are upgrade priorities consistent across related deliverables?

**Example discrepancy:**
```
Sheet: Market Intelligence Scorecard
"Customer voice: C-grade, needs 20 more quotes"

Sheet: Creative Strategy (depends on customer voice)
No mention of incomplete customer voice, no caveats on creative angles

Issue: Downstream sheet doesn't acknowledge upstream quality limitation
Resolution: Add note to Creative Strategy flagging that angles are preliminary pending customer voice completion
```

**When Running Discrepancy Scan:**
1. Check numerical values (existing protocol)
2. Check confidence tags match across references
3. Check methodology is documented consistently
4. Check upgrade paths are acknowledged downstream
5. Flag quality issues alongside data issues

---

---

## VALIDATION RULES (Auto-Checks)

### Rule 1: Gross Margin Consistency
**Check:** All sheets using gross margin show same %  
**Source of Truth:** Landed Cost Breakdown  
**Frequency:** Every time COGS or pricing changes  
**Sheets to Check:** Unit Economics, Offer Strategy, Financial Model  
**Current Status:** âŒ VIOLATION - D1 active

### Rule 2: AOV Consistency
**Check:** All sheets using AOV show same value  
**Source of Truth:** Offer Strategy (once finalized)  
**Frequency:** When Offer Strategy finalizes, verify all sheets  
**Sheets to Check:** Unit Economics, Financial Model, Media Buying  
**Current Status:** ðŸŸ¡ NOT YET TESTABLE - Offer Strategy not finalized

### Rule 3: Market Size Consistency
**Check:** Competitor traffic estimates align  
**Source of Truth:** Market Data (with confidence level noted)  
**Frequency:** When new research data arrives  
**Sheets to Check:** Market Data, Market Landscape, Media Buying  
**Current Status:** ðŸŸ¡ VARIANCE DETECTED - D2 active

### Rule 4: ICP Segment Consistency
**Check:** Segments defined in ICP match usage elsewhere  
**Source of Truth:** ICP definitions  
**Frequency:** When creative/GTM references segments  
**Sheets to Check:** ICP, Creative Strategy, Email Segmentation, Media Buying  
**Current Status:** âšª NOT YET TESTABLE - ICP not finalized

---

## RESOLUTION PROCESS

### When New Discrepancy Found:

1. **Document Immediately:**
   - Add to Active Discrepancies section
   - Assign severity (Critical/High/Medium/Low)
   - Detail the conflict clearly

2. **Determine Source of Truth:**
   - Which sheet has "real" data?
   - Which is assumption vs verified?
   - Document the logic

3. **Assess Impact:**
   - What's affected?
   - Is it blocking work?
   - What's the priority?

4. **Create Resolution Protocol:**
   - Clear steps to resolve
   - Owner assigned
   - Timeline set

5. **Update Related Docs:**
   - Flag in MASTER_CONTROL.md if critical
   - Add to Open_Questions.md if decision needed
   - Note in Decision_Log.md when resolved

### When Discrepancy Resolved:

1. **Update All Affected Sheets**
2. **Verify with Cross-Check**
3. **Document Resolution:**
   - What was decided
   - What changed
   - Lesson learned
4. **Move to Resolved Section** (don't delete)
5. **Create/Update Validation Rule** to prevent recurrence
6. **Update MASTER_CONTROL.md** status

---

## DISCREPANCY TEMPLATE

```markdown
### D#: [Discrepancy Title]

**Status:** [ACTIVE | IN RESOLUTION | NEEDS DATA | RESOLVED]  
**Severity:** [ðŸ”´ CRITICAL | ðŸŸ¡ MEDIUM | ðŸŸ¢ LOW]  
**Discovered:** [Date and context]

**The Conflict:**
- **Sheet 1:** [Name] - [Value/Assumption]
- **Sheet 2:** [Name] - [Different Value/Assumption]
- **Gap:** [Description of mismatch]

**Details:**
[Specific numbers, cells, or data points]

**Root Cause:**
[Why did this happen?]

**Impact:**
[What's affected? How serious?]

**Resolution Options:**
1. [Option 1]
2. [Option 2]

**Resolution Protocol:**
- [ ] [Step 1]
- [ ] [Step 2]
- [ ] [Step 3]

**Affected Sheets:**
[List all sheets that reference this data]

**Validation Rule:**
[What rule should prevent this in future?]

**Owner:** [Who's responsible]  
**Due:** [Timeline]  
**Related:** [Links to other docs]
```

---

**Last Updated:** 2026-02-02 by Claude  
**Next Review:** When D1 and D2 resolved
