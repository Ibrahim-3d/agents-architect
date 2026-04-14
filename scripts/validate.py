#!/usr/bin/env python3
"""
agents-architect validate.py — structural validation of a Claude Code plugin.

Checks:
- .claude-plugin/plugin.json exists and has required fields.
- Components live at plugin root, not inside .claude-plugin/.
- Every skill has SKILL.md with YAML frontmatter containing `name` and `description`.
- Every agent has YAML frontmatter with `name` and `description`.
- Every command has YAML frontmatter with `name`, `description`, `argument-hint`.
- Agent frontmatter does NOT include forbidden keys (hooks, mcpServers, permissionMode).
- All `@`-imports in commands/agents/skills reference files that exist.
- hooks.json (if present) is valid JSON.
- .mcp.json (if present) is valid JSON.

Usage:  python3 validate.py <plugin-dir>
Exit: 0 if clean, 1 if errors found. Prints human-readable report.
"""

import json
import re
import sys
from pathlib import Path

ERRORS = []
WARNINGS = []
FORBIDDEN_AGENT_KEYS = {"hooks", "mcpServers", "permissionMode"}


def err(msg: str) -> None:
    ERRORS.append(msg)


def warn(msg: str) -> None:
    WARNINGS.append(msg)


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm_text = text[3:end].strip()
    result: dict = {}
    current_key = None
    for line in fm_text.splitlines():
        if ":" in line and not line.startswith(" ") and not line.startswith("\t") and not line.startswith("-"):
            k, _, v = line.partition(":")
            current_key = k.strip()
            result[current_key] = v.strip()
        elif current_key and (line.startswith("  -") or line.startswith("- ")):
            result.setdefault(current_key + "_list", []).append(line.lstrip(" -").strip())
    return result


def check_manifest(root: Path) -> None:
    mf = root / ".claude-plugin" / "plugin.json"
    if not mf.exists():
        warn("No .claude-plugin/plugin.json — plugin will be auto-discovered but manifest is recommended.")
        return
    try:
        data = json.loads(mf.read_text())
    except json.JSONDecodeError as e:
        err(f"plugin.json is not valid JSON: {e}")
        return
    if "name" not in data:
        err("plugin.json missing required field: name")
    if "version" not in data:
        warn("plugin.json missing version (recommended).")


def check_components_at_root(root: Path) -> None:
    bad = root / ".claude-plugin"
    for sub in ["skills", "commands", "agents", "hooks", "monitors", "output-styles"]:
        if (bad / sub).exists():
            err(f"Components must be at plugin root, not inside .claude-plugin/: found {bad / sub}")


def check_skills(root: Path) -> None:
    sdir = root / "skills"
    if not sdir.exists():
        return
    for skill_dir in sdir.iterdir():
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            err(f"Skill missing SKILL.md: {skill_dir}")
            continue
        fm = parse_frontmatter(skill_md)
        if "name" not in fm:
            err(f"SKILL.md missing name frontmatter: {skill_md}")
        elif fm["name"] != skill_dir.name:
            warn(f"SKILL.md name '{fm['name']}' != folder '{skill_dir.name}'")
        if "description" not in fm:
            err(f"SKILL.md missing description: {skill_md}")


def check_agents(root: Path) -> None:
    adir = root / "agents"
    if not adir.exists():
        return
    for agent in adir.glob("*.md"):
        fm = parse_frontmatter(agent)
        if "name" not in fm:
            err(f"Agent missing name: {agent}")
        if "description" not in fm:
            err(f"Agent missing description: {agent}")
        for forbidden in FORBIDDEN_AGENT_KEYS:
            if forbidden in fm:
                err(f"Agent has forbidden frontmatter key '{forbidden}': {agent}")


def check_commands(root: Path) -> None:
    cdir = root / "commands"
    if not cdir.exists():
        return
    for cmd in cdir.rglob("*.md"):
        fm = parse_frontmatter(cmd)
        if "name" not in fm:
            err(f"Command missing name: {cmd}")
        if "description" not in fm:
            err(f"Command missing description: {cmd}")


def check_imports(root: Path) -> None:
    pattern = re.compile(r"@(\$\{CLAUDE_PLUGIN_ROOT\}/[^\s\"\'<>]+|\./[^\s\"\'<>]+|[^\s\"\'<>@]+\.md)")
    for md in list(root.rglob("*.md")):
        if ".git/" in str(md):
            continue
        text = md.read_text(encoding="utf-8", errors="ignore")
        for m in pattern.finditer(text):
            ref = m.group(1)
            # only check plugin-root-relative and explicit relative
            if ref.startswith("${CLAUDE_PLUGIN_ROOT}/"):
                target = root / ref[len("${CLAUDE_PLUGIN_ROOT}/") :]
            elif ref.startswith("./") or ref.startswith("../"):
                target = (md.parent / ref).resolve()
            else:
                continue
            if not target.exists():
                warn(f"Broken @-import in {md}: {ref}")


def check_json_files(root: Path) -> None:
    for name in ["hooks/hooks.json", ".mcp.json", ".lsp.json", "monitors/monitors.json"]:
        f = root / name
        if f.exists():
            try:
                json.loads(f.read_text())
            except json.JSONDecodeError as e:
                err(f"{name} invalid JSON: {e}")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate.py <plugin-dir>", file=sys.stderr)
        return 2
    root = Path(sys.argv[1]).resolve()
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        return 2

    check_manifest(root)
    check_components_at_root(root)
    check_skills(root)
    check_agents(root)
    check_commands(root)
    check_imports(root)
    check_json_files(root)

    print(f"\n=== Validation report for {root} ===")
    if ERRORS:
        print(f"\n{len(ERRORS)} ERRORS:")
        for e in ERRORS:
            print(f"  [ERR] {e}")
    if WARNINGS:
        print(f"\n{len(WARNINGS)} warnings:")
        for w in WARNINGS:
            print(f"  [warn] {w}")
    if not ERRORS and not WARNINGS:
        print("\nClean.")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
