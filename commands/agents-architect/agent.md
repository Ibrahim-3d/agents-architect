---
name: agents-architect:agent
description: Author a single sub-agent from a short brief. Use to add a specialist to an existing plugin.
argument-hint: "<agent-name> \"<role>\" [--plugin <path>] [--tools <csv>] [--model <name>]"
allowed-tools:
  - Read
  - Write
  - Task
  - AskUserQuestion
---

<objective>
Fast path to a single sub-agent file with correct frontmatter + XML-tagged body.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/agents-architect/references/agent-tool-allowlists.md
@${CLAUDE_PLUGIN_ROOT}/agents-architect/templates/agent.template.md
</execution_context>

<context>
Arguments: $ARGUMENTS
</context>

<process>
1. Parse args.
2. `AskUserQuestion` to fill: artifact produced, upstream files read, downstream consumers, whether isolation needed.
3. Spawn `agents-architect-agent-author`. It writes `agents/<name>.md`.
4. Report back.
</process>

<output>
Agent path + tool allowlist justification + 5-line summary.
</output>
