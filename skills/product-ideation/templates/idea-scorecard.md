# Idea Scorecard

Score the idea on each of 8 dimensions, 1 (terrible) to 5 (excellent). Total out of 40.

## Decision rule

| Total | Verdict |
|---|---|
| **<25** | Don't build it. Pivot inside the maze or pick a different idea. |
| **25-32** | Maybe. The idea has potential but at least one weak dimension is going to bite. Fix it before building. |
| **33-37** | Strong. Run the validation ladder this week. |
| **38-40** | Suspiciously high. Either the idea is exceptional, or you're scoring with rose-tinted glasses. Ask a skeptical friend to score it independently. |

---

## The 8 dimensions

### 1. Pain intensity (Painkiller vs vitamin)
*Source: Jason Cohen / common SaaS wisdom*

| Score | Signal |
|---|---|
| 5 | Users can name the exact moment the pain hits. They've already tried 2+ solutions. They complain publicly. |
| 4 | Users feel the pain weekly, have a manual workaround, would describe it as "annoying" or worse. |
| 3 | Pain is real but episodic. Users mostly tolerate it. |
| 2 | Users can imagine the value but don't actively suffer today. |
| 1 | Pure "nice to have." No current workaround because no one's bothered. |

**Quick test:** Ask 5 potential users *unprompted*: "What's the most annoying part of your day?" If your problem doesn't come up unprompted in 1 of 5 mouths, score 2 or below.

---

### 2. Frequency of use

| Score | Signal |
|---|---|
| 5 | Daily, often multiple times. The product becomes a habit. |
| 4 | Multiple times per week. |
| 3 | Weekly. |
| 2 | Monthly. |
| 1 | Quarterly or less (annual taxes, hiring, fundraising tools — these *can* be huge but require extra-strong other dimensions). |

**Why this matters:** Frequency drives habit, habit drives retention, retention drives LTV. A daily-use vitamin can outperform a yearly painkiller.

**Exception:** Low-frequency products with extreme stakes (legal contracts, IPO software, insurance) work despite low frequency because the *single use* is so high-value.

---

### 3. Existing alternatives (the "are people already paying?" test)

| Score | Signal |
|---|---|
| 5 | Yes, multiple alternatives exist, all are awful, users complain about all of them. |
| 4 | Yes, alternatives exist but are inadequate for a clear segment. |
| 3 | Adjacent tools exist but no one has solved the specific problem. |
| 2 | Workarounds exist (spreadsheets, manual labor) but no SaaS competitor. |
| 1 | No one is solving this and no one has a workaround. **This is usually a bad sign**, not a green field — it means demand is unproven. |

**Counterintuitive but true:** A score of 1 on this dimension is almost always disqualifying. If the demand existed, *something* (even bad) would be filling it.

---

### 4. Willingness to pay (WTP)

| Score | Signal |
|---|---|
| 5 | Users have already pre-paid you, paid a competitor, or named a price >2x your planned ask. |
| 4 | Users named a price ≥ your planned ask in interviews and provided a credit card on the landing page. |
| 3 | Users named a price ≥ your planned ask, but haven't put money down yet. |
| 2 | Users said "I'd pay something" but didn't name a number. |
| 1 | Users said "free or nothing." |

**Don't trust scores 3 and below.** People dramatically overestimate their own future spending. Score 4-5 require *behavioral evidence* (a card, a check, a wire), not statements.

**B2B benchmark:** A SaaS idea with no one willing to pay $50/mo (or $500/year) for the unbuilt version is rarely a viable startup. The exception is consumer or freemium where revenue comes from scale.

---

### 5. Founder-market fit

| Score | Signal |
|---|---|
| 5 | You *are* the customer, have built or sold in this category, or have 10+ years deep in the domain. You have an audience. |
| 4 | You've worked adjacent to this market, know it well, have warm intros to 50+ buyers. |
| 3 | You're a credible outsider with a clear hypothesis. You can become an insider in 30-60 days. |
| 2 | You don't know the market. You'd need 6+ months to develop credibility. |
| 1 | You don't know the market and can't easily access it (regulated industry, geographic distance, language). |

**Why this matters more than founders think:** An idea is a 5-7 year commitment. If you don't naturally enjoy the customer, the day-to-day work, and the world they live in, you'll quit in year 2.

**Permission slip for low scores:** Some great founders entered industries cold (Bezos and books, Musk and rockets). They moved fast on building credibility. If you score 1-2, your validation step *is* "embed in the market for 30 days," not "build software."

---

### 6. Distribution

| Score | Signal |
|---|---|
| 5 | You have a way to reach 1,000+ qualified prospects within 7 days for $0. (Existing audience, employer relationship, community insider, etc.) |
| 4 | You can reach 1,000+ for <$1,000 (warm intros, relevant content distribution, community access). |
| 3 | Standard channels exist (SEO, ads, cold outbound) and you understand the unit economics. |
| 2 | Channels exist but they're contested and expensive. You haven't run them before. |
| 1 | You have no plan for how the first 100 customers find you. |

**The blunt rule:** Distribution kills more startups than product. If you can't sketch a plausible path to the first 100 customers without ads, the answer is usually "spend the next 60 days building distribution before building product."

---

### 7. Tailwind

| Score | Signal |
|---|---|
| 5 | Major tech, regulatory, or demographic shift is making this newly possible *and* newly necessary. (Today: AI agents, GenAI APIs, on-device ML, real-time voice, robotics, climate disclosure regs, aging boomers.) |
| 4 | A clear secular tailwind is making this 5-10x easier or cheaper than 3 years ago. |
| 3 | Things are stable but the category is growing. |
| 2 | The category is mature, no obvious wind. |
| 1 | The category is shrinking or about to be disrupted by something else. |

**Don't fight the wind.** A mediocre idea on a strong tailwind beats a brilliant idea fighting the current.

---

### 8. Moat path

| Score | Signal |
|---|---|
| 5 | Clear, multi-layered defensibility in 3 years (data network effects, two-sided marketplace, brand, switching costs, regulatory moat). |
| 4 | One strong defensibility mechanism (proprietary data, integrations, brand). |
| 3 | Modest moat (better UX, niche focus, integration depth). |
| 2 | Easy to copy. Defense is just "execute faster." |
| 1 | Commodity. The first competitor with capital wins. |

**For idea-stage:** A 3 is usually enough. Lock-in builds with use; brand builds with time. The point is to *have a path*, not full defensibility on day one.

**Caveat for AI-wrapper era (2024-2025):** Many ideas score 1-2 on moat because "GPT-X plus a UI" is easy to copy. The path to a real moat usually runs through (a) proprietary data, (b) deep workflow integration, (c) trust and brand, or (d) network effects. State which.

---

## Output format

When scoring, present results as:

```
Idea: [one-sentence description]
JTBD: When [trigger], I want [job], so I can [outcome].

Pain intensity        4/5  — Users complain in [community], multiple workarounds.
Frequency             3/5  — Weekly use; not daily.
Existing alternatives 4/5  — 3 incumbents, all clunky, segment is loud.
Willingness to pay    2/5  — No one has paid yet; named prices in interviews only.
Founder-market fit    4/5  — Founder ran ops at [company] for 4 years.
Distribution          5/5  — Founder runs 12K-member Slack of exactly this audience.
Tailwind              4/5  — AI making real-time analysis newly cheap.
Moat path             3/5  — Brand + workflow integration; defensible if first to land 100 logos.

TOTAL: 29/40 — "Maybe, validate hard."

Weak link: WTP. Next step (this week): pre-sell $X for a 30-day pilot to 5 warm contacts in the Slack. If 2 buy, score moves to 4 and total to 31. If 0 buy, kill it.
```

Always end with **what would change the score** and a **specific next step** to test the weakest dimension.
