# Wedge Template

A "wedge" is the smallest, sharpest version of an app/SaaS that addresses one (or two combined) high-scoring complaint clusters. Output of this template is a one-page concept you can defend in front of a skeptical friend or pitch to a complainer in a DM.

Fill in for each top cluster you're considering building.

---

## The one-pager

```
WEDGE NAME: [working title — 1-3 words]
ELEVATOR LINE: [Product] for [ICP] who [specific pain]. Unlike [incumbent], [unique angle].

THE COMPLAINT CLUSTER
- Cluster name: [in users' words]
- Score: [from cluster-rubric.md]
- Frequency: [%]
- 3 verbatim quotes:
  1. "..."
  2. "..."
  3. "..."

THE NAMED ICP
- Who specifically: [demographic, role, life stage]
- Where they hang out: [subreddit, Discord, conference, publication]
- Estimated paying-capable population: [number]
- 5 named real people (linked from your scrape):
  1. [username/handle/source]
  2. ...
  3. ...
  4. ...
  5. ...

THE 3-FEATURE MVP
- Feature 1: [the one that fixes the cluster, in plain English]
- Feature 2: [the supporting flow needed for #1 to work]
- Feature 3: [the bare-minimum onboarding/account/payment]
(Anything not in this list is post-launch.)

THE PRICING
- Model: [one-time / monthly / annual / freemium]
- Price points to test: [$X, $Y, $Z]
- Source of price evidence: [interview quotes, what they pay competitors, comparable apps]

WHY THE INCUMBENT WON'T COPY
[1-3 sentences on the structural reason the incumbent ignores this — usually: their metrics, their org structure, their TAM math]

THE FIRST 50 CUSTOMER PLAN
- Channel 1: [DM the complainers — count of named ones you have]
- Channel 2: [post in [subreddit/community] with your story]
- Channel 3: [reach out to [niche newsletter / podcast / influencer]]
- Days to first paying user: [target = 30]
- Days to 10 paying users: [target = 60]
- Days to 50 paying users: [target = 120]

THE 90-DAY BUILD/LAUNCH PLAN
- Week 1-2: Validate via 10 Mom Test interviews + landing page live
- Week 3-4: Concierge-MVP for 3 paid pilots (manual delivery)
- Week 5-10: Build the actual MVP (3 features)
- Week 11: Soft launch to interview list + landing page waitlist
- Week 12: Public launch (Product Hunt, IH, Twitter, the relevant subs)

THE KILL CRITERIA
This wedge dies if, by [date]:
- [ ] Fewer than 3 of 10 Mom Test interviews show real pain
- [ ] Landing page CTA click-through is <2% on qualified traffic
- [ ] Pre-sell asks return zero buyers from 5 warm contacts
- [ ] Concierge MVP retains 0 of 3 paid pilots after 30 days

If any of these hits, pivot inside the maze (different ICP, different angle, different bundle) before another month of building.
```

---

## Worked example: "Streakless"

```
WEDGE NAME: Streakless
ELEVATOR LINE: Meditation app for people who quit Calm/Headspace because of streak guilt. Unlike incumbents, Streakless gives you 1 free skip per week and rolls forward unused days.

THE COMPLAINT CLUSTER
- Cluster name: "i lose my streak from one missed day"
- Score: 26/30
- Frequency: 18%
- 3 verbatim quotes:
  1. "deleted the app after it told me i broke my 89-day streak from one missed night"
  2. "the streak anxiety stressed me out more than not meditating did. ironic."
  3. "i'd pay for a calm clone that just lets me skip a day without guilt-tripping me"

THE NAMED ICP
- Who specifically: 25-45 year-old professionals who've tried meditation apps, quit specifically over streaks
- Where they hang out: r/meditation (1.2M), r/Anxiety (700K), r/productivity, indie wellness Slacks, "calm app sucks" Reddit threads
- Estimated paying-capable population: ~500K (1% of global meditation app users with this specific complaint)
- 5 named real people:
  1. u/zenstuck (Reddit, 4 mentions of streak rage)
  2. @sarahmeditates (Twitter, 3-tweet thread on Calm streak anxiety)
  3. App Store reviewer "MindfulMike" (linkable to Twitter @mindfulmike)
  4. u/AnxietyAndOats (deleted Calm post, 200 upvotes)
  5. @therapybroke (TikTok, 50K-view rant about Headspace streak)

THE 3-FEATURE MVP
- Feature 1: Compassionate streak — automatic 1 free skip per week, rollover up to 4, no-guilt UI copy
- Feature 2: 50-meditation library covering sleep, anxiety, focus, body scan (curated, not a content firehose)
- Feature 3: Stripe-based $5/mo paywall after 7-day free, no card required for trial

THE PRICING
- Model: monthly subscription
- Price points to test: $4.99, $7.99, $9.99
- Source of price evidence: Calm = $14.99, Headspace = $12.99; users said "I'd pay something just not as much as Calm" — undercut by 50%+

WHY THE INCUMBENT WON'T COPY
Calm and Headspace tie growth metrics to "current streak length" and "consecutive days opened." Removing streak punishment would tank their daily-active-user retention metric in the short term. Their growth team won't ship it; this is a 5-year structural moat.

THE FIRST 50 CUSTOMER PLAN
- Channel 1: DM the 5 named complainers + 25 more from the same threads (~50% reply, ~10 paid)
- Channel 2: Post the soft-launch in r/meditation as "I built this because I quit Calm — would love feedback" (~20 paid)
- Channel 3: Reach out to 3 mindfulness newsletter writers (Wait But Why, Lenny Substack-adjacent, Dr. K therapy YT) for a mention (~20 paid)
- Days to first paying user: 30
- Days to 10 paying users: 45
- Days to 50 paying users: 90

THE 90-DAY PLAN
- Wk 1-2: Interview 10 named complainers; deploy landing page on Carrd; collect 100 emails
- Wk 3-4: Run 3 paid concierge pilots (record 3 custom guided meditations per pilot for $20 each)
- Wk 5-10: Build the MVP in React Native + Stripe + Firebase (solo, 6 weeks)
- Wk 11: Soft launch to interview list + waitlist
- Wk 12: Public launch on Product Hunt, IH, r/meditation, with Twitter thread

KILL CRITERIA
By 60 days from now:
- [ ] If <3 of 10 interviewed complainers say "yes I'd pay $5/mo for this" → kill
- [ ] If landing page CTA <2% on r/meditation traffic → kill
- [ ] If 0 of 5 warm pre-sell asks convert → pivot price down or change angle to "habit, not streak"
- [ ] If concierge pilots show people actually want more content variety, not streak-flexibility → wrong cluster, restart from rubric
```

---

## How to use the wedge template in a session

1. **Score 3-5 clusters first** using `cluster-rubric.md`
2. **Pick the top 1-3** and fill in this template for each
3. **Read them side by side** — usually one is obviously stronger
4. **Pick one** and put the rest in a "later wedges" file (you'll come back if this one dies)
5. **Send the kill criteria to a friend** — public commitment makes it easier to actually kill if needed
6. **Start the 90-day plan today.** Not tomorrow.

The most common failure mode is filling in 5 wedge templates and starting none. Pick one. Ship.
