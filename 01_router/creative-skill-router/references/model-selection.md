# Model Selection Rules

## Purpose

Select the correct execution adapter after identifying the creative task.

## Principles

Do not choose a model based only on popularity.
Choose according to the communication style required.

## NAI5 (`nai5-community-prompt-engineering`)

Use when:

- tag-based control is preferred
- artist stack weighting is useful
- character blocks are clearly defined
- community prompt syntax is expected

Output:

Structured tags + weighted syntax.

## Anima (`anima-prompt-compiler`)

Use when:

- visual concepts are complex
- atmosphere and composition matter
- natural language is more effective

Output:

Natural visual description.

## General Image Models (`general-image-prompt-adapter`)

Use when:

- the target is Midjourney, DALL-E / GPT Image, Imagen / Gemini image, Flux, SDXL-style checkpoints, or unnamed
- scene understanding is primary
- conversational editing is needed
- less syntax control is required

Output:

Natural-language paragraph; parameters outside the prompt only when the target officially supports them; every model claim carries an evidence label.

## Unknown target

If the owner did not name a model and it affects the format, ask one question. Default to `general-image-prompt-adapter` in generic mode.

## Rule

The router selects the adapter.
The adapter does not redesign the concept.
