# NAI5 Style and Render Layer

## Global Style + Quality Layer

Place global visual direction before character blocks, while keeping the main subject and framing in the front half of the prompt.

## Quality / Aesthetic

NovelAI's V5 Full Quality Tags include:
`very aesthetic, masterpiece, no text`

Its Light quality preset includes:
`very aesthetic, amazing quality, no text`

Official Prompt Tips also recommend `very aesthetic`, `best quality`, and `high quality` when a generation lacks quality.

Common community quality tokens:
```
masterpiece
best quality
high quality
very aesthetic
amazing quality
absurdres
highres
best illustration
```

Use a coherent subset rather than mechanically stacking every synonym. The goal is a strong quality prior plus the intended visual language.

## Complexity

V5 supports:
```
low complexity
medium complexity
high complexity
ultra complexity
```

For dense premium character illustration, `high complexity` is a sensible starting point. Use `ultra complexity` when the blueprint genuinely calls for very high visual density.

Supporting terms:
```
high detail
intricate details
fine details
```

## Rendering / Material

Choose rendering terms that reinforce the intended look:
```
detailed shading
smooth gradients
realistic texture
anime coloring
painterly
ligne claire
cinematic lighting
depth of field
ambient occlusion
global illumination
```

Avoid contradictory rendering directions simply because each is individually “high quality”.

## Style Suppression / Control

Use targeted negative numerical emphasis when a known style conflict needs suppression:
```
-2::simple illustration::
-5::artist collaboration::
-1::censored::
```

This is control, not a substitute for positive design.

## Prompt Order

A practical structure:
```
subject + framing,
year / era,
weighted artist stack,
quality + aesthetic,
complexity,
rendering,
targeted style control,
scene / environment,
character detail,
expression / clothing / pose,
optional quality tail / no text
```

NovelAI explicitly notes that prompt order matters and recommends keeping the most important information in the front half.

## Principle

Quality tags establish the generation's quality/aesthetic prior; complexity controls density; rendering terms define the material/light treatment; artist tags establish a style prior. None of these replace the underlying character and composition blueprint.
