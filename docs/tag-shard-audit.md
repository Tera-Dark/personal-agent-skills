# Danbooru shard sizing · conservative v5.1 audit

Current root manifest records 5,834 artist shards for 42,196 artist tags. Three-letter prefix shards make each Web-first lookup small, but bloat tracked Git file count.

A dry-run-only audit reports a projection using two-character coarse prefixes **only when the combined JSON bytes remain under a 48 KB cap**; otherwise the existing third-character paths remain separate. This DOES NOT migrate the public schema, alias namespace logic, URLs, snapshot source hash, or any generated files.

    python3 scripts/tag_shard_audit.py --check

Why no automatic rewrite? The existing hard-tag boundary relies on exact manifest prefix rules, nested bucket manifests and a pinned third-party data snapshot. A live migration would regenerate thousands of files, require new source/schema and compatibility tests, and risk external Web-first clients. Proceed only after checking the report, reversible staging build, and equal exact/alias/missing test results on a representative tag corpus.

License attribution: see THIRD_PARTY_NOTICES.md. Attribution is not a legal conclusion about redistribution rights.
