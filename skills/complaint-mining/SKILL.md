---
name: complaint-mining
description: "Find indie/bootstrapped app and SaaS ideas by systematically mining public complaints — App Store and Play Store 1-2 star reviews, Reddit rants, G2 / Capterra / Trustpilot reviews, Twitter/X / YouTube / TikTok comments. Workflow: pick a category, pull complaints (manual + scripts + paid tools), cluster with LLMs, score the clusters, hypothesize a wedge app, then DM the complainers themselves as the first 100 customers. Includes Python scripts (App Store RSS, google-play-scraper, praw), tool matrix (AppFollow, AppBot, Sensor Tower, Asodesk, etc.), and Claude prompts for clustering at scale. Use when the user wants to build a small, profitable app/SaaS and is hunting for ideas — keywords: 'mine app reviews', 'app store complaints', 'find SaaS ideas from reviews', 'better version of [app]', 'indie hacker idea', 'bootstrap idea', 'voice of customer', 'cluster reviews'. For broader generation lenses (PG self-problem, schlep blindness, niches), see product-ideation. For validation after a wedge is picked, see product-ideation's validation-playbook."
---

# Skill: Complaint Mining

## Purpose

Turn public complaints into shippable indie/bootstrap app ideas. The premise:

1. **Public complaint = pre-qualified prospect.** Anyone who writes a 1-star review or rants in a subreddit has self-identified as a buyer for a better version.
2. **Cluster of complaints = product wedge.** The same complaint repeated by 50 strangers across 3 platforms is a market signal.
3. **Complainers = your first 100 customers.** They're already on record and reachable — most apps never see this distribution gift.

This skill is for **indie hackers and bootstrappers** building $5K-$50K MRR apps, not VC-scale plays. Small TAMs (1K-10K total buyers) are fine — even good — because the competition is thin and the buyers are loud.

For broader idea generation (your own problems, schlep blindness, vertical SaaS), use `product-ideation`. For validation after you've picked a wedge, use `product-ideation`'s validation-playbook. This skill specifically owns the **complaint → app concept** pipeline.

## When to Use This Skill

- "I want to build an app — find me a niche where users hate the existing options"
- "Mine the App Store reviews for [category]"
- "What are people complaining about in [subreddit]?"
- "Cluster these reviews into themes"
- "Build me a list of underserved app categories"
- "Pick a competitor app — what would I build to take its angry users?"
- "How do I scrape Play Store reviews?"
- "Help me message the people who left 1-star reviews on [app]"

If the user is asking *what to build*, walk the full workflow. If they're asking a narrow question (e.g., "show me a script"), answer it but offer the next step.

## The Indie-Hacker Premise

Adjust your defaults to fit a solo or 2-person bootstrapped builder:

| Dimension | Default for indie/bootstrap | Why |
|---|---|---|
| Target MRR | $5K-$50K is great; $1M+ is out of scope | Solo founder lives well at $30K MRR |
| TAM | 1K-10K paying customers is enough | At $20/mo × 5K = $100K MRR |
| Build time | 30-90 days to first paying user | Anything longer = pivot risk too high |
| Pricing | $5-30/mo SaaS or $5-30 one-time mobile | Mass-market consumer pricing |
| Distribution | The complainers themselves + their community | No paid acquisition until PMF |
| Moat | Niche focus + speed + caring | Big players won't bother with 5K-customer markets |

The mental model is **Pieter Levels** (NomadList, PhotoAI), **Jon Yongfook** (Bannerbear), **Damon Chen** (Testimonial.to), **Marc Lou** (multiple micro-apps), **Tyler Tringas** (Storemapper, Calm Fund). Fast shipping, public building, charge from day one, niche audiences.

## The 6-Stage Workflow

```
1. Pick a target  →  2. Pull complaints  →  3. Cluster
                                                 ↓
6. Outreach  ←  5. Hypothesize wedge  ←  4. Score clusters
```

### Stage 1 — Pick a target (15 min)

Two ways to enter:

**A. Category-first** ("mine the meditation app space")
- List the top 10 apps in the category (App Store + Play Store + G2)
- Find the trade subreddit(s) and Discord(s)
- Identify the dominant complaint hashtags / search terms

**B. Competitor-first** ("find a wedge against Notion")
- Pull 1-2 star reviews, recent
- Find the competitor's subreddit, Discord, or feature-request board
- Search Twitter/X for "Notion is so [adjective]" patterns

If the user is blank on category, prompt with the indie-hacker fertile zones:

- **Mobile apps with high installs but mediocre ratings** (3.5-4.0 stars, 100K+ reviews — there's volume but unhappy buyers)
- **B2B SaaS in unsexy verticals** (HVAC, dental, legal, accounting — low NPS on G2)
- **Productivity tools with passionate haters** (Notion, Asana, Slack, Zoom — adjacent wedges)
- **"AI X" tools released in 2023-2024** (often shipped fast, brittle, lots of new complaints)
- **Mobile games / utility apps with predatory monetization** (people rage about ads, paywalls)
- **Health, fitness, sleep, period-tracking apps** (huge volume, polarized reviews)
- **Local services apps** (delivery, dating, ride-share regional players)

### Stage 2 — Pull complaints (1-3 hours)

Use the source matrix in `templates/source-matrix.md`. Default playbook for a mobile app target:

1. **App Store reviews** — pull the latest 500 1-2 star reviews via the public RSS feed (`scripts/appstore_reviews.py`)
2. **Play Store reviews** — pull via `google-play-scraper` Python lib (`scripts/playstore_reviews.py`)
3. **Reddit** — search the app name + subreddit posts via `praw` (`scripts/reddit_complaints.py`)
4. **Twitter/X** — manual advanced search if no API budget; otherwise X API
5. **YouTube** — `youtube-comment-downloader` on top tutorial / review videos
6. **G2 / Capterra / Trustpilot** — manual browse of 1-2 star reviews if B2B

For B2B SaaS, swap App/Play Store for **G2 + Capterra + Trustpilot + LinkedIn search**.

Aim for **300-1,000 raw complaint snippets** before clustering. Less and the clustering is noisy; more and the LLM context blows up.

Save them to a single CSV/JSONL with: source, date, rating, text, user_handle (if public), permalink.

### Stage 3 — Cluster the complaints (30 min with LLM, 4 hours manual)

Use the clustering prompt in `templates/prompts.md`. Two passes:

**Pass A — Auto-cluster** (Claude, Sonnet/Opus): paste 200-500 review snippets, ask for 8-15 themes with verbatim quote samples and rough frequency.

**Pass B — Refine** (you): merge near-duplicate themes, split themes that mix two issues, throw away themes that are about you-the-developer (rude support, billing) rather than the product itself.

Output: a table of 5-12 distinct **complaint clusters**, each with:
- Cluster name (in users' words)
- 3-5 verbatim quotes
- Estimated frequency (% of reviews mentioning it)
- Severity tag (showstopper / annoyance / vitamin)

### Stage 4 — Score the clusters (30 min)

Run each cluster through the rubric in `templates/cluster-rubric.md`. Six dimensions, 1-5:

1. **Frequency** — what % of complaints mention this?
2. **Severity** — does this stop them from using the app, or just annoy?
3. **Fixability** — can a solo dev ship a fix in 90 days?
4. **Audience size** — how many people total feel this pain?
5. **WTP signal** — are people in the reviews asking for an alternative or saying they'd pay?
6. **Defensibility** — would the incumbent fix this if you launched?

Total /30. The top 1-3 clusters become your wedge candidates.

### Stage 5 — Hypothesize the wedge (1 hour)

For the top clusters, fill in the `templates/wedge-template.md`. Each wedge is a one-page concept:

- Cluster the wedge addresses
- The single most painful symptom
- The 3-feature MVP that fixes it
- The pricing + business model
- The named ICP (who specifically)
- The first 50 customer acquisition plan
- 90-day build/launch plan

The point is to make picking obvious. After this, you should have 1-3 concepts you can defend in front of a skeptical friend.

### Stage 6 — Outreach to complainers (ongoing)

This is the unfair advantage. The complainers are public — DM them. Templates in `templates/outreach-templates.md`:

- **Reddit DM** — "saw your rant about X, building Y, want to be #1 user?"
- **Twitter/X reply or DM** — same
- **App Store reviews** — most reviewers leave a public handle / display name; try Twitter / Google search to find them
- **G2 reviewers** — usually have LinkedIn profiles — InMail
- **YouTube commenters** — channel about pages often have email

Realistic conversion: 30-50% reply rate, 5-10% become paid users. With 200 contacted, you have your first 10-20 paying customers.

This is the entire customer acquisition strategy until $5K MRR. **No ads needed.**

## Tooling Choices

Three tiers (full matrix in `templates/source-matrix.md`):

**Tier 0 — Free / DIY** — public RSS feeds, free scraper libs, manual browsing, free Reddit API, F5Bot for keyword alerts. Sufficient for the first 5-10 mining sessions.

**Tier 1 — Paid review tools** — AppFollow, AppBot, Asodesk for app reviews; ASOMobile (free tier); Pulsetic for monitoring. Use when you're mining a new category every week and want sentiment dashboards.

**Tier 2 — Enterprise** — Sensor Tower, data.ai (App Annie), AppMagic, AppTweak, Brandwatch, Mention. $$$ — mostly overkill for indie founders; rent through a friend or use only when scoping a serious bet.

**LLM clustering** — Claude API (use prompt caching on the review batch — same prompt across many cluster passes). Sonnet is fine; Opus for messy categories. See `prompts.md`.

## Decision Rules

**Build the wedge if:**
- Top cluster scores 22+/30 on the rubric
- 3+ verbatim quotes literally name what they wish existed
- You can list 50 specific public users to DM by Friday
- The MVP fits a 30-90 day solo build
- Pricing > $5/mo (mobile) or $20/mo (SaaS) is plausible from interview/review evidence

**Pivot or kill if:**
- Top cluster is <18/30 — complaints are too diffuse or about issues a solo can't fix (geography, hardware, regulation)
- The fix requires the incumbent's data (you can't replicate it)
- Complaints are about pricing, not product — race to the bottom is a bad indie play
- The category is < 5K total possible buyers, OR > 10M (you can't outflank big players)

**Always do this before building:**
- 10 Mom Test interviews with named complainers (use `product-ideation`'s interview-script.md)
- A 1-day landing page with a "Get notified" CTA shared in the same subreddit
- A pre-sell ask to 5 warmest contacts from the interviews

## Legal / Ethical Notes

- **App Store reviews** — public via Apple's RSS feed, fine to use
- **Play Store reviews** — public, but Google's ToS technically restricts automated scraping. `google-play-scraper` is widely used; respect rate limits, don't republish at scale
- **Reddit** — official API is fine for read access; don't spam-DM (read each subreddit's rules)
- **G2 / Capterra / Trustpilot** — read manually; their ToS forbids automated scraping
- **Twitter/X** — official API is paid; manual advanced search for indie projects
- **YouTube** — comments scraping via official Data API is fine within quota
- **TikTok** — gray area; manual browsing only

When in doubt: **read manually, save quotes, attribute back to public usernames.** You're doing research, not bulk-data collection.

## Language Guidance

**Be a product-archaeologist, not a brainstorm partner.** The user's job is to dig the data; your job is to keep them from confirmation-biasing the dig.

- **Push for quantity early.** "Pull 500 reviews before clustering 5." Small samples produce phantom patterns.
- **Demand verbatim quotes.** "Don't tell me 'users are frustrated.' Quote three of them."
- **Catch confirmation bias.** "You picked the cluster that matches your favorite idea. Score the others first, then pick."
- **Push for the DM.** "Stop reading the reviews. DM 10 of them this afternoon. Their reply or non-reply is the data."
- **Set 7-day deadlines.** "By Friday you'll have a CSV of 500 complaints, 8 clusters, 3 wedges, and 10 outreach DMs sent."

**Bad example:**

"This category has lots of negative reviews. You should probably look at meditation apps next. Want me to outline some features?"

**Good example:**

"Pulled 412 1-star reviews of Calm + Headspace from the past 6 months. Three clusters worth attention: (a) 31% complain about 'losing streak' anxiety from missed days — quote: 'i deleted the app after it told me i broke my 89-day streak from one missed night'; (b) 22% want offline-first because their commute has no signal; (c) 17% specifically want non-religious sleep audio without the meditation-influencer voice. Of those, (b) is most fixable solo (90-day build) and most defensible (incumbents won't ship offline because their growth team needs daily logins). 50 named complainers from the (b) cluster are linkable to public Twitter handles — I'll draft DMs. Build wedge or pivot?"

## Handoffs

- **`product-ideation`** — for broader idea generation lenses (PG self-problem, schlep blindness, niches), the full scoring rubric, and the validation ladder (interviews → landing page → pre-sell)
- **`copywriting`** — for the landing page copy and outreach DM polishing
- **`product-management`** — once a wedge is picked and validated, for PRD/scope work

## Notes

The single biggest failure mode of this skill is **read-only research**. Founders mine for weeks, build elaborate spreadsheets of complaints, and never send a DM or build a landing page. Every session must end with one outbound action: a DM sent, a landing page deployed, an interview booked. Keep the user out of the spreadsheet trap.
