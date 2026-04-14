# Changelog

All notable changes will be documented here. SemVer.

## 0.1.0 — 2026-04-14

Initial release.

- 9 slash commands under `/agents-architect:*` namespace.
- 8 sub-agents covering research → planning → authoring → packaging → eval.
- 7 authoring skills: skill-authoring, agent-authoring, command-authoring, context-management, plugin-packaging, mcp-integration, domain-research.
- Reference library: anthropic-best-practices, skill-triggers, agent-tool-allowlists, context-budget, memory-tiers, plugin-manifest, mcp-selection.
- Templates for skill, agent, command, plugin.json, marketplace.json, CLAUDE.md.
- Scripts: validate.py, scaffold.py, install.sh.
- Hooks: SessionStart (chmod scripts), PreCompact (checkpoint reminder).
- Self-multiplication: `/agents-architect:new` produces installable Claude Code plugins for arbitrary domains.
- Context management: tiered budget (PEAK/GOOD/DEGRADING/POOR), checkpoint → /compact flow.
- Structurally informed by GSD (gsd-build/get-shit-done): orchestrator↔specialist, modular refs, single-artifact-per-agent.
