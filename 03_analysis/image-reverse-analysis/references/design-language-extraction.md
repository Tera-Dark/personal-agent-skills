# Design Language Extraction — 反推要点

> 从 `skills/nai5-prompt-engineering/references/reverse-image-analysis.md` 迁入（v2.0.0）。与模型无关。完整分析顺序见本 Skill 的 SKILL.md；本文件是各步骤的提取要点。

## Analysis Pipeline

Reference image -> design language -> prompt

Analyze:

## 1. Silhouette

Find the strongest visual identity:
- hairstyle
- clothing outline
- unique shape
- pose

## 2. Color Language

Identify:
- main color
- secondary color
- accent color

## 3. Fashion Structure

Break down:
- garment type
- layering
- fabric
- embroidery
- accessories

## 4. Mood

Convert emotion into visual language:

Example:
melancholic moon fantasy

becomes:
moonlight, soft expression, flowing fabric, quiet atmosphere

## 5. Reconstruction

Create an original design inspired by principles, not a direct copy of the image.
