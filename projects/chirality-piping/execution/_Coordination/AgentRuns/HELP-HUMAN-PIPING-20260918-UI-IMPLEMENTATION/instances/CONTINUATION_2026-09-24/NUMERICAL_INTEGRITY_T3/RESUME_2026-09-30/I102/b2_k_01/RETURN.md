# I102 (lane K): B3-K (J2k), then B2-K

TASK (Type 2), I102, lane K's implementer (I-K), for ROOT (HELP_HUMAN, Agent 0). Fresh instance; no delegation. 2026-10-08 UTC.

**Brief:** `R/BRIEFS/B2_K_LANE.md` (`5eab543d…`) with `R/BRIEFS/B1_COMMON.md` (`2d170307…`), both verified. Basis: KD `R/I94/b2_kd_01/DESIGN.md` (`4e8c33a4…`), `R/REVIEW_RV115/b2_kd_01/` (REVIEW, ADDENDUM_01–04), I96's `R/I96/b3_d_01/DESIGN.md` §8 (`ad7942f6…`), I97's B2-C (CONTRACT `165cd4b1…`, REVISION_01 `6f6a583f…`, REVISION_02 `79007dcd…`), and the RR sections the brief names.

**Where:** `WT/b2-k`, `codex/piping-t3-b2-k-20261008` from main `601ba408e4`. Every change is inside FK and S-13's file list; PP and every FK dependent were compiled and tested, never edited.

## Heads

| Part | Commit | Content |
|---|---|---|
| 1: B3-K (J2k) | `806424c6de` | K3-1, K3-2 (option (a)), K3-3 |
| 2: B2-K | `f7494326f1`, then **`ef51a2d295`** (tests only: three mutant-killing tests and the C01 cross-build witness, with a `cfg(test)` accessor) | KD as amended (SF-1–SF-4; R-1–R-11; N-3, N-6–N-9; SA-1; A-1; SA4-1 (a)–(e); B-2 (b)) |

## Part 1: what changed

- **K3-1:** `ProductMaterial::BaseENu { e, nu }` → `MaterialOperands::ExactENu` (appended variant; `ProductMaterial` stays 96 bytes, `ProductMemberFacts` 160; asserted).
- **K3-2:** `build_member` computes represented Z (hull(I_K/c, Ẑ)) and the Iy = Iz axis-bit check for every material. A `cfg(test)`-only thread-local hook restores the old material gate (SA-2's discriminator); outside tests it is a constant `false`.
- **The declared oracle exception, exactly:** generator line 68 drops `if mode else (F(),F())`; fixture lines 22 and 122 become `("+ep2", "+fp2")` and `("+8p-1", "+8p0")`. Fixture `467f8811…745f72c`, generator `d9618a32…e03eda` (both as ruled). No other oracle byte changed.
- **K3-3** (5 tests, `b3k_*`): AxisBits for ExactENu with Iy ≠ Iz, keeping its exact work prefix; the restored gate fails BaseENu stress and maximum rows with `bad("represented Z")` (proof and per-row recipe), both certify with K3-2, and the ordinary route is unaffected; MaterialBits and InvalidMaterial through the public variant (member level and through the whole prepared proof); NA-6's own ν = 0.3125 control: E/2.625 = 80e9 exactly, so the exact route certifies **bit for bit** as the ordinary route with G = 80e9 (values and verdicts); ν = 0.3: the source lane strictly encloses the exact G, excludes Ĝ, and Ĝ·J enters as a nonzero coefficient difference; the six non-ExactENu vectors pass unchanged (the existing oracle test).

## Part 2: what changed (FKR unless noted)

- **API (additive):** `adaptive.rs` `PreparedCaseSource` (I1); `combine.rs` `CombinationOperand`, `RetainedCombination::solve_sources(_recorded)`, `CombinationReason::NoSelectedOperand` (appended unit variant); `origins.rs` `OriginCapacity::for_invocation`, `RecordedInvocation::register_prepared_source`, `RecordedOperand`, `solve_combination_sources`; `FK/src/structural.rs` re-exports. `solve`, `solve_recorded` and `solve_combination` are wrappers over the same cores; `for_calls(a, b)` is `for_invocation(a, b, 0)` (N-6: identical fields and CountRange names).
- **Order (KD §1.4):** capacity → Call → NoOperands → NestedCombination → OperandsDiffer → **NoSelectedOperand** → custody (R-1: `MissingSelectedOrigin` for a prepared operand whose id is out of range, whose source is not a case's, has a combination ledger, or is not its full K4SRC bytes; R-11: a kernel-selected source is accepted) → combined preparation → Run on the **first selected operand's group**, merged caches and imports from selected operands only (authored index kept).
- **SF-1:** a batch needs `runs.len() + n + (combinations − used) ≤ runs`, else `Capacity` with nothing recorded; dormant under `for_calls`. Sources are reserved at cases + combinations (= runs under `for_calls`).
- **Owner (I9):** `product_owner(run, solve) -> Option<NativeOwner>` replaces `product_case_owner`; both certificate entries accept a recorded combination owner; the kind must agree with the prep's factors.
- **View (§3.2):** the blanket refusal is gone; a combination owner's prescribed terms must carry its factors' bits in order and the right count (else `PairIdentity`) and be exactly +0.0 by bits (N-3; else `UnsupportedCombination`); each DOF's and term's visit is booked before its check (N-8); flags stay all false.
- **Residual (§3.3, `source_residual.rs`):** for a combination owner the free rows add, and the reaction offsets subtract, the owner's K4LED net enclosed outward at 1024 bits (`product_certificate.rs` `ledger_net`: two `Add` entries, fresh context and sum, work collected on every exit). Case branches unchanged.
- **Certificate (`final_case.rs`):** `row_scales`' combination coverage (no maximum, mode, parity or modulus rows; slots 0–19; no mode record); `project` forms each combination displacement magnitude as RN64, ties to even, of the exact 3-norm of the node's frozen mm components (A-1; DEF-C r2), by `rn64_norm3`: exact S, a 1024-bit nearest sqrt rounded once, then exact sides at y₀'s **actual neighbours' midpoints** (SA4-1 (a)); MAX's upper midpoint MAX + 2^970 refuses at or above (b); an overflowing estimate is decided from MAX by the same comparison (c, B-2 (b)); a second step or a zero/underflowing estimate with S > 0 is an invariant failure (d, e). Visits and one scalar operation counted as `support_hypot` does; context and sum work merged.
- **NA4-5:** the ordinary route keeps nested `hypot` for a combination's displacement magnitude, and the retained route now forms (ii). The same components can give values about 2 ulps apart on the two routes; G7 holds on both.

## Part 2: tests (KD §7 as amended), by name

| Id | Test (FKT `retained_k4/`) |
|---|---|
| C01 | `combine_tests::b2k_c01_the_old_api_is_the_source_api_and_a_mixed_combination_has_the_all_selected_bits`; `origins_tests::b2k_c01_c04_mixed_operands_match_all_selected_bits_charge_nothing_and_change_no_operand`; `combine_tests::b2k_c01_existing_combinations_print_their_bytes` (cross-build witness against J2k) |
| C02 | `combine_tests::b2k_c02_operands_differ_on_a_prepared_or_a_selected_operand` |
| C03 | `product_final_case_tests::b2k_k08_…` (combined ledger = oracle K4LED bytes for C1–C9) and `b2k_k10_…` (C3: operand-row sum exactly 0, excluded by both lanes) |
| C04 | `origins_tests::b2k_c01_c04_…` |
| C05 | `product_final_case_tests::b2k_c05_the_combination_coverage_rule` |
| C06 | `product_final_case_tests::b2k_c06_a_nonzero_prescription_in_a_later_operand_is_unsupported` |
| W05, W06 | `origins_tests::b2k_w05_w06_custody_of_terminal_work_and_imports_from_selected_operands_only` |
| K-01 | `combine_tests::b2k_k01_a_prepared_case_source_is_exactly_the_solve_paths_prep` |
| K-02 (SF-1, N-6) | `origins_tests::b2k_k02_for_invocation_registration_and_the_run_capacity_check` |
| K-03 (R-11) | `origins_tests::b2k_k03_an_unavailable_operand_is_rebuilt_identity_checked_and_custody_refuses_otherwise`; `b2k_k03_each_i7_check_refuses_on_its_own` |
| K-04 | `origins_tests::b2k_k04_no_selected_operand_is_refused_after_the_native_checks`; `combine_tests::b2k_k04_unrecorded_all_prepared_is_no_selected_operand_after_the_native_checks` |
| K-05 | `origins_tests::b2k_k05_a_prepared_first_operand_keeps_authored_order_and_takes_the_group_of_operand_one` |
| K-06 | `origins_tests::b2k_k06_product_owner_is_the_recorded_kind_of_the_run`; `product_final_case_tests::b2k_k06_both_certificate_entries_accept_a_recorded_combination_owner_only` |
| K-07 (N-3, N-8) | `product_final_case_tests::b2k_k07_view_admits_p2_refuses_corruption_and_keeps_native_data_flags` |
| K-08 (SF-4) | `product_final_case_tests::b2k_k08_residual_and_recovery_contain_the_oracle_and_nets_are_exact_outward` |
| K-09 (N-7, A-1) | `product_final_case_tests::b2k_k09_full_prepared_proof_certifies_combinations_and_prints_the_diagnose_rows`; `b2k_rn64_norm3_vectors_signed_zeros_refusal_and_work`; `b2k_rn64_norm3_agrees_with_the_oracle_vectors` |
| K-10 (SF-2) | `product_final_case_tests::b2k_k10_mutation_controls_fail_containment` |
| K-11 (R-5) | `source_residual_tests::source_residual_combination_and_missing_uniqueness_are_explicit_refusals` (the declared re-pin) |
| K-12 | `product_final_case_tests::b2k_k12_the_i42_bridge_holds_for_a_p2_combination_owner` |
| K-13 | the existing tests unchanged, and their printed output identical to J2k (below) |
| K-14 | PP `profile_in_build_record` and the retained-memory law tests in the registered build |

**The specimen** (KD §6 plus RV115): one cantilever, D = 0.1, t = 0.005, E = 210e9, G = 80e9, K section = the correctly rounded annulus (the oracle's bits equal FK's `prepare_product_annulus`); operands A, B, A2, P, Q, H, and R/R2 (SF-2: root Fy = 5 and a cross-operand cancelling Fz pair at the restrained root, which the representative A lacks); C1–C6 as KD, C7 = A + R + R2 (SF-2), C8 = 0.1·B + A2 (SF-3: 0.1·3 needs 54 bits), C9 = 2^600·A + 2^-600·A2 (N-9). C4 has a prepared first operand.

## What passed (logs in `_run_records/`; main = `601ba408e4`, archived to scratch without `execution/`)

**FK suite** (`cargo test --locked --offline`, debug, as CI runs it):

| Tree | lib | integration tests | doc |
|---|---|---|---|
| main | 480 passed, 1 ignored | 3/13/20/15/1/5/3 passed | 6 |
| Part 1 `806424c6de` | 485 (+5 `b3k_*`), 1 ignored | identical | 6 |
| Part 2 `ef51a2d295` | 508 (+5 `b3k_*`, +23 `b2k_*`), 1 ignored | identical (S11 site table included) | 6 |

The test lists differ from main only by the 28 added tests; no test was removed and no existing outcome changed. K-11's test keeps its name and passes with its declared re-pin.

**PP suite** (`--no-fail-fast`): main, Part 1 and Part 2 are identical, test for test: lib 545 passed, **1 failed** (`s11g_tests::t13_committed_fallback_uz_is_byte_identical`, the known Mac failure, on main too), 10 ignored; all 23 integration binaries pass.

**K-14 / NA-5:** PP `profile_in_build_record` runs **in the registered identity build** (rustc 1.97.1, aarch64-apple-darwin, debug, no rustflags: no `I65_G6_RECORD_SKIP`) and passes at both heads; at Part 2 all 42 retained-memory law tests pass, and all 244 printed atom values equal Part 1's (layout neutral; S-4).

**FK dependents:** all 22 (the full closure: 15 core crates, 6 validation benchmarks, the desktop `src-tauri`) compile with all targets at both heads, plus `numerical_robustness --features seeded-faults` and FK `--features mutation-controls`: 0 failures. **Their own test suites** (R-3/R-4's "compile and test") at main and at Part 2: identical crate by crate. 20 crates pass on both; `core/runner/headless` fails the same two pinned-output tests on both (`load_reference_one_actual_solve_mints_bound_evidence_and_canonical_document_both_modes`, `cli_load_reference_one_both_modes_is_controlled_and_equals_the_library_route`; same tests and outcomes). At Part 2, `self_weight_wasm` and `operation_applier` first failed to compile their tests with a serde_json 1.0.149/1.0.151 type clash: my shared target directory across crates whose lockfiles pin 1.0.149, 1.0.150 and 1.0.151 (they had compiled cleanly with all targets in that directory minutes before). In a fresh target directory they pass with main's counts (14 and 194). A host artifact, not a code difference.

**K-13 (case-path byte identity, re-based on J2k per SA-1):** the existing tests of `source_bridge`, `source_residual`, `product_final_case`, `product_certificate`, `combine`, `origins`, `kf1_tracker`, `method` and `publication` were run single-threaded with `--nocapture` on Part 1 and Part 2. All **127** common tests pass on both, and their printed output (938 lines, including the I42, I44 and I51 work-count and layout prints) is **identical**; only the 23 new tests are extra. **C01 across builds:** `b2k_c01_existing_combinations_print_their_bytes` (old API only) prints, for every model combination, the legacy outcome, the recorded combination, calls, sources, groups, builds, runs (Debug length and fixed-key hash) and the meter; its J2k and Part 2 outputs are identical (8 of 8 lines).

**The oracle** (`product_certificate_vectors.py`, standard library only, no production import): default mode verifies both fixtures. The existing fixture stays `467f8811…` (J2k's, S-11 as SA-1 re-bases it); the new `product_certificate_combination_vectors.rs` is `1999a326…`; the generator is now `0721e645…`. It carries C1–C9's exact K-law and G-law truths for all 52 native and 20 stress rows (N-7), each combination's K4LED bytes and nonzero nets as [RD1024, RU1024] and RN1024, the representative-only tip responses (KD §6 item 4 (ii)), and 400+ RN64 3-norm vectors from its own integer square root (the SA4-1 vectors, constructed exact midpoints and their ±1-ulp neighbours, random patterns).

**K-09's diagnose** (`--diagnose`, on the kernel's printed rows): **648 of 648 verdicts agree** for C1–C9, independently recomputing the truth containment in both lanes, S* from the published rows (N-7), every class, absolute bound, the five-operation A_f64, A_exact and both decimal tests, each K4LED and its sha256, and every (ii) magnitude. The oracle's 3-norm agrees with I97's 411 sealed vectors (read only). **Certification:** C2, C3, C6, C7, C9 certify every row; C1, C4, C5 lose two and C8 one stress row (relative MPa bending rows failing `SharperExact`). The test's net-case control shows these are DEF-O's: a case whose loads are the exact split products has the same K4LED and publication, and its proof decides **every shared row identically**, failures included.

**Kernel 3-norm:** `rn64_norm3` agrees with the oracle on all fixture vectors, including the three SA4-1 vectors at MIN_POSITIVE (RV115's counterexample, RV118's witness, and a near-threshold triple with its one-ulp control below).

## Mutants (`_run_records/MUTANTS.md`; one per new check, each on a scratch copy of the committed FK)

- **Part 1:** 4 run, **4 killed** by assertions (K3-1's mapping; the material gate restored, also killed by the existing oracle test with the declared lines; the axis bits; the hull).
- **Part 2:** 35 run against `f7494326f1`; 27 killed. Three survivors were killable and are now killed at `ef51a2d295` by the follow-up tests (the recorded cache-merge order; I7's case-owner and no-ledger conditions, each redundant with the other and with the K4SRC check in any real store, now shown live by tampering one recorded fact). **30 killed, 5 survive, each equivalent or unreachable:**
  - p2m29, p2m30 (the tie clauses of the exact side test): at an exact tie S = m² with m ≤ 55 bits, the 1024-bit square root is exactly m and `to_binary64` already ties to even, so y₀ is never odd at a tie. Kept as defence.
  - p2m32 (SA4-1 (d), a second step): one step always suffices from a 1024-bit estimate.
  - p2m33 (SA4-1 (c), an overflowing estimate): reaching it needs S within about 2^-1022 relative below (MAX + 2^970)²; three binary64 squares are spaced far more coarsely there, so no input reaches it.
  - p2m34 (SA4-1 (e), a zero estimate with S > 0): unreachable, since S > 0 makes √S ≥ 2^-1074.

## Open, and for ROOT

1. **K-09 as KD hoped (C1–C5 certify every row) does not hold for KD's specimen:** C1, C4 and C5 each lose two MPa bending rows (C8 one) to DEF-O's projection rounding (raw MPa then ×10^6 against a one-rounding allowance; the stress analogue of RV115's NC-1, routed to SQ). Not a B2-K defect: the net-case control fails exactly the same rows, and the diagnose agrees on every verdict. Part 1 met the same limit on its own specimen (most load sets lose one to ten rows on the ordinary and exact routes alike); its witness uses a load set that certifies.
2. **K-01's refusal half has no specimen:** a `PrimitiveSource` refuses non-finite loads, and the 4,352-bit ledger accumulator cannot overflow from binary64 terms in practice. `PreparedCaseSource::new` is `CasePrep::new`, the same call `solve_cases` maps.
3. **W05's terminal `Refused` is unreachable without a seeded fault** (a selected operand's factor already passed on the same stiffness). The test pins custody on a reachable terminal (`Budget(Case)` after nonzero work, through `solve_sources_recorded`) and the legacy projection's clearing directly.
4. **Placement:** K-12's bridge test and the specimen live in `product_final_case_tests.rs` (S-13 admits no new helper file); `source_bridge_tests.rs` is unchanged.
5. **B2-C:** no conflict found; the API names and order match CONTRACT §1–§2.5 and REVISION_02 §2.2 (with SA4-1).
6. **NA4-5:** the ordinary and retained routes now form a combination's displacement magnitude differently (nested `hypot` against (ii)), up to about 2 ulps apart; G7 holds on both.
7. **Stops:** none fired (S-1 to S-14, SF-1's invariant; S-11 and K-13 on J2k's oracle).

## Host and execution record

- Every cargo ran through `WT/tools/t3_cargo.sh --locked --offline`; targets under `WT/targets/i102-b2-k/`, scratch and `TMPDIR` under `WT/scratch/i102_b2_k/`. Main, Part 1 and Part 2 were archived (`git archive`, without `execution/`) into scratch trees so that later runs used the exact commits.
- **Slips, disclosed:** one FK `cargo check` (seconds) overlapped my PP suite run, and one evidence chain was started detached and watched through its log rather than as a tool-tracked background job. Host `python3` ran two text edits early on; every oracle, diagnose and mutant run used VENV.
- Both product commits pass `WT/tools/t3_host_screen.py` (15 files, 0 hits) and `validate_private_terms.py --from-host` with the private list (0 findings). No symlink and no folder named `build` in this record.
