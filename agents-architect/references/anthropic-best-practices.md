# Anthropic Best Practices (condensed)

Curated rules distilled from Anthropic's Claude Code, Skills, Sub-agents, Hooks, and Plugin docs. Load this reference when authoring any agentic primitive.

## Skills

- **Description is the classifier input.** Treat it as the single most important line. Lead with the capability verb, enumerate 10-30 trigger phrase variants, include negative triggers vs. siblings.
- **Progressive disclosure.** Keep SKILL.md body lean. Push long content into `reference.md` and `scripts/`.
- **Name matches folder.** `skills/<name>/SKILL.md` with `name: <name>` in frontmatter.
- **Scripts for determinism.** If work is algorithmic, ship a `scripts/` sidecar; SKILL.md instructs the model to invoke it rather than reimplement.

## Sub-agents

- **Fresh context, tight tools.** Sub-agents run in a new window with an allowlist. Use them for isolation, parallelism, and read-only analysis.
- **Single artifact.** Each agent produces one canonical file. Avoid cross-cutting updates.
- **Forbidden in plugin agents:** `hooks`, `mcpServers`, `permissionMode`.
- **isolation: "worktree"** is the only valid isolation value.
- **Exit summary ≤ 10 lines.** Keeps the orchestrator context lean.

## Slash commands

- **Namespace = plugin name.** `commands/<ns>/<cmd>.md` → invoked as `/ns:cmd`.
- **allowed-tools is an allowlist.** Omit to inherit; set tight for safety.
- **@-imports are inline at expansion time.** Use `${CLAUDE_PLUGIN_ROOT}` for plugin-relative paths.
- **$ARGUMENTS is a raw string.** Document the parse in `argument-hint`; the model handles extraction in the body.
- **Orchestrator vs. task.** Orchestrators always spawn via Task; never inline specialist work.

## Hooks

- **Event names are case-sensitive.** `PostToolUse`, not `postToolUse`.
- **Script permissions.** `chmod +x` and use `${CLAUDE_PLUGIN_ROOT}` paths.
- **Types:** `command`, `http`, `prompt`, `agent`.
- **Key events:** `SessionStart` (deps install), `PreToolUse` (guard/block), `PostToolUse` (format/lint), `PreCompact`/`PostCompact` (checkpoint hygiene).

## MCP servers

- **`.mcp.json` or inline in `plugin.json`.** Prefer file for non-trivial configs.
- **`${CLAUDE_PLUGIN_DATA}`** for persistent deps (venvs, node_modules).
- **`userConfig.sensitive: true`** for tokens — stored in keychain.
- **Tool names:** verb-first, specific (`blender_render_scene`).
- **Return JSON, log stderr.** stdout is the protocol.

## Plugin layout

- `.claude-plugin/plugin.json` + `marketplace.json` are the ONLY files in `.claude-plugin/`.
- All components (skills/, commands/, agents/, hooks/, bin/) live at plugin root.
- Paths must be relative and start with `./`.
- Symlinks are preserved in the plugin cache — use them for shared resources rather than `../` traversal.

## Versioning

- SemVer. Bump `version` on every public content change or Claude Code's cache will serve stale content.
- Maintain `CHANGELOG.md`.

## Context management

- Never read agent definition files — `subagent_type` auto-loads them.
- Never inline large files into subagent spawn prompts — pass paths and let the agent Read.
- Read depth scales with context window: < 500k → frontmatter only for heavy specialist output; ≥ 500k → full body allowed.
- Checkpoint to disk before `/compact`.
