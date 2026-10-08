# 06_extensions

Owner 通过聊天新增的、放不进 00–05 层的模块（"杂七杂八"）。

- 每个模块一个目录：`06_extensions/<name>/SKILL.md`（+ 可选 `references/`）。
- 结构与其它层完全一致；模板在 `kernel/templates/`，规则在 `kernel/EXTENSION-PROTOCOL.md`。
- 提交后 CI 会校验（`scripts/validate_skills.py`）并重建 `bundle/`，新模块自动进入索引。
- 长大了、职责清楚了，就移到对应的语义层；移动只需改 `metadata.layer` 和目录位置。

目前为空。
