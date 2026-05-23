# Evaluation Rubric (Bootstrap / Indie Hacker Calibration)

Score each cluster (group of related verbatims, see Step 4 in `SKILL.md`) on five dimensions, 1–5 each. Total / 25.

This rubric is calibrated for **bootstrap economics** — small concentrated reach + high WTP wins, *not* "huge addressable market." If you score a cluster as if you're chasing a $100M ARR SaaS, you'll kill bootstrap-perfect ideas. Calibrate to ramen profitability ($5k–$10k MRR) and Calm Company territory ($50k–$200k MRR).

---

## 1. Pain intensity (1–5)

How much does this hurt the user, right now?

| Score | Signal |
|---|---|
| **5** — Hair on fire | Profanity, all-caps, "I hate", explicit threats to switch, posts at 2am, multi-paragraph rants |
| **4** — Daily friction | Repeated complaints, sighing language ("ugh, again"), workaround explicitly framed as "annoying" |
| **3** — Mild but persistent | "It would be nice if", "kind of frustrating", neutral tone |
| **2** — One-off irritation | Single complaint, no emotional weight, easily ignored |
| **1** — Vitamin | "Cool if existed" — interest but no urgency |

**Tell:** count negative emotional words per verbatim. >2 per 100 words = high intensity.

---

## 2. Frequency (1–5)

How often does the user hit this pain?

| Score | Signal |
|---|---|
| **5** — Multiple times per day | "Every time I", "constantly", "all day", workflow-blocking |
| **4** — Daily | "Every day", "first thing in the morning", "before I can start work" |
| **3** — Weekly | "Every Monday", "end of week", "weekly review" |
| **2** — Monthly | "Month-end", "every billing cycle", "quarterly" |
| **1** — Annually or less | Tax season, year-end, once-per-year ritual |

**Tell:** look for temporal anchors ("every", "always", "before [recurring event]"). Lower frequency = harder to keep someone subscribed. Vertical SaaS that solves a monthly pain (closing the books) can still work — but the pain must be excruciating to compensate.

---

## 3. Willingness to pay (1–5)

**THE MOST IMPORTANT DIMENSION FOR BOOTSTRAPPERS.** Reach without WTP is a charity. Rob Walling: "Don't build for people who won't pay."

| Score | Signal |
|---|---|
| **5** — Already paying for a worse solution | Using and complaining about a paid tool. Hiring freelancers/VAs ($300–$2k/mo). Paying for Zapier hacks. Building custom internal tools. Explicit "I would pay $X for this" comments. |
| **4** — Paying with time at a level that's clearly expensive | "I spend 5 hours/week", "my whole Monday morning", a full FTE doing X manually |
| **3** — Adjacent paid tools in the workflow | Audience uses paid tools nearby in the workflow (signals budget exists) |
| **2** — Free workarounds only | Spreadsheets, free Notion templates, manual processes — no current spend |
| **1** — Resistant to paying | "I wish [X] was free", "everything costs money", complaints about pricing as the primary pain |

**Bootstrap rule:** if 0/30 verbatims mention paying for *anything* in the workflow, the audience is wrong. Either pick a different audience or move on.

**ARPU calibration:**
- WTP=5 with "$50–$500/mo" signals → Track A territory
- WTP=5 with "$10–$50/mo" or "$50–$200 one-time" signals → Track B territory
- WTP=5 but with sub-$10 signals → likely too low for sustainable SaaS

---

## 4. Reach (1–5) — Bootstrap-inverted

**Counterintuitive:** for bootstrappers, reach is *goldilocks*, not "more is better." Too big = VC-backed competition; too small = math doesn't close.

| Score | Signal |
|---|---|
| **5** — Goldilocks: 1k–10k concentrated, addressable in 1–3 named channels at target ARPU | The bootstrap sweet spot. Big enough for $10k–$200k MRR. Small enough that big players ignore it. |
| **4** — 500–1k concentrated, OR 10k–100k with target ARPU | Either narrow + high-ARPU vertical SaaS, or broad prosumer market that still fits one-person scale |
| **3** — 100k–1M scattered across many channels | Larger market but harder to reach repeatably; risk of VC-backed competitor |
| **2** — <500, OR >1M and competitive | Either too small to support a business at target ARPU, or so large that VC-funded players will dominate distribution |
| **1** — Unreachable: no clear channel, no community, hard to identify in the wild | Even high WTP can't save this — you can't find them |

**Math check before scoring 5:**

- Track A: customer count × $100/mo > $10k/mo? (≈100 customers @ $100/mo for ramen profitable)
- Track B: customer count × $20/mo > $5k/mo? (≈250 customers @ $20/mo for ramen profitable)
- If no even at full market penetration → niche is too small **at this price point**. Either raise ARPU or pick a bigger niche.

**Math check before scoring 4 or below for "too big":**

- Are there already 3+ VC-funded startups in this space? If yes, downgrade reach by 1. You're competing with their CAC budgets, not just their products.

---

## 5. Solution gap (1–5) — Bootstrap-reframed

What's the current competitive landscape?

| Score | Signal |
|---|---|
| **5** — Horizontal tool bent for vertical use, OR disenfranchised user base | The bootstrap goldmine. Users already pay for Notion/Airtable/Excel + adapt it; you sell the purpose-built version. OR: a beloved tool died/got acquired/got worse, audience is actively shopping. |
| **4** — Many bad vertical solutions, no leader | Fragmented market, "I've tried X, Y, Z and none of them really work." Wedge = the one that actually fits the workflow. |
| **3** — One vocal monopolist with loud haters | Incumbent vulnerable on price, vertical fit, UX, or pricing model. Wedge = position against the specific complaints. |
| **2** — Established market with mostly-happy users | Hard to displace. Possible only with a sharp price/feature/positioning differentiator. |
| **1** — Greenfield in a hot space (AI, crypto, no-code) | Will attract well-funded competitors faster than you can ship. OR: zero solutions because no real market. |

**Wait — greenfield scores LOW?**

Yes, in bootstrap context. Greenfield in a hot space (AI agents, crypto infra) attracts VC money in months; you'll be outspent on CAC and integrations before you reach PMF. Greenfield in a cold space is usually because nobody wants it.

The bootstrap sweet spot is **"market exists, current solutions suck, no one with capital cares enough to dominate."**

If you're sure your greenfield is in a cold-but-real space (rare), score it 3, not 5 — the lack of competition is suspicious until proven otherwise.

---

## Composite score

Total /25.

| Score | Meaning |
|---|---|
| **22–25** | Pursue immediately; hand to `office-hours` |
| **18–21** | Strong candidate; pursue if it aligns with founder context |
| **14–17** | Mid; rework the wedge or pick a different audience slice |
| **10–13** | Weak; park and re-mine in 3–6 months |
| **<10** | Kill |

**Any dimension scoring 1 is a kill signal** regardless of total:

- **Pain = 1** → vitamin trap, never closes a sale
- **Frequency = 1** → high churn, user forgets you exist
- **WTP = 1** → no business model
- **Reach = 1** → no go-to-market path
- **Solution gap = 1** → too late or no real market

---

## VC-bait kill signals (auto-fail regardless of score)

The cluster maps to one of these shapes → kill it for bootstrap purposes:

- **Two-sided marketplace** (needs supply AND demand subsidized)
- **Pure network-effect / social product** (value scales with user count)
- **Ad-supported consumer model** (needs MAU scale)
- **Enterprise sales >$25k ACV** (long sales cycle, solo founder = bottleneck)
- **Hardware-dependent** (capital + ops burden)
- **Requires regulatory clearance** (PHI, banking, securities)
- **Competing on price in a commodity market** (race to bottom)
- **Pure "AI wrapper" with no audience moat** (commoditized by next model release)
- **Only customers are pre-monetization "creators" / "students" / unfunded hobbyists** (no WTP)

These are real opportunities — just not for you with this skill. Note them, move on.

---

## Sanity checks before scoring

Before applying this rubric, verify:

1. **At least 3 unrelated verbatims per cluster.** Rule of three. One vivid complaint can't be scored honestly.
2. **Verbatims span at least 3 months** OR multiple sources. Bursty pain may be situational (an outage, a viral bad event).
3. **You can name the persona in one sentence** including their vertical, role, or hobby + WTP context.
4. **You can name the track** (A: B2B micro-SaaS, B: Prosumer). Mixed-track clusters score badly — they're usually two opportunities pretending to be one.

If any fail, go back to mining before scoring. Premature scoring inflates conviction in noise.

---

## Worked example (Track A)

**Cluster:** "Solo bookkeepers can't easily reconcile Shopify + ad-spend + bank for their DTC clients"

| Dimension | Score | Reasoning |
|---|---|---|
| Pain | 5 | Multiple verbatims with profanity, "I hate Mondays", "this is killing me" |
| Frequency | 4 | "Every week", "end of month" — weekly + monthly pain |
| WTP | 5 | Multiple "we use [paid tool] and it doesn't work" + one "I'd pay $200/mo for this" |
| Reach | 5 | ~30k US-based DTC-focused bookkeepers (Bench, Pilot, indies). Concentrated in 2 subreddits + 1 Slack. Math: 200 customers × $150/mo = $30k MRR — solid Calm Company. |
| Solution gap | 4 | Many bad solutions (QBO, Xero, Bench, manual). No leader for the DTC-specific bookkeeper use case. |

**Total: 23/25 → Pursue.** Track A. Hand to `office-hours`.

---

## Worked example (Track B)

**Cluster:** "Indie game devs running paid playtests on itch.io can't easily collect structured per-build feedback"

| Dimension | Score | Reasoning |
|---|---|---|
| Pain | 4 | Multiple "ugh, Forms again", "playtest feedback is a mess" |
| Frequency | 4 | Every new build (= weekly for active devs) |
| WTP | 4 | Already pay for Notion ($10/mo), itch.io membership, sometimes UserTesting. One explicit "$20/mo would be a no-brainer." |
| Reach | 5 | ~5k–10k active itch.io devs running paid playtests. Concentrated in r/gamedev, IndieGameDevs Discord, itch.io community. Math: 400 customers × $19/mo = $7.6k MRR. |
| Solution gap | 5 | Horizontal tools bent (Notion + Google Forms + Discord). No purpose-built vertical solution. |

**Total: 22/25 → Pursue.** Track B. Hand to `office-hours`.
