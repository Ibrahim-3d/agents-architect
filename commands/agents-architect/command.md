---
name: agents-architect:command
description: Author a single slash command from a brief. Use to extend an existing plugin with a new /command.
argument-hint: "<ns:name> \"<objective>\" [--plugin <path>] [--args <schema>] [--spawns <agent1,agent2>]"
allowed-tools:
  - Read
  - Write
  - Task
  - AskUserQuestion
---

<objective>
Fast path to a single slash command file with correct frontmatter, @-imports, and orchestration body.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/agents-architect/templates/command.template.md
</execution_context>

<context>
Arguments: $ARGUMENTS
</context>

<process>
1. Parse args. Infer namespace from plugin dir if missing.
2. `AskUserQuestion` to fill: gates (what needs user confirmation), outputs (files written), idempotency rules.
3. Spawn `agents-architect-command-author`. It writes `commands/<ns>/<name>.md`.
4. Report back.
</process>

<output>
Command path + allowed-tools + 5-line summary.
</output>
