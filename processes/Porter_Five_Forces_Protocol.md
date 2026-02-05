# Porter's Five Forces Protocol
**Version**: v1.0.0
**Author**: Claude (collaborative with Caio)
**Date Created**: 2026-02-04
**AI Model**: claude-sonnet-4-20250514
**AI Role**: Framework Application
**Human Validation**: None
**Purpose**: Step-by-step protocol for producing a Porter's Five Forces analysis deliverable
**Status**: Draft
**Related Files**: ci-protocol/07_FRAMEWORKS.md, ci-protocol/04_PERSONA_DIALOGUE.md, standards/Deliverable_Structure_Standards.md, standards/Document_Metadata_Standards.md
**Framework Type**: Strategic Analysis
**Target Grade**: B+ (achievable with Track A only; A requires Track B data collection)
**Time Budget**: 3-5 hours (Track A), 8-15 hours (with Track B)
**Validated Against**: IonWave Porter's Five Forces Analysis (PFF-2026-02-04-001)

---

## OVERVIEW

This protocol produces a Porter's Five Forces industry-structure analysis for the DTC premium electrolyte / marine plasma category. It follows the applied (not textbook) Porter's framework defined in ci-protocol/07_FRAMEWORKS.md, outputs in the three-section deliverable format per standards/Deliverable_Structure_Standards.md, and includes a mandatory persona dialogue stress-test per ci-protocol/04_PERSONA_DIALOGUE.md.

---

## PREREQUISITES

Before starting, read:
1. **ci-protocol/07_FRAMEWORKS.md** — Section: Competitive Strategist → Framework A: Porter's Five Forces (Applied). This is the analytical lens. Focus on the "what to look for" sections specific to DTC supplements.
2. **standards/Deliverable_Structure_Standards.md** — Three-section output format (Main Content + Intelligence Gaps + Scorecard). All confidence tagging rules.
3. **ci-protocol/04_PERSONA_DIALOGUE.md** — Persona dialogue rules, saturation framework, round logging.
4. **standards/Document_Metadata_Standards.md** — Metadata requirements for the output file.

Also read (for IonWave context):
5. **IonWave/01_Strategic_Foundation.xlsx** — Kill criteria, thesis, assumptions. Feeds into what the Porter's analysis must validate.
6. **IonWave/02_Market_Intelligence.xlsx** — Existing competitive data. Don't duplicate; build on it.
7. **SESSION_LOG.md** — Last 3 entries for any prior Porter's work or relevant context.

---

## PHASE 1: BASELINE ASSESSMENT (30 min)

**Goal:** Understand what data already exists before researching.

1. Read 02_Market_Intelligence.xlsx — identify which sheets contain data relevant to each of the five forces
2. Read 01_Strategic_Foundation.xlsx — identify kill criteria, assumptions, and positioning that the Porter's analysis must interact with
3. Check if any prior Porter's analysis exists (avoid duplication)
4. Document what you know, what you estimate, and what's blank for each force

**Output:** Mental model of existing data coverage per force.

---

## PHASE 2: WEB RESEARCH (1-2 hours)

**Goal:** Gather current, source-cited data to ground each force.

For each force, research the specific inputs defined in ci-protocol/07_FRAMEWORKS.md:

### Force 1 — Threat of New Entrants
- Capital requirements to launch and scale a DTC supplement brand
- Recent new entrant activity in the electrolyte space
- Regulatory barriers (FDA/DSHEA, FTC advertising compliance)
- Paid social ad cost trends (CPM changes, CAC benchmarks)

### Force 2 — Bargaining Power of Buyers
- Customer price sensitivity (review analysis, Reddit discussions)
- Switching costs (subscription lock-in mechanisms, cancel friction)
- Information availability (comparison content, review density)
- Alternative availability (competitor count, substitute options)

### Force 3 — Bargaining Power of Suppliers
- Supplier landscape for key ingredients (marine plasma vs synthetic)
- Supplier concentration and switching costs
- Forward integration risk (do suppliers sell direct?)
- Exclusivity risk (are preferential arrangements possible?)

### Force 4 — Threat of Substitutes
- DIY alternatives (recipes, cost per serving, accessibility)
- Food-based substitutes and other product categories
- Customer willingness to substitute (community evidence)
- Price differential between substitutes and branded products

### Force 5 — Competitive Rivalry
- Major players, their revenue, positioning, and owned-channel advantages
- Market growth rate (TAM, CAGR data from market research firms)
- M&A and consolidation activity
- Ad spend trends and escalation signals

**Rules:**
- Cite every source with URL and verification date
- Assign confidence grades (A/B/C/D) to each data point per standards/Deliverable_Structure_Standards.md
- When data is unavailable, estimate with D-grade and document the upgrade path
- Prioritize data from the last 12-18 months

---

## PHASE 3: ANALYSIS (1-2 hours)

**Goal:** Produce the five-force analysis following the three-section deliverable structure.

### Section 1: Main Content
For each force:
1. Rate as LOW / MODERATE / HIGH (per ci-protocol/07_FRAMEWORKS.md verdict format)
2. State which factor(s) dominate the rating
3. Include all supporting evidence with confidence tags
4. Write a Strategic Implication for IonWave (what does this force mean for the business?)
5. Produce an Overall Industry Attractiveness summary

### Section 2: Intelligence Gaps
For each significant gap:
1. Follow the gap template from Deliverable_Structure_Standards.md exactly
2. Prioritize using the CRITICAL / HIGH / MEDIUM / LOW framework
3. Distinguish between Track A gaps (Claude can research) and Track B gaps (human must act)
4. Include specific validation steps with time estimates

### Section 3: Scorecard
1. Confidence overview table (per-force grade + key limitation)
2. Top 3 strategic implications (ACTIONABLE, not just summaries)
3. Upgrade shopping list (prioritized by impact, with time estimates)
4. Cross-reference to dependent files per processes/Dependency_Map.md

### Metadata
Apply full metadata per Document_Metadata_Standards.md, including:
- Version (start at v1.0.0)
- AI Model identifier
- AI Role: Framework Application
- Status: Draft (until persona dialogue is complete)
- Related Files list

---

## PHASE 4: PERSONA DIALOGUE (1-2 hours)

**Goal:** Stress-test the analysis through multi-persona review.

**This phase is MANDATORY.** The analysis must not be marked as complete or moved to Review status until the persona dialogue has been run and documented.

### Setup
1. Read ci-protocol/04_PERSONA_DIALOGUE.md (full protocol)
2. Generate a Protocol Run ID: `PFF-{YYYY-MM-DD}-{NNN}`
3. Have the full Porter's analysis in context

### Execution
1. Run dialogue rounds per 04_PERSONA_DIALOGUE.md structure
2. Log each round in the prescribed format
3. Apply UPGRADED outcomes to the analysis in real-time
4. Track saturation per detection rules (3 consecutive RESOLVED, or 2 UNRESOLVED restatements, or all personas agree)
5. Hard stop at round 8

### Key Areas to Challenge (specific to Porter's analysis)
- **Investor:** Challenge confidence grades, ask what happens if estimates are wrong by 2x, probe falsifiability
- **Anthropologist:** Demand customer voice evidence for buyer behavior claims, challenge assumed preferences
- **Strategist:** Probe competitive response scenarios, challenge defensibility window claims, test sub-segment framing

### Output
1. Apply all UPGRADED outcomes to the Porter's analysis file (bump version)
2. Produce a Persona Dialogue Summary file (per 04_PERSONA_DIALOGUE.md format)
3. Update Porter's analysis metadata:
   - Add `Persona Dialogue Run: {Protocol Run ID}`
   - Update Status: Draft → Review
   - Add Change Log entry listing upgrades applied

---

## PHASE 5: FINALIZATION (15 min)

1. Update VERSION_MANIFEST.md with the new file and version
2. Add to DOCUMENTATION_INDEX.md if not already present
3. Log all actions in SESSION_LOG.md
4. Flag dependent files for review per processes/Dependency_Map.md cross-references

---

## TRACEABILITY REQUIREMENTS

Every Porter's Five Forces analysis must have:

| Artifact | Location | Purpose |
|----------|----------|---------|
| Analysis deliverable | `IonWave/Porter_Five_Forces_Analysis.md` | The actual analysis (3-section format) |
| Dialogue summary | `IonWave/Porter_Five_Forces_Dialogue_Summary.md` | Evidence that analysis was stress-tested |
| Dialogue Run ID | In analysis metadata header | Links analysis to specific dialogue run |
| Session log entry | `SESSION_LOG.md` | What was done, when, with what findings |
| Version bump | In analysis metadata | Shows pre- and post-dialogue versions |

If any of these artifacts are missing, the analysis is not considered complete.

---

## QUALITY CHECKLIST

Before marking the analysis as complete, verify:

- [ ] All five forces have a LOW/MODERATE/HIGH rating with dominant factor stated
- [ ] Every factual claim has a confidence tag (A/B/C/D) with source
- [ ] Every estimate shows methodology
- [ ] All below-A grades have upgrade paths
- [ ] Intelligence Gaps section includes at least 3 gaps
- [ ] Each gap has: What We Estimate, Confidence, Why It Matters, Impact If Wrong, How to Validate, Timeline, Priority
- [ ] Scorecard matches actual content quality (no optimistic grading)
- [ ] Persona dialogue was run (Protocol Run ID in metadata)
- [ ] Dialogue summary saved as separate file
- [ ] Cross-references to dependent files listed
- [ ] Metadata complies with Document_Metadata_Standards.md
- [ ] Session log updated

---

## LESSONS FROM FIRST APPLICATION (PFF-2026-02-04-001)

The following lessons were extracted from the first application of this protocol to the IonWave Porter's Five Forces Analysis:

1. **The persona dialogue is where the real analytical value lives.** The initial analysis was competent but the dialogue surfaced 5 material upgrades that the solo analysis missed — particularly the exclusivity vs forward integration distinction in supplier power, the category creation framing, and the capital tension with the Strategic Foundation.

2. **Watch for overconfident strategic implications.** The initial analysis positioned the LMNT lawsuits as an "actionable opportunity" — the dialogue correctly downgraded this to "potential opportunity requiring validation." Solo analysis tends toward actionability bias; personas correct for this.

3. **Cross-file tensions are easy to miss.** The capital adequacy tension ($30-50K plan vs structural forces requiring more) only surfaced because the Investor persona connected the Porter's findings back to the Strategic Foundation. Make this connection explicit during Phase 3.

4. **The DIY substitute analysis benefits from specificity.** "You can't DIY marine plasma" sounded like a strong moat until the dialogue revealed that Biocean ampoules are available online. Always test moat claims against specific customer behaviors.

5. **Sub-segment framing needs the dual-level caveat.** Porter's forces operate at the broad market level (where customers shop); sub-segment positioning is strategy, not a separate market structure. State both levels explicitly.
