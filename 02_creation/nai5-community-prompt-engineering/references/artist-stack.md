# NAI5 Artist Stack Engineering

## Purpose

Guide weighted artist mixing for NovelAI V5 community prompts.

Format:

```
0.6::artist:name::
```

## Principles

Artist tags are not decoration. They influence:
- line quality
- color language
- composition
- character design feeling

Avoid blindly stacking famous artists.

### Default random-mix habit

When the user provides an artist pool and asks for a random artist stack:

- Randomly select **4–6 artists by default**.
- Use a clear hierarchy rather than equal-strength blending.
- Suggested starting range:
  - primary artist: `0.5–0.6`
  - secondary artist: `0.4–0.5`
  - remaining artists: `0.25–0.4`
- Keep the combined artist influence roughly around `1.5–2.0` unless the user explicitly asks for aggressive blending.
- If the selected artists have strongly conflicting visual languages, reduce the number of artists rather than increasing weights.
- Do not turn a user-supplied pool into a 10+ artist stack merely because many artists are available.

### Preserve user syntax

If the user's pool contains escaped tags, wildcards, parentheses, suffixes, or unusual syntax, preserve them exactly unless the user explicitly asks for normalization. Do not silently rewrite a tag into a different artist identifier.

If an entry contains an obvious malformed or ambiguous trailing weight/value, do not guess its intended meaning and push it into a high-weight stack. Prefer skipping it or using it only after the user clarifies.

A good stack balances:

- character design
- rendering
- lighting
- illustration composition

The stack supports the blueprint; it does not replace character or composition design.

Always keep `artist collaboration` controlled when needed:

```
-1::artist collaboration::
```
