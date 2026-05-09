# Generation Prompts

When the user is blank or vague, use these prompts to surface candidates. **Pick 2-4 lenses per session, not all 8.** Match the lens to what you know about the user (their job, audience, constraints).

Always tag generated ideas with the lens they came from. The tag matters because the *next* validation move depends on the lens.

---

## Lens 1 — Self-problem (Paul Graham)

> "What problem do *you* personally have, weekly or daily, that nobody has solved well?"

### Sub-prompts
- "What's the most annoying part of your week, every week?"
- "What workaround have you built (a spreadsheet, a script, a routine, a person you pay) because no off-the-shelf tool works?"
- "What did you Google last month that gave you no good answer?"
- "What software would make you actively happy if it existed and ran in the background?"

### Why this lens works
- Founder-market fit is automatic (you *are* the user)
- Validation is fast — interview people like you
- You can test ideas against your own behavior, not stated preferences

### Why it fails
- Your problems may be too niche or non-monetizable
- "Problems software people have" market is overcrowded
- You may be wrong about how unique your problem is

### Output format
For each candidate, draft:
- The problem in one sentence
- The current ugly workaround
- The named ICP (yourself + people like you)
- A guess at WTP

---

## Lens 2 — Schlep blindness (Paul Graham)

> "What problems do smart founders avoid because they sound boring, painful, regulated, or unsexy?"

### Sub-prompts
- "What industry do you cringe to think about working in? Why?"
- "What problem requires sales, not just product? Most founders avoid that."
- "What problem requires regulation expertise? (Healthcare, finance, defense, govtech)"
- "What problem requires unsexy operational work (data labeling, customer migration, manual onboarding)?"
- "What problem requires you to build *trust* with skeptical buyers (lawyers, doctors, plumbers)?"

### Why this lens works
- The competitive set is tiny — most founders self-select out
- The buyers are starved for builders who care
- Margins are usually high (because of the schlep)

### Why it fails
- You actually have to do the schlep — it's painful by construction
- Distribution is harder (your buyer isn't on Twitter)
- Long sales cycles for B2B variants

---

## Lens 3 — Insider knowledge (Arvid Kahl)

> "What does your day job let you see that outsiders can't?"

### Sub-prompts
- "What internal tool at your company should be a startup? (And why doesn't it leak out?)"
- "What's the internal joke about which tool 'doesn't work'?"
- "What workflow do you do that requires 4+ tools chained together?"
- "What does your team buy that the market is still figuring out?"
- "What manual process exists because no software is good enough?"
- "Who in your industry would pay you $500 a month for a thing that took you 30 minutes to build?"

### Why this lens works
- Insider context is a moat
- You have customers (your colleagues, your industry peers) on tap
- You can validate at lunch instead of running ads

### Why it fails
- Risk of building "your version" of an internal tool that doesn't generalize
- Conflicts with employer (IP, non-compete)
- "Niche tool for ex-coworkers" can be too small a market

---

## Lens 4 — Live in the future (Paul Graham)

> "What's possible *now* that wasn't 2 years ago — and where's the gap?"

### Today's tailwinds (rotating list — update as the world changes)
- **AI agents** — multi-step workflows that were "just LLM chat" a year ago
- **Foundation-model APIs** — multimodal understanding, real-time voice, code execution
- **On-device ML** — Apple Intelligence, local LLMs, privacy-preserving features
- **Real-time voice** (Realtime APIs, ElevenLabs, etc.) — voice agents that feel human
- **Robotics + foundation models** — humanoids, warehouse, last-mile
- **Compute getting cheap** — fine-tuning under $100, inference at scale
- **Coding agents** — Claude Code, Cursor, Devin, etc., reshaping software development itself
- **Regulatory shifts** — AI act (EU), CSRD reporting, data residency, child safety online
- **Demographic** — boomer retirement (services + capital), Gen Z entering the workforce, aging in place
- **Energy** — battery cost curves, solar penetration, grid software
- **Climate compliance** — corporate disclosure requirements, carbon accounting

### Sub-prompts
- "What tedious workflow could be replaced by an agent now?"
- "What used to require a $5M ML team and now needs an API call?"
- "What used to require a phone bank and now needs a voice agent?"
- "What used to be 'we'd need a human to read this' and now isn't?"
- "What old industry needs new compliance software due to recent regulation?"
- "What demographic shift is creating new buyers in old categories?"

### Why this lens works
- You're surfing, not paddling against the current
- New capabilities create temporary monopolies before incumbents react
- The 18-month window is real — first mover with strong execution wins

### Why it fails
- The space is crowded with founders chasing the same wave
- Wrappers without moats get crushed by foundation models eating the workflow
- Timing risk — you might be 2 years too early

---

## Lens 5 — Niche / vertical (Pieter Levels, Arvid Kahl)

> "What underserved community has bad software and a name they call themselves?"

### Sub-prompts
- "What's a community that runs on Excel + Slack + Zoom + manual spreadsheets?"
- "What's an industry where the best software is from 2008?"
- "What's a profession with a strong identity and a trade publication?"
- "What's a hobby community that spends real money?"
- "What audience would you genuinely enjoy spending the next 5 years with?"

### Vertical SaaS prompt list (boring industries, active 2024-2025 demand)
- Trade services: HVAC, plumbing, electricians, roofers, landscapers, pest control, pool service
- Health adjacent: dental hygienists, chiropractors, physical therapists, optometrists, vets
- Personal services: hair salons, barbers, nail salons, spas, tattoo studios
- Food: small distillery, food trucks, bakeries, butchers, catering
- Real estate: property managers, HOAs, RV parks, mobile home parks, self-storage
- Niche manufacturing: small CNC shops, machine shops, custom cabinetmakers
- Trucking: independent owner-operators, freight brokers, trucking dispatch
- Field service: pest control, alarm/security install, propane, oil & gas service
- Legal: solo practitioners, court reporters, paralegals
- Funeral homes, cemeteries, monument makers
- Independent insurance brokerages
- Music teachers, tutors, sports coaches

### Why this lens works
- The category leader has been around since 2003 and the UI is awful
- Buyers are *thrilled* when someone shows up
- Network effects: one happy customer in a 50-person trade community brings 5 friends

### Why it fails
- TAM is real but capped — exit might be $30M-$200M, not $1B
- Distribution requires showing up at trade shows / Facebook groups, not running Twitter ads
- High-touch onboarding (which is also a moat — see lens 2)

---

## Lens 6 — Boring / cash-flow (Andrew Wilkinson)

> "What unsexy industry runs on Excel and PDFs?"

### Sub-prompts
- "What industry would your friends laugh at if you announced you were building software for it?"
- "What category does VC ignore?"
- "Where are the buyers offline (newspaper readers, conference attendees, trade journal subscribers)?"
- "What businesses are profitable but not 'tech'? Could you sell them software they need?"

### Tip
"Boring" overlaps heavily with "schlep blindness" and "vertical SaaS." Use this lens when the user wants a cash-flow business, not venture scale. The mental model is "tiger product" (Wilkinson) — durable, profitable, dominant in a small pond, not trying to take over the world.

---

## Lens 7 — Adjacent (YC RFS, Lenny Rachitsky)

> "Pick a category leader. What's the obvious extension nobody's built?"

### Sub-prompts
- "What does Notion not do that Notion users wish it did?"
- "What feature do users beg for in [Tool X]'s subreddit?"
- "What workflow happens *next* after the user finishes with [Tool X]?"
- "What does [Tool X] cost? Could you offer 80% for 20% to a price-sensitive segment?"
- "Who is *underserved* by [Tool X] — too small, wrong vertical, wrong region?"

### Adjacency patterns
- **Vertical version:** Stripe → Stripe for healthcare, Stripe for marketplaces
- **SMB version:** Salesforce → HubSpot
- **Region version:** Toast → version for [country]
- **Add-on:** Calendly → Calendly for sales teams (Chili Piper)
- **Workflow neighbor:** Figma is upstream of design QA → Figma plugin or design QA tool

### Why this lens works
- Demand is proven (the category exists)
- Buyers are easy to identify (users of the leader)
- You don't have to educate the market

### Why it fails
- The leader can copy you (or already has the feature in beta)
- Distribution: how do you reach their users without using their platform?
- "Better cheaper alternative" rarely wins — it's a race to zero

---

## Lens 8 — Complaint mining

> "Where are people loudly unhappy?"

**For deep, systematic complaint mining (App Store / Play Store / Reddit / G2 scraping with Python scripts and Claude clustering), see the dedicated [`complaint-mining`](../../complaint-mining/) skill.** This lens is the lightweight version — useful when complaint mining is one of several generation lenses you're running in a session.

### Sub-prompts
Run searches systematically, not casually. For each, take 5 verbatim quotes:

- **Reddit:** `site:reddit.com "I hate" [keyword]`, `site:reddit.com "the worst part of [keyword]"`, top posts in 3-5 relevant subs
- **G2 / Capterra:** 1-star and 2-star reviews of every major competitor
- **Twitter / X:** `"[tool] is so" "[adjective]"`, `"why does [tool]" "[broken thing]"`
- **YouTube:** comments under tutorials for the legacy tool
- **Hacker News:** Algolia search the keyword, sort by points, read comments
- **Trustpilot, Glassdoor:** for industries with public-facing services
- **App store:** 1-star reviews of the top 5 apps in the category

### What you're looking for
- The same complaint repeated by 5+ people in different places
- Specific descriptions ("it crashes when I try to export to PDF") not generic ("it sucks")
- Public anger — the louder, the more they care

### What you do with the output
- Use the verbatim quotes as your headline candidates
- Each cluster of complaints = a wedge
- Reach out to the *complainers* directly. They're already pre-qualified.

---

## Combining lenses

The strongest ideas usually come from **intersecting two lenses**:

| Combination | Pattern |
|---|---|
| Self-problem × Niche | "I'm a [niche], here's what I needed but couldn't find" |
| Insider × Live in the future | "I worked in X for 5 years, AI now makes Y newly possible" |
| Schlep × Boring | "Nobody wants to build software for funeral homes; they'll pay anyway" |
| Adjacent × Niche | "[Tool X] but for [specific niche]" |
| Complaint mining × Live in the future | "Here's an angry thread; here's why AI fixes it now" |

When generating, try one combo per round. After 3-4 rounds, you'll have 30-40 candidates and 5-10 will be obviously stronger than the rest.

---

## Output format

When generating ideas, present as a table:

```
| # | Idea (1 sentence) | Lens(es) | Audience | Why now |
|---|---|---|---|---|
| 1 | An AI agent that writes weekly status updates for engineering managers from their Jira + GitHub activity | Self × Live in future | EM at 50-500-person startups | LLMs cheap enough for nightly batch summarization |
| 2 | Compliance reporting for mid-size manufacturers under CSRD | Boring × Live in future | EU manufacturers $50M-$500M revenue | CSRD takes effect for this band 2025 |
| ... | ... | ... | ... | ... |
```

Then, after the table, **highlight 3-5** for closer scoring on the rubric. The point of generation is to make the picking obvious.
