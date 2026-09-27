# Personal Agent Skills Architecture

## Overview

Personal Agent Skills is designed as a layered creative intelligence system.

The system separates:

- identity
- aesthetic judgment
- creative planning
- execution
- technical adaptation

The goal is not only producing outputs, but producing outputs consistent with the creator's creative vision.

---

# System Architecture

```
User Request

↓

Identity Layer

↓

Creative Direction Layer

↓

Planning Layer

↓

Execution Skill

↓

Model Adapter

↓

Output
```

---

# Layer 0: Identity Layer

Location:

```
00_core/personal-identity-profile
```

Purpose:

Understand who the creator is.

Contains:

- aesthetic preferences
- dislikes
- business goals
- workflow style

Question answered:

"What kind of creator is this for?"

---

# Layer 1: Creative Direction Layer

Location:

```
00_core/aesthetic-director-core
```

Purpose:

Transform requests into creative decisions.

Responsibilities:

- understand artistic intent
- define emotional direction
- establish visual identity
- remove artificial randomness

Question answered:

"Why should this artwork exist?"

---

# Layer 2: Planning Layer

Purpose:

Create a design blueprint before generation.

Character design flow:

```
identity

↓

silhouette

↓

costume

↓

emotion

↓

pose
```

Illustration flow:

```
theme

↓

composition

↓

lighting

↓

environment
```

Question answered:

"What should be created?"

---

# Layer 3: Execution Layer

Location:

```
02_creation/
```

Responsible for model-specific expression.

Examples:

NAI5:

- weighted tags
- artist stack
- character blocks

Anima:

- natural language
- composition-first prompting

Question answered:

"How does this model understand the idea?"

---

# Layer 4: Technical Layer

Location:

```
04_tools/
```

Responsible for:

- ComfyUI
- LoRA
- datasets
- workflows

Question answered:

"How do we implement it?"

---

# Execution Flow

Example:

User:

"Design a fantasy girl"

System:

1. Read personal-identity-profile

2. Run aesthetic-director-core

3. Generate creative blueprint

4. Select specialist skill

5. Adapt to target model

6. Output final result

---

# Priority Rules

Higher layers override lower layers.

Priority:

```
Identity

>

Aesthetic Direction

>

Creative Planning

>

Model Syntax

>

Raw Prompt Keywords
```

A technically correct prompt is not acceptable if it violates creative direction.
