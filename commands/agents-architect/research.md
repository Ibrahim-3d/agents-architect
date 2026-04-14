---
name: agents-architect:research
description: Research a domain and produce DOMAIN.md without building a plugin. Useful for exploration before committing to a full /agents-architect:new.
argument-hint: "<domain> [--deep]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Task
  - WebSearch
  - WebFetch
---

<objective>
Run the domain-research pass in isolation. Output: `~/.claude/agents-architect-sessions/<ts>-<domain>/DOMAIN.md` + MCP_PLAN.md.
</objective>

<context>
Arguments: $ARGUMENTS — first positional = domain, optional `--deep`.
</context>

<process>
1. Parse args. Create session dir.
2. Spawn `agents-architect-domain-researcher` and `agents-architect-mcp-scout` in parallel.
3. Wait. Present combined 20-line summary to user.
4. Offer next step: `/agents-architect:new <domain>` if user wants to proceed.
</process>

<output>
Session dir path + DOMAIN.md + MCP_PLAN.md paths + combined summary.
</output>
