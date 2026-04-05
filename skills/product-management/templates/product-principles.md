# Product Principles

Our foundational beliefs about how we build product. These principles guide every decision — from what we choose to build, to how we prioritize, to how we ship.

---

## 1. Start with the Customer Problem

Every feature, initiative, and project begins with a clearly articulated customer problem. We don't build solutions looking for problems. We deeply understand user pain points through research, data, and direct conversation before committing resources.

**What this looks like:**
- Before any PRD is written, the PM must articulate the problem in one sentence a customer would agree with.
- We maintain a living "customer pain log" sourced from support tickets, sales calls, user interviews, and usage analytics.
- We distinguish between *stated needs* (what customers ask for) and *latent needs* (what they actually struggle with but can't articulate).

**Anti-patterns to avoid:**
- Building features because a competitor has them
- Shipping something because an executive had an idea in the shower
- Confusing "customers asked for X" with "customers need X"

---

## 2. Bias Toward Action

Speed matters. We prefer shipping an 80% solution quickly and iterating over spending months perfecting something in isolation. Fast feedback loops from real users are more valuable than internal debates.

**What this looks like:**
- If a decision is reversible, make it quickly. Reserve deep deliberation for irreversible, high-stakes choices.
- We set aggressive timelines and cut scope to meet them rather than pushing dates.
- "What's the smallest version of this we could ship this week?" is a question we ask constantly.

**Anti-patterns to avoid:**
- Bikeshedding on low-stakes decisions
- Waiting for perfect data before acting
- Confusing motion with progress — shipping fast means shipping *something that teaches us*, not just shipping anything

---

## 3. Outcomes Over Output

We measure success by the impact we create, not the features we ship. A quarter with one high-impact release beats a quarter with ten low-impact ones.

**What this looks like:**
- Every initiative has measurable success metrics defined before development begins.
- We celebrate moving metrics, not launching features.
- Quarterly reviews focus on "what changed for our users" not "what did we build."
- We're willing to kill features that shipped but didn't move the needle.

**Anti-patterns to avoid:**
- Equating a busy roadmap with a productive team
- Counting story points or PRDs as measures of PM effectiveness
- Refusing to sunset features because "we already built it"

---

## 4. Simplicity is a Feature

Complexity is the enemy of adoption. We ruthlessly simplify — removing steps, reducing cognitive load, and saying no to feature creep. The best product is one that feels effortless.

**What this looks like:**
- For every feature added, ask: can we remove something else? Does this make the core experience simpler or more complex?
- We design for the 80% use case. Power-user features live behind progressive disclosure.
- Onboarding should require zero documentation. If users need a guide, the UX has failed.
- We regularly audit our product surface area and deprecate what isn't earning its keep.

**Anti-patterns to avoid:**
- Adding toggles and settings to avoid making product decisions
- "Just add a tooltip" as a solution to confusing UX
- Letting optionality masquerade as flexibility

---

## 5. Build for the Long Term

We make decisions that compound over time. Technical debt, UX debt, and organizational debt are real costs. We invest in foundations that scale.

**What this looks like:**
- Every quarter includes dedicated capacity (typically 15-20%) for paying down debt and improving infrastructure.
- We choose boring, proven technology unless there's a compelling reason not to.
- We write tests, maintain documentation, and design APIs that won't embarrass us in two years.
- We think in terms of platforms and primitives, not just features.

**Anti-patterns to avoid:**
- Treating debt paydown as "nice to have" that always gets bumped
- Rewriting from scratch instead of incrementally improving
- Over-engineering for hypothetical future requirements

---

## 6. Transparency and Intellectual Honesty

We share context broadly, admit when we're wrong, and change course when the data tells us to. Ego has no place in product decisions.

**What this looks like:**
- Post-mortems are blameless. We focus on systems, not individuals.
- Metrics dashboards are accessible to everyone — not just leadership.
- When an experiment fails, we say so publicly and share what we learned.
- PMs openly share the reasoning behind prioritization decisions, including what was cut and why.
- "I don't know" and "I was wrong" are respected answers.

**Anti-patterns to avoid:**
- Cherry-picking metrics that make a launch look successful
- Hiding bad news or burying negative experiment results
- Making decisions in private channels and presenting them as fait accompli

---

## 7. Cross-Functional Partnership

Great products come from engineering, design, and product working as true partners — not a relay race. We involve all disciplines early and often.

**What this looks like:**
- Engineers and designers are included in problem discovery, not just solution delivery.
- Technical feasibility informs product decisions from day one — not as a gate at the end.
- We share credit across the whole team. There is no "product's idea" vs. "engineering's implementation."
- Design reviews, tech reviews, and product reviews happen together, not in sequence.

**Anti-patterns to avoid:**
- PMs writing specs in isolation and "throwing them over the wall"
- Treating design as "making it pretty" after the product decisions are made
- Engineers learning about customer context only from Jira tickets

---

## 8. Opinionated but Open-Minded

We have strong convictions about our product direction, loosely held. We make decisive product bets but remain genuinely open to evidence that challenges our assumptions.

**What this looks like:**
- We ship with conviction but instrument everything to learn.
- Product debates are resolved with "let's test it" whenever possible.
- We distinguish between core beliefs (slow to change) and tactical approaches (fast to change).
- Customer feedback is treated as signal, not gospel — we synthesize patterns, not react to individual requests.

**Anti-patterns to avoid:**
- Flip-flopping on strategy every time a customer complains
- Stubbornly holding a position in the face of overwhelming counter-evidence
- Treating every customer request as a referendum on product direction

---

*These principles are living guidelines. We revisit and refine them as our product, market, and team evolve. If a principle consistently leads to bad outcomes, we change the principle — not the outcome.*
