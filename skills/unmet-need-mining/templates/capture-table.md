# Capture Table

The structured format for collecting verbatims during Step 3 of `SKILL.md`. Copy this template into a doc, spreadsheet, or Notion page and fill one row per quote.

**Rule:** capture **exact quotes only**. Paraphrasing destroys the asset. The verbatim language is what becomes your headlines, ad copy, positioning, and search-keyword targeting.

**Tag each row with a track** (A: B2B micro-SaaS, B: Prosumer) in the cluster column once you start clustering. Mixed-track clusters score badly — they're usually two opportunities pretending to be one.

---

## Minimum columns

| # | Source URL | Verbatim quote | Persona signal | Frequency signal | WTP signal | Current workaround | Cluster (filled later) |
|---|---|---|---|---|---|---|---|

### Column definitions

- **# —** running number, for reference during clustering
- **Source URL —** direct link to the post / review / comment so you can re-validate later
- **Verbatim quote —** the user's *exact words*, including profanity, typos, and emotion. Trim only for length; never reword.
- **Persona signal —** what you can infer about the speaker: role, audience, context. Pull from username, subreddit, review badge, signature, profile, or comment context. ("Solo Shopify owner", "RevOps at mid-market SaaS", "freelance wedding photographer")
- **Frequency signal —** any temporal anchor in the quote: "every day", "every Monday", "month-end", "once per project". If none stated, write "unstated."
- **WTP signal —** what they're already spending on this problem: time, money, tools, freelancers, workarounds. ("Pays for Zapier + 2 hours/week manual reconcile", "uses free spreadsheet", "hired a VA for $400/mo")
- **Current workaround —** the explicit or implicit workflow they use today. The workaround is your competition.
- **Cluster —** leave blank until Step 4. You'll group rows here by Job-to-be-Done.

---

## Example rows (illustrative)

| # | Source URL | Verbatim quote | Persona signal | Frequency signal | WTP signal | Current workaround | Cluster |
|---|---|---|---|---|---|---|---|
| 1 | reddit.com/r/Shopify/comments/.../ | "I genuinely hate that I spend 4 hours every Monday morning reconciling my Meta and TikTok ad spend against actual product profit in a stupid spreadsheet. There has to be a better way. Triple Whale is too expensive for my size." | Solo Shopify owner, sub-$1M GMV | Weekly (4hr Mondays) | Aware of Triple Whale ($-priced out); spends time | Manual Google Sheet pulling Meta/TikTok/Shopify exports | Ad-spend-to-profit attribution for SMB Shopify |
| 2 | g2.com/products/triple-whale/reviews/... | "Love the data but pricing is brutal for stores under $1M. Cancelled and went back to spreadsheets." | DTC owner, sub-$1M | Daily check, monthly billing pain | Was paying ~$300/mo; churned to free | Spreadsheet | Ad-spend-to-profit attribution for SMB Shopify |
| 3 | apps.apple.com/us/app/[bookkeeping-app]/reviews → 1★ | "Doesn't connect to Shopify properly. Have to export CSV every week. What is this, 2010?" | Solo bookkeeper / DTC owner | Weekly CSV export | Pays for app already (~$15/mo) | CSV export + manual import | Ad-spend-to-profit attribution for SMB Shopify |

These three rows would cluster together (column 8) because they describe the same Job-to-be-Done: *"As a sub-$1M DTC store owner, I want to know real per-product profit including ad spend, so I can decide where to scale spend, without paying enterprise prices."* — **Track A** wedge: vertical SaaS at $30–$80/mo for an underserved SMB niche.

### Track B example (prosumer)

| # | Source URL | Verbatim quote | Persona signal | Frequency signal | WTP signal | Current workaround | Cluster |
|---|---|---|---|---|---|---|---|
| 4 | reddit.com/r/gamedev/comments/.../ | "Running a paid playtest this week and feedback is back to being a complete mess in Notion. Spent more time chasing testers than reading their notes. There has to be a better way for indies." | Solo / 2-person indie game studio | Per-build (weekly during active development) | Pays for itch.io membership + Notion ($10/mo) | Notion + Google Forms + Discord DMs | **B**: Per-build playtest feedback for indies |
| 5 | reddit.com/r/IndieGaming/comments/.../ | "UserTesting is way out of budget for an indie. I'd genuinely pay $20/mo for something that just gave me a per-build form with tester deduplication and a heatmap." | Indie game dev (sub-$50k revenue) | Per-build | Already paying for Notion; explicit $20/mo WTP | Manual + free tools | **B**: Per-build playtest feedback for indies |
| 6 | discord IndieGameDevs #feedback channel quote | "ugh another playtest cycle, time to copy 40 google forms responses into a notion table by hand again" | Solo dev, mid-prototype | Per-build | Time cost = 1-2 hours per build | Google Forms → manual Notion entry | **B**: Per-build playtest feedback for indies |

These three rows cluster as a **Track B** wedge: a $19/mo (or $99 one-time) per-build playtest feedback tool for itch.io indies. JTBD: *"When I ship a new playtest build, I want to collect, deduplicate, and visualize tester feedback without manually wrangling Google Forms and Notion."*

---

## Volume target

- **Minimum:** 30 verbatims before clustering
- **Sweet spot:** 50–80 verbatims
- **Diminishing returns:** beyond ~150 you're adding noise, not signal

Spread across **at least 3 sources** to avoid single-channel bias.

---

## Anti-patterns to avoid

| Anti-pattern | Fix |
|---|---|
| Summarizing the quote ("user complains about pricing") | Always paste the exact words |
| Capturing only the headline / title of a post | Read the body and top comments — the gold is usually there |
| Skipping the workaround column | The workaround IS your competition. Without it you can't differentiate. |
| Mixing personas in one row | One verbatim per row. Persona inference is per-quote. |
| Cluster-as-you-go | Cluster after capture is done. Pre-clustering biases what you notice. |

---

## Tooling

- **Spreadsheet** (Google Sheets, Excel) — best for filtering and sorting later
- **Notion / Coda** — good if you'll share with a co-founder
- **Plain markdown table** in a text file — fine for solo work
- **LLM-assisted clustering** — once you have 30+ rows, paste into an LLM and ask: "Group these verbatims into 3–8 clusters by the underlying Job-to-be-Done. For each cluster, list the row numbers and write a one-sentence JTBD statement in the form 'When [situation], I want to [motivation], so I can [outcome].'"

---

## Hand-off

When the table is full and clustered:

- **Per cluster:** the row numbers, the JTBD statement, and a rough count.
- **Top 3 clusters** by intuitive pain × frequency × WTP go into the scoring rubric (`evaluation-rubric.md`).
- **Top 1–3 from scoring** become wedge sentences (Step 6 in `SKILL.md`) and hand off to `office-hours`.
