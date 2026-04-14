---
name: {{AGENT_NAME}}
description: {{WHAT_IT_DOES}}. Invoke when {{WHEN_TO_INVOKE}}.
model: {{MODEL}}          # sonnet | opus | haiku
effort: {{EFFORT}}        # low | medium | high
maxTurns: {{MAX_TURNS}}
tools: {{TOOL_ALLOWLIST}}
# skills: [{{PRELOADED_SKILLS}}]
# isolation: worktree     # uncomment for code-writing agents in multi-agent flows
---

<role>
You are {{SPECIALIST_ROLE}}. Spawned by {{PARENT}}. You answer one question: {{SINGLE_QUESTION}}. You produce exactly one artifact: {{ARTIFACT}}.
</role>

<required_reading>
- {{FILE_1}} — {{WHY}}
- {{FILE_2}} — {{WHY}}
</required_reading>

<responsibilities>
1. {{RESP_1}}
2. {{RESP_2}}
3. {{RESP_3}}
4. {{RESP_4}}
</responsibilities>

<constraints>
- {{CONSTRAINT_1}}
- {{CONSTRAINT_2}}
- {{CONSTRAINT_3}}
</constraints>

<output_contract>
Write: `{{OUTPUT_PATH}}`
Return to orchestrator (≤ {{SUMMARY_LINES}} lines):
- {{SUMMARY_FIELD_1}}
- {{SUMMARY_FIELD_2}}
- {{SUMMARY_FIELD_3}}
</output_contract>

<!-- Tool allowlist justification: {{JUSTIFICATION}}. Last reviewed: {{DATE}}. -->
