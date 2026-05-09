# Cluster Rubric

Score each cluster on 6 dimensions, 1 (terrible) to 5 (excellent). Total /30.

## Decision rule

| Total | Verdict |
|---|---|
| **<15** | Skip. Cluster is too weak — diffuse, niche, or unfixable. |
| **15-21** | Maybe. Combine with another cluster or pivot the angle. |
| **22-26** | Strong. Build a wedge concept (`wedge-template.md`) and start outreach this week. |
| **27-30** | Suspiciously high. Either a winner or you're rose-tinting. Have a skeptical friend score independently. |

## The 6 dimensions

### 1. Frequency

What % of analyzed reviews mention this complaint?

| Score | Threshold |
|---|---|
| 5 | >25% of reviews mention it (top complaint by far) |
| 4 | 15-25% mention it |
| 3 | 8-15% |
| 2 | 3-8% (real but minority) |
| 1 | <3% (probably noise) |

**Why this matters:** Frequency = market size. A wedge that solves 25% of users' top pain has a much wider TAM than one that fixes a 3% niche annoyance.

**Caveat:** A 3-5% complaint with extreme severity (people uninstalling) can outscore a 30% complaint that's a mild annoyance. Use frequency × severity, not frequency alone.

---

### 2. Severity

How badly does the pain hurt?

| Score | Signal |
|---|---|
| 5 | Showstopper — users uninstall, churn, or cancel because of this |
| 4 | Major — users complain publicly, switch tools, but stay grudgingly |
| 3 | Annoyance — users tolerate it but mention it as a frustration |
| 2 | Vitamin — users wish it were better |
| 1 | Background grumble — listed but not felt |

**Heuristics for severity:**
- "I deleted the app because…" → 5
- "I'm switching to…" → 5
- "It drives me crazy that…" → 4
- "Wish they would fix…" → 3
- "It would be nice if…" → 2

---

### 3. Fixability (solo / 90-day MVP)

Could a solo founder ship a 80%-good fix in 30-90 days?

| Score | Signal |
|---|---|
| 5 | Pure software fix; no data dependencies; standard tech stack |
| 4 | Software + standard third-party APIs (Stripe, OpenAI, Twilio) |
| 3 | Requires non-trivial integration with the incumbent's data (OAuth, file import) |
| 2 | Requires partnerships, regulatory approval, or hardware |
| 1 | Cannot be fixed without scale (e.g., "the network has nobody on it") |

**Indie-hacker reality check:** If the fix requires you to negotiate API access from the incumbent, kill it. If it requires SOC 2 to even start selling, kill it (unless that *is* your wedge — which is its own play).

---

### 4. Audience size

How many people total feel this pain enough to pay?

| Score | Signal |
|---|---|
| 5 | 100K-1M+ paying-capable users (large category, indie-friendly) |
| 4 | 10K-100K (sweet spot for $5K-$50K MRR) |
| 3 | 1K-10K (viable indie product if WTP is high) |
| 2 | 100-1K (only viable as services or very high WTP) |
| 1 | <100 (not a business) |

**Indie-hacker note:** A score of 4 is often *better* than 5. Smaller audiences are less contested by big players, and you can know all your customers personally.

**Don't confuse total app users with "people who feel this complaint."** If only 5% of a 1M-user app feels this pain, your real audience is 50K — which is great.

---

### 5. WTP signal

Are people in the reviews / threads telling you they'd pay for an alternative?

| Score | Signal |
|---|---|
| 5 | "I'd pay $X for an app that just did this." Multiple users name a number. |
| 4 | "I'm paying for [competitor] because it does X" — they're already spending |
| 3 | They mention a workaround (Google Sheet, Zapier, manual) — paid time = WTP signal |
| 2 | They want a fix but free-only language ("why do I have to pay for this?") |
| 1 | Audience is allergic to paying (mostly free-tier users on principle) |

**Critical:** Public reviews almost never have someone name a price. So a 5 here is rare. A 4 (people paying for adjacent tools) is the realistic high.

**Indie-hacker pricing reality:**
- Mobile B2C: $5-30 one-time or $5-15/mo subscription
- Prosumer SaaS: $10-50/mo
- B2B SaaS niche: $50-300/mo

If the audience can't sustain those, the cluster is a 2 or below.

---

### 6. Defensibility (vs. incumbent retaliation)

If you launch and start gaining users, can the incumbent kill you by shipping the fix?

| Score | Signal |
|---|---|
| 5 | Incumbent structurally won't fix this (their growth team needs the broken behavior) |
| 4 | Incumbent has been ignoring this for 3+ years; they probably won't pivot |
| 3 | Incumbent might fix it eventually but would take 12+ months |
| 2 | Incumbent could fix it in a quarter if they noticed |
| 1 | Trivial fix; incumbent will copy if you become a threat |

**Examples of structural non-fixes (great score 5 candidates):**
- Calm doesn't ship offline-first because it kills daily-active-user metrics
- Notion doesn't ship a "simple mode" because their growth depends on power users
- Salesforce doesn't ship simple pricing because their sales-led model needs RFPs
- Strava doesn't ship privacy-by-default because their growth depends on social sharing

These are the **anti-incumbent wedges** — features the incumbent *can't* ship without hurting their core metric.

---

## Worked example

**Cluster:** "i lose my streak from one missed day" (meditation app)

| Dimension | Score | Reasoning |
|---|---|---|
| Frequency | 4 | 18% of 1-2 star reviews mention streak loss |
| Severity | 5 | "Deleted the app" appears 11 times in this cluster |
| Fixability | 5 | Pure software — alternative streak logic with grace days |
| Audience size | 5 | Global meditation app users = 50M+; even 1% = 500K |
| WTP signal | 3 | Workaround = "I just stopped opening the app" — no spending evidence |
| Defensibility | 4 | Incumbents won't ship "skip days OK" because it hurts retention metrics |

**Total: 26/30 — Strong.**

**Wedge concept:** A meditation app where the streak forgives 1 missed day per week + 2 per month + lets you "pre-pay" rest days from previous meditation. Pricing: $5-9/mo. ICP: people who deleted Calm/Headspace specifically over streak loss.

**Next step (this week):** DM 30 named complainers from Reddit + App Store reviews; ask them to test a Notion mockup of the streak logic.

---

## Common scoring errors

- **Inflating frequency** because you remember the loud reviews. Compute it numerically: count cluster-mentioning reviews / total reviews analyzed.
- **Inflating audience size** by using total app installs. Use the cluster's *share* of complaints applied to monthly active users.
- **Inflating WTP** because you've decided to build it. WTP must come from review evidence, not your hopes.
- **Underrating defensibility** because you fear competition. The right question is "would the incumbent want to fix this?" not "could they?"

## When to score multiple clusters together

Some wedges are bundles — solving 2-3 mid-scoring clusters at once. Score them combined if:
- The same ICP feels both pains
- A single product can address both without scope creep
- The combined frequency hits 30%+

If you have to bundle 4+ clusters to make a wedge work, the underlying market probably isn't there.
