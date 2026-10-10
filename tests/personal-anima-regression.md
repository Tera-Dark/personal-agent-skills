# P12 Shared Prompt Architecture Regression Matrix

> Manual/model-behavior regression suite for the shared Prompt Core and Anima / NAI5 renderer architecture.
> Machine-checkable contracts are enforced by scripts/check_personal_anima_regression.py.
> BLOCKED means required evidence is unavailable; it must never be converted to PASS by memory or fuzzy matching.

## Test record

~~~text
case: <ID>
result: PASS | FAIL | BLOCKED
owner: <layer>
evidence: <prompt/output excerpt or visual observation>
notes:
~~~

## 1. Tag identity / IP / artist

### P12-TAG-01 — exact canonical
- Input: 1girl
- Expect: exact canonical match; eligible for hard_tags.
- Owner: danbooru-tag-gate

### P12-TAG-02 — exact alias
- Input: one alias taken from the live Anima 1.0 index.
- Expect: alias → indexed canonical tag; alias kept only as trace metadata.
- Owner: danbooru-tag-gate
- Evidence: record the live index entry.

### P12-TAG-03 — missing tag
- Input: definitely_not_a_real_anima_tag_xyz
- Expect: missing; never enters hard_tags; meaning may fall back to NL.
- Owner: danbooru-tag-gate

### P12-TAG-04 — fuzzy trap
- Input: an intentional misspelling near a known tag.
- Expect: never promoted to exact/alias and never inserted into hard_tags.
- Owner: danbooru-tag-gate

### P12-TAG-05 — character / IP isolation
- Input: a verified character anchor plus a plausible same-name general term.
- Expect: character identity requires character-group evidence; general wording cannot be upgraded.
- Owner: danbooru-tag-gate + classifier

### P12-TAG-06 — artist isolation
- Input: a verified artist token plus a similar-looking non-artist token.
- Expect: artist identity requires artist-group evidence.
- Owner: danbooru-tag-gate + classifier

## 2. Appearance / clothing / action / composite

### P12-TAG-07 — appearance classification
- Input: verified hair / face / appearance anchors.
- Expect: smallest defensible intent classes; no identity inference from spelling.
- Owner: visual-prompt-core

### P12-TAG-08 — clothing classification
- Input: verified layered garment and accessory anchors.
- Expect: clothing and accessory remain distinct; redundant items may become omit.
- Owner: visual-prompt-core

### P12-TAG-09 — action vs pose
- Input: one stable pose anchor and one event/action anchor.
- Expect: pose and action stay separate.
- Owner: visual-prompt-core

### P12-TAG-10 — composite tag packet
- Input: subject + identity + hair + clothing + accessory + pose + decorative extras.
- Expect: verified core/structural/signature survive before support/omit extras.
- Owner: classifier + skeleton + compressor

## 3. Special syntax / identity preservation

### P12-SYN-01 — Reverse:1999 canonical identity
- Input: 37_(reverse:1999)
- Expect serialized form exactly 37\(reverse1999\).
- Owner: anima-renderer

### P12-SYN-02 — ordinary tags stay ordinary
- Input: 1girl, long_hair, and another normal verified tag.
- Expect: no global escaping or unrelated rewriting.
- Owner: anima-renderer

### P12-SYN-03 — serialization idempotence
- Input: already serialized 37\(reverse1999\).
- Expect: serializing again produces the same string.
- Owner: anima-renderer

### P12-SYN-04 — punctuation is identity-sensitive
- Input: a tag containing parentheses / colon / underscore.
- Expect: validation does not silently normalize syntax before serialization.
- Owner: gate + serializer

## 4. Skeleton / compression

### P12-SKL-01 — what vs relation
- Input: finished blueprint with concrete anchors plus garment overlap, asymmetry and pose causality.
- Expect: stable facts go to Tag block; relations go to compact NL; no third visible block.
- Owner: visual-prompt-core

### P12-SKL-02 — no noun-pile replacement
- Input: multi-layer outfit with explicit hierarchy.
- Expect: NL contains a relational clause instead of repeating garment nouns.
- Owner: visual-prompt-core

### P12-CMP-01 — core survives compression
- Input: intentionally overlong prompt with identity, framing, signature garment, pose, critical relation and decorative prose.
- Expect: core facts survive; decorative prose is removed first.
- Owner: visual-prompt-core

### P12-CMP-02 — small prompts stay small
- Input: simple full-body character.
- Expect: no padding to hit a word count; stop at minimum sufficient control.
- Owner: compressor + compiler

### P12-CMP-03 — punctum survives
- Input: one explicit punctum and one strange detail.
- Expect: both remain visible design facts; generic decoration cannot replace them.
- Owner: compressor + aesthetic protection

## 5. Aesthetic protection / design drift

### P12-PRT-01 — no redesign during compilation
- Input: locked silver hair, gold eyes, asymmetric black garment architecture, fixed pose and palette.
- Expect: all locked facts survive unchanged.
- Owner: aesthetic protection + compiler

### P12-PRT-02 — asymmetry protection
- Input: blueprint intentionally weighted to one side.
- Expect: compression/serialization do not normalize it into bilateral symmetry.
- Owner: aesthetic protection

### P12-PRT-03 — quiet field protection
- Input: white-background character plate with one dense focal pocket.
- Expect: no automatic flowers, particles, ribbons, glow, butterflies, scenery or filler.
- Owner: aesthetic protection

## 6. P11 failure regression

### P12-FLR-01 — standalone module failure
- Expect: [card-only]; no memory reconstruction; unrelated loaded modules may continue.
- Owner: Kernel

### P12-FLR-02 — pipeline-pack failure
- Expect: [pipeline-unavailable]; no model-specific Anima prompt from unavailable stages.
- Owner: Kernel + Router

### P12-FLR-03 — Tag Index failure
- Expect: [tag-index-unavailable]; affected hard tags become unverified and route to NL.
- Owner: Tag Gate

### P12-FLR-04 — no silent stage skip
- Input: upstream Anima stage unavailable while compiler is named.
- Expect: pipeline never jumps directly to compiler.
- Owner: Router + compiler

## 7. Web-first / pipeline integrity

### P12-WEB-01 — cold start
- Input: fresh chat + repository URL only.
- Expect: current generated handshake; no stale hard-coded version/module count.
- Owner: Kernel + build

### P12-WEB-02 — one target prompt pack fetch
- Input: unfinished character idea + request for Anima prompt.
- Expect: declared Anima or NAI5 pipeline pack is selected as one fetch; constituent stages are loaded together.
- Owner: Router + Kernel

### P12-WEB-03 — shared stage order
- Expect: Visual Prompt Core → Danbooru Tag Gate → target renderer.
- Owner: harness.json + generated pipeline

### P12-WEB-04 — no redundant refetch
- Input: a second Anima request after the pack is loaded.
- Expect: no constituent refetch unless /reload <name> is explicit.
- Owner: Kernel

## 8. Real-task regression set

### P12-REAL-01 — modern gacha character
- Pass: strong silhouette + motion axis + asymmetric design + one punctum + local density pocket; no generic pretty-OC filler.
- Owner: director + character-design-engine + Anima pipeline

### P12-REAL-02 — full-body standing character
- Pass: full-body framing survives; prompt stays compact; pose/anatomy facts are not buried under atmosphere prose.
- Owner: character-design-engine + compiler

### P12-REAL-03 — high-fashion outfit
- Pass: garment architecture and physical attachment remain legible; tags do not flatten layering into a noun pile.
- Owner: character-design-engine + skeleton + compiler

### P12-REAL-04 — authored illustration
- Pass: illustration thesis, camera and environment-character relationship survive; image does not collapse to a character plate.
- Owner: illustration-direction + Anima pipeline

### P12-REAL-05 — reference-derived original
- Pass: transferable structure is extracted first; object renaming is not treated as originality.
- Owner: image-reverse-analysis + director

### P12-REAL-06 — prompt under token pressure
- Pass: secondary details disappear before identity, silhouette, garment architecture, action or punctum.
- Owner: compressor + compiler

## 9. P12 exit criteria

- [ ] exact / alias / missing / fuzzy / character / IP / artist covered
- [ ] appearance / clothing / action / composite packet covered
- [ ] special syntax has exact-output + idempotence checks
- [ ] Tag/NL boundary is tested
- [ ] compression tests deletion priority, not just word count
- [ ] aesthetic protection proves design facts survive compilation
- [ ] all three P11 failure scopes are exercised
- [ ] one-fetch Anima pipeline and shared stage order are exercised
- [ ] recent real tasks cover gacha / full-body / high-fashion / illustration / reference / token pressure
- [ ] deterministic P12 contract checker passes in CI
- [ ] no degraded path promotes unverified tags into hard_tags


## 10. Selective Tag Index Retrieval

### P12-WEB-TAG-01 — small lookup instead of full download
- Input: verify `white_background`, an artist tag, and a Reverse:1999 character anchor.
- Expect: read the manifest once, group candidates by source group/prefix, and fetch only the relevant shards.
- Fail: attempt to fetch the entire upstream `tags_index.json` into a web-model context.

### P12-WEB-TAG-02 — exact then alias
- Input: `long_hair` plus an exact source alias `long-hair`.
- Expect: canonical input is `exact`; alias input resolves to `long_hair` only after exact misses.
- Fail: fuzzy correction or a search result is treated as a verified alias.

### P12-WEB-TAG-03 — absent versus inaccessible
- Expect: a prefix absent from the source manifest may be `missing`; a manifest-listed shard that cannot be fetched is `unverified`.
- Fail: transport failure is reported as a nonexistent tag.

### P12-WEB-TAG-04 — duplicate alias
- Input: an alias mapping to multiple canonical tags in the same group.
- Expect: do not guess; mark it missing for hard-tag output and use natural language.


### P12-WEB-TAG-05 — namespaced artist sharding
- Input: verify `artist:starshadowmagician` in the upstream `artists` group.
- Expect: path prefix is derived from `starshadowmagician` after removing `artist:` for location only; exact identity remains `artist:starshadowmagician`.
- Fail: all artists are packed into one `ar.json` shard or the canonical tag is rewritten.
