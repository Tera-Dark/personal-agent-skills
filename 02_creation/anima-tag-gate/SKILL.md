---
name: anima-tag-gate
description: Web-first validation gate for Anima Danbooru hard tags. Resolves exact canonical tags, exact aliases, or missing without fuzzy promotion. Uses the Anima 1.0 tag index protocol and never changes creative decisions. Triggers: Anima tag validation, Danbooru tag check, hard tag verification.
metadata:
  author: Tera-Dark
  version: "1.0.0"
  layer: "02_creation"
  load: "on-demand"
  status: "active"
  triggers: "Anima tag validation, Danbooru tag check, hard tag verification"
---

# Anima Tag Gate

This is a **validation layer**, not a design layer. It verifies already-decided hard anchors before they enter an Anima prompt.

## 1. Core contract

Every proposed hard tag has exactly one gate state:

- `exact` — the submitted string is the canonical tag.
- `alias` — the submitted string is listed as an alias of a canonical tag; return the canonical tag and preserve the alias trace.
- `missing` — no exact or alias evidence was found in the configured Anima 1.0 index.

`fuzzy`, semantic similarity, search-engine suggestions, model memory, or candidate ranking **never** become `hard_tags`.

Missing tags are not errors in the creative brief. They are routed to Natural Language instead.

## 2. Web-first data source

The reference corpus follows Good Anima's `anima-1.0.csv → tags_index.json` design, but this skill does not require Python, SQLite, an EXE, or a local path.

Primary source:

`https://raw.githubusercontent.com/ShiroEirin/comfyui-good-anima/main/danbooru-tags/tags_index.json`

Source shape:

```json
{
  "general": [["canonical_tag", 12345, "alias_a,alias_b"]],
  "artist": [["artist_name", 12345, "alias_a"]],
  "character": [["character_name", 12345, "alias_a"]],
  "series": [["series_name", 12345, "alias_a"]]
}
```

The first item is canonical, the second is count metadata, and the third is a comma-separated alias list. Counts are evidence metadata only; they never affect creative ranking.

## 3. Lookup algorithm

For each proposed hard anchor:

1. Normalize only transport-level differences: surrounding whitespace and accidental duplicate spaces.
2. Search the requested group for an **exact canonical** match.
3. If no canonical match exists, search the same group for an **exact alias** match.
4. If alias matched, return its canonical tag and the matched alias.
5. Otherwise return `missing`.
6. Never promote a fuzzy or semantically similar result to `exact` or `alias`.

Do not silently normalize underscores, parentheses, colons, slashes, or other Danbooru syntax into a different tag. Those characters can carry identity and Anima escaping semantics.

## 4. Result contract

Use this compact internal structure:

```json
{
  "input": "<verified alias from the live index>",
  "group": "general",
  "status": "alias",
  "canonical": "<canonical tag from the same index entry>",
  "matched_alias": "<submitted alias>",
  "source": "anima-1.0-index"
}
```

For an exact hit:

```json
{
  "input": "long_hair",
  "group": "general",
  "status": "exact",
  "canonical": "long_hair",
  "source": "anima-1.0-index"
}
```

For a miss:

```json
{
  "input": "cinematic silver aura",
  "group": "general",
  "status": "missing",
  "canonical": null,
  "source": "anima-1.0-index"
}
```

## 5. What may enter `hard_tags`

Only `exact` and `alias` results may enter `hard_tags`.

- `exact` → emit the canonical tag.
- `alias` → emit the canonical tag and keep the alias only as trace metadata.
- `missing` → do not emit a tag; translate the intended meaning into `soft_phrases` or `nltags_block`.

Do not dump every confirmed result into the final prompt. The creative brief still controls which verified anchors matter.

## 6. Group policy

Preferred group mapping:

| Intent | Group |
|---|---|
| artist | `artist` |
| character | `character` |
| series / IP | `series` |
| appearance | `appearance` / `body` |
| clothing | `clothing` / `outfit` |
| accessory / prop | `accessory` / `prop` |
| pose / action | `pose` / `action` |
| expression | `expression` |
| scene / background | `scene` / `background` |
| lighting | `lighting` |
| generic hard anchor | `general` |

If the intended group is ambiguous, do not widen into fuzzy matching. Either verify against the most defensible group or downgrade the phrase to NL.

## 7. Character / series / artist rules

These are high-value identity anchors and should be verified whenever they are part of the blueprint.

- Character: verify the character group; do not substitute a similarly named character.
- Series/IP: verify the series group separately when a series anchor is used.
- Artist: verify only against the artist group; never infer an artist from a general tag.
- Preserve the user's selected artist rather than choosing a more popular one.

## 8. Anima syntax is a later layer

Canonical Danbooru data is **not** the final Anima string.

Example:

`37_(reverse:1999)` is a canonical/registry representation that must later be converted by the Anima syntax layer to:

`37\\(reverse1999\\)`

Do not perform this conversion inside the tag database or validation result. This keeps canonical identity separate from prompt serialization.

## 9. Failure / degradation

If the web source cannot be read, the JSON is malformed, the expected group is absent, or the lookup cannot be proven:

- do not invent a tag;
- mark the anchor `unverified` internally;
- route its meaning to NL;
- optionally tell the user that tag verification was unavailable only when it materially affects the requested output.

A source failure is never permission to use fuzzy matching.

## 10. Prompt budget

Tag Gate is not allowed to increase prompt length merely because more tags were verified. Verification answers **whether a tag is valid**, not **whether it deserves inclusion**.

The compiler remains responsible for compact selection and the final Anima skeleton.

## 11. Quick acceptance tests

- `1girl` → `exact` → `1girl`
- `long_hair` → `exact` → `long_hair`
- `cinematic silver aura` → `missing` → NL
- an unknown artist-like string in `general` → not an artist
- `37_(reverse:1999)` → identity preserved; syntax escaping deferred
- fuzzy search suggestion → never `hard_tags`

For the full P2 acceptance protocol, including a live-index alias test, group isolation, failure-mode checks, and compiler integration, use `tests/test-suite.md`.

## References

- `references/anima-tag-index.md` — Web-first index source, schema, and licensing boundary
- `tests/test-suite.md` — P2 acceptance and regression matrix
