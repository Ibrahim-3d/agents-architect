---
name: agents-architect:install
description: Install a generated plugin locally via the marketplace mechanism. Self-installs agents-architect or installs any plugin produced by /agents-architect:new.
argument-hint: "[<path-or-name>]"
allowed-tools:
  - Read
  - Bash
  - AskUserQuestion
---

<objective>
One-step install for agents-architect-produced plugins.
</objective>

<context>
Arguments: $ARGUMENTS — plugin name (if already in a marketplace) or path to plugin dir.
</context>

<process>
1. If $ARGUMENTS is empty, default to agents-architect itself at `${CLAUDE_PLUGIN_ROOT}`.
2. If $ARGUMENTS is a path, run:
   - `claude plugin marketplace add <path>`
   - Read `<path>/.claude-plugin/plugin.json` to get the plugin name.
   - `claude plugin install <name>@<marketplace-name>`
3. If $ARGUMENTS is a name, assume the marketplace is already added and run `claude plugin install <name>`.
4. Verify: `claude plugin list` + confirm the plugin appears.
5. Print enable/disable + uninstall commands for reference.
</process>

<output>
Installed plugin name + scope + a next-step hint (e.g., "try /<ns>:<cmd>").
</output>
