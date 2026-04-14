# Memory Tiers

Layered, lazy, on-disk-first.

## Tier 0 — System + tools
Model card + tool schemas. Fixed. Not editable.

## Tier 1 — CLAUDE.md (project memory)
Loaded every session at ≤500 lines. Contents:
- Project purpose (1 paragraph)
- Stack + build/test commands
- Glossary (nicknames, acronyms, project-specific terms)
- Conventions (file layout, naming, commit style)
- Red-lines (things Claude must NEVER do)
- Pointers to deeper docs via `@` imports — do NOT inline them here.

## Tier 2 — Skills (loaded on trigger)
`SKILL.md` files load only when their descriptions match the prompt. Use progressive disclosure: body ≤ 150 lines; push depth into `reference.md` / `scripts/` loaded on demand.

## Tier 3 — References (loaded by `@`-import)
Long docs referenced from commands/skills/agents. Only pulled in when a workflow needs them. Keep each reference focused on one topic.

## Tier 4 — Session scratchpads (on disk, cross-turn)
`.planning/STATE.md`, `.arch/state.json`, `.planning/research/*.md`. Checkpoint here; orchestrators Read selectively.

## Tier 5 — Subagent isolates (throwaway context)
Heavy work runs in a fresh window; only the exit summary returns to the orchestrator. The specialist's full output lives on disk (e.g., `DOMAIN.md`) and is re-Read if ever needed.

## Designing a plugin's memory tiers

For each command flow, decide:
1. What goes in CLAUDE.md (always loaded)?
2. Which skills trigger automatically (load on trigger)?
3. Which references are `@`-imported by which commands/agents?
4. What state gets checkpointed to disk?
5. Which specialists own which heavy reads (isolation boundary)?

Write the answers into the plugin's `context-budget.md` and `state-schema.md` so they're explicit and audit-able.
