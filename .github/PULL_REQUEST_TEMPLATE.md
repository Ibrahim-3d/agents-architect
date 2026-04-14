## What
<!-- One-line summary of the change -->

## Why
<!-- The problem or use case -->

## How
<!-- Implementation notes — new skill? new agent? template change? -->

## Checklist
- [ ] `python3 scripts/validate.py .` passes
- [ ] If new skill: description < classifier limit, includes positive + negative examples
- [ ] If new agent: has `allowed-tools`, no forbidden keys (`hooks`, `mcpServers`, `permissionMode`)
- [ ] If new command: uses `$ARGUMENTS` correctly, heavy context via `@`-imports
- [ ] CHANGELOG.md updated
- [ ] Version bumped in `plugin.json` if user-facing change
