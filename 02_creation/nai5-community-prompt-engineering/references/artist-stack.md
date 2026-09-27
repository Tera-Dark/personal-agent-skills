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

A good stack balances:

- character design
- rendering
- lighting
- illustration composition

Typical:

```
5-12 artists
0.25-1.5 weight
```

Always keep `artist collaboration` controlled when needed:

```
-1::artist collaboration::
```
