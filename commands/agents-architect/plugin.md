---
name: agents-architect:plugin
description: Bundle a directory of skills/agents/commands into a validated, installable Claude Code plugin. Produces plugin.json, marketplace.json, README, LICENSE, CHANGELOG, and a tarball. Use when you've authored components ad-hoc and want to ship them.
argument-hint: "<path-to-plugin-dir> [--name <n>] [--version <v>]"
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Task
  - AskUserQuestion
---

<objective>
Turn a loose directory of components into a validated, installable plugin + tarball.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/agents-architect/templates/plugin.json.template
@${CLAUDE_PLUGIN_ROOT}/agents-architect/templates/marketplace.json.template
</execution_context>

<context>
Arguments: $ARGUMENTS — path (required), name + version optional.
</context>

<process>
1. Validate path exists and contains at least one of `skills/`, `commands/`, `agents/`.
2. `AskUserQuestion` for missing metadata: name, description, version, license.
3. Spawn `agents-architect-plugin-packager`. It writes manifests, docs, runs `scripts/validate.py`, builds tarball.
4. If validation fails, report errors and let user choose: auto-fix / manual / abort.
5. Print install instructions.
</process>

<output>
Tarball path + install command + eval summary.
</output>
