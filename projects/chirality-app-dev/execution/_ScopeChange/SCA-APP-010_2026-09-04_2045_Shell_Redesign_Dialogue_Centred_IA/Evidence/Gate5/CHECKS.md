# SCA-APP-010 Gate-5 Checks

All commands run from the repository root of worktree
`/Users/ryan/dev/chirality/.claude/worktrees/task-management-gen-pass-518da2`
on branch `claude/sca-app-010-gate1-intake` unless stated.

## Basis and sequence

| Step | Check | Result |
| --- | --- | --- |
| §5.1 | Audited execution basis | `11b47882f7e8726a42829cd26db5ecd8383f43b5`; `git merge-base --is-ancestor 95b5687a7 HEAD` true; `git diff --stat 95b5687a7 HEAD` outside the snapshot and receipts ledger empty |
| §5.1 | Frozen inputs | decomposition `e46084ab…`, companion `e47fced6…`, `_LATEST.md` `f235ced4…`, builder `9d4774bf…`, actions `8b579266…`, delta `c610f494…`, map `2045684e…` all exact; SCA-APP-009 tree `1c5b9e68049460c3a9a6c1abadc1b8a64e2bc085` |
| §5.1 | Collision scan | `grep -c` for `SOW-081..084`, `DEC-025`, `OI-008` on the live decomposition = 0 |
| §5.1 | Fresh pre-change audit | `Evidence/Gate5/PRE_CHANGE_AUDIT/`: WARNINGS, 0 / 63 / 7, identical to Gate 1; closure FAIL on SCA-APP-009's open state |
| §5.2 | Rollback bundle | scratch `gate5_rollback/` with `SHA256SUMS` for the two pre-images and the pointer |
| §5.3 | Builder regeneration | exit 0, `VALIDATION: PASS`, `git status` on `Gate3/` empty (byte-identical) |
| §5.4 | Fresh post-change candidate audit | `Evidence/Gate5/AUDIT_DECOMP/`: WARNINGS, 0 / 74 / 8; 10 / 52 / 84, 79 / 4 / 1, S9 M41 L2, reverse-view 0 / 0, OI-008 = 4; no new blocker or major; `Post_Change_Coverage.json` = `coverage_summary.json` (`f4b140f3…`) |
| §5.5 | Independent Gate-5 review | `Evidence/Gate5/GATE5_INDEPENDENT_REVIEW.md` SHA-256 `fd9fc54f79681c548afb60803c67cee6f9112ca73b32910de597d7febfae4611`: PASS, 0 / 0 / 2 MINOR |
| §5.6 | Cumulative map | accumulator: 45 rows, 0 findings; `--check-map` parity; CRLF-normalised `cmp` identical to `Supersession_Map.csv` |
| §5.7 | Apply pair | `cp` of the two candidates; live hashes `c7c05169…` and `63383f04…`; `git diff -U0` equals `Gate3/DECOMP_DIFF.patch` and `Gate3/COMPANION_DIFF.patch` |
| §5.8 | RECONCILIATION | `reconcile_authority_corpus.py status`: v20, no drift; companion 83 / 83 / 50 / 18, 83 pins to the live decomposition; `Evidence/Gate5/RECONCILIATION_REPORT.md` |
| §5.9 | Snapshot completion | `Decision_Log.md` (G4-CONFIRM, G5-AUTHORIZE), `Handoff_State.md`, `RUN_SUMMARY.md`, this file, `POINTER_CANDIDATE_VALIDATION.md`, `MANIFEST.sha256` last |
| §5.10 | Scope backcheck | changed paths versus the approval basis: the two authoritative files, the snapshot, and `loop/LOOP_RECEIPTS.md`; `_LATEST.md` unchanged; SCA-APP-009 tree unchanged |

## Repository validators (applied state, audited basis)

| Validator | Result |
| --- | --- |
| `tools/validation/validate_app_dev_loop_receipts.py` | VALID |
| `tools/validation/validate_candidate_whitespace.py --base-ref 95b5687a7` | PASS |
| G0 `validate_root_materialization_fence.py` | PASS |
| G1 `validate_root_harness_adapter.py` | PASS (exit 0) |
| G2 `validate_root_surface_ownership.py` | PASS (exit 0) |
| G3 `validate_root_work_graph_dispatch.py` | PASS |
| G4 `validate_instruction_tranche_manifest.py --base 95b5687a7 --head HEAD --added-manifests-only` | PASS; 0 instruction-surface paths |
| `tools/run_affected_tests.py --base 95b5687a7` | 671 passed |
| `tools/practitioner_harness/harness.py self-check` | exit 0; no BLOCK |
| `git diff --check` | clean |

## Disclosed deviations

1. **Out-of-sequence artifact.** `Evidence/Gate5/POINTER_CANDIDATE_VALIDATION.md`
   was written and the audit files were staged while the step-5 review was
   still running (review MINOR-002). The file makes no claim about the live
   pointer beyond `Live pointer changed: NO`; the step-10 backcheck above is
   the authoritative path-boundary check.
2. **Gate-5 authorization row.** The owner's "proceed to Gate 5" was recorded
   as `G5-AUTHORIZE` with the reading labelled as the agent's (review
   MINOR-001).
3. **Landing basis advanced after the audits.** After application and
   validation, `origin/main` `4b6d2bb2c` (PR #709 and PR #710, DEL-09-07
   Scope of Work initialization and its run records, `APP_HOLD_REGISTER.csv`,
   project `AGENTS.md`) was merged into the branch as `57572b3a2` to resolve
   the receipts ledger. Re-verified after the merge: live decomposition
   `c7c05169…`, companion `63383f04…`, `_LATEST.md` `f235ced4…`, SCA-APP-009
   tree `1c5b9e68…`; `git diff --name-only origin/main HEAD` outside the
   snapshot and receipts ledger is exactly the two authoritative files;
   candidate whitespace PASS against `origin/main`; corpus v20 no drift; G4
   PASS against `origin/main`. The merged-in paths touch no audited surface
   except that DEL-09-07 now has a `ScopeOfWork.md`, which the next
   AUDIT_DECOMP will count as 52 / 52 instead of 51 / 51. The pre- and
   post-change audits were not rerun for this delta.
4. **Receipt renumbering.** This branch's Receipts 229 to 232 were renumbered
   231 to 234 (parent 230) because main's PR #709 and #710 carry 229 and
   230. Content unchanged apart from the identifiers.

## Pointer sub-gate (G5-POINTER, after PR #708 merged as `7795b0972`)

| Check | Result |
| --- | --- |
| Owner ruling | `Decision_Log.md` G5-POINTER, verbatim "update the LATEST pointer to the SCA-APP-010 once the PR #708 is merged." |
| Branch | `claude/sca-app-010-pointer` from `origin/main` `7795b0972cac147869607d994173753e4a2fc232` |
| Live pointer post-image | SHA-256 `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` = literal candidate payload |
| Target snapshot | exists; `MANIFEST.sha256` verified for every frozen file before regeneration; only `Decision_Log.md`, `Handoff_State.md`, and `POINTER_CANDIDATE_VALIDATION.md` changed, by design, and this file and the manifest |
| Authoritative hashes | decomposition `c7c05169…`, companion `63383f04…` unchanged |
| SCA-APP-009 tree | `1c5b9e68049460c3a9a6c1abadc1b8a64e2bc085` unchanged |
| Changed-path scope | `_LATEST.md`, the five snapshot files above, `loop/LOOP_RECEIPTS.md` |
| Validators | receipts VALID; self-check exit 0; candidate whitespace PASS; `git diff --check` clean |
