# Anima Tag Classifier — P3 Acceptance Suite

P3 validates category assignment and filtering **after** P2 verification. It does not test tag discovery.

## Pass rule

Only P2-verified tags may enter this layer. Classification may change metadata such as intent or prompt role, but never the canonical tag string.

## Test matrix

| ID | Input state | Expected classification/filter | Acceptance |
|---|---|---|---|
| P3-01 | verified `1girl` | `subject / core` | retained |
| P3-02 | verified character-group identity | `identity_scope=character / core` | retained when blueprint locks identity |
| P3-03 | verified artist-group identity | `identity_scope=artist / core` | retained only when user/blueprint requests artist |
| P3-04 | verified series-group identity | `identity_scope=series / core` | retained only when series/IP is locked |
| P3-05 | same-looking token verified only in `general` | `identity_scope=none` | never promoted to identity |
| P3-06 | verified hair tag | `hair` | classified without rewriting |
| P3-07 | verified garment tag | `clothing` | classified as clothing, not generic appearance |
| P3-08 | verified held object | `prop` | classified as prop |
| P3-09 | verified stance tag | `pose` | classified as pose |
| P3-10 | verified event/interaction | `action` | classified as action |
| P3-11 | verified light-direction tag | `lighting` | classified as lighting |
| P3-12 | redundant decorative tag | `support` or `omit` | never automatically emitted |
| P3-13 | fuzzy/unverified candidate | outside verified packet | never classified into compiler hard tags |
| P3-14 | two overlapping verified synonyms | one retained, redundant one omitted | no tag pile |
| P3-15 | tag conflicts with locked blueprint fact | locked fact wins | classifier does not redesign blueprint |

## Filtering procedure

1. Start with P2-verified packet.
2. Assign intent and identity scope using the smallest defensible class.
3. Mark blueprint-critical identity/subject/framing facts as `core`.
4. Mark major garment/pose/spatial anchors as `structural`.
5. Mark deliberate visual puncta as `signature`.
6. Keep only useful `support` tags.
7. Omit redundant or decorative tags.
8. Pass the reduced packet to `anima-prompt-compiler`.

## P3 exit criteria

P3 is **PASS** only when:

- [ ] identity scope is isolated by verified source group;
- [ ] appearance/body/hair/face/clothing/accessory/prop/pose/action/expression/scene/background/lighting remain distinguishable;
- [ ] unverified tags cannot become classified hard tags;
- [ ] classification never rewrites canonical tag text;
- [ ] filtering removes redundant tag piles;
- [ ] core/structural/signature anchors survive filtering;
- [ ] classifier never changes blueprint design decisions;
- [ ] final packet remains within the existing compiler prompt budget.
