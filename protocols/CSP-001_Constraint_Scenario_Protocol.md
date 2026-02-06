# Constraint Scenario Protocol (CSP-001)

**Version**: 1.0.0
**Type**: Meta-Control Protocol (MC-002)
**Author**: Caio, Claude (collaborative)
**Date Created**: 2026-02-06
**Last Updated**: 2026-02-06
**AI Model**: claude-sonnet-4-5-20250929
**Purpose**: Systematic stress-testing of hypotheses through extreme constraint scenarios to surface hidden assumptions, decompose into sub-hypotheses, and improve composite confidence scoring
**Status**: Active
**Trigger**: Periodic (quarterly) or Event (new hypothesis created, hypothesis grade drops, pre-validation planning)
**Owner Role**: Meta Standards Officer (MSO) or Operator

---

## Overview

The Constraint Scenario Protocol (CSP) is a diagnostic methodology that applies extreme constraints to hypotheses to reveal hidden assumptions, expose missing hypotheses, and decompose monolithic hypotheses into testable sub-components. It operates on the hypothesis system itself — making it a Meta-Control Protocol.

**Core Insight**: Imposing an extreme constraint on a hypothesis forces you to derive the *necessary conditions* for that hypothesis to hold. Those necessary conditions are either (a) hidden assumptions that should be explicit sub-hypotheses, or (b) missing capabilities that the plan needs to address.

---

## When to Run This Protocol

| Trigger | Context | Urgency |
|---------|---------|---------|
| **New hypothesis created** | Run CSP on any new HYP entry to decompose before it calcifies | Within 1 session |
| **Hypothesis grade drops** | A downgrade (e.g., C→D) signals the hypothesis needs deeper examination | Next session |
| **Pre-validation planning** | Before spending money to validate, stress-test to ensure you're validating the right thing | Before capital deployment |
| **Quarterly review** | Systematic pass through all ASSUMED/TESTING hypotheses | Scheduled |
| **Strategic pivot signal** | External event changes assumptions (market shift, competitor move, regulation) | Immediate |

---

## Protocol Steps

### STEP 1: Select Target Hypothesis

**Input**: Hypothesis registry (`data/hypotheses/registry.json`)

**Selection Criteria** (priority order):
1. **Primitive hypotheses first** — those with `depends_on: []` (they have no upstream to blame)
2. **Lowest grade** — D-grade hypotheses have the most hidden assumptions
3. **Highest impact severity** — CRITICAL > HIGH > MEDIUM > LOW
4. **Most constraint scenario coverage** — hypotheses touched by the most scenarios (see Scenario Library)

**Output**: Selected `HYP-XXX` with rationale for selection

**Decision Rule**: When multiple candidates exist, prefer the hypothesis that is both *primitive* and *low-grade* — these are the foundations where hidden assumptions do the most damage.

---

### STEP 2: Identify Applicable Constraint Scenarios

**Input**: Scenario Library (see Section: Scenario Library below), selected hypothesis

**Process**:
1. Read each constraint scenario's extreme condition
2. Ask: "Does this constraint create tension with the target hypothesis?"
3. A scenario applies if the constraint would force the hypothesis to *work differently* or *not work at all*

**Tension Test**: For each scenario, fill in this sentence:
> "If [CONSTRAINT], then [HYPOTHESIS] would need to [WHAT CHANGES?]"

If you can fill in the sentence, the scenario applies. If the hypothesis is unaffected by the constraint, skip that scenario.

**Output**: List of applicable scenarios ranked by tension severity (HIGH/MEDIUM/LOW)

---

### STEP 3: Apply Each Scenario — The Three-Question Drill

For each applicable scenario, work through three questions in order:

#### Question 1: "What would have to be true?"

Derive the *necessary conditions* for the hypothesis to survive under the constraint. These are not strategies — they are logical requirements.

**Method**: Work backwards from the hypothesis value. If the hypothesis says "10% organic lift" and the constraint is "$0 marketing budget," then what conditions must hold for 10% organic to exist at all?

**Output**: List of 3-7 necessary conditions

#### Question 2: "How could it possibly work?"

Now generate *specific mechanisms* — concrete strategies or tactics that could create those conditions. These must be actionable, not aspirational.

**Method**: For each necessary condition from Q1, generate at least one concrete mechanism. If you can't generate a mechanism, the condition is *currently unaddressed* — flag it.

**Output**: List of mechanisms mapped to conditions. Unaddressed conditions flagged.

#### Question 3: "What does this reveal?"

Extract the diagnostic insights. What did this scenario expose about the hypothesis that wasn't visible before?

**Method**: Compare the necessary conditions (Q1) and mechanisms (Q2) against what the hypothesis currently assumes. Look for:
- **Hidden assumptions** — conditions the hypothesis takes for granted
- **Missing capabilities** — mechanisms that don't exist yet but would need to
- **Relationship surprises** — dependencies on other hypotheses you didn't expect
- **Timing dependencies** — sequencing that the flat hypothesis hides
- **Framing problems** — the hypothesis is asking the wrong question

**Output**: List of diagnostic findings, categorized by type

---

### STEP 4: Synthesize Across Scenarios

After applying all scenarios, look for patterns across the diagnostic findings:

**Cross-Scenario Analysis**:
1. **Recurring conditions** — if the same necessary condition appears under multiple scenarios, it's a *structural dependency* (likely a sub-hypothesis)
2. **Contradictions** — if two scenarios require opposite conditions, the hypothesis contains unresolved tension
3. **Convergence** — if multiple scenarios reveal the same gap, that gap is *critical*

**Output**: Consolidated diagnostic summary with findings ranked by frequency and severity

---

### STEP 5: Decompose into Sub-Hypotheses

Based on the consolidated diagnostics, decompose the target hypothesis into sub-hypotheses.

**Decomposition Rules**:

1. **Each sub-hypothesis must be independently testable** — if you can't imagine a validation method, it's not a hypothesis, it's a wish
2. **Sub-hypotheses must be exhaustive** — together they must account for the parent hypothesis value
3. **Sub-hypotheses should be as independent as possible** — minimize overlap between what each one claims
4. **Naming convention**: `HYP-XXX.Y` (e.g., HYP-006.1, HYP-006.2, HYP-006.3)
5. **Nesting is allowed**: `HYP-XXX.Y.Z` for sub-sub-hypotheses (arbitrarily nestable)

**Sub-Hypothesis Schema** (extends parent schema):

```json
{
  "id": "HYP-006.1",
  "name": "Referral Program Contribution",
  "parent_id": "HYP-006",
  "category": "growth",
  "description": "Referral program will contribute 3-4% of total customer volume",
  "weight": 0.35,
  "impact_severity": "MEDIUM",
  "current_state": "ASSUMED",
  "current_grade": "D",
  "revisions": [],
  "validation_plan": {},
  "feeds_into": [],
  "depends_on": [],
  "risk_if_wrong": {},
  "constraint_scenario_origin": "CSP-001 applied to HYP-006, Scenario 3 ($0 Marketing Budget)",
  "decomposition_rationale": "Referral is a distinct mechanism from SEO, influencer, and PR — requires its own program design, incentive structure, and measurement"
}
```

**Key fields added to sub-hypothesis schema**:
- `parent_id` — links to parent hypothesis
- `weight` — contribution to parent composite score (all weights must sum to 1.0)
- `constraint_scenario_origin` — which CSP run created this sub-hypothesis
- `decomposition_rationale` — why this is a separate sub-hypothesis and not part of the parent

**Output**: Array of sub-hypotheses with weights, registered in hypothesis system

---

### STEP 6: Compute Composite Score

The parent hypothesis score becomes a *weighted composite* of its sub-hypothesis scores.

**Composite Scoring Rules**:

```
Parent Grade = weighted_composite(sub_hypothesis_grades)

Where:
  A = 4, B = 3, C = 2, D = 1

  Composite Score = Σ(weight_i × grade_score_i)

  Score → Grade:
    3.5 - 4.0 → A
    2.5 - 3.4 → B
    1.5 - 2.4 → C
    1.0 - 1.4 → D
```

**Weak Link Rule**: The composite score CANNOT exceed the grade of the highest-weighted sub-hypothesis if that sub-hypothesis is D-grade. Rationale: a critical component at D undermines the whole.

**Example**:
```
HYP-006 Organic & Referral Lift (parent)
├── HYP-006.1 Referral Program (weight: 0.35, grade: D) = 0.35
├── HYP-006.2 SEO & Content (weight: 0.25, grade: D) = 0.25
├── HYP-006.3 Influencer Seeding (weight: 0.20, grade: D) = 0.20
├── HYP-006.4 PR & Earned Media (weight: 0.10, grade: D) = 0.10
└── HYP-006.5 Community & WOM (weight: 0.10, grade: D) = 0.10

Composite = (0.35×1) + (0.25×1) + (0.20×1) + (0.10×1) + (0.10×1) = 1.0 → Grade D

After validation of referral program:
├── HYP-006.1 Referral Program (weight: 0.35, grade: B) = 1.05
├── HYP-006.2 SEO & Content (weight: 0.25, grade: C) = 0.50
├── HYP-006.3 Influencer Seeding (weight: 0.20, grade: D) = 0.20
├── HYP-006.4 PR & Earned Media (weight: 0.10, grade: D) = 0.10
└── HYP-006.5 Community & WOM (weight: 0.10, grade: C) = 0.20

Composite = 1.05 + 0.50 + 0.20 + 0.10 + 0.20 = 2.05 → Grade C
```

**Output**: Updated parent hypothesis grade, decomposition documented in revision

---

### STEP 7: Surface New Hypotheses

The constraint scenario process often reveals *entirely new hypotheses* that don't decompose from the target but are newly discovered dependencies.

**Detection Criteria**: A new hypothesis is warranted when:
1. A necessary condition from Step 3 isn't covered by ANY existing hypothesis or sub-hypothesis
2. The condition is testable (not a wish)
3. The condition has material impact on the business model

**Process**:
1. Review all unaddressed conditions from Step 3 (Q2)
2. Review all "framing problems" from Step 3 (Q3)
3. For each candidate, check: does an existing hypothesis cover this? (Check registry)
4. If no → create new hypothesis following standard creation protocol (Hypotheses Architecture Standards, "Adding a New Hypothesis")

**Output**: List of new hypotheses to create (with IDs, descriptions, and evidence from the CSP run)

---

### STEP 8: Update Relationship Graph

The decomposition and new hypothesis discovery may change the dependency graph.

**Updates Required**:
1. **Parent ↔ Sub links**: Parent `has_children: ["HYP-006.1", ...]`, children `parent_id: "HYP-006"`
2. **New dependency edges**: If the CSP revealed that HYP-006 depends on a new HYP-009, add `depends_on` link
3. **Reframed relationships**: If the CSP revealed that the relationship between two existing hypotheses should be reconceived (e.g., "mitigation" → "portfolio diversification"), update `related_hypotheses`

**Output**: Updated dependency graph in registry

---

### STEP 9: Document the Run

Every CSP execution is logged as a process document for institutional memory.

**Document Format**: `protocols/case_studies/CSP-001_HYP-XXX_[date].md`

**Required Sections**:
1. Target hypothesis and selection rationale
2. Applicable scenarios and tension ratings
3. Three-Question Drill results per scenario
4. Cross-scenario synthesis
5. Sub-hypothesis decomposition table
6. Composite score calculation
7. New hypotheses surfaced
8. Relationship graph changes
9. Recommendations and next steps

**Output**: Archived case study document

---

### STEP 10: Update Registry and Close

Apply all changes to the hypothesis system:

1. Add sub-hypotheses to `registry.json`
2. Update parent hypothesis with `has_children`, new composite grade, and revision entry documenting the decomposition
3. Create new hypotheses in registry
4. Update `index.json` with bidirectional links
5. Log all events in `validation_log.json`
6. Update `_meta` counts

**Validation Log Event Type**: `CONSTRAINT_SCENARIO_APPLIED`

```json
{
  "entry_id": "LOG-XXX",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ",
  "event_type": "CONSTRAINT_SCENARIO_APPLIED",
  "hypothesis_id": "HYP-006",
  "actor": "Session YYYY-MM-DD #N",
  "description": "CSP-001 applied: decomposed into 5 sub-hypotheses, surfaced 1 new hypothesis (HYP-009)",
  "scenarios_applied": ["Scenario 2", "Scenario 3", "Scenario 4"],
  "sub_hypotheses_created": ["HYP-006.1", "HYP-006.2", "HYP-006.3", "HYP-006.4", "HYP-006.5"],
  "new_hypotheses_created": ["HYP-009"],
  "composite_grade_before": "D",
  "composite_grade_after": "D",
  "notes": "Grade unchanged but now decomposed into independently testable components"
}
```

---

## Scenario Library

The Scenario Library is a collection of extreme constraints to apply. New scenarios can be added through Meta-Control.

### Current Scenarios

| ID | Scenario | Constraint | Primary Tension |
|----|----------|-----------|-----------------|
| SC-01 | $100M Revenue in 12 Months | Scale 1000x in 12 months | Tests scalability assumptions |
| SC-02 | $100K MRR in 3 Months | 4x speed compression | Tests speed assumptions and dependencies |
| SC-03 | $0 Marketing Budget | Remove all paid channels | Tests organic viability and resilience |
| SC-04 | 10 Hours/Week from Day 1 | Extreme time constraint | Tests automation and delegation assumptions |

### Adding New Scenarios

Any scenario that imposes a *single extreme constraint* while leaving all other variables free is a valid scenario. Good scenarios:
- Are specific enough to analyze (not "what if everything goes wrong")
- Impose a single constraint (not multiple simultaneous constraints)
- Create productive tension (not just "everything breaks")
- Reveal something non-obvious when analyzed

**Scenario Schema**:
```json
{
  "id": "SC-XX",
  "name": "Descriptive Name",
  "constraint": "The specific extreme condition",
  "primary_tension": "What category of assumptions does this stress?",
  "three_questions": {
    "what_would_have_to_be_true": [],
    "how_could_it_possibly_work": [],
    "what_does_this_reveal": []
  },
  "added_by": "Session ID",
  "date_added": "YYYY-MM-DD"
}
```

---

## Protocol Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                  CONSTRAINT SCENARIO PROTOCOL                    │
│                         (CSP-001)                                │
└─────────────────────────────────────────────────────────────────┘

Step 1: SELECT TARGET
  │  Input: Hypothesis Registry
  │  Rule: Primitive + Low-grade + High-impact
  ▼
Step 2: IDENTIFY SCENARIOS
  │  Input: Scenario Library
  │  Test: "If [CONSTRAINT], then [HYPOTHESIS] needs to [WHAT?]"
  ▼
Step 3: THREE-QUESTION DRILL (per scenario)
  │  Q1: What would have to be true?     → Necessary Conditions
  │  Q2: How could it possibly work?     → Mechanisms (or gaps)
  │  Q3: What does this reveal?          → Diagnostic Findings
  ▼
Step 4: SYNTHESIZE ACROSS SCENARIOS
  │  Look for: Recurring conditions, contradictions, convergence
  ▼
Step 5: DECOMPOSE INTO SUB-HYPOTHESES
  │  Rule: Independently testable, exhaustive, minimal overlap
  │  Output: HYP-XXX.1, HYP-XXX.2, ... with weights
  ▼
Step 6: COMPUTE COMPOSITE SCORE
  │  Formula: Σ(weight_i × grade_score_i)
  │  Weak Link Rule: Can't exceed critical D-grade component
  ▼
Step 7: SURFACE NEW HYPOTHESES
  │  Test: Unaddressed conditions not covered by any existing HYP
  ▼
Step 8: UPDATE RELATIONSHIP GRAPH
  │  Add: parent↔child links, new dependencies, reframed relationships
  ▼
Step 9: DOCUMENT THE RUN
  │  Output: Case study in protocols/case_studies/
  ▼
Step 10: UPDATE REGISTRY AND CLOSE
     Output: Updated registry, index, validation log
```

---

## Relationship to Other Protocols

- **Hypotheses Architecture Standards** (`standards/Hypotheses_Architecture_Standards.md`) — CSP produces inputs to the hypothesis system. Sub-hypotheses follow the same schema. Composite scoring extends the existing grading system.
- **Systems Architecture Standards** (`standards/Systems_Architecture_Standards.md`) — CSP is a Meta-Control Protocol (MC-002). It operates on the hypothesis system itself, not on business operations directly.
- **Validation Planning** — CSP should run BEFORE validation spending. A decomposed hypothesis tells you *what specifically* to validate, preventing wasted capital on broad tests.

---

## Version History

**v1.0.0 (2026-02-06)**:
- Initial protocol definition
- 10-step process formalized
- Scenario Library with 4 scenarios from Danilo's ops model v10
- Sub-hypothesis schema with composite scoring
- Case study format defined
- Flow diagram added

---

**For reference case study, see**: `protocols/case_studies/CSP-001_HYP-006_2026-02-06.md`
