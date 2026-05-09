# Frameworks: Product Ideation

This is the canonical reference. Cite the source when teaching the framework. Worked examples matter more than the names.

---

## Paul Graham — How to Get Startup Ideas

> "The way to get startup ideas is not to try to think of startup ideas. It's to look for problems, preferably problems you have yourself."
> — Paul Graham, *How to Get Startup Ideas* (2012)

### Five PG principles

| Principle | What it means | Question to ask |
|---|---|---|
| **Organic** | The best ideas come from problems the founder has personally | "What's broken in *your* daily life or work?" |
| **Live in the future** | Found a thing that's missing — not a thing nobody has | "What's possible now that wasn't 2 years ago, and where's the gap?" |
| **Schlep blindness** | Founders avoid problems that sound painful or boring; that's where the gold is | "What's a problem you've been ignoring because it sounds awful?" |
| **Self-funding founder test** | Would smart founders dismiss this? Good — they're missing it | "Whose dismissal is a buying signal?" |
| **Wave** | Ride a tech or social shift; don't fight it | "What new tailwind is opening this up?" |

### Worked example

**Bad PG-style question:** "What's a good app idea for college students?"

**Good PG-style question:** "Last week I needed to do X and I ended up emailing a spreadsheet to three people. Why is that still the best option in 2025?"

The first invites generic answers. The second points at an organic problem with a live tailwind (collaboration tooling, AI extraction, etc.).

---

## Y Combinator — Make Something People Want

YC's filter is brutally simple: **does anyone want it?** Their public material adds three operating principles:

1. **"Do things that don't scale"** (PG) — manual onboarding, hand-deliver the service, do the work of the product yourself before automating it.
2. **"Talk to users"** (every YC partner) — every week, every founder, no exceptions.
3. **RFS (Requests for Startups)** — YC's public list of "ideas we'd fund." Use it as a *seed list*, not a prescription. Current themes (rotating): AI agents for verticals, robotics, defense tech, climate, scientific tooling, "small fast businesses," AI coding tools, healthcare, government tech.

### How to use RFS as a generation lens

Don't pick an RFS bullet wholesale. Use it to ask: **"What's the *boring vertical implementation* of this RFS?"**

| RFS theme | Generic | Boring vertical |
|---|---|---|
| AI agents | "AI agent for sales" | "AI agent that updates HubSpot from voicemails for industrial reps" |
| Government tech | "Software for cities" | "License renewal system for municipal sanitation departments" |
| Climate | "Climate SaaS" | "Compliance reporting for mid-size manufacturers under CSRD" |

The vertical version is harder to fund but easier to sell.

---

## Jobs-to-be-Done (Christensen)

People don't buy products; they **hire** products to do a job. Reframe demand around the *job*, not the *user*.

### JTBD statement template

> When **[situation/trigger]**, I want to **[motivation / job]**, so I can **[expected outcome]**.

### Worked example

**Product:** A milkshake (the canonical Christensen story)

**Surface user research:** "Who buys milkshakes? Men 30-50, weekday mornings, drive-through."

**JTBD reframe:** "When I have a long, boring commute and need to keep my hand busy and my stomach full until lunch, I hire a milkshake to be a thick, slow, one-handed, non-messy breakfast."

The competitors aren't other milkshakes. They're bananas, donuts, and bagels.

### How to use JTBD in ideation

1. State the job in the canonical format above
2. List the **alternatives** people currently hire (real ones — what they actually do today)
3. List the **non-functional jobs** (status, anxiety reduction, social signal) — see Eugene Wei, "Status as a Service"
4. Ask: which alternative is doing the job *worst*, and is the gap big enough to charge for?

---

## The Mom Test (Rob Fitzpatrick)

The full method is in `templates/interview-script.md`. The core rules, distilled:

1. **Talk about their life, not your idea.** The moment you describe what you're building, the data is contaminated.
2. **Ask about specifics in the past, not generics in the future.** "When did you last do X?" not "Would you use Y?"
3. **Talk less, listen more.** If you're talking >30% of the interview, you're pitching, not learning.

### The compliment trap

If the interview ends with:
- "Cool idea!"
- "Yeah I'd totally use that"
- "Let me know when it launches"

…you got nothing. These are politeness signals.

### What real data looks like

- **A story:** "Last month we lost a deal because…"
- **Specific numbers:** "I spend like 4 hours every Friday on this"
- **A current alternative:** "Right now I do this in a Google Sheet plus three Slack DMs"
- **Money:** "I pay $89/mo for [tool] but it doesn't [thing]"
- **Emotion:** "It drives me insane that…"

---

## The Idea Maze (Balaji Srinivasan)

> "A good entrepreneur has a thesis on how the maze works. They've thought through every dead end."

The Idea Maze is a tree of every possible version of solving a given problem. Before committing to one branch, you should be able to articulate why the others are wrong (or worse, for now).

### How to run it

1. State the **underlying problem** in one sentence (not your solution)
2. Branch on these vectors, generating 1-3 sub-ideas each:
   - **Audience:** B2C, prosumer, SMB, mid-market, enterprise
   - **Wedge:** Which sub-task or single feature you start with
   - **Distribution:** Bottoms-up, top-down, viral, content, PLG, sales-led, partnerships
   - **Business model:** Subscription, usage, marketplace take rate, lead gen, services, hardware, ads
   - **Time horizon:** Cash-flow business in 6 months vs. venture-scale in 7 years
3. For each branch, write a **one-sentence thesis** ("This wins because…") and a **one-sentence killer** ("This dies because…")
4. Pick the branch with the strongest thesis *that you can act on this month*

### Worked example

**Problem:** Independent bookkeepers spend 6+ hours/week reconciling client receipts.

| Branch | Thesis | Killer |
|---|---|---|
| AI receipt-extractor SaaS, $29/mo | Painful, painkiller, mature CV models make it cheap | Already 5 competitors; race to zero margin |
| Done-for-you service ($500/mo) | High WTP, no software risk | Low margin, hard to scale, you become an agency |
| Enterprise add-on for QuickBooks | Big budget, mature buyer | 18-month sales cycle, you have no logos |
| White-label for accounting firms | Each firm = 50 clients, 1:50 sales leverage | Long deal cycles, custom asks |
| Open-source tool, paid hosted version | Distribution via dev/finance crossover | Hard to monetize, niche audience |

**Pick:** White-label, because you have an aunt who runs an accounting firm. (Founder-market fit beats market size early.)

---

## Arvid Kahl — Audience-First / Embedded Entrepreneur

Most founders pick a problem then go hunt for users. Kahl's inversion: **pick an audience you're already part of, embed for months, and the problem will surface itself.**

### The audience filter

A good audience to build for:
1. Has **a name they call themselves** ("freelance illustrators," not "creative people")
2. Hangs out in **identifiable places** (subreddit, Discord, Slack group, conference, trade publication)
3. Has **disposable budget or business expenses**
4. Has **public complaints** you can read

### How to embed

- Join the Slack/Discord/subreddit. Read for two weeks before posting.
- Show up at industry events (online or off).
- Interview 20 members about their *work*, not your idea.
- Become known as "the person who's curious about how this industry works."
- The idea will appear by week 3 or 4.

### Why this works

You compress the "find an idea" and "find a distribution channel" steps into one. By the time you have an idea, you also have 100 warm leads.

---

## Pieter Levels — Indie Niche Micro-SaaS

Pieter's body of work (NomadList, RemoteOK, PhotoAI) suggests these tactics:

- **Build in public.** Tweet every metric. The audience compounds.
- **Niche to a community you're in.** Nomads, photographers, indie founders.
- **One person, no funding.** Constraint forces simplicity.
- **Ship in days, not months.** First version live in 7 days.
- **Charge from day one.** Free users don't tell the truth.
- **Layer products.** Each launch becomes a distribution channel for the next.

This is the opposite of YC-scale advice. Use it when the user wants a $30K-$500K/mo business, not a $1B outcome.

---

## Andrew Wilkinson — Boring / Cash-flow Businesses

Wilkinson (Tiny, Meteor) buys and builds unsexy, profitable, durable businesses. The lens for ideation:

- Look for industries where **the software is 15 years old** and the buyers are not on Twitter
- Look for businesses where **the founder wants to retire** (acquisition lane, but the same instinct points at greenfield gaps)
- "Boring" is not a bug — it's a moat. Smart competition stays away.

### Examples of "boring" categories with active 2024-2025 SaaS gold rushes
- Pool service, HVAC, plumbing, landscaping (vertical SaaS)
- Funeral homes, cemeteries
- Self-storage, RV parks, mobile home parks
- Independent insurance brokerages
- Veterinary clinics, dental practices
- Court reporting, legal services
- Trucking dispatch, freight brokerage
- Inventory for small manufacturers

If the category makes you wince, look closer.

---

## Jason Cohen — Painkiller vs Vitamin

> "If your product is a painkiller, customers will tolerate ugly software, missing features, and bad onboarding. If it's a vitamin, every flaw becomes an excuse to leave."

### The test

A painkiller has these signals:
- Users can name the **specific moment** the pain hits
- Users have **a workaround** in place today (hacks, spreadsheets, hired help)
- Users **complain publicly** about the pain
- Users **search** for solutions (Google trends, "best X for Y" queries)
- Users have **switched tools before** trying to fix it

A vitamin has these signals:
- Users say "that would be nice" but can't name a moment
- No current workaround — they just live with it
- No search volume, no public complaints
- No switching history — never bothered

**Default to painkiller categories.** Vitamins occasionally win (Notion, Figma) but require world-class execution and a tailwind. Painkillers tolerate average execution.

---

## Marc Andreessen — Market > Team > Product

> "In a great market — a market with lots of real potential customers — the market pulls product out of the startup. In a terrible market, you can have the best product in the world and an absolutely killer team, and it doesn't matter — you're going to fail."

### The implication for ideation

When scoring an idea, weight the *market* more than your *clever solution*. A mediocre product in a hungry market beats a brilliant product in a dead market every time.

A "great market" signal stack:
- People are **already paying for** terrible alternatives
- The category has **growing search volume**
- New entrants are **getting funded or growing**
- Buyers can **describe the urgency** in their own words
- There's a **regulatory, technological, or demographic shift** pulling demand up

If three or more of these don't apply, the market is probably not great — even if the idea sounds clever.

---

## Eugene Wei — Status as a Service (consumer only)

For consumer products, the unit of analysis isn't utility — it's status. People use products that give them **proof of work** for accumulating social capital.

Questions to ask of a consumer idea:
1. What's the **scarce signal** the user gets to display?
2. What's the **proof of work** required to earn it?
3. What **new social graph** does this create?
4. Why can't the user get the same status from an existing platform?

If the answers are weak, the consumer product will probably not retain.

---

## Rahul Vohra — PMF Survey

After you have a working MVP and 40+ active users, ask them:

> "How would you feel if you could no longer use [product]?"
>
> a) Very disappointed
> b) Somewhat disappointed
> c) Not disappointed
> d) N/A — I don't use it anymore

**Rule:** ≥40% answering "very disappointed" = product-market fit.

This is the post-build signal. Don't use it pre-launch — but design your MVP knowing this is the bar.

Follow-up questions for the "very disappointed" segment:
1. What type of person do you think would most benefit from [product]?
2. What's the main benefit you receive?
3. How can we improve [product] for you?

The first answer reveals **who the real ICP is** (often different from who you thought). The second reveals the **headline value prop**. The third reveals the **next quarter's roadmap**.

---

## Putting it together

Different lenses for different jobs:

| Job | Use |
|---|---|
| Generate ideas from blank | PG (organic), schlep blindness, niche/audience (Kahl), boring (Wilkinson) |
| Reframe an idea | JTBD |
| Find pivot options | Idea Maze |
| Score an idea | Painkiller/vitamin (Cohen), market lens (Andreessen) |
| Validate cheaply | Mom Test |
| Confirm PMF post-MVP | Vohra survey |

Most users won't need all of them in one session. Pick the 2-3 that fit where they are.
