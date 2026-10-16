# MOSS-Image JSON Layout · 正式提示词与草稿区别

[Official] 参考：
- https://github.com/OpenMOSS/MOSS-Image/blob/main/USERGUIDE_ZH.md
- https://github.com/OpenMOSS/MOSS-Image/blob/main/skills/moss-image-prompt-enhancer/references/layout.md

## 选择

有明确 **多块文字/多对象相对位置/分镜版式/精确海报布局** 才使用 Layout。普通摄影或人物情绪图用 Caption；复杂场景不自动代表 Layout。它是实验性排版控制，不能保证每个字绝对准确。

## A. 可编辑的 Layout 草稿（给人和编译器，不直接给模型）

`{
  "width": 1024,
  "height": 1024,
  "bbox_coord_space": "abs",
  "bbox_format": "xyxy",
  "summary": {
    "meta": ["album cover"],
    "canvas": "single",
    "caption": "A quiet blue-grey lo-fi album cover with a hand-drawn anime girl and photographic residential street."
  },
  "items": [
    {"label": "character", "caption": "A shy anime schoolgirl wearing a cream cardigan, on the left side.", "bbox": [80, 240, 500, 900]},
    {"label": "text", "caption": "Large off-white uppercase album title in the open upper-right area.", "text": "AFTER SCHOOL", "bbox": [544, 160, 940, 288]}
  ]
}`

- 左上角是 (0,0)，单位实际像素，`bbox=[x_min,y_min,x_max,y_max]`；
- `width/height` 必须为 16 的正整数倍，和生成设置一致；不提供兼容尺寸时先向用户说明。
- 纯 Caption 草稿 `{"caption":"..."}` 编译后是 **Caption 字符串**，不是包着 JSON 的模型输入。

## B. 必须编译为模型接受的 Layout

- 模型格式：`bbox_coord_space:"abs_centralized"` 和 `bbox_format:"yxyx"`。
- 模型每个 item `bbox=[y_min-H/2,x_min-W/2,y_max-H/2,x_max-W/2]`，按先 y 后 x 排序。
- 上述少女 `[80,240,500,900]` 在 1024×1024 下变为 `[-272,-432,388,-12]`；标题 `[544,160,940,288]` 变为 `[-352,32,-224,428]`。
- 模型提示词最终顶层只保留 `summary`、`items`、`bbox_coord_space`、`bbox_format`；`width` / `height` 不在最终 JSON 中。
- 必须校验画幅边界、box 正面积、文本是否完整和主体是否适配框；多面板用 `summary.canvas:"multi_panel"`，但不能让每个元素随意跨格。
- 对需要严格文字的作品，保留 `text` 中的原语言和换行，且字体大/小由实际画幅预留空间决定。

## 编译

推荐使用官方兼容工具（纯 Python 标准库）：
- 项目集成：`python3 scripts/moss_layout.py draft.json --output ready.txt`。
- 官方 enhancer 脚本：`https://github.com/OpenMOSS/MOSS-Image/blob/main/skills/moss-image-prompt-enhancer/scripts/compile_prompt.py`。

Web-first 环境没有 shell 时：
1. 若元素很少、整数边界明确，可以严格对照上面公式组成正式 yxyx JSON，并自检每一个坐标。
2. 无法计算/验证精度时，交付 Caption，说明未提供受检 Layout；**绝不能假装 xyxy 草稿是可用输入**。
3. 不修改用户指定的文字内容、行距或布局意图以“凑坐标”。

## 与 NAI5 的界限

`character 1:`、`character 2:`、`source#`、单字符串 `|`、NAI5 权重均不是 MOSS JSON Layout。多人 Layout 通过分配不同 character items 实现相对位置（仍要说明彼此关系）。
