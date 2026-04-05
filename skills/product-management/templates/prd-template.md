# PRD Template

Use this template when writing Product Requirements Documents. Fill in each section — if a section isn't applicable, explicitly state why rather than deleting it.

---

## [Feature/Initiative Name]

**Author:** [PM Name]
**Status:** Draft / In Review / Approved / In Development
**Last Updated:** [Date]
**Pod:** [Owning pod]
**Target Cycle:** [Cycle number or date range]

---

## 1. Problem Statement

### What problem are we solving?

[2-3 sentences describing the problem from the customer's perspective. Be specific about who has this problem and what impact it has on them.]

### Who has this problem?

| Persona | Description | Severity |
|---------|-------------|----------|
| [Primary persona] | [Brief description and how they encounter this problem] | [Critical / High / Medium] |
| [Secondary persona] | [Brief description] | [Critical / High / Medium] |

### Evidence

What evidence do we have that this problem is real and worth solving?

- **Quantitative:** [Usage data, support ticket volume, funnel drop-off, etc.]
- **Qualitative:** [Customer quotes from interviews, sales call themes, NPS feedback]
- **Market:** [Competitive dynamics, industry trends, analyst reports]

### What happens if we don't solve this?

[Describe the consequences of inaction — customer churn risk, competitive disadvantage, revenue impact, etc.]

---

## 2. Goals and Success Metrics

### Goals

| Goal | Description | How We'll Measure |
|------|-------------|-------------------|
| **Primary goal** | [The #1 thing this initiative must achieve] | [Specific metric + target] |
| **Secondary goal** | [Additional value we expect to create] | [Specific metric + target] |

### Success Metrics

| Metric | Current Baseline | Target | Measurement Method | Timeline |
|--------|-----------------|--------|--------------------|----------|
| [Primary metric] | [Current value] | [Target value] | [How we'll measure] | [When we'll evaluate] |
| [Secondary metric] | [Current value] | [Target value] | [How we'll measure] | [When we'll evaluate] |
| [Guardrail metric] | [Current value] | [Must not go below X] | [How we'll measure] | [Ongoing] |

**Guardrail metrics** are things that must NOT get worse as a result of this change. For example, if we're optimizing for activation, page load time is a guardrail.

### What does "done" look like?

[1-2 sentences describing the concrete outcome that lets us say "this initiative was successful."]

---

## 3. Solution Overview

### Proposed Approach

[2-4 paragraphs describing the solution at a high level. Focus on the user experience — what changes for the customer? How does their workflow improve?]

### Key User Flows

**Flow 1: [Name — e.g., "First-time setup"]**
1. User does [action]
2. System responds with [response]
3. User sees [outcome]
4. ...

**Flow 2: [Name — e.g., "Daily usage"]**
1. User does [action]
2. ...

### Wireframes / Mocks

[Link to Figma, screenshots, or embedded images. Low-fidelity is fine at the PRD stage — the goal is to communicate intent, not pixel-perfect design.]

### Alternatives Considered

| Option | Pros | Cons | Why Not |
|--------|------|------|---------|
| **Option A (Chosen)** | [Advantages] | [Drawbacks] | — |
| **Option B** | [Advantages] | [Drawbacks] | [Why we didn't choose this] |
| **Option C** | [Advantages] | [Drawbacks] | [Why we didn't choose this] |
| **Do Nothing** | [No investment cost] | [Continued pain] | [Why inaction isn't acceptable] |

---

## 4. Requirements

### P0 — Must Have (Launch blockers)

These are non-negotiable for the initial release. The feature does NOT ship without these.

| # | Requirement | Acceptance Criteria |
|---|------------|-------------------|
| P0-1 | [Requirement description] | [Specific, testable criteria for "done"] |
| P0-2 | [Requirement description] | [Specific, testable criteria] |
| P0-3 | [Requirement description] | [Specific, testable criteria] |

### P1 — Should Have (High value, not blocking launch)

We strongly want these in v1 but will launch without them if necessary.

| # | Requirement | Acceptance Criteria |
|---|------------|-------------------|
| P1-1 | [Requirement description] | [Specific, testable criteria] |
| P1-2 | [Requirement description] | [Specific, testable criteria] |

### P2 — Nice to Have (Fast follow)

Planned for the iteration immediately after launch.

| # | Requirement | Acceptance Criteria |
|---|------------|-------------------|
| P2-1 | [Requirement description] | [Specific, testable criteria] |
| P2-2 | [Requirement description] | [Specific, testable criteria] |

### Explicitly Out of Scope

Just as important as what's in scope. List things that are intentionally NOT included and why.

- **[Thing we're not doing]** — [Why: e.g., "Low impact relative to effort" or "Planned for Phase 2"]
- **[Another thing we're not doing]** — [Why]

---

## 5. Technical Considerations

### Architecture Notes

[High-level technical approach. This isn't a tech spec — it's context for the PM and designer to understand constraints and trade-offs.]

- **Data model changes:** [Any new tables, fields, or relationships?]
- **API changes:** [New endpoints? Breaking changes?]
- **Third-party dependencies:** [External services, APIs, or libraries?]
- **Performance considerations:** [Scale expectations, latency requirements]

### Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| [Risk 1] | [High/Med/Low] | [High/Med/Low] | [What we'll do about it] |
| [Risk 2] | [High/Med/Low] | [High/Med/Low] | [What we'll do about it] |

### Migration / Backward Compatibility

[Does this require data migration? Will it break existing integrations or workflows? What's the rollback plan?]

---

## 6. Design Considerations

### UX Principles for This Feature

[Any specific UX goals or constraints — e.g., "Must work on mobile," "Should require zero configuration," "Must be accessible to screen readers"]

### Edge Cases

| Scenario | Expected Behavior |
|----------|------------------|
| [Edge case 1 — e.g., "User has no data yet"] | [What should happen] |
| [Edge case 2 — e.g., "User loses connection mid-flow"] | [What should happen] |
| [Edge case 3 — e.g., "User has 10,000+ items"] | [What should happen] |

### Error States

| Error | User-Facing Message | Recovery Path |
|-------|-------------------|---------------|
| [Error type 1] | [What the user sees] | [How they fix it] |
| [Error type 2] | [What the user sees] | [How they fix it] |

---

## 7. Launch Plan

### Rollout Strategy

| Phase | Audience | Duration | Success Criteria for Next Phase |
|-------|----------|----------|-------------------------------|
| **Internal dogfooding** | Team | 1 week | No P0 bugs, core flows work |
| **Beta** | [X friendly customers] | 1-2 weeks | Positive feedback, no major issues |
| **% Rollout** | [X]% of users | 1 week | Metrics trending positively |
| **GA** | All users | — | — |

### Launch Checklist

- [ ] Analytics instrumentation verified
- [ ] Feature flags configured
- [ ] Documentation updated (help center, API docs)
- [ ] Support team briefed and FAQ prepared
- [ ] Marketing notified (if customer-facing change)
- [ ] Rollback plan tested
- [ ] Performance benchmarks met
- [ ] Accessibility review completed

### Communication Plan

| Audience | Channel | Message | Timing |
|----------|---------|---------|--------|
| Internal team | [Slack/Email] | [What and why] | [Before launch] |
| Customer support | [Training session] | [How it works, common questions] | [Before launch] |
| Customers | [In-app/Email/Changelog] | [What's new and why it matters] | [At launch] |

---

## 8. Timeline

| Milestone | Target Date | Owner |
|-----------|------------|-------|
| PRD approved | [Date] | PM |
| Design complete | [Date] | Designer |
| Development starts | [Date] | Eng Lead |
| Internal alpha | [Date] | Eng Lead |
| Beta launch | [Date] | PM |
| GA launch | [Date] | PM |
| Success review (4 weeks post-launch) | [Date] | PM |

### Dependencies

| Dependency | Owner | Status | Impact if Delayed |
|------------|-------|--------|-------------------|
| [Dependency 1] | [Team/Person] | [On track / At risk / Blocked] | [What happens] |
| [Dependency 2] | [Team/Person] | [Status] | [Impact] |

---

## 9. Risks and Mitigations

| Risk | Category | Likelihood | Impact | Mitigation | Owner |
|------|----------|-----------|--------|------------|-------|
| [Risk 1] | Product / Tech / Market / Ops | H/M/L | H/M/L | [Plan] | [Who] |
| [Risk 2] | Product / Tech / Market / Ops | H/M/L | H/M/L | [Plan] | [Who] |

---

## 10. Open Questions

| # | Question | Owner | Due Date | Resolution |
|---|---------|-------|----------|------------|
| 1 | [Question that needs to be answered before/during development] | [Who] | [When] | [Answer once resolved] |
| 2 | [Another open question] | [Who] | [When] | [Pending] |

---

## Appendix

### Customer Quotes

> "[Relevant quote from customer interview]" — [Customer type/role], [Date]

> "[Another quote]" — [Customer type/role], [Date]

### Related Documents

- [Link to design file]
- [Link to technical spec]
- [Link to competitive analysis]
- [Link to customer research summary]

### Changelog

| Date | Author | Change |
|------|--------|--------|
| [Date] | [Name] | Initial draft |
| [Date] | [Name] | [What changed and why] |

---

*Reminder: A PRD is a communication tool, not a legal document. Its job is to align the team on what we're building, why, and how we'll know if it worked. Iterate on it as you learn more — a PRD that never changes after approval is a PRD that's being ignored.*
