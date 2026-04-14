---
name: {{NAMESPACE}}:{{COMMAND}}
description: {{ONE_LINE_DESCRIPTION}}
argument-hint: "{{ARG_SCHEMA}}"
allowed-tools:
  - Read
  - Write
  - Bash
  - Task
  - AskUserQuestion
---

<objective>
{{OBJECTIVE_PARAGRAPH}}

**Creates/Updates:**
- `{{OUTPUT_1}}` — {{PURPOSE_1}}
- `{{OUTPUT_2}}` — {{PURPOSE_2}}
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/{{REF_PATH_1}}
@${CLAUDE_PLUGIN_ROOT}/{{TEMPLATE_PATH_1}}
</execution_context>

<context>
Arguments: $ARGUMENTS
Parse as: {{PARSE_RULE}}
</context>

<process>
### Phase 1 — {{PHASE_1_NAME}}
1. {{STEP_1}}
2. {{STEP_2}}

### Phase 2 — {{PHASE_2_NAME}}
3. Spawn `{{AGENT}}` via Task with `<required_reading>` listing: {{FILES}}.
4. Wait for agent's ≤10-line summary. Do NOT read its full output file.

### Phase 3 — User gate
5. `AskUserQuestion`: "{{GATE_QUESTION}}" [Proceed / Edit / Abort].

### Phase 4 — {{PHASE_4_NAME}}
6. {{STEP}}
</process>

<output>
{{OUTPUT_SUMMARY_SPEC}}
</output>
