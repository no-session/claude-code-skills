# Prioritization Framework

How we decide what to build. This framework ensures we invest our limited resources in the highest-impact work.

---

## Philosophy

Prioritization is the most important thing a product team does. Saying no is more valuable than saying yes. A clear framework doesn't make decisions for us — it makes our reasoning explicit, debatable, and improvable.

We prioritize at three levels:
1. **Strategic:** What problem spaces do we invest in? (Quarterly)
2. **Tactical:** What specific initiatives do we commit to? (Per cycle)
3. **In-flight:** When scope needs to change mid-cycle, what gives? (Continuous)

---

## Level 1: Strategic Prioritization (Quarterly)

### The Investment Portfolio

Each quarter, we allocate our total capacity across four buckets:

| Bucket | Target Allocation | Description |
|--------|------------------|-------------|
| **New Value** | ~40% | New features and capabilities that don't exist today |
| **Improve Existing** | ~30% | Enhancements to existing features based on customer feedback and data |
| **Keep the Lights On** | ~15% | Bug fixes, maintenance, infrastructure, security |
| **Explore** | ~15% | Research spikes, prototypes, strategic bets that may not pay off this quarter |

These are guidelines, not rules. The exact split shifts based on product maturity, market dynamics, and strategic priorities. But if any bucket drops to 0%, something is wrong.

### Strategic Scoring

For deciding which *problem spaces* to invest in, we evaluate:

| Criteria | Weight | Score (1-5) | Description |
|----------|--------|-------------|-------------|
| **Customer Impact** | 30% | | How many users are affected? How severe is the pain? |
| **Strategic Alignment** | 25% | | Does this advance our core value proposition and long-term vision? |
| **Revenue Impact** | 20% | | Does this drive acquisition, retention, expansion, or monetization? |
| **Feasibility** | 15% | | Can we ship a meaningful version in one cycle? |
| **Learning Value** | 10% | | Even if it doesn't "work," will we learn something critical? |

**Total Score = Σ (Weight × Score)**

---

## Level 2: Tactical Prioritization (Per Cycle)

### The RICE-Inspired Framework

For deciding which *specific initiatives* make it into a cycle, we use a modified RICE score:

**Impact Score = (Reach × Impact × Confidence) / Effort**

| Factor | Scale | How to Estimate |
|--------|-------|----------------|
| **Reach** | Number of users/accounts affected per quarter | Use product analytics, segment size data |
| **Impact** | 0.25 (minimal), 0.5 (low), 1 (medium), 2 (high), 3 (massive) | Based on expected effect on target metric |
| **Confidence** | 100% (high), 80% (medium), 50% (low) | Based on quality of evidence — user research, data, past experiments |
| **Effort** | Person-weeks of work | Engineering estimate (include design, QA, documentation) |

### Priority Tiers

| Tier | Meaning | Action |
|------|---------|--------|
| **P0 — Must Do** | Blocking revenue, breaking core UX, or critical for strategic commitment | Ships this cycle, no exceptions |
| **P1 — Should Do** | High impact on core metrics, strong evidence of customer need | Ships this cycle if capacity allows |
| **P2 — Could Do** | Meaningful improvement, moderate evidence | Next cycle candidate |
| **P3 — Won't Do (Now)** | Interesting but lower impact or insufficient evidence | Backlog, revisit quarterly |

### The Stack Rank Test

After scoring, stack rank all candidates and draw a line at your capacity. Everything above the line is committed. Everything below is explicitly not committed.

**Rules:**
- The line is sacred. Don't try to squeeze "just one more thing" in.
- If something new comes in mid-cycle that's above the line, something currently above the line must move below it.
- Show the full ranked list (including what's below the line) to stakeholders. Transparency about what we're *not* doing is as important as what we are.

---

## Level 3: In-Flight Prioritization (Continuous)

### When Scope Changes Mid-Cycle

Things change. A critical bug appears, a key customer has an urgent need, an assumption proves wrong. When this happens:

**The Trade-Off Conversation:**
1. **Name the new thing** and estimate its effort.
2. **Name what it replaces.** Something must come off the plate. "We'll just work harder" is not acceptable.
3. **Get alignment** from the pod lead and PM. If the trade-off is significant, loop in leadership.
4. **Communicate the change** to stakeholders who were expecting the displaced work.

### The Escalation Ladder

| Situation | Who Decides |
|-----------|-------------|
| Scope trade-off within a feature (e.g., cut an edge case) | Pod (PM + Eng Lead) |
| Trade one initiative for another within the same pod | PM + Eng Lead |
| Pull resources from one pod to another | PM + Leadership |
| Change quarterly strategic priorities | Leadership team |

---

## Common Prioritization Traps

### Traps to Avoid

1. **The Loudest Customer Wins.** One customer screaming ≠ a pattern. Look for signals from multiple sources.
2. **HiPPO (Highest Paid Person's Opinion).** Executive ideas go through the same framework as everything else.
3. **Sunk Cost Fallacy.** "We already built half of it" is not a reason to finish something that isn't valuable.
4. **Urgent vs. Important.** Fires feel urgent, but strategic work creates compounding value. Protect time for important, non-urgent work.
5. **Feature Parity Chasing.** Building something just because a competitor has it, without evidence that our customers need it.
6. **Complexity Hiding.** "It's just a small feature" often hides integration work, edge cases, and ongoing maintenance.

### Healthy Prioritization Smells

- Your backlog has more items marked "Won't Do (Now)" than "In Progress"
- You can explain to any stakeholder why their request isn't in the current cycle — with specifics
- Engineers aren't surprised by what they're building next
- You're saying "no" at least 3x more than you're saying "yes"

---

## Templates

### Quarterly Investment Allocation

| Bucket | This Quarter | Last Quarter | Notes |
|--------|-------------|-------------|-------|
| New Value | X% | X% | [Why the change?] |
| Improve Existing | X% | X% | [Why the change?] |
| Keep the Lights On | X% | X% | [Why the change?] |
| Explore | X% | X% | [Why the change?] |

### Cycle Prioritization Scorecard

| Initiative | Reach | Impact | Confidence | Effort | Score | Tier |
|------------|-------|--------|------------|--------|-------|------|
| [Initiative 1] | | | | | | |
| [Initiative 2] | | | | | | |
| [Initiative 3] | | | | | | |
| --- CAPACITY LINE --- | | | | | | |
| [Initiative 4] | | | | | | |

---

*This framework is a tool for thinking, not a substitute for judgment. When the numbers say one thing but your gut says another, explore why. Sometimes the framework is missing context. Sometimes your gut is wrong. The goal is to make the reasoning visible so we can improve it together.*
