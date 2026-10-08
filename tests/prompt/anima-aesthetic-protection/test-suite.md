# P7 Anima Aesthetic Protection — Acceptance Suite

## P7-01 — protected packet exists

Before final Anima compilation, the blueprint exposes its thesis, macro silhouette, focal hierarchy, major spatial decisions, signature construction and locked facts.

## P7-02 — translation only

Changing a long phrase into a shorter equivalent is allowed when visual meaning is unchanged.

Example:

`the open coat falls over the fitted inner layer`
→ `open coat over fitted inner layer`

## P7-03 — silhouette lock

A distinctive silhouette element cannot be deleted merely because it costs tokens.

## P7-04 — asymmetry lock

Explicit left/right asymmetry must survive compression. `asymmetrical outfit` is not an acceptable replacement when the side distribution is part of the design.

## P7-05 — composition lock

A deliberately offset, cropped, framed or scale-contrasted composition must not be normalized into centered full-body presentation.

## P7-06 — focal hierarchy lock

The main punctum survives. Compression cannot introduce a second competing punctum.

## P7-07 — atmosphere restraint

Prompt processing must not add generic flowers, particles, butterflies, glow, ribbons, decorative framing or other filler that was absent from the blueprint.

## P7-08 — environment relation

If the environment is part of the composition's structure, its relationship to the character survives even when decorative environment nouns are removed.

## P7-09 — palette hierarchy

Base / structural / accent color hierarchy survives. Compression may shorten wording but cannot flatten intentional color contrast.

## P7-10 — material identity

A defining material contrast survives. Generic `beautiful fabric` cannot replace a specific structural material relationship.

## P7-11 — model-fashion bias rejection

Do not change a design because another composition or prompt convention is more common for the model.

## P7-12 — minimality boundary

Delete until the next deletion would alter a protected design decision, then stop.

## P7-13 — drift failure

If the final prompt changes subject, framing, silhouette, asymmetry, focal hierarchy, key action or design grammar, mark `design_drift` rather than silently rewriting the blueprint.

## P7-14 — pipeline boundary

Accepted order:

Design Gate → Tag Gate → Classifier → Skeleton → Aesthetic Protection → Compressor → Serializer → Compiler

Protection audits; it does not create new design.

## P7 Exit Criteria

- [ ] Prompt optimization cannot silently redesign the image.
- [ ] Key aesthetic decisions are explicitly protected.
- [ ] Compression stops at the design boundary.
- [ ] Generic model conventions cannot override locked design.
- [ ] Design drift becomes a failure state, not an opportunity for invention.