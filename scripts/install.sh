#!/usr/bin/env bash
# install.sh — symlink every skill in this hub into an agent's skills directory.
#
# The hub keeps skills in numbered layer folders (00_core/, 01_router/, ...) for
# readability, but most agent runtimes discover skills one level deep:
#   Claude Code : ~/.claude/skills/<name>/SKILL.md
#   Codex       : ~/.agents/skills/<name>/SKILL.md
#   (project)   : ./.claude/skills/<name>/SKILL.md
# This script flattens the layout with symlinks so every skill is discoverable
# while the repo stays organized.
#
# Usage:
#   scripts/install.sh                       # -> ~/.claude/skills
#   scripts/install.sh ~/.agents/skills      # -> Codex
#   scripts/install.sh ./.claude/skills      # -> project-local
#   scripts/install.sh --dry-run [target]
set -euo pipefail

DRY=0
if [[ "${1:-}" == "--dry-run" ]]; then DRY=1; shift; fi
TARGET="${1:-$HOME/.claude/skills}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

mkdir -p "$TARGET"
count=0
while IFS= read -r skill_md; do
  dir="$(dirname "$skill_md")"
  name="$(basename "$dir")"
  link="$TARGET/$name"
  if [[ -L "$link" || -e "$link" ]]; then
    if [[ "$(readlink -f "$link" 2>/dev/null || true)" == "$(readlink -f "$dir")" ]]; then
      echo "  = $name (already linked)"; continue
    fi
    echo "  ! $name exists at $link and is not this hub — skipping"; continue
  fi
  if [[ $DRY -eq 1 ]]; then echo "  + $name -> $dir (dry run)"; else ln -s "$dir" "$link"; echo "  + $name -> $dir"; fi
  count=$((count+1))
done < <(find "$ROOT" -mindepth 2 -maxdepth 3 -name SKILL.md -not -path '*/.git/*' | sort)

echo "linked $count skill(s) into $TARGET"
