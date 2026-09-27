# Personal Agent Skills Hub

> Personal AI Creative Operating System
>
> 面向长期创作工作流的模块化 Agent Skill 仓库。
> 目标：让 AI 不只是执行提示词，而是先理解创作意图，再完成设计、分析与模型适配。

---

## Architecture

```text
User Intent
    |
    v
00_core
Identity + Aesthetic Direction
    |
    v
01_router
Task Classification & Skill Routing
    |
    v
02_creation
Creative Production Skills
    |
    v
03_analysis
Reverse Engineering & Evaluation
    |
    v
04_tools
Workflow Implementation
```

核心原则：

- 设计决策与模型语法分离
- 用户审美优先于通用模板
- Skill 负责流程，references 负责知识
- 不让单个 Skill 承担全部职责

---

## Repository Structure

```text
.
├── 00_core/
│   ├── personal-identity-profile/
│   └── aesthetic-director-core/
│
├── 01_router/
│   └── creative-skill-router/
│
├── 02_creation/
│   ├── character-design-engine/
│   ├── illustration-direction/
│   ├── nai5-community-prompt-engineering/
│   └── anima-prompt-engineering/
│
├── 03_analysis/
│   ├── image-reverse-analysis/
│   └── prompt-analysis/
│
├── 04_tools/
│   ├── comfyui-workflow/
│   ├── lora-training/
│   └── dataset-management/
│
└── docs/
```

---

## Skill Responsibilities

### Core

负责：

- 用户长期偏好
- 审美方向
- 创作判断标准

### Router

负责：

- 判断任务类型
- 调用正确 Skill
- 保证执行顺序

### Creation

负责：

- 角色设计
- 插画规划
- NAI5 Prompt 编译
- Anima Prompt 编译

### Analysis

负责：

- 图片拆解
- Prompt 分析
- 视觉语言提取

### Tools

负责：

- ComfyUI 工作流
- LoRA 训练
- 数据集管理

---

## Design Philosophy

传统 AI 工作流：

```text
需求 -> Prompt -> 生成
```

本项目采用：

```text
需求
 ↓
理解
 ↓
设计蓝图
 ↓
模型适配
 ↓
生成
```

Prompt 不是设计本身，而是设计思想与模型之间的沟通语言。

---

## Extension Guide

新增 Skill 时：

1. 创建独立目录
2. 使用 SKILL.md 定义职责
3. 将详细知识放入 references/
4. 避免跨层职责污染

推荐结构：

```text
skill-name/
├── SKILL.md
└── references/
```

---

## Documentation

- `docs/architecture.md` - 系统架构
- `docs/project-map.md` - 项目地图
- `docs/skill-development-guide.md` - Skill 开发规范

---

## License

MIT License
