# Claude Code Skills

A collection of skills for Claude Code — reusable prompt-driven workflows you can add to your projects.

## Skills

| Skill | Description |
|-------|-------------|
| [product-management](./product-management/) | Product management assistant for PRDs, specs, feature planning, and prioritization |

## Usage

**For all your projects (personal):**

```bash
# Copy a skill folder into your personal skills directory
cp -r product-management ~/.claude/skills/product-management
```

**For a specific project (shared with team via git):**

```bash
# Copy into the project's .claude/skills directory
cp -r product-management .claude/skills/product-management
```

Claude Code discovers skills automatically from both locations — no plugin installation needed. Customize the templates and configuration to match your team's workflow.

## Skill Structure

Each skill follows this convention:

```
<skill-name>/
├── SKILL.md        # The skill file (required). YAML frontmatter with name and description, followed by skill content.
├── templates/      # Supporting templates and reference docs (optional)
└── examples/       # Real-world configuration examples (optional)
```

## Contributing

1. Create a subfolder named after your skill
2. Add a `SKILL.md` with frontmatter: `name` and `description`
3. Add supporting files (templates, examples) as needed
4. Add your skill to the table above
5. Open a PR

## Acknowledgments

The **product-management** skill was inspired by [Eno Reyes](https://x.com/EnoReyes) (co-founder of [Factory](https://factory.ai/)), who demoed his PM skill in [this video](https://www.youtube.com/watch?v=j7CaMx2c56M) on the [Behind the Craft](https://www.youtube.com/@BehindTheCraft) channel by [Peter Yang](https://x.com/petergyang).

## License

MIT
