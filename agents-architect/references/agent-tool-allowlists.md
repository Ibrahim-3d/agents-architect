# Canonical Tool Allowlists by Archetype

Default to the tightest set that achieves the job.

| Archetype            | Tools                                                                 | Notes                                           |
|----------------------|-----------------------------------------------------------------------|-------------------------------------------------|
| Domain researcher    | `Read, Write, WebSearch, WebFetch, Grep, Glob`                        | Writes DOMAIN.md only.                          |
| Code researcher      | `Read, Grep, Glob, Bash`                                              | Read-only codebase analysis.                    |
| Pattern mapper       | `Read, Grep, Glob, Write`                                             | Writes PATTERNS.md.                             |
| Planner              | `Read, Write, AskUserQuestion`                                        | Writes PLAN.md.                                 |
| Executor / coder     | `Read, Write, Edit, Bash, Glob, Grep`                                 | Add `isolation: worktree` in multi-agent flows. |
| Code reviewer        | `Read, Grep, Glob, Bash`                                              | Read-only; no Write.                            |
| Doc writer           | `Read, Write, Edit, Glob`                                             | No Bash unless the doc references commands.     |
| Doc verifier         | `Read, Bash, Grep`                                                    | Runs snippets; read-only on source.             |
| Security auditor     | `Read, Grep, Glob, Bash`                                              | Read-only.                                      |
| MCP scout            | `Read, Write, WebSearch, WebFetch`                                    | Writes MCP_PLAN.md.                             |
| Evaluator            | `Read, Bash, Glob, Grep`                                              | Read-only; writes EVAL_REPORT.md only.          |
| Packager             | `Read, Write, Edit, Bash, Glob`                                       | Writes manifests + tarball.                     |
| Background watcher   | `Read, Bash`                                                          | Long-running; use `background: true`.           |

## Justification comment

Every agent file should end with:

```
<!-- Tool allowlist justification: <why each tool is needed>. Last reviewed: <YYYY-MM-DD>. -->
```

So future auditors can verify the allowlist without guessing.

## Forbidden in plugin-shipped agents

- `hooks`
- `mcpServers`
- `permissionMode`

(Security: plugin agents cannot widen their own permissions. Configure these at plugin level.)
