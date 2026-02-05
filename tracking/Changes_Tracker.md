# IonWave Changes Tracker

**Purpose:** Document what changed, when, and why - version control for the operations model  
**Maintenance:** Claude logs significant changes  
**Usage:** Track evolution, understand decisions, prevent confusion

---

## 2026-02-02: Tracking System Implementation

**Change Type:** SYSTEM  
**Changed By:** Claude + Caio  

**What Changed:**
Created comprehensive tracking system for IonWave operations model:
- MASTER_CONTROL.md (navigation and orchestration)
- Decision_Log.md (decision history)
- Open_Questions.md (active questions)
- Discrepancy_Register.md (cross-sheet conflicts)
- Execution_Status.md (progress tracking)
- Changes_Tracker.md (this file)

**Why:**
The v10 model has 681 sheets (planned 842 with P-IP-V structure). Without scaffolding:
- Impossible to navigate effectively
- No way to track dependencies
- No system for detecting conflicts
- Decisions get lost in chat history
- Can't tell what's blocking what

**Impact:**
- Operators can now navigate systematically
- Claude can maintain decision history
- Cross-sheet conflicts surfaced automatically
- Order of operations clear
- Blocker visibility immediate

**Related:**
- See MASTER_CONTROL.md for full system overview
- All tracking files in `/mnt/project/ionwave-tracking/`

---

## 2026-02-02: Gross Margin Discrepancy Discovered

**Change Type:** ISSUE IDENTIFIED  
**Changed By:** Claude during bootstrap analysis  

**What Changed:**
Discovered critical conflict:
- Unit Economics assumes 70% gross margin
- Landed Cost Breakdown calculates 40% gross margin
- 30 percentage point gap affects entire financial model

**Why This Matters:**
- Blocks Unit Economics finalization
- Blocks Offer Strategy development
- Blocks Financial Model
- May affect Trade viability

**Status:** IN RESOLUTION  
**Owner:** Danilo (decision needed)  
**Timeline:** 48 hours  

**Related:**
- Discrepancy_Register.md #D1
- Decision_Log.md #2026-02-02-001
- Open_Questions.md #Q1

---

## CHANGE LOG TEMPLATE

```markdown
## YYYY-MM-DD: [Change Title]

**Change Type:** [CONTENT | STRUCTURE | SYSTEM | DECISION | ISSUE IDENTIFIED]  
**Changed By:** [Who made the change]

**What Changed:**
[Specific description of what's different]

**Why:**
[Rationale for the change]

**Impact:**
[What's affected? What does this enable/prevent?]

**Related:**
[Links to decisions, issues, other docs]
```

---

## CHANGE TYPES

**CONTENT:**
- Updates to deliverable content
- New analysis or research
- Data refresh
- Quality improvements

**STRUCTURE:**
- Sheet reorganization
- Model restructuring
- File splitting/consolidation
- Navigation changes

**SYSTEM:**
- Process changes
- Workflow updates
- Tool additions
- Protocol modifications

**DECISION:**
- Strategic decisions made
- Direction changes
- Pivot points
- Resource allocation

**ISSUE IDENTIFIED:**
- Problems discovered
- Conflicts found
- Blockers identified
- Risks surfaced

---

## MAINTENANCE NOTES

**When to Log Changes:**
- Significant content updates (not minor typos)
- Any structural reorganization
- Decisions that affect direction
- Issues that block progress
- System or process changes

**When NOT to Log:**
- Minor formatting tweaks
- Typo corrections
- Chat summaries
- Routine updates captured elsewhere

**Cross-References:**
- Link to Decision_Log when decisions drive changes
- Link to Discrepancy_Register when issues found
- Link to Open_Questions when questions arise

---

**Last Updated:** 2026-02-02 by Claude  
**Next Entry:** When significant change occurs
