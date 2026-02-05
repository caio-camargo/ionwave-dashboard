# Competitive Intelligence Protocol — INDEX
**Read this first. It routes you through everything else.**

---

## STATE TRACKER
*Update this section as you work. This survives context compaction.*

```
PROTOCOL_RUN_ID: [auto-generate on first run]
COMPETITOR: [name]
PHASE: [current phase — see routing below]
CHECKPOINT_TYPE: [none | scoping | surprise]
PERSONAS_COMPLETED: [list which have run]
PERSONA_ROUNDS: [current round count]
PERSONA_SATURATED: [yes/no]
BENCHMARKS_CHECKED: [yes/no]
NARRATIVE_AUDIT: [pending/complete]
COMPONENT_AUDIT: [pending/complete]
UPGRADES_GENERATED: [pending/complete]
SCORECARD: [pending/complete]
HUMAN_INTERRUPTS_PENDING: [list any type (b), (c), (d) interrupts awaiting response]
OUTPUT_FILE: [path to deliverable]
LAST_UPDATED: [timestamp]
```

---

## WHAT THIS PROTOCOL DOES

Takes a competitor name as input. Produces an integrated competitive intelligence deliverable with:
- All estimates produced (even if only D-grade confidence)
- Every claim explicitly graded
- Below-A items include prioritized upgrade paths
- Scorecard summarizing quality + upgrade shopping list

Zero human legwork required to produce output. Human participates only by responding in chat (scoping questions, confirming discrepancies, making strategic calls).

---

## SESSION START (runs before any protocol work)

```
1. Read 09_RUNTIME.md (file architecture, what persists where)
2. Read DISCREPANCY_REGISTER.md from project (if it exists)
3. Surface any OPEN or ACKNOWLEDGED items to human before proceeding
4. If workbook is available, scan for new discrepancies (08_DEPENDENCY_MAP.md defines what to check)
5. Update register if anything changed
6. Then route to whatever work the human requested (see EVENT-DRIVEN ROUTING below)
```

---

## EVENT-DRIVEN ROUTING

This is not a linear checklist. Route based on what just happened:

```
START
  └→ Read 01_SCOPING_CHECKPOINT.md
  └→ Run scoping checkpoint (ask clarifying questions)
  └→ Wait for human response
  └→ [EVENT: scoping complete] → goto RESEARCH

RESEARCH
  └→ Read 02_RESEARCH_PHASE.md
  └→ Reference 07_FRAMEWORKS.md ("what to look for" sections guide what data to collect)
  └→ Begin web research on competitor
  └→ [EVENT: source found] → goto VERIFY
  └→ [EVENT: source blocked] → mark D-grade, record in upgrade path, continue RESEARCH
  └→ [EVENT: surprise / unexpected finding] → goto SURPRISE_CHECKPOINT
  └→ [EVENT: research complete] → goto BENCHMARK_CHECK

VERIFY
  └→ Cross-check source against 02_RESEARCH_PHASE.md verification rules
  └→ Assign confidence grade (A/B/C/D)
  └→ [EVENT: large discrepancy detected] → goto DISCREPANCY_INTERRUPT
  └→ [EVENT: verified OK] → continue RESEARCH

SURPRISE_CHECKPOINT
  └→ Read 01_SCOPING_CHECKPOINT.md (surprise variant)
  └→ Present finding to human, ask clarifying questions
  └→ Wait for human response
  └→ Update state tracker
  └→ [EVENT: human responds] → continue RESEARCH (or redirect if needed)

DISCREPANCY_INTERRUPT
  └→ Present discrepancy to human (type (b) interrupt)
  └→ Wait for confirmation before proceeding
  └→ [EVENT: human confirms] → continue with confirmed value
  └→ [EVENT: human redirects] → update and continue RESEARCH

BENCHMARK_CHECK
  └→ Read 03_BENCHMARK_CHECK.md
  └→ Run narrative audit (broad coherence across all estimates)
  └→ Run component audit (each estimate vs. industry benchmarks)
  └→ Flag anomalies as potential exploitable insights
  └→ [EVENT: anomaly detected] → document in output as strategic note
  └→ [EVENT: benchmark check complete] → goto PERSONA_DIALOGUE

PERSONA_DIALOGUE
  └→ Read 07_FRAMEWORKS.md (grounds each persona in actual analytical frameworks)
  └→ Read 04_PERSONA_DIALOGUE.md
  └→ Run synthetic dialogue (Skeptical Investor ↔ Customer Anthropologist ↔ Competitive Strategist)
  └→ Track rounds toward saturation
  └→ [EVENT: new tension surfaced] → increment round, continue dialogue
  └→ [EVENT: saturation reached OR hard stop hit] → save dialogue summary, goto ASSEMBLY
  └→ [EVENT: qualitative judgment needed] → goto JUDGMENT_INTERRUPT

JUDGMENT_INTERRUPT
  └→ Present options to human (type (c) interrupt)
  └→ Wait for human response
  └→ [EVENT: human responds] → continue PERSONA_DIALOGUE

STRATEGIC_DECISION_INTERRUPT
  └→ Present analysis to human (type (d) interrupt)
  └→ Wait for human response
  └→ [EVENT: human responds] → continue from interrupted phase

ASSEMBLY
  └→ Read 05_ASSEMBLY.md
  └→ Build integrated deliverable (Estimates view + Gaps view + Scorecard)
  └→ Generate prioritized upgrade paths for all below-A items
  └→ [EVENT: assembly complete] → goto SELF_GRADE

SELF_GRADE
  └→ Read 06_SELF_GRADE.md
  └→ Grade output against rubric
  └→ Verify all items have confidence grades
  └→ Verify all below-A items have upgrade paths
  └→ Verify scorecard is accurate
  └→ [EVENT: grading complete] → DELIVER

DELIVER
  └→ Present deliverable to human
  └→ Read 08_DEPENDENCY_MAP.md
  └→ Look up all downstream edges from this deliverable
  └→ Flag affected deliverables for review (with: what changed, why, numeric vs strategic)
  └→ If change activates a kill trigger → type (d) strategic decision interrupt
  └→ Update state tracker: PHASE = COMPLETE
```

---

## FILE MAP

| File | When to Read | Purpose |
|------|-------------|---------|
| **00_INDEX.md** | Always first | This file. Routing + state. |
| **01_SCOPING_CHECKPOINT.md** | At START and on SURPRISE | Question sets for scoping and surprise checkpoints |
| **02_RESEARCH_PHASE.md** | During RESEARCH | Source hierarchy, verification rules, what to search for |
| **03_BENCHMARK_CHECK.md** | After research completes | Industry benchmarks by metric type, anomaly detection |
| **04_PERSONA_DIALOGUE.md** | After benchmarks | Persona definitions, saturation framework, hard stop, dialogue rules |
| **05_ASSEMBLY.md** | After dialogue completes | How to structure the integrated deliverable |
| **06_SELF_GRADE.md** | Before delivery | Grading rubric, upgrade path generation rules |
| **07_FRAMEWORKS.md** | Before PERSONA_DIALOGUE + during RESEARCH | The actual analytical frameworks each persona draws on. Applied form with worked LMNT example. |
| **08_DEPENDENCY_MAP.md** | After DELIVER (any time output is produced or updated) | What feeds what across the full Imagination Sprint. Determines which downstream deliverables need review when this module's output changes. |
| **09_RUNTIME.md** | Once per session, before anything else | Where files live, what persists, the upload loop, and how the Discrepancy Register works. |

---

## INTERRUPT HANDLING QUICK REFERENCE

| Type | When | Action | Blocking? |
|------|------|--------|-----------|
| **(a) Blocked source** | Can't access data | Mark D-grade, add upgrade path, continue | No |
| **(b) Large discrepancy** | Finding contradicts expectations significantly | Pause, present to human, wait | Yes |
| **(c) Qualitative judgment** | Requires human interpretation | Pause, present options, wait | Yes |
| **(d) Strategic decision** | Requires human strategic call | Pause, present analysis, wait | Yes |
| **Scoping checkpoint** | START of run | Ask clarifying questions | Yes |
| **Surprise checkpoint** | Unexpected finding mid-research | Ask clarifying questions | Yes |

---

## CONFIDENCE GRADE QUICK REFERENCE

| Grade | Meaning | Upgrade Path Required? |
|-------|---------|----------------------|
| **A** | Verified from authoritative source | No |
| **B** | Corroborated or strong single source | Yes (brief — what would make it A) |
| **C** | Industry benchmark or derived estimate | Yes (what data collection needed) |
| **D** | No verifiable source found / best guess | Yes (detailed — where to find this data) |

---

*Protocol v0.1 — 2026-02-01*
*Designed from: LMNT competitive intelligence execution + Danilo's spreadsheet automation framework*
