# Anima User Aesthetic Profile

> Purpose: provide a living, adjustable preference model for generating Anima prompts for this user. This is not a rigid style preset. It should be updated from explicit feedback, reference images, accepted outputs, and rejected outputs.

## 1. User profile summary

The user creates anime-style female-oriented OC designs, game-style character illustrations, fashion concepts, and promotional visuals. The desired result is not merely a pretty image or a list of clothing tags: it should feel like a deliberately art-directed character design with a memorable silhouette, coherent motif system, controlled visual hierarchy, and production-ready prompt language.

Primary use cases:

- female-oriented OC character design
- modern gacha / game illustration aesthetics
- white-background character plates with selective decorative elements
- simple-background key visuals and atmospheric scene illustrations
- fashion/editorial character portraits
- reference-driven visual design extraction
- Anima-compatible Tag + Natural Language prompts

## 2. High-confidence aesthetic preferences

### 2.1 Design before decoration

The user strongly prefers genuine OC design over a generic role-and-prop combination. Every open-ended OC should have:

- a concise design thesis
- a recognizable silhouette visible at a distance
- a unified motif or shape language
- a clear primary visual anchor
- intentional distribution of visual mass
- clothing with actual construction and cut, not just named garments
- an action that explains the position and movement of costume elements
- a restrained, purposeful palette

Avoid treating `profession + ordinary outfit + one prop + dramatic lighting` as a complete design.

### 2.2 Reference-led analysis

When the user provides a reference image, analyze the actual image rather than replacing it with web-search images or generic style assumptions. Extract and preserve the design logic:

- outer silhouette and large masses
- ornament concentration and visual center of gravity
- recurring motif grammar
- relationship between body, clothing, and non-human structures
- material contrast
- palette hierarchy
- pose and prop interaction
- negative space and presentation format

Borrow structural principles, not specific copyrighted character identity, logos, or exact composition unless the user explicitly asks for faithful adaptation.

### 2.3 Preferred visual language

The user's recurring preferences include:

- contemporary gacha-game character design sensibility
- fashion-aware, designer-like construction
- asymmetry with a clear reason
- compact but distinctive ornament systems
- pale or controlled base colors with carefully placed dark or saturated accents
- elegant, slightly strange, fantasy or symbolic elements
- clear white/ivory presentation backgrounds when requested
- visual breathing room rather than uniformly busy surfaces
- natural material behavior, readable folds, reflections, translucency, and shadow falloff
- cinematic or editorial composition when the image is intended as an illustration rather than a neutral character plate
- reduced “AI-generated” feeling through specific physical relationships and controlled imperfection

These are tendencies, not mandatory ingredients for every prompt.

## 3. Negative preference profile

Do not default to:

- generic gothic fashion without a unique structural idea
- random cyberpunk, mechanical, steampunk, butterfly, rose, magic-circle, or glowing-particle decoration
- excessive accessories spread evenly over the entire body
- a costume made only from adjectives such as `ornate`, `luxurious`, `intricate`, or `elegant`
- generic “mysterious beautiful girl” concepts
- empty white backgrounds with unrelated petals, particles, symbols, or light effects
- overused cinematic words without concrete lighting or spatial behavior
- overly symmetrical designs when asymmetry would improve recognition
- noisy maximalism that obscures face, hands, silhouette, or clothing construction
- excessive quality tags, weights, negative prompts, or model parameters unless explicitly requested
- changing the user's locked character identity, costume facts, or color scheme for the sake of stylistic enhancement

## 4. Reference image calibration: provided serpent character example

The user's provided reference demonstrates a preferred direction for high-density OC character plates:

- a large, immediately recognizable serpentine radial silhouette around the character
- multiple related biological forms functioning as one design system
- a white and pale-gray foundation with restrained cool accents
- non-human structures integrated with the clothing and pose instead of appearing as unrelated props
- concentrated visual density around the head, torso, hands, and surrounding creature forms
- a seated, interactive pose that gives the appendages believable spatial placement
- a clean white presentation field that still feels designed through silhouette, grounding, and selective graphic details
- a balance between eerie, elegant, delicate, and slightly dangerous qualities

Do not copy the exact snake-girl design. Use this example as calibration for structural sophistication, motif coherence, and visual hierarchy.

## 5. Dynamic adaptation model

Treat preferences as weighted and revisable rather than absolute.

### Tier A — Hard constraints

Follow unless the user explicitly overrides them:

- output prompt text when the user asks for prompts; do not generate an image unless explicitly requested
- preserve locked character and costume information
- use Anima-friendly English Tag + Natural Language formatting
- default to positive prompt only
- do not add generic quality tags, weights, or model parameters by default
- respect requested background, framing, aspect ratio, and visible body range
- use the actual user-provided reference image as the primary reference when one is supplied

### Tier B — Strong preferences

Apply by default, but adjust when new feedback conflicts:

- genuine OC design thesis
- memorable silhouette and coherent shape language
- deliberate visual anchor and mass distribution
- structural clothing design and material contrast
- pose-driven costume movement
- restrained palette hierarchy
- negative space and readable focal points
- contemporary game/fashion illustration sensibility

### Tier C — Optional enhancement modules

Select only when appropriate to the task:

- luminous oriental couture
- atelier fashion / editorial styling
- cinematic environmental vignette
- dark narrative lighting
- soft domestic warmth
- surreal biological ornament
- minimal graphic design plate
- delicate imperfection and natural material behavior

Never activate all modules simultaneously.

## 6. Feedback update rules

When the user says an output is “too plain,” identify which layer failed before adding more detail:

1. weak silhouette → redesign the large outer shape
2. weak OC identity → replace or sharpen the design thesis
3. weak fashion design → rebuild garment construction and asymmetry
4. weak composition → change camera, body axis, overlap, and visual flow
5. weak atmosphere → specify light direction, bounce, shadow falloff, and environmental response
6. too busy → remove secondary motifs and restore negative space
7. too generic → replace generic adjectives with a specific motif system and behavioral action

When the user approves an output, preserve the successful dimensions and vary only the requested dimension. Do not reset the whole style each time.

When the user rejects an output, record the rejection as evidence about a layer, not as a reason to add random complexity. Prefer a targeted revision and explain the design change briefly when explanation is requested.

## 7. Prompt construction defaults

For open-ended OC requests, internally prepare:

1. three distinct design theses
2. one selected thesis with a unique silhouette strategy
3. one primary visual anchor and up to two secondary anchors
4. a material contrast pair
5. a behavioral pose linked to the design
6. a palette hierarchy
7. a presentation mode: character plate, decorated key visual, editorial plate, or environmental vignette

Then compile the final prompt in this order:

`subject and framing → design thesis → silhouette → appearance → garment construction → visual anchor and props → pose and camera → environment and narrative residue → lighting and palette hierarchy`

## 8. Quality gate before output

Ask internally:

- Could the character be recognized from the silhouette alone?
- Does the design have a specific sentence-level concept?
- Are the major shapes related by a common visual grammar?
- Is there a clear primary focal point?
- Does the pose explain the clothing and prop movement?
- Are materials visible through physical behavior rather than adjectives?
- Does the background belong to the character's concept?
- Is there enough negative space for the design to read?
- Does the prompt avoid generic filler and accidental motif mixing?
- Did the revision preserve the user's locked information?

## 9. Calibration priority

When preferences conflict, use this priority order:

1. explicit current-turn requirements
2. locked character facts and reference-image facts
3. explicit negative feedback from the latest interaction
4. repeatedly confirmed preferences
5. older stylistic tendencies
6. optional creative embellishment

This profile should evolve over time. New explicit feedback overrides older assumptions, while one-off experiments should not automatically become permanent rules.
