# 08 — DEPENDENCY MAP
**What feeds what. What breaks when something changes. How the system routes updates.**

This is the structural backbone the PRD requires: "when upstream assumptions change, the system automatically identifies which downstream sections are affected." This file is what makes that possible.

---

## THE FOUR LAYERS

The Imagination deliverables are not a flat list. They have structure. Dependencies only flow downward — with one exception (noted below).

```
LAYER 1: RESEARCH          (no upstream dependencies — inputs come from outside)
  ├── Competitive Intel
  ├── Market Data
  ├── Benchmark Data
  ├── Voice of Customer
  └── Landed Cost Breakdown

LAYER 2: STRATEGY          (depends on Layer 1)
  ├── Thesis
  ├── ICP
  └── Assumptions Register

LAYER 3: FINANCIAL MODEL   (depends on Layers 1-2)
  ├── Unit Economics  ←──────────────┐
  ├── Offer Strategy  ──────────────→┘  ⚠️ CIRCULAR (see below)
  └── Sensitivity Analysis

LAYER 4: EXECUTION PLANNING (depends on Layers 1-3)
  ├── Decision Framework
  ├── Funnel Architecture
  ├── Creative Strategy
  ├── Cash Flow Model
  ├── Investor Narrative
  └── Choreography  (terminal — synthesizes everything)
```

---

## DEPENDENCY EDGES

Each edge below is a real data flow traced from the IonWave v8 sheets. Format: SOURCE → TARGET (what specifically flows).

### Layer 1 → Layer 2

```
Competitive Intel  → Thesis              (competitor landscape, threat assessment)
Competitive Intel  → ICP                 (competitor target audiences — define ours by contrast)
Market Data        → Thesis              (pricing matrix — where does IonWave sit?)
Voice of Customer  → ICP                 (actual pain language — who has this pain?)
Competitive Intel  → Assumptions Register (assumption A07: "LMNT won't respond")
```

### Layer 1 → Layer 3

```
Landed Cost        → Unit Economics      (COGS per box — the single most critical input)
Landed Cost        → Offer Strategy      (margin floor — sets the minimum viable price)
Landed Cost        → Sensitivity Analysis (COGS as stress-test variable)
Benchmark Data     → Unit Economics      (CAC/churn benchmarks as baseline assumptions)
Benchmark Data     → Sensitivity Analysis (industry ranges for stress testing)
```

### Layer 2 → Layer 3

```
Thesis             → Offer Strategy      (positioning determines price architecture)
ICP                → Offer Strategy      (who's buying determines AOV strategy)
```

### Layer 3 → Layer 3 (the circular dependency)

```
Offer Strategy     → Unit Economics      (AOV input)
Unit Economics     → Offer Strategy      (margin targets constrain pricing)
```

### Layer 3 → Layer 4

```
Unit Economics     → Sensitivity Analysis (base assumptions to stress-test)
Unit Economics     → Cash Flow Model     (revenue/margin shape the cash curve)
Unit Economics     → Decision Framework  (kill triggers derived from LTV:CAC)
Unit Economics     → Investor Narrative  (the math that makes it investable)
Unit Economics     → Choreography        (target numbers)
Offer Strategy     → Funnel Architecture (price points shape messaging)
Sensitivity Analysis → Decision Framework (thresholds that define GO/KILL)
```

### Layer 2 → Layer 4

```
Thesis             → Investor Narrative  (the bet — why this is investable)
ICP                → Creative Strategy   (psychographics determine angle categories)
ICP                → Funnel Architecture (audience temperature routing)
Assumptions Register → Decision Framework (what we're betting on)
```

### Layer 1 → Layer 4

```
Competitive Intel  → Creative Strategy   (competitor ad angles to steal/counter)
Voice of Customer  → Creative Strategy   (exact customer language for copy)
Landed Cost        → Cash Flow Model     (inventory cost timing)
Competitive Intel  → Investor Narrative  (market size proof)
Cash Flow Model    → Investor Narrative  (timeline to revenue/profitability)
```

---

## THE CIRCULAR DEPENDENCY: Offer Strategy ↔ Unit Economics

This is the only place dependencies flow upward. It requires special handling.

**The loop:**
```
Offer Strategy sets AOV ($47 sub / $59 one-time)
    ↓
Unit Economics uses AOV to calculate margin per order
    ↓
Unit Economics derives margin targets (need 60%+ GM)
    ↓
Offer Strategy uses margin targets to set price floors ($39 minimum)
    ↓
back to top
```

**How to handle it:** These two sheets must be solved as a joint optimization, not updated sequentially. When either input changes (COGS from Landed Cost, or ICP insights that shift AOV strategy), both sheets update together in a single pass. The system should treat them as one compound deliverable called PRICING_MODEL with inputs (COGS, ICP, Thesis positioning) and outputs (price architecture, margin stack, LTV:CAC).

**The shared inputs that trigger joint recalculation:**
- Landed Cost Breakdown changes (COGS)
- Thesis positioning changes (premium vs value)
- ICP changes (different segment = different willingness to pay)

---

## CASCADE SCENARIOS

These are the three most likely real-world disruptions, traced through the dependency graph to show exactly what breaks and in what order.

### Scenario A: COGS rises (supplier quotes come back higher)

This is the highest-risk cascade because Landed Cost Breakdown feeds 4 different sheets.

```
TRIGGER: Landed Cost base case COGS rises (e.g., $18.15 → $24.80)

IMMEDIATE (same layer):
  Unit Economics: margin drops from 40% → 20% at current price
  Offer Strategy: margin floor rises, $39 minimum no longer viable
  Sensitivity Analysis: kill trigger thresholds shift

JOINT RECALCULATION (the circular pair):
  Must solve: what price makes the math work at new COGS?
  Options: raise price to $59+ OR increase subscription rate OR both
  Output: new AOV, new margin stack, new LTV:CAC

CASCADE DOWN:
  Cash Flow Model: runway shrinks (lower margin = less cash per order)
  Decision Framework: GO criteria may now require higher CAC threshold
  Investor Narrative: numbers change — recheck investability story
  Choreography: target numbers update
```

### Scenario B: Competitive Intel discovers incumbent is 3x larger than estimated

This is the LMNT $206M scenario we already hit. Strategic layer changes but financial layer is mostly independent.

```
TRIGGER: Competitive Intel revenue estimate corrected (e.g., $66M → $206M)

IMMEDIATE:
  Thesis: threat assessment changes — incumbent is dominant, not moderate
  Strengths & Threats: LMNT threat severity rises
  Assumptions Register: A07 ("LMNT won't respond") confidence drops

CASCADE DOWN:
  Investor Narrative: "market proven" claim actually strengthens (bigger market)
    BUT competitive threat section needs rewrite
  Decision Framework: may need new kill trigger for incumbent response
  Risks: probability assessment on "LMNT launches marine plasma" rises

NOT AFFECTED:
  Unit Economics (doesn't depend on competitor revenue)
  Landed Cost (independent of competitive landscape)
  Offer Strategy (price set by our positioning, not their revenue)
```

### Scenario C: ICP shifts to a different segment

```
TRIGGER: ICP primary segment changes (e.g., male biohackers → female wellness)

IMMEDIATE:
  Creative Strategy: all angle categories wrong — rebuild
  Funnel Architecture: audience temperature routing changes
  Offer Strategy: willingness-to-pay, messaging, bundle strategy changes

CASCADE DOWN:
  Ad Copy Bank, Ad Specs: rebuild from new Creative Strategy
  Unit Economics: AOV may change if new segment has different price sensitivity
    → triggers joint recalculation with Offer Strategy
  Voice of Customer: collection priorities shift (different platforms, different language)

UPSTREAM RIPPLE:
  Thesis: differentiation strategy may need revision
    (if new segment has different competitive context)
```

---

## WHAT THE SYSTEM NEEDS TO DO WHEN SOMETHING CHANGES

When any deliverable is updated, the system must:

**1. Identify the changed deliverable's layer.**

**2. Look up all downstream edges from that deliverable** (use the edge list above).

**3. For each downstream deliverable, flag it as "needs review."** The flag should include:
   - Which upstream input changed
   - What specifically changed (the old value and new value, or the nature of the change)
   - Whether this is a numeric input (can auto-propagate) or a strategic input (requires human judgment)

**4. If the change hits the Offer↔UnitEcon circle, treat as joint recalculation.** Don't update one without the other.

**5. Interrupts:** 
   - Numeric changes that propagate cleanly (COGS number flows into a formula) → auto-propagate, flag for human review
   - Strategic changes that require interpretation (threat assessment changes) → pause, present to human as type (c) interrupt
   - Changes that activate kill triggers → pause immediately, type (d) strategic decision interrupt

---

## WHICH DELIVERABLES THE CI PROTOCOL CURRENTLY SERVES

The competitive intelligence protocol (files 00-07) produces output that feeds:

```
Competitive Intel ──→ Thesis
                  ──→ ICP  
                  ──→ Creative Strategy
                  ──→ Investor Narrative
                  ──→ Strengths & Threats
                  ──→ Assumptions Register (indirectly, via Thesis)
```

That's 6 downstream deliverables affected by CI protocol output. When the protocol produces or updates a competitive intelligence deliverable, the system should automatically flag all 6 for review, with notes on what changed and why.

---

## FUTURE MODULES NEEDED (in dependency order)

To cover the full PRD, modules must be built in this order — each one can only be built after its upstream dependencies have modules:

```
ALREADY BUILT:
  [x] Competitive Intel / Market Data    (files 00-08)

BUILD NEXT (Layer 1 — no upstream deps):
  [ ] Landed Cost Breakdown              ← highest-risk single input, build 2nd
  [ ] Benchmark Data                     ← feeds validation layer
  [ ] Voice of Customer                  ← feeds ICP and Creative Strategy

THEN (Layer 2 — depends on Layer 1):
  [ ] Thesis                             ← synthesis of CI + Market Data
  [ ] ICP                                ← depends on Thesis + VoC

THEN (Layer 3 — the financial model):
  [ ] Unit Economics + Offer Strategy    ← must be built as joint module (circular dep)
  [ ] Sensitivity Analysis               ← depends on Unit Economics

THEN (Layer 4 — execution planning):
  [ ] Decision Framework                 ← depends on UnitEcon + Sensitivity
  [ ] Creative Strategy                  ← depends on CI + ICP + VoC
  [ ] Funnel Architecture                ← depends on ICP + Offer + Creative
  [ ] Cash Flow Model                    ← depends on UnitEcon + Landed Cost
  [ ] Investor Narrative                 ← synthesis of everything
  [ ] Choreography                       ← terminal, synthesizes all layers
```

---

## QUICK REFERENCE: IMPACT LOOKUP

*"I just changed X. What else do I need to update?"*

| Changed | Affects | Severity |
|---------|---------|----------|
| Competitor pricing | Thesis, Offer Strategy positioning | MEDIUM |
| Competitor revenue | Thesis, Investor Narrative, Assumptions Register, Risks | HIGH |
| COGS (any scenario) | Unit Economics, Offer Strategy, Cash Flow, Sensitivity Analysis | CRITICAL |
| ICP segment | Creative Strategy, Funnel Architecture, Offer Strategy, VoC priorities | HIGH |
| Price point | Unit Economics, Funnel Architecture, Cash Flow, Investor Narrative | HIGH |
| Kill trigger threshold | Decision Framework, Choreography | MEDIUM |
| Subscription rate assumption | Unit Economics, LTV calculation, Cash Flow | HIGH |
| Churn rate assumption | Unit Economics, LTV calculation, Sensitivity Analysis | HIGH |
| Market size estimate | Investor Narrative, Thesis | LOW-MEDIUM |
| Ad benchmark (CAC/ROAS) | Unit Economics, Sensitivity Analysis, Decision Framework | MEDIUM |
