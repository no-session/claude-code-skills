# PRD Review Rubric

Use this rubric when reviewing PRDs. Internalize the criteria but deliver feedback as narrative — not a scorecard. The PM should walk away knowing exactly what to fix and why, not staring at a table of numbers.

---

## Scoring Scale

| Score | Meaning |
|-------|---------|
| **0 — Missing** | Section is absent or contains only placeholder text |
| **1 — Weak** | Section exists but lacks substance, specificity, or evidence |
| **2 — Adequate** | Section covers the basics but has gaps or could be sharper |
| **3 — Strong** | Section is clear, specific, evidence-backed, and actionable |

---

## Section Rubric

### 1. Problem Statement

| Score | Criteria |
|-------|----------|
| 0 | No problem statement, or just a feature description disguised as a problem |
| 1 | Problem is stated but vague, lacks specificity about who has it or how severe it is |
| 2 | Clear problem with identified personas, but missing quantified impact or evidence |
| 3 | Specific problem, clear personas with severity ratings, supported by quantitative and qualitative evidence, consequences of inaction articulated |

**Key questions:** Can you state the problem in one sentence a customer would agree with? Is there evidence this is real and not assumed? Do we know how many people are affected and how badly?

---

### 2. Goals & Success Metrics

| Score | Criteria |
|-------|----------|
| 0 | No goals or metrics defined |
| 1 | Goals exist but are vague ("improve the experience") with no measurable targets |
| 2 | Measurable goals with targets, but missing baselines, timelines, or guardrail metrics |
| 3 | Primary and secondary goals with specific metrics, current baselines, targets, measurement methods, evaluation timelines, and guardrail metrics that must not regress |

**Key questions:** Could an engineer look at these metrics and know exactly what to instrument? Will we actually be able to tell if this worked 4 weeks after launch? Have we defined what "done" looks like?

---

### 3. Solution Overview

| Score | Criteria |
|-------|----------|
| 0 | No solution described, or just a list of features with no context |
| 1 | High-level description but no user flows, no wireframes, no alternatives considered |
| 2 | Clear approach with user flows, but missing wireframes/mocks or alternatives considered |
| 3 | Well-articulated approach focused on user experience, key user flows documented, wireframes or mocks linked, alternatives considered with clear reasoning for the chosen approach, "do nothing" option evaluated |

**Key questions:** Can a designer start working from this? Does this explain *why* this approach over others? Is the solution framed around user outcomes, not just system behavior?

---

### 4. Requirements (P0/P1/P2)

| Score | Criteria |
|-------|----------|
| 0 | No requirements listed, or just a vague feature wishlist |
| 1 | Requirements exist but no priority tiers, no acceptance criteria |
| 2 | Prioritized requirements (P0/P1/P2) but acceptance criteria are vague or inconsistent |
| 3 | Clear P0/P1/P2 tiers, each requirement has specific and testable acceptance criteria, explicit out-of-scope section with reasoning |

**Key questions:** Could QA write test cases from the acceptance criteria alone? Is it clear what's a launch blocker vs. a nice-to-have? Are we explicit about what we're NOT building?

---

### 5. Technical Considerations

| Score | Criteria |
|-------|----------|
| 0 | No technical context provided |
| 1 | Minimal technical notes, no risk assessment |
| 2 | Architecture notes and some risks identified, but missing migration plan or backward compatibility analysis |
| 3 | Data model changes, API changes, third-party dependencies, performance considerations, technical risks with mitigations, migration and rollback plan |

**Key questions:** Has engineering reviewed this? Are there any "unknown unknowns" hiding here? What's the rollback plan if this goes wrong?

---

### 6. Design Considerations

| Score | Criteria |
|-------|----------|
| 0 | No design considerations |
| 1 | Brief mention of UX but no edge cases or error states |
| 2 | UX principles stated, some edge cases identified, but error states incomplete |
| 3 | Clear UX principles for this feature, comprehensive edge cases with expected behavior, error states with user-facing messages and recovery paths |

**Key questions:** What happens when things go wrong? What does the empty state look like? What about users with 10x or 100x the normal data volume?

---

### 7. Launch Plan

| Score | Criteria |
|-------|----------|
| 0 | No launch plan |
| 1 | Vague plan ("we'll roll it out gradually") with no specifics |
| 2 | Staged rollout defined but missing launch checklist or communication plan |
| 3 | Clear rollout phases with audience, duration, and success criteria for each phase; comprehensive launch checklist (analytics, feature flags, docs, support briefing); communication plan by audience |

**Key questions:** Is analytics instrumentation on the checklist? Will the support team know this is coming? What has to be true before we go from beta to GA?

---

### 8. Timeline

| Score | Criteria |
|-------|----------|
| 0 | No timeline |
| 1 | Single target date with no milestones |
| 2 | Milestones with dates and owners, but dependencies not mapped |
| 3 | Milestones with dates, owners, and dependencies identified with impact-if-delayed analysis; includes post-launch success review date |

**Key questions:** Are there dependencies that could block us? Who owns each milestone? When will we evaluate whether this actually worked?

---

### 9. Risks & Mitigations

| Score | Criteria |
|-------|----------|
| 0 | No risks identified |
| 1 | Risks listed but no categorization, likelihood assessment, or mitigations |
| 2 | Risks categorized with likelihood and impact, but mitigations are vague |
| 3 | Risks categorized (product/tech/market/ops) with likelihood, impact, specific mitigation plans, and owners assigned |

**Key questions:** Are we being honest about what could go wrong? Do the mitigations actually reduce risk, or are they just restating the risk as a plan? Is someone accountable for each risk?

---

### 10. Open Questions

| Score | Criteria |
|-------|----------|
| 0 | No open questions section (suspicious — there are always open questions) |
| 1 | Questions listed but no owners or due dates |
| 2 | Questions with owners and due dates, but some are stale or already answerable |
| 3 | Active, relevant questions with owners, due dates, and resolutions tracked as they're answered |

**Key questions:** Are these genuine unknowns, or are they decisions the PM is avoiding? Will these be resolved before development starts?

---

## Pass/Fail Criteria

**A PRD cannot be approved without all of the following:**

1. **Clear problem statement** — Specific, evidence-backed, with identified personas (Section 1 score ≥ 2)
2. **Measurable goals** — At least one primary metric with a baseline and target (Section 2 score ≥ 2)
3. **P0 requirements with acceptance criteria** — Every launch-blocking requirement has testable criteria (Section 4 score ≥ 2)
4. **Success metrics with targets** — Defined metrics, measurement method, and evaluation timeline (Section 2 score ≥ 2)
5. **Timeline with milestones** — At least key milestones with dates and owners (Section 8 score ≥ 2)
6. **Risk assessment** — At least major risks identified with mitigations (Section 9 score ≥ 1)

If any of these fail, the PRD needs revision before it moves to development.

---

## How to Use This Rubric

**Don't** hand the PM a filled-in scorecard. Instead:

1. Read the PRD with this rubric in mind
2. Identify the biggest gaps — what's missing or weak that would actually cause problems?
3. Write feedback as prose: lead with the most critical issue, explain why it matters, and suggest what "good" looks like
4. Call out what's strong — PMs need to know what's working so they keep doing it
5. End with a clear verdict: approved, needs minor revisions (list them), or needs significant rework (explain what)

**Example feedback:**

> This PRD has a solid problem statement and the requirements are well-structured — you've clearly done the customer research. The main gap is measurement: there are no success metrics defined, which means we won't know if this worked after launch. Before this goes to eng, you need to define at least a primary metric with a current baseline and a target. I'd also add guardrail metrics for page load time since this touches the core workflow. The timeline section needs milestones — right now it's just a target launch date with no checkpoints in between.
>
> **Verdict:** Needs minor revisions. Add success metrics and timeline milestones, then this is ready.

---

*This rubric is a thinking tool. The value is in the critical thinking it prompts, not in the scores themselves.*
