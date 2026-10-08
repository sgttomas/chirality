# I109 round 4: PR-N's repair round 01 (RV126's S-1 and notes; B-1 ruled)

TASK (Type 2), for WORKING_ITEMS for T3 (Agent 1). Brief: `R/BRIEFS/PR_N_REPAIR_01.md` (sha256 `7888bbea…`, verified). Basis: RV126's review `R/REVIEW_RV126/pr_n_01/REVIEW.md` (`3ca41a9e…`) and ROOT's ruling RR "PR-N (#1163), RV126's B-1: the platform-independent rank screen is accepted, option (i)", relayed by WORKING_ITEMS, so N-2 and N-5 were done in this round. B1_COMMON's rules apply, with WORKING_ITEMS in ROOT's place.

Placeholders: `WT` the T3 host root; `NUM` the numerics worktree; `P` `projects/chirality-piping`; `PP` `P/core/product_physics`; `FK` `P/core/solver/frame_kernel`; `T` the NUMERICAL_INTEGRITY_T3 instance; `R` `T/RESUME_2026-09-30`.

## 1. The commits

On `codex/piping-t3-correct-norm-20261008` in `WT/pr-n`, on top of `dab19291a8`. Not pushed; WORKING_ITEMS pushes and mirrors the product files into NUM.

| Commit | What |
|---|---|
| `8ca80508b6` | **The repair commit, for code and tests.** Its message states S-1's correction: the code commit `8dd64c1835` said that a published 3-component magnitude is the correctly rounded norm. In fact the magnitudes formerly formed with libm `hypot` are correctly rounded norms, while `source_receipt::scaled_norm` and `displacement_magnitude` are deterministic IEEE but not correctly rounded, and unchanged. It touches 3 production files (comment-only) and 2 test files. |
| `0c7490e1be` | **The package commit**: CHANGE_RECORD.md, PR_BODY.md and SHA256SUMS in `T/IMPLEMENTATION/PR_N/`. citations.json is unchanged, because the repair adds no record citation to maintained source. Before anything was pushed, I amended this commit once (from `d56f257cba`) to correct one sentence. That sentence said the repair changes 5 of the 21 maintained files. In fact it changes 4 and adds a fifth (see §5). |

The code commit's message is not recut, as the ruling says.

## 2. The items

| Item | Done in |
|---|---|
| S-1 | `PP/src/lib.rs:38` (repair commit); CHANGE_RECORD §1 (the sentence reworded, plus a new bullet naming the two unchanged magnitudes and quoting the code commit's overbroad sentences); PR_BODY's second bullet |
| N-1 | `PP/tests/preview_physics_runtime.rs` header. The intensified identity (m08) uses FK's `correct_norm::norm2`, which is verified against an exact oracle. |
| N-2 | `FK/src/rigid_body.rs:465-466` and `:542-543`. Each now says that K5's screen uses its own form in place of `assess_rigid_body`'s `norm2(ζ, 1)` (formerly `hypot`), and cites `:89-132` |
| N-3 | CHANGE_RECORD's call-sites sentence and PR_BODY's, in the wording RV126 gave |
| N-4 | `FK/src/correct_norm.rs` module header: `mul_add` is a correctly rounded fma, the hardware's or the platform's `fma`. CHANGE_RECORD §1 "Operations" states that the claim holds given a correctly rounded `fma` and cites RV126's result that wasm32 equals aarch64 on 2,721,296 results. PR_BODY's first bullet does the same. |
| B-1 / N-5 | CHANGE_RECORD §1: the rank-screen row, plus a new paragraph, "The rank screen's changed decisions". It covers the band changes (59,600 and 66,967 of 1,045,305 probes, within 1.5·10⁻³ relative of the threshold, where the libm decision was non-monotone and platform-dependent); the witness-class change at 10²⁰⁰ scale (1 of 300,000 bodies, which changes the refusal's integrity code); and the node motions (22,966 of 246,587 synthetic mechanisms; no committed pin moves). It cites RV126 §2a and ROOT's ruling. §2 adds a bullet for these, and PR_BODY adds "The rank screen" paragraph. |
| N-6 | CHANGE_RECORD §3 names the four TS files. Before this round I109 had run `retainedPrecision.test.ts` only (1,102 passed); RV126 ran all four (1,314 passed). In this round I109 ran all four at the repair commit (§4). PR_BODY's Evidence section says the same. |
| N-7 | CHANGE_RECORD §3 and §4 and PR_BODY record two dispatches, both read with `gh run view`. 37820998162 on `7bd84e0526` (21 files equal to `8dd64c1835`'s) succeeded, numerical cargo suite included. 37824479785 on `dab19291a8` succeeded: numerical cargo suite, source coverage and remainder, and the source-mode E2E. Both skipped the accessibility job. |
| N-8 | `FK/tests/retained_k4/product_final_case_tests.rs:341-342`: the expected values are the exact constants 13, +0 and `f64::from_bits(4)` (= RN(√14·2⁻¹⁰⁷⁴)) instead of a libm chain |

CHANGE_RECORD §4 now shows RV126's verdict: FAIL on B-1 only, B-1 ruled accept, and the repair round awaiting RV126's confirmation. It also marks the two dispatches as successes, notes that Pass B and I112 refer to `8dd64c1835`, which the repair leaves line-neutral, and adds rows for this round's checks. The other gates stay pending; WORKING_ITEMS gives their verdicts.

## 3. Line-neutrality per production hunk

`_run_records/line_neutrality.txt` covers every production hunk of `8ca80508b6`, meaning every changed path under PP, FK and stress_recovery `src`. stress_recovery is not touched.

| Hunk | Lines | Comment-only | File length |
|---|---|---|---|
| `PP/src/lib.rs` `@@ -38,1 +38,1` | 1 → 1 | yes (`//`) | 24,517 → 24,517 |
| `FK/src/correct_norm.rs` `@@ -6,5 +6,5` | 5 → 5 | yes (`//!`) | 296 → 296 |
| `FK/src/rigid_body.rs` `@@ -465,2 +465,2` | 2 → 2 | yes (`///`) | 1,410 → 1,410 |
| `FK/src/rigid_body.rs` `@@ -542,2 +542,2` | 2 → 2 | yes (`//`) | (same file) |

Every hunk starts and ends at the same line numbers, so line numbers, `line!()` and every code line are unchanged. Two hunks are doc comments (`//!`, `///`), which rustdoc reads; they do not enter code generation.

## 4. The suites, at `8ca80508b6`

These ran on the Mac with fresh targets `WT/targets/i109-n4-{crates,pybins,wasm}`. Every cargo went through `WT/tools/t3_cargo.sh` (`--locked --offline`) and vitest and pytest through `WT/tools/t3_slot.sh`, one job at a time. The script is `_run_records/tools/pr_n_repair_checks.sh`; the results are in `_run_records/checks/` (`chain.log`, `results.txt`).

| Suite | Result |
|---|---|
| PP (`cargo test`, Git archive of the revision) | 743 passed, 0 failed, 79 ignored; m08's three tests ok |
| FK | 550 passed, 0 failed, 2 ignored; `i51_support_hypot_identity_order_zero_subnormal_and_failed_prefixes` ok |
| `result_export` | 199 passed, 0 failed |
| PY: `test_retained_precision_contract.py`, `test_retained_precision_schema.py` (with the checked-JSON and units binaries built from the archive) | 1,079 passed |
| TS: `retainedPrecision.test.ts`, `retainedPrecisionIntegration.test.tsx`, `retainedPrecisionResultExport.test.tsx`, `retainedPrecisionStressNeutral.test.tsx`, exactly the four files that read the corpus | 4 files, 1,314 passed |

The TS run used the worktree. Its tree outside execution equals `8ca80508b6`, and the script checks this before running. Its prerequisites are ignored by Git:
- `node_modules`, an APFS clone (`cp -cR`) of `WT/t3-norm`'s install, made against the same `package-lock.json` and `package.json` files. Nothing was installed.
- The wasm engine, built from the archive as `scripts/build-wasm-engine.mjs` builds it (cargo through `t3_cargo.sh`, then `wasm-bindgen --target web`).

RV126 recorded 499 FK tests; this run counts 550 across the crate's test binaries. I did not investigate the difference. Both counts have 0 failures.

## 5. Source equality and citations, at the new head `0c7490e1be`

**`source_equality.py`** (`T/IMPLEMENTATION/F2A_D1/`, unchanged): **PASS, checks 1–5**. Records: `_run_records/source_equality.{out,json}`.
- Run as `--pr 0c7490e1be --int ec7902ed24 --main 7eae707bb7 --package <PR_N>`.
- WORKING_ITEMS gave no NUM commit, so `--int` is a scratch head (`_run_records/scratch_int.txt`): NUM `8dac73c9a0`, whose non-execution tree equals `ef8ab78473`'s, plus the repair commit's 5 maintained files. It was made with `git commit-tree`; no ref exists and it was never pushed.
- B = `7eae707bb7`. **|S| = 22.**
- Checks 1, 2 and 5: all 22 paths are identical.
- Check 3: no merge was needed.
- Check 4: the 4 execution files lie inside the package, and the package sums verify.

**`check_citations.py`** (`--base 7eae707bb7 --head 0c7490e1be`, the package's unchanged `citations.json`): **PASS**. Resolved 1, ambiguous 0, unresolved 0; 0 verification failures; 0 unused entries; 0 code-line citations. Records: `_run_records/check_citations.out`, `citations_resolved.md`. The new comments' `(:89-132)` has no file prefix, so it is not a code-line citation, as with the `(:88-131)` it replaces.

**For WORKING_ITEMS's NUM mirror:** the PR now carries 22 maintained files, not 21. `FK/tests/retained_k4/product_final_case_tests.rs` (N-8) was not part of the code commit. The mirror has 5 files to take from `8ca80508b6`:
- `PP/src/lib.rs`;
- `PP/tests/preview_physics_runtime.rs`;
- `FK/src/correct_norm.rs`;
- `FK/src/rigid_body.rs`;
- `FK/tests/retained_k4/product_final_case_tests.rs`.

After the mirror, rerun `source_equality.py` with `--int` set to that NUM commit.

## 6. The package (`T/IMPLEMENTATION/PR_N/` at `0c7490e1be`)

| File | sha256 |
|---|---|
| `CHANGE_RECORD.md` | `220cd55a33807490705fa2f36b20f9d4cb57faffbe3c305604fd9c7c1896f395` |
| `PR_BODY.md` | `064953f3a6476c487a266597e41ec4d61177f1897b8d68a230335d2d745139c2` |
| `citations.json` | `c89eea2834aaecaa048405f01557de38149bde6185b54ffe13f8328b3161e754` (unchanged) |

The PR description on GitHub is WORKING_ITEMS's to update from PR_BODY.md.

## 7. Stops

None. The host accepted every edit, commit and record. No item needed a non-line-neutral production edit.
