# Execution Flow

## Standard Pipeline

```
User Request
    ↓
Task Classification
    ↓
Identity Context
    ↓
Aesthetic Direction
    ↓
Creative Planning
    ↓
Skill Selection
    ↓
Model Adapter
    ↓
Evaluation Loop
```

## Rules

1. Understand before generating.
2. Create design decisions before writing prompts.
3. Keep model syntax isolated from creative reasoning.
4. Always allow evaluation and iteration.

## Failure Recovery

If output quality is poor:

- do not immediately add more keywords
- inspect concept, composition, emotion, and identity first
- revise the correct layer
