# Sources Playbook

Source-by-source how-to-mine reference. Use alongside `SKILL.md` Step 2 ("Cast a search net").

For each source: **what it's best for**, **how to search**, **what to capture**, **gotchas**.

**Bootstrap weighting:** sources marked **⭐ bootstrap-strong** are disproportionately valuable for Track A (B2B micro-SaaS) or Track B (prosumer one-person tools). See `SKILL.md` "Pick your track first" for which apply to which.

---

## Bootstrap-specific intel sources

Before diving into pain-mining, get a baseline for *what already sells at bootstrap scale*. These are "proof of WTP at small scale" sources, not pain sources — use them for counter-validation and pattern recognition.

### MicroAcquire / Acquire.com listings

**What it gives you:** publicly listed bootstrap SaaS for sale, with MRR, ARR, customer count, ARPU, churn, and asking price. A live catalog of "businesses at this shape and size actually exist and are valuable."

**How to use:**

- Browse listings in your target audience or category
- Read the seller's "Why are you selling" + customer pain narrative
- Filter by MRR band: $5k–$50k MRR listings = bootstrap-shaped
- Note the ARPU and customer-count combinations that recur — they tell you what the market closes at

**Why it matters:** validates that a wedge shape is monetizable before you build. If 5 listings in your niche are profitable at $10k–$30k MRR, that's proof the math closes.

### Indie Hackers product pages and milestone posts

**What it gives you:** founders publicly posting MRR milestones, often with the story of what pain their customers had and how they found them.

**How to use:**

- Search `indiehackers.com/products` for your niche
- Read the "milestone" / "revenue" / "interview" posts
- Look for the founder's description of customer pain — often more candid than marketing site copy

### TinySeed portfolio + Calm Company Fund portfolio

**What it gives you:** vetted lists of bootstrap-shaped businesses that took (small) investment. The portfolio companies' problem statements are a curated "what bootstrap-fundable looks like" reference.

### Failory ("startup post-mortems")

**What it gives you:** documented failures — including bootstrap failures. Read the "why we failed" sections to identify which audiences refused to pay, which markets were too small, which workflows users wouldn't change. A negative-space map of bad-fit opportunities.

### BuiltWith / Wappalyzer

**What it gives you:** reverse-lookup of what tools a site uses. Useful for "find people running [incumbent] and mine their complaints elsewhere."

**Example flow:** identify 50 sites running [incumbent] via BuiltWith → search "[company name] [incumbent name] frustrating / wish / instead" on Twitter, LinkedIn, Reddit → harvest verbatims from people who use it daily.

---

## Reddit ⭐ bootstrap-strong (both tracks)

**Best for:** Almost every audience. Long-form, candid, often timestamped and persona-tagged through subreddit context.

**How to search:**

```
site:reddit.com/r/[subreddit] "I wish there was"
site:reddit.com/r/[subreddit] "is there a tool"
site:reddit.com/r/[subreddit] "alternative to [competitor]"
site:reddit.com "[competitor] sucks"
```

Inside Reddit: sort by **Top → Year / All Time** for the subreddit. The most-upvoted posts of all time are usually a pain/wishlist post or a "why does X work this way" post — both gold.

**Tools:**

- **gummysearch.com** — paid, purpose-built. Surfaces high-pain posts across subs, filters by "questions / pain / shopping / advice."
- **F5Bot** — free keyword alerts (emails you new posts matching a keyword).
- **reddit-advanced-search** via old.reddit.com — supports `self:yes`, date ranges, and sort.

**What to capture:**

- Quote (exact, including profanity — emotional intensity is signal)
- Subreddit (= persona proxy)
- Post date (frequency / recency)
- Upvote count (loose proxy for resonance)
- Top comments (often contain workarounds and "I'm using X to do this" — pre-qualified buyers)

**Gotchas:**

- Subreddit demographics skew young, technical, English-speaking, US/UK. Triangulate.
- A single viral rant ≠ pattern. Apply the rule of three across different threads and timeframes.
- Some subreddits are highly moderated (r/marketing) and complaints get removed. Try unmoderated adjacent subs.

---

## App Store (iOS), Play Store (Android), Chrome Web Store ⭐ bootstrap-strong (Track B)

**Best for:** Consumer apps, prosumer apps, mobile-first SaaS, browser extensions. The single most overlooked goldmine for Track B (prosumer one-person tools).

**Chrome Web Store specifically:** the lowest-friction surface to ship a paid prosumer tool on. Extension reviews are public, sortable, and frequently include the user's exact workflow. Mine the top-3 incumbents in any category for 1★/2★ reviews.

**How to search:**

- Open the app's listing → reviews → **sort by "Most Critical"** (iOS) or filter by 1–2 stars (Play Store).
- Read the last 6–12 months of 1★ and 2★ reviews. Skip 5★ entirely.
- Mine **review responses** from the company — patterns the company keeps apologizing for = unfixed structural issues.

**Tools:**

- **AppFollow** / **Sensor Tower** / **data.ai** — paid, but powerful. Export all reviews to CSV, filter by keyword.
- For free: copy-paste reviews into a doc, then ask an LLM to cluster them.

**What to capture:**

- Quote
- Star rating (1 vs 2 matters — 1★ is rage, 2★ is "almost works")
- App version (regression vs persistent issue)
- Device / OS if mentioned
- Whether the company responded

**Gotchas:**

- Many low-star reviews are about app crashes / login bugs. Those are engineering issues, not opportunities. Filter them out before clustering.
- App store reviews skew toward people who care enough to be angry. Frequent buyers/users rarely review.
- Vertical app store leaders (top 3 in a category) collect 90% of reviews. Tail apps may have the better unmet-need signal but less volume.

---

## Trustpilot

**Best for:** DTC ecommerce, subscription services, fintech, insurance, telecoms, travel, some SaaS.

**How to search:**

- Direct: `trustpilot.com/review/[domain]` → filter by 1★ or 2★.
- Google: `site:trustpilot.com "[competitor]" "1 star"`.

**What to capture:**

- Quote
- Reviewer location (often shown — surprisingly useful for geo-specific opportunities)
- Whether company responded
- "Verified" badge (filters out fake reviews)

**Gotchas:**

- Companies actively solicit positive reviews and dispute negative ones. Take overall star averages with salt.
- Heavy survivorship bias toward angry one-time customers vs. happy repeat customers.
- Trustpilot itself runs a paid removal program. Some pain is filtered out.

---

## G2 and Capterra ⭐ bootstrap-strong (Track A)

**Best for:** B2B SaaS. The richest source for Track A (B2B micro-SaaS) opportunity mining — reviewers are role-tagged (CMO, Ops Manager), company-size-tagged, and required to fill out structured "Pros / Cons / What problem are you solving."

**How to search:**

- Direct: `g2.com/products/[competitor]/reviews` → sort by lowest rating.
- Read the **"Cons"** and **"What problems are you solving and how is that benefiting you?"** fields — both are mandatory and unusually candid.
- Cross-reference: G2's "compare" pages between two competitors are where switching pain shows up explicitly.

**What to capture:**

- Quote (split into "current pain" vs "what made me consider switching")
- Role / department of reviewer (persona)
- Company size band (SMB / Mid-Market / Enterprise — pricing implications)
- Industry (often = vertical SaaS wedge)

**Gotchas:**

- G2 incentivizes reviews with gift cards. Some reviews are perfunctory. Filter for review length >100 words.
- Vendors actively manage their G2 presence — recent negative reviews may get countered with bulk positive reviews. Look at reviews 6–18 months old for cleaner signal.

---

## Hacker News

**Best for:** Developer tools, infrastructure, AI/ML, devex, B2D SaaS, indie / bootstrap audience.

**How to search:**

- **HN Algolia** (`hn.algolia.com`) is the only good search. Use it.
- Specific patterns:
  - `"Ask HN" "tool for"`
  - `"Ask HN" "alternatives to"`
  - `"why doesn't anyone"`
  - `"Show HN" → read critical comments, not the post`
- Look at **comments on Show HN posts of failed/abandoned products** — comments often explain why the founder's wedge was wrong (= someone else's opportunity).

**What to capture:**

- Quote
- Commenter karma (rough credibility proxy)
- Post date (recency matters — dev tooling shifts fast)
- Linked GitHub repos / personal sites (commenters often signal their own context)

**Gotchas:**

- HN audience skews senior, opinionated, contrarian. Pain reported here may not generalize to broader developer market.
- HN hates marketing. "I would pay for this" comments are rare but golden — when they appear, they're meant.
- Heavy AI/LLM bias in 2025–2026. Filter signal from hype.

---

## Indie Hackers ⭐ bootstrap-strong (both tracks)

**Best for:** Solo founder / bootstrapper audience, niche SaaS, side projects, audience-building tools. Also the best single source for **counter-validating** that a wedge shape monetizes at bootstrap scale.

**How to search:**

- `indiehackers.com` search box, plus `site:indiehackers.com "I wish"` via Google.
- Read the **"Looking for a co-founder"** posts — the problem statements often describe an unmet need they want help building for.
- Read **revenue milestone posts** — successful niche SaaS founders often describe the pain their customers had.

**Gotchas:**

- Audience is small and self-selecting. Pain reported here is for "people who want to start a SaaS" — narrow segment, but high WTP.

---

## Twitter / X

**Best for:** Real-time complaints, high-status user pain (founders, designers, executives), micro-niche communities.

**How to search:**

- X advanced search: `(keyword) (lang:en) (min_faves:50) -filter:replies`
- Patterns: `"I wish X had"`, `"why doesn't [product]"`, `"I hate [tool]"`, `"alternative to [competitor]"`
- Watch reply threads on big creators' "what tool do you use for X" tweets — full of pain + workarounds.

**Gotchas:**

- Very noisy. Engagement-bait skews signal.
- Algorithm changes have collapsed reach for unknown accounts — pain from non-blue-check users is undersampled.
- High-status complaints don't always translate to a market (1 founder ≠ 10,000 customers).

---

## YouTube comments

**Best for:** Prosumer hardware (cameras, audio, 3D printing), software tutorials, online courses, tools-of-the-trade for any visual profession.

**How to search:**

- Find the top review or tutorial video for `[category] [year]` (e.g. "best CRM for solopreneurs 2026").
- Read comments sorted by Top.
- Specific pattern: comments that say *"I tried this but..."* or *"The reviewer didn't mention..."* — these are unmet-need flares.

**Gotchas:**

- Manual — no good search tool. Plan to spend 30–60 min per video for serious mining.
- Comments skew toward people with strong opinions (positive or negative).
- Spam-heavy. Filter aggressively.

---

## Discord and Slack communities

**Best for:** Domain-expert audiences (data scientists, game devs, niche professionals), modern indie/community-led SaaS, AI/LLM tooling.

**How to search:**

- Most communities require joining and lurking. Pick 2–3, lurk for 2+ weeks.
- Search within the community for pain phrases once you have access.
- The **#help** and **#general** channels are highest pain density.

**Gotchas:**

- Access-gated. Some communities ban "mining" or self-promotion.
- Discord conversations are ephemeral and hard to cite — capture quotes immediately.
- Slack communities (e.g. Rands Leadership, indie SaaS Slacks) require invitation or vouching.

---

## Quora

**Best for:** Beginner-to-intermediate user pain. "How do I" questions reveal underserved skill ramps and missing tooling.

**How to search:**

- `site:quora.com "best tool for"` / `"how do I"` + your domain keyword.
- Read the questions, not just answers — unanswered questions are gold (= unmet need with no current solution).

**Gotchas:**

- Quora's content quality has degraded. Many answers are SEO spam. Filter for answers by verified users with relevant credentials.

---

## Glassdoor "Cons" section ⭐ bootstrap-strong (Track A — underused)

**Best for:** Internal-tools-as-a-service opportunities (= ConvertKit-style starts), ops-tooling pain, B2B niches where employees complain about their employer's tech. Severely underused by indie hackers, partly because the search UX is bad. Worth the effort.

**How to search:**

- `glassdoor.com/Reviews/[Company]-Reviews-E[ID].htm` → filter to negative reviews → read "Cons."
- Patterns: "the [tool] we use is", "we still track [X] in spreadsheets", "the [department] software is from [year]."

**Gotchas:**

- Underused but powerful. Many enterprise pain points surface here that never make G2.
- HR-policy complaints dominate. Filter for tooling/process pain.

---

## Gartner Peer Insights

**Best for:** Enterprise software (security, ITSM, observability, data infra). Hard to access without a corporate account but reviews are unusually detailed.

**Gotchas:**

- Often paywalled / gated.
- Vendor-influence is heavy — read the "Cons" section critically.

---

## Niche forums (still alive in 2026) ⭐ bootstrap-strong (both tracks)

Don't dismiss old-school forums — they're often where the most engaged power users still live, with disposable income, sticky audiences, and near-zero competition for the wedge you'd build. Some of the best bootstrap businesses target forum-grade audiences exactly. Examples:

- **Photography**: dpreview forums (status uncertain), Fred Miranda, fstoppers comments
- **Audio production**: Gearspace, Sound on Sound forums
- **3D printing**: Reddit r/3Dprinting + manufacturer-specific forums (Prusa, Bambu)
- **Tabletop gaming**: BoardGameGeek forums
- **Trades**: Contractor Talk, Plumber forums, ServiceTitan community
- **Real estate**: BiggerPockets forums
- **Finance pros**: WallStreetOasis (junior bankers), Bogleheads (retail investors)

These forums have low SEO visibility but high pain density and often near-zero competition for the wedge you'd build.
