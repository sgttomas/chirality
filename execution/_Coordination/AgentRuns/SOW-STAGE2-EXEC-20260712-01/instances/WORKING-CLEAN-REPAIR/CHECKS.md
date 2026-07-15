# WORKING-CLEAN-REPAIR Checks

Verdict: `PASS`

Basis: `main@715f618e93528d626a73d2134781e8c9c27f6c90`

## Repair and corpus checks

- `python3 .../WORKING-CLEAN-REPAIR/run_repair.py` — PASS; 57 changed members
  (53 App, four Piping); manifest
  `21287ee0a3ef6fbcda6b0870fe7d81f82eb4b899d4cbed047a5772dce6d3e838`.
- `python3 .../WORKING-CLEAN-REPAIR/validate_repair.py` — PASS; validation
  `6e6839dd3eb0a2272e5a23476d474b51bde94e6f94668c8b3b4d3e2cf3c92b7b`.
- 57 `chirality-sow-finalization/v1` reports bind every before hash, after
  hash, report hash, 1,753 externalized source blocks, and migration control.
- 146/146 conversion members resolve as valid, single-format `SOW_V1`; all
  prohibited production tokens are absent.
- All eight Piping PKG-00 exclusions remain `LEGACY_FOUR_DOC` and byte-equal
  to `HEAD` for all four legacy files.
- Lifecycle remains 153 `IN_PROGRESS` plus the sole issued Piping
  `DEL-01-01`.
- Project diff is exactly the 57 manifest paths; no other project path changed.

## Focused and root checks

The command ledger is `checks/RESULTS.json`
(`df4c18f637ec3b0265d0c81b05a3ec4c67796510a173a509fc070dd4ce58ac1d`).

- `python3 -m pytest -q tools/scope_of_work/test_scope_of_work_tools.py` —
  19 passed.
- `python3 -m pytest -q tools/practitioner_harness` — 264 passed.
- `python3 tools/validation/validate_agent_instructions.py` — exit 0.
- `python3 tools/validation/validate_instruction_entrypoints.py` — exit 0.
- `python3 tools/validation/validate_path_anchors.py .` — exit 0.
- `python3 tools/validation/validate_skill_metadata.py` — exit 0.

## Project checks

All project checks used disposable copies; dependency caches were read-only
inputs and no build output entered this worktree.

- App `npm run typecheck` — PASS; log hash
  `2bcf8e9aadbaab700665caaa6fa3f1a40cd36e9596d9215ccbea7d3f920b59af`.
- App `npm test -- --run` — 713 passed, four skipped; log hash
  `440a6a4830c36132cb0cb1b792e23b7f1315a65bec236302c05873289f2ad917`.
- App `npm run build` — PASS; log hash
  `418ea8e962770d44701e351e1c7acacfea7cb0654de04b83e85a6e35af93b917`.
- Piping `npm run build:wasm --workspace apps/desktop` — PASS; log hash
  `4ab2597140aa32b71a69a41e68a2f8dbda97c8483bbabb29bff666f3428790d6`.
- Piping `npm run test:desktop` — 476 passed; log hash
  `0ef5d8c0808533bd05e4c3414e35c020efe2ad93724c88a9a63bcdf70cb3f0ae`.
- Piping `npm run build:desktop` — PASS; log hash
  `bb5006b36e74136b4b5bdcff23c6ffd45975de12de865f5971dc7c294b0a9180`.

The superseded Piping pre-WASM failure logs remain under `checks/` and are
dispositioned in `ATTEMPTS.md`.
