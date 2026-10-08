# T3-B1 merged: #1154 at `f4a0430412`

WORKING_ITEMS (Agent 1), 2026-10-08 UTC.

**The merge.** [#1154](https://github.com/sgttomas/chirality/pull/1154) merged at 17:24:49Z as merge commit `7eae707bb7`.
- Parents: main `9f1f96b17b` and the PR head `f4a0430412` (`_run_records/PARENTS.txt`).
- Command: `gh pr merge 1154 --merge --match-head-commit f4a04304…` (`_run_records/MERGE_COMMAND.txt`).
- The head is two commits on main `953d8c9446`: the code `7f5f72912e` (NUM `31eed8497f`'s 33 maintained files) and the package `f4a0430412` (`IMPLEMENTATION/B1/`, 7 files). Main's diff is 40 files.
- Main moved from `953d8c9446` to `9f1f96b17b` after the cut: App v4 only, with 0 paths under P. The PR was CLEAN at the merge.

## Gates

| Gate | Result | Evidence |
|---|---|---|
| Independent complete-diff review | RV125 (RV-X): PASS 0/0/7 at `0752ae8b98`, and CONFIRMED the platform test repair (0/0/1) | `R/REVIEW_RV125/b1_x_01/` |
| Pass B | I107: no stop. RV124 CONFIRMED it (0/0/2) | `R/I107/b1_passb_01/`, `R/REVIEW_RV124/b1_passb_01/` |
| Source equality, citations, GEN-8 | Pass on the final head | RR "RV125 confirms PR-B1's platform test repair; …" |
| Hosted CI on `f4a0430412` | Every automatic run succeeded. The full-SHA dispatch 37808185743 succeeded (`target_base` `953d8c9446`, mode full). The earlier dispatch 37806597259 failed at selection, because its `target_base` `dd50b1692c` is not in the head | `_run_records/CI_RUNS_f4a0430412.txt` |
| Exact-head Mac DEC-025 against a fresh main baseline | **`ALL-DONE`** (label `B1_f4a0430412_r2`). Baseline: `WT/main-baseline` at main `dd50b1692c`, whose P equals `953d8c9446`'s. Both sides used fresh targets | `dec025/` |
| src-tauri suite, head and main | 116 = 116; the sorted test lines are identical | `dec025/srctauri_*` |

## DEC-025 in detail (`dec025/`)

- **The sweep** stopped at PP's known Mac `t13`.
- **The 40 manifests** (`cmp_cargo.json`):
  - base 2,723 ok, 11 ignored, 3 FAILED; candidate 2,776 ok, 80 ignored, 3 FAILED;
  - **0 changed outcomes.** The 3 failures are the same known Mac tests on both sides (`t13` and the two `load_reference` both-mode tests);
  - **added 131:** 54 ok (the pre-freeze gate's 53, plus the platform fix's ring test) and 77 ignored (the per-mode witness and challenge entry points SQ runs);
  - **removed 9:** the pre-freeze gate's 9 renames.
- **pytest:** 4,426 passed and 32 skipped, with 132 subtests. Collection: main 3,833, head 4,458, so +625, B1's reader and corpus tests. Every collected test passed, apart from the same 32 skipped.
- **vitest:** 141 files and 4,245 tests passed. Main's piping desktop is unchanged since SI1c's 3,620, so +625.
- **Builds:** `build:wasm:desktop` and `build:desktop` exit 0.

## After the merge

- NUM absorbed main at `a232d1edd5`. NUM equals main outside `P/execution`.
- PR-N is cut from main next (I109's norm and re-pins).
- J0 on `b2` waits for PR-N and the pressure retirement.
- **RV125's text notes N-4, N-6 and N-7** are corrected in the merged package itself (I108's refresh for `7f5f72912e`: PR_BODY lines 12–13, CHANGE_RECORD's erratum), so no qualification is carried here.
