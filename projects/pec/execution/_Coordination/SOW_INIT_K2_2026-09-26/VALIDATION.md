# VALIDATION — D-PEC-103 act (SOW_INIT_K2_2026-09-26)

The proposal's "Finite verification" table, run in the act worktree from the repository root with `PYTHONDONTWRITEBYTECODE=1` (CPython 3.13.7). Each command, its exit code and its output are in `evidence/` (file named in the last column). "Base" is fetched `origin/main` `d385b6a19` until the merge of `3e861f53c`, after which it is `3e861f53c`.

| # | Check | Result | Evidence |
|---|---|---|---|
| 1a | Ruling and register row `D-PEC-103` `RULED A + S + M + C8` on fetched `origin/main` | `d385b6a19` (PR #989) contains both; `git merge-base --is-ancestor d385b6a19 origin/main` exit 0 | this file; `MANIFEST.md` |
| 1b | Prep `SHA256SUMS` (66 entries) and the 17 run-root copies | all OK; 0 mismatches | `MANIFEST.md` |
| 1c | `apply_k2.py --check-only` | exit 0, `CHECK preflight passed; planned write set 2 creates, 0 modifies, 0 removes`; all 17 pins as tabled | `apply_checkonly.out` |
| 1d | Reliance holds, `dispatch-for-production`, before dispatch (both contracts, DEL-10-13 `_DEPENDENCIES.md`, both `_STATUS.md`) | `ALLOW`, exit 0, ×5 | `reliance_hold_dispatch.out` |
| 1e | Reliance holds, `rely-for-production`, before fan-in (same five targets) | `ALLOW`, exit 0, ×5 | `reliance_hold_fanin.out` |
| A | `apply_k2.py`, one real run | exit 0; `CHECK targets 2/2 byte-exact; write set = grant (2 created, 0 modified, 0 removed under projects/pec outside the run root); pinned 17/17 unchanged` | `apply.out` |
| 2 | `validate_scope_of_work.py` ×2 | `PASS format=SOW_V1` ×2 after A, after C8 and at the final head | `validate_DEL-*.out`, `validate_DEL-*_postC8.out`, `final_validate_DEL-*.out` |
| 3 | `derive_review_checklist.py`, twice each | exit 0; 17 and 19 items (= AC definitions 17 and 19); reruns byte-identical; `2227dbeb85fa807763bdd4a7b899fd8f406586a2f49533e3ece6c660bd659641` and `8e07ff3ef26e8b413109e8bd71204e28eb2ae15b77b4e6dc851900db63bcba30`, equal to the prepared values; equal again at the final head | `checklist_DEL-*.out`, `checklist_DEL-*_rerun.out`, `checklist_DEL-*.rerun.json`, `../checklist_DEL-*.json` |
| 4 | `check_boundary_owner_resolution.py --json … --show-not-checkable` ×2 | exit 0; "boundary requirements checked: 1 \| per-act exclusions for skill QA: 0 \| … \| contracts failing: 0" each; no `UNRESOLVED_OWNER`/`UNDEFINED_CLAIM`; 0 `NOT_CHECKABLE`. Hand resolution as tabled in the proposal, independently checked by the verifier (item 21, with Note 2) | `boundary_DEL-*.out`, `../boundary_DEL-*.json` |
| 5 | `verify_k2_quotes.py --tree . --gitdir . --prep <run root> --observation 125cfacc1` | `RESULT PASS 137/137`; "DEP rows citing this contract: 0" ×2; again at the final head on base `3e861f53c` | `verify_quotes.out`, `final_verify_quotes.out` |
| 6 | `verify_k2_state_claims.py --gitdir . --prep <run root>` | `RESULT PASS 482/482`; again at the final head | `verify_state_claims.out`, `final_verify_state_claims.out` |
| 7 | `check_cited_ids.py --commit 125cfacc1`; `scan_old_s2_text.py --prior ce934ac33 --current 125cfacc1` | `RESULT PASS 0/0`; `RESULT PASS stale=0 current=43`; both again at the final head | `check_cited_ids.out`, `scan_old_s2_text.out`, `final_*` |
| 8 | Lifecycle: `git diff --name-status origin/main...HEAD -- '**/_STATUS.md'` | empty after A and C8 (before S); after S exactly the two `_STATUS.md` files, with the tabled postimages `75366b6b…a127` and `3771d526…e567` at `{D}` = 2026-09-26 (no slot-rule difference) | `lifecycle_preS.out`, `final_lifecycle.out`, `../S_TASK_RETURN.md` |
| 9 | `validate_decomposition_registers.py --strict projects/pec/execution` | exit 1, 0 errors, 26 warnings (the pre-existing `XRG-013` set, D-GOV-48 owner-deferred); output **byte-identical** before A, after A, after C8, and at the final head (after S and the base merge) | `strict_{pre,postA,postC8,final}.out`, `state_compare.out` |
| 10 | `harness.py self-check`; `validate_pec_loop_receipts.py --repo-root .`; `analyze_dep_closure.py projects/pec/execution` | harness exit 0 and receipts exit 0 at every point; closure exit 0, circular dependencies PASS, 0 bidirectional pairs; each output identical at the four points (closure stdout compared without its command-echo line, which names the per-point output directory; `closure_summary` compared with timestamp and path keys removed, as `run_k2_checks.sh` does) | `harness_*.out`, `receipts_*.out`, `closure_*.out`, `closure_summary_*.json`, `state_compare.out` |
| 11 | C8: `apply_k2_c8.py --check-only`, then one real run | check-only exit 0 (`planned write set 1 modify`); apply exit 0, `CHECK target byte-exact; write set = grant (0 created, 1 modified, 0 removed …); pinned 3/3 unchanged`; the file equals `609aa807…5693`; the diff is the one tabled line; rows 9 and 10 unchanged | `c8_checkonly.out`, `c8_apply.out`, `c8_diff.out` |
| 12 | Containment: `git diff --name-status origin/main...HEAD` | outside the run root exactly 6 paths: the two created contracts, the two `_STATUS.md` (S), DEL-10-13 `_DEPENDENCIES.md` (C8), and the brief copy `AgentRuns/.../briefs/K2A_D103_SOW_ACT.md`; everything else is under `SOW_INIT_K2_2026-09-26/`. The return file `AgentRuns/.../returns/K2A_D103_SOW_ACT.md` is added last | `containment_preS.out`, `final_containment.out` |
| 13 | `git diff --check origin/main...HEAD` | clean (exit 0) before S and at the final head | `whitespace_preS.out`, `final_whitespace.out` |

## Pins at the final head

`final_pins.out`: `apply_k2.py`'s 17 pins hash 14/17 as tabled. The three that differ are exactly the granted postimages: both `_STATUS.md` (S) and DEL-10-13 `_DEPENDENCIES.md` (C8). At A time all 17 matched (row A). `apply_k2_c8.py`'s 3 pins match 3/3. (Verifier Note 1.)

## Base movement

During the act `origin/main` moved from `d385b6a19` to `3e861f53c` (PR #983). `git diff --stat d385b6a19 3e861f53c -- projects/pec _DomainEngines tools workflows docs AGENTS.md agents` is empty: only Piping files changed, and no pinned file or quoted locus. The base was merged into the branch (`c0d4098ca`, no rebase), and the quote and state-claim verifiers, cited IDs, old-S2 scan, validators, checklists, strict registers, harness, receipts and closure were rerun at that head with the results above.

## Independent verification

`VERIFIER_VERDICT_01.md`: PASS WITH NOTES; 0 BLOCKING, 0 NON-BLOCKING, 6 NOTEs. The verifier also reran `run_k2_checks.sh` on a clean export of `d385b6a19` (`OVERALL PASS`, including fault injection 19/19). Dispositions are appended to the verdict.

## Not run

- The rerun-refusal (a second `apply_k2.py` or `apply_k2_c8.py` run in the worktree) was not performed, because the brief allows one run of each. The verifier's export rerun exercised it (`rerun refuses 1` for both).
- Re-audit: not recommended by the proposal and not run.
- Source-only, kill-test and parity checks: not applicable (no capability changed).
