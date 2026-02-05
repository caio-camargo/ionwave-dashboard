# Hypotheses Architecture Standards
**Version**: v1.0.0
**Author**: Caio, Claude (collaborative)
**Date Created**: 2026-02-05
**Last Updated**: 2026-02-05
**AI Model**: claude-sonnet-4-20250514
**Purpose**: Document the hypotheses architecture system - how to add, update, validate, and maintain business hypotheses as ontological primitives
**Status**: Final
**Related Files**: data/hypotheses/registry.json, data/hypotheses/index.json, data/hypotheses/validation_log.json, IonWave/Hypothesis_Dependency_Audit.md

---

## Overview

The Hypotheses Architecture treats business assumptions as **ontological primitives** - first-class entities with full lifecycle tracking, validation status, confidence grading, and dependency relationships. This system enables transparent weak link detection and systematic validation planning.

**Core Principle**: Every business assumption must be tracked as a hypothesis with explicit confidence grading, evidence trails, and validation plans.

---

## Architecture Components

### 1. Registry (`data/hypotheses/registry.json`)
**Purpose**: Central registry of all business hypotheses with full revision history

**Schema**:
```json
{
  "schema_version": "1.0.0",
  "last_updated": "YYYY-MM-DD",
  "hypotheses": [
    {
      "id": "HYP-XXX",
      "name": "Descriptive Name",
      "category": "economics|operations|market|product|growth",
      "description": "What this hypothesis states",
      "impact_severity": "CRITICAL|HIGH|MEDIUM|LOW",
      "current_state": "ASSUMED|TESTING|VALIDATED|INVALIDATED|RETIRED",
      "current_grade": "A|B|C|D",
      "revisions": [
        {
          "version": 1,
          "date": "YYYY-MM-DD",
          "value": "The specific value or claim",
          "confidence_grade": "A|B|C|D",
          "reasoning": "Why this value, what evidence supports it",
          "evidence": ["List of supporting sources"],
          "updated_by": "Name or session ID"
        }
      ],
      "validation_plan": {
        "method": "How to test this hypothesis",
        "cost": "Estimated cost to validate",
        "timeline": "Expected validation timeframe",
        "success_criteria": "What constitutes validation"
      },
      "feeds_into": ["HYP-XXX", "HYP-YYY"],
      "depends_on": ["HYP-ZZZ"],
      "risk_if_wrong": "Impact description if hypothesis is invalidated"
    }
  ],
  "metadata": {
    "total_hypotheses": 8,
    "by_state": {},
    "by_grade": {},
    "by_severity": {}
  }
}
```

### 2. Index (`data/hypotheses/index.json`)
**Purpose**: Bidirectional linking between hypotheses and supporting documents

**Schema**:
```json
{
  "schema_version": "1.0.x",
  "hypothesis_to_documents": {
    "HYP-XXX": {
      "hypothesis_name": "Name",
      "reference_count": 5,
      "referenced_in": [
        {
          "document": "path/to/file.md",
          "section": "Section name",
          "context": "How this document relates to the hypothesis",
          "relevance": "PRIMARY|SUPPORTING|RELATED|CONTEXT"
        }
      ]
    }
  },
  "document_to_hypotheses": {
    "path/to/file.md": {
      "hypotheses_referenced": ["HYP-001", "HYP-002"],
      "document_type": "ANALYSIS|RESEARCH|DATA|TRACKING|CONTEXT",
      "primary_purpose": "Brief description",
      "confidence_contribution": "How this document affects hypothesis confidence"
    }
  },
  "context_documents": {
    "description": "Documents providing reasoning and background",
    "documents": []
  },
  "metadata": {
    "total_hypotheses": 8,
    "total_documents": 13,
    "total_references": 53
  }
}
```

### 3. Validation Log (`data/hypotheses/validation_log.json`)
**Purpose**: Chronological event log of all hypothesis lifecycle events

**Schema**:
```json
{
  "schema_version": "1.0.0",
  "log_entries": [
    {
      "entry_id": "LOG-XXX",
      "timestamp": "YYYY-MM-DDTHH:MM:SSZ",
      "event_type": "HYPOTHESIS_CREATED|HYPOTHESIS_REVISED|STATE_CHANGED|VALIDATION_STARTED|VALIDATION_COMPLETED|ARCHITECTURE_ESTABLISHED",
      "hypothesis_id": "HYP-XXX",
      "actor": "Name or session ID",
      "description": "What happened",
      "state_change": {
        "from": "OLD_STATE",
        "to": "NEW_STATE"
      },
      "confidence_grade": "A|B|C|D",
      "supporting_evidence": ["List of evidence"],
      "document_refs": ["path/to/file.md"],
      "notes": "Additional context"
    }
  ],
  "metadata": {
    "total_entries": 11,
    "hypotheses_tracked": 8,
    "event_types": {}
  }
}
```

---

## State Machine

Hypotheses progress through a defined lifecycle:

```
ASSUMED → TESTING → VALIDATED
                 ↘ INVALIDATED → RETIRED
```

### State Definitions

**ASSUMED** (Initial State)
- Hypothesis established based on benchmarks, research, or expert judgment
- Not yet empirically tested with IonWave-specific data
- Confidence grade typically C or D
- **Transition to TESTING**: When validation activities begin (e.g., launch, first customers, testing campaign)

**TESTING**
- Active validation in progress
- Collecting empirical data from operations, customers, or experiments
- Confidence grade may improve as data accumulates
- **Transition to VALIDATED**: Success criteria met consistently
- **Transition to INVALIDATED**: Evidence contradicts hypothesis

**VALIDATED**
- Empirically confirmed with IonWave-specific data
- Confidence grade typically A or B
- Hypothesis proven correct within stated parameters
- Continue monitoring for degradation
- **Transition to INVALIDATED**: New evidence contradicts validation

**INVALIDATED**
- Empirical evidence contradicts hypothesis
- Requires revision of dependent hypotheses
- Document lessons learned
- **Transition to RETIRED**: No longer relevant to business
- **Transition to ASSUMED**: Revised hypothesis replaces invalidated one (new HYP-ID)

**RETIRED**
- No longer relevant to current business model
- Hypothesis archived for historical reference
- Cannot transition to other states (permanent)
- Keep in registry with RETIRED status for audit trail

---

## Confidence Grading System

All hypotheses use A/B/C/D grading to indicate evidence quality:

### Grade Definitions

**A - Verified from Authoritative Source**
- IonWave-specific empirical data (actual customers, actual operations)
- Directly measured, not inferred
- Sample size sufficient for confidence intervals
- Example: "CAC = $32 (±$3) from 100 customer acquisitions over 3 months"

**B - Strong Single Source or Good Triangulation**
- Multiple independent data points converge on same value
- Strong proxy data (e.g., LMNT customer behavior as proxy for IonWave)
- Structural analysis with validated assumptions
- Example: "Gross margin 67% validated across 3 competitor pricing structures"

**C - Industry Benchmark with Documented Methodology**
- Category benchmarks with transparent methodology
- Single credible source without triangulation
- Reasonable inference from validated data
- Example: "CAC $30-45 based on SaaS freemium benchmarks, adjusted for supplements"

**D - Best Guess with Documented Upgrade Path**
- Educated assumption without direct validation
- Speculative but reasoned estimate
- Wide range reflects uncertainty
- Example: "Monthly churn 12% (range 8-15%) based on SMB SaaS benchmarks, not supplement-specific"

### Grade Requirements by State

- **ASSUMED**: Typically C or D grades (benchmarks, research)
- **TESTING**: C or D grades improving toward B as data accumulates
- **VALIDATED**: A or B grades (empirical confirmation required)
- **INVALIDATED**: Any grade (evidence contradicts hypothesis)
- **RETIRED**: Retain final grade for historical reference

---

## Adding a New Hypothesis

### Step 1: Assign Hypothesis ID
Format: `HYP-XXX` where XXX is zero-padded sequential number (HYP-001, HYP-002, etc.)

Check `data/hypotheses/registry.json` metadata for `total_hypotheses` count, then increment.

### Step 2: Create Registry Entry

Add to `registry.json` hypotheses array:

```json
{
  "id": "HYP-009",
  "name": "Average Order Value (AOV)",
  "category": "economics",
  "description": "Average revenue per order before subscription conversion",
  "impact_severity": "MEDIUM",
  "current_state": "ASSUMED",
  "current_grade": "D",
  "revisions": [
    {
      "version": 1,
      "date": "2026-02-05",
      "value": "$45 (range $35-55)",
      "confidence_grade": "D",
      "reasoning": "Estimated from Seaonic pricing ($1.79/serving × 30 servings = $53.70) and LMNT starter pack pricing ($45). No IonWave-specific data yet.",
      "evidence": [
        "Seaonic 30-serving pouch: $53.70",
        "LMNT 30-stick sample pack: $45",
        "Category analysis from Marine_Plasma_Market_Sizing.md"
      ],
      "updated_by": "Session 2026-02-05 #4"
    }
  ],
  "validation_plan": {
    "method": "Track first 50 orders, calculate mean and standard deviation",
    "cost": "Free (operational data)",
    "timeline": "Month 1-2 (first 50 orders)",
    "success_criteria": "AOV within $35-55 range with 95% confidence"
  },
  "feeds_into": ["HYP-005"],
  "depends_on": [],
  "risk_if_wrong": "If AOV is lower than $35, unit economics degrade significantly (lower LTV). If higher than $55, may price out target customers."
}
```

### Step 3: Update Index

Add to `index.json` hypothesis_to_documents:

```json
"HYP-009": {
  "hypothesis_name": "Average Order Value (AOV)",
  "reference_count": 1,
  "referenced_in": [
    {
      "document": "IonWave/Marine_Plasma_Market_Sizing.md",
      "section": "Seaonic Competitive Intel - Pricing",
      "context": "Seaonic pricing structure used as AOV benchmark",
      "relevance": "SUPPORTING"
    }
  ]
}
```

Add to existing documents in document_to_hypotheses:

```json
"IonWave/Marine_Plasma_Market_Sizing.md": {
  "hypotheses_referenced": ["HYP-001", "HYP-002", "HYP-004", "HYP-007", "HYP-008", "HYP-009"],
  "document_type": "RESEARCH",
  "primary_purpose": "Size marine plasma DTC sachet segment, estimate Seaonic revenue, validate TAM assumptions",
  "confidence_contribution": "Reframes market opportunity; validates margin and AOV assumptions; challenges timeline"
}
```

### Step 4: Log Creation Event

Add to `validation_log.json` log_entries array:

```json
{
  "entry_id": "LOG-012",
  "timestamp": "2026-02-05T14:30:00Z",
  "event_type": "HYPOTHESIS_CREATED",
  "hypothesis_id": "HYP-009",
  "actor": "Session 2026-02-05 #4",
  "description": "Average Order Value hypothesis established from competitor pricing analysis",
  "state_change": {
    "from": null,
    "to": "ASSUMED"
  },
  "confidence_grade": "D",
  "supporting_evidence": [
    "Seaonic pricing: $53.70 for 30 servings",
    "LMNT pricing: $45 for 30-stick sample pack"
  ],
  "document_refs": ["IonWave/Marine_Plasma_Market_Sizing.md"],
  "notes": "MEDIUM severity - impacts LTV calculation but not critical path. Validation via first 50 orders."
}
```

### Step 5: Update Metadata

Increment counts in all three files:
- `registry.json` → `metadata.total_hypotheses`
- `index.json` → `metadata.total_hypotheses`
- `validation_log.json` → `metadata.total_entries`, `metadata.hypotheses_tracked`

---

## Updating a Hypothesis (Adding a Revision)

When new evidence emerges or analysis refines a hypothesis:

### Step 1: Add Revision to Registry

Append to `revisions` array in `registry.json`:

```json
{
  "version": 2,
  "date": "2026-02-15",
  "value": "$42 (±$4, 95% CI)",
  "confidence_grade": "B",
  "reasoning": "First 50 orders: mean $42.30, std dev $8.15. Range $35-55 validated. Upgraded from D to B based on empirical data.",
  "evidence": [
    "50 orders tracked in Month 1-2",
    "Mean AOV: $42.30, Std Dev: $8.15",
    "95% CI: $38-46"
  ],
  "updated_by": "Session 2026-02-15 #1"
}
```

Update `current_grade` if changed:
```json
"current_grade": "B"
```

### Step 2: Log Revision Event

Add to `validation_log.json`:

```json
{
  "entry_id": "LOG-025",
  "timestamp": "2026-02-15T10:00:00Z",
  "event_type": "HYPOTHESIS_REVISED",
  "hypothesis_id": "HYP-009",
  "actor": "Session 2026-02-15 #1",
  "description": "AOV hypothesis upgraded from D to B based on 50 actual orders",
  "state_change": {
    "from": "ASSUMED",
    "to": "ASSUMED"
  },
  "confidence_grade": "B",
  "revision_details": {
    "what_changed": "Value refined to $42 (±$4) from estimated $45 (range $35-55)",
    "why_changed": "50 orders of empirical data replaced benchmark estimates",
    "impact": "Confidence upgraded D→B; range narrowed significantly"
  },
  "supporting_evidence": [
    "50 orders tracked, mean $42.30",
    "95% confidence interval: $38-46"
  ],
  "document_refs": ["tracking/Revenue_Metrics_Log.md"]
}
```

### Step 3: Update Index (if new documents)

If the revision is based on a new document, add it to `index.json`:

```json
"referenced_in": [
  {
    "document": "IonWave/Marine_Plasma_Market_Sizing.md",
    "section": "Seaonic Competitive Intel - Pricing",
    "context": "Seaonic pricing structure used as AOV benchmark",
    "relevance": "SUPPORTING"
  },
  {
    "document": "tracking/Revenue_Metrics_Log.md",
    "section": "Month 1-2 AOV Analysis",
    "context": "First 50 orders empirical data upgraded confidence to B",
    "relevance": "PRIMARY"
  }
]
```

---

## Changing Hypothesis State

When a hypothesis transitions through the state machine:

### Example: ASSUMED → TESTING

When validation activities begin:

**Step 1**: Update `current_state` in `registry.json`:
```json
"current_state": "TESTING"
```

**Step 2**: Log state change in `validation_log.json`:
```json
{
  "entry_id": "LOG-013",
  "timestamp": "2026-02-10T09:00:00Z",
  "event_type": "STATE_CHANGED",
  "hypothesis_id": "HYP-001",
  "actor": "Session 2026-02-10 #1",
  "description": "CAC hypothesis transitioned to TESTING as first ad campaigns launched",
  "state_change": {
    "from": "ASSUMED",
    "to": "TESTING"
  },
  "confidence_grade": "C",
  "supporting_evidence": [
    "Launched Meta ad campaign #1 with $500 budget",
    "Tracking pixel installed, attribution configured"
  ],
  "document_refs": ["tracking/Marketing_Campaign_Log.md"],
  "notes": "Testing will run for 30 days, targeting 15-20 acquisitions to validate CAC range"
}
```

### Example: TESTING → VALIDATED

When success criteria are met:

**Step 1**: Update state AND add validation revision in `registry.json`:
```json
"current_state": "VALIDATED",
"current_grade": "A",
"revisions": [
  // ... previous revisions ...
  {
    "version": 3,
    "date": "2026-03-15",
    "value": "$34 (±$3, 95% CI)",
    "confidence_grade": "A",
    "reasoning": "CAC validated over 100 acquisitions across 3 campaigns. Mean $34.20, range $28-41. Hypothesis confirmed within predicted $30-45 range. Upgraded to A-grade.",
    "evidence": [
      "100 acquisitions tracked over 45 days",
      "3 independent campaigns: Meta ($35 CAC), Google ($32 CAC), organic ($28 CAC implied)",
      "Blended CAC: $34.20 (±$3)"
    ],
    "updated_by": "Session 2026-03-15 #2"
  }
]
```

**Step 2**: Log validation in `validation_log.json`:
```json
{
  "entry_id": "LOG-040",
  "timestamp": "2026-03-15T16:00:00Z",
  "event_type": "VALIDATION_COMPLETED",
  "hypothesis_id": "HYP-001",
  "actor": "Session 2026-03-15 #2",
  "description": "CAC hypothesis VALIDATED - 100 acquisitions confirm $34 (±$3) within predicted range",
  "state_change": {
    "from": "TESTING",
    "to": "VALIDATED"
  },
  "confidence_grade": "A",
  "supporting_evidence": [
    "100 acquisitions across 3 campaigns",
    "Meta: $35, Google: $32, Organic implied: $28",
    "Blended: $34.20, 95% CI: $31-37"
  ],
  "document_refs": ["tracking/Marketing_Campaign_Log.md", "IonWave/CAC_Validation_Report.md"],
  "notes": "CRITICAL hypothesis validated. Original range $30-45 confirmed. This de-risks capital planning significantly."
}
```

### Example: TESTING → INVALIDATED

When evidence contradicts hypothesis:

**Step 1**: Update state and add invalidation revision:
```json
"current_state": "INVALIDATED",
"current_grade": "A",  // High confidence that it's WRONG
"revisions": [
  // ... previous revisions ...
  {
    "version": 3,
    "date": "2026-03-15",
    "value": "$65 (±$8, 95% CI) - INVALIDATED",
    "confidence_grade": "A",
    "reasoning": "CAC hypothesis INVALIDATED. Actual CAC $65 is 86% higher than predicted $35. Original range $30-45 was too optimistic. Root cause: CPMs higher than benchmarked ($80 vs. $60 expected) + lower CTR (0.8% vs. 1.5% assumed).",
    "evidence": [
      "100 acquisitions tracked: mean CAC $65, range $55-78",
      "Meta CPMs: $80 (vs. $60 benchmarked)",
      "CTR: 0.8% (vs. 1.5% assumed)"
    ],
    "updated_by": "Session 2026-03-15 #2"
  }
]
```

**Step 2**: Log invalidation:
```json
{
  "entry_id": "LOG-040",
  "timestamp": "2026-03-15T16:00:00Z",
  "event_type": "VALIDATION_COMPLETED",
  "hypothesis_id": "HYP-001",
  "actor": "Session 2026-03-15 #2",
  "description": "CAC hypothesis INVALIDATED - actual $65 CAC is 86% above predicted $35",
  "state_change": {
    "from": "TESTING",
    "to": "INVALIDATED"
  },
  "confidence_grade": "A",
  "supporting_evidence": [
    "100 acquisitions: mean $65, range $55-78",
    "Root causes: CPMs $80 vs. $60 expected, CTR 0.8% vs. 1.5% assumed"
  ],
  "document_refs": ["tracking/Marketing_Campaign_Log.md", "IonWave/CAC_Postmortem_Analysis.md"],
  "notes": "CRITICAL hypothesis invalidated. Requires immediate revision of HYP-007 (Timeline), HYP-008 (Capital). Original financial model assumptions no longer valid."
}
```

**Step 3**: Flag dependent hypotheses for review:
- Add notes to HYP-007 (Timeline) and HYP-008 (Capital) that HYP-001 invalidation affects them
- Create new hypothesis HYP-001-REV with corrected CAC estimate

---

## Retiring a Hypothesis

When a hypothesis is no longer relevant (e.g., business model pivot):

**Step 1**: Update state to RETIRED in `registry.json`:
```json
"current_state": "RETIRED",
"revisions": [
  // ... all previous revisions ...
  {
    "version": 4,
    "date": "2026-06-01",
    "value": "N/A - RETIRED",
    "confidence_grade": "N/A",
    "reasoning": "Business model pivoted from freemium to paid-only. Free-to-subscription conversion rate no longer relevant. Hypothesis retired, not invalidated - it may have been correct but is no longer applicable.",
    "evidence": ["Strategic pivot documented in Strategy_Revision_v2.md"],
    "updated_by": "Session 2026-06-01 #1"
  }
]
```

**Step 2**: Log retirement:
```json
{
  "entry_id": "LOG-078",
  "timestamp": "2026-06-01T10:00:00Z",
  "event_type": "STATE_CHANGED",
  "hypothesis_id": "HYP-002",
  "actor": "Session 2026-06-01 #1",
  "description": "Free-to-subscription conversion hypothesis RETIRED due to business model pivot to paid-only",
  "state_change": {
    "from": "ASSUMED",
    "to": "RETIRED"
  },
  "confidence_grade": "N/A",
  "supporting_evidence": ["Strategic pivot to paid-only model - freemium discontinued"],
  "document_refs": ["IonWave/Strategy_Revision_v2.md"],
  "notes": "Hypothesis remains in registry for historical reference. Not invalidated - simply no longer applicable to current business model."
}
```

**Note**: Do NOT delete retired hypotheses from registry. Keep them for audit trail and historical context.

---

## Integration Requirements

### Mandatory for Analysis Documents

**REQUIRED**: All analysis deliverables (document_type: ANALYSIS or RESEARCH) MUST include hypothesis metadata.

#### In Markdown Files

Add to document frontmatter or metadata section:

```markdown
# Strategic Foundation Analysis v1.2.0
**Hypotheses Referenced**: HYP-001, HYP-004, HYP-007, HYP-008

[... document content ...]
```

#### In JSON Files

Add to `_meta` envelope:

```json
{
  "_meta": {
    "data_type": "narrative",
    "quality_score": "7/10",
    "status": "complete",
    "version": "1.2.0",
    "hypotheses_referenced": ["HYP-001", "HYP-004", "HYP-007", "HYP-008"],
    "confidence_contributions": {
      "HYP-001": "Identifies CAC tension; provides structural evidence for CAC inflation",
      "HYP-004": "Validates margin assumptions through supplier analysis"
    }
  }
}
```

### Updating the Index

When creating/updating analysis documents, update `data/hypotheses/index.json`:

**Step 1**: Add document to hypothesis_to_documents for each referenced hypothesis

**Step 2**: Add document to document_to_hypotheses with metadata

**Step 3**: Increment `metadata.total_documents` and `metadata.total_references`

### Non-Mandatory Cases

Hypothesis metadata is **optional** for:
- TRACKING documents (live logs, not versioned analyses)
- CONTEXT documents (dialogue summaries, meeting notes)
- Process documentation
- Standards and guidelines

---

## Month 1-2 Validation Guidance

Early validation is critical for de-risking the business model. Focus on CRITICAL and HIGH severity hypotheses with D or C grades.

### Priority 1: HYP-001 (CAC) - CRITICAL, Grade C

**Validation Method**: Track first 3 paid acquisition campaigns

**Metrics to Track**:
- Total ad spend per campaign
- Total acquired customers per campaign
- Blended CAC across all campaigns
- CAC by channel (Meta, Google, etc.)

**Success Criteria**:
- CAC falls within $30-45 range
- Sample size ≥30 acquisitions for statistical validity
- 95% confidence interval width <$10

**Go Decision**: CAC ≤$40 → proceed with planned budget
**No-Go Decision**: CAC >$50 → pause, revise financial model, consider pivot

**Testing Budget**: $3,000 (Month 1-2)
- Campaign 1: $1,000 Meta ads
- Campaign 2: $1,000 Google search
- Campaign 3: $1,000 influencer/affiliate test

**Documentation**: Log all campaigns in `tracking/Marketing_Campaign_Log.md` with:
- Campaign ID, channel, budget, impressions, clicks, conversions
- Calculated CAC per campaign
- Aggregate blended CAC

### Priority 2: HYP-003 (Monthly Churn) - HIGH, Grade D

**Validation Method**: Track first cohort retention for 3 months

**Metrics to Track**:
- Monthly subscription retention rate
- Churn rate by month (Month 1, Month 2, Month 3)
- Churn reasons (cancellation surveys)
- Reactivation rate

**Success Criteria**:
- Monthly churn ≤15% (invalidates hypothesis if >15%)
- Cohort size ≥20 subscribers for meaningful signal
- Churn reasons identified for product iteration

**Go Decision**: Churn ≤12% → LTV assumptions hold
**Caution**: Churn 12-15% → LTV lower than expected, monitor closely
**No-Go Decision**: Churn >15% → LTV economics break, major revision needed

**Testing Timeline**: Month 2-5 (need 3 full months of retention data)

**Documentation**: Log in `tracking/Subscription_Retention_Log.md`:
- Cohort start date, initial size
- Monthly retention counts
- Calculated churn rates
- Customer feedback on why they canceled

### Priority 3: HYP-005 (Blended LTV) - CRITICAL, Grade D

**Validation Method**: Calculate from HYP-003 (Churn) + HYP-004 (Margin) + actual ARPU

**Note**: This is a **composite hypothesis** - validate HYP-003 and HYP-004 first, then recalculate LTV.

**Formula**:
```
Blended LTV = (Monthly ARPU × Gross Margin) / Monthly Churn Rate
```

**Metrics to Track**:
- Actual monthly ARPU (average across all subscription tiers)
- Actual gross margin (validated from first 100 orders)
- Validated monthly churn rate (from HYP-003)

**Success Criteria**:
- LTV falls within $64-159 range predicted in financial model
- LTV:CAC ratio ≥3.0 (sustainable unit economics)

**Go Decision**: LTV:CAC ≥3.0 → unit economics validated
**Caution**: LTV:CAC 2.0-3.0 → marginal, requires capital efficiency
**No-Go Decision**: LTV:CAC <2.0 → unsustainable, major pivot required

**Testing Timeline**: Month 5-6 (after HYP-003 validation completes)

**Documentation**: Create `IonWave/LTV_Validation_Report.md` synthesizing:
- Validated ARPU, margin, churn inputs
- Calculated LTV with confidence intervals
- LTV:CAC ratio analysis
- Comparison to original financial model assumptions

### Priority 4: HYP-002 (Conversion Rate) - HIGH, Grade C

**Validation Method**: Track free-to-paid and paid-to-subscription conversion

**Metrics to Track**:
- Free samples distributed
- Free → paid conversion rate
- Paid → subscription conversion rate
- Time-to-conversion distribution

**Success Criteria**:
- Paid → subscription ≥40% (validates hypothesis if ≥50%)
- Sample size ≥50 paid customers for statistical validity

**Testing Timeline**: Month 2-4

**Documentation**: Log in `tracking/Conversion_Funnel_Log.md`

---

## Dependency Chain Management

Some hypotheses depend on others - track these relationships explicitly.

### Example: HYP-005 (LTV) depends on HYP-003 (Churn) + HYP-004 (Margin)

**In Registry**:
```json
{
  "id": "HYP-005",
  "name": "Blended LTV",
  "depends_on": ["HYP-003", "HYP-004"],
  "feeds_into": ["HYP-007", "HYP-008"]
}
```

**Implications**:
- Cannot validate HYP-005 until HYP-003 and HYP-004 are validated
- If HYP-003 or HYP-004 are invalidated, HYP-005 must be recalculated
- Changes to HYP-005 propagate to HYP-007 (Timeline) and HYP-008 (Capital)

### Chain of Weak Links

If a hypothesis depends on D-grade inputs, it cannot exceed D-grade confidence:

```
HYP-003 (Churn) = D grade
HYP-004 (Margin) = B grade
→ HYP-005 (LTV) = MAX(D, B) = D grade
```

Document this in the hypothesis:
```json
"reasoning": "LTV is composite of Churn (D-grade) and Margin (B-grade). Confidence limited by weakest link (churn uncertainty). Upgrading LTV requires first upgrading HYP-003."
```

---

## Dashboard Integration

The hypotheses tracker dashboard auto-renders from JSON files. No manual updates needed.

**Dashboard Location**: https://caio-camargo.github.io/ionwave-dashboard/views/hypotheses-tracker.html

**Features**:
- Color-coded confidence grades (A/B/C/D)
- Impact severity badges (CRITICAL/HIGH/MEDIUM/LOW)
- State indicators (ASSUMED/TESTING/VALIDATED/INVALIDATED/RETIRED)
- Filtering by severity, grade, state
- Full revision history display
- Dependency visualization
- Validation plans
- Risk assessments

**Auto-updates**: Dashboard reads from `data/hypotheses/registry.json` and `index.json` - just commit and push changes to GitHub to update the live dashboard.

---

## Quality Control Checklist

Before committing hypothesis changes, verify:

- [ ] Hypothesis ID is unique and sequential (check metadata.total_hypotheses)
- [ ] All required fields populated (id, name, category, description, impact_severity, current_state, current_grade)
- [ ] Revision includes: version, date, value, confidence_grade, reasoning, evidence, updated_by
- [ ] Confidence grade matches evidence quality (D = best guess, C = benchmark, B = triangulated, A = empirical)
- [ ] State matches lifecycle position (new hypotheses = ASSUMED)
- [ ] Validation plan includes: method, cost, timeline, success_criteria
- [ ] Dependencies documented if hypothesis is composite or feeds into others
- [ ] Risk_if_wrong describes actual business impact
- [ ] Index updated with bidirectional linking (hypothesis ↔ documents)
- [ ] Validation log entry created with proper event_type
- [ ] Metadata counts updated in all three files
- [ ] Related analysis documents include hypotheses_referenced metadata

---

## Examples from Current System

### Example 1: Well-Documented Hypothesis (HYP-004 - Gross Margin)

**Why B-grade**:
- Multiple independent validation sources (competitive intel, supplier research)
- Narrow range (65-70%) across all sources
- Structural constraints identified (supplier power limits expansion)

**Evidence Trail**:
- 6 document references (PRIMARY, SUPPORTING, RELATED)
- Includes data files, analysis docs, and competitive research
- Each reference explains HOW it supports the hypothesis

### Example 2: Weak Link Hypothesis (HYP-003 - Churn)

**Why D-grade**:
- Speculative assumption (SaaS benchmarks, not supplement-specific)
- Wide range (8-15%) reflects uncertainty
- No IonWave-specific data yet

**Validation Priority**: HIGH (feeds into CRITICAL hypothesis HYP-005)

**Upgrade Path**: Track first cohort for 3 months, upgrade to B-grade with N≥20

### Example 3: Composite Hypothesis (HYP-005 - LTV)

**Why D-grade**:
- Depends on HYP-003 (Churn, D-grade) and HYP-004 (Margin, B-grade)
- Cannot exceed confidence of weakest dependency
- Formula-driven: LTV = f(Churn, Margin, ARPU)

**Validation Approach**: Validate dependencies first, then recalculate

---

## Maintenance Cadence

### Weekly (During Active Testing)
- Update validation log with new testing data
- Add revisions to hypotheses as evidence accumulates
- Update confidence grades if warranted by new data

### Monthly (Ongoing Operations)
- Review all TESTING hypotheses for state transitions
- Check if success criteria met → transition to VALIDATED or INVALIDATED
- Audit dependency chains for consistency

### Quarterly (Strategic Review)
- Review all hypotheses for relevance to current business model
- Retire hypotheses that are no longer applicable
- Add new hypotheses as business evolves
- Update index with new document references

### As Needed (Major Events)
- Invalidation of CRITICAL hypothesis → immediate review of dependents
- Strategic pivot → review all hypotheses for continued relevance
- New analysis deliverable → update index with hypothesis references

---

## Troubleshooting

### Issue: Hypothesis has conflicting evidence

**Solution**: Document the conflict in the revision reasoning. Use ranges to reflect uncertainty. Lower confidence grade to reflect ambiguity.

Example:
```json
"reasoning": "CAC estimates conflict: Meta benchmarks suggest $30-35, but category analysis of marine plasma suggests $40-50 due to novelty premium. Using blended range $30-45 until empirical data available. Grade C reflects benchmark uncertainty."
```

### Issue: Can't validate hypothesis (too expensive, too long)

**Solution**: Document why validation isn't feasible. Provide alternative validation path or accept D-grade as permanent.

Example:
```json
"validation_plan": {
  "method": "DEFERRED - requires 12+ months of cohort data",
  "cost": "N/A",
  "timeline": "Month 12+",
  "success_criteria": "Churn rate stabilizes <12% after 12 months"
},
"notes": "Early-stage validation not feasible - need full customer lifecycle. Accept D-grade for first 12 months, monitor monthly for trends."
```

### Issue: Hypothesis invalidated - now what?

**Solution**:
1. Log invalidation with full root cause analysis
2. Identify all dependent hypotheses (feeds_into relationships)
3. Flag dependents for revision
4. Create new hypothesis with corrected assumption (new HYP-ID)
5. Update financial model, strategic plans, or roadmaps as needed

### Issue: Too many hypotheses - system becoming unwieldy

**Solution**: Focus on CRITICAL and HIGH severity only. MEDIUM and LOW hypotheses can be tracked in document text without formal registry entries. Current system has 8 hypotheses - aim to keep <15 for manageability.

---

## Version History

**v1.0.0 (2026-02-05)**:
- Initial standards document
- Documented registry, index, validation log schemas
- Defined state machine and confidence grading system
- Provided JSON examples for all operations
- Included Month 1-2 validation guidance for top 4 hypotheses
- Established mandatory integration requirements for analysis documents
- Defined simple RETIRED state for hypothesis retirement

---

**For questions or clarifications, see:**
- `data/hypotheses/registry.json` - Current hypothesis registry
- `IonWave/Hypothesis_Dependency_Audit.md` - Comprehensive audit with examples
- `00_START_HERE.md` - Integration into project workflow
- Dashboard: https://caio-camargo.github.io/ionwave-dashboard/views/hypotheses-tracker.html
