---
name: danbooru-tag-gate
description: Web-first validation boundary for Danbooru-derived hard tags shared by Anima and NAI5 workflows. Resolves exact canonical tags, exact aliases, or missing without fuzzy promotion. Use whenever a prompt packet needs verified Danbooru identity.
metadata:
  author: Tera-Dark
  version: "1.2.0"
  layer: "03_prompt"
  load: "on-demand"
  status: "active"
  triggers: "Danbooru tag, tag validation, tag check, exact tag, alias, tag verification"
---

# Danbooru Tag Gate

## 定位

输入：visual-prompt-core 标记的 tag candidates。
输出：共享 verified tag packet，供任意 renderer 消费。

上游：visual-prompt-core 或模型适配流程中的 tag candidates
下游：anima-renderer / nai5-renderer
不做：不设计、不选择 artist、不进行 fuzzy matching、不负责目标模型语法。

## 数据源

Primary Web-first source:

https://raw.githubusercontent.com/ShiroEirin/comfyui-good-anima/main/danbooru-tags/tags_index.json

数据结构按 group 保存 canonical tag、count、aliases。Count 只作证据元数据，不参与创意排序。

## Gate 状态

每个 candidate 只能得到一个状态：
- exact — 输入就是该 group 的 canonical tag。
- alias — 输入精确命中该 group 的 alias，返回 canonical tag。
- missing — exact / alias 均未证明。

永远不要把以下内容升级成 hard tag：
- fuzzy similarity
- search-engine suggestion
- semantic guess
- model memory
- 看起来像 tag 的自然语言

## Lookup

1. 只做 transport-level normalization：首尾空白、意外重复空格。
2. 先查指定 group 的 exact canonical。
3. 未命中再查同 group 的 exact alias。
4. alias 命中时保留 alias trace，同时以 canonical 为最终身份。
5. 否则标记 missing。
6. 不修改 underscore、parentheses、colon、slash 等可能有身份意义的字符。

## Group / identity

身份范围必须来自证据，而不是字符串长相：
- artist → artist
- character → character
- series → series
- visual tag → general / 对应语义组

尤其是 character / series / artist：
- 不得跨 group 猜测；
- 不得因为名字相似而替换身份；
- 用户指定 artist 时，不得擅自换成更流行的 artist。

## Renderer boundary

Gate 只提供：
input
group
status
canonical
matched_alias
source

不要在这里做：
- Anima syntax escaping
- NAI5 weight syntax
- NAI5 char1 / source# / target# / mutual#
- renderer-specific ranking

Canonical identity 永远保持原值。

## Failure

如果 Web source 不可读、结构异常或无法证明 lookup：
- affected tag → unverified
- 禁止 hard tag emission
- renderer 可把含义退回自然语言或普通描述
- 不用记忆替代证据
- 不进行 fuzzy fallback

故障标签只有在确实影响输出时才暴露给用户。

## 最小选择

验证“存在”不等于“应该输出”。Gate 不得增加 prompt budget。最终是否保留 tag，由 shared prompt planning 和 renderer 的选择规则决定。

## 输出契约

input:
group:
status: exact | alias | missing
canonical:
matched_alias:
source: danbooru-index

## 自检

- [ ] exact / alias / missing 逻辑严格。
- [ ] 不做 fuzzy promotion。
- [ ] canonical identity 未被改写。
- [ ] 不包含任何 Anima / NAI5 独占语法。
- [ ] source failure 时 fail-closed。
