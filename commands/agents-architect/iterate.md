---
name: agents-architect:iterate
description: Iterate on an existing agents-architect-generated plugin — re-run eval, fix flagged skills/agents/commands, bump version. Use after /agents-architect:new when the eval report suggests improvements, or after manual edits.
argument-hint: "<plugin-path> [--focus skills|agents|commands|eval]"
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Task
  - AskUserQuestion
---

<objective>
Improve a generated plugin in-place based on eval findings or user-listed issues.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/agents-architect/references/skill-triggers.md
@${CLAUDE_PLUGIN_ROOT}/agents-architect/references/agent-tool-allowlists.md
</execution_context>

<context>
Arguments: $ARGUMENTS — path to the plugin, optional focus.
</context>

<process>
1. Read `EVAL_REPORT.md` if present; else spawn `agents-architect-evaluator` to produce one.
2. `AskUserQuestion` to pick what to fix (from report) + any manual issues.
3. For each chosen fix, spawn the appropriate author agent (`agents-architect-skill-author`, `agents-architect-agent-author`, `agents-architect-command-author`, `agents-architect-context-architect`) with a targeted brief.
4. After fixes, re-run `agents-architect-evaluator`. Diff scores.
5. Bump `plugin.json.version` (patch or minor). Update `CHANGELOG.md`.
6. Rebuild tarball via `agents-architect-plugin-packager`.
</process>

<output>
Before/after eval scores + changed files + new tarball path.
</output>
