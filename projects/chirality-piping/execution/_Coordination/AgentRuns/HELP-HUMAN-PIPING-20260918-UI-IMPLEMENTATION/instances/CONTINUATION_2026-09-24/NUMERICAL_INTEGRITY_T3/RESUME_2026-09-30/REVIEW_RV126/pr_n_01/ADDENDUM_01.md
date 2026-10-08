# RV126 (RV-N), addendum 01: confirmation of PR-N's repair round 01

**Who:** RV126, TASK (Type 2), for WORKING_ITEMS for T3 (Agent 1), 2026-10-08 UTC. I wrote none of this code.
**Basis:**
- my review, `REVIEW.md` in this folder (`3ca41a9e…`);
- RR "PR-N (#1163), RV126's B-1: the platform-independent rank screen is accepted, option (i)";
- I109's record `R/I109/pr_n_repair_01/RETURN.md`;
- WORKING_ITEMS' request: confirm each item, give the verdict at `0c7490e1be`, and reconcile FK's 550 against my 499.

**The head:** #1163 at **`0c7490e1be723fd72c762403e282e2d789f3af38`**. On top of the reviewed `dab19291a8` it adds:
- `8ca80508b6`, the repair commit: 3 production files (comment-only) and 2 test files;
- `0c7490e1be`, the package: CHANGE_RECORD.md, PR_BODY.md and SHA256SUMS.

**Placeholders:** as in `REVIEW.md`. `A` is now my archive of `0c7490e1be` (`P/execution` excluded). `E1` = `_run_records/addendum_01/`.

## Verdict: **PASS** at `0c7490e1be`: 0 BLOCKING, 0 SHOULD-FIX, 8 NOTE (all eight answered)

- **B-1 is closed by ROOT's ruling** (option (i)), and the package states what the ruling requires.
- **S-1 is repaired** within the ruling: the code commit's message is not recut.
- **N-1 to N-8 are all answered.**
- **The production edits are comment-only and line-neutral.** The two edited tests pass in my run at the head.
- **No new finding.** One wording point (the package's "RV126 ran all four at `dab19291a8`") is accurate in substance; it is explained under N-6.

## The items

| ID | Status | Evidence at `0c7490e1be` |
|---|---|---|
| B-1 | **CLOSED by ruling** (option (i), accept) | ROOT's ruling keeps `d538f469af`. **The package states the decision changes:** CHANGE_RECORD §1 (the rank-screen row and the new paragraph "The rank screen's changed decisions") and §2, and PR_BODY ("The rank screen"). They cover the band changes in both directions (59,600 and 66,967 of 1,045,305 probes, within 1.5·10⁻³ relative of the threshold), the witness-class change at 10²⁰⁰ scale (1 of 300,000, changing the refusal's integrity code), and N-5's node motions (22,966 of 246,587). **Each number equals `REVIEW.md` §2a and `E/results/`.** "No true mechanism is admitted" and "no committed pin moves" are as I reported. The rank-screen code is unchanged since the review (`rigid_body.rs:53`, `:109`) |
| S-1 | **CONFIRMED REPAIRED** | **The comment:** `PP/src/lib.rs:38` now reads "magnitudes formerly formed with libm `hypot` are correctly rounded norms; `source_receipt::scaled_norm` and `displacement_magnitude` stay deterministic IEEE, not correctly rounded". It is accurate, and still one comment line. **The package:** CHANGE_RECORD §1 replaces the sentence ("Every magnitude formerly formed with libm `hypot` is now a correctly rounded norm"), adds a bullet naming both unchanged magnitudes, and quotes the code commit's two overbroad sentences as corrected. Its description of `scaled_norm` matches `PP/src/source_receipt.rs:46-53`. PR_BODY's second bullet carries the same correction. **The messages:** the repair commit's message states the correction. Per the ruling, the code commit's message stays as written and the merge record notes it |
| N-1 | **CONFIRMED** | `PP/tests/preview_physics_runtime.rs:6-8`: the header now excepts m08's use of FK's `correct_norm::norm2`, "verified against an exact oracle". The m08 tests pass (below) |
| N-2 | **CONFIRMED** | `FK/src/rigid_body.rs:465-466` and `:542-543` now contrast K5's forms with `assess_rigid_body`'s `norm2(ζ, 1)` (formerly `hypot`) and cite `:89-132`. That range is the Jacobi at the head: line 89 opens it, and the sweep loop closes at 132 |
| N-3 | **CONFIRMED** | CHANGE_RECORD §1 and PR_BODY: "30 of the 32 product `hypot` calls now call the norm: every one that reaches published bytes, a receipt or diagnostic text, plus the rank screen … and `elastic_section` (no caller)" |
| N-4 | **CONFIRMED** | `FK/src/correct_norm.rs:6-10`: `mul_add` is "a correctly rounded fma (hardware, or the platform's `fma` where there is none)". CHANGE_RECORD §1 "Operations" makes the claim conditional on a correctly rounded `fma` and cites my wasm32 = aarch64 result. PR_BODY's first bullet does the same. §2's first bullet carries the condition |
| N-5 | **CONFIRMED** | Covered with B-1 above. The rank-screen row says L "scales a witnessed mechanism's published node motions", and the new paragraph gives the two published carriers (diagnostic text, retained wire) and 22,966 of 246,587 |
| N-6 | **CONFIRMED** | CHANGE_RECORD §3 names the four TS files. It separates I109's round-2 run (`retainedPrecision.test.ts` alone, 1,102) from mine (all four, 1,314). PR_BODY's Evidence says the same, and I109 also ran all four at `8ca80508b6` (1,314). **Wording:** the package says I ran them "at `dab19291a8`". In fact I ran them on an archive of `8dd64c1835` with `P/execution` excluded (`REVIEW.md` §5). That tree is identical to `dab19291a8`'s outside the execution records, so the statement is accurate in substance. No change needed |
| N-7 | **CONFIRMED** | CHANGE_RECORD §3 and §4 and PR_BODY record both dispatches as successes. I read both with `gh run view` (read-only). **37820998162** on `7bd84e0526`: success, numerical cargo suite included (read in the review). **37824479785** on `dab19291a8`: success in every job but the skipped accessibility barrier, the numerical cargo suite and the source-mode desktop E2E included (`E1/pr_state.txt`) |
| N-8 | **CONFIRMED** | `FK/tests/retained_k4/product_final_case_tests.rs:341-342` now expects the exact constants 13, +0 and `f64::from_bits(4)`. That last value is RN(√14)·2⁻¹⁰⁷⁴: √14 ≈ 3.742 rounds to 4 on the subnormal grid. The test passes (below) |

## The repair is comment-only and line-neutral

**Production files** (`git diff -U0 8dd64c1835 8ca80508b6` over `PP/src`, `FK/src` and `P/core/loads`):
- **0 non-comment lines changed.**
- **4 hunks:** `PP/src/lib.rs` `@@ -38 +38`, `FK/src/correct_norm.rs` `@@ -6,5 +6,5`, and `FK/src/rigid_body.rs` `@@ -465,2 +465,2` and `@@ -542,2 +542,2`.
- **File lengths are unchanged:** 24,516, 295 and 1,409 lines (`wc -l`).
- stress_recovery is not touched.

**The other changes:**
- **Tests:** the m08 header (+2 lines) and N-8's two lines.
- **The package commit** touches only the execution records: `git diff 8ca80508b6 0c7490e1be` outside `P/execution` is empty.

This agrees with I109's `line_neutrality.txt` and with WORKING_ITEMS' check.

## My checks at the head

These ran on an archive of `0c7490e1be`, with a fresh target and cargo through `t3_cargo.sh` (`E1/r1_results.txt`):

| Check | Result |
|---|---|
| FK lib, filtered to `i51_support_hypot_identity_order_zero_subnormal_and_failed_prefixes` and `correct_norm` | **4 passed, 0 failed** (480 filtered out). These are N-8's test and the norm's 3 unit tests |
| PP `--test preview_physics_runtime` | **26 passed, 0 failed**, the three m08 tests among them |

Not re-run:
- the full suites, readers and oracle. The production edits are comment-only and line-neutral, so my review's results stand. I109 re-ran PP, FK, RE, PY and TS at `8ca80508b6`, with 0 failures (`R/I109/pr_n_repair_01/_run_records/checks/`);
- `source_equality.py` and `check_citations.py`. WORKING_ITEMS and I109 report both pass at the head.

**The PR as filed:** #1163's head is `0c7490e1be` and its body equals `PR_BODY.md` there. The package's `SHA256SUMS` verifies 3 of 3: CHANGE_RECORD.md `220cd55a…`, PR_BODY.md `064953f3…`, citations.json `c89eea28…`. Hosted CI on the new head was still pending when I read it; that gate is WORKING_ITEMS'.

## FK's 550 against my 499: the same binaries agree; the runs selected different test targets

- **My review's FK run** was `cargo test --lib --test correct_norm_oracle --test k5_constrained_bodies` (`E/tools/run_crates.sh`): three test targets and no doc-tests.
  - The lib unit tests: 483 passed, 1 ignored (KF2's release-only cost test).
  - `correct_norm_oracle`: 1 passed, 1 ignored (the dump).
  - `k5_constrained_bodies`: 15 passed.
  - Total: 499 passed, 2 ignored (`E/results/crates_summary.txt`).
- **I109's run** was a plain `cargo test` over every FK test target (`R/I109/pr_n_repair_01/_run_records/tools/pr_n_repair_checks.sh`). Its `results.txt` has ten `test result` lines: the lib (483 passed, 1 ignored), the eight integration binaries in `FK/tests/` (`correct_norm_oracle` 1 plus 1 ignored, and `k5_constrained_bodies` 15, among them), and the doc-tests.
- **The difference:** the 51 extra tests come from the other six integration binaries (`k1_k2a_interaction`, `k2a_checked_formation`, `k2b_force_scaling`, `k5_scale`, `m03_skew_scope`, `s11_site_table`) and the doc-tests. Neither run had a failure.
- **Where the binaries overlap, the counts are identical.** N-8's test lives in the lib binary, which includes `tests/retained_k4/` by path. So it was in both runs, and in my addendum run.

## Host and records

- Every cargo went through `WT/tools/t3_cargo.sh` (`--locked --offline`). Nothing was installed, there were no Git writes, and no other job was signalled. `gh` was used read-only.
- `E1/` holds:
  - `run_r1.sh`;
  - `r1_results.txt`;
  - `pr_state.txt` (#1163's head and body, the package sums, the two dispatches).

  Machine paths in them are replaced by `WT`.
- The archive `WT/rv126/`, the scratch `WT/scratch/rv126_n/` and the target `WT/targets/rv126-r1` are deleted.
- `SHA256SUMS.addendum_01` covers this file and `E1/`. `REVIEW.md` and `SHA256SUMS` are unchanged.
