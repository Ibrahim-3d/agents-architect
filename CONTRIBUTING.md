# Contributing to agents-architect

Thanks for the interest. agents-architect is a meta-plugin — it builds other plugins — so the contribution bar is a little different from a normal library.

## Before you open a PR

1. `python3 scripts/validate.py .` passes with zero errors (warnings about template placeholders are expected).
2. Every JSON manifest parses.
3. Every new SKILL.md has both **positive** and **negative** trigger examples.
4. Every new agent declares `tools` and avoids `hooks`, `mcpServers`, `permissionMode`.
5. Every new command uses `$ARGUMENTS` and `@`-imports heavy context.

## Adding a new authoring skill

The fastest way: run it through itself.

```
/agents-architect:skill my-new-authoring-skill
```

Then hand-edit and iterate.

## Adding a new sub-agent

Pattern:

```yaml
---
name: arch-<role>
description: One sentence. What this agent does, when to route to it.
tools: [Read, Write, Edit, Bash]
---

You are the <role>. Your sole output artifact is `<path>`. You never…

<workflow>
1. …
</workflow>

<red_lines>
- …
</red_lines>
```

Keep each agent to a single artifact contract. If you need two outputs, split into two agents.

## Style

- Prefer prose over bullets inside agent bodies and skill references.
- Reference files rather than inlining large content.
- Kebab-case names everywhere (agents, skills, commands, plugin name).

## Running locally

```
git clone https://github.com/Ibrahim-3d/agents-architect
cd agents-architect
python3 scripts/validate.py .
```

Install it as a local plugin:

```
ln -s "$(pwd)" ~/.claude/plugins/agents-architect
```

## Release process

1. Bump `version` in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.
2. Update `CHANGELOG.md`.
3. `git tag vX.Y.Z && git push --tags`
4. GitHub release action (if configured) will attach a tarball.

## Questions

Open a discussion or ping in your issue.
