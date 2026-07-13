# Schema and Content Verdict — DEL-13-04

Verdict: `PASS`

## Format and schema

- The current P3-bound/live state and child `legacy_state/` contain the four legacy production documents and no `ScopeOfWork.md`. Validation resolves the isolated copy as valid `LEGACY_FOUR_DOC` with zero issues.
- The child `workspace/` contains `ScopeOfWork.md` and none of the four legacy production documents. Validation resolves it as valid `SOW_V1` with zero issues.
- Candidate SHA-256 is `01ce58d6636f39535933c8f365735336118da7bf85223346bf6b7d1c78bdd046`, exactly the sealed expectation and Stage-1 Git object.
- The unchanged candidate retains only the historical `D-GOV-15@58aa81d62f4a32e3c2d687e4356a1e4be8141674` pilot marker. No D-GOV-16 marker was inserted; this is the required `PILOT-VALIDATION-001` posture.

## Source coverage and identity

- The mapper emits 48 rows, all `PRESERVED`, covering `CLM-001` through `CLM-048`.
- Coverage is exact and non-overlapping: Datasheet 130/130 lines in 10 ranges; Specification 123/123 in 13; Procedure 147/147 in 13; Guidance 80/80 in 12. Total: 480/480.
- Every mapping binds its current source SHA-256, the exact candidate SHA-256, and a defined `CLM-*` target.
- Parity reports 48 passing checks, zero issues, exact source hashes, and exact candidate hash.

## Objective and evaluation grounding

- `OUT-001` mirrors accepted `SOW-066` and `OBJ-014`: deterministic physical-to-analytical transformation with warnings, omissions, assumptions, and traceability. The current and frozen decomposition bases contain identical relevant `SOW-066`, `OBJ-014`, and `DEL-13-04` mappings.
- `AC-001` is grounded in the fully preserved specification source ranges, including deterministic transform, warning, traceability, unit, missing-data, protected-content, professional-boundary, and explicit deferral obligations.
- `VER-001` is grounded in the fully preserved procedure and verification ranges: schema/map/parity/hash checks, focused transform/adapter/dependency evidence, and independent authority review.
- The single evaluation-matrix row binds `OUT-001` to `SOW-066`, `OBJ-014`, `CLM-011`, `AC-001`, and `VER-001`. There are no orphan `OUT-*`, `AC-*`, or `VER-*` definitions.

## Stage-1 reproduction

- Fresh claim-map bytes equal Stage-1 `CLAIM_MAP.csv`; fresh parity Markdown bytes equal Stage-1 `PARITY_REPORT.md`.
- Fresh parity check arrays, issues, candidate/source hashes, and source-file bindings equal Stage-1. The JSON `scope_of_work` path is portably child-local, so its envelope hash differs while semantics are identical.
- Fresh checklist `items` equal the accepted Stage-1 checklist exactly: one `DEL-13-04-AC-001`, linked to `OUT-001` and `DEL-13-04-VER-001`, with exact text and source identity. Only the lawful envelope posture changes from historical `PILOT_DUAL` to target-only `SOW_V1` under `PILOT-VALIDATION-001`.
- Fresh rendered HTML hash `0d515733a042576ac8917d8e0cf52c82b42b25357d84a43f959ebd9663cf2797` equals Stage-1 evidence.

No schema or project-content discrepancy was found.
