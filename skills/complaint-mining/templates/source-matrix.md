# Source Matrix

Every public complaint source, what it's good for, how to access it, and what it costs.

## Quick decision table

| You want to find | Best source(s) |
|---|---|
| Mobile consumer app complaints | App Store RSS, Play Store scrape |
| B2B SaaS complaints | G2, Capterra, Trustpilot, LinkedIn |
| Loud public rants in users' words | Reddit, Twitter/X |
| Verbal/visual demos of frustration | YouTube, TikTok |
| New apps shipping bad UX | Product Hunt comments |
| Ranked-by-anger summaries | Hacker News, Indie Hackers |

---

## Apple App Store

**Why it's gold:** Public RSS feed, no auth needed, fresh reviews daily, includes star rating + verbatim text + reviewer display name.

**Coverage:** All apps on the App Store, all locales, last 500 reviews per app per locale.

**Free access:**
- Public RSS feed: `https://itunes.apple.com/us/rss/customerreviews/id={APP_ID}/sortBy=mostRecent/page=1/json`
- Up to 10 pages × 50 reviews = 500 most recent reviews
- Locale code (`us`, `gb`, `de`, etc.) gives you regional reviews — useful for finding underserved geographies
- Script: see `scripts/appstore_reviews.py`

**Finding the app ID:**
- Go to the app's iTunes page
- URL contains `/id123456789/` — that's the ID
- Or use iTunes Search API: `https://itunes.apple.com/search?term={APP_NAME}&entity=software`

**Limitations:**
- 500-review cap per locale per fetch — pull multiple locales for broader sample
- No comments / replies, just the review
- Display names are pseudonyms; reviewer is harder to DM than Reddit user

**Best for:** Mobile consumer apps in Health, Fitness, Productivity, Sleep, Period, Meditation, Photo, Habit, Finance, Mental Health.

---

## Google Play Store

**Why it's gold:** Larger user base than App Store globally, especially in IN, BR, MX, ID, ES. More verbose reviews.

**Coverage:** All Android apps. No hard cap on review count (versus App Store's 500).

**Free access:**
- `google-play-scraper` Python library — widely used, well-maintained
- `npm` version: `google-play-scraper` for Node
- Script: see `scripts/playstore_reviews.py`

**Finding the app ID:**
- Play Store URL: `https://play.google.com/store/apps/details?id=com.example.app`
- The `id` param is the package name

**Limitations:**
- Google's ToS technically restricts automated scraping; `google-play-scraper` works but respect rate limits (1-2 req/sec, not 100)
- Reviews are paginated; pulling 5K+ takes a while
- No public reviewer profiles — harder to DM (usernames only)

**Best for:** Same categories as App Store, plus underserved regions where Android dominates.

---

## Reddit

**Why it's gold:** Long-form complaints with context, public usernames, easy to DM, niche subreddits = high concentration.

**Coverage:** All public subreddits. Old posts via search are partial; recent (last year) is good.

**Free access:**
- **Manual search** — `site:reddit.com [app name] sucks`, `site:reddit.com "I hate [tool]"`, sort posts by top → all time
- **`praw` Python library** — official Reddit API wrapper
- Free tier: 60 requests/min, more than enough for indie research
- Script: see `scripts/reddit_complaints.py`

**API setup:**
1. Create a Reddit account if you don't have one
2. Go to `https://www.reddit.com/prefs/apps` → "create app"
3. Pick "script" type → get client_id and client_secret
4. Use them in praw

**Search patterns that work:**
- `[app name] sucks` / `[app name] alternatives`
- `why does [app] [bad thing]`
- `hate [app] because`
- `switched from [app] to`
- `gave up on [app]`
- Top posts in `r/[app]_users` or `r/[app]criticism` if exist

**Best for:** Software complaints (everything from VSCode plugins to dating apps), niche communities (any sub with 10K+ members and weekly traffic), pain-point validation.

**Bonus tools:**
- **F5Bot** (free) — emails you whenever a keyword is mentioned anywhere on Reddit. Set keywords for "competitor name" + "alternative" + "I hate" — passive monitoring.

---

## G2 / Capterra / GetApp / Software Advice

**Why it's gold:** Verified B2B reviews — reviewer's name, title, company size, industry are usually public. Warm prospects.

**Coverage:** Most B2B SaaS. Smaller categories may have <50 reviews per product.

**Free access:** Manual browse only. Both have anti-scraping measures and ToS forbid automation.

**Workflow:**
1. Find the category page (e.g., G2's "CRM Software" page)
2. Sort by lowest rating
3. Read 1-2 star reviews of top 5 products
4. Open each reviewer's LinkedIn (their G2 profile usually links)
5. Save the review text + reviewer's LinkedIn URL

**Tools:**
- G2 Crowd Reviews — read manually
- Capterra — read manually; cross-references many of the same reviews
- GetApp / Software Advice — Gartner-owned, similar coverage
- TrustRadius — fewer reviews but more detailed

**Best for:** B2B SaaS competitive research — exactly what enterprise buyers complain about, with names attached.

**Pro tip:** Look at the **3-star reviews** as much as 1-star. 1-star is often a billing dispute or one bad rep. 3-star is "this product almost works for me but" — that's the wedge.

---

## Trustpilot

**Why it's gold:** Cross-category (B2C and B2B), strong reviewer accountability (verified purchase), public reviewer profiles.

**Coverage:** Strong in EU and UK; growing in US. Best for ecommerce, fintech, telecom, travel, services.

**Free access:** Manual browse. ToS forbids scraping; respect it.

**Workflow:**
- Search for the brand
- Filter by 1-2 stars
- Sort by recent
- Read 50 reviews → cluster
- Click reviewer profiles for cross-product context (often reviewers complain about multiple competitors — gold for ICP)

**Best for:** Fintech apps, banking, telecom, travel booking, delivery, retail brands.

---

## Twitter / X

**Why it's gold:** Real-time, public, reactive ("when X happens, I rage-tweet"). Great for catching new bugs and brand drama.

**Coverage:** Whatever's currently trending. Historical search is limited without API access.

**Access:**

| Tier | What you get | Cost |
|---|---|---|
| **Free / browser** | Advanced search via twitter.com/search-advanced | $0 |
| **Basic API** | 10K tweets/month read, 1 user | $100/mo |
| **Pro API** | 1M tweets/month, full archive | $5K/mo |
| **Enterprise** | Custom | $$$ |

For indie work, **stick to advanced search.** It's slower but free. Build a saved-search bookmark per category.

**Search patterns:**
- `"[app name] is so" -filter:replies` (rant catcher)
- `"why does [app]" -filter:replies`
- `"i hate [app]"`
- `"switching from [app]"`
- `"[app] alternative"`
- `near:[city] within:25mi "[app]"` (geo filter)
- Date range: `since:2024-01-01 until:2024-12-31`

**Best for:** Real-time pulse, finding influential complainers (who already have audiences), B2C consumer apps.

**Bonus tools:**
- **Mention** ($$) — keyword monitoring across Twitter + web
- **Brandwatch** ($$$) — enterprise sentiment

---

## YouTube

**Why it's gold:** Comments under "[app] review" or "[app] tutorial" videos are heavily filtered for actual users. Often deeply specific frustrations because the video walks the user through the exact feature that's broken.

**Coverage:** Any tool/app with tutorial videos (most have hundreds).

**Free access:**
- **Manual** — search "[app] review", filter for last year, scroll comments
- **`youtube-comment-downloader`** Python library — pulls all comments, no auth needed
- **Official YouTube Data API v3** — 10K units/day free quota

**Search patterns:**
- "[app] review", "[app] honest review", "[app] vs", "[app] pros and cons", "[app] tutorial"
- Filter: This year / This month
- Sort comments by Top to find consensus complaints

**Best for:** Tools with active how-to content — Notion, Airtable, Webflow, Salesforce, Excel, Photoshop. Less useful for simple consumer apps.

---

## TikTok / Instagram Reels

**Why it's gold:** Gen Z + millennials voice frustrations more often in video than text. New apps get rage-reviewed in hot/quick form.

**Coverage:** Mostly consumer apps, dating, fashion, finance, beauty, food delivery.

**Access:** Mostly manual. Scraping is gray — TikTok's ToS forbids it, and tools that try get rate-limited.

**Search patterns:**
- `#[appname]review`
- `#[appname]sucks`
- `#[appname]rant`
- "POV: you opened [app]" (sketch format)

**Tools:**
- **Tokboard, Pentos** ($$) — TikTok analytics
- **Trend.io** ($$) — surface viral complaint formats

**Best for:** Consumer trends, dating apps, fashion apps, finance apps. Skip for B2B SaaS.

---

## Product Hunt

**Why it's gold:** Comments under launches surface "this is just X but" critiques and feature requests in real time.

**Coverage:** New launches mostly. Comment threads die after launch day, so you have to monitor the daily front page.

**Free access:** Manual. The Product Hunt API exists but is rate-limited.

**Workflow:**
- Subscribe to daily digest
- Read comment threads for any product in your category
- Save complaints and feature requests
- DM the comment author — they're already in the launch mood

**Best for:** Brand-new categories where complaints can't be on G2 yet.

---

## Hacker News

**Why it's gold:** Long, technical, often signed-by-real-people complaints about developer-facing tools. Comments are durable (don't decay) and indexed.

**Coverage:** Developer tools, infra, productivity, AI. Less useful for consumer apps.

**Free access:**
- Algolia search: `https://hn.algolia.com/?q=[query]` — by points, recent, etc.
- Threads with 100+ comments are gold

**Search patterns:**
- `Show HN: [category]` — the launches with critique threads
- `[tool] alternative`
- `Why I left [tool]`
- `[tool] review`

**Best for:** Developer tools, AI tools, infra/devops, productivity SaaS aimed at engineers.

---

## Indie Hackers

**Why it's gold:** Founders posting their journeys complain about competitors' tools openly. Forum is small but high-signal.

**Coverage:** Founder-tools and indie SaaS.

**Access:** Free, manual. https://www.indiehackers.com — search bar.

**Best for:** Building tools for indie founders themselves.

---

## App store specialty tools

For when free + scripts isn't enough:

| Tool | Best for | Cost |
|---|---|---|
| **AppFollow** | Real-time review monitoring + AI sentiment, multi-app dashboards | Free tier; paid from $59/mo |
| **AppBot** | Review aggregation, sentiment, themes | Free tier; paid from $39/mo |
| **Asodesk** | ASO + reviews + competitor tracking | Free tier; paid from $35/mo |
| **ASOMobile** | ASO-focused, reviews secondary | Free tier; paid from $20/mo |
| **Appfigures** | Cross-store analytics + reviews | Free tier; paid from $10/mo |
| **Sensor Tower** | Enterprise market intelligence | $$$ ($1K-10K/mo) |
| **data.ai (App Annie)** | Enterprise market intelligence | $$$ |
| **AppMagic** | Mid-market intel | $$ ($300-1K/mo) |
| **AppTweak** | ASO + intel | $$ ($69-799/mo) |
| **Mobile Action** | Lower-cost intel | $$ ($69+/mo) |
| **The Tool** | Russian-built, ASO + reviews | $$ |

**Indie-hacker recommendation:** Start with the free tier of **Appfigures** or **AppBot**. Upgrade to **AppFollow** ($59/mo) only when you're mining new categories weekly.

---

## VOC clustering / synthesis tools

For taking 1,000+ reviews and turning them into themes faster than manual:

| Tool | Best for | Cost |
|---|---|---|
| **Idiomatic** | Enterprise VOC clustering | $$$ |
| **Productboard insights** | If you already use Productboard | $$ |
| **Anecdote** | Mobile review themes | $$ |
| **Claude API + custom prompt** | Indie / DIY clustering | $0.50-5 per cluster pass |
| **OpenAI embeddings + clustering** | Custom code, very cheap | < $1 per 1K reviews |

**Indie-hacker recommendation:** Use Claude with the prompt in `templates/prompts.md`. With prompt caching, mining a category costs <$2 in API spend.

---

## Putting it together

For a **mobile consumer app target**:
1. App Store RSS (free, scripted) — 500 latest 1-2 star reviews × 3 locales
2. Play Store scrape (free, scripted) — 1K 1-2 star reviews
3. Reddit search (free, scripted) — top complaints in 2 relevant subs
4. Twitter advanced search (free, manual) — 50 recent rants
5. Cluster via Claude (paid, ~$2)

Total cost: <$5 + 4 hours.

For a **B2B SaaS target**:
1. G2 manual browse — 50 1-2 and 3-star reviews of top 3 competitors
2. Capterra cross-check — same workflow
3. Trustpilot — if relevant brand-level
4. LinkedIn — message reviewers
5. Reddit / Hacker News for technical buyer complaints
6. Cluster manually or via Claude

Total cost: <$5 + 6 hours (more reading, less scraping).
