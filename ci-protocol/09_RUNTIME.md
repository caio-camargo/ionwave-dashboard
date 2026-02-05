# 09 — RUNTIME & FILE ARCHITECTURE
**Where things live. What persists. How the workflow actually loops.**

This is the operational reality of how the system runs. Everything else in the protocol suite assumes this is understood.

---

## FILE LOCATIONS AND ROLES

```
CLAUDE PROJECT (source of truth, persists across sessions)
  ├── IonWave_Ops_Model_v8_Complete.xlsx   ← the workbook. Claude reads, never writes.
  ├── 00_START_HERE.md                     ← project onboarding
  ├── 01-04 context docs                   ← Studio 3 context
  ├── Market_Landscape_Bootstrap_Plan.md   ← process doc
  └── DISCREPANCY_REGISTER.md             ← derived artifact. Claude maintains. See below.

CLAUDE OUTPUTS (writable, resets between sessions)
  ├── 00_INDEX.md through 09_RUNTIME.md   ← the protocol suite (delivered here)
  └── [any workbook updates]              ← when we produce a new workbook version,
                                             human downloads from here, then re-uploads to project

CLAUDE WORKING DIRECTORY (/home/claude)
  └── temporary files only. Nothing here survives the session.
```

**The key distinction:** the workbook is SOURCE DATA. The protocol suite and the discrepancy register are DERIVED ARTIFACTS. They are produced by reading the workbook and applying logic. They don't need to live inside the workbook.

---

## THE WORKBOOK UPLOAD LOOP

The workbook lives in the project. Claude can read it every session. Claude cannot write back to it.

When the protocol produces an updated workbook (e.g., a new sheet added, or existing data corrected), the loop is:

```
1. Claude produces updated workbook → /mnt/user-data/outputs/
2. Human downloads it from outputs
3. Human re-uploads it to the project
```

This is manual and it's the expected cost of working in this runtime. It should only happen when we actually change the workbook — not every session. Most sessions, Claude reads the workbook and produces protocol outputs (markdown files, analysis) without touching the workbook itself.

---

## THE DISCREPANCY REGISTER

### What it is

A markdown file that lives in the Claude project. It catalogs every cross-sheet inconsistency detected by scanning the workbook against the dependency map defined in 08_DEPENDENCY_MAP.md.

It is a DERIVED artifact. Claude regenerates it each session by reading the workbook fresh. It does not need to be "maintained" by the human — Claude re-detects everything from source data each time.

### Why it's markdown, not a workbook sheet

The workbook can't be written to from this runtime without a manual round-trip. The discrepancy register needs to be visible and active every session without that friction. A project markdown file is read automatically at the start of each session. A workbook sheet would require downloading, opening in Excel, and re-uploading just to see it.

### What it contains

Each entry has:

```
## DISCREPANCY-[ID]: [short title]

**Status:** OPEN | RESOLVED | ACKNOWLEDGED
**Severity:** CRITICAL | HIGH | MEDIUM
**Detected:** [session date]
**Last reviewed:** [session date or "not yet"]

**Sheet A:** [name] — assumes [value/claim]
**Sheet B:** [name] — assumes [value/claim]
**Conflict:** [plain language: what's inconsistent and why it matters]

**Dependency path:** [which downstream deliverables are affected]
**Resolution options:**
  1. [concrete option]
  2. [concrete option]

**Resolution:** [filled in when status changes to RESOLVED]
```

### Status rules

- **OPEN:** Detected and not yet addressed. Surfaces at the start of every session. Claude flags it before doing any other work.
- **ACKNOWLEDGED:** Human has seen it and made a conscious decision to leave it for now (e.g., "we'll resolve this when supplier quotes come back"). Does NOT disappear — it surfaces again each session with a note that it's acknowledged but unresolved.
- **RESOLVED:** The underlying discrepancy has been fixed in the source sheets. Claude verifies this by re-scanning. If the discrepancy is gone, status stays RESOLVED. If it reappears (e.g., someone edited a sheet back), status flips to OPEN automatically.

### When it runs

The consistency scan runs at the START of any session where the workbook is available. Before any protocol work begins. The register is updated, and any OPEN items are surfaced to the human.

It also runs at DELIVER (end of any protocol run) — because producing new output can introduce new discrepancies or resolve existing ones.

### Known discrepancies (current)

```
## DISCREPANCY-001: Unit Economics vs Landed Cost margin assumption

**Status:** OPEN
**Severity:** CRITICAL
**Detected:** 2026-02-01

**Sheet A:** Unit Economics — assumes 70% gross margin throughout all scenarios
**Sheet B:** Landed Cost Breakdown — base case shows 40% gross margin ($18.15 COGS on $47 subscription price); even optimistic case shows only 57%

**Conflict:** Unit Economics is built on a margin assumption that Landed Cost Breakdown's own numbers contradict. The base case LTV:CAC ratio of 3.0x (marked "marginal, viable") is calculated at 70% margin. At the actual 40% base-case margin, contribution margin per order collapses and LTV:CAC falls well below viability thresholds. Every downstream deliverable that uses Unit Economics outputs (Sensitivity Analysis, Cash Flow Model, Decision Framework, Investor Narrative, Choreography) is built on this incorrect foundation.

**Dependency path:** Landed Cost → Unit Economics → Sensitivity Analysis, Cash Flow Model, Decision Framework, Investor Narrative, Choreography. Also: Landed Cost → Offer Strategy → Unit Economics (circular pair — both need joint recalculation).

**Resolution options:**
  1. Raise price to $59 one-time / $53 subscription to recover margin (Landed Cost sheet already notes this as option 2)
  2. Negotiate supplier pricing to hit LOW estimates ($12.35 COGS) which yields 57% margin — still not 70%, but closer
  3. Rerun Unit Economics at actual margin scenarios (40% base, 57% optimistic) and accept that base case may not be viable without price increase
  4. Joint recalculation: solve Offer Strategy + Unit Economics together at realistic COGS inputs

**Resolution:** [pending]
```

---

## SESSION START CHECKLIST

Every session, before protocol work begins:

1. Read 00_INDEX.md (routing + state)
2. Read DISCREPANCY_REGISTER.md — surface any OPEN items to human
3. If workbook is available, scan for new discrepancies (compare against dependency map in 08)
4. Update register if anything changed
5. Then proceed to whatever work the human requested

---

## WHAT CLAUDE CAN AND CANNOT DO IN THIS RUNTIME

| Action | Can do? | Where |
|--------|---------|-------|
| Read project files | Yes | /mnt/project/ |
| Read uploaded files | Yes | /mnt/user-data/uploads/ |
| Write to outputs | Yes | /mnt/user-data/outputs/ |
| Write to project | No | writes don't sync back |
| Persist state across sessions | Via project files only | human must upload |
| Run Python against workbook | Yes | /home/claude (temporary) |
| Maintain the discrepancy register | Yes | as a project markdown file |
| Update the workbook in place | No | requires download/re-upload loop |
| Track real time | No | event-driven triggers only |
