# P8 Web-first Harness — Acceptance Suite

## P8-01 — repository URL bootstrap

Given the repository URL, resolve a commit SHA and fetch `bundle/HARNESS.md` at that SHA. Keep that SHA for all repository files. If pinning fails, use main with version checks and an explicit consistency caveat.

## P8-02 — raw bundle is runtime source of truth

The raw `bundle/HARNESS.md` is the canonical runtime artifact. The GitHub page is only a discovery/bootstrap surface.

## P8-03 — no local dependency

Normal web use must not require repository cloning, Python, Node, SQLite, an executable, or a local HTTP server.

## P8-04 — fresh-session probe

The handshake exposes the loaded harness version and module count, not proof of freshness. A cached API response can select an old but consistent commit. If the initial message contains a task, complete it without a standalone handshake.

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

## Manual web smoke tests

Run in a fresh chat for each case, on the actual target platform. Record platform/date, loaded commit or fallback, files actually fetched, result and failure. These cases are pending until observed; text tests cannot establish model compliance.

1. **Link only:** send the repository URL; confirm the loaded version handshake and the resolved commit when available.
2. **Link plus task:** request a NAI5 portrait in the same message; confirm it completes the task rather than stopping at the handshake.
3. **Identity check:** request a known character and an exact alias; check the actual manifest and shard evidence, and do not count a guessed tag as verified.
4. **Follow-up:** ask to change only lighting; confirm previously accepted identity, outfit and framing remain locked.
5. **Unavailable source:** restrict or simulate an unavailable critical file; confirm the AI says what it could not verify and follows the relevant fallback instead of inventing a result.

## P8 Exit Criteria

- [ ] Repository URL can bootstrap the harness on URL-capable web AI.
- [ ] Raw Bundle is canonical.
- [ ] No local runtime is required.
- [ ] Revision consistency and fallback uncertainty are observable; freshness is not guaranteed.
- [ ] On-demand loading is explicit.
- [ ] Fetch failure degrades honestly.
- [ ] CI keeps generated artifacts synchronized.
- [ ] Version is synchronized across source and generated outputs.
