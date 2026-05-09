# Validation Playbook

The job: learn whether the problem is real and whether they'd pay — *without writing production code*.

The cheapest test that gives a yes/no signal wins. Don't run an expensive test when a cheap one will do.

## The validation ladder

Climb in order. Each rung is more expensive (in time + ego) than the last. Stop climbing when a rung gives you a clear "yes, build it" signal.

| Rung | Time | Cost | Output signal |
|---|---|---|---|
| 1. Demand signal scan | 1 hour | $0 | Are people complaining publicly? |
| 2. Mom Test interviews | 1-2 weeks | $0-$200 (gift cards) | Is the pain real? Specific? Currently spending? |
| 3. Landing page + waitlist | 1-3 days | $0-$200 | Will targeted traffic give an email? |
| 4. Fake-door / pricing test | 1 day on top of #3 | $0 | Will they click "Buy now" at a stated price? |
| 5. Concierge MVP | 1-2 weeks | varies | Will they accept the manually-delivered service? |
| 6. Wizard of Oz | 1-3 weeks | varies | Will they use it when it looks automated? |
| 7. Pre-sell | varies | $0 | Will they put a credit card down before product exists? |
| 8. PMF survey (post-MVP only) | 1 day | $0 | Are 40%+ "very disappointed" without it? |

---

## Rung 1: Demand signal scan (1 hour)

Before any interviews, do desk research. Search for the problem in users' own words.

**Where to look:**
- **Reddit** — search for the problem in 3-5 relevant subreddits. Look at posts with high upvotes that aren't questions but rants. Read the comments.
- **X/Twitter** — search for "[problem keyword] is so [adjective]" or "I hate [adjective] [tool]"
- **G2 / Capterra / Trustpilot** — read 1-star and 2-star reviews of competitors. Each complaint is a feature wedge.
- **YouTube comments** — under tutorials for the legacy tool you'd replace
- **Indie Hackers, Hacker News** — search for the keyword
- **Niche forums and Slack/Discord communities** — same searches, but the audience is more concentrated

**Output:** A list of 10-20 verbatim quotes from real users describing the pain in their own language. Save them. They become headlines and ad copy.

**Decision rule:**
- 0 quotes found in 1 hour → demand might not exist publicly. Mom Test interviews are now the priority.
- 5-10 quotes → confirmed background pain. Proceed to interviews.
- 20+ angry quotes → strong tailwind. Skip interviews if you must, go to landing page.

---

## Rung 2: Mom Test interviews

See `templates/interview-script.md`. Do 8-15 in 1-2 weeks. Stop when the next person's story is predictable.

**Recruiting:**
- LinkedIn cold message (target: 30% reply rate). Lead with research, not product.
- Niche Slack / Discord / subreddit posts ("I'm researching how [role] handle [thing] — 20 min, anyone open?")
- Warm intros from previous interviewees
- Existing audience (mailing list, twitter followers) if you have one
- $25 gift card for cold prospects if needed (skip for warm)

**Do not pay for interviews on UserTestify-style platforms when validating a startup idea.** The participants are professional respondents, not real prospects.

---

## Rung 3: Landing page + waitlist (1-3 days)

The single best pre-build validation move. Most idea-stage founders skip this for months. Don't.

### Build it

- One page. Hero, value prop, 3 features, social proof (or a "as researched on" if you don't have any), CTA.
- Tools: Carrd, Framer, Webflow, Notion, plain HTML. Don't spend more than a day building.
- Hand off the actual copy to `copywriting` if needed.

### Drive traffic (the harder part)

You need **300-1,000 targeted visitors** for a meaningful signal. Cheap channels:

- **Reddit posts** in 1-3 relevant subs — share genuine context, not spam. Best post type: "I built X to solve Y — here's why" or "Free tool for [niche]." Subreddit rules vary.
- **Twitter / X** — your own audience plus 2-3 friends with relevant followers
- **Hacker News Show HN** — only if the build is interesting, not for early validation
- **Indie Hackers** — same caveat
- **Niche newsletters** — sponsorship, $50-$500
- **Targeted ads** — Reddit ads, X ads, LinkedIn ads. $100-$300 budget. Best for B2B with a clear ICP.
- **Cold outreach** — 50 personalized emails to LinkedIn ICP, with the landing page as the CTA

### Read the signal

Set up basic analytics (Plausible, Simple Analytics, GA4). Track:

- **Visitors** (denominator must be qualified — junk traffic from random subs doesn't count)
- **CTA click rate** (% who click the primary action)
- **Email signup rate** (% who give email)
- **Pricing-test "Buy now" click rate** (if you ran rung 4)

**Benchmarks** (rough; varies wildly by category):
- ≥10% CTA clicks on qualified traffic = strong demand signal
- 5-10% = moderate; investigate which segments converted
- <2% on qualified traffic, multiple sources = the message or the offer is wrong

### Common mistakes
- Driving unqualified traffic (general subreddits, broad ads), then concluding "no demand"
- Giving up after 50 visitors. Need 300+ for any signal.
- Burying the CTA. The CTA is the test — make it the loudest thing on the page.
- Not iterating headlines. Try 2-3 headlines on the same page; whichever wins is your real value prop.

---

## Rung 4: Fake-door pricing test (1 day on top of rung 3)

Add a "Buy now" or "Start trial" button with a stated price. When clicked, show:

> "Thanks — we're not quite live yet. Drop your email and we'll let you know the moment your account is ready. We'll honor the [$X/mo] price you saw today as long as you sign up by [date]."

The CTA click is the test, not the email capture. Click-through to "Buy" tells you about **price tolerance**, not just curiosity.

**What to test:**
- Multiple price points on different visitor cohorts ($29, $49, $99/mo)
- Annual vs monthly framing
- "Free trial" vs "Start free, paid plans from $X" vs "Pricing"

**Benchmark:** If 0% of qualified visitors click a "Buy now" button at a stated price, the price (or the offer) is wrong.

---

## Rung 5: Concierge MVP (1-2 weeks)

Recruit 3-5 customers (preferably from your interviews — already warm). Deliver the service **manually**, by hand, no software.

**Examples:**
- Idea: AI tool that summarizes weekly Slack activity → You spend 2 hrs/week reading their Slack, write the summary in a Google Doc, email it.
- Idea: Automated bookkeeping → You manually reconcile their books in QuickBooks for 30 days.
- Idea: AI sales coach → You watch their sales calls and write feedback yourself.

**Charge.** Even $50 for the manual service. Free customers don't tell the truth.

**The signal you're looking for:**
- Do they keep using it? (Engagement)
- Do they recommend it to peers? (Referrals)
- Will they renew or extend? (Retention)
- Do they pay on time, without complaint? (Real WTP)

**The point:** Confirm they value the *outcome* before you build the *mechanism*. If concierge fails, automation won't save it.

---

## Rung 6: Wizard of Oz (1-3 weeks)

A working software UI that pretends to be automated but is humans on the back end. Common pattern for AI features in 2024-2025:

- User clicks "Generate" → request goes into a queue → you (or an offshore VA) fulfill it manually → response appears in the UI

The customer experience is "the product works"; your reality is you're doing it by hand.

**When to use this:**
- The expected experience requires a believable software UI (concierge feels too high-touch)
- The "automation" is the part you're least sure about — test if the *outcome* is valued before investing in the model/integration

---

## Rung 7: Pre-sell (varies)

Take real money before the product exists.

**Two patterns:**

**Pattern A: B2B pilot** — write a one-page pilot agreement: "We'll deliver [outcome] over 30/60/90 days. $X for the pilot, with credit toward your first year if you continue. If you're not happy at the end, full refund." Sell to 3-5 design partners.

**Pattern B: B2C / prosumer pre-order** — post a Stripe pre-order link with a delivery date. Wave it in front of warm prospects.

**The signal:**
- Pre-sell to 3-5 warm contacts → minimum bar
- Pre-sell to 1-2 cold prospects → strong signal
- Crickets → either the offer is wrong, the price is wrong, or the problem isn't acute

**Key:** Pre-sells must hurt to fail. If you frame it as "no commitment, just an indication of interest," you'll get yes from people who'd never pay. The point of the credit card is the friction.

---

## Rung 8: PMF survey (post-MVP)

Source: Rahul Vohra. Don't use this until you have 40+ active users on a working product.

> "How would you feel if you could no longer use [product]?"
>
> a) Very disappointed
> b) Somewhat disappointed
> c) Not disappointed
> d) N/A — I don't use it anymore

**Rule:** ≥40% "very disappointed" = product-market fit.

Below 40%, focus on the "very disappointed" cohort: who are they, what's the main benefit they cite, what would they want next? Build for *them*, not the average.

---

## Choosing the right rung

| Situation | Start here |
|---|---|
| "I have an idea, no users yet, no audience" | Rung 1 → 2 → 3 |
| "I've done 10 interviews, people seem interested" | Rung 3 + 4 (don't do more interviews) |
| "I have a B2B service I can deliver manually" | Rung 5 directly |
| "I have warm prospects from interviews" | Rung 7 (pre-sell) directly |
| "I have an MVP and 100 users" | Rung 8 |

The most common failure mode: **camping on rung 2** for months. Three weeks of interviews is enough; then climb.

---

## What "validated" means

You're done with this skill (and ready to hand off to `product-management`) when you can answer all three of these with specifics:

1. **Who** — first ICP, named (with 5+ specific people you could text)
2. **What** — the JTBD they're hiring you for, in their own words
3. **Why now** — the tailwind or the breakage that makes this a problem worth $X to them today

If any of these is fuzzy, you're not validated yet — keep climbing the ladder.
