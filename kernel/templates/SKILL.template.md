---
name: example-module-name
description: One sentence on what this module does. Use when the user asks for X, mentions Y, or says 触发词A, 触发词B. Does not do Z (state the boundary; adapters must say "Does not design").
metadata:
  author: Tera-Dark
  version: "0.1.0"
  layer: "06_extensions"
  load: "on-demand"
  status: "active"
  triggers: "触发词A, 触发词B, keyword-c, keyword-d"
---

# Example Module Name

## 定位

输入：<what this module receives — a request? a blueprint? an image? a prompt?>
输出：<what it emits — the exact artifact>
上游：<which module usually runs before this one>
下游：<which module consumes its output>
不做：<explicit boundary. Adapters: 只翻译，不设计；收到的不是 blueprint 就退回 aesthetic-director-core。>

## 硬规则

- MUST …
- MUST NOT …
- 任何关于外部模型 / 工具行为的断言带证据标签：`[Official]` `[Community]` `[Personal experiment]` `[Unverified]`。

## 执行流程

```
Step 1  <决定 A>        <它依据什么>
Step 2  <决定 B>        <由 Step 1 推出>
Step 3  <决定 C>        …
Step N  自检            见下
```

## 输出契约

```
<exact shape: fields / table / code block format>
<creative modules must include: 删掉的 / 否决的方向>
```

## 自检

- [ ] <check 1>
- [ ] <check 2>
- [ ] 输出符合契约，没有多余解释？

## References

<!-- One line per file that actually exists in this module's references/ folder, written as
     - backtick references/FILENAME.md backtick — what knowledge lives there
     Every backticked references/ path MUST exist (the validator checks). If this module has no
     references, delete this whole section. -->
