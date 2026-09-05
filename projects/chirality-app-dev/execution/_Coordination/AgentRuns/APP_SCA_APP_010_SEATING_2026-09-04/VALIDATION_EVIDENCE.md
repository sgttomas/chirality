# Validation Evidence — APP_SCA_APP_010_SEATING_2026-09-04

All commands run from the repository root of worktree
`/Users/ryan/dev/chirality/.claude/worktrees/task-management-gen-pass-518da2`
on branch `claude/sca-app-010-seating` (basis `787a551e70d9fb33f6f9a9fe228443d890a8d02d`).
Raw outputs are under `Evidence/validation/`.

## Build integrity

| Check | Result |
| --- | --- |
| Pre-images frozen before any write | `Evidence/pre_images.json`: 73 carrier files plus the decomposition; `build_seating.py --freeze` |
| Decomposition identity at apply | SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`; every anchored row and ledger line found at its expected line number |
| Apply | `build_seating.py --apply`: all pre-images matched; every transaction keyed on exactly-once text; whitespace check over every staged text before any write; 73 files written; 20 items seeded |
| Post-image parity | `build_seating.py --check`: 73 post-images verified (`Evidence/post_images.json`) |
| First apply attempt | Aborted on a pre-existing trailing-whitespace line in DEL-03-02's Scope of Work after four carriers had been written; those files were reverted with `git checkout -- projects/`, the builder was corrected to check every staged text before any write and to ignore untouched lines, and the apply was rerun from the same frozen pre-images. A second revert and rerun followed two byte-quality refinements (package-scope wrapping; matrix basis cells and DEL-02-02's OUT-001 label). A third revert and rerun applied the independent review's findings F1 to F4 (placeholder removal, outside-carrier memory wording, ruling citations, history placement). The final tree is the fourth apply; a second, fresh independent reviewer instance (same model and role, different instance) re-verified the re-frozen diff. |
| APP-HOLD dispatch preflight | `app_hold.py check --operation dispatch` for all seventeen carriers: `ALLOW` (`Evidence/app_hold/DEL-*.json`) |

## Repository validators (final tree)

| Validator | Result |
| --- | --- |
| `tools/scope_of_work/validate_scope_of_work.py` ×13 carriers | PASS, format SOW_V1 (`scope_of_work_validator.txt`) |
| `execution/_Reconciliation/References/reconcile_authority_corpus.py status` | corpus v20, no drift (`corpus_status.txt`) |
| `tools/practitioner_harness/harness.py self-check` | exit 0; no BLOCK (`harness_self_check.txt`) |
| G0 `validate_root_materialization_fence.py` | exit 0 |
| G1 `validate_root_harness_adapter.py` | exit 0 |
| G2 `validate_root_surface_ownership.py` | exit 0 |
| G3 `validate_root_work_graph_dispatch.py` | exit 0 |
| G4 `validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only` | run after commit; recorded in the receipt |
| `tools/validation/validate_candidate_whitespace.py --base-ref origin/main` | PASS |
| `tools/run_affected_tests.py --base origin/main` | 671 passed (`run_affected_tests.txt`) |
| `git diff --check` | clean |
| `tools/validation/validate_app_dev_loop_receipts.py` | VALID before the Receipt 238 append; rerun after the append and recorded in the receipt |
| Frontend gates | skipped: no product source changed (`frontend/**` untouched) |

## Independent review

`REVIEW.md` in this folder, written by a bounded read-only Claude Code
subagent over the frozen diff `Evidence/frozen_diff.patch` (`git diff -U0`, zero context so no pre-existing whitespace is reproduced; SHA-256
`66c0163c5b2f531674d130d5b9a2c4390d41046411e3f4679e06302f88e887b2`). The first pass returned PASS with two MAJOR and four MINOR findings; all were
applied and a second, fresh reviewer instance re-verified the re-frozen diff
(second pass PASS, one MINOR on run-packet wording, applied here). Verdict and
findings are recorded there and summarised in `HANDOFF_STATE.md`.

## Scope backcheck

Changed paths versus the basis: the seventeen carriers' `_STATUS.md` and
`MEMORY.md`; the thirteen carriers' `ScopeOfWork.md`, `_CONTEXT.md`, and
`_REFERENCES.md`; `_DECISIONS/D-APP-108_*.md` (new) and one `_REGISTER.md` row;
the repo-root Root notice (new); this run folder; `loop/LOOP_RECEIPTS.md`
(append). No `frontend/**`, `docs/**`, decomposition, companion register,
pointer, SCA snapshot, dependency register, workplan, or prior receipt changed.
