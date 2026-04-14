---
name: agents-architect:new
description: Build a complete domain-specialized Claude Code plugin from scratch. Researches the domain, plans skills/agents/commands, authors all files, packages a tarball, evaluates.
argument-hint: "<domain> [--tool <primary-tool>] [--name <plugin-name>] [--deep]"
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Task
  - AskUserQuestion
  - WebSearch
  - WebFetch
---

<objective>
End-to-end orchestration: given a domain (e.g., "3d-modeling", "cardiac-pharmacokinetics", "legal-contract-review"), produce an installable Claude Code plugin with researched best practices, domain-tuned skills, specialist sub-agents, user-facing slash commands, a CLAUDE.md context layer, and (where available) bundled MCP integrations.

**Creates under** `~/.claude/agents-architect-sessions/<timestamp>-<plugin-name>/`:
- `DOMAIN.md` — researched survey
- `MCP_PLAN.md` — available/missing MCPs + fallbacks
- `SKILL_PLAN.md`, `AGENT_PLAN.md`, `COMMAND_PLAN.md` — architecture
- `<plugin-name>/` — the generated plugin (complete directory)
- `EVAL_REPORT.md` — scored output
- `dist/<plugin-name>-<version>.tar.gz` — installable artifact
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/agents-architect/references/anthropic-best-practices.md
@${CLAUDE_PLUGIN_ROOT}/agents-architect/references/context-budget.md
@${CLAUDE_PLUGIN_ROOT}/agents-architect/templates/plugin.json.template
</execution_context>

<context>
Arguments: $ARGUMENTS
Parse as: first positional = domain slug, then optional `--tool <name>`, `--name <plugin-name>`, `--deep` (triggers deeper research pass).
Default plugin-name = `<domain>-arch` (kebab-case).
</context>

<process>
### Phase 0 — Init

1. Parse $ARGUMENTS. If domain missing, `AskUserQuestion`: "What domain?"
2. Compute `session_dir = ~/.claude/agents-architect-sessions/<YYYYMMDDHHMMSS>-<plugin-name>/`. Create it via Bash.
3. Write `session_dir/STATE.md` with parsed args + timestamp.

### Phase 1 — Research (parallel)

Spawn two specialists concurrently via Task:

- `agents-architect-domain-researcher` with prompt: "Research <domain>. Write DOMAIN.md to <session_dir>. <required_reading>: none beyond the skill."
- `agents-architect-mcp-scout` with prompt: "Scan MCPs for <domain> tools. Write MCP_PLAN.md to <session_dir>. <required_reading>: <session_dir>/DOMAIN.md once it exists (poll)."

Wait for both. Read only their 10-line summaries, not the full files.

### Phase 2 — User gate

`AskUserQuestion`: present domain summary + MCP findings + 3 proposed plugin scopes (minimal / standard / ambitious). User picks one.

### Phase 3 — Plan (sequential, context-lean)

Spawn `agents-architect-domain-researcher` again OR use the orchestrator LLM directly to produce (short, ≤2 pages each):

- `SKILL_PLAN.md` — list of skills to create. Each entry: name, purpose, trigger surface, siblings.
- `AGENT_PLAN.md` — list of sub-agents. Each: name, role, tools, model, artifact.
- `COMMAND_PLAN.md` — list of slash commands. Each: name, args, objective, agents spawned, gates.

User gate: `AskUserQuestion` "Proceed with this plan? [Yes / Edit / Abort]".

### Phase 4 — Author (parallel where safe)

Create `session_dir/<plugin-name>/` with standard layout. Spawn in parallel:

- `agents-architect-skill-author` — writes `skills/`
- `agents-architect-agent-author` — writes `agents/`
- `agents-architect-command-author` — writes `commands/`

Wait. Then sequentially:

- `agents-architect-context-architect` — writes `CLAUDE.md.template`, `references/context-budget.md`, state schemas.

### Phase 5 — Package

Spawn `agents-architect-plugin-packager`. It writes `.claude-plugin/plugin.json`, `marketplace.json`, `README.md`, `CHANGELOG.md`, `LICENSE`, runs validation, produces tarball.

### Phase 6 — Evaluate

Spawn `agents-architect-evaluator`. It scores the plugin and writes `EVAL_REPORT.md`. If score < 0.7, `AskUserQuestion`: "Low eval score. [Iterate / Ship anyway / Abort]".

### Phase 7 — Install (optional)

`AskUserQuestion`: "Install locally now?" If yes, run:
- `claude plugin marketplace add <session_dir>/<plugin-name>`
- `claude plugin install <plugin-name>@<plugin-name>`

### Phase 8 — Summary

Print to user:
- Session dir path
- Tarball path
- Install command
- Eval verdict
- Next-step suggestions (e.g., `/agents-architect:iterate <plugin-name>`)

Checkpoint `STATE.md` after each phase. Between phases 3-4 and after phase 5, consider `/compact` if context tier has degraded.
</process>

<output>
Summary block with: session dir, artifact paths, install command, eval score, next steps.
</output>
