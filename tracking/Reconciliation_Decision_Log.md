# Reconciliation Decision Log

**Purpose:** Append-only log of every reconciliation decision between IonWave_Ops_Model_v10_Protocol and Bootstrap system.
**Reference:** `IonWave/Reconciliation_Audit.md` for full context and crosswalk.
**Format:** Each entry is immutable once recorded. New entries appended at bottom.

---

## Decision Template

```
### REC-NNN | YYYY-MM-DD | Domain
**Cluster:** BCL-X / SCL-X / FCL-X
**Danilo TUP(s):** MXX, MYY
**Bootstrap File(s):** File XX, File YY
**Decision:** DANILO CANON / BOOTSTRAP CANON / MERGE / SKIP / DEFER
**Rationale:** [Why this decision was made]
**Decided by:** [Who]
**Hypotheses affected:** HYP-NNN (if any)
**Data changes required:** [What needs to change in data/, dashboard/, or manifest.json]
**Status:** DECIDED / IMPLEMENTED / VERIFIED
```

---

## Decisions

### REC-011 | 2026-02-05 | Taxonomy Architecture
**Cluster:** System-wide
**Danilo TUP(s):** S4 (Taxonomy), S0 (Studio Thesis), Directory, Master Cluster Map
**Bootstrap File(s):** data/manifest.json, 00_START_HERE.md, dashboard/
**Decision:** ADOPT (Hybrid)
**Rationale:** Six architectural sub-decisions were resolved:
1. **Imagination/Implementation Passet split** — ADOPT. Our Bootstrap work IS the Imagination Passet. This is a framing adoption, not a restructuring. The Implementation Passet is a separate future layer.
2. **Lifecycle model (Production > Grading > Lock > Implementation > Review)** — ACKNOWLEDGE, NOT ADOPT YET. We are building the system; the current iterative process is appropriate for construction. The canonical lifecycle applies once the system is built.
3. **Legibility Architecture ("Claude is the UI")** — ADOPT. This was Caio's original idea. The dashboard exists as a visual interface but the primary interaction model is Claude navigating the data layer. The spreadsheet/JSON is the database; Claude is the interface.
4. **School Model** — DEFER. Novel organizational framework, understood at concept level, but mostly out of scope for present work. Revisit when team scales beyond 2 people.
5. **Trust Protocol** — ADOPT conceptually. Map to hypothesis framework — four trust levels (Strategic, Domain, Execution, Vibes) as a lens on which hypotheses require which kind of validation.
6. **Three-Level Flywheel** — ACKNOWLEDGE. Danilo's portfolio-level vision (Content → People → Models → Businesses → Proof → Content). Good to know, mostly out of scope for present IonWave Business Level work.
**Decided by:** Caio
**Hypotheses affected:** Trust Protocol mapping may affect validation approach for all HYP-001 through HYP-008
**Data changes required:** Add `"passet": "imagination"` metadata to manifest.json. Add `"danilo_tup"` and `"danilo_cluster"` mapping fields per file. Create data/crosswalk.json. Keep file numbering (01-38) as primary keys.
**Status:** DECIDED

### REC-009 | 2026-02-05 | Studio Level
**Cluster:** SCL-0 through SCL-5
**Danilo TUP(s):** S0-S40 (41 TUPs)
**Bootstrap File(s):** N/A (no direct equivalent)
**Decision:** DEFER
**Rationale:** Studio Level is Danilo's system-level IP describing how the venture studio operates. Contains substantive architectural content (Three-Level Architecture, Trust Protocol, Coordination Hedgefund thesis, School Model). Good to understand but out of scope for present IonWave Business Level work.
**Decided by:** Caio
**Hypotheses affected:** None directly
**Data changes required:** None
**Status:** DECIDED

### REC-010 | 2026-02-05 | Funnel Level
**Cluster:** FCL-0 through FCL-3
**Danilo TUP(s):** F0-F20 (21 TUPs)
**Bootstrap File(s):** N/A (no direct equivalent)
**Decision:** DEFER
**Rationale:** Funnel Level is a separate layer (Dan James / Thakos operation) that operates alongside IonWave. Both a standalone revenue line and the recruiting engine. Out of scope for present work.
**Decided by:** Caio
**Hypotheses affected:** None
**Data changes required:** None
**Status:** DECIDED

### REC-002a | 2026-02-05 | BCL-0 Sub-decision: Bifurcation Points
**Cluster:** BCL-0 (Thesis & Meta)
**Danilo TUP(s):** M0 — `131_bifurcation_points.json`
**Bootstrap File(s):** data/hypotheses/registry.json (HYP-001 through HYP-008 kill thresholds)
**Decision:** ADOPT as controllers within systems architecture
**Rationale:** Bifurcation points are controllers in the systems engineering sense. They define parameters (threshold values), metrics (measured values to compare), and reactive protocols (defined responses when a metric crosses a parameter). The full controller stack becomes: Early Warning (80% of bifurcation) → Bifurcation (investigate/intervene) → Kill (stop the business). Danilo's 8 bifurcation points are adopted. Specific parameter values (e.g., churn bifurcation at 10% vs HYP-003 kill at 15%) are not contradictions — they are different severity levels in the same controller. Parameter reconciliation with hypothesis thresholds to be done when the controller layer is formalized. Metrics layer and reactive protocols to be built during implementation.
**Decided by:** Caio
**Hypotheses affected:** HYP-001 (CAC), HYP-003 (Churn), HYP-004 (Margin) — parameters overlap but at different severity levels
**Data changes required:** Formalize controller layer in systems architecture. Reconcile bifurcation parameters with hypothesis kill thresholds.
**Status:** DECIDED

### REC-002b | 2026-02-05 | BCL-0 Sub-decision: Computational PMF
**Cluster:** BCL-0 (Thesis & Meta)
**Danilo TUP(s):** M0 — `137_computational_pmf.json`
**Bootstrap File(s):** No equivalent
**Decision:** ADOPT as an Observer in the systems architecture
**Rationale:** Computational PMF is an Observer — a composite state estimator that takes 10 signals and produces a single legible PMF assessment. Individual signals (Sean Ellis >40%, Retention M2 >40%, Organic >30%, NPS >50, CAC trend declining, Referral >10%, Explanation cost <30s, Price sensitivity low, Inbound growing, Time to value <7 days) become formalized Metrics feeding from the metrics layer. Weighted composite score (Sean Ellis 25%, Retention 20%, Organic 15%, NPS 15%, CAC Trend 10%, Referral 5%) provides score bands (0-30 No PMF, 30-50 Early, 50-70 Achieved, 70+ Strong). Five diagnostic patterns serve as a fault-tree. Lives in an OpKit associated with M0 (Trade Thesis) — PMF is an early thesis-level deliverable. Modular; can be relocated later.
**Decided by:** Caio
**Hypotheses affected:** HYP-005 (Blended LTV) — PMF Observer provides a richer assessment than LTV alone
**Data changes required:** Each of the 10 PMF signals to be formalized as individual Metrics. Observer to be defined in systems architecture alongside controllers. OpKit association with M0 to be registered.
**Status:** DECIDED

### REC-002d | 2026-02-05 | BCL-0 Sub-decision: Anti-Goals
**Cluster:** BCL-0 (Thesis & Meta)
**Danilo TUP(s):** M0 — `115_anti_goals.json`
**Bootstrap File(s):** File 37 (Strategic Initiatives) — `anti_goals` sheet (not migrated, contents unknown)
**Decision:** ADOPT as boundary conditions
**Rationale:** Anti-goals are boundary conditions that define the solution space — what IonWave is NOT. Eight constraints with specific temptation triggers (e.g., no new flavor until $50K MRR). Danilo's ecommerce domain expertise makes these credible operational constraints. Our File 37 has an anti_goals sheet but it's unmigrated and likely less developed. Adopt Danilo's as canon; reconcile with File 37 content if/when it's migrated.
**Decided by:** Caio
**Hypotheses affected:** None directly — boundary conditions constrain the solution space rather than making testable claims
**Data changes required:** Register anti-goals as boundary conditions in systems architecture. Temptation triggers are parameters on those boundaries.
**Status:** DECIDED

### REC-002f | 2026-02-05 | BCL-0 Sub-decision: Thesis Structure (16 Required Decisions) + Downstream Reads
**Cluster:** BCL-0 (Thesis & Meta)
**Danilo TUP(s):** M0 — `1204_m0_thesis_structure.json`, `1205_m0_thesis_downstream.json`
**Bootstrap File(s):** data/01_strategic_foundation/thesis.json, data/hypotheses/registry.json, IonWave/ICP_Analysis.md, IonWave/Financial_Model_Revenue_Validation.md
**Decision:** ADOPT format as OpKit for M0; our answers fill the fields
**Rationale:** Danilo's thesis structure is a decision-forcing checklist: 16 fields across ICP (3), Positioning (3), Product (3), Distribution (2), Finance (2), Kill Criteria (2), plus a downstream map showing which clusters consume which fields. Our Bootstrap work already answers most of these (thesis.json has positioning, ICP analysis has customer definition, financial model has price point and COGS), but they're scattered across files. Danilo's contribution is the checklist format — a single place that forces all 16 to be explicit. Adopt as an OpKit for the thesis deliverable. The downstream reads map (1205) complements our manifest.json dependency chains with a field-level view.
**Decided by:** Caio
**Hypotheses affected:** None — this is a scaffolding/navigation tool
**Data changes required:** Register thesis structure checklist as OpKit for M0. Populate fields by cross-referencing existing Bootstrap answers. Downstream reads map to be integrated with manifest.json dependency system.
**Status:** DECIDED

### REC-002i | 2026-02-05 | BCL-0 Sub-decision: Bootstrap Canon Confirmation
**Cluster:** BCL-0 (Thesis & Meta)
**Danilo TUP(s):** M0 (thesis, ODD-1 overlap)
**Bootstrap File(s):** data/01_strategic_foundation/ (all), data/hypotheses/ (all), IonWave/*.md (analysis deliverables)
**Decision:** BOOTSTRAP CANON — these assets are definitive and not overwritten
**Rationale:** The following represent validated analytical work product constituting the Imagination Passet content produced through our Bootstrap process. Danilo's model does not replicate them:
1. **Narrow thesis** (thesis.json) — supersedes Danilo's ODD-1 ($30K MRR/18mo replaces $100K/12mo)
2. **8 hypotheses** + registry + index + validation_log — ontological primitive with no Danilo equivalent
3. **Porter's Five Forces Analysis** — structural industry analysis with 5 forces scored
4. **Marine Plasma Market Sizing** — five-signal Seaonic revenue triangulation, sub-segment reframing
5. **Financial Model Revenue Validation** — 3-scenario month-by-month model
6. **ICP Analysis** + dialogue summary — validated archetypes with psychographic depth
7. **Migrated JSON data** (Files 01, 02, 03A, 03B — 27 sheets with `_meta` envelopes, A/B/C/D grades)
8. **Assumptions register** with provenance, confidence grades, and cross-file tension flags
9. **Strategic Foundation Analysis** — thesis reconciliation, capital tension, intelligence gaps
10. **Hypothesis Dependency Audit** — 53 cross-references across 13 documents
11. **Dialogue summaries** (Strategic Foundation, Porter's, ICP) — traceability records with UPGRADED/RESOLVED outcomes
**Decided by:** Caio
**Hypotheses affected:** All — this decision confirms HYP-001 through HYP-008 as canon
**Data changes required:** None — these are already in the data layer. Ensure Danilo's ODD-1 content does not overwrite the narrow thesis during any future migration.
**Status:** DECIDED

### REC-002h | 2026-02-05 | BCL-0 Sub-decision: M34 (Trade Architecture), M38 (Strategic Frameworks), M39 (Conceptual)
**Cluster:** BCL-0 (Thesis & Meta)
**Danilo TUP(s):** M34 (24 planned tabs), M38 (44 planned tabs), M39 (14 planned tabs)
**Bootstrap File(s):** File 34 (Performance & Optimization, not migrated), File 37 (Strategic Initiatives, not migrated)
**Decision:** SKIP — 100% template, no substantive content; Danilo has writings elsewhere he can fill in
**Rationale:** All three TUPs are entirely template/placeholder — zero content behind the tab names. M38's 44 tabs (game physics, eigenform tracker, Markov blanket audit, beauty score) and M39's 14 tabs (implicate/explicate order, love as mutual information) are ambitious vocabulary but no content. Our equivalent files (34, 37) are also unmigrated and thin. Danilo has various writings on these conceptual topics beyond what's in the Ops Model; he can populate these when the time comes. Not blocking any current work.
**Decided by:** Caio
**Hypotheses affected:** None
**Data changes required:** None
**Status:** DECIDED

### REC-002g | 2026-02-05 | BCL-0 Sub-decision: Command Center
**Cluster:** BCL-0 (Thesis & Meta)
**Danilo TUP(s):** M40 — `924_command_center.json`
**Bootstrap File(s):** File 24 (Command & Navigation) — `command_center` sheet (not migrated)
**Decision:** DEFER — implementation-layer; Danilo's elaboration on his own prior work
**Rationale:** Pre-launch readiness checklist (18 items, Studio vs Operator responsibilities, blocker protocol, phase progression). Implementation-layer concern like the ODD system. Additionally, whatever exists in our File 24 was created by Danilo in the first place — this command center is an elaboration on that original work. Defer to implementation phase.
**Decided by:** Caio
**Hypotheses affected:** None
**Data changes required:** None now. Preserve for implementation phase.
**Status:** DECIDED

### REC-002e | 2026-02-05 | BCL-0 Sub-decision: ODD System (Compilation Map, Sequencer, Dependency Map)
**Cluster:** BCL-0 (Thesis & Meta)
**Danilo TUP(s):** M34 scope — `750_odd_compilation_map.json`, `752_odd_completion_sequencer.json`, `753_odd_dependency_map.json`
**Bootstrap File(s):** data/manifest.json (dependency chains)
**Decision:** DEFER — implementation-layer concern
**Rationale:** The ODD system (7 deliverables, L0-L6 maturity levels, 7-phase build order, critical path with bottlenecks) is an execution playbook — it describes how to build the actual business from the Trade documentation. This belongs to the Implementation Passet, not the Imagination Passet we're constructing. Danilo's ecommerce expertise makes this a valuable asset to preserve for when implementation begins. Not in current scope.
**Decided by:** Caio
**Hypotheses affected:** None
**Data changes required:** None now. Preserve for implementation phase.
**Status:** DECIDED

### REC-002c | 2026-02-05 | BCL-0 Sub-decision: Ontology Additions
**Cluster:** System-wide (surfaced during BCL-0 review)
**Danilo TUP(s):** Multiple — ODD compilation map, reference models, IP tabs
**Bootstrap File(s):** Existing ontological primitives (Hypothesis, TUP)
**Decision:** ADOPT four new ontological entities
**Rationale:** The reconciliation surfaced the need to formalize entities that were implicit in both systems:
1. **Controller** — feedback mechanism with parameters (thresholds), metrics (measured values), and reactive protocols (responses). Bifurcation points are the first instance. The full severity stack: Early Warning → Bifurcation → Kill.
2. **Observer** — composite state estimator that takes multiple signals and produces a legible assessment. Computational PMF is the first instance.
3. **OpKit** — a collection of documents that scaffold the generation of a deliverable. Contains Reference Models (examples of the type), templates, checklists, diagnostic tools. Each TUP (or element therein) has an associated OpKit. Navigation: given any TUP, Claude can find its OpKit.
4. **Metric** — a formalized individual measure with a defined source, collection method, and frequency. Feeds into both Controllers (as the measured value compared to parameters) and Observers (as input signals).
Additionally clarified: **IP (Industry Perspectives) tabs are NOT OpKits.** IPs are baselines and orientation — they tell you "here's the landscape." OpKits are scaffolding — they tell you "here's how to build the thing."
**Decided by:** Caio
**Hypotheses affected:** Architecture-level change; affects how all hypotheses, controllers, and observers are structured
**Data changes required:** Define Controller, Observer, OpKit, and Metric schemas in the systems architecture. Register OpKit associations per TUP in the data layer. Build navigation so Claude can locate OpKits for any TUP.
**Status:** DECIDED

### REC-003 | 2026-02-05 | DR & Creative
**Cluster:** BCL-3 (DR & Creative)
**Danilo TUP(s):** M11 (VSL Production), M12 (Ad Creative), M13 (Media Buying), M14 (Testing), M15 (Landing Pages)
**Bootstrap File(s):** File 09 (Brand & Messaging, 6 sheets), File 10A (Creative Strategy, 2 sheets), File 10B (Creative Production, 9 sheets), File 11A (Funnel Strategy, 8 sheets), File 11B (Pages & Email, 6 sheets), File 12 (Media & Acquisition, 5 sheets) — 36 sheets total, all XLSX-only, none migrated, none audited
**Decision:** DANILO CANON
**Rationale:** All six Bootstrap files in this cluster were originally prepared by Danilo. His Ops Model content is newer and represents his evolved thinking on the DR/creative domain — his area of ecommerce expertise. The Bootstrap files are his earlier work; the Ops Model is his revision. Defer to the newer version. Content includes execution-ready assets (VSL scripts, hook libraries, landing page copy, ad creative briefs, media buying playbooks) that reflect domain knowledge we don't independently possess. No Bootstrap analytical work product (hypotheses, analyses, validated data) exists in this cluster to preserve.
**Decided by:** Caio
**Hypotheses affected:** None directly — this cluster produces creative assets, not testable claims
**Data changes required:** When migrating BCL-3, use Danilo's Ops Model content as source rather than the original Bootstrap XLSX files. Consolidation candidates noted: 7 duplicate-suffix sheets across Files 10B, 11A, 11B should be merged.
**Status:** DECIDED

### REC-004 | 2026-02-05 | Operations & Infra
**Cluster:** BCL-6 (Operations & Infra)
**Danilo TUP(s):** M1 (Labor Deployment), M9 (Ecommerce Infra), M24 (Fulfillment), M30 (Analytics), M31 (Hiring), M35 (Execution Plans), M36 (Operational Infra), M37 (AI & Automation)
**Bootstrap File(s):** File 04 (Planning & Roadmaps, 10 sheets), File 15 (Operations & Fulfillment, 4 sheets), File 16 (Team & Organization, 7 sheets), File 18 (Analytics & Reporting, 7 sheets), File 19 (Systems & Automation, 6 sheets), File 28 (Process & Workflows, 7 sheets), File 31 (Implementation & Execution, 7 sheets) — 48 sheets total, all XLSX-only, none migrated, none audited
**Decision:** DANILO CANON
**Rationale:** All Bootstrap files in this cluster were originally prepared by Danilo. His Ops Model content is his evolved thinking. No Bootstrap analytical work product exists in this cluster — no migrations, no analyses, no hypotheses tied to these files. Operations is Danilo's ecommerce domain expertise. His newer version supersedes.
**Decided by:** Caio
**Hypotheses affected:** None
**Data changes required:** When migrating BCL-6, use Danilo's Ops Model content as source.
**Status:** DECIDED

### REC-006 | 2026-02-05 | Retention & Lifecycle
**Cluster:** BCL-4 (Retention & Lifecycle)
**Danilo TUP(s):** M17 (Email), M18 (SMS), M19 (Customer Lifecycle), M20 (Support), M21 (Subscriptions), M22 (Referral)
**Bootstrap File(s):** File 07 (Offer Strategy, 6 sheets), File 11B (Pages & Email, 6 sheets), File 14 (Community & Engagement, 5 sheets), File 27 (Customer Experience Journey, 13 sheets), File 30 (Risk & Crisis, 4 sheets) — 34 sheets total, all XLSX-only, none migrated, none audited
**Decision:** DANILO CANON
**Rationale:** Same pattern as BCL-3 and BCL-6. All Bootstrap files originally prepared by Danilo, no analytical additions from our Bootstrap work. His Ops Model is the newer version. SMS (M18) is net-new content with no Bootstrap equivalent. Email sequences (M17) are execution-ready assets from his domain expertise.
**Decided by:** Caio
**Hypotheses affected:** None
**Data changes required:** When migrating BCL-4, use Danilo's Ops Model content as source. Note File 11B overlap with BCL-3 — already flagged as DANILO CANON there.
**Status:** DECIDED

### REC-008 | 2026-02-05 | Governance & School
**Cluster:** BCL-7 (Governance & School)
**Danilo TUP(s):** M32 (School Model), M33 (Governance & CM)
**Bootstrap File(s):** File 32 (Quality & Standards, 13 sheets), File 33 (Governance & Structure, 9 sheets) — 22 sheets total, all XLSX-only, none migrated, none audited
**Decision:** DEFER
**Rationale:** School Model deferred per REC-011 (architecture decision). Bootstrap files originally prepared by Danilo, no analytical additions. Governance content (RACI, stakeholder maps) exists in both systems but neither has been through our analytical process. Defer until team scales and School Model relevance is revisited.
**Decided by:** Caio
**Hypotheses affected:** None
**Data changes required:** None now.
**Status:** DECIDED

### REC-005 | 2026-02-05 | Product & Science
**Cluster:** BCL-1 (Product & Science)
**Danilo TUP(s):** M5 (Formulation), M6 (Supply Chain), M7 (Regulatory), M8 (Brand Identity)
**Bootstrap File(s):** File 05A (Product Strategy, 5 sheets), File 05B (Formulation & Supply, 6 sheets), File 09 (Brand & Messaging, 6 sheets), File 17 (Legal & Compliance, 8 sheets), File 36 (Reference & Specifications, 16 sheets) — 41 sheets total, all XLSX-only, none migrated, none audited
**Decision:** DANILO CANON
**Rationale:** All Bootstrap files originally prepared by Danilo. His Ops Model content supersedes. No Bootstrap analytical work product in this cluster.
**Decided by:** Caio
**Hypotheses affected:** None
**Data changes required:** When migrating BCL-1, use Danilo's Ops Model content as source.
**Status:** DECIDED

### REC-007 | 2026-02-05 | Growth & Market
**Cluster:** BCL-5 (Growth & Market)
**Danilo TUP(s):** M10 (Pricing & Offer), M16 (Content & SEO), M23 (Influencer & Creator), M26 (Competitive Intel), M27 (Customer Research), M28 (Market Expansion), M29 (PR & Communications)
**Bootstrap File(s):** File 02 (Market Intelligence, 10 sheets, MIGRATED), File 03A (Customer Research ICP, 5 sheets, MIGRATED), File 03B (Customer Research VOC, 7 sheets, MIGRATED), File 07 (Offer Strategy, 6 sheets), File 13 (Content & SEO, 8 sheets), File 21 (Expansion & Growth, 7 sheets), File 22 (R&D, 4 sheets), File 25 (Partnerships & Influencers, 5 sheets) — 52 sheets total
**Decision:** DANILO CANON
**Rationale:** All Bootstrap files originally prepared by Danilo. His Ops Model content supersedes across the board. Note: Files 02, 03A, 03B are migrated to JSON and have associated analysis deliverables (Porter's, ICP Analysis, Market Sizing) — those analytical outputs are Bootstrap canon per REC-002i, but the underlying file content itself is Danilo's work. When migrating this cluster, Danilo's newer Ops Model versions replace the original XLSX content. The analytical deliverables and hypotheses system sit on top as a separate layer and are unaffected.
**Decided by:** Caio
**Hypotheses affected:** None — analytical layer (hypotheses, analyses) preserved separately per REC-002i
**Data changes required:** When migrating BCL-5, use Danilo's Ops Model content as source. Migrated JSON data in data/02, data/03a, data/03b may need to be reconciled with Danilo's newer content — the analytical outputs remain canon but the underlying data may be updated.
**Status:** DECIDED

---

## Pending Decisions Queue

| ID | Domain | Cluster | Recommendation | Priority | Blocker |
|----|--------|---------|----------------|----------|---------|
| REC-001 | Money & Legal | BCL-2 | DANILO CANON (investigate) | 1 | Margin crisis needs resolution |
| ~~REC-002~~ | ~~Thesis & Meta~~ | ~~BCL-0~~ | ~~MERGE (9 sub-decisions)~~ | ~~—~~ | ~~DECIDED 2026-02-05~~ |
| ~~REC-003~~ | ~~DR & Creative~~ | ~~BCL-3~~ | ~~DANILO CANON~~ | ~~—~~ | ~~DECIDED 2026-02-05~~ |
| ~~REC-004~~ | ~~Operations & Infra~~ | ~~BCL-6~~ | ~~DANILO CANON~~ | ~~—~~ | ~~DECIDED 2026-02-05~~ |
| ~~REC-005~~ | ~~Product & Science~~ | ~~BCL-1~~ | ~~DANILO CANON~~ | ~~—~~ | ~~DECIDED 2026-02-05~~ |
| ~~REC-006~~ | ~~Retention & Lifecycle~~ | ~~BCL-4~~ | ~~DANILO CANON~~ | ~~—~~ | ~~DECIDED 2026-02-05~~ |
| ~~REC-007~~ | ~~Growth & Market~~ | ~~BCL-5~~ | ~~DANILO CANON~~ | ~~—~~ | ~~DECIDED 2026-02-05~~ |
| ~~REC-008~~ | ~~Governance & School~~ | ~~BCL-7~~ | ~~DEFER~~ | ~~—~~ | ~~DECIDED 2026-02-05~~ |
| ~~REC-009~~ | ~~Studio Level~~ | ~~SCL-*~~ | ~~DEFER~~ | ~~—~~ | ~~DECIDED 2026-02-05~~ |
| ~~REC-010~~ | ~~Funnel Level~~ | ~~FCL-*~~ | ~~DEFER~~ | ~~—~~ | ~~DECIDED 2026-02-05~~ |
| ~~REC-011~~ | ~~Taxonomy Architecture~~ | ~~System-wide~~ | ~~ADOPT (Hybrid)~~ | ~~—~~ | ~~DECIDED 2026-02-05~~ |
