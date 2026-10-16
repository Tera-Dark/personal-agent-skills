# Visual Benchmarks · v5.1

Purpose: turn creative-judgment hypotheses into user-run, repeatable A/B evidence. **No automatic image grading**. This validates experiment design, not whether generated images are good.

## Three starting test classes
- portrait: preserve OC hair/eyes/gender/clothes, improve crop and face priority;
- cinematic-duo: preserve both identities, change only interaction blocking/touch/eyelines;
- concept-poster: change only dominant graphic-concept mechanism, not who is depicted.

## Workflow
1. Pre-register the case and use this helper to prepare a JSON metadata record:

    python3 scripts/visual_benchmark.py template --case cinematic-duo --run-id duo-test-001

2. Fix all settings: checkpoint, seed, resolution, steps, sampler, guidance, externally fixed artist stack, quality and negative. The baseline and variant differ by ONE registered design axis, not by multiple factors.
3. Run both images personally in NAI5/Anima. Compare actual output in the chat, privately. The public repo stores **no images, complete prompts, private URLs or unpublished commission art**.
4. Only after review, set result.status=USER-RATED, add reviewer, separate 1–5 ratings for every case dimension, one winner (or inconclusive) and brief abstract comments. Never mark textual spec as image-tested.
5. When explicitly asked to save experiment metadata, run:

    python3 scripts/visual_benchmark.py record --file run.json
    python3 scripts/visual_benchmark.py validate

## Caveats
A matched seed does not guarantee causal comparison across changed prompt text. Repeat with multiple paired seeds and track variance. Aesthetic scores represent a user's contextual preference, not universal quality. The evaluator must distinguish model failure from art-direction failure. Feedback that should become a long-lived preference still needs separate Learn review and explicit confirmation.
