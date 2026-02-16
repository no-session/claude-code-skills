---
description: Product Management Assistant . Use when working on design docs, PRDs, product specs, feature planning, prioritization, or any PM-related work. Provides context on Factory's product principles, positioning, and team structure.
---

> **Note:** This is an example showing how Factory configured the [generic product-management skill](../../SKILL.md) with their company's Notion documents. Use this as a reference for how to customize the skill for your own organization.

# Skill: Factory Product Management

## Purpose

Assist with product management work at Factory by providing access to our foundational product documents, frameworks, and team context. This skill points you to the source of truth documents that should guide all product work.

## When to use this skill

- Writing or reviewing PRDs and product specs
- Working on design documents
- Discussing feature prioritization
- Planning product work
- Understanding team ownership and pod structure
- Referencing product principles or positioning

## Source of Truth Documents

**IMPORTANT**: Always fetch these Notion documents to get the latest content. These are the authoritative sources for Factory's product approach.

### Core Product Philosophy

1. **Product Principles** — Our foundational beliefs about how we build product
   https://www.notion.so/309cd0f922e881f48253f1914812c501

2. **Core Value Proposition** — What we uniquely offer
   https://www.notion.so/309cd0f922e8812795a0fd8e9e3d6b28

3. **11-Star Experience** — Our vision for the ideal user experience
   https://www.notion.so/309cd0f922e881aa8c0ee8df7752abe8

4. **Product Positioning** — How we position ourselves in the market
   https://www.notion.so/309cd0f922e881ca8415d7739f481335

### How We Work

5. **How We Build** — Our approach to building product
   https://www.notion.so/309cd0f922e881148107ca925ce76709

6. **Prioritization Framework** — How we decide what to build
   https://www.notion.so/309cd0f922e881919011cf9dd5d06e66

7. **Product Research Bets** — Our current research areas and bets
   https://www.notion.so/309cd0f922e881939402cb359c3360d3

### Templates & Current Plans

8. **PRD Template** — Use this template when writing PRDs
   https://www.notion.so/309cd0f922e8817f812cc2fba8261095

9. **Quarterly Plan** — Current quarterly product plan with ownership areas, pods, and team members
   https://www.notion.so/309cd0f922e881868607f00a0d51daad

## Required Behavior

1. **Fetch from Notion**: When working on product documents, use FetchUrl to pull the relevant Notion docs above. These are the source of truth and may be updated.

2. **Reference principles**: Ensure product work aligns with our Product Principles and Core Value Proposition.

3. **Use the PRD template**: When creating PRDs, follow the structure in the PRD Template doc.

4. **Check ownership**: Reference the quarterly plan to understand pod ownership and team structure when relevant.

5. **Stay current**: The quarterly plan and research bets change frequently — always fetch fresh content rather than relying on cached knowledge.

## Workflow

When asked to help with product work:

1. Identify which source documents are relevant to the task
2. Fetch those Notion documents using FetchUrl
3. Apply the context from those documents to the work at hand
4. For PRDs, follow the PRD Template structure
5. For prioritization discussions, apply the Prioritization Framework
6. For team/ownership questions, reference the quarterly plan

## PRD Reviews

When reviewing a PRD, use the rubric in `../../templates/prd-review-rubric.md` (co-located with this skill). The rubric:

- Scores each section against our PRD template (0-3 scale)
- Identifies critical gaps that block approval
- Provides a structured output format

**Quick pass/fail criteria** — a PRD cannot be approved without:

- Clear problem statement
- Measurable goals
- P0 requirements with acceptance criteria
- Success metrics with targets
- Timeline with milestones
- Risk assessment

## Language Guidance

**Prefer prose over heavy markdown.** Product work is ultimately about communicating with humans — PMs, engineers, leadership. Your output should be readable and shareable, not a wall of tables and checklists.

Guidelines:

- Write in narrative form that flows naturally and could be copy-pasted into a Slack message or email
- Use **bold** and *emphasis* to highlight key points, but sparingly
- Headers are fine for organizing longer responses, but don't over-structure short feedback
- Don't use the pattern "**Label:** wall of text" — it's stilted. Just write naturally and let bold phrases emerge organically within sentences, or use a header with a line break before the paragraph.
- Avoid excessive tables — use them only when comparing multiple items or when structure genuinely aids comprehension
- Bullet points are okay for lists, but prefer a sentence that synthesizes over a bullet dump
- Lead with the "so what" — what's the actionable takeaway?
- Be direct and opinionated; don't hedge excessively

**Bad example:**

| Section | Score | Status |
|---------|-------|--------|
| Goals | 1 | Missing |
| Metrics | 0 | Missing |

**Good example:**

"The biggest gap here is that there's no way to know if this ships successfully. You've got clear context on *why* we're doing this, but no success metrics or timeline. Before this goes to eng, you need to answer: what does 'good' look like for ACP adoption, and by when?"

When using the PRD rubric, internalize the checklist but communicate findings as narrative feedback that the PM can act on and share with stakeholders.

## Notes

This skill is intentionally not prescriptive about specific styles or formats beyond pointing to the source documents. The Notion docs themselves contain the detailed guidance — this skill ensures Droid knows where to look.
