# I109: platform-independent published norms (a correctly rounded `hypot`) and the libm inventory

TASK (Type 2) under ROOT (HELP_HUMAN, Agent 0). Brief: `R/BRIEFS/PLATFORM_DETERMINISM_01.md` (sha256 `f4b45068…`). Common rules: `R/BRIEFS/B1_COMMON.md` (`2d170307…`). Motivation: RR "I107's Pass B (no stop); PR-B1's hosted CI fails on Linux: …".

Scratch was `WT/scratch/i109_norm/`; targets were `WT/targets/i109-*`. Every cargo ran through `WT/tools/t3_cargo.sh` (`--locked --offline`), one heavy job at a time. Nothing was installed, and no DEC-025, RSS or timing measurement was run.

## 1. Result

- **Branch** `codex/piping-t3-platform-norm-20261008` (worktree `WT/t3-norm`), from NUM `af53e1447c`. Head **`cd8e710039`**: four commits.
  1. `c613c68160`: the norm, `P/core/solver/frame_kernel/src/correct_norm.rs` (`norm2`, `norm3`). It comes with unit tests, 1,200 committed exact vectors and the oracle's dump entry.
  2. `c8369cfda2`: every published-path `hypot` now goes through the norm (PP, the retained certificate and stress_recovery).
  3. `d538f469af`: the rigid-body rank screen goes through the norm. This is an admission decision, and it closes that T3-close item. It is separable, so ROOT can drop it to keep only published values.
  4. `cd8e710039`: a comment-only rewording of the module's proof sketch.

  The measurement below ran on `d538f469af`. The difference to the head is that comment only.
- **The oracle:** 0 misrounded results out of 22,000,000. That is norm3 and norm2 on each of 11,000,000 triples: 10,000,000 random ones across the whole range and 1,000,000 adversarial ones. They were checked against exact integer square roots. Debug and release builds give identical bits.
- **The inventory:** 578 calls on 431 lines.
  - Product code: 123 calls, 87 of them platform-dependent libm (hypot 32, sin 23, cos 25, atan2 2, asin 1, exp 3, exp_m1 1).
  - Readers: 54 calls.
  - Tests: 401 calls.
  - **30 of the 32 product `hypot` calls are replaced.** The other 2 are in `performance_harness`, which is not a product dependency.
- **Moved bytes on the Mac:** five tests move, every one by **one value of 1 ulp** plus the hashes over it (§5). Two committed pins/fixtures move, one hash-only pin moves, one test-side expectation moves, and two reader-corpus entries move.
  - Of the 66 committed request and model fixture envelopes, 62 are byte-identical, and 5 values (all 1 ulp) move in the other 4.
  - The candidate reproduces **all 30** committed raw fixtures. The base reproduces 27 of them.
- **`t13` passes on the Mac.** So do the runner's two `load_reference` both-mode tests. Those were the three known Mac failures.
- **Linux:** the CI dispatch request is in §6. A strong prior result is already in hand:
  - the Mac candidate's W-C2 dense document is **byte-identical** to I107's glibc variant document;
  - its (C, B, A) dense pin equals I107's `CBA_DENSE_GLIBC`.

  The glibc W-C2 and (C, B, A) platform pins are therefore expected to become unnecessary. The cap_maximal ring pins (sin/cos) are not affected by this work.
- **Stops:** none.

## 2. The norm

`correct_norm::norm2(a, b)` = RN(√(a² + b²)) and `correct_norm::norm3(a, b, c)` = RN(√(a² + b² + c²)). Both round to nearest, ties to even.

- **Operations:** only IEEE `+ − × ÷`, `sqrt` and `f64::mul_add`. All of these are correctly rounded, Rust never contracts, and `mul_add` is a correctly rounded fma in hardware or software. Every platform therefore gives the same bits.
- **Method:**
  1. Sort the absolute values in descending order and scale by 2⁻ᵉ so the largest lies in [1, 2).
  2. If the second component is below 2⁻⁶⁰, the result is the largest, because the exact norm lies below the midpoint above it.
  3. Otherwise the kept squares are split exactly with `mul_add`. A third component below 2⁻¹²⁰ counts only as a sticky bit: its square is below 2⁻²⁴⁰, which is under the 2⁻²²⁴ granularity of S − m², so it can only break an exact tie, upward.
  4. A double-double square root gives the candidate. The candidate then moves one ulp at a time on the destination's real grid, including subnormal results and the overflow threshold 2¹⁰²⁴ − 2⁹⁷⁰. It stops when the exact sign of S − m² at both neighbouring midpoints m says it is nearest. That sign comes from Shewchuk's grow-expansion with zero elimination.
- **Special values:** these follow C Annex F's `hypot`.
  - An infinite argument gives +∞, even beside a NaN.
  - Otherwise, a NaN gives NaN.
  - ±0 gives +0.
  - `norm2(x, ±0)` = |x|.
- **Decided: the correctly rounded 3-norm, not a chain.**
  - The rows publish the magnitude of a vector. The 3-norm is its nearest double, with one rounding of at most ½ ulp, and it does not depend on the component order.
  - On 200,000 random comparable-magnitude triples, the correctly rounded chain RN(hypot(RN(hypot(a, b)), c)) differs from the 3-norm in 33,232 (16.6%, all by 1 ulp). The chain itself changes with the component order in 52,476 (26.2%).
  - For scale, macOS arm64 libm `hypot` is not correctly rounded on 16.7% of random pairs (50,046 of 300,000). Its chain differs from the 3-norm on 27.6%.
  - The cost of the 3-norm and the chain is the same.
- **Sharing: one module.**
  - PP and frame_kernel use `open_pipe_stress_frame_kernel::correct_norm`.
  - stress_recovery has no direct frame_kernel dependency, so it includes the same file by `#[path]`. There are no Cargo.toml or Cargo.lock changes, and none of the 14 reviewed inputs moves.
- **The readers do not need the module.**
  - RS, PY and TS recompute norms only inside a 64ε relative guard (`guarded`, `_consistent_norm`, `consistentNorm`). The norm differs from libm, CPython or the JS engine by at most 1 ulp.
  - A bitwise PY mirror would be the oracle's `ref_norm`, using exact integers. It is not proposed.
- **Tests on the branch:**
  - Annex F cases.
  - Exact, permutation and overflow cases.
  - Exact 2-D midpoints k(2n + 1, 2n(n + 1), 2n² + 2n + 1). Ties go down when h ≡ 1 mod 4 and up when h ≡ 3 mod 4. Each is broken upward by a kept third component and by a sticky one.
  - `correct_norm_vectors`: 1,200 committed vectors (900 adversarial, 300 random). Their expected bits come from the exact oracle, not from the implementation.

## 3. The oracle

The oracle is `_run_records/tools/norm_oracle.py`.
- Every binary64 is n/2ᵈ, so S = N/4ᴰ with integer N.
- RN(√S) is decided with `math.isqrt` on N, scaled to one bit beyond the destination's quantum. The subnormal quantum is 2⁻¹⁰⁷⁴, and overflow occurs at 2¹⁰²⁴ − 2⁹⁷⁰.
- The reference was checked against independent `fractions.Fraction` midpoint comparisons on 23,825 cases (`selftest`).

**Inputs (seed 109):**
- **10,000,000 random triples** in ten classes:
  - arbitrary bit patterns;
  - comparable magnitudes over the whole exponent range;
  - near-equal exponents;
  - the sticky boundary;
  - subnormal results;
  - the overflow range;
  - the 2⁻⁶⁰ boundary with signed zeros;
  - small integers and mixed scales.
- **1,000,000 adversarial triples:**
  - exact 2-D midpoints in both tie directions, with 1-ulp perturbations and sticky third components;
  - near-midpoints built from b² ≈ a·ulp(a) + ulp²/4 (2-D and 3-D) and from random 54-bit midpoints;
  - binade boundaries;
  - the subnormal grid;
  - the overflow threshold;
  - special values.

  In a 20,000-triple sample of the adversarial set, 1,054 are exact midpoints and 9,259 lie within 2⁻⁴⁰ ulp of one.

**Result:** 0 misrounded among 11,000,000 norm3 and 11,000,000 norm2 results. Of the triples, 9,611,343 took the main path, 1,344,663 the largest-only path and 43,994 were special.

After a refactor, the module was re-dumped in debug and in release. Both are bit-identical to the verified output (`_run_records/oracle/`).

## 4. The inventory

The inventory is `_run_records/inventory/inventory.tsv`: 431 rows. Each row gives:
- path and line;
- the function and the number of calls;
- the context;
- what it computes and what it reaches;
- whether a reader recomputes it;
- its platform class;
- the action.

It comes from `libm_scan.py`, a lexer that drops comments and strings, run over NUM `af53e1447c`. The scope is:
- PP;
- `P/core/solver/*` and `P/core/loads/*`;
- `result_export` (the RS reader);
- the PY reader (`P/core/analysis_runs`);
- the TS reader (`P/apps/desktop/src/features/results`).

| | calls | not correctly rounded |
|---|---:|---|
| Product code (PP, solvers, loads) | 123 | 87 libm: hypot 32, sin 23, cos 25, atan2 2, asin 1, exp 3, exp_m1 1 |
| Readers (RS, PY, TS) | 54 | hypot 17, all inside the 64ε guard (RS 11 libm, PY 3 CPython's own algorithm, TS 3 `Math.hypot`, engine-dependent); PY `** 2` 1 (libm `pow`) |
| Tests | 401 | 86 libm: hypot 23, sin 25, cos 21, log2 13, log10 1, atan2 1, exp_m1 1, sin_cos 1 |
| **All** | **578** | |

- **Product `hypot`: 30 of the 32 calls are replaced, on 19 lines:**
  - PP's ordinary route: support and support-action force and moment magnitudes, combined magnitudes, the formation guard's end q, the intensified i·|M|/Z, and the preview-physics combination magnitudes;
  - the tangent-discontinuity |cross|;
  - the load-reference length (the published `reference_length_m`);
  - the pressure-region chord and residual (guard and text);
  - the retained adapter guard;
  - the retained certificate's support projection, still charged as two scalar operations;
  - stress_recovery's bending amplitude;
  - the rigid-body screen.
- **Product sin/cos (48), atan2 (2), asin (1), exp (3) and exp_m1 (1)** reach published bytes or admission decisions and are not replaced (§7).
- **Not platform-dependent:**
  - `powi` on variables: 29 product calls. These are one fixed multiplication sequence on every target, because LLVM's expansion and `__powidf2` square the same way.
  - `powi` of 2: 6 product calls and 4 in the RS reader. These are exact.
  - `to_degrees`: a single multiplication.
  - `2 ** k` and `2.0 ** k` in the readers: exact.
- **Readers recompute** the support, combination and intensified magnitudes (RS, PY and TS) only inside the guard. The fit strain is recomputed exactly from the published `reference_length_m`; the length itself is not recomputed.

## 5. The measurement on the Mac (nothing re-pinned)

### 5.1 The 40 manifests

`_run_records/suites/` holds this run. It used CI's numerical cargo profile, as in ROOT's `run_suites_nff.sh`, but through `t3_cargo.sh` (`suites40.sh`). Both sides were archived from Git with `P/execution` excluded, and each had a fresh target.

| | ok | ignored | FAILED |
|---|---:|---:|---:|
| Base, NUM `af53e1447c` | 2,775 | 80 | 3 (`t13` and the runner's two `load_reference` tests: the known Mac failures) |
| Candidate, `d538f469af` | 2,780 | 81 | 5 (the moved tests below) |

**Changed outcomes: 8.**
- **3 fixed** (FAILED to ok):
  - `s11g_tests::t13_committed_fallback_uz_is_byte_identical`;
  - `load_reference_route_tests::load_reference_one_actual_solve_mints_bound_evidence_and_canonical_document_both_modes`;
  - `load_reference_cli::cli_load_reference_one_both_modes_is_controlled_and_equals_the_library_route`.
- **5 moved** (ok to FAILED): listed in §5.2.

**Added: 11.**
- The norm's 3 unit tests in frame_kernel, and again in stress_recovery, where they come with the included file.
- `correct_norm_vectors` (ok) and `correct_norm_oracle_dump` (ignored).
- 3 frame_kernel doc tests renamed by a one-line shift. The same 3 count as the **3 removed**.

Every other manifest is identical.

### 5.2 The moved bytes

Every move is **one value, 1 ulp**. Re-pinning means replacing the value and the hashes over it.

| Test (PP) | Committed artifact or pin | Value moved | Hashes |
|---|---|---|---|
| `retained_facade_tests::b1_sp_w_c2_direct_entry_publishes_the_pinned_successor` | `W_C2_PINNED` dense: document, receipt and published bytes | case C `rigid:N0` support force magnitude, `1.6258317075882521e-12` → **`1.6258317075882523e-12`** | document `f2800bd4…` → `c11f7566…`; receipt `612e23ca…` → `ca6a62a6…`; bytes `a77c010b…` → `604e4a33…` |
| `retained_facade_tests::b1_sp_w_c2_fixtures_are_the_live_successors` | `P/fixtures/results/retained_precision_w_c2_successor_dense_scrutiny.json` | the same value (`/source/results[377]`) | in the file: `publication_sha256` `57624d75…` → `35fa7aca…`, `receipt_sha256` as above; file sha256 `f2800bd4…` → `c11f7566…` |
| `retained_facade_tests::b1_sp_sf2_selected_not_first_and_two_selected_pins` | `CBA_PINNED` dense: receipt and bytes | the same value (`results[35]`) | `7aeecbac…`/`c719bd8d…` → `255785d2…`/`a320a5d3…`. (A, A2) in both modes and (C, B, A) sparse are unchanged; the scratch run reported, rather than asserted, so (A, A2) was reached. |
| `retained_wire_tests::u1_ordinary_bytes_unchanged_under_capture` | `ORDINARY_SHA256` dense: the rf_skew milestone's ordinary bytes (asserted on aarch64 macOS only) | the milestone's `rigid:N0` support force magnitude, the same 1-ulp step | length 69,366 unchanged; sha256 `21ca629c…` → `aa8b93ba…` |
| `preview_physics_runtime::m08_marker_intensified_measure_matches_references_and_never_combines` | no committed pin: the test's own expectation `i * (My.hypot(Mz) / Z)` (libm), asserted equal | case L2, pipe b–c end i: `18516192.493245974` → `18516192.493245978` (1 distinct row, met in 3 of 56 checks) | none. The fix is the test's formula, with `norm2` in place of `hypot`. |

- **Reader corpus** (`P/fixtures/results/retained_precision_cases.json`): two cases move, each by the same value plus its `publication_sha256` and `receipt_sha256`.
  - `w_c2_dense_scrutiny`, whose source is a D-U6-5 copy of the W-C2 dense fixture.
  - `sf2_c_b_a_dense_scrutiny`.

  Their dependants: 1 mutation is based on `w_c2_dense_scrutiny` (`f1_p4_parity_on_w2_published_case_a_dense`, `rehash: all`), 0 on `sf2_c_b_a_dense_scrutiny`, and no must-pass entry references either.

  The other producer-solved cases do not move: U8 L0, `cause_milestone_reversed`, SF-2 (A, A2), and the sparse W-C2 and (C, B, A). Their pinning tests pass on the candidate, and the scratch dumps also show the SF-2 and sparse W-C2 documents unchanged. The synthetic cases are templates.
- **Envelope regeneration** (`_run_records/moved/regen_envelopes_base_vs_cand.json`): every committed request and model fixture (P/fixtures/product_preview and result_export's) was run on both sides, 33 inputs in both modes.
  - 62 of 66 envelopes are byte-identical.
  - 4 differ, in 5 values, all `support_reaction_*_magnitude_v2` rows, all 1 ulp:
    - `load_reference/connected`: sparse 2 values, dense 1;
    - `rf_skew…` dense: 1 value (the u1 row above);
    - `load_reference_fallback_uz` sparse: 1 value.
  - Of the 30 committed raw fixtures beside those requests, **the candidate reproduces all 30**. The base misses 3 of them: `connected` sparse and dense, and `fallback_uz` sparse. Those are `t13`'s and the runner's fixtures: Linux pins that macOS libm missed by 1 ulp.
- **Static audit of committed documents** (`_run_records/moved/committed_magnitudes_audit.json`): 616 magnitudes in 73 documents across 379 JSON files. Of these, 28 are not the correctly rounded 3-norm:
  - **3 are the moved values above:** the W-C2 dense fixture and the corpus copies of W-C2 and SF-2 (C, B, A) dense.
  - **17 are in the corpus's synthetic DRAFT cases 0–14.** These are hand-built templates, not producer pins; their values equal the correctly rounded chain.
  - **4 are in the `fields` raw fixtures of physics_source and load_reference_source.** The candidate reproduces them byte for byte, so they come from the selected-source route's registered norm recipes (`source_receipt`'s fixed IEEE arithmetic: deterministic, not libm), which I109 did not change.
  - **4 are in reader-contract input snapshots that no test compares with live output:** `preview_physics_connected_{dense,sparse}.json` and `physics_connected_{ui_,}mechanics_sparse.json`.

  None of the 28 needs to move for the tests to pass.

## 6. Linux: the CI dispatch request, and the B1 platform pins

**Request:** please run a hosted-CI diagnostic dispatch (not for merge) of `codex/piping-t3-platform-norm-20261008` at **`cd8e710039`** (full SHA `cd8e7100399eb8e6dd666dede3083a4d2c93f20c`), with at least the numerical cargo suite. Nothing is re-pinned, so the five tests of §5.2 fail by design. Read on glibc:

1. **`t13` and the runner's two `load_reference` tests: expected to pass.** They now pass on the Mac against the same committed bytes.
2. **The W-C2 tests:** the failure output prints `B1_SP_WC2_PIN dense_scrutiny c11f7566f1f0c469bc0a2808466dd9dd137ea64abed327fb9e4d35ff92ded22f ca6a62a6187a08d7b2e2643911fd232b02076b9032be1455754ff780540995f2 604e4a3380b28d3757d7a7f20aa5d72eae8a93bdc9e24dc966afe6b48fafca3f` on the Mac. The same line on Linux means the same bytes. Sparse passes on the Mac.
3. **SF-2:** the Mac prints `B1_SP_SF2_PIN c_b_a dense_scrutiny 255785d20cf0aa9f497ea324d744eb3e946871d5aac863ed8d0081d0521e8c92 a320a5d33707c1fc8c12a35de624720dddbc35084979522c96ab1906e17c708f`.
4. **m08:** passes on Linux only if glibc's `hypot` is correctly rounded on its inputs. It is a test-side libm expectation either way.
5. **Unchanged by this branch:** the two W2b input pins still fail on glibc, because their ring is `10·cos t, 10·sin t`. `u1`'s hash is asserted only on aarch64 macOS.

**The B1 platform pins (I107's fix; not on NUM `af53e1447c`).** I read them read-only with `git show` from `codex/piping-t3-pr-b1-20261008` at `f4a0430412`. I did not touch that worktree.
- **The glibc W-C2 and (C, B, A) variants: expected to become unnecessary.**
  - Apply I107's `W_C2_DENSE_GLIBC` (the value and the two hashes) to the committed W-C2 dense fixture. The result is **byte-identical to the Mac candidate's document**, sha256 `c11f7566…` (`_run_records/moved/glibc_variant_equals_candidate.txt`).
  - `CBA_DENSE_GLIBC` equals the Mac candidate's (C, B, A) dense pair.
  - The exact oracle on the fixture's own components gives `1.6258317075882523e-12`: glibc was correctly rounded there, and macOS was 1 ulp off.

  The candidate computes with IEEE operations only, so it gives these bytes on glibc too; item 2 of the dispatch confirms this. Re-pinning to the candidate's bytes then leaves one pin for both platforms, and the `cfg(target_env = "gnu")` variants can go.
- **The ring (I107's `CAP_MAXIMAL_RING`) stays.** It is a sin/cos test input. Spelling it as binary64 bits is platform-independent in itself.
- **`u1`'s aarch64-macOS-only ordinary pin** could become unconditional once a Linux run shows the same milestone bytes. This dispatch cannot show that, because the assert is skipped on Linux.

## 7. The other functions on published paths (recommendations; none implemented)

| Function | Product sites | Reaches | Recommendation | Size |
|---|---|---|---|---|
| `sin`, `cos` | 48: `curved_bend` (46: local stiffness, consistent uniform and radial-pressure loads, section resultants, end tangents, the trigonometric Gram matrices); `nonlinear_integration::structural_adapter` (2: the curved symmetry chord) | published bytes of every model with a curved bend, through the solve | **A correctly rounded `sin_cos` on the bend's bounded domain**, \|x\| ≤ 2π (φ ∈ (0, π), θ ∈ [0, φ], 2φ). No Payne–Hanek reduction is needed. The design: a 3-part Cody–Waite reduction by π/2, a double-double polynomial, a Ziv rounding test, and an exact or triple-double fallback. The oracle would be Python `decimal` series to 300 bits on 10⁷ cases plus the known hard cases. | ~400 lines plus the oracle; 1–1.5 days |
| `atan2` | 2: `curved_bend` φ = atan2(\|n\|, rᵢ·rⱼ); PP `preview_physics`'s tangent-discontinuity angle (a warning threshold and its printed text) | φ feeds everything above; a warning and its text | **A correctly rounded `atan2`**, built the same way, so the bend is deterministic end to end. The warning could test \|d×t\| against tan(10⁻⁶)·(d·t) without the angle, but its text prints the angle. | ~300 lines; 1 day (shares the oracle) |
| `asin` | 1: PP `lib.rs`'s implied included angle 2·asin(c/2R), checked against the user's angle and printed in a blocking diagnostic | an admission decision and its text | **Reformulate with the correctly rounded `atan2`:** 2·atan2(h, √((R − h)(R + h))), with h = c/2. | ~10 lines once `atan2` exists |
| `exp`, `exp_m1` | 4: PP `case_state/thermal.rs`'s logarithmic stretches exp(dᵢ) and exp(dₒ) (published), the path-stretch check, and the logarithmic thermal strain expm1(δ) (published; it drives thermal loads) | every logarithmic-law thermal case | **A correctly rounded `exp`/`expm1`.** The arguments are thermal-strain integrals with \|x\| ≪ 1, so a bounded-domain double-double kernel with a Ziv test and an exact fallback suffices, with a general Cody–Waite-by-ln 2 path for completeness. | ~300 lines plus oracle; 1 day |
| `powi` on variables | 29: PP areas, second moments, self-weight and the displacement magnitude; `straight_pipe`'s partial-load terms | published bytes | **Already deterministic.** Rust documents `powi`'s precision as unspecified, so spell out the products (`x * x`, `(x * x) * (x * x)`, `x * (x * x)`). The bits are the same and nothing moves. | ~20 lines |
| PY reader `** 2` | 1: `physics_source.py:117`, an outward-rounded bound | a reader decision | Use `v * v`, which is exactly RN(v²). CPython's `**` is libm `pow`. The outward rounding already covers a 1-ulp error, so this concerns bits, not soundness. | 1 line |
| Readers' `hypot` | 17 | reader checks inside the 64ε guard | **Cannot change an outcome.** No change. | none |

**Order:**
1. `sin_cos` and `atan2`: every bend model's bytes.
2. `exp`/`expm1`: logarithmic thermal cases.
3. `asin`: free once `atan2` exists.
4. The `powi` spelling and the PY `** 2`.

Each of 1–3 moves published bytes wherever a libm was not correctly rounded, so each needs a §5-style measurement. Test inputs built from platform trigonometry (the cap_maximal ring and 4 toleranced inputs) stay platform-dependent on their own.

## 8. Records

All paths are relative to this folder. The folder was written at the same R path inside `WT/t3-norm`, untracked, and `WT/numerics` was not touched. ROOT copies and commits it.
- `_run_records/oracle/`:
  - `oracle_report.json` and `oracle_chain.log`;
  - `recheck_debug_release.log`;
  - `chain_vs_norm.json`, `adv_closeness.json` and `platform_hypot_rate_mac.json`.
- `_run_records/inventory/`:
  - `inventory.tsv` and `inventory_summary.json`;
  - `libm_scan_af53e1447c.tsv`, the raw scan.
- `_run_records/suites/`:
  - both summaries, `manifests.txt` and both outcome lists;
  - `cmp_base_cand.{json,txt}`;
  - `cand_pp_failures.txt`.
- `_run_records/moved/`:
  - `regen_envelopes_base_vs_cand.json`;
  - `retained_docs_base_vs_cand.jsonl` and `retained_docs_sha256.txt`;
  - `retained_pins_{base,cand}.txt` and `m08_intensified_{base,cand}.txt`;
  - `committed_magnitudes_audit.json`;
  - `glibc_variant_equals_candidate.txt`.
- `_run_records/tools/`: every script used. `regen_patch.py` is a measurement-only patch applied to the scratch archives, never to the branch: an SF-2 dump that reports rather than asserts, an m08 report and an envelope example. `sums.py` wrote SHA256SUMS.
