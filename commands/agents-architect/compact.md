---
name: agents-architect:compact
description: Checkpoint the current agentic session to disk and emit a resume prompt so you can /compact safely. Use when context has degraded (tier DEGRADING or POOR) mid-workflow.
argument-hint: "[--to <path>] [--note <short-note>]"
allowed-tools:
  - Read
  - Write
  - Bash
---

<objective>
Safe checkpoint before context compaction. Writes STATE.md with: current phase, decisions made, files produced, next action.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/agents-architect/references/context-budget.md
</execution_context>

<context>
Arguments: $ARGUMENTS — optional output path (defaults to `./STATE.md`) and note.
</context>

<process>
1. Read any existing STATE.md to preserve history.
2. Write an updated STATE.md with:
   - `## Phase` (current)
   - `## Decisions` (from recent turns)
   - `## Files produced` (list with paths)
   - `## Next action` (one line)
   - `## Open questions` (if any)
3. Print the resume prompt: "After /compact, read STATE.md and continue from Next action."
</process>

<output>
STATE.md path + resume prompt.
</output>
