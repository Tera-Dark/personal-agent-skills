# Model Selection Rules

## Purpose

Select the execution adapter only after the creative artifact passes the Aesthetic Gate and Blueprint Gate.

## NAI5

Use when tag-based control, weighted artist stacks, and NovelAI V5 community syntax are desired.

Pipeline:
identity → Aesthetic Gate FULL/AUDIT → type specialist when needed → Blueprint Gate → nai5-community-prompt-engineering

Output:
compact weighted community tags using the NAI5 canonical skeleton.

## Anima

Use when complex visual concepts, atmosphere and natural-language relationships are important.

Pipeline:
identity → Aesthetic Gate FULL/AUDIT → type specialist when needed → Blueprint Gate → anima-prompt-compiler

Output:
Anima Tag Lock + Natural-language Relations.

## General Image Models

Use for Midjourney, DALL-E / GPT Image, Imagen / Gemini image, Flux, SDXL-style checkpoints or unnamed targets.

Pipeline:
identity → Aesthetic Gate FULL/AUDIT → type specialist when needed → Blueprint Gate → general-image-prompt-adapter

## Unknown target

If the target model changes the required prompt format, ask one question. Otherwise default to generic mode.

## Rule

The adapter is the final compiler. It never decides the concept.
