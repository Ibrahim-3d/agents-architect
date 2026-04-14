# Context Budget Rules

## Tier thresholds

| Tier       | % used  | Orchestrator behavior                                                                |
|------------|---------|--------------------------------------------------------------------------------------|
| PEAK       | 0–30    | Full ops. Read bodies of specialist output. Spawn 3+ agents in parallel.             |
| GOOD       | 30–50   | Prefer frontmatter-only reads. Delegate heavy work. Parallelism OK.                  |
| DEGRADING  | 50–70   | Economize. Frontmatter + summaries only. Warn user. Prep checkpoint.                 |
| POOR       | 70+     | Emergency. Write STATE.md. Refuse new heavy reads. Run `/agents-architect:compact` then `/compact`. |

## Read-depth by model context window

| Context window | Specialist output bodies  | SUMMARY.md    | PLAN.md (non-current phase) |
|----------------|---------------------------|---------------|------------------------------|
| < 500k (default 200k) | Frontmatter / header only | Frontmatter   | Current phase only           |
| ≥ 500k (1M)           | Full body permitted       | Full permitted | Current phase only          |

## Universal rules

1. **Never** read agent definition files; `subagent_type` auto-loads them.
2. **Never** inline large files into subagent spawn prompts — pass paths via `<required_reading>`.
3. **Always** tell specialists to write to disk and return ≤10-line summaries.
4. **Always** checkpoint to STATE.md before any `/compact`.
5. Proactively warn the user when transitioning to DEGRADING: "Context is heavy. Checkpoint?"

## Degradation warning signs (catch pre-POOR)

- Agent uses vague phrases ("appropriate handling", "standard patterns") instead of specifics.
- Tool-call count per turn drops below baseline.
- Agent omits protocol steps it normally follows.
- User restates facts already in context.

## Delegation heuristic

If the orchestrator needs to process > 3 files or > 1000 lines to make a decision, spawn a specialist. Read only its summary.

## Checkpoint schema

`STATE.md`:

```markdown
# State
Session: <id>
Updated: <timestamp>

## Phase
<current phase>

## Decisions
- <key=value>

## Files produced
- <path> — <one-line purpose>

## Next action
<one line>

## Open questions
- ...
```

Any architect command may be resumed via `Read STATE.md`.
