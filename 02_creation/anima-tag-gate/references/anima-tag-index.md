# Anima 1.0 Tag Index — Web-First Protocol

## Purpose

This reference defines the external corpus used by `anima-tag-gate`.

Good Anima documents an `anima-1.0.csv → tags_index.json` pipeline. Its generated index stores canonical tags, usage counts, and aliases in category buckets. This repository adopts the **data contract and validation semantics**, not the local Python/SQLite/EXE runtime.

## Source

- Repository: `https://github.com/ShiroEirin/comfyui-good-anima`
- Index: `https://raw.githubusercontent.com/ShiroEirin/comfyui-good-anima/main/danbooru-tags/tags_index.json`
- Upstream index shape: `{ group: [[canonical, count, aliases]] }`

## Web lookup rule

When a hard anchor needs verification, retrieve the index and inspect the intended group. Prefer an exact canonical match, then an exact alias match. Do not use fuzzy similarity as proof.

The final prompt must never contain a tag merely because a search engine or model guessed it was close.

## Provenance

This is an upstream-derived validation protocol. The upstream repository is GPL-3.0 licensed. We do not vendor its full generated corpus here; the skill references the public source instead. Any future vendored dataset must be reviewed for licensing and repository-size impact before inclusion.

## Why the full corpus is not copied here

The personal harness is designed to be pasted into web AI sessions. A giant static tag dump would consume context, make updates expensive, and encourage models to scan unrelated tags. The harness therefore keeps the source pointer + lookup contract lightweight and asks the runtime model to fetch only when a hard anchor actually needs verification.
