# 02 — RESEARCH PHASE
**What to search for, how to verify it, what to do when you can't.**

---

## SOURCE QUALITY HIERARCHY

Not all sources are equal. This hierarchy determines confidence grades.

| Tier | Source Type | Examples | Confidence Floor |
|------|------------|----------|-----------------|
| **1** | Audited filings / official disclosures | SEC Form C-AR, 10-K, company blog pricing pages | A |
| **2** | Primary company pages (verified live) | Official website pricing, product pages, "About" | A (if screenshot possible) / B (if URL-only) |
| **3** | Third-party corroboration (3+ sources agree) | Multiple review sites + news articles + forums converge | B |
| **4** | Industry reports / analyst coverage | IBISWorld, Shopify Research, category reports | B (if recent) / C (if >1 year old) |
| **5** | Single credible source** | One news article, one analyst mention | C |
| **6** | Social media / forums / reviews** | Reddit, Amazon reviews, Trustpilot | C (for individual claims) / B (if 3+ sources corroborate) |
| **7** | Derived calculations** | Our math from other data points | C (if methodology documented) / D (if assumptions heavy) |
| **8** | Industry benchmarks (generic)** | "DTC supplement brands typically..." | C (clearly labeled as benchmark, not competitor-specific) |
| **9** | Best guess / no source** | Reasoning from category knowledge | D |

**Key principle:** A single authoritative source (SEC filing, official pricing page) outranks 10 secondary sources. But secondary sources CAN corroborate to reach B-grade when primary is unavailable.

---

## WHAT TO SEARCH FOR (by metric type)

### Pricing
**Search queries:**
- `[competitor] pricing 2026`
- `[competitor] subscription cost per serving`
- `[competitor] vs [known competitor] price`

**Target:** Official website pricing page. If blocked (robots.txt), use third-party review sites that quote prices with dates.

**Confidence rules:**
- A: Live website price + date verified
- B: Price quoted in 3+ recent (< 3 months) sources that agree
- C: Price from single review article
- D: Price mentioned in passing, date unclear

### Revenue / Financial Scale
**Search queries:**
- `[competitor] revenue`
- `[competitor] SEC filing` (if they've done Reg CF/A crowdfunding)
- `[competitor] funding valuation`
- `[competitor] annual report`

**Target:** SEC filings first (EDGAR). Then funding databases (Crunchbase, PitchBook — often paywalled). Then news coverage.

**Confidence rules:**
- A: Audited financials from filing
- B: Triangulated from 3+ data points with documented methodology
- C: Single source estimate or calculation from uncertain inputs
- D: Back-of-envelope from traffic or ad spend assumptions

**Critical note on triangulation:** When triangulating, document EACH input separately with its own confidence grade. The output confidence is limited by the weakest input.

### Traffic / Engagement
**Search queries:**
- `[competitor] website traffic`
- `[competitor] similarweb`
- `[competitor] monthly visitors`

**Target:** Paid tools (SEMrush, SimilarWeb) give A-grade data but Claude can't access them. Free proxies: social follower counts × engagement benchmarks, Alexa rank (deprecated but sometimes cached), Google cache snippets.

**Confidence rules:**
- A: Paid tool data (requires human legwork — flag as type (a) interrupt)
- B: Free tool data corroborated by social metrics
- C: Proxy calculation with documented methodology
- D: Category-level guess

### Customer Voice
**Search queries:**
- `[competitor] reviews reddit`
- `[competitor] reviews amazon`
- `[competitor] trustpilot`
- `[competitor] complaints`
- `[competitor] vs [known competitor]`

**Target:** Actual customer quotes. Minimum 10 for B-grade, 30+ for A-grade. Track themes and frequency.

**Saturation rule:** Stop collecting when 5 consecutive quotes don't add a new theme. This is the stopping condition for customer voice research.

### Market Size / Category
**Search queries:**
- `[category] market size 2025 2026`
- `[category] industry report`
- `[category] TAM`

**Target:** Multiple free sources to triangulate. Premium reports (IBISWorld) are A-grade but paywalled — flag as upgrade path.

---

## VERIFICATION RULES

When you find a source, before recording it:

1. **Is this source current?** (< 6 months old preferred; > 1 year = flag for refresh)
2. **Is this the primary source or is it quoting someone else?** (Chase to primary if possible)
3. **Does this conflict with another source?** If yes and the gap is >50% → trigger type (b) interrupt (DISCREPANCY_INTERRUPT in routing). Pause and present to human before proceeding.
4. **Can this be corroborated?** Search for 1-2 additional sources that confirm or deny

---

## BLOCKED SOURCE HANDLING

When a source is inaccessible (robots.txt, paywall, login required):

1. **Record it as a type (a) interrupt** — do NOT pause. Just note it.
2. **Mark the metric as D-grade** (or whatever the best alternative source gives you)
3. **Add to upgrade path:** Exact URL, what data it would provide, estimated time for human to collect
4. **Continue research** using alternative sources

**Examples of common blocks:**
- drinklmnt.com often blocks automated access → use review sites that quote their pricing
- SEMrush/SimilarWeb require login → flag for human, use proxy calculations
- IBISWorld reports are paywalled → flag for human, triangulate from free sources

---

## RESEARCH COMPLETION CRITERIA

Research phase is complete when ALL of these are true:
- [ ] Pricing: at least one source found (any grade)
- [ ] Revenue/scale: at least one estimate produced (any grade)
- [ ] Product details: basic profile documented
- [ ] Customer voice: at least 5 quotes collected (more for Tier 1)
- [ ] All blocked sources logged for upgrade paths
- [ ] All discrepancies resolved or escalated

If any of these can't be met (truly zero information available), document WHY in the output and proceed with skeleton + D-grade + upgrade paths.
