# PM Interview Frameworks

The five frameworks that cover ~95% of PM interview questions. Teach these with worked examples, not definitions.

---

## The CIRCLES Method — Product Design

**Lewis C. Lin's framework.** For "Design a product for X" or "How would you improve Y?"

### C — Comprehend the Situation
- Clarify the goal: revenue, engagement, retention, acquisition, something else?
- Surface constraints: time, platform, existing users, regulatory
- Ask 2-3 clarifying questions — shows you don't jump to solutions
- Good openers: "Who is the primary user?" "What's the success metric?" "Are we greenfield or constrained to the existing product?"

**Failure mode:** Asking 10 questions. You're not gathering requirements, you're showing you know what matters.

### I — Identify the Customer
- List 2-3 potential user personas (be specific — "college students planning road trips" not "young users")
- Choose ONE to focus on and say why
- Describe context, jobs-to-be-done, current behavior

**Failure mode:** Picking the obvious persona. "Power users" is lazy. Pick the interesting segment — lapsed users, first-timers, cross-platform users.

### R — Report Customer's Needs
- List 3-5 user needs for the chosen persona
- Frame as problems, not solutions ("users need to find relevant content quickly" not "users need a search bar")

**Failure mode:** Listing features disguised as needs.

### C — Cut Through Prioritization
- Use Impact × Effort, RICE, or a 2x2
- Pick 1-2 needs to solve
- State your reasoning — there's no right answer, but there IS right reasoning

**Failure mode:** Saying "I'd prioritize all three." You have to choose.

### L — List Solutions
- 3+ solutions for your prioritized need
- Range from simple to ambitious
- Don't self-edit — breadth first

**Failure mode:** One solution described in detail. Breadth > depth here.

### E — Evaluate Trade-offs
- Compare on: user impact, technical feasibility, business value, time to ship
- Use a 2x2 or pros/cons matrix
- Show structured thinking, not gut feel

### S — Summarize Recommendation
- Commit to ONE solution
- Explain why over the others
- Name success metrics (leading + lagging)
- Name what you'd test first (MVP / A/B test setup)

### Worked Example: "How would you improve Instagram Stories?"

**C:** "A few quick questions: Are we focused on creator engagement, viewer engagement, or monetization? Any segment in mind? Technical constraints?" *(Hiring manager: creator engagement, no constraints.)*

**I:** "Three personas: power creators, casual creators, lurkers. I'll focus on casual creators — they're 60%+ of story creators but post infrequently because creation friction is high. Power creators are saturated; lurkers aren't a story problem."

**R:** Three needs for casual creators:
1. Reduce creation friction — too many steps to post
2. Increase confidence — anxiety about posting publicly
3. Better feedback — unclear if anyone saw their story

**C:** Prioritizing #1. Creation friction is the bottleneck — if people can't create easily, nothing else matters. Friction also compounds: one bad posting experience kills the next three attempts.

**L:** Four solutions:
1. "Quick Story" — one-tap capture and post
2. AI-assisted templates — suggest layouts based on photo content
3. Collaborative stories — lower the bar by sharing creation with friends
4. Draft mode — save and refine before posting

**E:** Quick Story = high impact, low effort. Templates = medium effort, good engagement potential. Collaborative = high effort, big upside if network effects kick in. Drafts = low impact, mostly solves a different problem.

**S:** "I'd recommend Quick Story — one-tap mode that captures, adds a smart filter, posts in under 3 seconds. Success metric: weekly story creators up 15% among casual segment. Guardrail: creator regret rate (stories deleted within 1 hour) stays flat. I'd A/B test first with casuals who haven't posted in 30+ days."

### CIRCLES Time Budget (8-12 min answer)

| Step | Time | Warning |
|---|---|---|
| C | 60-90s | Over 2 min = rambling |
| I | 60-90s | Skipping persona = disaster |
| R | 60-90s | Must be problems, not features |
| C | 60s | Must commit |
| L | 2-3 min | Most important section |
| E | 2 min | Don't skip |
| S | 1-2 min | Must include metrics |

---

## The AARM Method — Metrics Questions

**Lewis C. Lin's framework.** For "How would you measure X?" or diagnostic "Metric Y dropped — why?"

### A — Acknowledge
- Restate the metric and context
- Classify: diagnostic ("why did X drop?") vs design ("how would you measure X?")
- Clarify scope: time window, segment, platform

### A — Analyze
- Break the metric into components with an issue tree
- Example: Revenue = Users × Conversion × ARPU → which component moved?
- Go 2-3 levels deep before jumping to causes
- For diagnostics: external (market, competition) vs internal (product change, bug, seasonality, marketing)

### R — Recommend
- Based on analysis, recommend which area to investigate or which metric to track
- Prioritize by: impact on business, ease of measurement, actionability

### M — Measure
- Define specific metrics with targets
- **Leading indicators** (predict future) + **lagging indicators** (confirm past)
- **Guardrail metrics** — things that shouldn't get worse
- **North Star** — single metric capturing core value

### Core Metric Frameworks to Name-Drop

**AARRR (Pirate Metrics):** Acquisition → Activation → Retention → Revenue → Referral

**North Star examples:**
- Airbnb = nights booked
- Slack = messages sent (by active teams)
- Spotify = time spent listening
- Facebook = DAU
- Stripe = payment volume

**Input vs Output:**
- Input = what you control (features shipped, experiments run, CS response time)
- Output = what results (revenue, retention, NPS)
- Good PMs track both; great PMs lead with input metrics

**Counter-metrics / Guardrails:** Always name one. "I'd track X is going up, and make sure Y doesn't get worse."

### Worked Example: "Instagram Stories engagement is down 8% MoM. Why?"

**A:** "Engagement is a compound metric — are we talking views, creates, replies, or time spent? Let's assume views per DAU since that's the main dashboard metric. Time window — is this gradual or a step-change?"

**A:** Issue tree:
```
Stories views per DAU ↓
├── Supply side (creation)
│   ├── Fewer creators? (check: weekly story creators)
│   ├── Fewer stories per creator?
│   └── Lower story quality → lower view-through?
├── Demand side (viewing)
│   ├── Fewer sessions?
│   ├── Shorter sessions?
│   └── Time shifted to Reels/feed?
└── Platform / external
    ├── Algorithm change
    ├── iOS 17 tracking change
    └── Competitor launch (TikTok feature?)
```

**R:** Most likely: demand-side shift to Reels. Stories cannibalization is a known pattern after Reels launches. I'd investigate in this order: (1) Reels time-spent trend over same window, (2) cohort analysis of story viewers who increased Reels time, (3) creation metrics to rule out supply-side.

**M:** Track:
- Leading: Stories % of total Instagram session time
- Lagging: Weekly story viewers, story view-through rate
- Guardrail: Total Instagram DAU, total time spent (don't want to fix stories by hurting overall engagement)
- Segment by: iOS vs Android, tenure cohort, creator vs lurker

### Diagnostic Question Cheat Sheet

When asked "Metric X dropped":
1. **Confirm** — is the data accurate? (Often overlooked — could be instrumentation)
2. **Scope** — all users or a segment? All platforms?
3. **Time shape** — sudden drop vs gradual decline vs unexpected spike
4. **Internal causes** — product change, pricing, bug, deprecation
5. **External causes** — market, competition, seasonality, platform policy
6. **Measurement** — what to track going forward

---

## The DIGS Method — Behavioral Questions

**Lewis C. Lin's framework.** For "Tell me about a time when..."

### D — Dramatize the Situation
Set the scene with stakes. Not "We had a project" but "We were 2 weeks from launch and our biggest customer threatened to churn."

**The stakes test:** If you removed the numbers and timeline from your opener, does it still sound important? If yes, you haven't dramatized.

### I — Indicate the Alternatives
Show you considered multiple approaches. "I could have done X, Y, or Z. I chose Y because..."

This is what separates DIGS from STAR. Alternatives demonstrate judgment — the single most valuable behavioral signal.

### G — Go Through What You Did
Walk through your specific actions step by step. Use "I" not "we" — the interviewer wants to know YOUR contribution. Name the people you influenced, the docs you wrote, the meetings you ran.

### S — Summarize the Impact
End with measurable results + what you learned. "The result was X. If I did it again, I'd change Y."

**The impact test:** If you can't say a number, you don't have a story yet.

### DIGS vs STAR

| | STAR | DIGS |
|---|---|---|
| Simplicity | Higher | Lower |
| Judgment signal | Weak | Strong |
| Senior interviews | Okay | Better |
| Best for | Early career | Mid+ career |

Use DIGS if you can. If a story really doesn't have alternatives (e.g., "tell me about a time you fixed a bug"), STAR is fine.

### The Story Bank

Build 5-7 stories that cover 80% of behavioral questions. Each should tag to multiple question types.

| Story | Covers |
|---|---|
| The high-stakes launch | execution, pressure, cross-functional, ambiguity |
| The hard no | leadership, saying no, influence, prioritization |
| The failed bet | failure, learning, resilience, data |
| The tough teammate | conflict, EQ, feedback, collaboration |
| The data surprise | data-driven, curiosity, pivoting, analysis |
| The user insight | user empathy, discovery, strategic change |
| The proud moment | impact, purpose, culmination |

For each story, prep: 60-second, 2-minute, and 5-minute versions.

### Worked Example: "Tell me about a time you disagreed with leadership."

**D:** "Six months into my last role, my VP wanted us to ship a paid tier for our core product by Q2. Our data showed free users weren't converting because of a missing collaboration feature, not because of a pricing wall. We were 4 months away, $2M of planned revenue on the line."

**I:** "I saw three options: (1) execute the plan, (2) publicly push back and risk my credibility, (3) run a 2-week research sprint and present a counter-proposal with data. I picked 3 — I wasn't going to win a hallway fight with the VP, but data would give me a fair hearing."

**G:** "I wrote a 1-page memo with three cohorts of user data. I ran 12 interviews, segmented by engagement level. I partnered with the finance lead to model both paths. I scheduled 30 minutes with my VP and walked her through it without a pre-read — she values live debate. I made the ask: 'Let me ship the collab feature in 6 weeks, gate the paid tier on conversion outcomes.'"

**S:** "She agreed. We shipped collab, free-to-paid conversion went from 2.1% to 5.8% in the quarter after. Revenue hit $2.4M — 20% over the original plan. What I learned: when I disagree with leadership, bring data and an alternative, not an objection. Objections get overruled; alternatives get debated."

---

## Fermi Estimation — Guesstimate Questions

For "Estimate the number of X in Y." No formal acronym, but a repeatable structure.

### The 5-Step Process

1. **Clarify scope** — time window, geography, segment, assumptions
2. **Pick a path** — top-down (population → segment → behavior) or bottom-up (unit × frequency × N)
3. **Break it down** — decompose into 3-5 multiplicative factors
4. **Populate with reasonable numbers** — use known anchors (US population = 330M, HH = 2.5 people, etc.)
5. **Sanity check** — does the order of magnitude feel right? If it came out as $50T or 3 doors, something is off.

### Known Anchors to Memorize

| Anchor | Number |
|---|---|
| US population | ~335M |
| US households | ~130M (2.5 people) |
| World population | ~8.1B |
| Smartphone users US | ~300M |
| Internet users worldwide | ~5.4B |
| iPhone users US | ~150M |
| Hours in a year | ~8,760 |
| Minutes in a day | 1,440 |

### Worked Example: "Estimate the annual US AirPods sales."

**Scope:** "New retail sales, consumer only, 2024, USA."

**Path:** Bottom-up. Sales = (iPhone users) × (AirPods ownership rate) × (replacement rate).

**Break down:**
- iPhone users US: ~150M
- AirPods ownership among iPhone users: ~40% (I'd refine this with research, but starting assumption)
- Effective replacement rate: every 3 years (battery degradation) → 33% replace annually
- New buyers entering the market: ~5% of iPhone base annually

**Populate:**
- Replacement: 150M × 0.40 × 0.33 = ~20M units
- New: 150M × 0.05 = ~7.5M units
- Total: ~27.5M units

**Sanity check:** At ~$150 ASP, that's ~$4B. Apple reports Wearables/Home/Accessories at ~$40B global, AirPods is the biggest line — US is maybe 1/3 of that, so ~$13B. My estimate is low by ~3x — suggests my ownership rate (40%) is too conservative. Real number is probably 60%+, which puts units at ~45M. Good interview answer says this: "My bottom-up gives $4B, but cross-checking against Apple's wearables segment suggests I'm underestimating ownership — realistic number is likely 40-50M units."

### Fermi Failure Modes

- **No clarifying questions** — you'll miss a scope constraint and waste 5 minutes
- **Top-down when bottom-up is cleaner** (or vice versa) — try both mentally, pick the shorter chain
- **Math mistakes under pressure** — write it down, don't try to do it in your head
- **No sanity check** — the sanity check is the most impressive part

---

## STAR (Backup for Behavioral)

For completeness. Use DIGS instead when you can.

- **S**ituation — context
- **T**ask — what you needed to do
- **A**ction — what you did
- **R**esult — what happened

The problem with STAR: no "alternatives considered" step, so it reads like a summary instead of judgment. At senior levels, this hurts you.

---

## Which Framework to Use — Decision Tree

```
Is it "Tell me about a time..."?
  → DIGS (STAR if simple)

Is it "Design a product" or "How would you improve X"?
  → CIRCLES

Is it "How would you measure X" or "Metric dropped, why"?
  → AARM

Is it "Estimate the number of X"?
  → Fermi

Is it "Should X buy / enter / partner with Y"?
  → Strategy (see question-bank-product-strategy.md)

Is it technical / system design?
  → Custom (see question-bank-technical.md)
```
