# Skill Trigger Engineering

The description field is classifier input. These patterns maximize precision and recall.

## Phrase surface

Aim for 10-30 trigger variants. Cover:

- **Imperative forms**: "Write X", "Draft X", "Create X", "Generate X".
- **Meta-descriptions**: "Help me with X", "I need X for Y".
- **Problem framings**: "My X is Z", "X feels wrong", "fix X".
- **Noun-form queries**: "ideas for X", "examples of X".
- **Domain jargon**: the 5 terms a practitioner would use verbatim.

## Disambiguation

For every skill with a neighbor, add one or more clauses:

- `Not for <neighbor>; use <that skill> for...`
- `For editing existing content, see copy-editing. For writing new content from scratch, this skill.`

Without these, two overlapping skills both fire and the classifier picks randomly.

## Negative triggers

Include 2-5 common false-positive patterns:

- "Not for casual conversation about X."
- "Not for translation between languages."

## Length budget

Descriptions under ~400 tokens. Every skill description loads every turn; they compound.

## Anti-patterns

- "AI-powered, intelligent, comprehensive" — marketing adjectives dilute the classifier signal.
- Starting with "This skill is..." — passive, adds no trigger value. Start with a verb.
- "Use when appropriate" — meaningless. Specify prompts verbatim.
- Overlapping descriptions with no negative triggers — both skills fire, quality tanks.

## Worked example

**Bad description:**
> This is an AI-powered comprehensive tool for helping with emails. Use it when appropriate to write professional emails.

**Good description:**
> Write or improve cold outreach and follow-up emails. Use when the user asks to "write a cold email", "draft a follow-up", "email this prospect", "reach out to [name]", "sequence for [persona]", or shares a draft saying "sounds too salesy" / "make this more personal". Not for internal emails to colleagues (use internal-comms skill). Not for newsletter content (use email-sequence).

## Eval

Each skill ships `evals/positive.md` (10+ prompts that must fire) and `evals/negative.md` (10+ that must not). Review classifier behavior in practice; rewrite descriptions where precision/recall is poor.
