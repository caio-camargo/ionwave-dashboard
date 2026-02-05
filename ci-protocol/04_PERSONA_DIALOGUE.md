# 04 — PERSONA DIALOGUE
**Three personas stress-test the analysis. Saturation framework determines when to stop.**

---

## THE THREE PERSONAS

### Skeptical Investor
**Mindset:** "Show me evidence, not estimates. Would I write a check based on this?"
**Challenges:** Unsupported claims, overconfident estimates, missing validation paths
**Asks questions like:**
- "What's the source for this number? What if it's wrong?"
- "What scenario would make this analysis irrelevant?"
- "Where are the gaps that could blow up the thesis?"
- "Is this estimate falsifiable? How would we know if it's wrong?"

### Customer Anthropologist
**Mindset:** "What are actual customers saying? Show me their words, not assumptions."
**Challenges:** Assumed preferences, missing customer voice, anecdotal reasoning
**Asks questions like:**
- "Do we have quotes backing this claim?"
- "Are we projecting what we THINK customers want, or what they actually say?"
- "What are customers who LEAVE this competitor saying vs. those who stay?"
- "Is this pain point real or hypothetical?"

### Competitive Strategist
**Mindset:** "Why hasn't someone already done this? What's the structural reason this gap exists?"
**Challenges:** Naive competitive assumptions, missing response scenarios, underestimated incumbent advantages
**Asks questions like:**
- "If this opportunity is real, why hasn't [incumbent] already captured it?"
- "What's the defensibility window and what closes it?"
- "Are we underestimating how fast competitors can respond?"
- "What would we need to be true for this analysis to hold in 12 months?"

---

## DIALOGUE STRUCTURE

### How a Round Works

1. **Skeptical Investor** reviews the current analysis state and raises 1-2 challenges
2. **Customer Anthropologist** responds — either confirms with evidence, or raises a counter-challenge
3. **Competitive Strategist** synthesizes — either resolves the tension or escalates it as a genuine gap

Each round produces one of three outcomes:
- **RESOLVED:** The tension was addressed by existing evidence. No change to output needed.
- **UPGRADED:** The tension revealed a gap that can be filled from existing research. Update the analysis.
- **UNRESOLVED:** The tension is a genuine intelligence gap. Document it in the Gaps view.

### Round Logging

After each round, log:
```
ROUND [N]:
  INVESTOR_CHALLENGE: [1 sentence]
  ANTHROPOLOGIST_RESPONSE: [1 sentence]  
  STRATEGIST_SYNTHESIS: [1 sentence]
  OUTCOME: [RESOLVED / UPGRADED / UNRESOLVED]
  ACTION: [what changed, if anything]
```

---

## SATURATION FRAMEWORK

### Definition
Saturation = the dialogue is producing diminishing returns. New rounds are restating previously identified tensions rather than surfacing new ones.

### Detection Rules
Saturation is reached when ANY of these is true:
- **3 consecutive rounds produce RESOLVED outcomes** (nothing new surfacing)
- **The last 2 UNRESOLVED gaps are restatements** of gaps already documented
- **All three personas agree** the analysis is coherent (no new challenges)

### Hard Stop
**Maximum rounds: 8**

This is a safety valve, not a target. Most dialogues should saturate in 3-5 rounds. If we hit 8 without saturation, something is structurally wrong — either the analysis has a fundamental gap that can't be resolved without human input, or the personas are cycling. At round 8, stop regardless, document what's unresolved, and flag for human review.

### Saturation Log
When saturation is reached (or hard stop hit), record:
```
SATURATION_REACHED: [yes / hard_stop]
ROUNDS_RUN: [N]
REASON: [which detection rule fired, or "hard stop reached"]
UNRESOLVED_GAPS: [list]
TENSIONS_RESOLVED: [list]
```

---

## DIALOGUE OUTPUT

The dialogue itself is scaffolding — it doesn't appear in the main deliverable. But it produces two things:

### 1. Tensions that modify the analysis
Any UPGRADED outcome means the analysis needs updating before assembly. These changes happen in real-time as the dialogue runs.

### 2. Dialogue Summary (process document)
After the dialogue completes, produce a summary in this format:

```markdown
# Persona Dialogue Summary
**Competitor:** [name]
**Protocol Run:** [ID]
**Rounds Run:** [N]
**Saturation:** [yes/no — if no, hard stop at round 8]

## Tensions Surfaced

### [Tension 1 — brief title]
- **Raised by:** [persona]
- **Nature:** [what the challenge was]
- **Outcome:** [RESOLVED/UPGRADED/UNRESOLVED]
- **Resolution:** [how it was addressed, or why it remains open]

### [Tension 2 — brief title]
[repeat]

## Key Insights
[2-3 sentences: what the dialogue revealed that wouldn't have been caught by solo analysis]

## What Would Have Been Missed Without This Step
[1-2 specific examples of gaps or upgrades the dialogue surfaced]
```

This summary is saved as a process document alongside the deliverable. It's evidence that the analysis was stress-tested.

---

## PERSONA INTERACTION RULES

1. **Personas challenge the analysis, not each other.** They're not debating — they're each applying their lens to the same material.

2. **Customer Anthropologist can only make claims backed by collected quotes.** If there's no customer voice evidence, the Anthropologist says so — they don't fabricate.

3. **Skeptical Investor grades claims, doesn't dismiss them.** The challenge is "show me evidence" not "this is wrong." If evidence exists, the challenge is resolved.

4. **Competitive Strategist resolves structural questions.** "Why hasn't someone done this?" has an answer — it might be "they haven't yet but will" or "there's a structural barrier" or "they have, we just don't know about it."

5. **No persona can upgrade a claim's confidence grade unilaterally.** Confidence grades are determined by source quality (see 02_RESEARCH_PHASE.md), not by how convincing the argument sounds.

---

## EXAMPLE DIALOGUE (abbreviated)

**Round 1:**
- INVESTOR: "The revenue estimate is $206M based on SEC filing. But the filing is FY2023 — what if they've contracted significantly since then?"
- ANTHROPOLOGIST: "Customer voice shows continued high engagement — 30+ recent reviews across platforms, no signal of brand decline. Doesn't prove current revenue but suggests continued activity."
- STRATEGIST: "Ad library still shows 200+ active ads as of Jan 2026. A contracting company would typically reduce ad spend. Evidence suggests sustained scale."
- OUTCOME: RESOLVED (multiple signals support continued scale; note the aging risk in output)

**Round 2:**
- INVESTOR: "The competitive response scenario says LMNT won't enter marine plasma because it conflicts with their brand. But their $7M sampling program shows they're willing to experiment."
- ANTHROPOLOGIST: "No customer voice evidence that LMNT users are asking for marine plasma specifically. Sampling program targets acquisition, not product line expansion."
- STRATEGIST: "Sampling and product diversification are different strategic moves. But the $7M spend shows operational flexibility — they COULD pivot resources if marine plasma proved out. Lower probability than initially stated."
- OUTCOME: UPGRADED (adjust competitive response probability upward; document sampling flexibility)
