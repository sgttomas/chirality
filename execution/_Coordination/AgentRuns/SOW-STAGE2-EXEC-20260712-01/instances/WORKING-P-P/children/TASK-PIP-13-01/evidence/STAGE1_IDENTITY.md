# DEL-13-01 Stage-1 Identity Check

Verdict: `PASS`

- Candidate SHA-256 is `6c76b2c785acc56ee1e67aaba64930e457b8c2ca20d4d9e8b4156cebe579c43d` for the child candidate, the P4 pilot extraction, and the exact Stage-1 Git object at `31c35ea9798c29cd0af16b7089186f3942dcfcb1`.
- All four source hashes and `_STATUS.md` match `stage1_evidence/SOURCE_HASHES.sha256`, the exact P3 execution-manifest row, `legacy_state/`, live production, and `main@0d260eb024d8b8dada0df477b70ac880a6906ffa`.
- Fresh claim map is byte-identical to `stage1_evidence/CLAIM_MAP.csv`, SHA-256 `7a27243b10472501be53ee68d1fadbdd33c0276582dc621381ea05d16bab21d7`.
- Fresh parity Markdown is byte-identical to Stage 1. Fresh parity JSON is semantically identical after removing only the run-specific `scope_of_work` path; checks, hashes, schema, and verdict are exact.
- Fresh render SHA-256 `802aae3631d1c779401d4b011464f89eb9ab2cb83d5241ae66dd18f4f27ba2ca` is byte-identical across both reproductions and matches Stage 1.
- Both fresh deterministic checklists are byte-identical and bind the exact candidate SHA-256, `AC-001`, and matrix-linked `VER-001`. Stage-1 evidence did not preserve a checklist artifact, so no historical checklist byte-comparison is claimed.
- Historical Stage-1 validation reported `PILOT_DUAL`. Under active `PILOT-VALIDATION-001`, this run lawfully validates the unchanged legacy-only state as `LEGACY_FOUR_DOC` and the unchanged SOW-only target as `SOW_V1`; no synthetic dual overlay or D-GOV-16 marker was introduced.
