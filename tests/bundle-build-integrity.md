# P10 Bundle Build Integrity — Acceptance Suite

## P10-01 — single source of truth

`harness.json`, `VERSION`, `kernel/KERNEL.md`, and skill source files are the only inputs that define generated runtime artifacts.

## P10-02 — complete generated outputs

`scripts/build.py` generates `bundle/HARNESS.md`, `bundle/HARNESS-FULL.md`, compact `bundle/modules/*.md`, individual `bundle/references/<module>/...` files, declared `bundle/pipelines/*.md`, `bundle/manifest.json`, and `docs/skill-registry.md`. The full harness still embeds every reference.

## P10-03 — pipeline pack discovery

Every entry under `pipeline.pipeline_packs` produces a matching `bundle/pipelines/<name>.md` file.

## P10-04 — orphan detection

`build.py --check` detects generated module bundles, individual reference files, and pipeline packs that no longer correspond to source configuration.

## P10-05 — manifest coherence

`bundle/manifest.json` must expose the same module set and pipeline-pack declarations as the source configuration, including each pack's ordered module list and generated bundle URL.

## P10-06 — generated Kernel entries

Kernel pipeline-pack entries come from configuration substitution; routes are not duplicated as hand-maintained URLs in the source Kernel.

## P10-07 — version coherence

`VERSION`, Bundle headers, manifest version, handshake, and generated registry version resolve to the same release.

## P10-08 — deterministic rebuild

Running `python3 scripts/build.py --check` immediately after a clean build reports no stale generated files, ignoring only build-date changes.

## P10-09 — automatic CI path

Pushes to `main` validate sources, rebuild generated artifacts when stale, revalidate the result, and commit the generated outputs.

## P10 Exit Criteria

- [ ] Generated outputs are complete.
- [ ] Pipeline packs are first-class build artifacts.
- [ ] Orphan packs/modules are detected.
- [ ] Manifest and Kernel are configuration-derived.
- [ ] Version data stays synchronized.
- [ ] Clean rebuild passes `--check`.
- [ ] CI rebuild path remains automatic.

## P11 — Reference-Level Runtime Loading

### P11-01 — slim module contract
- Expect: `bundle/modules/<name>.md` contains the module contract and a compact list of reference URLs, not the full contents of every reference.
- Fail: a simple task must fetch every reference to read the module contract.

### P11-02 — individual reference artifacts
- Expect: every declared `references/*.md` source generates a version-matched `bundle/references/<module>/references/*.md` artifact and a manifest URL.
- Fail: module links point to missing artifacts or stale generated files are not detected.

### P11-03 — full portable bundle remains complete
- Expect: `bundle/HARNESS-FULL.md` still embeds every active module's complete references for upload/paste-based environments.
- Fail: full harness becomes dependent on separate reference fetches.

### P11-04 — selective loading
- Input: simple white-background standing character.
- Expect: load only the needed aesthetic calibration references; do not load poster grammar, dataset tooling, or unrelated artist experiments.
