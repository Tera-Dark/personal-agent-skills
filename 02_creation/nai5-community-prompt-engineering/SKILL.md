---
name: nai5-community-prompt-engineering
description: Convert creative blueprints into NovelAI v5 community prompt format.
priority: 20
---

# NAI5 Community Prompt Engineering

## Purpose

Translate an already designed character or illustration concept into NAI5-compatible prompt structure.

This skill does not decide the artistic direction. It receives a creative blueprint from upstream layers.

## Pipeline

Creative Blueprint
↓
NAI5 Syntax Conversion
↓
Prompt Output

## Output Structure

- artist stack
- style modifiers
- character blocks
- scene tags
- negative section when needed

## Character Block

Preferred format:

char1:

- identity
- appearance
- clothing
- expression
- action

## Principles

Prioritize meaningful tags over keyword dumping.

Use weighting syntax only when it improves control.

Example:

0.7::artist:name::

Avoid adding generic quality words without purpose.
