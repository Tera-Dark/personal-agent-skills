# Anima Tag Index — Sharded Web-First Protocol

## Purpose

Good Anima derives a compact index from `anima-1.0.csv`, grouping canonical tags, counts and aliases. The Harness keeps upstream data as the source of truth, but web models must not load the entire JSON file.

## Runtime retrieval

- Manifest: `https://raw.githubusercontent.com/Tera-Dark/personal-agent-skills/main/bundle/tag-index/manifest.json`
- Shards: `https://raw.githubusercontent.com/Tera-Dark/personal-agent-skills/main/bundle/tag-index/<group>/<prefix>.json`
- Each generated shard contains exact canonical keys and exact aliases for one group/prefix.
- Read the manifest once per session or until its source SHA changes. Group candidates by group and prefix to reuse fetched shards.
- If a listed shard is unreadable, its candidates are unverified. If the manifest proves that a prefix is absent from the complete source snapshot, candidates under that prefix are missing.
- Never infer a missing tag from a search snippet or model memory.

## Build and validation

`scripts/build_tag_index.py` downloads upstream data only in CI/build environments, validates its schema, generates deterministic two-character lookup shards, removes orphaned shards, and supports `--check` for reproducibility verification. `--self-test` runs offline routing and alias tests.

The CI workflow regenerates shards on pushes and requires them to be current on pull requests. A partial cache is never treated as a complete source index.

## Provenance and licensing

- Upstream repository: `https://github.com/ShiroEirin/comfyui-good-anima`
- Upstream index: `https://raw.githubusercontent.com/ShiroEirin/comfyui-good-anima/main/danbooru-tags/tags_index.json`
- Upstream data license: GPL-3.0. Generated shards publish the source SHA-256 in the manifest.
- The derived dataset has separate provenance/licensing from the Harness source code; the root MIT license does not relicense upstream data.

## Identity contract

- `exact`: input string is a canonical key in the requested group.
- `alias`: exact alias match resolves uniquely to one canonical key.
- `missing`: neither exact nor uniquely resolvable alias exists in the source snapshot.
- `unverified`: a declared shard could not be read or validated.

Counts never decide creative priority. Identity matching never normalizes punctuation or performs fuzzy similarity.
