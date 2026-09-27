---
name: creative-skill-router
description: Universal routing layer for creative tasks. Determines intent, loads identity and aesthetic context, then selects specialist skills.
priority: 1
---

# Creative Skill Router

## Purpose

Route user requests through the correct creative pipeline.

The router does not create final prompts. It coordinates:

User Intent -> Identity -> Aesthetic Direction -> Specialist Skill -> Model Adapter

## Core Rules

1. Creative tasks should not directly call model prompt skills.
2. User preferences override generic defaults.
3. Select skills by intent, not keywords.
4. Separate design decisions from model syntax.

## Pipeline

```
Request
 ↓
Task Classification
 ↓
Personal Identity Profile
 ↓
Aesthetic Director
 ↓
Specialist Skill
 ↓
Output Format
```
