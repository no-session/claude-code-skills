# Scraping Playbook

End-to-end pipeline: pull complaints → cluster → score → pick a wedge. All scripts live in `../scripts/`. Default tools are free; paid tools noted where they save time.

## Setup once

```bash
pip install google-play-scraper praw youtube-comment-downloader anthropic
```

For Reddit, also create app credentials:
1. https://www.reddit.com/prefs/apps → "create app" → script type
2. Copy client_id + client_secret
3. Set env vars:
```bash
export REDDIT_CLIENT_ID=...
export REDDIT_CLIENT_SECRET=...
export REDDIT_USER_AGENT="complaint-mining/1.0 by u/yourusername"
```

For Claude clustering:
```bash
export ANTHROPIC_API_KEY=...
```

## Pipeline 1 — Mobile consumer app target

Worked example: target = a meditation app you'd build a wedge against.

### Step 1: Pull App Store reviews

Find the app ID from the App Store URL (`apps.apple.com/us/app/.../id1234567890`).

```bash
# 500 most recent 1-2 star reviews, US locale
python scripts/appstore_reviews.py 1234567890 \
    --locale us --max-pages 10 --min-rating 1 --max-rating 2 \
    --out appstore_us_complaints.csv

# Same in another locale to broaden
python scripts/appstore_reviews.py 1234567890 \
    --locale gb --max-pages 10 --min-rating 1 --max-rating 2 \
    --out appstore_gb_complaints.csv
```

Combine multiple locales for richer signal — different markets surface different pain points.

### Step 2: Pull Play Store reviews

Find the package name from the Play Store URL (`play.google.com/store/apps/details?id=com.example.app`).

```bash
python scripts/playstore_reviews.py com.example.app \
    --lang en --country us --count 1000 --min-rating 1 --max-rating 2 \
    --out playstore_complaints.csv
```

### Step 3: Pull Reddit complaints

```bash
# Try a few keyword variants
python scripts/reddit_complaints.py "calm app sucks" \
    --subreddits meditation Anxiety productivity all \
    --limit 50 --filter-complaints \
    --out reddit_calm_complaints.csv

python scripts/reddit_complaints.py "switched from headspace" \
    --subreddits meditation \
    --limit 50 --include-comments --filter-complaints \
    --out reddit_headspace_switching.csv
```

### Step 4: Pull YouTube comments

Find 3-5 high-view "[app] review" or "[app] vs" videos. Run the scraper on each.

```bash
python scripts/youtube_comments.py "https://youtube.com/watch?v=ABC123" \
    --limit 500 --sort popular --out youtube_review_video1.csv
```

### Step 5: Combine into one corpus

```bash
# Quick way: concatenate the text columns into a JSONL
python -c "
import csv, json
sources = [
    ('appstore_us_complaints.csv', 'content', 'rating'),
    ('appstore_gb_complaints.csv', 'content', 'rating'),
    ('playstore_complaints.csv', 'content', 'rating'),
    ('reddit_calm_complaints.csv', 'text', 'score'),
    ('reddit_headspace_switching.csv', 'text', 'score'),
    ('youtube_review_video1.csv', 'text', 'votes'),
]
with open('all_complaints.jsonl', 'w') as out:
    for path, text_col, rating_col in sources:
        with open(path) as f:
            for row in csv.DictReader(f):
                out.write(json.dumps({
                    'source': path,
                    'text': row.get(text_col, ''),
                    'rating': row.get(rating_col, ''),
                }) + '\n')
"
```

### Step 6: Cluster with Claude

```bash
python scripts/cluster_with_claude.py all_complaints.jsonl \
    --jsonl --text-key text --max-rows 500 \
    --out clusters.json
```

Output is a JSON of 5-12 clusters with verbatim quotes and frequency. Open it, read it, then refine manually (merge near-dupes, split mixed clusters).

### Step 7: Score and pick

Use `cluster-rubric.md` to score each cluster on 6 dimensions. Pick the top 1-3 for wedge concepts using `wedge-template.md`.

### Step 8: Outreach

Build a list of named complainers (Reddit usernames, App Store handles cross-referenced to social, YouTube channels). Use `outreach-templates.md`. Send 10-30 DMs the same week.

---

## Pipeline 2 — B2B SaaS target

Worked example: target = build a wedge against a clunky CRM.

### Step 1: Manual G2 + Capterra harvest

Search G2 for the category ("CRM Software"). For each of the top 5 products:
1. Sort reviews by lowest rating
2. Read 30-50 1-3 star reviews
3. For each, copy: review text + reviewer name + reviewer LinkedIn + company size + role

Save to a CSV with columns: `source, product, rating, role, company_size, text, linkedin_url`.

Capterra often duplicates G2 reviews, but it indexes some not on G2. Do both.

### Step 2: Trustpilot if relevant

For consumer-adjacent B2B (Mailchimp, Squarespace, Shopify, Stripe), Trustpilot has heavy review volume and verified-purchase reviewers.

### Step 3: Reddit + Hacker News

```bash
python scripts/reddit_complaints.py "salesforce alternative" \
    --subreddits sales smallbusiness sales_engineering \
    --limit 100 --include-comments --filter-complaints \
    --out reddit_salesforce_alts.csv
```

For developer-facing B2B, also Algolia-search Hacker News:
- `https://hn.algolia.com/?q=salesforce+alternative`
- Read threads with 100+ comments

### Step 4: LinkedIn search

LinkedIn doesn't have a complaints API, but search posts for `"frustrated with [product]"` or `"switching from [product]"`. Manual but high-quality leads.

### Step 5: Cluster

Same as pipeline 1, with the combined CSV.

### Step 6: Outreach via LinkedIn InMail

For B2B, LinkedIn outreach to G2 reviewers is the highest-converting channel. The DM template is in `outreach-templates.md`.

---

## Pipeline 3 — "I have no target, find me a category"

When the user is blank, run a **complaint-volume scan** before picking a deep target.

### Step 1: Generate candidate categories

Pick 5-10 candidate categories based on indie-hacker fertility:
- Sleep apps, meditation apps, period trackers, habit trackers (high install + mediocre ratings)
- Note-taking, todo, calendar (passionate haters, lots of switching)
- B2B verticals: legal, dental, HVAC, accounting (G2 + Capterra signal)
- New AI tools released 2023-2024 (often brittle, lots of complaints)
- Mobile games with predatory monetization
- Local services apps (delivery, dating regional)

### Step 2: Sample 50 reviews per category

For each candidate, pull just 50 reviews of the top 3 apps. Don't deep-mine — you're scoring the category, not the wedge.

### Step 3: Score categories

For each category, score:
- **Volume** — how many complaints exist?
- **Specificity** — are complaints specific (gold) or vague (skip)?
- **Repeated themes** — do the same 2-3 issues come up across apps?
- **Ranter density** — what % of reviews are real rants vs. "doesn't sync sometimes"?
- **Audience accessibility** — can you find named complainers to DM?

The category that wins on 4+ dimensions is your deep-mine target.

### Step 4: Run pipeline 1 or 2 on that category

---

## Cost estimates

For one full mining session on a mobile app category:

| Step | Tool | Cost |
|---|---|---|
| App Store pulls | Free RSS | $0 |
| Play Store pulls | google-play-scraper | $0 |
| Reddit pulls | praw + free tier | $0 |
| YouTube pulls | youtube-comment-downloader | $0 |
| Clustering | Claude API (Sonnet, 500 reviews) | ~$1-3 |
| **Total** | | **~$1-3** |

For B2B SaaS, replace the App/Play Store pulls with manual G2 work (free, ~3 hrs of labor).

## Common pitfalls

- **Pulling too few reviews** — under 200 and clustering is noisy. Push for 500+.
- **Pulling only 1-star** — 2 and 3-star reviews often have the most useful "almost works for me" signal. Include them.
- **Clustering before reading** — always read 30-50 reviews manually first to anchor your sense of what's there. Don't outsource the gut.
- **Ignoring locale signal** — complaints in `gb` or `de` or `in` locales often show different problems than `us`. Geographic underservice is itself a wedge.
- **Skipping outreach** — 80% of users who do this skill stop at the spreadsheet. Send the DMs the same week or you've wasted the work.
- **Re-publishing scraped data** — don't. You're using it for personal research and outreach, not building a public dataset.
