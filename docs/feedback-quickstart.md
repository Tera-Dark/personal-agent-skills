# Casual Feedback → Draft → Approval (v5.1)

A casual review such as "the expression is good but the jacket changed" must remain **scoped**. Do not pretend a remark proves NAI5 output quality in all future images.

## No JSON required in conversation
Ask the connected agent: "帮我把这轮出图的喜欢/不喜欢整理成待确认的反馈，不直接更新长期偏好". The agent extracts small, abstract, separate positive/negative candidate rules, marks whether it actually saw the image, presents them for your review, and only writes approved material to GitHub when authorized.

## Optional local helper
The helper takes a few short command-line fields and prints a valid JSON candidate:

    python3 scripts/feedback_draft.py --rule-id portrait.camera --scope mode:portrait --axis camera --rule "Keep visible upper torso" --artifact-id anon-r01 --evidence-type USER-IMAGE-REPORT

Optionally add --out review.json to save a DRAFT locally; this DOES NOT record, promote, write to GitHub or change prompts.

After you personally verify it:

    python3 scripts/learn.py record --file review.json
    python3 scripts/learn.py review
    python3 scripts/learn.py promote portrait.camera
    python3 scripts/learn.py digest

The promote command remains guarded by independent evidence or an explicit user policy and its review requirement. Opposing user feedback can revoke practical effect without erasing history. Public projects should retain abstract creative rules only, not user photos, private OC details, complete conversations or personal identifiers.
