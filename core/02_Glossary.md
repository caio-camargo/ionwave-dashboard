# 02 - Glossary

**Purpose:** Quick reference for Studio 3 and project-specific terminology

---

## Organizational Terms

**Studio 3** - Venture studio building D2C businesses systematically

**Trade** - Individual business being built (e.g., IonWave)

**Operator** - Person executing Trade development, equity partner in their Trade

**Compliance Manager (CM)** - Direct oversight of Operators, grading deliverables, quality control. Currently: Anya.

**General Manager (GM)** - Operational architect, system implementer. Currently: Caio.

**Founder** - Strategic decision-maker, system designer. Danilo.

**Venture Partner (VP)** - Industry advisor and/or investor who supports a Trade. Provides domain expertise, makes introductions, may invest capital.

**Strategic Marketing Advisor** - Grading, thesis evaluation, marketing expertise. Currently: Rhen.

---

## Phase Terms

**Strategic Thesis** - First-stage deliverable validating market opportunity, applying W Formula to score viability

**W Formula** - Trade potential scoring formula: W = (P Ã— V Ã— R Ã— S) / X
- P = Pain (customer problem severity)
- V = Value (purchasing power)
- R = Recurring (subscription/repeat potential)
- S = Scale (market size)
- X = Complexity (execution difficulty)

**Imagination Sprint** - 21-day strategic planning phase. Deliverables: market research, ICP, brand strategy, unit economics, GTM architecture, etc. Output: validated business plan.

**Implementation Sprint** - 30-45 day asset production phase. Deliverables: 100+ ads, VSLs, landing pages, email sequences, store setup, etc. Output: ready-to-launch business.

**Ad Validation** - Testing ads with real spend to find winners (CTR >1.5%, CVR >2.5%, CAC <target)

**Fundraising** - Securing capital from VPs or external investors to fund inventory + ad scaling

**In-Process** - Live, operating business generating revenue

**Gate** - GO/NO-GO decision point between phases (e.g., Imagination Gate determines if Trade proceeds to Implementation)

---

## Documentation Terms

**OpKit** - Production support bundle containing everything needed to produce high-quality deliverables

**Production OpKit** - For repeatedly created deliverables across multiple Trades
- Example: Strategic Thesis OpKit, Market Landscape Map OpKit
- Contains: Instructions, Template, Graded Examples (A/B/C), Rubric

**Foundation OpKit** - For singular evolving foundational documents
- Example: Documentation Standards OpKit, Protocol Creation OpKit
- Contains: Target document, Brief, Design rationale, Historical record

**Protocol** - Standardized procedure for a specific task
- Example: "Deliverable Grading Protocol", "Operator Check-in Protocol"

**Controller** - Monitoring mechanism that watches a parameter and triggers responses
- Example: "CAC Controller" triggers alert if customer acquisition cost exceeds threshold

**Parameter** - Numeric value or threshold that defines system behavior
- Example: "Imagination Sprint Duration = 21 days", "Pass Threshold = 75/100"

**Passet** - Standardized folder structure for organizing Trade work
- Imagination Passet, Implementation Passet, Fundraising Passet
- Contains "void spaces" (templates to fill in)

---

## Quality Terms

**Grade** - Letter grade assessment (A/B/C/D/F) of deliverable quality
- A- or better = proceed
- B = acceptable but needs refinement
- C or below = revision required

**Grading Rubric** - Structured criteria for evaluating deliverable quality
- Point-based (e.g., 85+ points = A-)
- Category-based (Evidence, Analysis, Presentation)

**Reference Model** - Example deliverable showing what A/B/C grade looks like
- A-grade: Exemplary, use as template
- B-grade: Acceptable, shows minimum viable
- C-grade: Shows common mistakes to avoid

**Provenance** - Document history tracking
- Version history
- Who created/modified
- Why changes were made
- Risk classification

**Confidence Grade** - Honesty about data quality (A/B/C/D scale)
- A: Verified from authoritative source (SEC filing, official website, 3+ corroborating sources)
- B: Strong single source or good triangulation (credible news, industry reports)
- C: Industry benchmark applied or derived estimate with documented methodology
- D: Best guess with no solid source (blocked access, no data available)
- Key principle: D-grade is acceptable IF documented with upgrade path
- See 04_Working_Principles_updated.md for full inline quality documentation standards

---

## IonWave-Specific Terms

**IonWave** - Trade #84: Premium liquid marine plasma electrolytes, positioned between LMNT (mass market synthetic) and Seaonic (ultra-premium marine plasma)

**IonWave Files** - 38 organized Trade files covering all business domains
- Evolved from: v8 (88 sheets) → v10 (681 sheets, deprecated) → current organized structure
- Previous v10 maintained for reference only (very large, avoid opening unless necessary)
- Current files: 01_Strategic_Foundation through 38_Cross_Functional_Support
- See Master_Index.md for complete inventory of all sheets

**Market Landscape Map** - Competitive intelligence deliverable (part of 02_Market_Intelligence.xlsx)
- Completed during bootstrap phase as quality improvement example
- Key components: Competitor grid, market sizing, customer voice, positioning analysis

---

## Process Terms (This Project)

**Bootstrap** - Current phase: improving first example to discover methodology

**Track A Work** - Strategic analysis requiring no data collection tools
- Expert framework application
- Customer voice mining (web search)
- Competitive response scenarios

**Track B Work** - Data gathering requiring paid tools or manual collection
- SEMrush traffic data
- Paid market research reports
- Extensive competitor coverage

**Expert Framework** - Analytical lens applied to improve quality
- Examples: Porter's Five Forces, Skeptical Investor Lens, Customer Anthropologist

**Recursive Improvement** - Core methodology
- Improve example (IonWave) â†’ Extract patterns â†’ Codify process â†’ Test on next deliverable â†’ Refine

**4-6/10 â†’ 8-9/10** - Quality elevation target
- 4-6/10 = Danilo's heroic effort, good structure but missing evidence/depth
- 8-9/10 = Investor-grade, evidence-backed, strategic rigor, comprehensive

---

## Working Terms

**Question-Driven Workflow** - Formalized approach
1. User states goal
2. Claude asks clarifying questions
3. User answers
4. Claude produces deliverable
5. User validates, iterate or proceed

**Checkpointing** - Align before building
- Show thinking â†’ get feedback â†’ then build
- Prevents wasted work on wrong direction

**Forcing Function** - Requirement that forces quality
- Example: "30+ customer quotes required" forces actual evidence gathering
- Example: "Source URL for every claim" forces verification

---

## Documentation Standards

**Document Metadata** - Required metadata for all documents
- Version, Author, Date Created/Modified, AI Model (if applicable), Purpose, Status
- Enables version tracking, authorship clarity, AI transparency, lifecycle management
- See Document_Metadata_Standards.md for complete requirements and examples

**Version Manifest** - Central version tracking for all versionable files
- Tracks current version of all 38 Trade files + methodology docs + architecture docs
- Auto-increment patch (+0.0.1) by default, manual minor/major bumps
- See VERSION_MANIFEST.md for full manifest and versioning rules

**Deliverable Structure** - Mandatory three-section format for all deliverables
- Section 1: Main Content (with inline confidence tags [A/B/C/D | Source | Date])
- Section 2: Intelligence Gaps (what we don't know, impact if wrong, validation paths)
- Section 3: Scorecard (quality self-assessment, upgrade shopping list)
- See Deliverable_Structure_Standards.md for detailed requirements

**Inline Quality Documentation** - Every claim must self-document its quality
- Factual claims tagged: [Confidence: A/B/C/D | Source: URL | Verified: date]
- Estimates include: methodology, "could be wrong if" scenarios, validation path
- Analysis tagged: [Analysis: Claude | Framework: X | Validated: pending/yes]
- See 04_Working_Principles_updated.md for full tagging standards

---

## Common Abbreviations

**GM** - General Manager (Caio)
**CM** - Compliance Manager (Anya)
**VP** - Venture Partner
**ICP** - Ideal Customer Profile
**GTM** - Go-to-Market
**TAM/SAM/SOM** - Total/Serviceable/Obtainable Market
**CAC** - Customer Acquisition Cost
**LTV** - Lifetime Value
**COGS** - Cost of Goods Sold
**AOV** - Average Order Value
**CVR** - Conversion Rate
**CTR** - Click-Through Rate
**ROAS** - Return on Ad Spend

---

**Glossary complete. Proceed to 03_What_We_Did.md**
