# Skill Development Guide

## Purpose

This document defines the standard for creating and maintaining skills in Personal Agent Skills.

The goal is to keep the system modular, understandable and scalable.

---

# Core Principle

One skill should solve one clear problem.

Avoid creating large mixed-purpose skills.

Bad:

```
Image generation skill
```

Good:

```
Character design skill
NAI5 prompt adapter
ComfyUI workflow skill
```

---

# Layer Separation

Skills should respect the following architecture:

```
Identity

↓

Creative Direction

↓

Planning

↓

Execution

↓

Technical Implementation
```

Do not put user preferences inside model adapters.

Do not put model syntax inside creative planning.

---

# Required Structure

Every skill should contain:

```
skill-name/

├── SKILL.md

└── references/
```

---

# SKILL.md Requirements

Every skill should define:

```yaml
name:
description:
priority:
trigger:
input:
output:
dependencies:
```

---

# References

Use reference files for:

- detailed knowledge
- examples
- rules
- templates
- domain information

Keep the main SKILL.md focused on execution logic.

---

# Dependency Rules

Higher-level skills provide decisions.

Lower-level skills provide execution.

Example:

```
Character Design
        ↓
NAI5 Prompt Engineering
```

NAI5 should not redesign the character.

It only translates the existing concept into NAI5 syntax.

---

# Quality Checklist

Before adding a new skill:

- Does this solve a unique problem?
- Does it overlap with existing skills?
- Is the input/output clearly defined?
- Can another skill use it as a dependency?
- Does it improve the overall agent workflow?
