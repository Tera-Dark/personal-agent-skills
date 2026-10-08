# P8 Web-first Harness — Acceptance Suite

## P8-01 — repository URL bootstrap

Given only the repository URL, an AI model with URL access should read the README AI bootstrap and then fetch the current raw `bundle/HARNESS.md`.

## P8-02 — raw bundle is runtime source of truth

The raw `bundle/HARNESS.md` is the canonical runtime artifact. The GitHub page is only a discovery/bootstrap surface.

## P8-03 — no local dependency

Normal web use must not require repository cloning, Python, Node, SQLite, an executable, or a local HTTP server.

## P8-04 — fresh-session probe

The handshake exposes the current harness version and module count. A mismatch is treated as stale/cached content.

## P8-05 — on-demand loading

Only selected on-demand modules are fetched from generated raw URLs. A model must not assume every module is already loaded.

## P8-06 — graceful fetch failure

If raw module loading fails, use only the indexed module card with `[card-only]` degradation. Do not silently substitute remembered module content.

## P8-07 — generated bundle consistency

Source changes must regenerate `bundle/HARNESS.md`, `bundle/HARNESS-FULL.md`, `bundle/modules/*`, `bundle/manifest.json`, and `docs/skill-registry.md`.

## P8-08 — version synchronization

`VERSION`, handshake, Bundle headers and generated manifest version must resolve to the same release version.

## P8-09 — web-first documentation

README and usage docs present the web/no-local-runtime path as the primary creative usage mode.

## P8-10 — pipeline-pack exposure

The generated manifest exposes `web_first`, shared prompt packs, and the active module index.

## P8 Exit Criteria

- [ ] Repository URL can bootstrap the harness on URL-capable web AI.
- [ ] Raw Bundle is canonical.
- [ ] No local runtime is required.
- [ ] Freshness is observable.
- [ ] On-demand loading is explicit.
- [ ] Fetch failure degrades honestly.
- [ ] CI keeps generated artifacts synchronized.
- [ ] Version is synchronized across source and generated outputs.