# I109 round 2: PR-N's re-pins on the norm branch

TASK (Type 2). The return path is WORKING_ITEMS for T3 (Agent 1), by the owner's decision of 2026-10-08 (RR "Owner decisions: …; T3 gains a WORKING_ITEMS manager"). The brief is `R/BRIEFS/PR_N_REPIN_01.md` (sha256 `10d3ce93…`). Round 1 was ruled in RR "I109: a correctly rounded norm replaces libm `hypot` on published paths; …".

Host rules are B1_COMMON's:
- every cargo through `WT/tools/t3_cargo.sh` (`--locked --offline`), queued behind ROOT's DEC-025;
- one heavy job at a time;
- no installs.

Scratch was `WT/scratch/i109_norm/` and targets `WT/targets/i109-n2-*`.

## 1. Result

- **Branch** `codex/piping-t3-platform-norm-20261008` in `WT/t3-norm`. Head **`7bd84e0526`**, which is not pushed. On top of `b9dea77a85` (WORKING_ITEMS' merge of NUM `acd5bb51bc`) come three re-pin commits. Each touches product files only, with no records:
  1. `f3939f2141`: re-pins every affected pin to the correctly rounded bytes, so there is one pin for every platform. It retires B1's glibc variants, makes u1 unconditional and gives m08 `norm2`.
  2. `e4ec1cb5c9`: the ring check's absolute escape now applies only to the near-zero residues (RV125 A1-N1).
  3. `7bd84e0526`: the PY reader's 07n snapshot pins move to the re-pinned successors.
- **glibc (run 37808190331, head `b9dea77a85`): success,** with the numerical cargo suite and every job green (§2).
- **The 40 manifests on the Mac:**
  - Result: 2,786 ok, 81 ignored, **0 FAILED**. This ran on `e4ec1cb5c9`. `7bd84e0526` adds only a Python file, so the cargo run applies to the head.
  - Against round 1's base (NUM `af53e1447c`), **3 outcomes change**, all FAILED to ok: `t13` and the runner's two `load_reference` tests.
  - **12 tests are added:**
    - the norm's 3 unit tests in frame_kernel and the same 3 in stress_recovery;
    - `correct_norm_vectors` and the dump entry;
    - the merged `cap_maximal_ring_is_the_trigonometric_ring`;
    - 3 frame_kernel doc tests renamed by a line shift, which are also the 3 removed.
  - **Reader suites on the head:**
    - PY: `test_retained_precision_contract.py` and `test_retained_precision_schema.py`, 1,079 passed;
    - TS: `retainedPrecision.test.ts`, 1,102 passed.
- **The D1 call graph:** 16 of the norm's 17 production call sites lie in the retained route's call graph. Only `elastic_section.rs` does not (§4).
- **Request:** a Linux dispatch of `7bd84e0526` (§5).
- **Stops:** none.

## 2. glibc: run 37808190331

The run is a `workflow_dispatch` on head `b9dea77a85`: the four round-1 commits plus B1's platform fix through NUM. **Every job succeeded,** including the numerical cargo suite over all 40 manifests (`_run_records/glibc/`). Read against round 1's §6 items:

**What it establishes:**
1. **`t13` and the runner's two `load_reference` tests pass on glibc.** They now also pass on the Mac (§3). The committed documents `fallback_uz` and `load_reference/connected` are therefore produced byte for byte on both platforms.
2. **W-C2 dense: the norm on glibc produces I107's glibc variant document exactly.** On Linux, `b1_sp_w_c2_fixtures_are_the_live_successors` compares the live successor through the private driver with the fixture plus `W_C2_DENSE_GLIBC`'s three replacements. Round 1 showed that this variant document is byte-identical to the Mac candidate's (`c11f7566…`). The bytes are therefore equal across platforms, and they are the bytes the Mac fixture is now re-pinned to.
3. **SF-2 (C, B, A) dense:** `CBA_DENSE_GLIBC` holds on glibc. That pair equals the Mac candidate's pair, which is the new `CBA_PINNED` dense.
4. **m08 passes on glibc.** Its expectation used glibc's `hypot` and the product used `norm2`; they agree on those inputs. glibc was correctly rounded there, as it was on `rigid:N0`.
5. **The W2b input pins pass on glibc** with B1's bit-spelled ring.

**What it does not establish:**
- **The Direct-entry W-C2 pins.** `W_C2_PINNED`'s document, receipt and bytes come through the registered Direct entry, which is Stale on Linux, so the test asserts only the plain bytes there.
- **u1's ordinary hash on glibc.** At `b9dea77a85` it was still asserted on aarch64 macOS only. The re-pinned head asserts it everywhere, and the requested run is the first to check it.
- **Bitwise equality of every published byte across platforms.** It shows equality only where a pinned document is compared. The remaining libm calls on product paths (sin, cos, atan2, asin, exp, expm1; round 1 §7) are not exercised by any pin that would differ, so their platform dependence is unmeasured.
- **Release builds.** CI and these checks run debug tests. Round 1's oracle showed debug and release give identical norm bits.

## 3. The re-pins and the checks on the Mac

Every moved pin moves by **one value of 1 ulp and the hashes over it**: case C's `rigid:N0` support force magnitude, `1.6258317075882521e-12` to the correctly rounded `1.6258317075882523e-12`.

| Item | Change |
|---|---|
| `fixtures/results/retained_precision_w_c2_successor_dense_scrutiny.json` | The value, `publication_sha256` `57624d75…` → `35fa7aca…` and `receipt_sha256` `612e23ca…` → `ca6a62a6…`; file sha256 `f2800bd4…` → `c11f7566…` |
| `W_C2_PINNED` dense | (`c11f7566…`, `ca6a62a6…`, `604e4a33…`) |
| `CBA_PINNED` dense | (`255785d2…`, `a320a5d3…`) |
| B1's glibc variants | `GLIBC`, `W_C2_DENSE_GLIBC`, `W_C2_DENSE_GLIBC_RECEIPT`, `w_c2_on_this_platform` and `CBA_DENSE_GLIBC` removed. The fixtures test compares with the fixture again, on every platform. |
| u1 `ORDINARY_SHA256` | `ORDINARY_PINNED_TARGET` removed, so the assertion runs on every target. Dense is (69366, `aa8b93ba…`). Its later dense assertions, including the milestone successor, pass unchanged. |
| m08 (`preview_physics_runtime.rs`) | The expectation is `sif * (norm2(My, Mz) / Z)`, exact on every platform. |
| Reader corpus `retained_precision_cases.json` | Case `w_c2_dense_scrutiny`: its source equals the re-pinned fixture's, and `provenance.fixture_sha256` and `receipt_sha256` change. Case `sf2_c_b_a_dense_scrutiny`: its source equals the new (C, B, A) successor, with `successor_bytes_sha256`, `receipt_sha256` and `publication_sha256` updated. Mutation `f1_p4_parity_on_w2_published_case_a_dense` gets the value in its `set results`, so it is still the new base plus one row. That is 11 lines in all, each checked by parsing. |
| PY reader `test_retained_precision_contract.py` | `N07_W_C2` dense and `N07_PP_PINNED["sf2_c_b_a_dense_scrutiny"]` take the same hashes. |
| Ring check (RV125 A1-N1) | The absolute 1e-14 escape now covers only the three nonzero near-zero residues (N8's x, N16's y, N24's x), and they are counted. Every other coordinate, N0's exact 0 included, must be within one ulp. |
| `t13` and the runner's `load_reference` tests | No change. The product tree has no known-failure listing of them: `git grep` finds only their definitions. |

**The checks**, with fresh targets and every cargo through `t3_cargo.sh` (`_run_records/checks/`):

| Check | Revision | Result |
|---|---|---|
| PP suite | `e4ec1cb5c9` | 743 passed, 0 failed, 79 ignored |
| `result_export` suite | `e4ec1cb5c9` | 199 passed, 0 failed |
| 40 manifests | `e4ec1cb5c9` | 2,786 ok, 81 ignored, 0 FAILED |
| PY reader, the two corpus files | `7bd84e0526` | 1,079 passed |
| TS reader, `retainedPrecision.test.ts` | `7bd84e0526` | 1,102 passed |

- **First runs, fixed in the commits above:**
  - On `c11acb3a22`, the ring check counted 4 residues: N0's exact 0 matched `< 1e-14`. The amended `e4ec1cb5c9` excludes zero.
  - On `e4ec1cb5c9`, the PY suite failed once, on `N07_W_C2`. That is the third commit.
- **TS prerequisites:**
  - **The wasm engine:** the TS setup requires it. It was built as `scripts/build-wasm-engine.mjs` builds it: `operation_applier`, wasm32, `--features wasm --release` through `t3_cargo.sh`, then `wasm-bindgen 0.2.123 --target web` into the gitignored `public/wasm-engine`.
  - **`node_modules`:** an APFS clone of an existing T3 install with the same `package-lock.json` (non-optional packages identical). Nothing was installed.

## 4. The D1 call graph: where the norm is called

This uses SQ's call graph (`R/I104/b1_sq_01/_run_records/chain/callgraph_g5.py`). It was run with SQ's `run_point.sh` settings (rules `callgraph_rules.g4.json`, `crate_dirs.txt`, the extra dependency PP to `result_export`) on `c11acb3a22`'s `P/core`, from the root `run_linear_static_preview_value_with_retained_direct`. Of 3,497 nodes, 2,813 are reachable from the root. `norm2`, `norm3` and all their helpers are among them. Two same-named local functions are excluded: formation_check's wide `norm3` and final_case's enclosure `norm2` (`_run_records/d1/`).

| Call site (at the head) | Function | In D1 |
|---|---|---|
| `PP/src/lib.rs:4928`, `:5124` | `solve_load_case_observed` (ordinary support magnitude; formation guard q) | yes |
| `PP/src/lib.rs:11876`, `:11882` | `append_signed_support_results` (support-action magnitudes) | yes |
| `PP/src/lib.rs:13511` | `append_combined_vector_magnitude` | yes |
| `PP/src/preview_physics.rs:465`, `:634`, `:966`, `:967` | `tangent_diagnostics`, `render` (intensified), `append_combination_results` | yes |
| `PP/src/pressure_runtime.rs:1082`, `:1100` | `traverse_region` | yes |
| `PP/src/retained_product.rs:2446` | `observables_view` (the retained support guard) | yes |
| `PP/src/case_state/resolve.rs:899` | `resolve_case` (reference length) | yes |
| `P/core/solver/frame_kernel/src/structural/retained/product_certificate/final_case.rs:1851` | `support_hypot` (the certificate's projection) | yes |
| `P/core/solver/frame_kernel/src/rigid_body.rs:53`, `:109` | `assess_rigid_body` | yes |
| `P/core/loads/stress_recovery/src/elastic_section.rs:106` | `evaluate_elastic_section` | **no** |

The ordinary-route sites are in D1 because the Direct entry runs the ordinary route, which is D1's single plain run.

- **Correction to round 1:** `evaluate_elastic_section` has **no caller** outside its own module and tests (`git grep`). Round 1's inventory row for it ("published bytes: stress rows, maxima") is wrong: it reaches no product output. Its replacement keeps the public function platform-independent, nothing more.
- **For Pass B:**
  - `correct_norm` allocates nothing; it uses fixed `[f64; 10]` stack arrays and is not recursive.
  - Its correction `loop` has no static bound in its form. By construction it runs at most two iterations: one ulp move and the final check. The candidate is one rounding, at most two with a subnormal destination, of a double-double root accurate to about 2⁻¹⁰⁰, so it is RN or a neighbour of it.
  - If Pass B's loop scan needs a static bound, that is a code change: a counted loop with the same body.

## 5. The Linux dispatch request

Please run a hosted-CI diagnostic dispatch of `codex/piping-t3-platform-norm-20261008` at **`7bd84e0526`** (full SHA `7bd84e0526a8480c9d5572a4e647fe247b9980e1`), with at least the numerical cargo suite. Expect 0 failures. The first-time checks there are:
- u1's ordinary pins on glibc: sparse (68250, `9c7ec1a1…`) and dense (69366, `aa8b93ba…`);
- the W-C2 fixtures test, now comparing with the single fixture;
- SF-2 with the single `CBA_PINNED`;
- m08 with `norm2`;
- the tightened ring check against glibc's `cos`/`sin`, within one ulp except the three residues.

The Direct-entry W-C2 pins still take the Stale path on Linux. PY and TS run in their own CI jobs if the workflow includes them.

## 6. Records

All paths are relative to this folder. It was written at the R path inside `WT/t3-norm`, untracked; `WT/numerics` was not touched.
- `_run_records/checks/`:
  - the chain log and both crate results;
  - the 40-manifest summary, `manifests.txt` and the comparison with round 1's base (`.json`, `.txt`);
  - the reader logs and tails;
  - the first-run failures.
- `_run_records/glibc/`: run 37808190331's jobs, conclusions and numerical steps.
- `_run_records/d1/`: `d1_norm_sites.json` and the call graph's `cg.out.json`.
- `_run_records/tools/`: `pr_n_checks.sh`, `pr_n_readers.sh`, `d1_norm_sites.py`, `suites40.sh`, `cmp_suites.py` and `sums.py`.
