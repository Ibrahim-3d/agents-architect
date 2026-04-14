# Plugin Manifest Reference

Distilled from Claude Code's plugin reference.

## `.claude-plugin/plugin.json`

### Required
- `name` (string, kebab-case, unique)

### Metadata (recommended)
- `version` (SemVer)
- `description`
- `author` (`{name, email?, url?}`)
- `homepage`
- `repository`
- `license`
- `keywords` (string array)

### Components (if using custom paths)
- `skills` (string | array) — directories containing `<n>/SKILL.md`
- `commands` (string | array) — flat `.md` or directories
- `agents` (string | array)
- `hooks` (string | array | object)
- `mcpServers` (string | array | object)
- `outputStyles` (string | array)
- `lspServers` (string | array | object)
- `monitors` (string | array | object)

All paths relative, start with `./`. To keep defaults AND add more: `"skills": ["./skills/", "./extras/"]`.

### User-facing config
- `userConfig`: `{ KEY: { description, sensitive: bool } }`
  - Non-sensitive → `${user_config.KEY}` substitution + `CLAUDE_PLUGIN_OPTION_KEY` env
  - Sensitive → keychain; ~2KB total limit.

### Channels (for message-injection MCPs)
- `channels`: `[{ server: <mcp-key>, userConfig: {...} }]`

### Env substitutions
- `${CLAUDE_PLUGIN_ROOT}` — plugin install path (changes on update).
- `${CLAUDE_PLUGIN_DATA}` — `~/.claude/plugins/data/<id>/` (persists).

## `.claude-plugin/marketplace.json`

```json
{
  "name": "<marketplace-name>",
  "owner": { "name": "…", "email": "…" },
  "description": "…",
  "plugins": [
    { "name": "<plugin>", "source": "./" | "git+https://…", "description": "…", "version": "…" }
  ]
}
```

## Directory layout

```
my-plugin/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json      (if shipping a marketplace)
├── skills/<name>/SKILL.md
├── commands/<ns>/<cmd>.md
├── agents/<agent>.md
├── hooks/hooks.json
├── .mcp.json                 (optional)
├── .lsp.json                 (optional)
├── monitors/monitors.json    (optional)
├── bin/                      (executables added to PATH in Bash tool)
├── scripts/
├── settings.json             (default plugin settings)
├── README.md
├── LICENSE
└── CHANGELOG.md
```

**Critical:** components at root, NOT inside `.claude-plugin/`.

## Validation

```bash
claude plugin validate ./my-plugin
# or inside session:
/plugin validate
```

## Install

```bash
claude plugin marketplace add <git-url-or-local-path>
claude plugin install <name>@<marketplace>
# scopes: --scope user|project|local|managed
```

## Cache

Plugins are copied to `~/.claude/plugins/cache/<name>-<marketplace>-<version>/`. Old versions kept 7 days for running sessions. No `../` traversal from cache — use symlinks if shared resources must live outside plugin dir.
