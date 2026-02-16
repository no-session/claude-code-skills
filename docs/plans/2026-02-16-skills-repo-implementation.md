# Claude Code Skills Repo — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Scaffold the claude-code-skills repo with the product-management skill, templates, Factory example, and root README.

**Architecture:** Flat repo with one folder per skill. Each skill has a SKILL.md and optional supporting files. Root README catalogs all skills.

**Tech Stack:** Markdown only. No build tools or dependencies.

**Source files location:** `/Users/pawankumar/Library/Application Support/Claude/local-agent-mode-sessions/fe15c4e0-128b-4e40-a564-71eac2581ef2/8e1ddef0-4e24-4c54-aa09-b6d746585d22/local_06b982ea-186d-4a26-b2bf-c8e633246c12/outputs/`

---

### Task 1: Create directory structure

**Files:**
- Create: `product-management/templates/` (directory)
- Create: `product-management/examples/factory/` (directory)

**Step 1: Create the directories**

```bash
mkdir -p product-management/templates product-management/examples/factory
```

**Step 2: Verify**

```bash
ls -R product-management/
```

Expected: `templates/` and `examples/factory/` directories exist.

---

### Task 2: Copy template files

Copy the 9 template files from source, renaming to drop numeric prefixes.

**Files:**
- Create: `product-management/templates/product-principles.md` (from `01-product-principles.md`)
- Create: `product-management/templates/core-value-proposition.md` (from `02-core-value-proposition.md`)
- Create: `product-management/templates/11-star-experience.md` (from `03-11-star-experience.md`)
- Create: `product-management/templates/product-positioning.md` (from `04-product-positioning.md`)
- Create: `product-management/templates/how-we-build.md` (from `05-how-we-build.md`)
- Create: `product-management/templates/prioritization-framework.md` (from `06-prioritization-framework.md`)
- Create: `product-management/templates/product-research-bets.md` (from `07-product-research-bets.md`)
- Create: `product-management/templates/prd-template.md` (from `08-prd-template.md`)
- Create: `product-management/templates/quarterly-plan.md` (from `09-quarterly-plan.md`)
- Create: `product-management/templates/prd-review-rubric.md` (from `prd-review-rubric.md`)

**Step 1: Copy files with renamed paths**

Read each source file and write it to the target path with the new name. No content changes — these templates are already generic.

**Step 2: Verify**

```bash
ls product-management/templates/
```

Expected: 10 files listed.

**Step 3: Commit**

```bash
git add product-management/templates/
git commit -m "feat: add product management templates and rubric"
```

---

### Task 3: Create the generic SKILL.md

**Files:**
- Create: `product-management/SKILL.md`

**Step 1: Write the generic SKILL.md**

Derive from the Factory original (`product-management-SKILL.md` in source) with these changes:

1. **Frontmatter:** Replace with:
   ```yaml
   ---
   name: product-management
   description: "Product Management Assistant. Use when working on PRDs, product specs, feature planning, prioritization, or any PM-related work."
   ---
   ```

2. **Title:** Change from "Factory Product Management" to "Product Management"

3. **Purpose:** Replace Factory-specific text with generic: "Assist with product management work by providing access to foundational product documents, frameworks, and team context."

4. **Add "Getting Started" section** after Purpose:
   - Explains the templates in `templates/` are starter frameworks
   - Instructs users to customize templates with their company context
   - Instructs users to replace `[YOUR_LINK_HERE]` placeholders with their own doc URLs (Notion, Confluence, Google Docs, etc.)
   - Notes that if no external links are configured, the bundled templates serve as defaults

5. **Source of Truth Documents:** Replace each Notion URL with `[YOUR_LINK_HERE]` placeholder. Add a note under each that the bundled template in `templates/<filename>.md` can be used as a starting point.

6. **Required Behavior:** Change "Fetch from Notion" to "Fetch from your configured document sources" and generalize all Factory references.

7. **Workflow:** Replace "Fetch those Notion documents using FetchUrl" with "Fetch documents from your configured sources, or reference the bundled templates"

8. **PRD Reviews:** Update rubric path from `prd-review-rubric.md` to `templates/prd-review-rubric.md`

9. **Notes:** Remove "Droid" reference, generalize to "your coding agent"

10. **Preserve as-is:** "When to use this skill", "Language Guidance", "PRD Reviews" pass/fail criteria — these are already generic.

**Step 2: Verify**

- Confirm no Factory-specific references remain
- Confirm no Notion URLs remain (all replaced with placeholders)
- Confirm rubric path points to `templates/prd-review-rubric.md`

**Step 3: Commit**

```bash
git add product-management/SKILL.md
git commit -m "feat: add generic product management skill"
```

---

### Task 4: Create the Factory example SKILL.md

**Files:**
- Create: `product-management/examples/factory/SKILL.md`

**Step 1: Write the Factory example**

Copy the original `product-management-SKILL.md` with two changes:

1. **PRD Reviews section:** Update rubric path from `prd-review-rubric.md` to `../../templates/prd-review-rubric.md`
2. **Add a note at the top** (after frontmatter, before the title): a brief comment explaining this is an example showing how Factory configured the generic skill with their Notion docs.

Everything else stays exactly as-is — Notion URLs, Factory branding, "Droid" references.

**Step 2: Verify**

- Confirm Notion URLs are preserved
- Confirm rubric path is `../../templates/prd-review-rubric.md`

**Step 3: Commit**

```bash
git add product-management/examples/factory/SKILL.md
git commit -m "feat: add Factory example for product management skill"
```

---

### Task 5: Create root README.md

**Files:**
- Create: `README.md`

**Step 1: Write the README**

Structure:

```markdown
# Claude Code Skills

A collection of skills for Claude Code — reusable prompt-driven workflows you can add to your projects.

## Skills

| Skill | Description |
|-------|-------------|
| [product-management](./product-management/) | Product management assistant for PRDs, specs, feature planning, and prioritization |

## Usage

[Brief instructions on how to use a skill in Claude Code — copy the skill folder to your project, or reference it in your Claude Code settings]

## Skill Structure

Each skill follows this convention:

- `<skill-name>/SKILL.md` — The skill file (required). Contains YAML frontmatter with `name` and `description`, followed by the skill content.
- `<skill-name>/templates/` — Supporting templates and reference docs (optional)
- `<skill-name>/examples/` — Real-world configuration examples (optional)

## Contributing

1. Create a subfolder named after your skill
2. Add a `SKILL.md` with frontmatter: `name` and `description`
3. Add supporting files (templates, examples) as needed
4. Add your skill to the table above
5. Open a PR

## License

MIT
```

**Step 2: Verify**

- Link to product-management folder resolves
- Table renders correctly in markdown preview

**Step 3: Commit**

```bash
git add README.md
git commit -m "feat: add root README with skills catalog"
```

---

### Task 6: Add LICENSE file

**Files:**
- Create: `LICENSE`

**Step 1: Write MIT license**

Standard MIT license text with copyright holder as the user.

**Step 2: Commit**

```bash
git add LICENSE
git commit -m "chore: add MIT license"
```

---

### Task 7: Final verification

**Step 1: Verify repo structure**

```bash
find . -not -path './.git/*' -not -path './.git' | sort
```

Expected output should match the design doc structure.

**Step 2: Verify all files committed**

```bash
git status
```

Expected: clean working tree.

**Step 3: Review git log**

```bash
git log --oneline
```

Expected: 6 commits (design doc + tasks 2-6).
