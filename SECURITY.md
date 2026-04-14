# Security Policy

## Reporting a vulnerability

If you discover a security issue in agents-architect — particularly one that could affect users running generated plugins — please **do not** open a public issue.

Email: papsiman5@gmail.com
Subject: `[agents-architect security] <short summary>`

Please include:
- Affected version(s)
- Repro steps
- Impact (local code execution, credential leak, prompt injection surface, etc.)
- Suggested mitigation if you have one

We aim to respond within 72 hours.

## Scope

In scope:
- Prompt-injection vectors in generated plugin scaffolds
- Hook scripts that could exfiltrate data
- MCP scout recommendations that could mislead users into installing malicious servers
- Sub-agent `allowed-tools` loopholes

Out of scope:
- Third-party MCP servers this plugin may recommend (report upstream)
- Claude Code core behavior (report to Anthropic)

## Disclosure

After a fix ships, we'll credit reporters in `CHANGELOG.md` unless anonymity is requested.
