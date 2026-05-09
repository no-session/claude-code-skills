# Claude / LLM Prompts

Copy-paste prompts for the manual side of the workflow (when you don't want to run the script). Designed for Claude Sonnet/Opus; works on other frontier LLMs with minor adjustments.

For the scripted version, see `scripts/cluster_with_claude.py`.

---

## Prompt 1 — Complaint clustering

**System / role:**

```
You are a senior product researcher running voice-of-customer analysis for an indie founder. You cluster raw user complaints into actionable product themes.

Output rules:
- Produce 5-12 distinct clusters. Merge near-duplicates.
- Name each cluster in the users' own language (e.g., "i lose my streak from one missed day"), not abstract jargon.
- For each cluster: name, 1-line description, 3-5 verbatim quote excerpts (with original wording, including typos), estimated frequency as % of input reviews, and severity tag.
- Severity tags: "showstopper" (people uninstall), "annoyance" (people stay but complain), "vitamin" (nice-to-have wish).
- Drop clusters that are about price, billing, refunds, or customer support — focus on product clusters.
- Output strictly valid JSON. No prose before or after.
```

**User:**

```
Here are {N} user complaints (one per line, prefixed with [rating★]).

[paste 200-500 reviews here, one per line]

Cluster them per the rules above. Output JSON with this shape:

{
  "clusters": [
    {
      "name": "cluster name in user words",
      "description": "1-line description",
      "frequency_pct": 17,
      "severity": "showstopper|annoyance|vitamin",
      "verbatim_quotes": ["quote 1", "quote 2", "quote 3"]
    }
  ],
  "total_reviews_input": N,
  "notes": "any caveats about the data quality"
}
```

---

## Prompt 2 — Cluster sanity check

After Pass A, run this to catch common errors.

```
Here are {N} complaint clusters from a meditation app review-mining pass:

[paste cluster JSON]

Audit them as a skeptical researcher would:

1. Flag any clusters that are actually two distinct issues mashed together. Suggest the split.
2. Flag any near-duplicate clusters that should be merged. Suggest the merge.
3. Flag any cluster whose verbatim quotes don't actually match the cluster description.
4. Flag any cluster that looks like it might be confirmation bias (e.g., one or two loud reviewers, not a real pattern).
5. Suggest 1-3 clusters that *should* exist based on the verbatim quotes but weren't named.

Output as a structured list of findings, no JSON needed.
```

---

## Prompt 3 — Hypothesis generation from a cluster

Once you have a strong cluster, ask Claude to draft wedge concepts.

```
You are an indie hacker advisor. I've identified the following complaint cluster from public reviews of [target app/category]:

CLUSTER NAME: [cluster name]
FREQUENCY: [X]% of analyzed reviews
SEVERITY: [showstopper / annoyance / vitamin]
VERBATIM QUOTES:
1. "..."
2. "..."
3. "..."
4. "..."
5. "..."

Generate 5 distinct wedge concepts a solo founder could ship in 30-90 days that would address this cluster. For each, output:

- One-line description (what it is)
- Specific ICP (who exactly buys it; demographic + role + life stage)
- Pricing model (one-time / monthly; price range)
- 3-feature MVP (smallest possible scope)
- The "why incumbent won't copy this" argument
- The first-50-customer plan
- The single biggest risk

Order them from highest-conviction to lowest. The top 1-2 should be obvious bets given the cluster evidence.
```

---

## Prompt 4 — Cross-platform synthesis

When you've pulled complaints from multiple platforms (App Store + Play Store + Reddit + YouTube), synthesize cross-platform themes.

```
I have user complaints about [target app] from 4 sources:

App Store reviews (US, GB locales): [N1 reviews]
Play Store reviews (en, es, hi locales): [N2 reviews]
Reddit threads (r/[sub1], r/[sub2]): [N3 posts/comments]
YouTube comments under tutorial videos: [N4 comments]

For each cluster you identify, note:
- Which platforms it appears in (cross-platform = stronger signal)
- Whether the complaint differs by platform (Android vs iOS users may rage about different things)
- Whether the complaint differs by locale/region

Output the cross-platform clusters first (these are highest priority), then platform-specific or region-specific ones (these may be wedges for underserved segments).
```

---

## Prompt 5 — ICP profiling from complaints

Once you've picked a cluster, profile the people complaining.

```
Here are 30 verbatim complaints from public reviews + Reddit posts about [target app], all from the cluster "[cluster name]":

[paste 30 complaints, with handle / source where public]

Profile the typical complainer:
- Likely age range, life stage
- Likely profession or role
- Likely usage context (when, where, why they use the app)
- What they care about beyond this app (related interests / values you can infer)
- What other apps they probably use
- Where you'd find more of them online (specific subreddits, Discords, newsletters, podcasts)
- Their tone (formal, casual, sarcastic, anxious)

Then write 3 example "user personas" using made-up names but real composite traits.

The goal is for me to recognize these people in the wild and message them in their own register.
```

---

## Prompt 6 — Outreach DM drafting

After you have an ICP profile and a wedge concept, draft outreach messages.

```
I'm building [wedge name]: [elevator line].

The ICP is: [paste persona summary]

I'm reaching out to people who left public 1-2 star reviews on [incumbent app] specifically about [the cluster pain]. I'll DM them on [Reddit / Twitter / etc.].

Draft 3 distinct DM templates. Each must:
- Be under 80 words (longer = unread)
- Reference their specific public complaint (so it doesn't feel like spam)
- NOT pitch the product. Instead: ask if they'd be open to a 15-min chat OR be a beta tester.
- Include one specific honest claim about the wedge (no marketing fluff)
- End with a low-friction ask (yes/no or pick a time)

The 3 templates should test different framings:
1. Empathy-first ("I quit Calm for the same reason")
2. Curiosity-first ("Quick research question, not a pitch")
3. Direct-offer ("Building a fix; want free access?")

For each, also write a 1-line subject/preview text.
```

---

## Prompt 7 — Kill / build decision

When you've completed scoring and built a wedge concept, sanity-check the decision.

```
I've mined [target category] complaints. Top wedge candidate is below. Please play devil's advocate.

WEDGE: [paste the one-pager from wedge-template.md]

Argue against this build. Be specific:

1. The single most likely reason this fails in year 1.
2. The cluster I'm probably overweighting.
3. The hidden constraint I haven't considered (regulatory, technical, distributional).
4. The smarter pivot inside the same maze that I should consider.
5. The competitor or substitute I'm probably underestimating.
6. The ICP assumption that's most fragile.

End with a 1-3-5 verdict:
- 1 = kill it
- 3 = pivot before building (and exact pivot)
- 5 = build it but watch for [specific failure signal in first 90 days]
```

---

## Prompts for specific sources

### Reddit search-term generator

```
I'm researching complaints about [app/category]. Generate 30 Reddit search queries that would surface complaint posts. Mix:
- Obvious patterns ("[app] sucks", "[app] alternative")
- Emotional patterns ("hate [app] because", "[app] anxiety")
- Switching patterns ("switched from [app]", "deleted [app]")
- Workaround patterns ("instead of [app]", "use [tool] for [job]")
- Demographic patterns ("[app] for [audience]")

Output as a list with the subreddits I should run each query against.
```

### App Store review keyword filtering

```
Here are 500 raw App Store reviews of [app]. Filter to only those that:
- Express a specific product complaint (not billing/support/general "this is bad")
- Mention a workaround, alternative, or specific desired feature
- Quote a specific moment or use case

Reject reviews that are:
- Generic 1-star with no detail ("trash app")
- About price unless they name a price they'd pay
- About the developer's response, not the product

Output the filtered set as JSON: [{rating, content, why_kept}, ...]
```

---

## Pricing notes for Claude API use

- Sonnet 4.6 — input ~$3/M tokens, output ~$15/M. A 500-review cluster pass uses ~30K input + 2K output ≈ $0.12.
- Opus 4.7 — ~5x more expensive but better at messy categories with weird user dialect.
- **Use prompt caching** on the system message + cluster instructions — they don't change between iterations. Saves 90% on input cost when re-running.
- For very large corpora (5K+ reviews), batch in chunks of 300-500 and ask Claude to merge clusters across passes in a final synthesis prompt.
