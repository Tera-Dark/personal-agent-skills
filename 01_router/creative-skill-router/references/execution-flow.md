# Execution Flow

## Standard creative pipeline

User Request
→ Task Classification
→ Identity Context
→ Aesthetic Gate (FULL / AUDIT / ESCALATE)
→ Specialist / Design Packet
→ Blueprint Gate
→ Model Adapter
→ Output Verification
→ Evaluation Loop on feedback

## Gate semantics

### FULL
Use when the user has not made the core design decisions. The director commits to a thesis, rejects alternatives, builds causality, subtracts, and keeps one coherent strange point.

### AUDIT
Use when the user already specified the design. The director checks structural completeness, causal gaps, generic drift and unrequested additions without rewriting locked facts.

### ESCALATE
If AUDIT finds a missing decision that materially affects the result, return to FULL rather than inventing it in an adapter.

## Blueprint Gate

Minimum type-specific artifacts:

- Character: thesis + silhouette + anchor hierarchy + applicable garment structure + material/palette logic + pose/camera + punctum/strange detail + locked facts.
- Illustration: thesis + captured moment + motif + scale/placement + camera + environment relationship + physical light + density + narrative residue + punctum/strange detail + locked facts.
- Finished-design packet: concrete user-supplied facts covering the adapter's required fields and passing AUDIT.

## Failure recovery

If output quality is poor:
1. Do not add keywords first.
2. Use evaluation-loop to identify the highest failed layer.
3. Re-enter the owning design or adapter layer only.
4. Preserve approved and locked dimensions.
5. Re-run Blueprint Gate before returning to an adapter.

## Technical invariant

Adapters translate. They do not create missing design decisions.
