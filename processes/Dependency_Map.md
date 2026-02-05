# IonWave Dependency Map - File Relationships & Workflow

**Purpose:** Understand how files connect and depend on each other
**Use Case:** Know which files to update together, workflow sequences
**Last Updated:** 2026-02-04

> **NOTE:** Dependency chains and feedback loops are also encoded in `data/manifest.json`
> in machine-readable format. For Claude, `manifest.json` is the faster way to access this
> information. This document provides the human-readable narrative and update workflows.
>
> **File format status:** Files 01-03B are now JSON (in `data/`). Files 04-38 remain XLSX (in `IonWave/`).
> Dependencies work the same regardless of format.

---

## 📋 HOW TO USE THIS MAP

**When to use:**
- You're updating one file and need to know what else to update
- You're creating a workflow and need to know the sequence
- You want to understand data flow across the system

**Key Concepts:**
- **Feeds Into:** File A provides data/insights that inform File B
- **Requires:** File B cannot be created without File A
- **Updates Together:** Files should be updated in sync
- **Workflow Sequence:** The order files are typically created/used

---

## 🔄 CORE DEPENDENCY CHAINS

### Chain 1: Strategic Foundation → All Other Files

```
01_Strategic_Foundation
  ├─ Thesis & Assumptions
  └─ FEEDS INTO ↓
      ├─ 02_Market_Intelligence (validates market opportunity)
      ├─ 03A_Customer_Research_ICP (defines who we serve)
      ├─ 05A_Product_Strategy (what we build)
      ├─ 06_Unit_Economics (business model viability)
      └─ 04_Planning_Roadmaps (what we do when)
```

**Why this matters:** Changes to strategic foundation require reviewing ALL downstream files.

---

### Chain 2: Customer Research → Product → Messaging

```
03A_Customer_Research_ICP
03B_Customer_Research_VOC
  ├─ Customer insights & pain points
  └─ FEEDS INTO ↓
      ├─ 05A_Product_Strategy (product positioning)
      ├─ 05B_Formulation_Supply (product specs to solve pain points)
      ├─ 09_Brand_Messaging (how we talk to customers)
      ├─ 10A_Creative_Strategy (creative angles)
      └─ 11A_Funnel_Strategy (conversion optimization)
```

**Why this matters:** Customer insights drive product AND messaging decisions.

---

### Chain 3: Unit Economics → Financial Model

```
06_Unit_Economics
  ├─ LTV, CAC, margins
  └─ FEEDS INTO ↓
      ├─ 08_Financial_Model (revenue projections)
      ├─ 07_Offer_Strategy (pricing strategy)
      ├─ 20_Fundraising (how much capital needed)
      └─ 04_Planning_Roadmaps (what we can afford to do when)
```

**Why this matters:** Unit economics changes ripple through entire financial model.

---

### Chain 4: Product → Creative → Media

```
05A_Product_Strategy + 05B_Formulation_Supply
  └─ FEEDS INTO ↓
      09_Brand_Messaging
        └─ FEEDS INTO ↓
            10A_Creative_Strategy
              └─ FEEDS INTO ↓
                  10B_Creative_Production
                    └─ FEEDS INTO ↓
                        12_Media_Acquisition (what ads to run where)
```

**Why this matters:** Product changes cascade through entire creative pipeline.

---

### Chain 5: Funnel → Financial Model

```
11A_Funnel_Strategy
11B_Pages_Email
  ├─ Conversion rates at each step
  └─ FEEDS INTO ↓
      ├─ 06_Unit_Economics (affects CAC)
      ├─ 08_Financial_Model (revenue projections)
      └─ 18_Analytics_Reporting (what to measure)
```

**Why this matters:** Funnel performance directly impacts financial projections.

---

## 🔗 CROSS-FILE DEPENDENCIES BY DOMAIN

### STRATEGIC PLANNING

**Primary Files:**
- 01_Strategic_Foundation
- 02_Market_Intelligence
- 04_Planning_Roadmaps

**Dependencies:**
```
Market Intelligence REQUIRES:
  ├─ Strategic Foundation (what market to analyze)
  └─ INFORMS:
      ├─ Customer Research (who's in the market)
      ├─ Product Strategy (competitive positioning)
      └─ Unit Economics (market pricing context)

Planning & Roadmaps REQUIRES:
  ├─ Strategic Foundation (what we're building toward)
  ├─ Unit Economics (resource constraints)
  ├─ Team Organization (capacity constraints)
  └─ INFORMS:
      ├─ All execution files (timeline dependencies)
      └─ Fundraising (capital timing)
```

**Update Frequency:** Quarterly or when major strategic shifts occur

---

### CUSTOMER UNDERSTANDING

**Primary Files:**
- 03A_Customer_Research_ICP
- 03B_Customer_Research_VOC
- 27_Customer_Experience_Journey

**Dependencies:**
```
Customer Research ICP REQUIRES:
  ├─ Market Intelligence (market segments)
  └─ Strategic Foundation (target customer hypothesis)

Voice of Customer INFORMS:
  ├─ Product Strategy (what features to build)
  ├─ Brand Messaging (how to communicate)
  ├─ Creative Strategy (what resonates)
  ├─ Offer Strategy (what to bundle)
  └─ Funnel Strategy (objection handling)

Customer Journey REQUIRES:
  ├─ Customer Research (who they are)
  ├─ Funnel Strategy (touchpoints)
  └─ INFORMS:
      ├─ Pages & Email (content for each stage)
      ├─ Community Engagement (retention tactics)
      └─ Analytics (what to measure)
```

**Update Frequency:** Continuous - as new customer insights emerge

---

### PRODUCT DEVELOPMENT

**Primary Files:**
- 05A_Product_Strategy
- 05B_Formulation_Supply
- 36_Reference_Specifications

**Dependencies:**
```
Product Strategy REQUIRES:
  ├─ Strategic Foundation (positioning)
  ├─ Customer Research (needs & pain points)
  ├─ Market Intelligence (competitive landscape)
  └─ Unit Economics (cost constraints)

Formulation & Supply REQUIRES:
  ├─ Product Strategy (what to formulate)
  ├─ Reference Specifications (quality standards)
  └─ Legal Compliance (regulatory requirements)

These INFORM:
  ├─ Brand Messaging (product benefits)
  ├─ Creative Production (product imagery)
  ├─ Operations (fulfillment specs)
  └─ Financial Model (COGS)
```

**Update Frequency:** As product evolves

---

### BUSINESS MODEL & ECONOMICS

**Primary Files:**
- 06_Unit_Economics
- 07_Offer_Strategy
- 08_Financial_Model

**Dependencies:**
```
Unit Economics REQUIRES:
  ├─ Product Strategy (COGS)
  ├─ Offer Strategy (pricing)
  ├─ Funnel Strategy (conversion rates)
  ├─ Media Acquisition (CAC estimates)
  └─ Customer Research (LTV estimates)

Offer Strategy REQUIRES:
  ├─ Customer Research (willingness to pay)
  ├─ Market Intelligence (competitive pricing)
  ├─ Unit Economics (margin requirements)
  └─ Product Strategy (what we can bundle)

Financial Model REQUIRES:
  ├─ Unit Economics (per-customer economics)
  ├─ Media Acquisition (acquisition costs)
  ├─ Operations (fixed costs)
  ├─ Team Organization (payroll)
  └─ Planning Roadmaps (timing)

These INFORM:
  ├─ Fundraising (capital needs)
  ├─ Strategic Foundation (viability)
  └─ All operational decisions
```

**Update Frequency:** Monthly - as actuals come in

---

### BRAND & CREATIVE

**Primary Files:**
- 09_Brand_Messaging
- 10A_Creative_Strategy
- 10B_Creative_Production

**Dependencies:**
```
Brand Messaging REQUIRES:
  ├─ Strategic Foundation (brand positioning)
  ├─ Customer Research (target audience)
  ├─ Product Strategy (value propositions)
  └─ Market Intelligence (competitive differentiation)

Creative Strategy REQUIRES:
  ├─ Brand Messaging (voice & tone)
  ├─ Customer Research (what resonates)
  └─ INFORMS:
      ├─ Creative Production (what to create)
      ├─ Media Acquisition (ad performance)
      └─ Funnel Strategy (messaging consistency)

Creative Production REQUIRES:
  ├─ Creative Strategy (frameworks)
  ├─ Brand Messaging (copy guidelines)
  ├─ Product Strategy (product imagery)
  └─ FEEDS:
      ├─ Media Acquisition (ads to deploy)
      └─ Pages & Email (assets to use)
```

**Update Frequency:** Creative Production weekly, Strategy monthly

---

### ACQUISITION & CONVERSION

**Primary Files:**
- 11A_Funnel_Strategy
- 11B_Pages_Email
- 12_Media_Acquisition
- 13_Content_SEO

**Dependencies:**
```
Funnel Strategy REQUIRES:
  ├─ Customer Journey (touchpoints)
  ├─ Offer Strategy (what we're selling)
  ├─ Brand Messaging (how we communicate)
  └─ INFORMS:
      ├─ Pages & Email (content for each stage)
      ├─ Unit Economics (conversion rates)
      └─ Analytics (funnel metrics)

Pages & Email REQUIRES:
  ├─ Funnel Strategy (page types needed)
  ├─ Brand Messaging (copy)
  ├─ Creative Production (images/videos)
  └─ Customer Research (objection handling)

Media Acquisition REQUIRES:
  ├─ Creative Production (ads to run)
  ├─ Unit Economics (CAC targets)
  ├─ Financial Model (budget)
  └─ INFORMS:
      ├─ Unit Economics (actual CAC)
      ├─ Analytics (channel performance)
      └─ Financial Model (actual spend)

Content & SEO REQUIRES:
  ├─ Brand Messaging (voice)
  ├─ Customer Research (search intent)
  └─ INFORMS:
      ├─ Media Acquisition (organic traffic)
      └─ Funnel Strategy (top-of-funnel)
```

**Update Frequency:** Media & Content weekly, Funnel/Pages monthly

---

### OPERATIONS

**Primary Files:**
- 15_Operations_Fulfillment
- 16_Team_Organization
- 17_Legal_Compliance
- 19_Systems_Automation

**Dependencies:**
```
Operations REQUIRES:
  ├─ Product Strategy (what to fulfill)
  ├─ Financial Model (volume projections)
  ├─ Customer Journey (delivery expectations)
  └─ INFORMS:
      ├─ Financial Model (fulfillment costs)
      └─ Customer Experience (delivery quality)

Team Organization REQUIRES:
  ├─ Strategic Foundation (org needs)
  ├─ Financial Model (payroll budget)
  ├─ Planning Roadmaps (hiring timeline)
  └─ INFORMS:
      ├─ Financial Model (payroll actuals)
      └─ Planning Roadmaps (capacity constraints)

Legal Compliance CONSTRAINS:
  ├─ Product Strategy (what we can claim)
  ├─ Brand Messaging (how we communicate)
  ├─ Creative Production (ad compliance)
  └─ Pages & Email (disclosure requirements)

Systems & Automation REQUIRES:
  ├─ All operational processes defined
  └─ INFORMS:
      ├─ Team Organization (reduces headcount needs)
      └─ Financial Model (efficiency gains)
```

**Update Frequency:** Operations weekly, others monthly

---

### MEASUREMENT & OPTIMIZATION

**Primary Files:**
- 18_Analytics_Reporting
- 23_Decision_Support
- 34_Performance_Optimization

**Dependencies:**
```
Analytics REQUIRES:
  ├─ Funnel Strategy (what to measure)
  ├─ Unit Economics (target metrics)
  ├─ Media Acquisition (channel setup)
  └─ INFORMS:
      ├─ ALL FILES (actual vs. plan)
      └─ Decision Support (data for decisions)

Decision Support REQUIRES:
  ├─ Analytics (current state)
  ├─ Strategic Foundation (decision criteria)
  └─ INFORMS:
      ├─ Planning Roadmaps (go/no-go decisions)
      └─ Strategic Foundation (strategy pivots)

Performance Optimization REQUIRES:
  ├─ Analytics (what to optimize)
  ├─ Unit Economics (optimization targets)
  └─ INFORMS:
      ├─ All execution files (improvements)
      └─ Financial Model (impact of optimizations)
```

**Update Frequency:** Analytics daily/weekly, others monthly

---

### GROWTH & FUNDING

**Primary Files:**
- 20_Fundraising
- 21_Expansion_Growth
- 22_Research_Development

**Dependencies:**
```
Fundraising REQUIRES:
  ├─ Strategic Foundation (vision)
  ├─ Financial Model (capital needs)
  ├─ Unit Economics (proof of model)
  ├─ Market Intelligence (market size)
  ├─ Analytics (traction metrics)
  └─ ENABLES:
      ├─ Expansion Growth (capital for growth)
      └─ Team Organization (hiring)

Expansion Growth REQUIRES:
  ├─ Unit Economics (positive in core market)
  ├─ Operations (scalable processes)
  ├─ Financial Model (expansion budget)
  └─ INFORMS:
      ├─ Strategic Foundation (growth strategy)
      └─ Planning Roadmaps (expansion timeline)

Research & Development REQUIRES:
  ├─ Customer Research (unmet needs)
  ├─ Market Intelligence (opportunities)
  └─ INFORMS:
      ├─ Product Strategy (innovation pipeline)
      └─ Strategic Foundation (future positioning)
```

**Update Frequency:** As needed for specific initiatives

---

## ⚡ CRITICAL UPDATE WORKFLOWS

### Workflow 1: Changing Strategic Foundation
**Impact:** High - affects almost everything

**Update Sequence:**
1. Update 01_Strategic_Foundation
2. Review & adjust 02_Market_Intelligence (still aligned?)
3. Review & adjust 03A_Customer_Research_ICP (still right audience?)
4. Review & adjust 05A_Product_Strategy (still right product?)
5. Review & adjust 06_Unit_Economics (still viable?)
6. Review & adjust 04_Planning_Roadmaps (timeline changes?)
7. Communicate changes to all team members

**Est. Time:** 2-4 weeks for full cascade

---

### Workflow 2: Updating Unit Economics
**Impact:** Medium-High - affects financial model & strategy

**Update Sequence:**
1. Update 06_Unit_Economics (new LTV/CAC/margins)
2. Update 08_Financial_Model (new projections)
3. Update 20_Fundraising (if capital needs change)
4. Update 04_Planning_Roadmaps (if timeline affected)
5. Update 07_Offer_Strategy (if pricing needs adjustment)
6. Update 12_Media_Acquisition (if CAC targets change)

**Est. Time:** 1-2 days

---

### Workflow 3: Launching New Creative
**Impact:** Low-Medium - contained to creative/media

**Update Sequence:**
1. Create in 10B_Creative_Production
2. Deploy via 12_Media_Acquisition
3. Monitor in 18_Analytics_Reporting
4. If winning: Update 10A_Creative_Strategy (document what worked)
5. If losing: Archive, try new angles

**Est. Time:** Ongoing weekly

---

### Workflow 4: Monthly Financial Review
**Impact:** Medium - informs all decisions

**Review Sequence:**
1. Update actuals in 18_Analytics_Reporting
2. Compare to 08_Financial_Model projections
3. Update 06_Unit_Economics with actual LTV/CAC
4. If significant variance:
   - Update 08_Financial_Model assumptions
   - Review 04_Planning_Roadmaps timeline
   - Review 12_Media_Acquisition spend
   - Review 20_Fundraising capital needs
5. Document in 23_Decision_Support (what we learned)

**Est. Time:** 1 day

---

### Workflow 5: Quarterly Strategic Review
**Impact:** High - course corrections

**Review Sequence:**
1. Assess performance vs 01_Strategic_Foundation goals
2. Review 02_Market_Intelligence for changes
3. Review 03B_Customer_Research_VOC for new insights
4. Review 18_Analytics_Reporting trends
5. Update 04_Planning_Roadmaps for next quarter
6. Update team via 16_Team_Organization communication
7. Update 20_Fundraising if trajectory changes

**Est. Time:** 3-5 days

---

## 🎯 FILES BY UPDATE FREQUENCY

### Daily:
- 18_Analytics_Reporting (dashboards)
- 12_Media_Acquisition (ad management)

### Weekly:
- 10B_Creative_Production (new ads)
- 11B_Pages_Email (optimizations)
- 13_Content_SEO (publishing)

### Monthly:
- 06_Unit_Economics (actuals)
- 08_Financial_Model (variance review)
- 04_Planning_Roadmaps (progress check)
- 16_Team_Organization (HR updates)

### Quarterly:
- 01_Strategic_Foundation (strategy review)
- 02_Market_Intelligence (competitive scan)
- 03B_Customer_Research_VOC (insights synthesis)
- 04_Planning_Roadmaps (roadmap update)

### As Needed:
- 05A_Product_Strategy (product launches)
- 17_Legal_Compliance (regulatory changes)
- 20_Fundraising (funding rounds)
- 21_Expansion_Growth (new markets)

### Reference Only:
- 24_Command_Navigation
- 36_Reference_Specifications
- 37_Strategic_Initiatives

---

## 🔍 DEPENDENCY TROUBLESHOOTING

### "I want to change pricing"
**Affects:**
1. 07_Offer_Strategy (pricing tiers)
2. 06_Unit_Economics (margins, break-even)
3. 08_Financial_Model (revenue projections)
4. 09_Brand_Messaging (value communication)
5. 11B_Pages_Email (pricing pages)
6. 20_Fundraising (if valuation affected)

**Update in this order:** 7 → 6 → 8 → 9 → 11B → 20

---

### "I learned something new about customers"
**Affects:**
1. 03B_Customer_Research_VOC (document insight)
2. 09_Brand_Messaging (how we talk to them)
3. 10A_Creative_Strategy (what resonates)
4. 11A_Funnel_Strategy (objection handling)
5. Potentially 05A_Product_Strategy (if affects product)

**Update in this order:** 3B → 9 → 10A → 11A → (maybe 5A)

---

### "Our conversion rate changed significantly"
**Affects:**
1. 18_Analytics_Reporting (document the change)
2. 06_Unit_Economics (CAC impact)
3. 08_Financial_Model (revenue impact)
4. 11A_Funnel_Strategy (what to optimize)
5. Potentially 20_Fundraising (if trajectory changes)

**Update in this order:** 18 → 6 → 8 → 11A → (maybe 20)

---

### "We're entering a new market segment"
**Affects:**
1. 01_Strategic_Foundation (strategic shift)
2. 02_Market_Intelligence (new market research)
3. 03A_Customer_Research_ICP (new ICP)
4. 06_Unit_Economics (different economics?)
5. 09_Brand_Messaging (different messaging)
6. 12_Media_Acquisition (different channels)
7. ALL creative and funnel files

**This is a major change - plan 4-8 weeks for full implementation**

---

## 📊 DEPENDENCY METRICS

**Highly Connected Files (affect many others):**
1. 01_Strategic_Foundation → affects 15+ files
2. 06_Unit_Economics → affects 10+ files
3. 03B_Customer_Research_VOC → affects 8+ files
4. 08_Financial_Model → affects 8+ files

**Standalone Files (few dependencies):**
- 24_Command_Navigation
- 36_Reference_Specifications
- Most files in 27-38 range

**Update Cascade Risk:**
- **High:** Strategic Foundation, Unit Economics
- **Medium:** Customer Research, Financial Model, Product Strategy
- **Low:** Creative Production, Analytics, Most support files

---

## 🎓 BEST PRACTICES

### When Making Changes:
1. **Check this map first** - understand ripple effects
2. **Update in sequence** - follow dependency chains
3. **Document changes** - note what you updated and why
4. **Communicate broadly** - if high-impact, tell team
5. **Verify consistency** - check dependent files align

### When Creating New Content:
1. **Identify dependencies** - what do you need first?
2. **Gather inputs** - pull from source files
3. **Create deliverable** - in appropriate file
4. **Update downstream** - cascade as needed
5. **Test consistency** - verify alignment

### When Something Feels Wrong:
1. **Trace dependencies** - what should this connect to?
2. **Check source files** - are inputs current?
3. **Verify calculations** - recalculate from source
4. **Look for conflicts** - inconsistencies between files
5. **Update systematically** - fix root cause, cascade

---

## 🎯 EXECUTION SEQUENCE — FILE IMPROVEMENT ORDER

**Purpose:** Given that we're improving 38 Trade files from 4-6/10 to 8-9/10, this section defines the optimal order to work on them, based on dependency position (upstream first), current quality, and Track A/B classification.

**Last Updated:** 2026-02-04

### How to Use This Table

1. Work top-to-bottom within each tier
2. Don't improve a downstream file until its upstream dependencies are at least 6/10
3. Track A work (Claude-driven) can proceed independently; Track B (human data collection) runs in parallel
4. Update the Quality Status column as audits are completed

### Tier 1: STRATEGIC FOUNDATION (improve first — everything depends on these)

**Format:** All Tier 1 files migrated to JSON (`data/`). Edit JSON directly, no XLSX needed.

| Priority | File | Format | Current Quality | Audited? | Key Blocker | Track | Next Action |
|----------|------|--------|----------------|----------|-------------|-------|-------------|
| 1.1 | 01_Strategic_Foundation | JSON | ~6.5/10 (w/ Analysis + Dialogue + Market Sizing) | ✅ Session #5 | Theses reconciled; Persona dialogue complete (5 upgrades); Sub-segment sized (Seaonic ~$100-180K/yr; segment ~$300K-$1.5M; thesis reframed — marine plasma = differentiation tool). Remaining: no financial model | A + B | Build/audit 08_Financial_Model; validate $30K MRR Year 1 target |
| 1.2 | 02_Market_Intelligence | JSON | ~5.5/10 (w/ Porter's) | ✅ Session #5 | Market Data sheet empty; Porter's added but supplier data at D-grade | A + B | Fill Market Data sheet with research data; execute Gap 1 (supplier contact — human) |
| 1.3 | 03A_Customer_Research_ICP | JSON | ~7/10 (w/ ICP Analysis + Dialogue) | ✅ Session #5 | Sheets consolidated; JTBD + VOC applied; Persona dialogue complete (ICP-2026-02-04-001: 4 upgrades — job vs switch trigger, Weekend Warrior softened, Job 3 downgraded, positioning-economics tension). Remaining: Female Wellness + Fasting VOC gaps, positioning-economics tension | A | Research Female Wellness ICP (3-4 hrs); collect fasting-specific VOC (2-3 hrs); model unit economics by segment |
| 1.4 | 03B_Customer_Research_VOC | JSON | ~6/10 (v1.0.1) | Partial | Improved in prior session; LMNT customer voice at saturation (31 quotes) | A | Already improved; review for completeness after 01 is upgraded |

### Tier 2: PRODUCT & ECONOMICS (improve after Tier 1 is ≥6/10)

| Priority | File | Current Quality | Audited? | Key Blocker | Track | Next Action |
|----------|------|----------------|----------|-------------|-------|-------------|
| 2.1 | 05A_Product_Strategy | Not yet audited | ❌ | Requires 01, 02, 03 inputs | A | Audit; then apply Porter's positioning implications |
| 2.2 | 05B_Formulation_Supply | Not yet audited | ❌ | Requires supplier data (Gap 1) | B (human) | Blocked until supplier contact is made |
| 2.3 | 06_Unit_Economics | Not yet audited | ❌ | Requires 05A (COGS), 07 (pricing), 12 (CAC) | A + B | Audit; apply Porter's CAC benchmarks and margin analysis |
| 2.4 | 07_Offer_Strategy | Not yet audited | ❌ | Requires 03 (willingness to pay), 02 (competitive pricing), 06 (margins) | A | Audit; apply buyer power and substitute threat context from Porter's |
| 2.5 | 08_Financial_Model | Not yet audited | ❌ | Requires 06 (unit economics), 12 (media spend), 16 (team costs) | A + B | Audit; apply capital tension flag from Porter's analysis |

### Tier 3: BRAND & CREATIVE (improve after Tier 2 is ≥6/10)

| Priority | File | Current Quality | Audited? | Key Blocker | Track | Next Action |
|----------|------|----------------|----------|-------------|-------|-------------|
| 3.1 | 09_Brand_Messaging | Not yet audited | ❌ | Requires 01 (positioning), 03 (audience), 05A (value props) | A | Audit; apply Porter's sub-segment positioning strategy |
| 3.2 | 10A_Creative_Strategy | Not yet audited | ❌ | Requires 09 (messaging), 03 (what resonates) | A | Audit after 09 is improved |
| 3.3 | 10B_Creative_Production | Not yet audited | ❌ | Requires 10A (strategy), 09 (copy), 05A (product imagery) | B (execution) | Not improvable via analysis — needs actual creative work |

### Tier 4: ACQUISITION & CONVERSION (improve after Tier 3 is ≥6/10)

| Priority | File | Current Quality | Audited? | Key Blocker | Track | Next Action |
|----------|------|----------------|----------|-------------|-------|-------------|
| 4.1 | 11A_Funnel_Strategy | Not yet audited | ❌ | Requires 27 (journey), 07 (offer), 09 (messaging) | A | Audit |
| 4.2 | 11B_Pages_Email | Not yet audited | ❌ | Requires 11A, 09, 10B | B (execution) | Needs actual page/email creation |
| 4.3 | 12_Media_Acquisition | Not yet audited | ❌ | Requires 10B (ads), 06 (CAC targets), 08 (budget) | A + B | Audit; apply Porter's CPM/ad spend data |
| 4.4 | 13_Content_SEO | Not yet audited | ❌ | Requires 09 (voice), 03 (search intent) | A | Audit |

### Tier 5: OPERATIONS & INFRASTRUCTURE (improve in parallel with Tiers 2-4)

| Priority | File | Current Quality | Audited? | Key Blocker | Track | Next Action |
|----------|------|----------------|----------|-------------|-------|-------------|
| 5.1 | 04_Planning_Roadmaps | Not yet audited | ❌ | Requires 01, 06, 16 | A | Audit after Tier 1-2 improvements settle |
| 5.2 | 15_Operations_Fulfillment | Not yet audited | ❌ | Requires 05A/B (product specs), 08 (volume) | B (execution) | Blocked until product specs are finalized |
| 5.3 | 16_Team_Organization | Not yet audited | ❌ | Requires 01 (org needs), 08 (payroll budget) | A | Audit |
| 5.4 | 17_Legal_Compliance | Not yet audited | ❌ | Constrains 05A, 09, 10B | A | Audit; apply FTC/DSHEA context from Porter's |
| 5.5 | 19_Systems_Automation | Not yet audited | ❌ | Requires all ops processes defined | B (execution) | Later — after processes are defined |

### Tier 6: GROWTH & FUNDING (improve after Tiers 1-2 are solid)

| Priority | File | Current Quality | Audited? | Key Blocker | Track | Next Action |
|----------|------|----------------|----------|-------------|-------|-------------|
| 6.1 | 20_Fundraising | Not yet audited | ❌ | Requires 01 (vision), 08 (capital needs), 06 (proof of model), 02 (market size) | A | Audit; apply Porter's market structure context |
| 6.2 | 21_Expansion_Growth | Not yet audited | ❌ | Requires 06 (positive economics), 15 (scalable ops) | A | Later — post-launch concern |
| 6.3 | 22_Research_Development | Not yet audited | ❌ | Requires 03 (unmet needs), 02 (opportunities) | A | Later — post-launch concern |

### Tier 7: MEASUREMENT & OPTIMIZATION (improve when execution begins)

| Priority | File | Current Quality | Audited? | Key Blocker | Track | Next Action |
|----------|------|----------------|----------|-------------|-------|-------------|
| 7.1 | 18_Analytics_Reporting | Not yet audited | ❌ | Requires 11A (what to measure), 06 (targets) | A | Audit framework; real data comes post-launch |
| 7.2 | 23_Decision_Support | Not yet audited | ❌ | Requires 18 (current state), 01 (decision criteria) | A | Audit |
| 7.3 | 34_Performance_Optimization | Not yet audited | ❌ | Requires 18 (what to optimize) | A | Later — post-launch |

### Tier 8: SUPPORT & REFERENCE (low priority — improve opportunistically)

| Priority | File | Current Quality | Audited? | Key Blocker | Track | Next Action |
|----------|------|----------------|----------|-------------|-------|-------------|
| 8.x | 14_Community_Engagement | Not yet audited | ❌ | — | A | Low priority |
| 8.x | 24_Command_Navigation | Not yet audited | ❌ | Standalone | — | Reference only |
| 8.x | 25_Partnerships_Influencers | Not yet audited | ❌ | — | A | Low priority |
| 8.x | 27_Customer_Experience_Journey | Not yet audited | ❌ | Requires 03, 11A | A | Audit |
| 8.x | 28_Process_Workflows | Not yet audited | ❌ | — | A | Low priority |
| 8.x | 29_Data_Information_Mgmt | Not yet audited | ❌ | — | A | Low priority |
| 8.x | 30_Risk_Crisis_Management | Not yet audited | ❌ | — | A | Low priority |
| 8.x | 31_Implementation_Execution | Not yet audited | ❌ | — | A | Low priority |
| 8.x | 32_Quality_Standards | Not yet audited | ❌ | — | A | Low priority |
| 8.x | 33_Governance_Structure | Not yet audited | ❌ | — | A | Low priority |
| 8.x | 35_Training_Enablement | Not yet audited | ❌ | — | A | Low priority |
| 8.x | 36_Reference_Specifications | Not yet audited | ❌ | Standalone | — | Reference only |
| 8.x | 37_Strategic_Initiatives | Not yet audited | ❌ | — | A | Low priority |
| 8.x | 38_Cross_Functional_Support | Not yet audited | ❌ | — | A | Low priority |

---

## 🔄 FEEDBACK LOOPS (Downstream Challenges Upstream)

**Purpose:** The dependency chains above show how information flows DOWNSTREAM (01 → 02 → 05A → etc). But analysis sometimes reveals that downstream findings challenge upstream assumptions. These feedback loops must be tracked to prevent the system from building on flawed foundations.

**Active Feedback Loops:**

| Source (Downstream) | Target (Upstream) | Tension | Status | Discovered |
|---------------------|-------------------|---------|--------|------------|
| Porter's Five Forces Analysis (02) | 01_Strategic_Foundation (Thesis sheet) | Capital tension: $30-50K raise may be insufficient given rising CPMs (27% YoY), zero switching costs, and category creation costs. Porter's structural forces suggest more capital needed. | RESOLVED — flagged in assumptions; replacement $30K MRR target proposed (SF dialogue Round 4) | 2026-02-04, Persona Dialogue PFF-2026-02-04-001 Round 5 |
| Porter's Five Forces Analysis (02) | 01_Strategic_Foundation (ODD-1 vs Thesis) | Two conflicting theses exist. Porter's analysis supports the Thesis sheet's narrow marine plasma positioning over ODD-1's broad electrolyte market framing. | RESOLVED — ODD-1 reclassified as v0/superseded; Thesis sheet canonical; see Strategic_Foundation_Analysis.md v1.1.0 | 2026-02-04, Session #5 audit |
| 03B_Customer_Research_VOC | 01_Strategic_Foundation (Interview Insights) | VOC work produced 31 LMNT quotes at saturation but this data was never connected back to Strategic Foundation's Interview Insights Synthesis sheet. | RESOLVED — backfilled with LMNT proxy data; labeled as proxy; must be replaced post-launch | 2026-02-04, Session #5 audit |
| ICP Analysis (03A) | 06_Unit_Economics | Positioning-economics tension: segment with strongest strategic position (Daily Wellness) may have lowest WTP, creating margin tension with marine plasma COGS | OPEN — needs unit economics modeling by segment | 2026-02-04, Persona Dialogue ICP-2026-02-04-001 Round 4 |
| Strategic Foundation Analysis (01) | Sub-segment sizing | Marine plasma sub-segment has no published market size; narrow thesis rests on un-sized market; Seaonic revenue unknown | RESOLVED — Seaonic ~$100-180K/yr; segment ~$300K-$1.5M; thesis reframed in Marine_Plasma_Market_Sizing.md v1.0.0 | 2026-02-04, Persona Dialogue SF-2026-02-04-001 Round 1 |

**How to Use:**
- When upgrading an upstream file, check this table for active feedback loops that should inform the upgrade
- When a downstream analysis challenges an upstream assumption, add a row here
- Mark loops as RESOLVED when the upstream file has been updated to address the tension
- Include the discovery source (session, dialogue run, etc.) for traceability

---

## 📋 ANALYSIS DELIVERABLES (Non-xlsx files that feed into the system)

**Purpose:** Some analytical work lives outside the Trade xlsx files (in .md format for version control and persona dialogue). These deliverables connect into the dependency system and should be treated as inputs to the relevant Trade files.

| Deliverable | Location | Feeds Into | Grade | Persona Dialogue? |
|-------------|----------|-----------|-------|-------------------|
| Porter's Five Forces Analysis | IonWave/Porter_Five_Forces_Analysis.md (v1.1.0) | 02_Market_Intelligence (new sheet added), 01_Strategic_Foundation (feedback loop), 05A, 06, 07, 09, 20 | B- | Yes — PFF-2026-02-04-001 (8 rounds, saturation) |
| ICP Analysis | IonWave/ICP_Analysis.md (v1.1.0) | 03A_Customer_Research_ICP (new sheets added), 01_Strategic_Foundation (JTBD Job 3 → thesis positioning), 05A, 07, 09, 10A | B | Yes — ICP-2026-02-04-001 (8 rounds, saturation, 4 upgrades) |
| Strategic Foundation Analysis | IonWave/Strategic_Foundation_Analysis.md (v1.2.0) | 01_Strategic_Foundation (thesis reconciliation, Interview Insights backfill, Narrative Hypotheses evidence, capital tension, Assumptions update), 06, 08 | B | Yes — SF-2026-02-04-001 (8 rounds, saturation, 5 upgrades) |
| Marine Plasma Market Sizing | IonWave/Marine_Plasma_Market_Sizing.md (v1.0.0) | 01_Strategic_Foundation (Gap 5 sub-segment sizing), 02_Market_Intelligence (competitive landscape), 06_Unit_Economics (Seaonic pricing benchmark), 08_Financial_Model ($30K MRR validation) | B- | N/A — research deliverable |

*Add future analysis deliverables here as they are produced.*

---

**Created:** 2026-02-02
**Enhanced:** 2026-02-04 (added execution sequence, feedback loops, analysis deliverables, JSON migration notes)
**Owner:** Studio 3 Core Team
**Maintained:** As system evolves — update Quality Status column after each audit, Feedback Loops after each analysis
**Machine-readable version:** `data/manifest.json` (dependency_chains, feedback_loops arrays)
