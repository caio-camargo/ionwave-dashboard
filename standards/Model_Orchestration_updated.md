# Model Orchestration Protocol

**Purpose:** How to work systematically across IonWave's 681+ sheet operations model  
**Audience:** Anyone working on IonWave (Danilo, Caio, future Operators, Claude)  
**Status:** Living document - update as workflow evolves

---

## THE CORE PROBLEM

**Without orchestration:**
- 681 sheets (842 with P-IP-V) is cognitively overwhelming
- Easy to miss dependencies
- Changes cascade unpredictably
- Conflicts hide in plain sight
- Decisions get lost
- Can't tell what's blocking what

**With orchestration:**
- Clear entry points and navigation
- Explicit dependencies mapped
- Conflicts surface automatically
- Decisions documented with context
- Blocker visibility immediate
- Order of operations clear

---

## THE ORCHESTRATION SYSTEM

### Navigation Layer
**MASTER_CONTROL.md** - Start here every session
- Order of operations (what to do first)
- Dependency map (what blocks what)
- Active conflicts (what needs resolution)
- Blocker summary (what's stuck)
- Next actions (critical path)

### Tracking Layer
**Decision_Log.md** - Decision history with full context  
**Open_Questions.md** - Questions needing resolution  
**Discrepancy_Register.md** - Cross-sheet conflicts  
**Execution_Status.md** - Progress dashboard  
**Changes_Tracker.md** - Version control / change log

### Model Layer
**IonWave_Ops_Model_v10_Organized.xlsx** - The actual business content
- (Future: Split into domain-specific workbooks)
- (Future: P-IP-V structure for each of 44 models)

---

## WORKING PATTERNS

### Pattern 1: Starting a Work Session

**Every session, follow this sequence:**

1. **Read MASTER_CONTROL.md** (5 min)
   - What's the current state?
   - What's blocking?
   - What's the critical path?

2. **Check relevant tracking files** (3 min)
   - Open_Questions.md - any decisions needed?
   - Discrepancy_Register.md - any conflicts affecting my work?
   - Execution_Status.md - what's the status of my work area?

3. **Work on content** (focus time)
   - Open relevant sheets in operations model
   - Make progress on deliverables
   - Note questions, conflicts, decisions as they arise

4. **Update tracking** (5 min at end)
   - Log any decisions in Decision_Log.md
   - Add any questions to Open_Questions.md
   - Flag any conflicts in Discrepancy_Register.md
   - Update status in Execution_Status.md
   - Update MASTER_CONTROL.md if critical path changed

**Total overhead: ~13 min per session for massive clarity gain**

---

### Pattern 2: When Making a Decision

**Never make a significant decision without documenting it:**

1. **Before deciding:**
   - Check Open_Questions.md - is this already a tracked question?
   - Check Discrepancy_Register.md - does this resolve a conflict?
   - Check MASTER_CONTROL.md dependencies - what's affected?

2. **Document the decision:**
   - Add to Decision_Log.md with full context:
     - What situation prompted this?
     - What options were considered?
     - What was decided and why?
     - What's the impact?
     - What needs to change?

3. **Update related tracking:**
   - If this resolves a question â†’ update Open_Questions.md status
   - If this resolves a conflict â†’ update Discrepancy_Register.md
   - If this unblocks work â†’ update Execution_Status.md
   - If this changes critical path â†’ update MASTER_CONTROL.md

4. **Execute the decision:**
   - Update all affected sheets
   - Verify changes with cross-checks
   - Confirm no new conflicts created

**Example Decision Flow:**

```
SITUATION: Need to decide on gross margin target

1. CHECK TRACKING:
   - Open_Questions.md #Q1 already tracking this
   - Discrepancy_Register.md #D1 showing conflict
   - MASTER_CONTROL shows this blocks Unit Economics

2. MAKE DECISION:
   - Danilo decides: Accept 40% margin reality
   - Rationale: Based on actual supplier data, more conservative

3. DOCUMENT:
   - Decision_Log.md #2026-02-02-003: "Accept 40% Gross Margin"
   - Full context, rationale, impact documented

4. UPDATE TRACKING:
   - Open_Questions.md #Q1 â†’ RESOLVED
   - Discrepancy_Register.md #D1 â†’ IN RESOLUTION (updating sheets)
   - Execution_Status.md â†’ Unit Economics unblocked

5. EXECUTE:
   - Update Unit Economics sheet (70% â†’ 40%)
   - Update Offer Strategy sheet (adjust for margin)
   - Update Financial Model (recalc projections)
   - Verify: All sheets now show 40% consistently

6. VERIFY & CLOSE:
   - Cross-check all sheets updated
   - Discrepancy_Register.md #D1 â†’ RESOLVED
   - Execution_Status.md â†’ Unit Economics âœ… COMPLETE
   - MASTER_CONTROL.md â†’ Remove from critical blockers
```

---

### Pattern 3: When Finding a Conflict

**Don't ignore conflicts - surface them immediately:**

1. **Detect the conflict:**
   - Notice same data point shows different values
   - Or: calculations that should match don't
   - Or: assumptions that should align are inconsistent

2. **Document in Discrepancy_Register.md:**
   - Describe the conflict clearly
   - Identify which sheets/values conflict
   - Assess severity (Critical/High/Medium/Low)
   - Determine "source of truth"

3. **Assess impact:**
   - What work is this blocking?
   - How urgent is resolution?
   - Does this need immediate decision?

4. **Update related tracking:**
   - If blocks critical work â†’ flag in MASTER_CONTROL.md
   - If needs decision â†’ add to Open_Questions.md
   - If affects schedule â†’ update Execution_Status.md

5. **Don't proceed if critical:**
   - Critical conflicts = STOP work in affected area
   - Resolve before continuing
   - Otherwise: cascade problems multiply

**Example Conflict Flow:**

```
SITUATION: Discover margin mismatch between sheets

1. DETECT:
   - Unit Economics shows 70% margin
   - Landed Cost shows 40% margin
   - 30 point gap = CRITICAL conflict

2. DOCUMENT:
   - Discrepancy_Register.md #D1: "Gross Margin Mismatch"
   - Detail: 70% vs 40%, affects pricing/strategy
   - Severity: ðŸ”´ CRITICAL
   - Source of truth: Landed Cost (actual supplier data)

3. ASSESS IMPACT:
   - Blocks: Unit Economics, Offer Strategy, Financial Model
   - Urgency: Must resolve within 48 hours
   - Needs: Danilo decision on path forward

4. UPDATE TRACKING:
   - MASTER_CONTROL.md â†’ Add to Active Discrepancies
   - Open_Questions.md #Q1 â†’ "Accept 40% or pursue 70%?"
   - Execution_Status.md â†’ Mark affected work as ðŸ”´ BLOCKED

5. ESCALATE:
   - Flag to Danilo in session
   - Present options (accept, negotiate, price up)
   - Get decision before proceeding
```

---

### Pattern 4: When Opening Any Sheet/Model

**Future state (with P-IP-V structure):**

Opening M09 (Unit Economics model) should follow this sequence:

1. **Check MASTER_CONTROL.md** (30 sec)
   - Is this in the right order of operations?
   - Any blockers affecting this model?
   - Any active discrepancies?

2. **Read P-M09 (Planning tab)** (2-3 min)
   - What's the vision for this model?
   - What novel concepts need understanding?
   - What dependencies exist?
   - What questions are open?

3. **Read IP-M09 (Industry Perspectives)** (3-5 min)
   - What's current industry state?
   - What's best-in-class?
   - What's our contrarian take?
   - What research gaps exist?

4. **Work on content tabs** (focus time)
   - Actually build/update the model
   - Reference P- and IP- tabs for context
   - Note new questions or issues

5. **Update V-M09 (Verification)** (5 min)
   - Per-tab verification checklist
   - Trust assignments
   - Note unverified claims

6. **Update tracking files** (3 min)
   - Any decisions? â†’ Decision_Log.md
   - Any questions? â†’ Open_Questions.md
   - Any conflicts? â†’ Discrepancy_Register.md
   - Status change? â†’ Execution_Status.md

**Current state (without P-IP-V yet):**

Opening "Unit Economics" sheet:

1. **Check MASTER_CONTROL.md** - blockers? dependencies?
2. **Work on sheet** - make updates
3. **Cross-check** - does this conflict with other sheets?
4. **Update tracking** - log changes/decisions/questions

---

### Pattern 5: Cross-Model Validation

**When finalizing any deliverable, check for conflicts:**

1. **Identify related sheets/models:**
   - What other sheets use data from this one?
   - What sheets does this one depend on?

2. **Run validation rules:**
   - Check MASTER_CONTROL.md validation rules section
   - Compare key values (margin, AOV, traffic, etc.)
   - Verify calculations match

3. **Document if conflicts found:**
   - Add to Discrepancy_Register.md immediately
   - Don't proceed if critical

4. **Get sign-off:**
   - V- tab (verification) should be complete
   - Owner should review and approve
   - Mark as âœ… COMPLETE only after validation

**Example Validation Flow:**

```
DELIVERABLE: Unit Economics sheet finalized

1. IDENTIFY RELATED:
   - Depends on: Landed Cost Breakdown (COGS input)
   - Feeds into: Offer Strategy (margin constraints)
   - Feeds into: Financial Model (revenue projections)

2. RUN CHECKS:
   - Gross margin matches Landed Cost? âœ… YES (40%)
   - AOV assumption aligns with Offer? âš ï¸ NEEDS CHECK
   - CAC target realistic per Media? âœ… YES ($28)

3. DOCUMENT ISSUES:
   - AOV not yet finalized in Offer Strategy
   - Add to Discrepancy_Register.md #D3 (monitoring)
   - Flag: When Offer complete, verify AOV matches

4. SIGN-OFF:
   - Verify numbers with Danilo
   - Update V-M09 verification checklist
   - Mark as ðŸŸ¢ COMPLETE (NEEDS REVIEW) until Offer Strategy done
   - Once Offer Strategy finalizes AOV â†’ revalidate â†’ âœ… COMPLETE
```

### Pattern 6: Deliverable Production (Inline Quality Documentation)

**Every deliverable follows this three-phase structure with inline quality tracking:**

#### PHASE 1: RESEARCH
**Collect data and tag confidence as you go:**

1. **Gather from available sources:**
   - Use web search, project knowledge, document analysis
   - Tag every claim inline: `[Confidence: A/B/C/D | Source: URL | Date]`
   - Don't let blocked sources stall work - mark D-grade and continue
   
2. **Document methodology for estimates:**
   - Show your math
   - State assumptions explicitly
   - Note "could be wrong if" scenarios
   
3. **Track gaps immediately:**
   - Note what you couldn't find
   - Assess strategic importance
   - Draft validation path

**Research complete when:** All target sections have SOMETHING (even if D-grade), gaps are documented

---

#### PHASE 2: ANALYSIS
**Apply frameworks and check consistency:**

1. **Run relevant frameworks:**
   - Competitive: Porter's Five Forces, positioning analysis
   - Financial: Benchmark comparison, anomaly detection
   - Strategic: Response scenarios, defensibility windows
   - Tag analysis: `[Analysis: Claude | Framework: X | Validated: pending]`

2. **Check internal consistency:**
   - Do estimates tell a coherent story?
   - Any mathematical impossibilities?
   - Does customer voice support strategic claims?

3. **Check external benchmarks:**
   - Compare estimates to industry norms
   - Flag anomalies (>2x deviation)
   - Assess: exploitable weakness or data issue?

4. **Identify unresolved tensions:**
   - Where do frameworks disagree?
   - What gaps would change conclusions?
   - What requires human judgment?

**Analysis complete when:** Frameworks applied, consistency checked, tensions documented

---

#### PHASE 3: ASSEMBLY
**Structure output with three mandatory sections:**

**Section 1: Main Content (Estimates & Analysis)**
- Every factual claim has confidence tag
- Every estimate shows methodology
- Strategic notes for key insights
- Cross-references to dependencies

**Section 2: Intelligence Gaps**
For each gap:
```
**Gap [N]: [Title]**
- What We Estimate: [current best guess with grade]
- Why This Matters: [strategic importance]
- Impact If Wrong: [optimistic & pessimistic scenarios]
- How to Validate: [specific actionable steps with timeline]
- Can We Proceed Without Knowing: [yes/no/caveats]
```
Prioritize by: (impact if wrong) × (probability we're wrong)

**Section 3: Scorecard**
```
## Confidence Overview
| Section | Grade | Key Limitation |
|---------|-------|----------------|
| Product Profile | B | Revenue estimate from proxy |
| Pricing | A | Verified from official source |
| Customer Voice | C | Only 12 quotes, need more depth |
| **Overall** | **B-** | |

## Top Strategic Implications
1. [Most important takeaway]
2. [Second most important]
3. [Third]

## Upgrade Shopping List (Prioritized)
| Priority | Task | Time | Outcome |
|----------|------|------|---------|
| 1 | Pull SEMrush traffic for competitor.com | 15 min | Traffic: C → A |
| 2 | Collect 20 more customer quotes | 3 hrs | Voice: C → B+ |
| 3 | Verify partnership claim via LinkedIn | 30 min | Profile: B → A |
```

**Assembly complete when:** All three sections present, grades documented, shopping list prioritized

---

#### PHASE 4: SELF-GRADE
**Quality gate before delivery:**

**Pre-delivery checklist:**
- [ ] All factual claims have confidence tags
- [ ] All estimates show methodology
- [ ] All B/C/D grades have upgrade paths (specific, time-estimated, actionable)
- [ ] Scorecard grades match actual content (no optimistic inflation)
- [ ] Strategic implications are concrete and useful
- [ ] Gaps are prioritized by impact
- [ ] Cross-references to dependent deliverables are noted
- [ ] Any new discrepancies flagged in Discrepancy Register

**Grade dimensions:**
1. Evidence coverage (found something for every section?)
2. Confidence honesty (grades match source quality?)
3. Upgrade path quality (actionable vs vague?)
4. Scorecard accuracy (matches reality?)
5. Strategic value (useful for decisions?)

**Key principle:** Protocol grade is about PROCESS quality, not data quality. A D-grade deliverable (all guesses) can be A-grade protocol if every guess is labeled, has upgrade path, and scorecard is honest.

---

**Example Application:**

```
DELIVERABLE: Competitive Intel on Seaonic

PHASE 1 - RESEARCH:
- Pricing: $75/box [A - seaonic.com - 2026-01-31]
- Revenue: $2-5M est [D - no sources found, category size proxy]
- Customer voice: 8 quotes collected [C - need 20+ for B-grade]
- Methodology documented for revenue estimate
- Gap: Traffic data blocked, market share unknown

PHASE 2 - ANALYSIS:
- Porter's applied: High threat of substitutes (LMNT cheaper)
- Benchmark check: $2.50/serving is 2.5x LMNT (premium confirmed)
- Anomaly: Very high price with low market presence (niche strategy?)
- Tension: Claims mass appeal but pricing suggests luxury

PHASE 3 - ASSEMBLY:
- Main content: 3 sections with inline tags
- Intelligence Gaps: 4 gaps documented with validation paths
- Scorecard: Overall C+, upgrade priority = traffic verification

PHASE 4 - SELF-GRADE:
- Evidence: 4/5 (missing traffic, rest covered)
- Honesty: 5/5 (D-grade honestly marked)
- Upgrade paths: 4/5 (mostly specific, 1 vague)
- Scorecard: 5/5 (matches content)
- Strategic value: 4/5 (good positioning insights)
- Overall: B+ protocol grade (honest C+ deliverable)
```

---

---

## SPECIAL WORKFLOWS

### Circular Dependency Resolution

**Situation:** Two models depend on each other (Unit Econ â†â†’ Offer Strategy)

**Protocol:**
1. **Recognize the circular dependency:**
   - Unit Economics needs AOV from Offer Strategy
   - Offer Strategy needs margin from Unit Economics

2. **Start with assumptions:**
   - Begin with best-guess assumptions in one model
   - Document as "ASSUMPTION - pending validation"

3. **Iterate to convergence:**
   - Build Offer Strategy based on Unit Econ assumptions
   - Check if Offer achieves assumed AOV
   - If no: Adjust either Unit Econ assumptions OR Offer design
   - Repeat until both models align

4. **Joint optimization session:**
   - Work on both models simultaneously
   - Test multiple scenarios
   - Find sweet spot where both work

5. **Verify and lock:**
   - Once converged, verify both models
   - Document final values in both
   - Mark dependency as resolved in MASTER_CONTROL.md

---

### Cascade Change Management

**Situation:** Change in upstream model affects downstream models

**Protocol:**
1. **Identify cascade path:**
   - Check MASTER_CONTROL.md dependency map
   - List all downstream dependencies

2. **Assess impact:**
   - How significant is the upstream change?
   - Which downstream models need updates?
   - What's the effort to cascade?

3. **Execute in sequence:**
   - Update immediate dependents first
   - Then second-order dependents
   - Then third-order

4. **Verify at each step:**
   - Check calculations after each update
   - Confirm no new conflicts created
   - Cross-reference validation rules

5. **Document cascade:**
   - Log in Changes_Tracker.md
   - Note: "Changed X, cascaded to Y, Z, W"
   - Update Execution_Status.md for all affected

**Example Cascade:**

```
CHANGE: Landed Cost COGS increases $12 â†’ $14

CASCADE PATH:
1. Landed Cost â†’ Unit Economics (margin drops 40% â†’ 35%)
2. Unit Economics â†’ Offer Strategy (need higher price OR volume)
3. Offer Strategy â†’ Financial Model (revenue projections change)
4. Financial Model â†’ Scenario Planning (all scenarios shift)

EXECUTION:
- Update Unit Economics: Recalc with $14 COGS
- Update Offer Strategy: Adjust pricing strategy
- Update Financial Model: Rerun projections
- Update Scenario Planning: Refresh scenarios
- Verify: All models now consistent at $14 COGS
- Document: Changes_Tracker.md #2026-02-XX
```

---

## ANTI-PATTERNS (What NOT to Do)

### âŒ Working Without Checking MASTER_CONTROL
**Problem:** Miss critical blockers or dependencies  
**Result:** Wasted work on something that's blocked or wrong

### âŒ Making Decisions Without Logging
**Problem:** Decisions get lost, can't remember rationale later  
**Result:** Rework, confusion, conflicting directions

### âŒ Ignoring Discrepancies
**Problem:** Conflicts compound, cascade downstream  
**Result:** Major rework needed, trust in model decreases

### âŒ Updating Sheets Without Cross-Checking
**Problem:** Create new conflicts while fixing old ones  
**Result:** Whack-a-mole with discrepancies

### âŒ Proceeding While Blocked
**Problem:** Build on wrong foundation  
**Result:** Entire work stream may need rebuilding

### âŒ Not Updating Tracking Files
**Problem:** System falls out of sync, loses value  
**Result:** Orchestration system becomes useless

---

## SUCCESS PATTERNS (What TO Do)

### âœ… Start Every Session with MASTER_CONTROL
**Why:** Situational awareness before diving in  
**Result:** Work on right things in right order

### âœ… Question-Driven Work
**Why:** Clarify before assuming  
**Result:** Fewer false starts, better first drafts

### âœ… Document as You Go
**Why:** Capture decisions in real-time with context  
**Result:** Clear decision trail, no lost rationale

### âœ… Surface Conflicts Immediately
**Why:** Small conflicts â†’ big problems if ignored  
**Result:** Clean, trustworthy model

### âœ… Cross-Check Before Finalizing
**Why:** Catch issues before they cascade  
**Result:** Fewer downstream problems

### âœ… Update Tracking Consistently
**Why:** System only works if maintained  
**Result:** Always-accurate view of status

---

## WORKFLOW CHOREOGRAPHY

### Human â†’ Claude Handoff

**When human does data collection (Track B work):**

1. **Human Phase:**
   - Execute data collection tasks
   - Document in sheets
   - Note any questions or issues

2. **Handoff to Claude:**
   - Upload updated workbook
   - Point to specific sheets updated
   - Share any context or questions

3. **Claude Phase:**
   - Analyze updated data
   - Apply expert frameworks
   - Cross-check with other sheets
   - Flag any discrepancies
   - Generate insights
   - Update tracking files
   - Present findings

4. **Validation Phase:**
   - Human reviews Claude's analysis
   - Validates patterns and insights
   - Makes decisions on open questions
   - Approves or requests iteration

5. **Iteration:**
   - If gaps remain: More data OR different analysis
   - If complete: Mark deliverable done
   - Update Execution_Status.md

---

## MAINTENANCE CADENCE

### Daily (If Active Work)
- Update Execution_Status.md as work progresses
- Log decisions immediately in Decision_Log.md
- Flag conflicts in Discrepancy_Register.md as found

### Weekly (Regular Review)
- Review Open_Questions.md - anything resolved?
- Review Discrepancy_Register.md - progress on conflicts?
- Update MASTER_CONTROL.md - critical path changed?
- Scan Changes_Tracker.md - anything need attention?

### Monthly (Deep Review)
- Validate tracking system still serving needs
- Refine workflows based on what's working
- Update orchestration protocol based on learnings
- Archive resolved items if getting cluttered

---

## TOOLS & TECHNIQUES

### For Claude

**When analyzing sheets:**
1. Load specific sheets (not entire 681-sheet workbook)
2. Note all numerical assumptions
3. Flag when values appear in multiple sheets
4. Check if values match or conflict
5. Document in Discrepancy_Register if conflict

**When updating tracking:**
1. Read existing file first (don't overwrite)
2. Append to Decision_Log (never delete entries)
3. Update status in Open_Questions and Discrepancy_Register
4. Maintain consistent formatting
5. Cross-reference between tracking files

**When providing analysis:**
1. Reference MASTER_CONTROL for context
2. Check Open_Questions for active decisions
3. Note any new conflicts discovered
4. Update Execution_Status with progress
5. Suggest next actions on critical path

---

## GETTING STARTED

### First-Time Setup (One-Time)

1. **Read all tracking files** (20 min)
   - Understand current state
   - See what's already documented
   - Learn the formats

2. **Review MASTER_CONTROL** (15 min)
   - Understand order of operations
   - See dependency map
   - Note active blockers

3. **Familiarize with key sheets** (30 min)
   - Open a few high-priority sheets
   - See what data exists
   - Understand structure

4. **Practice workflow** (try one deliverable)
   - Follow the patterns above
   - Update tracking files
   - Get comfortable with system

### Ongoing Use

**Before each session:**
- Read MASTER_CONTROL.md (5 min)
- Check relevant tracking (3 min)

**During session:**
- Work on content
- Note issues as arise

**After session:**
- Update tracking (5 min)
- Update MASTER_CONTROL if needed (2 min)

**Total overhead: ~15 min per session for massive coordination benefit**

---

## EVOLUTION

This orchestration system should evolve based on use:

**What works?**
- Keep and reinforce
- Document as pattern
- Train others on it

**What doesn't?**
- Identify friction points
- Propose improvements
- Test alternatives

**What's missing?**
- Add new tracking files as needed
- Create new workflows for special cases
- Refine protocols based on learnings

**Document evolution in Changes_Tracker.md**

---

**Last Updated:** 2026-02-02 by Claude  
**Status:** v1.0 - Initial orchestration protocol  
**Next Review:** After first full use cycle (1-2 weeks)
