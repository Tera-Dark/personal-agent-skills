# Learning data (no raw chats)

- events.jsonl: append-only short abstract feedback events, created by scripts/learn.py record.
- policies.json: explicitly approved preferences only; never promote merely because AI predicts a taste.
- actions.jsonl: append-only promote / undo audit.
- sessions/*.json: explicitly saved, whitelist-filtered creative handoff (public GitHub; DO NOT paste secrets).
- ../../00_core/personal-identity-profile/references/learning-digest.md: generated from approved policies, not hand-edited.

This repository may be publicly visible. NEVER store photos, full conversation transcripts, API keys, sensitive personal information or unpublished/private commissions. Current-turn preference always overrides the learned summary. Legacy feedback-ledger.md is kept as a historical human-readable archive, not counted automatically toward promotion.

Fast start from a cloned repository:

1. python3 scripts/learn.py review
2. python3 scripts/learn.py record --file feedback.json
3. python3 scripts/learn.py promote <rule_id> (only after evidence review)
4. python3 scripts/learn.py digest
5. python3 scripts/learn.py validate

Save a creative session with python3 scripts/learn.py session-save my-art --file state.json. Restore with python3 scripts/learn.py session-load my-art.

For web chat: when a connected agent has explicit write permission, it can edit these exact JSON/JSONL files via GitHub, then regenerate the digest through CI or a local run. Loading the repository alone never grants writes or background monitoring.
