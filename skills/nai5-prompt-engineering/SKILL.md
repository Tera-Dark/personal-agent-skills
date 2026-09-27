---
name: nai5-prompt-engineering
description: Expert NovelAI V5 Community Prompt Compiler. Creates weighted artist stacks, style layers, character blocks, interaction prompts and negative steering using community-style NAI5 workflows.
metadata:
  author: Tera-Dark
  version: "2.0.0"
---

# NAI5 Community Prompt Engineering

## Purpose

Generate NovelAI V5 prompts using the community prompt format instead of generic natural language prompting.

This skill focuses on:
- weighted artist stack construction
- global style and rendering layers
- character block formatting
- multi-character interaction tags
- negative steering
- reverse prompt analysis

## Core Prompt Architecture

Default structure:

```
[Artist Stack]

[Global Style Layer]

[Scene Base]

char1:

...

char2:

...

Negative:

...
```

## Artist Stack

Use weighted artist mixing when appropriate:

```
0.6::artist:name::
```

Rules:
- combine multiple artists for different visual contributions
- avoid random artist dumping
- consider lineart, color, composition and character design separately
- normal range: 5-12 artists
- typical weight range: 0.25-1.5

## Global Style Layer

Separate style control from character data.

Common layers:

Quality:
- masterpiece
- best quality
- very aesthetic
- amazing quality

Complexity:
- high complexity
- ultra complexity
- intricate details

Rendering:
- color shading
- cinematic lighting
- depth of field
- global illumination
- ambient occlusion

## Character Block

Always prefer character separation:

```
char1:
girl, identity, appearance, clothing, action
```

Order:
1. gender
2. character identity
3. hair
4. eyes
5. expression
6. outfit
7. accessories
8. action

## Interaction Tags

For multiple characters use:

- source#
- target#
- mutual#

Do not mix character actions into one block.

## Negative Steering

Negative prompts should control style and failure modes.

Examples:

Avoid monochrome:
```
-3::monochrome::
```

Avoid old styles:
```
-3::2000s (style)::
```

Avoid flat rendering:
```
-2::flat color::
```

## Reverse Analysis Workflow

When analyzing reference images:

1. identify composition
2. identify silhouette
3. identify palette
4. identify costume structure
5. identify materials
6. identify style direction
7. compile into NAI5 format

## Personal Aesthetic Rules

Prioritize:
- female-oriented character design
- high fashion costume logic
- elegant silhouette
- layered materials
- meaningful accessories

Avoid by default:
- random watches
- unnecessary cyberpunk
- excessive mechanical elements
- random weapons
- meaningless accessories

Accessories must support character identity.

## Output Rule

When user requests NAI5 prompts, output Community Pack style format by default.
Do not use long MJ-style natural language descriptions unless explicitly requested.
