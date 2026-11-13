# Google AI Studio Adapter

> Generated for Harness v{{VERSION}} · built {{BUILD_DATE}} · {{MODULE_COUNT}} modules indexed

This adapter is the Google AI Studio entry point. It embeds the ordinary L1 Harness below and adds platform-specific loading rules. The source of truth remains the existing kernel, module skills, task cards and pipeline definitions.

## 1. AI Studio / URL Context operating rules

- Enable **URL Context** in AI Studio's Tools before sending the entry URL.
- URL Context reads the URLs explicitly supplied to it. It does **not** automatically crawl or recursively fetch links found inside a fetched Markdown file.
- The embedded L1 Harness is already loaded. Do not fetch `HARNESS.md` again unless this adapter was truncated or unreadable.
- Treat links in the embedded index as a routing catalog, not proof that their contents have been loaded.
- After identifying the task, explicitly request the selected raw URLs through URL Context. Batch the smallest useful set in one request (one L2 card, at most one target pipeline pack, and only the necessary L3 module/reference files). Do not preload all modules.
- If AI Studio cannot make a second URL Context request, ask the user to provide the selected raw URL(s) or paste their contents. Continue only within the available evidence and mark missing critical sources unavailable.
- Never say a module, task card, pipeline or reference was loaded merely because its URL appeared in this document.

## 2. Balanced loading procedure

1. **L1 — already embedded:** use the Identity, Router, execution contract, full module index, failure policy, task-card URLs and pipeline URLs in the embedded Harness.
2. **L2 — select by intent:** fetch one matching task card when the task is a portrait, cinematic duo, concept poster or fast variant. For other tasks, skip L2 if no card fits.
3. **Pipeline — select by target:** for model-specific image prompting, fetch the matching pipeline pack: `nai5`, `anima`, `moss` or `moss-tags`. MOSS Caption/Layout uses `moss`; verified Tags use `moss-tags`.
4. **L3 — only when needed:** fetch the selected module contract and the specific reference files required for complex, novel, uncertain or failed tasks. Use the module index's exact URL. Technical tasks route to their corresponding module; `planned` modules are placeholders, not implemented capabilities.
5. **Version check:** compare each fetched file's Harness version with this adapter's version. If a file is from a different version, retry using the same commit-pinned path when available. If consistency cannot be established, disclose that limitation and apply the existing failure policy.

## 3. URL Context failure behavior

- **Task card unavailable:** continue only if the task can be handled safely with the embedded L1 rules; otherwise ask for the card.
- **Pipeline unavailable:** do not emit model-specific syntax that depends on the missing pipeline.
- **Module/reference unavailable:** use only the module's indexed fallback description for noncritical routing; do not substitute remembered content.
- **Danbooru index unavailable:** do not claim hard tags are verified; use natural-language descriptions where appropriate.
- **URL Context unavailable or disabled:** tell the user to enable URL Context or paste the required raw file contents. Do not pretend a browser fetch occurred.

## 4. User launch instruction

In a fresh AI Studio prompt, enable URL Context and provide this adapter URL:

`{{AISTUDIO_URL}}`

If the first message also contains a task, complete it rather than stopping at the handshake. If it contains only the adapter URL, use the Harness handshake. Keep subsequent reads scoped to the selected task and target.

---

## Embedded L1 Harness

The following is the canonical generated L1 Harness for this same build. Its identity, routing, task-card catalog, pipeline catalog and module index remain authoritative.

{{EMBEDDED_HARNESS}}
