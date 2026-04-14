#!/usr/bin/env bash
# push.sh — publish agents-architect to GitHub
# Usage:  ./push.sh [github-user] [repo-name]
set -euo pipefail

USER="${1:-Ibrahim-3d}"
REPO="${2:-agents-architect}"
REMOTE="git@github.com:${USER}/${REPO}.git"

if [ ! -d .git ]; then
  git init -b main
fi

git add -A
git commit -m "initial commit: agents-architect v0.1.0" || echo "(nothing to commit)"

if git remote | grep -q origin; then
  git remote set-url origin "$REMOTE"
else
  git remote add origin "$REMOTE"
fi

echo
echo "=== About to push to $REMOTE ==="
echo "Dry-run first. Push for real with:"
echo "  git push -u origin main"
echo
echo "Or create the repo via gh:"
echo "  gh repo create $USER/$REPO --public --source=. --remote=origin --push"
