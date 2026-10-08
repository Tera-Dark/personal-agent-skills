# P5 Anima Prompt Skeleton — Acceptance Suite

## P5-01 — two-part output remains stable

Given a finished blueprint, the user-visible structure remains:

Tag block

Natural-language block

No standalone third soft_phrases block is emitted.

## P5-02 — hard anchor separation

Concrete verified identity / subject / clothing / prop facts belong in Part A when they are blueprint-relevant.

A relational sentence such as:

the open coat falls over the fitted inner layer

belongs in Part B rather than being decomposed into a tag pile.

## P5-03 — soft phrase restraint

A compact phrase such as quiet editorial styling may survive when useful.

Generic quality phrases such as masterpiece, best quality, ultra detailed must not enter the skeleton.

## P5-04 — hierarchy relation survives

If the blueprint specifies open outer coat → fitted inner layer → asymmetric skirt, Part B must preserve the hierarchy rather than flattening it into three clothing nouns.

## P5-05 — spatial relation survives

A tag packet cannot replace a blueprint relation such as the ribbon trails behind the head from the left shoulder. The relation remains in NL.

## P5-06 — asymmetry survives

Explicit left/right or front/back asymmetry remains in NL.

The skeleton must not collapse right-side ornament cluster + left side plain into vague wording such as asymmetric outfit.

## P5-07 — pose causality survives

The skeleton preserves visible consequences: the raised arm pulls the sleeve upward while the skirt swings with the turn.

Do not reduce this to dynamic pose.

## P5-08 — missing tag degradation

A missing hard tag concept is translated into NL rather than fabricated into Part A.

## P5-09 — duplicate removal

If a clothing tag already fixes the garment identity, NL should describe hierarchy/placement instead of repeating the same garment name multiple times.

## P5-10 — compression

Under a tight token budget:

identity + framing + signature
> structural relation
> supporting material detail
> secondary accessory
> decorative background detail

Compression must not remove blueprint-locked facts or the punctum.

## P5-11 — no design drift

Skeleton generation cannot add an unrequested accessory, garment, background object, or character trait.

## P5-12 — pipeline boundary

Accepted order:

Gate → Classifier → Skeleton → Serializer → Compiler

The skeleton cannot verify tags or perform Anima syntax escaping.

## P5 Exit Criteria

- [ ] Two-part user-visible structure preserved.
- [ ] Good Anima hard/soft/NL separation absorbed without copying its three-block surface format.
- [ ] Tags answer stable facts; NL answers relations.
- [ ] Relation and causality survive compression.
- [ ] Generic quality language stays excluded.
- [ ] Missing anchors degrade to NL.
- [ ] No design drift.
- [ ] No token-budget expansion caused by the skeleton itself.
