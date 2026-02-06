# STUDIO 3 DOCUMENTATION INDEX
**Version**: v3.0.0
**Author**: Claude
**Date Created**: 2026-02-03
**Last Updated**: 2026-02-04
**AI Model**: claude-opus-4.5-20251101
**Purpose**: Complete inventory and categorization of all documentation files
**Status**: Final

---

## HOW TO USE THIS INDEX

**When you need to:**
- Find a specific document → Use Ctrl+F / Cmd+F
- Understand what exists → Browse categories below
- Know what's current vs deprecated → Check Status column
- Find the right doc for a task → See "When to Use" column

**Key:**
- ✅ = Current and actively maintained
- ⚠️ = Needs review/update (references outdated content)
- 🔄 = Live tracking (append-only, not versioned)
- 📦 = Historical/reference or archived
- ❌ = Deprecated or not found

**Folder Structure:**
```
root/           → Entry points, navigation, session log
data/           → JSON data layer (migrated Trade files + manifest) ← NEW
dashboard/      → Dynamic multi-page dashboard (HTML/CSS/JS) ← NEW
core/           → Required reading (Category 2)
standards/      → Standards & guidelines (Category 3)
systems/        → System overviews (Category 4)
tracking/       → Live tracking logs (Category 5)
processes/      → Process documentation (Category 6)
ci-protocol/    → Competitive Intelligence Protocol
IonWave/        → Trade files (34 remaining as xlsx, 4 migrated to JSON)
archive/        → Deprecated/historical files (including migrated XLSX)
```

---

## CATEGORY 1: ENTRY POINTS & NAVIGATION — `root/`

| File | Status | Purpose | When to Use |
|------|--------|---------|-------------|
| **00_START_HERE.md** | ✅ | Main entry point (v2.0.0) - read this first every session | Start of every session |
| **data/manifest.json** | ✅ | Machine-readable project index (all 38 files, dependencies, migration status) | Every session (Claude), finding files |
| SESSION_LOG.md | ✅ | Cross-session persistence log | Every session start/end |
| DOCUMENTATION_INDEX.md | ✅ | This file — complete inventory | Finding any document |
| README.md | ⚠️ | General project README | Initial project overview (check if current) |
| Master_Index.md | ⚠️ | Legacy sheet-by-sheet index of all 38 Trade files | Non-migrated files; supplemented by manifest.json |
| dashboard.html | 📦 Deprecated | Old single-file hardcoded dashboard | Superseded by dashboard/ (v2) |
| DASHBOARD_UPDATE_GUIDE.md | ✅ | How to update and deploy the v2 dashboard | Updating/deploying the dashboard |
| 00_MASTER_CONTROL.md | 📦 Archived | See archive/obsolete-2026-02-03/ | OLD: Entry point for v10 structure |
| 00_IMPLEMENTATION_GUIDE.md | 📦 Archived | See archive/obsolete-2026-02-03/ | Historical: inline quality documentation update |
| README_START_HERE.md | 📦 Archived | See archive/obsolete-2026-02-03/ | Outdated system overview |

**Action Needed**:
- ⚠️ Review README.md for outdated content

---

## CATEGORY 1B: DATA LAYER — `data/`

**JSON data layer for migrated Trade files. Primary data source for Claude and the dashboard.**

| File | Status | Purpose | When to Use |
|------|--------|---------|-------------|
| **data/manifest.json** | ✅ | Master index of all 38 files with migration status, dependencies, feedback loops | Every session start, finding any file |
| data/01_strategic_foundation/ | ✅ | 5 sheets + _meta.json | Working with Strategic Foundation data |
| data/02_market_intelligence/ | ✅ | 10 sheets + _meta.json | Working with Market Intelligence data |
| data/03a_customer_research_icp/ | ✅ | 5 sheets + _meta.json | Working with ICP data |
| data/03b_customer_research_voc/ | ✅ | 7 sheets + _meta.json | Working with VOC data |

**Convention:** Each directory contains `_meta.json` (file-level metadata) + one JSON per sheet. Sheets have `_meta` envelope with `data_type`, `quality_score`, `status`, `version`.

**For migrating more files:** See `processes/JSON_Migration_Guide.md`

---

## CATEGORY 1C: DASHBOARD — `dashboard/`

**Dynamic multi-page dashboard powered by JSON data layer.**

| File | Status | Purpose | When to Use |
|------|--------|---------|-------------|
| dashboard/index.html | ✅ | Mission Control — loads manifest.json dynamically | Project overview |
| dashboard/css/styles.css | ✅ | Shared dark theme stylesheet | Styling changes |
| dashboard/js/data-loader.js | ✅ | Fetches and caches JSON data files | Data loading changes |
| dashboard/js/renderers.js | ✅ | Auto-renders content by data_type | Rendering logic changes |
| dashboard/views/tup-navigator.html | ✅ | TUP/Cluster system navigator, ontological primitives, reconciliation status | Navigating TUP hierarchy |
| dashboard/views/hypotheses-tracker.html | ✅ | Hypotheses system tracker (8 hypotheses, confidence grades) | Viewing hypothesis status |
| dashboard/views/hypothesis-detail.html | ✅ | Individual hypothesis detail view | Drilling into one hypothesis |
| dashboard/views/financial-forecast.html | ✅ | 3-scenario financial model and timeline analysis | Viewing financial projections |
| dashboard/views/strategic-foundation.html | ✅ | Trade file 01 detail view | Viewing Strategic Foundation |
| dashboard/views/market-intelligence.html | ✅ | Trade file 02 detail view | Viewing Market Intelligence |
| dashboard/views/customer-research.html | ✅ | Trade files 03A + 03B combined view | Viewing Customer Research |

**Live at:** https://caio-camargo.github.io/ionwave-dashboard/

---

## CATEGORY 2: CORE DOCUMENTATION (Required Reading) — `core/`

| File | Status | Purpose | When to Use |
|------|--------|---------|-------------|
| **01_Studio3_Context.md** | ⚠️ | Organizational overview and structure | Understanding Studio 3 context |
| **core/02_Glossary.md** | ✅ | Key terminology, definitions, and documentation standards | When you see unfamiliar terms |
| **core/03_What_We_Did.md** | ✅ | History of bootstrap work including "What Happened Since" | Understanding project evolution |
| **core/04_Working_Principles_updated.md** | ✅ | How we work together - collaboration patterns, quality standards | Every session - how to work |

**Action Needed**:
- ✅ 02_Glossary.md and 03_What_We_Did.md updated (2026-02-03)
- ⚠️ 01_Studio3_Context.md not found in directory — needs creation or recovery
- Note: These are listed as "required reading" in 00_START_HERE.md

---

## CATEGORY 3: STANDARDS & GUIDELINES — `standards/`

| File | Status | Purpose | When to Use |
|------|--------|---------|-------------|
| **standards/Document_Metadata_Standards.md** | ✅ | Required metadata for all documents | Creating any new document |
| **standards/VERSION_MANIFEST.md** | ✅ | Version tracking for all versionable files | Checking current versions, updating files |
| **standards/Deliverable_Structure_Standards.md** | ✅ | Mandatory three-section structure for deliverables | Creating any deliverable |
| standards/Model_Orchestration_updated.md | ✅ | How to work systematically - 6 patterns for different tasks | Complex multi-step workflows |
| standards/Manifest_Verification_Workflow.md | ✅ | How to verify VERSION_MANIFEST is current | Daily/weekly manifest checks |
| standards/Quality_Architecture_Integration_v2.md | ✅ | Reconciling CI Protocol with Studio 3 architecture | Quality pattern integration |

---

## CATEGORY 4: SYSTEM OVERVIEWS — `systems/`

| File | Status | Purpose | When to Use |
|------|--------|---------|-------------|
| systems/CM_System_Overview.md | ✅ | Compliance Manager system (Anya role) | Understanding CM function |
| systems/ODD_System_Overview.md | ✅ | Overdetermined Documentation system | Understanding ODD methodology |
| systems/School_System_Overview.md | ✅ | Operator training system | Onboarding new operators |
| systems/Strategic_Games_Overview.md | ✅ | Strategic decision frameworks | High-level strategic thinking |
| systems/TUP_System_Overview.md | ✅ | Trade Under Planning pipeline | Managing new Trade ideas |
| systems/Trade_Structure_Overview.md | ✅ | How Trades are structured | Understanding Trade anatomy |
| systems/Operator_Management_Overview.md | ✅ | How operators are managed across Trades | Operator resource allocation |
| CM_System_Overview (1).md | 📦 Archived | See archive/obsolete-2026-02-03/ | Duplicate |

---

## CATEGORY 5: TRACKING & LOGS (Not Versioned - Live Documents) — `tracking/`

| File | Status | Purpose | When to Use |
|------|--------|---------|-------------|
| tracking/AB_Test_Log.md | 🔄 | Track A/B tests across all properties | Recording test results |
| tracking/Batch_Lot_Tracking.md | 🔄 | Track product batches and lot numbers | Manufacturing QC |
| tracking/Brand_Tracking_Metrics.md | 🔄 | Monitor brand health over time | Brand performance review |
| tracking/Budget_Spend_Log.md | 🔄 | Track budget allocation and spend | Financial tracking |
| tracking/Change_Control_Log.md | 🔄 | Log all significant changes to systems | Change management |
| tracking/Changes_Tracker.md | 🔄 | What changed and why | Version control narrative |
| tracking/CM_Alert_Log.md | 🔄 | Compliance Manager alerts | CM tracking |
| tracking/CM_Communication_Log.md | 🔄 | CM communications with team | CM tracking |
| tracking/CM_Interview_Log.md | 🔄 | CM interview notes | CM tracking |
| tracking/CM_KPI_Tracker.md | 🔄 | CM key performance indicators | CM tracking |
| tracking/CM_Milestone_Tracker.md | 🔄 | CM milestone progress | CM tracking |
| tracking/CM_Observations_Log.md | 🔄 | CM observations and insights | CM tracking |
| tracking/COA_Tracker.md | 🔄 | Certificate of Analysis tracking | Quality control |
| tracking/Cohort_Analysis_Tracker.md | 🔄 | Track customer cohort performance | Customer analytics |
| tracking/Compliance_Audit_Log.md | 🔄 | Compliance audit results | Regulatory tracking |
| tracking/Coordination_Debt_Tracker.md | 🔄 | Track coordination inefficiencies | Operational debt management |
| tracking/Creator_Pipeline_Tracker.md | 🔄 | Content creator pipeline status | Creator partnerships |
| tracking/Customer_Interview_Tracker.md | 🔄 | Track customer interview schedule/results | VOC research |
| tracking/Customer_Issue_Log.md | 🔄 | Log customer problems and resolutions | Customer support |
| tracking/Decision_Log.md | 🔄 | Append-only decision history with context | Recording strategic decisions |
| tracking/Discrepancy_Register_updated.md | 🔄 | Cross-sheet/file conflicts and inconsistencies | Data integrity |
| tracking/Eigenform_Tracker.md | 🔄 | Track eigenform development | Advanced strategy tracking |
| tracking/Execution_Status.md | 🔄 | Progress dashboard | Project status |
| tracking/Feature_Request_Log.md | 🔄 | Track feature requests | Product development |
| tracking/Influencer_Pipeline_Tracker.md | 🔄 | Influencer partnership pipeline | Influencer marketing |
| tracking/NPS_Tracking.md | 🔄 | Net Promoter Score tracking | Customer satisfaction |
| tracking/ODD_Status_Tracker.md | 🔄 | Overdetermined Documentation status | ODD system tracking |
| tracking/Open_Questions.md | 🔄 | Active questions requiring resolution | Decision support |
| tracking/Organizational_Neurosis_Log.md | 🔄 | Track organizational dysfunction patterns | Culture/process improvement |
| tracking/Paradigm_Shift_Log.md | 🔄 | Log significant strategic pivots | Strategic evolution |
| tracking/PR_Media_Tracker.md | 🔄 | PR and media coverage tracking | PR management |
| tracking/Price_Testing_Log.md | 🔄 | Pricing experiment results | Pricing strategy |
| tracking/Refund_Return_Tracker.md | 🔄 | Track refunds and returns | Customer service/operations |
| tracking/Screenshot_Evidence_Log.md | 🔄 | Visual evidence repository | Documentation |
| tracking/Sunk_Cost_Clarity_Log.md | 🔄 | Track sunk cost decisions | Strategic clarity |
| tracking/Supplier_Outreach_Tracker.md | 🔄 | Supplier contact and negotiation status | Supply chain |
| tracking/Time_Tracking_Log.md | 🔄 | Time allocation tracking | Resource management |
| tracking/Tool_Login_Credentials.md | 🔄 | Login information for various tools | Access management |
| tracking/Tracking_Setup.md | 🔄 | How tracking systems are configured | System administration |
| tracking/Trade_Execution_Tracker.md | 🔄 | Track execution across all Trades | Multi-Trade management |
| tracking/Verification_Log.md | 🔄 | Verification status for various items | Quality assurance |
| tracking/VSL_Iteration_Log.md | 🔄 | Video Sales Letter iteration tracking | Creative development |

**Note**: All tracking logs are append-only and NOT versioned per VERSION_MANIFEST rules.

---

## CATEGORY 6: PROCESS DOCUMENTATION — `processes/`

| File | Status | Purpose | When to Use |
|------|--------|---------|-------------|
| processes/DEMO_How_System_Works.md | ✅ | Concrete example walkthrough of tracking system | Learning the system |
| processes/Dependency_Map.md | ✅ | File relationships and workflow sequences | Understanding dependencies |
| **processes/JSON_Migration_Guide.md** | ✅ | Step-by-step process for migrating XLSX files to JSON | Migrating remaining 34 Trade files |
| processes/Knowledge_Logistics_Audit.md | ✅ | How knowledge flows through organization | Knowledge management |
| **processes/Porter_Five_Forces_Protocol.md** | ✅ | Step-by-step protocol for producing a Porter's Five Forces analysis | Applying Porter's Five Forces framework |
| processes/Workbook_Generation_Summary.md | 📦 | Summary of workbook generation from extraction | Historical reference |

---

## CATEGORY 6B: FORMAL PROTOCOLS — `protocols/`

**Meta-Control protocols that operate on the system itself (not on business operations).**

| File | Status | Purpose | When to Use |
|------|--------|---------|-------------|
| **protocols/CSP-001_Constraint_Scenario_Protocol.md** | ✅ | 10-step protocol for stress-testing hypotheses through extreme constraints | Before validation spending, quarterly review, new hypothesis created |
| protocols/case_studies/CSP-001_HYP-006_2026-02-06.md | ✅ | First CSP case study: HYP-006 Organic & Referral Lift decomposed into 5 sub-hypotheses | Reference for running CSP on other hypotheses |

**Note**: Protocols directory contains formal Meta-Control protocols per `standards/Systems_Architecture_Standards.md`. Case studies document each protocol execution for institutional memory.

---

## CATEGORY 7: COMPETITIVE INTELLIGENCE PROTOCOL — `ci-protocol/`

| File | Status | Purpose | When to Use |
|------|--------|---------|-------------|
| ci-protocol/00_INDEX.md | ✅ | Protocol routing and state tracker | Starting a CI analysis |
| ci-protocol/01_SCOPING_CHECKPOINT.md | ✅ | Phase 1: Scoping | Defining CI scope |
| ci-protocol/02_RESEARCH_PHASE.md | ✅ | Phase 2: Research | Conducting research |
| ci-protocol/03_BENCHMARK_CHECK.md | ✅ | Phase 3: Benchmarks | Checking benchmarks |
| ci-protocol/04_PERSONA_DIALOGUE.md | ✅ | Phase 4: Personas | Running persona dialogues |
| ci-protocol/05_ASSEMBLY.md | ✅ | Phase 5: Assembly | Assembling deliverable |
| ci-protocol/06_SELF_GRADE.md | ✅ | Phase 6: Self-grading | Grading the output |
| ci-protocol/07_FRAMEWORKS.md | ✅ | Phase 7: Frameworks | Applying frameworks |
| ci-protocol/08_DEPENDENCY_MAP.md | ✅ | File architecture reference | Understanding CI file dependencies |
| ci-protocol/09_RUNTIME.md | ✅ | Runtime environment definition | CI runtime setup |

**Note**: Complete 10-file protocol for competitive intelligence analysis. Start with `ci-protocol/00_INDEX.md`.

---

## CATEGORY 8: EXTRACTION & ORGANIZATION (Archived) — `archive/`

| File | Status | Purpose | When to Use |
|------|--------|---------|-------------|
| Categorization_And_Order_Of_Work.md | 📦 Archived | Analysis of 681 sheets | Historical reference only |
| Categorization_Final_Analysis.md | 📦 Archived | Final categorization decisions | Historical reference only |
| Extraction_Execution_Plan.md | 📦 Archived | Plan for extracting sheets from v10 | Historical reference only |
| Extraction_Progress.md | 📦 Archived | Progress tracking for extraction work | Historical reference only |
| Extraction_Roadmap.md | 📦 Archived | Roadmap for extraction phases | Historical reference only |
| FINAL_Categorization.md | 📦 Archived | Final categorization of all sheets | Historical reference only |

**Note**: All moved to `archive/obsolete-2026-02-03/`. These chronicle the extraction from v10 (681 sheets) to 38 organized Trade files.

---

## TRADE FILES — `data/` (migrated) + `IonWave/` (remaining)

4 Trade files migrated to JSON in `data/` (01, 02, 03A, 03B). 34 remaining as XLSX in `IonWave/`.
See `data/manifest.json` for complete inventory with migration status, or `Master_Index.md` for legacy sheet listing.

**Analysis Deliverables:**

| File | Status | Purpose | When to Use |
|------|--------|---------|-------------|
| **IonWave/Porter_Five_Forces_Analysis.md** | ✅ v1.1.0 | Porter's Five Forces industry-structure analysis | Competitive positioning, market-entry strategy |
| **IonWave/Porter_Five_Forces_Dialogue_Summary.md** | ✅ v1.0.0 | Traceability record of persona dialogue on Porter's analysis | Verifying analysis was stress-tested |
| **IonWave/ICP_Analysis.md** | ✅ v1.1.0 | ICP validation with JTBD framework, VOC cross-referencing, confidence grading | Customer targeting, messaging strategy, persona validation |
| **IonWave/ICP_Dialogue_Summary.md** | ✅ v1.0.0 | Traceability record of persona dialogue on ICP analysis (ICP-2026-02-04-001) | Verifying ICP analysis was stress-tested |
| **IonWave/Strategic_Foundation_Analysis.md** | ✅ v1.2.0 | Thesis reconciliation, Interview Insights backfill, Narrative Hypothesis evidence, capital tension analysis | Strategic direction, thesis validation, capital planning |
| **IonWave/Strategic_Foundation_Dialogue_Summary.md** | ✅ v1.0.0 | Traceability record of persona dialogue on Strategic Foundation analysis (SF-2026-02-04-001) | Verifying Strategic Foundation analysis was stress-tested |
| **IonWave/Marine_Plasma_Market_Sizing.md** | ✅ v1.0.0 | Seaonic revenue estimation, marine plasma sub-segment sizing, competitive landscape map | Market sizing, competitive intelligence, thesis validation |

---

## SUMMARY BY STATUS

| Status | Count | Meaning |
|--------|-------|---------|
| ✅ Current | 42 | Actively maintained, up to date (includes data/ and dashboard/) |
| ⚠️ Needs Review | 2 | Contains outdated references (README.md, Master_Index.md) |
| 🔄 Live Tracking | 42 | Append-only logs, not versioned |
| 📦 Archived/Deprecated | 18 | Historical/deprecated (see archive/), includes old dashboard.html |
| **TOTAL** | **104** | Including CI Protocol, data layer, and dashboard files |

---

## CRITICAL ACTIONS NEEDED

### Completed (2026-02-03):
1. ✅ Created new 00_START_HERE.md v1.0.0 with proper metadata
2. ✅ Audited 01-04 docs for outdated references
3. ✅ Archived deprecated docs to archive/obsolete-2026-02-03/
4. ✅ Created archive/ directory structure
5. ✅ Updated 02_Glossary.md and 03_What_We_Did.md
6. ✅ Reorganized all files into folder structure
7. ✅ Archived old duplicates (Model_Orchestration, Discrepancy_Register, README_START_HERE)
8. ✅ Archived Category 7 extraction docs
9. ✅ Moved Trade xlsx files to IonWave/
10. ✅ Added CI Protocol as new category

### Completed (2026-02-04):
11. ✅ Migrated Trade files 01-03B from XLSX to JSON data layer
12. ✅ Created data/manifest.json as machine-readable project index
13. ✅ Built dynamic multi-page dashboard (dashboard/)
14. ✅ Deployed to GitHub Pages
15. ✅ Created processes/JSON_Migration_Guide.md
16. ✅ Updated 00_START_HERE.md to v2.0.0 for JSON data layer
17. ✅ Rewrote DASHBOARD_UPDATE_GUIDE.md for v2 architecture
18. ✅ Updated this index with data/ and dashboard/ categories
19. ✅ Archived migrated XLSX files to archive/xlsx-pre-json-migration/

### Still Needed:
20. ⚠️ Review README.md for outdated content
21. ⚠️ Find or recreate 01_Studio3_Context.md
22. ⚠️ Migrate remaining 34 Trade files to JSON (ongoing)

---

## QUICK REFERENCE: WHICH DOC FOR WHICH TASK?

| Task | Document |
|------|----------|
| **Starting a session** | 00_START_HERE.md → then `data/manifest.json` |
| **Full project orientation (Claude)** | `data/manifest.json` |
| **Viewing project status visually (human)** | [Dashboard](https://caio-camargo.github.io/ionwave-dashboard/) |
| **Updating/deploying the dashboard** | DASHBOARD_UPDATE_GUIDE.md |
| **Session history** | SESSION_LOG.md |
| **Finding Trade file data (migrated)** | `data/{file_id}/` (01-03B) |
| **Finding Trade file data (not migrated)** | `IonWave/{filename}.xlsx` (04-38) |
| **Finding a specific sheet** | `data/manifest.json` or Master_Index.md |
| **Migrating a file to JSON** | processes/JSON_Migration_Guide.md |
| **Understanding file dependencies** | processes/Dependency_Map.md (or manifest.json) |
| **Creating a new document** | standards/Document_Metadata_Standards.md |
| **Checking current file versions** | standards/VERSION_MANIFEST.md |
| **Understanding how to work systematically** | standards/Model_Orchestration_updated.md |
| **Structuring a deliverable** | standards/Deliverable_Structure_Standards.md |
| **Recording a decision** | tracking/Decision_Log.md |
| **Tracking a conflict/inconsistency** | tracking/Discrepancy_Register_updated.md |
| **Understanding terminology** | core/02_Glossary.md |
| **Seeing project history** | core/03_What_We_Did.md |
| **Applying expert frameworks (Porter's, Investor Lens, etc.)** | ci-protocol/07_FRAMEWORKS.md |
| **Running Porter's Five Forces analysis** | processes/Porter_Five_Forces_Protocol.md |
| **Running competitive intelligence (full workflow)** | ci-protocol/00_INDEX.md |

---

**This index will be versioned once approved and added to VERSION_MANIFEST.**
