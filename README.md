# Claude Code Skills

A collection of Claude Code skills, packaged as a plugin.

## Skills

| Skill | Description |
|-------|-------------|
| [copywriting](./skills/copywriting/) | Persuasive copy for SaaS landing pages, emails, ads, and sales pages — headlines, CTAs, product descriptions, and marketing copy that drives action. |
| [pm-career-coach](./skills/pm-career-coach/) | PM career coach for resume reviews, career direction, and transitions into PM. Frameworks from Shreyas Doshi, Lenny Rachitsky, Jackie Bavaro, Ken Norton, Aakash Gupta, and Sachin Rekhi. |
| [pm-career-interview](./skills/pm-career-interview/) | PM interview drill partner. ~500 questions (behavioral, product design, strategy, metrics, technical, leadership) from Aakash Gupta's cheat sheets, with CIRCLES / AARM / DIGS / Fermi frameworks and worked examples. |
| [product-management](./skills/product-management/) | Product management skill for reviewing PRDs, specs, feature planning, and prioritization — inspired by [Eno Reyes](https://x.com/EnoReyes) (co-founder of [FactoryAI](https://factory.ai/)), who demoed his PM skill in [this video](https://www.youtube.com/watch?v=j7CaMx2c56M) on the [Behind the Craft](https://www.youtube.com/@PeterYangYT) channel by [Peter Yang](https://x.com/petergyang). |

## Usage

**Option A — install as a plugin (all skills at once):**

```bash
# From the Claude Code prompt
/plugin install <path-to-this-repo>
```

**Option B — copy a single skill:**

Personal (all projects):

```bash
cp -r skills/pm-career-interview ~/.claude/skills/pm-career-interview
```

Project-scoped (shared with team via git):

```bash
cp -r skills/pm-career-interview .claude/skills/pm-career-interview
```

Claude Code discovers skills automatically from both locations — no plugin installation needed if you prefer the copy approach.

## Skill Structure

Each skill follows this convention:

```
<skill-name>/
├── SKILL.md        # The skill file (required). YAML frontmatter with name and description, followed by skill content.
├── templates/      # Supporting templates and reference docs (optional)
└── examples/       # Real-world configuration examples (optional)
```

## Contributing

1. Create a subfolder under `skills/` named after your skill
2. Add a `SKILL.md` with frontmatter: `name` and `description`
3. Add supporting files (templates, examples) as needed
4. Add your skill to the table above
5. Open a PR

## License

MIT
