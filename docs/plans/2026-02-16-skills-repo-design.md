# Claude Code Skills Repo — Design Doc

**Date:** 2026-02-16
**Status:** Approved

## Goal

Create a public repo for sharing Claude Code skills. Each skill lives in its own subfolder. A root README provides a catalog of all skills. The first skill is a Product Management assistant.

## Repo Structure

```
claude-code-skills/
├── README.md                          # Project overview + skills catalog
├── product-management/
│   ├── SKILL.md                       # Generic, configurable PM skill
│   ├── templates/
│   │   ├── product-principles.md
│   │   ├── core-value-proposition.md
│   │   ├── 11-star-experience.md
│   │   ├── product-positioning.md
│   │   ├── how-we-build.md
│   │   ├── prioritization-framework.md
│   │   ├── product-research-bets.md
│   │   ├── prd-template.md
│   │   ├── prd-review-rubric.md
│   │   └── quarterly-plan.md
│   └── examples/
│       └── factory/
│           └── SKILL.md               # Real-world example with Notion URLs
```

## Root README

- Project title and one-liner
- Skills catalog table (name, description, link to folder)
- How to use a skill in Claude Code
- Contributing guide (folder structure convention, SKILL.md format)
- License (MIT)

## Generic SKILL.md

Derived from the Factory-specific original with these changes:

1. **Configuration block** at the top — users fill in their own doc links (Notion, Confluence, Google Docs, etc.) as placeholders `[YOUR_LINK_HERE]`
2. **"Getting Started" section** — copy templates, fill in company context, update doc links
3. **Generic language** — "your company/team" instead of "Factory"
4. **Template defaults** — if no external link provided, the bundled templates in `templates/` serve as the starting point
5. **Updated rubric path** — references `templates/prd-review-rubric.md`
6. **Everything else preserved** — workflow, required behavior, language guidance, PRD review sections are already generic

Frontmatter:

```yaml
---
name: product-management
description: "Product Management Assistant. Use when working on PRDs, product specs, feature planning, prioritization, or any PM-related work."
---
```

## Templates

The 9 content files from the original skill, renamed without numeric prefixes. These are generic frameworks/templates — not company-specific. Users customize them with their own company context.

The `prd-review-rubric.md` also lives in templates since it's a reference doc like the others.

## Factory Example

The original SKILL.md with Factory's Notion URLs preserved. Serves as a concrete reference for how a real company configured the skill. References shared templates via `../templates/` path to avoid duplication.

## Distribution

GitHub repo initially. Plugin registry listing planned for later.

## Audience

Public/open-source — READMEs and docs written for people unfamiliar with these skills.

## Adding Future Skills

Each new skill follows the same pattern:
1. Create a subfolder named after the skill
2. Add a `SKILL.md` with standard frontmatter (`name`, `description`)
3. Add supporting files (templates, examples) as needed
4. Add an entry to the root README skills catalog table
