# Anima Tag Gate — P2 Acceptance Suite

This is the manual/regression acceptance protocol for the Web-first Anima Tag Gate. It is intentionally data-source driven: the live Good Anima `tags_index.json` is the authority, not a copied local corpus.

## Pass rule

A case passes only when the gate follows the three-state contract:

- `exact` → canonical tag may enter `hard_tags`.
- `alias` → canonical tag may enter `hard_tags`; the submitted alias is retained only as provenance.
- `missing` / `unverified` → must not enter `hard_tags`; meaning is routed to Natural Language.

Fuzzy search, semantic similarity, search-engine suggestions, model memory, and candidate ranking are never valid evidence.

## Test matrix

| ID | Input | Group | Expected | Acceptance condition |
|---|---|---|---|---|
| P2-01 | `1girl` | `general` | exact | canonical output is exactly `1girl` |
| P2-02 | `long_hair` | `general` | exact | canonical output is exactly `long_hair` |
| P2-03 | `cinematic silver aura` | `general` | missing | no hard tag; meaning goes to NL |
| P2-04 | an intentionally misspelled/alternate spelling selected from the live index alias list | same group as canonical | alias | canonical is returned and matched alias is recorded |
| P2-05 | a fuzzy candidate that merely resembles a real tag | same group | missing | candidate is rejected; never promoted to hard tag |
| P2-06 | an artist-like string queried only in `general` | `general` | missing | it is not reclassified as an artist by similarity |
| P2-07 | a known character queried in `character` | `character` | exact or alias | character identity is verified in the character group |
| P2-08 | the same character-like string queried in `general` | `general` | missing unless independently canonical there | group isolation is preserved |
| P2-09 | a known IP queried in `series` | `series` | exact or alias | series/IP identity is verified separately |
| P2-10 | `37_(reverse:1999)` | `character` | identity-preserving | validation does not split, rewrite, or escape the canonical identity |
| P2-11 | `37\\(reverse1999\\)` before validation | `character` | unverified/missing unless literally present in source | serialized Anima syntax is not silently treated as canonical Danbooru identity |
| P2-12 | any valid tag while the source is unavailable/malformed | expected group | unverified | never invent a result; route meaning to NL |

## Alias test procedure

Because the full upstream index is intentionally not vendored, P2-04 must use a real alias from the live source at test time:

1. Open the configured `tags_index.json` source.
2. Select one entry whose third field contains a non-empty alias.
3. Copy one alias exactly, without spelling correction.
4. Submit it with the same group as its canonical entry.
5. Confirm the result is `alias`.
6. Confirm `canonical` equals the first field of that entry.
7. Confirm `matched_alias` equals the submitted string.
8. Confirm only the canonical tag is eligible for `hard_tags`.

This avoids hard-coding an alias that may disappear or change in a future upstream index revision.

## Negative controls

These cases must fail closed:

### Fuzzy rejection

Input: a near-spelling of a real canonical tag that is not itself an exact canonical tag or exact alias.

Expected: `missing`; never copy the nearest candidate into `hard_tags`.

### Semantic rejection

Input: a natural-language concept that is visually similar to a known tag but is not listed as canonical or alias.

Expected: `missing`; translate the intended meaning into NL.

### Group isolation

Input: an artist-like token against `general`, or a character token against `artist`.

Expected: no cross-group promotion. The gate may only accept evidence from the requested/defensible group.

### Syntax isolation

Input: `37_(reverse:1999)`.

Expected: preserve canonical identity during validation. The later Anima serialization layer may produce `37\\(reverse1999\\)`, but the gate itself must not mutate the registry identity.

## Failure-mode test

Simulate one of:

- upstream source unavailable;
- JSON cannot be parsed;
- requested group absent;
- lookup cannot be proven.

Expected behavior:

`unverified` → no hard tag → NL fallback.

A source outage must never cause the model to fall back to fuzzy matching or memory.

## Prompt-compiler integration check

Given a blueprint containing:

- one exact tag;
- one alias;
- one missing hard anchor;
- one fuzzy candidate;

The compiler must produce:

- exact → canonical hard tag;
- alias → canonical hard tag, alias omitted from final prompt;
- missing → Natural Language meaning;
- fuzzy candidate → rejected from hard tags.

The Tag Gate may not alter the blueprint's character, clothing, pose, composition, aesthetic, or punctum decisions.

## P2 exit criteria

P2 is **PASS** only when all of the following are true:

- [ ] exact canonical lookup works;
- [ ] alias lookup returns canonical + provenance;
- [ ] missing lookup fails closed;
- [ ] fuzzy candidates never become hard tags;
- [ ] semantic similarity never becomes hard tags;
- [ ] artist / character / series groups remain isolated;
- [ ] canonical identity is separate from Anima serialization;
- [ ] `37_(reverse:1999)` survives validation unchanged;
- [ ] source failure degrades to `unverified` → NL;
- [ ] compiler integration respects the same gate contract;
- [ ] no test requires a local Python runtime, SQLite database, EXE, or vendored full corpus.
