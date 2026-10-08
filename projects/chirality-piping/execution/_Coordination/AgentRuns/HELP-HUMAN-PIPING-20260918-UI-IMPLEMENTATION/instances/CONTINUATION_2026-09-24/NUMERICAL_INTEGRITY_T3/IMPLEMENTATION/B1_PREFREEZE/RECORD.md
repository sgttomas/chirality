# B1's pre-freeze gates (PLAN_v2 §3.9): the 40-manifest cargo suite and the src-tauri suite

ROOT, 2026-10-08 UTC.

**What ran:** `run.sh`, in `git archive` copies under the lock.
- **Candidate:** `b1` `0d19f995b5` with `R/I104/b1_sq_01/registration.diff` applied. That is `ddc8eaaf54`'s product content, and PR-B1's.
- **Base:** main `2007709549`, `b1`'s main base.
- **The suite:** `WT/scratch/calib/run_suites_nff.sh`, CI's numerical cargo profile.

Every step exited 0 (`chain.txt`).

## The 40 manifests, test by test (`cmp_cargo.py`, `cmp_cargo.json`)

| | ok | ignored | FAILED |
|---|---|---|---|
| Base | 2,706 | 11 | 3 |
| Candidate | 2,758 | 80 | 3 |

- **Changed outcomes:** 0.
- **The 3 failures** are the same tests on both sides, the known Mac failures:
  - `s11g_tests::t13_committed_fallback_uz_is_byte_identical`;
  - the two `load_reference` both-mode tests.
- **Added: 130.**
  - 53 ok: PP's B1 unit tests, `retained_precision_contract` (17), `result_export` (2), and the challenge's bound test.
  - 77 ignored: the witness and challenge entry points, now per input and per mode (`::dense`, `::sparse`), plus the DEF-O and ordinary controls. SQ runs them explicitly (`R/I104/b1_sq_01/`; RV124 confirmed).
- **Removed: 9, all renames.**
  - 8 witness tests that were already ignored in the base. They return as the per-mode modules, and W2b becomes `witness_w2b_cap_maximal_passed_report_no_triggered_case`, as ruled.
  - The challenge's `retained_direct_peak_is_within_the_profiles_ordinary_span` (ok) becomes `retained_direct_peak_is_within_the_profiles_bounds` (ok).

## src-tauri

116 passed on both sides. The sorted test lines are identical (`srctauri_*_tests.txt`).

**Result: the pre-freeze gate passes.** pytest and vitest were run by the reader and corpus slices (SR, SC). The exact-head DEC-025 on PR-B1 covers every suite again.
