# MCP Selection Decision Tree

```
Domain needs an external tool?
├── No  → Use built-in tools (Bash, Read, Write, Edit, WebSearch, WebFetch).
└── Yes → Is there a public MCP for it?
         ├── Registry hit (search_mcp_registry) → suggest_connectors → wire in .mcp.json
         ├── GitHub "mcp-server-<tool>" → vet → fork or pin; wire in .mcp.json
         └── No match →
              ├── Tool has a CLI → wrap via Bash (cheapest)
              ├── Tool has an SDK → thin custom MCP server (reusable)
              └── GUI-only → Playwright MCP for browser automation
```

## Registry usage

```
search_mcp_registry(keywords=["blender", "3d", "modeling"])
→ results with: name, id, capabilities, auth
```

For each promising hit: WebFetch the README to confirm tool surface, transport, and auth.

## Custom MCP decision

Write a custom MCP when:
- Tool is used ≥3 times across workflows.
- Bash-wrapping is flaky (long-running, stateful, or multi-step handshake).
- The SDK offers structured responses you can return as JSON.

Skip custom MCP when:
- Tool is invoked ad-hoc < 3x.
- Latency of Bash shell-out is acceptable.
- The data is trivially parseable from CLI stdout.

## Integration checklist

- [ ] `.mcp.json` or `mcpServers` inline in `plugin.json`.
- [ ] `userConfig` for any tokens/paths (`sensitive: true` for secrets).
- [ ] `SessionStart` hook to install deps into `${CLAUDE_PLUGIN_DATA}` if needed.
- [ ] Health-check command documented in README.
- [ ] Rate-limit + timeout per tool.
- [ ] Tool names verb-first and specific.
- [ ] stderr for logs, stdout for protocol only.
