# P4 Anima Tag Serializer — Acceptance Suite

## Purpose

Verify that canonical Danbooru/Anima identities remain unchanged through verification and classification while final Anima syntax is serialized only by explicit rules.

## P4-01 — Reverse:1999 special case

Input:

```text
canonical_tag = 37_(reverse:1999)
status = verified
prompt_role = core
```

Expected:

```text
serialized_tag = 37\\(reverse1999\\)
canonical_tag = 37_(reverse:1999)
serialization_status = verified
```

## P4-02 — ordinary subject tag unchanged

```text
1girl → 1girl
```

No transform record is required.

## P4-03 — ordinary underscore unchanged

```text
long_hair → long_hair
white_background → white_background
```

The serializer must not remove underscores globally.

## P4-04 — punctuation is not globally escaped

A non-registered tag containing parentheses, a colon, or a slash remains unchanged. The serializer must not infer a new syntax rule from punctuation alone.

## P4-05 — no token splitting

`37_(reverse:1999)` must serialize as one token. The output must never become separate tokens for `37`, `reverse`, and `1999`.

## P4-06 — canonical immutability

After serialization:

```text
result.canonical_tag == input.canonical_tag
```

For the special case, canonical remains `37_(reverse:1999)`.

## P4-07 — idempotence

```text
serialize("37_(reverse:1999)")
  = "37\\(reverse1999\\)"

serialize("37\\(reverse1999\\)")
  = "37\\(reverse1999\\)"
```

No double escaping is allowed.

## P4-08 — mixed tag packet

Given:

```text
1girl
37_(reverse:1999)
long_hair
white_background
```

Only the registered `37_(reverse:1999)` rule is transformed. All other tags remain unchanged.

## P4-09 — alias boundary

Alias resolution happens in P2. The serializer receives the canonical result, not an alias. It must not perform alias lookup or substitute an identity itself.

## P4-10 — unverified input rejected

A tag with `status=unverified`, `missing`, fuzzy candidate, or semantic guess must never become a serialized hard tag.

## P4-11 — omit boundary

A classifier result with `prompt_role=omit` must not be serialized into the compiler's hard-tag block.

## P4-12 — pipeline order

The only accepted order is:

```text
Gate → Classifier → Serializer → Compiler
```

Serializer must not run before identity verification or classification.

## P4-13 — unknown syntax fails closed

When an apparently syntax-sensitive tag has no explicit registered rule, do not guess. Preserve the canonical value internally and mark serialization as unverified; use the compiler's NL fallback when necessary.

## P4 Exit Criteria

- [ ] Exact `37_(reverse:1999)` → `37\\(reverse1999\\)`.
- [ ] Ordinary tags are preserved.
- [ ] No global punctuation escaping.
- [ ] No token splitting.
- [ ] Canonical identity remains immutable.
- [ ] Serialization is idempotent.
- [ ] Alias resolution remains P2 responsibility.
- [ ] Unverified and omitted tags cannot enter hard-tag serialization.
- [ ] Unknown syntax fails closed.
- [ ] Pipeline order is Gate → Classifier → Serializer → Compiler.
