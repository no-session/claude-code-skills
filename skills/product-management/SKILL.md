---
name: product-management
description: "Use when working on PRDs, product specs, design docs, feature planning, prioritization, or product strategy."
---

# Skill: Product Management

## Purpose

Assist with product management work by providing access to your team's foundational product documents, frameworks, and team context. This skill points you to the source of truth documents that should guide all product work.

## When to use this skill

- Writing or reviewing PRDs and product specs
- Working on design documents
- Discussing feature prioritization
- Planning product work
- Understanding team ownership and pod structure
- Referencing product principles or positioning

## Getting Started

- The `templates/` folder contains starter frameworks for each document type
- Customize the templates with your company's context
- Replace `[YOUR_LINK_HERE]` placeholders below with URLs to your own docs (Notion, Confluence, Google Docs, etc.)
- If no external links are configured, the bundled templates serve as defaults

## Source of Truth Documents

**IMPORTANT**: Always fetch these documents to get the latest content. These are the authoritative sources for your team's product approach.

### Core Product Philosophy

1. **Product Principles** — Our foundational beliefs about how we build product
   [YOUR_LINK_HERE]
   Template: templates/product-principles.md

2. **Core Value Proposition** — What we uniquely offer
   [YOUR_LINK_HERE]
   Template: templates/core-value-proposition.md

3. **11-Star Experience** — Our vision for the ideal user experience
   [YOUR_LINK_HERE]
   Template: templates/11-star-experience.md

4. **Product Positioning** — How we position ourselves in the market
   [YOUR_LINK_HERE]
   Template: templates/product-positioning.md

### How We Work

5. **How We Build** — Our approach to building product
   [YOUR_LINK_HERE]
   Template: templates/how-we-build.md

6. **Prioritization Framework** — How we decide what to build
   [YOUR_LINK_HERE]
   Template: templates/prioritization-framework.md

7. **Product Research Bets** — Our current research areas and bets
   [YOUR_LINK_HERE]
   Template: templates/product-research-bets.md

### Templates & Current Plans

8. **PRD Template** — Use this template when writing PRDs
   [YOUR_LINK_HERE]
   Template: templates/prd-template.md

9. **Quarterly Plan** — Current quarterly product plan with ownership areas, pods, and team members
   [YOUR_LINK_HERE]
   Template: templates/quarterly-plan.md

## Required Behavior

1. **Fetch from your configured document sources**: When working on product documents, fetch the relevant documents from your configured sources above, or reference the bundled templates. These are the source of truth and may be updated.

2. **Reference principles**: Ensure product work aligns with your Product Principles and Core Value Proposition.

3. **Use the PRD template**: When creating PRDs, follow the structure in the PRD Template doc.

4. **Check ownership**: Reference your quarterly plan to understand ownership and team structure when relevant.

5. **Stay current**: Your quarterly plan and research bets change frequently — always fetch fresh content rather than relying on cached knowledge.

## Workflow

When asked to help with product work:

1. Identify which source documents are relevant to the task
2. Fetch documents from your configured sources, or reference the bundled templates
3. Apply the context from those documents to the work at hand
4. For PRDs, follow the PRD Template structure
5. For prioritization discussions, apply the Prioritization Framework
6. For team/ownership questions, reference the quarterly plan

## PRD Reviews

When reviewing a PRD, use the rubric in `templates/prd-review-rubric.md` (co-located with this skill). The rubric:

- Scores each section against your PRD template (0-3 scale)
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
| Goals   | 1     | Missing |
| Metrics | 0     | Missing |

**Good example:**

"The biggest gap here is that there's no way to know if this ships successfully. You've got clear context on *why* we're doing this, but no success metrics or timeline. Before this goes to eng, you need to answer: what does 'good' look like for ACP adoption, and by when?"

When using the PRD rubric, internalize the checklist but communicate findings as narrative feedback that the PM can act on and share with stakeholders.

## Notes

This skill is intentionally not prescriptive about specific styles or formats beyond pointing to the source documents. Your configured docs (or bundled templates) contain the detailed guidance — this skill ensures your coding agent knows where to look.
