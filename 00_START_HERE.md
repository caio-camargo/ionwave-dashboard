# START HERE - Studio 3 Imagination Generation System
**Version**: v2.4.0
**Author**: Caio, Claude (collaborative)
**Date Created**: 2026-02-03
**Last Updated**: 2026-02-06
**AI Model**: claude-sonnet-4-5-20250929
**Purpose**: Single entry point for Studio 3 Imagination project - read this first every session
**Status**: Final
**Related Files**: DOCUMENTATION_INDEX.md, processes/Dependency_Map.md, data/manifest.json (TUP-based)

---

**READ THIS FIRST - EVERY TIME**

---

## What This Project Does

**Dual Purpose:**
1. **Improve & Complete IonWave**: Elevate quality from 4-6/10 to 8-9/10 and fill out all 38 Trade files completely
2. **Build the Imagination Generation System**: Create reusable frameworks and methodologies that work across all Studio 3 Trades

**Working Mode:** Improve example → extract patterns → codify → test → iterate

**Current Phase:** Bootstrap complete, system established - now executing systematically across all deliverables

---

## Current File Structure

### Data Layer — `data/` (TUP-based JSON, machine-optimized)
**This is the primary data source for Claude and the dashboard.**

**Organization:** TUP-based (Trade Unit Projects). 3 TUPs migrated to JSON, 38 TUPs pending migration.

```
data/
├── manifest.json                         ← MASTER INDEX: TUP-based, load this first for full project orientation
├── hypotheses/                           ← 🧪 HYPOTHESES ARCHITECTURE (ontological primitive)
│   ├── registry.json                     ← Central registry of 8 core business hypotheses
│   ├── index.json                        ← Bidirectional hypothesis ↔ document linking
│   └── validation_log.json               ← Chronological event log (11+ events)
├── m0_trade_thesis/                      ← M0 Trade Thesis (5 sheets, migrated from 01)
│   ├── _meta.json                        ← TUP-level metadata, dependencies, feedback loops
│   ├── assumptions_register.json
│   ├── interview_insights.json
│   ├── narrative_hypotheses.json
│   ├── odd1_thesis.json
│   └── thesis.json
├── m26_competitive_intel/                ← M26 Competitive Intel (10 sheets, migrated from 02)
│   ├── _meta.json
│   └── ... (10 sheet files)
└── m27_customer_research/                ← M27 Customer Research (12 sheets, merged from 03A ICP + 03B VOC)
    ├── _meta.json
    └── ... (ICP: 5 sheets, VOC: 7 sheets)
```

**Key points:**
- `manifest.json` now uses **TUP codes as primary keys** (m0, m26, m27, etc.) — contains all 41 TUPs, dependency chains, migration status
- **`hypotheses/`** — Central registry treating business assumptions as **ontological primitives** with validation tracking
- **TUP organization** — Data organized by TUP (Trade Unit Project) codes, not Bootstrap file numbers
- Each `_meta.json` contains TUP-level metadata: tup_id, tup_name, quality scores, dependencies, blockers, next actions
- Each sheet JSON has a `_meta` envelope with `data_type`, `quality_score`, `status`, and `version`
- Data types: `structured_table`, `narrative`, `hybrid`, `template`
- Inline confidence metadata on data points where applicable (A/B/C/D grading)

**For migrating more TUPs:** See `processes/JSON_Migration_Guide.md`
**For hypothesis tracking:** See `data/hypotheses/registry.json` and dashboard hypotheses tracker

### Archived Bootstrap Files — `archive/bootstrap-xlsx-pre-tup-migration/`
**Original Bootstrap XLSX files (01-38) archived during TUP migration.**

All 42 XLSX files (including version variants) moved to archive:
- 01-03B: Migrated to TUPs M0, M26, M27 (JSON)
- 04-38: Unmigrated, archived as reference (superseded by Danilo's TUP files)

**Reference:** See `data/crosswalk.json` for Bootstrap → TUP mapping, or `data/manifest.json` for current TUP inventory

### Dashboard — `dashboard/`
**Dynamic multi-page dashboard powered by TUP-based JSON data layer.**
```
dashboard/
├── index.html                    ← Mission Control (loads manifest.json, shows TUP status)
├── css/styles.css                ← Dark theme stylesheet
├── js/
│   ├── data-loader.js            ← Fetches and caches JSON data
│   └── renderers.js              ← Auto-renders content by data_type
└── views/
    ├── tup-navigator.html        ← 🗺️ TUP/Cluster system navigator
    ├── hypotheses-tracker.html   ← 🧪 Hypotheses system tracker
    ├── financial-forecast.html   ← 📊 Financial model scenarios
    ├── m0-trade-thesis.html      ← M0 Trade Thesis (formerly strategic-foundation)
    ├── m26-competitive-intel.html ← M26 Competitive Intel (formerly market-intelligence)
    └── m27-customer-research.html ← M27 Customer Research (merged 03A ICP + 03B VOC)
```

**Live at:** https://caio-camargo.github.io/ionwave-dashboard/
**Repo:** https://github.com/caio-camargo/ionwave-dashboard

**Key Dashboard Views:**
- **Mission Control** - TUP overview (3 migrated, 38 pending), cluster map, dependency chains, analysis deliverables
- **🗺️ TUP Navigator** - Complete TUP/Cluster hierarchy, ontological primitives, reconciliation status
- **🧪 Hypotheses Tracker** - 8 core business hypotheses with confidence grades, validation status, dependencies
- **📊 Financial Forecast** - 3-scenario financial model, timeline analysis, go/no-go frameworks
- **TUP Views** - Dynamic rendering of migrated TUP data (M0, M26, M27 currently available)

### Documentation Folders
```
IonWave/        → Analysis deliverables (Strategic Foundation, Porter's, ICP, Market Sizing, Financial Model, etc.)
core/           → Required reading (02_Glossary, 03_What_We_Did, 04_Working_Principles)
standards/      → Standards & guidelines (metadata, versioning, deliverable structure)
systems/        → System overviews (CM, ODD, School, TUP, Trade, etc.)
tracking/       → 42 live tracking logs (append-only, not versioned) + Open_Questions.md
processes/      → Process docs (Dependency_Map, JSON_Migration_Guide, demos)
ci-protocol/    → Competitive Intelligence Protocol (10-file workflow)
archive/        → Deprecated/historical files (including migrated XLSX files)
```

**Key Analysis Deliverables (`IonWave/`):**
- Strategic_Foundation_Analysis.md - Thesis reconciliation, capital tension analysis
- Porter_Five_Forces_Analysis.md - Market structure analysis
- ICP_Analysis.md - Customer segmentation, jobs-to-be-done
- Marine_Plasma_Market_Sizing.md - TAM/SAM/SOM analysis, Seaonic revenue estimation
- Financial_Model_Revenue_Validation.md - 3-scenario financial model (18-month base case)
- **Hypothesis_Dependency_Audit.md** - Comprehensive audit mapping 8 hypotheses to 35+ documents

### Version Control — Git / GitHub

**Repo:** https://github.com/caio-camargo/ionwave-dashboard
**Branch:** `main` (single branch, deployed to GitHub Pages)

**`.gitignore` policy:**
- `*.xlsx` — XLSX files are NOT version-controlled. JSON is source of truth for migrated files; non-migrated XLSX remain local only.
- `archive/` — Deprecated/historical files
- `.claude/` — Claude Code internal state
- Python artifacts, OS files

**What gets committed:** `data/`, `dashboard/`, `processes/`, `standards/`, `core/`, `ci-protocol/`, root `.md` files, `IonWave/*.md` analysis deliverables.

**What does NOT get committed:** `IonWave/*.xlsx`, `archive/`, `.claude/`

**Deployment:** Push to `origin/main` → auto-deploys to GitHub Pages. See `DASHBOARD_UPDATE_GUIDE.md` for deploy procedure.

### Deprecated Files (Reference Only)
**IonWave_Ops_Model_v10_Organized.xlsx** - 681-sheet comprehensive model
- Status: Deprecated, maintained for reference only
- Very large file - avoid opening unless specific need
- Superseded by 38 organized Trade files → now being migrated to JSON

**File Evolution:** v8 (88 sheets) → v10 (681 sheets) → 38 organized XLSX files → JSON data layer (in progress)

---

## Required Reading (In Order)

**Every session, read these first:**

1. **This document** (00_START_HERE.md) ← You are here
2. **`data/manifest.json`** - Machine-readable project index (all 38 files, dependencies, migration status)
3. **core/02_Glossary.md** - Key terminology and definitions
4. **core/03_What_We_Did.md** - Project history and methodology evolution
5. **core/04_Working_Principles_updated.md** - How we work together

**When working with Trade file data:**
- **Migrated files (01-03B):** Read from `data/{file_id}/` — load `_meta.json` first, then individual sheet JSONs
- **Non-migrated files (04-38):** Still in `IonWave/` as XLSX — requires openpyxl or manual reading
- **Migration process:** See `processes/JSON_Migration_Guide.md`

**When creating any document:**
- **standards/Document_Metadata_Standards.md** - Required metadata, versioning rules, document classes

**When looking for something:**
- **`data/manifest.json`** - Primary index: all 38 files with migration status, dependencies, quality scores
- **DOCUMENTATION_INDEX.md** - Complete inventory of all documentation files
- **Master_Index.md** - Legacy sheet-by-sheet index (still accurate for non-migrated files)
- **processes/Dependency_Map.md** - File relationships and workflow sequences

---

## Key Standards & Guidelines

### Documentation Standards
- **Metadata Required**: Version, Author, Date, Purpose, Status (AI Model if AI-generated)
- **Versioning**: Auto-increment patch (+0.0.1), tracked in standards/VERSION_MANIFEST.md
- **Document Classes**: Versioned operational, Methodology/framework, Ephemeral process, Live tracking

See `standards/Document_Metadata_Standards.md` for complete requirements.

### Quality Standards
- **Confidence Grading**: A/B/C/D scale for all factual claims
  - A: Verified from authoritative source
  - B: Strong single source or good triangulation
  - C: Industry benchmark with documented methodology
  - D: Best guess with documented upgrade path

- **Hypotheses Architecture**: Business assumptions tracked as ontological primitives
  - **Registry**: `data/hypotheses/registry.json` - 8 core hypotheses with revision history
  - **Index**: `data/hypotheses/index.json` - Bidirectional hypothesis ↔ document linking (53+ refs)
  - **Validation Log**: `data/hypotheses/validation_log.json` - Chronological event log
  - **State Machine**: ASSUMED → TESTING → VALIDATED/INVALIDATED
  - **Grading**: A/B/C/D confidence grades with transparent weak link detection
  - **Dependencies**: feeds_into/depends_on relationships showing hypothesis chains
  - **View**: https://caio-camargo.github.io/ionwave-dashboard/views/hypotheses-tracker.html

- **Deliverable Structure**: Three mandatory sections
  - Section 1: Main Content (with inline confidence tags)
  - Section 2: Intelligence Gaps (what we don't know, impact analysis, validation paths)
  - Section 3: Scorecard (quality self-assessment, upgrade shopping list)

See `core/04_Working_Principles_updated.md` for complete evidence standards.
See `IonWave/Hypothesis_Dependency_Audit.md` for hypothesis system documentation.

### Inline Quality Documentation
**Every claim must self-document its quality:**
```
[Confidence: A | Source: drinklmnt.com/pricing | Verified: 2026-01-31]
```

See `standards/Deliverable_Structure_Standards.md` for detailed requirements.

---

## How to Work with This System

### Question-Driven Workflow
**ALWAYS ask clarifying questions before producing deliverables**

Claude will ask 10-20 structured questions to understand:
- Purpose and audience
- Scope and boundaries
- Success criteria
- Time/resource constraints
- Tone and format preferences

**Why:** Prevents wasted work, forces clarity, documents rationale, produces better first drafts.

### Track A vs Track B Work

**Track A (Strategic Analysis - Claude Can Help):**
- Applying expert frameworks (Porter's Five Forces, Investor Lens, Customer Anthropologist)
- Mining customer voice from free sources (Reddit, Trustpilot, Amazon, forums)
- Competitive response scenario planning
- Strategic gap analysis
- Time: 4-6 hours | Cost: Free | Quality impact: 4/10 → 6-7/10

**Track B (Data Collection - Human Must Do):**
- SEMrush traffic research
- Paid market reports (IBISWorld, Statista)
- Extensive competitor research with screenshots
- Time: 15-20 hours | Cost: Tool subscriptions + labor | Quality impact: 6-7/10 → 8-9/10

**Principle:** Always start with Track A to get maximum value from existing data before collecting new data.

### Working with Dependencies
Files have dependencies - changing one may require updating others.

See `processes/Dependency_Map.md` for:
- Dependency chains (what feeds into what)
- Workflow sequences (recommended order of work)
- Which files must be updated together

### TUP / Cluster Navigation

Files are mapped to Danilo's TUP (Trade Unit Project) and Cluster hierarchy via `data/crosswalk.json`. Each file in `manifest.json` now has `danilo_tup`, `danilo_cluster`, and `passet` fields.

| Cluster | Name | TUPs | Our Files | Decision |
|---------|------|------|-----------|----------|
| BCL-0 | Thesis & Meta | M0, M34, M38, M39, M40 | 01, 24, 29, 34, 37 | MERGE (Bootstrap canon for analytics, Danilo for frameworks) |
| BCL-1 | Product & Science | M5, M6, M7, M8 | 05A, 05B, 09, 17, 36 | Danilo canon |
| BCL-2 | Money & Legal | M2, M3, M4, M25 | 06, 08, 17, 20, 33 | PENDING |
| BCL-3 | DR & Creative | M11-M15 | 09, 10A, 10B, 11A, 11B, 12 | Danilo canon |
| BCL-4 | Retention & Lifecycle | M17-M22 | 07, 11B, 14, 27, 30 | Danilo canon |
| BCL-5 | Growth & Market | M10, M16, M23, M26-M29 | 02, 03A, 03B, 07, 13, 21, 22, 25 | Danilo canon (analytical layer preserved) |
| BCL-6 | Operations & Infra | M1, M9, M24, M30-M31, M35-M37 | 04, 15, 16, 18, 19, 28, 31 | Danilo canon |
| BCL-7 | Governance & School | M32, M33 | 23, 30, 32, 33, 35 | Deferred |

**To find a TUP's OpKit or content:** Ask Claude. Claude navigates `crosswalk.json` and `manifest.json` to locate the right files.
**Full reconciliation log:** `tracking/Reconciliation_Decision_Log.md`
**Reconciliation audit:** `IonWave/Reconciliation_Audit.md`

### Ontological Primitives

The system's formal entities (full definitions in `standards/Systems_Architecture_Standards.md`):
- **Hypothesis** — testable business assumption with confidence grades and validation lifecycle (registry: `data/hypotheses/`)
- **TUP** — Trade Unit Project, the fundamental unit of knowledge about one subject
- **Protocol** — minimal executable unit of work (Process, Gate, Reactive, Meta-Control types)
- **Parameter** — numeric constraints with Variability Index (VI 1-5 indicating stability)
- **Controller** — monitoring mechanism that compares metrics to parameters and triggers reactive protocols
- **Passet** — structured information container (Drive folder with void spaces to be filled)
- **OpKit** — production support bundle scaffolding deliverable creation (Reference Models, templates, checklists)
- **Metric** — measured value tracked over time, consumed by Controllers
- **Observer** — composite state estimator (e.g., Computational PMF: 10 signals, weighted score, diagnostic patterns)
- **Meta-Control** — system-level supervisory module that tunes protocols, parameters, and controllers

### Finding Things
- **Full project orientation (Claude)?** → `data/manifest.json` (load first every session)
- **System architecture primitives?** → `standards/Systems_Architecture_Standards.md` (Protocol, Parameter, Controller, OpKit, Passet, Meta-Control)
- **TUP/Cluster mapping?** → `data/crosswalk.json` (maps file numbers to Danilo's TUP codes)
- **Reconciliation decisions?** → `tracking/Reconciliation_Decision_Log.md`
- **Project status at a glance (human)?** → [Dashboard](https://caio-camargo.github.io/ionwave-dashboard/) — see DASHBOARD_UPDATE_GUIDE.md
- **Business hypotheses/assumptions?** → `data/hypotheses/registry.json` or [Hypotheses Tracker](https://caio-camargo.github.io/ionwave-dashboard/views/hypotheses-tracker.html)
- **Hypothesis evidence mapping?** → `data/hypotheses/index.json` or `IonWave/Hypothesis_Dependency_Audit.md`
- **Critical strategic questions?** → `tracking/Open_Questions.md` (Q9, Q10, Q11 analyzed)
- **Specific TUP data (migrated)?** → `data/{tup_id}/` (M0, M26, M27 available as JSON)
- **Specific TUP data (not migrated)?** → Archived in `archive/bootstrap-xlsx-pre-tup-migration/` (reference only, superseded by Danilo's TUP files)
- **Sheet-level index?** → `data/manifest.json` (migrated files) or `Master_Index.md` (all files)
- **Looking for a document?** → DOCUMENTATION_INDEX.md
- **Understanding dependencies?** → processes/Dependency_Map.md (or `manifest.json` dependency_chains)
- **Checking current version?** → standards/VERSION_MANIFEST.md
- **Creating a document?** → standards/Document_Metadata_Standards.md
- **Structuring a deliverable?** → standards/Deliverable_Structure_Standards.md
- **Migrating a file to JSON?** → processes/JSON_Migration_Guide.md
- **Running competitive intelligence?** → ci-protocol/00_INDEX.md (full CI workflow)
- **Applying expert frameworks?** → ci-protocol/07_FRAMEWORKS.md (worked examples)

---

## What Claude Can Do

**Strategic Analysis:**
- Apply expert frameworks (Porter's Five Forces, Skeptical Investor, Customer Anthropologist, Category Expert)
- Synthesize existing data and extract patterns
- Generate strategic recommendations with documented reasoning
- Self-evaluate work against quality criteria with explicit confidence grades

**Research (Limited):**
- Web search for customer voice, reviews, public data
- Find market research sources (though often paywalled)
- Public company information (SEC filings if public)
- Mine customer insights from free sources

**Documentation:**
- Format data into structured deliverables
- Generate content based on templates and frameworks
- Quality check against rubrics and standards
- Identify gaps in evidence and create upgrade paths
- Create properly versioned documents with metadata

**Code & Data:**
- Read/write JSON data layer directly (no Python needed for migrated files)
- Python/openpyxl for XLSX extraction (non-migrated files only)
- Statistical analysis and modeling
- Dashboard and visualization updates
- Automation scripts

---

## Current Work Focus

### Bootstrap Phase Complete ✅
The system has been established through bootstrapping:
- Quality frameworks defined (A/B/C/D grading, deliverable structure)
- File organization complete (38 Trade files)
- Documentation standards set (metadata, versioning)
- Methodologies proven (competitive intelligence, customer voice, expert frameworks)

### TUP Migration (In Progress)
**Major architectural shift from Bootstrap file numbers to TUP-based organization:**
- **3 TUPs migrated**: M0 (Trade Thesis), M26 (Competitive Intel), M27 (Customer Research - merged ICP+VOC)
- **38 TUPs pending**: M1-M40 (excluding M0, M26, M27)
- JSON data layer optimized for TUP structure (one file per sheet, TUP-level metadata)
- Dynamic HTML dashboard with TUP-based navigation
- `manifest.json` rebuilt with TUP codes as primary keys (41 TUPs total)
- **Hypotheses Architecture** established as ontological primitive (8 core hypotheses, 53+ document references)
- Bootstrap XLSX files (01-38) archived to `archive/bootstrap-xlsx-pre-tup-migration/`

### Current Phase: Systematic Execution
Now applying established frameworks to:
- Continue JSON migration (Tier 2+ files as they're worked on)
- Complete all 38 IonWave Trade files
- Build reusable methodologies (Porter's Five Forces, etc.)
- Elevate quality from 4-6/10 to 8-9/10 across all deliverables
- Create proven patterns for future Trades

**Next Actions:** Reference `processes/Dependency_Map.md` for recommended work sequence, or `data/manifest.json` for per-file status and blockers.

---

## Key Principles

**Honesty About Quality:**
- Explicit confidence grades on all claims
- Document what we don't know (intelligence gaps)
- Show upgrade paths (how to improve from C to A)
- D-grade is acceptable if documented with validation path

**Evidence Over Opinion:**
- Source every claim: [Confidence: X | Source: Y | Date: Z]
- 30+ customer quotes minimum for voice of customer
- Methodology documented for all estimates
- "Could be wrong if..." scenarios for uncertainty

**Systematic Over Heroic:**
- Use frameworks and standards, don't reinvent
- Document as you go (inline quality tags)
- Check dependencies before changing files
- Version everything that matters

**Ask Before Assume:**
- Question-driven workflow prevents rework
- Clarify scope and success criteria upfront
- Checkpoint before building (show outline first)
- Validate decisions with explicit rationale

---

## Session Logging (Required)

**This project uses `SESSION_LOG.md` to maintain continuity across sessions.**

### At the start of every session:
1. Read the **last 3 session entries** in `SESSION_LOG.md` (they're reverse chronological — newest first)
2. Pay special attention to the **Next Steps** section of the most recent entry
3. Create a new entry at the top of the log using the template in that file
4. Only read older entries if you need context on a specific decision or file change

### During the session:
- Record all file changes (creates, edits, moves, archives) in the Actions table
- Log decisions and their rationale
- Note any issues or blockers encountered

### Session Closing Protocol (End of Every Session):

Run through this checklist before ending a session:

1. **Update SESSION_LOG.md**
   - Mark session status as `Complete`
   - List every file created/modified/deleted in the Actions table
   - Log all decisions and their rationale
   - Write clear "Next Steps" for the next session

2. **Check startup docs for staleness**
   - Does `00_START_HERE.md` still reflect reality? (file structure, branch names, dashboard views, current phase)
   - Does `DOCUMENTATION_INDEX.md` list any new files created this session?
   - Does `data/manifest.json` reflect any new data files or status changes?

3. **Commit and push**
   - Stage all relevant changes (data, dashboard, docs, tracking)
   - Commit with descriptive message
   - Push to `origin/main` to deploy dashboard updates
   - Verify no untracked files that should be committed

4. **Reconciliation check** (if applicable)
   - Are any new reconciliation decisions made? Update `tracking/Reconciliation_Decision_Log.md`
   - Does `IonWave/Reconciliation_Audit.md` need a version bump?
   - Does `data/crosswalk.json` need updates?

5. **Pending items** — explicitly note anything left unfinished in SESSION_LOG next steps

**Why:** Claude Code sessions don't share context. The session log and up-to-date docs are the only way to maintain continuity. If you skip this, the next session starts blind.

---

## Version History

**v2.4.0 (2026-02-06):**
- **MAJOR: TUP Migration** - Deprecated Bootstrap file numbering (01-38), adopted TUP-based organization (M0-M40)
- Migrated 3 TUPs: M0 (Trade Thesis), M26 (Competitive Intel), M27 (Customer Research - merged 03A+03B)
- Archived all Bootstrap XLSX files (01-38) to `archive/bootstrap-xlsx-pre-tup-migration/`
- Rebuilt `data/manifest.json` with TUP codes as primary keys (41 TUPs total, 3 migrated, 38 pending)
- Renamed data folders: `01_strategic_foundation` → `m0_trade_thesis`, `02_market_intelligence` → `m26_competitive_intel`, merged `03a_*` + `03b_*` → `m27_customer_research`
- Updated all dashboard views to TUP-based navigation (renamed view pages, updated Mission Control)
- Updated Data Layer section with TUP structure, archived Bootstrap Files section added

**v2.3.0 (2026-02-06):**
- Expanded Ontological Primitives section to include Protocol, Parameter, Passet, Meta-Control (now 10 primitives defined)
- Created `standards/Systems_Architecture_Standards.md` extracting formal definitions from Sprint_STAGE_5 historical document
- Added "System architecture primitives?" to Finding Things section
- Moved `Caio __ Danilo, Rhen Sprint_STAGE_5.md` to `archive/historical-reference/` (kept as context, extracted relevant architecture definitions)
- Updated AI Model reference to claude-sonnet-4-5-20250929

**v2.2.0 (2026-02-05):**
- Added TUP/Cluster navigation section with crosswalk table
- Added Ontological Primitives section (Hypothesis, TUP, Controller, Observer, OpKit, Metric)
- Created `data/crosswalk.json` mapping 38 files to Danilo's 41 Business Level TUPs and 8 clusters
- Added `danilo_tup`, `danilo_cluster`, `passet` fields to every file entry in `manifest.json`
- Added Finding Things entries for crosswalk and reconciliation log
- All content marked as Imagination Passet scope
- Reconciliation with `IonWave_Ops_Model_v10_Protocol.xlsx` — 10 of 11 decisions resolved (see `tracking/Reconciliation_Decision_Log.md`)

**v2.1.0 (2026-02-05):**
- Added Hypotheses Architecture system to data layer (`data/hypotheses/`)
- Updated Quality Standards section with hypotheses tracking requirements
- Added hypotheses tracker to Dashboard views (hypotheses-tracker.html, financial-forecast.html)
- Updated Finding Things with hypothesis and critical questions references
- Added Key Analysis Deliverables section under Documentation Folders
- Updated JSON Data Layer Migration status to note hypotheses system
- Added links to hypothesis dependency audit (53+ document references)

**v2.0.0 (2026-02-04):**
- Major update for JSON data layer migration
- Added `data/` directory structure and JSON conventions
- Updated Required Reading to include `manifest.json`
- Updated Finding Things for mixed JSON/XLSX access patterns
- Added Dashboard section documenting new multi-page architecture
- Updated Current Work Focus with migration status
- Updated "What Claude Can Do" for JSON data access
- References to `Master_Index.md` updated to note it's supplementary to `manifest.json`

**v1.0.0 (2026-02-03):**
- Complete rewrite from outdated v0.x
- Proper metadata header added
- Updated file structure (38 Trade files, deprecated v10)
- Added standards and guidelines sections
- Removed deprecated process doc references
- Added current phase and work focus
- Simplified "What Claude Can Do" (removed "Cannot" section)
- Added Quick Reference links to key documents

**Previous versions:** Superseded and archived

---

**Now read core/02_Glossary.md →**
