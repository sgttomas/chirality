# T3-PN merged: #1163 at `8b74dde497` (a correctly rounded norm replaces libm `hypot`)

WORKING_ITEMS (Agent 1), 2026-10-08 UTC.

**The merge.** [#1163](https://github.com/sgttomas/chirality/pull/1163) merged at 22:25:24Z as merge commit `ec5d397359`.
- Parents are main `f5014d7284` and the PR head `8b74dde497`; see `_run_records/PARENTS.txt` and `MERGE_COMMAND.txt`.
- **The head:** five commits on main `7eae707bb7` (PR-B1 merged):
  - `8dd64c1835`: the code, 21 maintained files;
  - `dab19291a8`: the package;
  - `8ca80508b6`: RV126's repair round 01. It is comment-only and line-neutral in production, with two test edits. It brings the maintained files to 22;
  - `0c7490e1be` and `8b74dde497`: the package refreshes, records only.
- **Main moved after the cut** from `7eae707bb7` to `f5014d7284`. Those commits touch App v4 only, with 0 paths under P.
- **The code commit's message is not recut.** It says every published 3-component magnitude is the correctly rounded 3-norm. The repair commit's message and the package correct that (RV126 S-1).
- **An earlier cut** (`c3b44875f5`, branch `…-pr-n-20261008`) overclaimed glibc in its message. No PR existed then, so it was replaced by a new branch and deleted.

## Gates

| Gate | Result | Evidence |
|---|---|---|
| Fresh independent review (RV-N) | RV126 FAIL on B-1 only at `dab19291a8`; then **PASS at `0c7490e1be`** (0/0/8). ROOT ruled B-1 option (i): RR "PR-N (#1163), RV126's B-1: the platform-independent rank screen is accepted, option (i)". RV126's own exact oracle: 0 misrounded in 2,801,296 | `R/REVIEW_RV126/pr_n_01/` |
| Pass B | I107: DELTAS TO READ, no stop. TEXT, forms and M unchanged. **RV124 CONFIRMED**, carried over to `0c7490e1be` | `R/I107/pr_n_passb_01/`, `R/REVIEW_RV124/pr_n_passb_01/` |
| T9 and the both-entry gate | I112 on `8dd64c1835`. **T9 PASS. Part 1 PASS, 884 of 884**, under ROOT's rule: RR "PR-N's T9 and both-entry gate: the acceptance rule is exact correct rounding with provenance, not an ulp budget". That covers 5,254 moved magnitudes, 10 of them by two ulps, and two diagnostic texts. gate_check found 0 trusted breach triples. **Part 2 PASS.** Carried over to the head (token-identical code) | `R/I112/pr_n_gates_01/` |
| Hosted CI | Every automatic run on `8b74dde497` succeeded | `_run_records/CI_RUNS.txt` |
| Full-SHA dispatches (`target_base` `7eae707bb7`) | 37824479785 (`dab19291a8`), 37833181297 (`0c7490e1be`) and 37850042817 (`8b74dde497`): success | as above |
| glibc diagnostics | 37808190331 (`b9dea77a85`) and 37820998162 (`7bd84e0526`, the re-pinned head): success | as above |
| Source equality, citations | Pass at `8b74dde497`, against NUM `eb94b91d3f` (22 files) | `_run_records/` |
| GEN-8 | 1 passed at `0c7490e1be` and at `8b74dde497` | `_run_records/gen8_*.txt` |
| Exact-head Mac DEC-025 against a fresh main baseline | **`ALL-DONE`** on `0c7490e1be` (label `PRN_0c7490e1be`; baseline `WT/main-baseline` at `7eae707bb7`). Carried over to `8b74dde497`, whose last commit is records only | `dec025/` |
| src-tauri, head and main | 116 = 116; the sorted test lines are identical | `dec025/srctauri_*` |

## DEC-025 in detail (`dec025/`)

- **The sweep passed every surface on the Mac**, the first time it has done so: no Mac platform failure remains.
  - The sweep marked the tree "dirty". The only dirty path was the untracked summary that PR-B1's run had left in `validation/evidence/sweeps/`, not source.
  - That file has been moved out of the worktree.
- **40 manifests** (`cmp_cargo.json`):
  - base 2,776 ok, 80 ignored, 3 FAILED; candidate 2,786 ok, 81 ignored, **0 FAILED**;
  - **changed: 3**, each FAILED → ok: `t13` and the runner's two `load_reference` tests;
  - added 11: the norm's unit tests in frame_kernel and stress_recovery, the oracle vectors and the dump, and 3 frame_kernel doc tests renamed by a one-line shift;
  - removed 3: those renames.
- **pytest:** 4,426 passed, 32 skipped. **vitest:** 141 files, 4,245 tests. **Builds:** exit 0. All three equal main's after PR-B1.

## After the merge

- NUM absorbed main at `becc8d8456`; NUM equals main outside `P/execution`.
- **Next for T3:** U3, the legacy pressure retirement (Stage 1 and Stage 2 as one PR), enters NUM. Then comes J0 on `b2`, with the Mac pins re-taken at the correctly rounded bytes.
- **Not done here:** the remaining libm calls on product paths (sin, cos, atan2, asin, exp, exp_m1) are a later round (CHANGE_RECORD §2).
