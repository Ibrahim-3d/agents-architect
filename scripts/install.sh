#!/usr/bin/env bash
# agents-architect install.sh — install a plugin locally via the marketplace mechanism.
# Usage: install.sh <plugin-dir>
# Requires: claude CLI in PATH.
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: install.sh <plugin-dir>" >&2
  exit 2
fi

PLUGIN_DIR="$(cd "$1" && pwd)"
if [[ ! -f "$PLUGIN_DIR/.claude-plugin/plugin.json" ]]; then
  echo "No .claude-plugin/plugin.json at $PLUGIN_DIR" >&2
  exit 1
fi

NAME="$(python3 -c "import json,sys; print(json.load(open('$PLUGIN_DIR/.claude-plugin/plugin.json'))['name'])")"
MKT_NAME="${NAME}-marketplace"
if [[ -f "$PLUGIN_DIR/.claude-plugin/marketplace.json" ]]; then
  MKT_NAME="$(python3 -c "import json; print(json.load(open('$PLUGIN_DIR/.claude-plugin/marketplace.json'))['name'])")"
fi

echo "==> Adding marketplace $MKT_NAME from $PLUGIN_DIR"
claude plugin marketplace add "$PLUGIN_DIR"

echo "==> Installing $NAME@$MKT_NAME (scope=user)"
claude plugin install "$NAME@$MKT_NAME" --scope user

echo "==> Installed. Verify with: claude plugin list"
