# v4.9 Experience Scorecard & Acceptance Targets

> This is an acceptance framework, not a claim that subjective taste or model image outcomes already reach 9/10. No image A/B runs are shipped in this PR. The only proven results are deterministic software contracts after CI passes.

## User workflow measured against seven dimensions

| Dimension | Concrete >=9/10 target | Evidence needed | Current baseline (2026-10-14) |
| --- | --- | --- | --- |
| Module isolation | No renderer owns aesthetics; no cross-model syntax leakage in 20 model-compilation checks | Ownership scans + NAI5/Anima spot tests | Architectural SPEC, previously ~9 |
| Personalized design | >=9/10 owner approval on >=20 independently reviewed images across portrait, OC, movie-still, poster | User-scored images and saved constraints | Not yet measured; strong source corpus |
| Web efficiency | Cold-start <=6600 heuristic tokens; one-link bootstrap; reference fetched only when relevant | Bundle manifest, 10 measured real chats | Budget gate executable; latency unmeasured |
| Feedback troubleshooting | >=90% of 20 failed examples preserve accepted layers and fix first failed axis | Before/after prompts, image results | Evaluation rubric + executable lock diff |
| Long-term learning | 100% unique event IDs; no repeated votes for one artwork; 0 false automatic promotions | Python tests, >=20 real signals | CLI unit tests, sparse initial data |
| Autonomous evolution | Explicit or >=3 independent supports, 0 active contradictory rules, manual promotion + undo audit | Policy/actions history and reviewable PR | Gated engine; not unsupervised training |
| QoL | >=90% success in 20 continuation/correction cases: continue, rollback, one-box, locked outfit, cross-session restore | User-run workflows + handoff test suite | Session snapshots/diff + conversational routing |

## Required quality gates before shipping changes

1. python3 scripts/validate_skills.py
2. python3 scripts/learn.py validate
3. python3 -m unittest discover -s tests -p "test_*.py" -v
4. python3 scripts/check_personal_anima_regression.py
5. python3 scripts/build_tag_index.py --self-test
6. python3 scripts/check_tag_index_snapshot.py
7. python3 scripts/build.py
8. python3 scripts/validate_skills.py --check-bundle
9. python3 scripts/check_output_contract.py

GitHub Actions runs the deterministic gates. The following require actual user follow-up and must not be marked PASS by text-only tests:

- Three or more independent artworks per frequently used visual mode
- Creative output preference transfer across NAI5 and Anima
- Image fidelity and IP costumes when using the real owner's ComfyUI / NovelAI environment
- Cold-start latency with available model/tool provider
- No hallucinated promotion during different chat systems' use

## Owner-run 3-minute acceptance script

A. Ask for an original 1999 film-still prompt; confirm original outfits and a motivated camera.
B. Say "光影很好但脸不对，只改脸"; observe positive layer locks.
C. Save the abstract design state as session file; ask "继续上次项目"; verify state loaded from repository, no hallucinated details.
D. Repeat same art feedback 3 times: support count must remain ONE.
E. Provide three genuinely independent art IDs with same rule/scope; verify only eligible after three, not active until promotion.
F. Enter opposite evidence: effective rule suspended until reviewed.
G. Undo a rule: audit still shows promotion and undo; generated digest excludes it.
H. Convert NAI5 weighted tags to Anima: parentheses syntax, no NAI5 number::tag:: leakage.

## Roadmap / intentional limits

- Not implemented: direct capture of every ChatGPT conversation, passive background agent, self-training LoRA, automated scoring of unviewed image quality, unreviewed pushes to public main.
- Optional phase after real feedback: issue-based GitHub intake or private data repo, image-run benchmark and plot/report UI. Do not install more moving parts until existing flows work.
- Maintain versioned golden prompts with owner-selected good/bad examples, only if the owner opts to make the sanitized examples public.

A release can pass code-level QA while its aesthetic performance remains **IMAGE-PENDING**. Keep those statuses distinct.
