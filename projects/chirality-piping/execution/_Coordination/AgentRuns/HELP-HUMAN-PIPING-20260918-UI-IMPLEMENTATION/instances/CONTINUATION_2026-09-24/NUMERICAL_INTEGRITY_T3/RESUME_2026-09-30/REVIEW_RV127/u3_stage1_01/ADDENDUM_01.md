# RV127 addendum 01: Stage 1's repairs confirmed; U3 Stage 2 reviewed

**Who:** RV127, TASK (Type 2), dispatched by WORKING_ITEMS for T3 (Agent 1), 2026-10-08 UTC. I wrote none of this code and did not delegate.

**The request:** WORKING_ITEMS' message of 2026-10-08:
- confirm I110's Stage 1 repairs;
- review Stage 2: bytes and H-1, the B1 re-pin, the consequential validation changes, G11, and nothing held by T4 touched.

I114's lane (G10/D-3, and this review's S-1 text) is out of scope.

**Basis:**
- RR "Owner decision: M07's flawed joint element, option A; U3 Stage 2 released". It also records ROOT's acceptance of this review's N-2. Per WORKING_ITEMS, N-1 and N-3 are moot.
- `R/BRIEFS/U3_PRESSURE_RETIRE_03.md` (`7c5f055a…`).
- `R/I110/pressure_retire_03/RETURN.md`; its SHA256SUMS verify.
- This review's `REVIEW.md` (`335df8b2…`).

| Head | Base | What |
|---|---|---|
| `6b6543dc1e` (pushed; equals `origin/codex/piping-t3-pressure-retire-20261008`) | Stage 1 head `4c0d5d7c00`; byte base B = main `7eae707bb7` | 4 commits: `769c109d82` (repairs), `cda85e06d5` (the scope), `9930cfe6db` (the legacy computation), `6b6543dc1e` (G11) |

**Placeholders:** as in REVIEW.md.
- `A` is my archive copies `WT/rv127/{base,cand2,h1mut}`:
  - `base` is B;
  - `cand2` is the head;
  - `h1mut` is the head with H-1's three `+ 0.0` removed.
  - `base` and `cand2` also carry probe-only tests.
- `E` = `_run_records/addendum_01/`.
- Line numbers are at the head unless marked B.

## Verdict: **PASS** at `6b6543dc1e`: 0 BLOCKING, 2 SHOULD-FIX, 7 NOTE. B-1 is closed.

- **The Stage 1 repairs are confirmed.**
  - **B-1:** `endpoint_section_cut_fixed_and_free_thermal_match_uniform_stations` (`PP/src/lib.rs`, `769c109d82`) is my probe verbatim, and it passes.
  - **N-4:** the gate is kept and pinned at unit level (`non_exact_source_blocks_gate_refuses_a_later_version_a_contract_or_regions`, which passes).
  - **N-5:** `pressureModeText` marks "retired" only for exactly `1.0.0/legacy_pressure_v1`. Other contracts show "unsupported". It names the count of legacy primitives a contract-free model still carries.
  - **N-6:** the retained entry and the CLI each have a zero-primitive refusal test, and both pass.
  - **N-7:** both texts name `2.0.0/exact_straight_pressure_v2`, pinned in the dispatch test.
  - **N-2:** accepted by ROOT.
  - **N-8:** remains open (the Linux CI dispatch).
- **Bytes are still identical, H-1 included.**
  - My harness (9 fields per row; REVIEW.md §1.3) at the head against B:
    - **98/98 sample rows are equal:** 16 exact documents, 25 implicit pressure-free documents and 8 of B1's corpus, each in both modes;
    - W1 is unchanged: 10 successors, 6 ordinary publications;
    - so are the 10 nonzero-pressure refusal rows.
  - My head hashes equal I110's round-3 head rows: 98/98 for ordinary and runner mechanics, 16/16 for W1.
  - The sample exercises signed zeros. Rows with `-0.0` in the ordinary envelope:
    - E: 32/32 rows, 4,861 tokens;
    - F: 24/50 rows, 5,655 tokens;
    - B1: 12/16 rows, 1,084 tokens.
  - Export documents carry 12,050, 13,386 and 252 `-0.0` tokens respectively.
  - H-1 holds by construction. See A1-N-5 for why the bytes alone do not show it.
- **The B1 re-pin is exactly the two atoms and nothing else.**
  - I ran `profile_in_build_record` at B and at the head, both in the registered build, so the record was asserted rather than skipped. Of 247 profile atoms, exactly two change:
    - `s((&str,StressRecoveryResult))`: 192 → 160;
    - `s((String,DerivedSection))`: 88 → 80.
  - Every phase in both modes falls by exactly 800 B. The whole drop is in the requested part; the moving part is unchanged.
  - `PINNED_RECORD` is the old record minus 800 in all 14 places. `W1_PHASE_BYTES` equals the record's W1, and `MAX_PHASE_BYTES` equals its maximum (W3).
  - `challenge_bounds_are_the_profile` passes at both.
  - No product file outside execution records cites the old figures.
- **The validation removals are the legacy computation's oracles only.** Two of them leave stale references (A1-S-2), and one copy of the legacy straight-pipe thrust survives elsewhere (A1-S-1).
- **G11 is confirmed.** Before the fix, the demo with C-150's lateral value removed solved with 628 rows, 3 of them review rows saying "consumed". At the head it is refused with `JOINT_ELEMENT_STIFFNESS_INCOMPLETE`. No committed document has an incomplete flexibility joint: I scanned 267 documents and found 4 flexibility joints, all complete.
- **Nothing T4 holds is touched.**
  - FK and NI source are unchanged. FK's only change is two site-table rows for the deleted CB functions.
  - `fixtures/`, `previewService.ts`, `core/product_preview` and I114's line `pressure_runtime.rs:226-228` are unchanged.
  - No added test reproduces the old element's numbers.

## Findings

| ID | Class | Where | Evidence | Remedy |
|---|---|---|---|---|
| A1-S-1 | SHOULD-FIX, **for ROOT** (scope: a second copy of the legacy straight-pipe thrust) | `P/core/loads/primitive_loads/src/lib.rs:2347-2376` (the `Pressure` arm of `prepare_straight_pipe_axial_effects`: axial force `= p · A_internal`). It is used by `P/validation/benchmarks/mechanics/src/lib.rs:4697-4762` (`MECH-TP-PHYS-008-THERMAL-PRESSURE-AXIAL-EFFECTS`, `pressure_thrust_force`) and `:4792-4928` (`MECH-TP-PHYS-009`), and those are bound into the shipped CLI's `run-benchmark` mechanics suite (`P/core/runner/headless/src/benchmark_binding.rs:812-875`). Documents: `P/validation/hand_calcs/mechanics/tp_phys_008_thermal_pressure_axial_effects.md:50-61`, `tp_phys_009_combined_load_axial_effects.md:53`, and the manual pages `mech-tp-phys-008-…` and `mech-tp-phys-009-…` | This is the legacy closed-end thrust: a pressure primitive becomes an axial load p·A_internal, the same model as PP's deleted `PressureThrustSource::PipeInternalArea` thrust. PP never calls this helper; only the two benchmarks do. The CLI therefore still runs it and reports a pressure-thrust value of 9.0 N as a matched benchmark value. It is the same class as this review's N-1, which WORKING_ITEMS called moot because "Stage 2 removes the benchmark". Stage 2 removed only `STRESS-PRESSURE-MEMBRANE-ORIGINAL` and `MECH-CURVED-BEND-PRESSURE-THRUST-ARC`. I110's inventory lists `primitive_loads` only at `:181`, "keep: the category must parse" | ROOT rules on one of two options: (a) remove the `Pressure` arm and the pressure halves of `MECH-TP-PHYS-008`/`009`, keeping their thermal halves, re-pinning their totals and suite counts, and updating the hand calculations and pages; or (b) keep them, and record that a CLI benchmark path still computes the legacy straight thrust. No exact or pressure-free model byte depends on either |
| A1-S-2 | SHOULD-FIX (stale references the removals leave) | (a) `P/docs/validation_manual/cases/stress/stress-range-mechanics-original.md:44`, `:51` and its generator `generate_validation_case_pages.py:600`; (b) `P/core/loads/stress_recovery/README.md:14`, `:55`; (c) `P/docs/validation_manual/headless_runner_reproduction.md:128`, `:143` with `P/validation/witness/generated/del1005_payload_binding_benchmark_multi_case.json` (`/suite_run/cases/2/values/4`, `/5`) | (a) The manual page cites `stress_range_blocks_asymmetric_optional_pressure_components` as evidence, and `9930cfe6db` deleted that test. The page's reproduction command now runs 0 tests. (b) The crate README still lists "thin-wall pressure membrane components" and their unit tests. (c) The reproduction doc reproduces the multi-case `run-benchmark` against a committed witness. That witness still carries `STRESS-TP-PMM-P3-MILLTOL`'s `pressure_hoop`/`pressure_longitudinal`, but the head produces 4 values for that case, not 6. No test compares this witness | (a) Drop the test from the generator's `STRESS-RANGE-MECHANICS-ORIGINAL` entry and regenerate the page. (b) Update the README. (c) Regenerate the witness, or add a dated note that it predates U3 |
| A1-N-1 | NOTE, **for ROOT** (published texts) | `PP/src/lib.rs:1944` (formulation limitation); `:12028` (curved-bend review row `pressure_thrust_treatment=arc_end_cap_tangent_pair_plus_consistent_radial_wall_load`); `:11988` (joint review row `pressure_thrust_generation=load_side_user_effective_area;pressure_thrust=…`) | These published texts now describe treatments that no longer exist. Examples: "Pressure thrust and pressure stress retain the existing preview formulation …", and a radial-wall-load treatment whose API is deleted. I110 kept them on purpose, because they are pressure-free bytes in every non-exact envelope, including B1's pinned bytes. That is right under the byte-equality rule | Changing them is a public-text decision that moves pressure-free and B1 bytes. That belongs to ROOT and the owner (or T4), as I110 says |
| A1-N-2 | NOTE, **for ROOT** (governance docs) | `docs/TYPES.md:172` (`StressRecovery` "recovers … pressure membrane stress components … from … pressure inputs"); `docs/SPEC.md:591`, `:599`; `docs/VALIDATION_STRATEGY.md:50-51`, `:74`; `docs/INTENT.md:175`, `:182`; `docs/PRD.md:662` | These still list pressure membrane and pressure thrust as current capabilities. They are instruction or governance texts, which this PR cannot change | Route to ROOT. Pressure capability text goes with T4 |
| A1-N-3 | NOTE, **for ROOT/WORKING_ITEMS** (coverage lost with O1, as ruled) | B `PP/src/lib.rs` O1 `current_composite_derived_normal_friction_and_reversal`, deleted in `cda85e06d5` | I111's REPORT:37 says that "only O1 covers the three-way reversal with stop release". Its optional re-author on the joint-free demo (REPORT:54) was not done, so that behaviour now has no test. The owner's option A removes O1 explicitly | Accept the gap, or queue I111's optional re-author against a new independent reference |
| A1-N-4 | NOTE (G11 test strength) | `PP/src/lib.rs` `flexibility_joint_missing_a_user_stiffness_is_refused_not_dropped` | The test's axial, angular and torsional cases do not show the defect. At B they are already refused, by M07's `JOINT_ELEMENT_EQUILIBRIUM_UNQUALIFIED`, because the demo's lateral value is nonzero. With lateral = 0, which M07 admits, the defect is real for each of them. My probe (`E/g11_zero_*.log`) gives `MECHANICS_SOLVED` at B, with 627 rows including 2 "consumed" review rows; at the head it gives `JOINT_ELEMENT_STIFFNESS_INCOMPLETE`. The fix is correct; only the test is weak | Optional: add the zero-lateral variants, which fail at B and pass at the head. Builder residuals (an unmapped pipe or node, a missing `y_reference`) stay with T4, as I110 lists |
| A1-N-5 | NOTE (H-1 evidence) | `P/core/loads/stress_recovery/src/lib.rs:904`; `PP/src/lib.rs:10454`, `:11620` | My mutant removes all three `+ 0.0` sites and is byte-identical to the head on every sample row (`E/compare_h1mut.json`). So the byte evidence does not discriminate these sites: no sample row has a sign-deciding −0.0 there. H-1 still holds by construction, because each site is B's expression with `unwrap_or(0.0)` replaced by `0.0`, with the same IEEE operations and order. Keeping the `+ 0.0` is right: in `summarize_components`, `min_normal = base_normal − bending_total` publishes −0.0 for a −0.0 axial value with zero bending unless `+ 0.0` normalizes it | None. I110's "proven by the byte evidence" should read "equal bytes; identical arithmetic" |

The open verification items from REVIEW.md still stand:
- N-8: the Linux CI dispatch of the head, covering `r2-smoke`, PP `t13` and the runner's load-reference goldens;
- Pass B (the D1 call graph) runs separately.

## 1. Stage 1 repairs (`769c109d82`)

| Item | Change | Check |
|---|---|---|
| B-1 | The thermal half restored as `endpoint_section_cut_fixed_and_free_thermal_match_uniform_stations`, outside any scope | Identical to my probe (`REVIEW.md` §3); passes at the head (`E/add_cand_pp.log`). The "each pressure-only" claim is corrected in I110's round-3 record |
| N-5 | `pressureModeText`: the exact contract shows its mode; exactly `1.0.0/legacy_pressure_v1` shows "retired"; any other contract shows "unsupported"; a contract-free model shows "pressure-free namespace", with a count and a remedy when it still carries legacy primitives (category or dimension `pressure`, as the solver matches them) | Matches the solver's three refusals. Vitest: 1 test added (I110) |
| N-6 | `zero_legacy_pressure_primitive_is_refused_on_the_ordinary_route_and_the_retained_entry` (the retained entry publishes the ordinary refusal byte for byte; no successor); `zero_legacy_pressure_primitive_is_refused_by_a_cli_solve` (both modes) | Both pass (`E/add_cand_pp.log`, `E/add_cand_runner_bin.log`) |
| N-7 | `pressure_runtime.rs:119` and `:136` texts name `2.0.0/exact_straight_pressure_v2`; codes unchanged; pinned in the dispatch test | Passes. These are refusal texts only; no exact or pressure-free byte moves (§2) |

## 2. Bytes and H-1 (`E/bytes_cand2.jsonl`, `E/compare_stage2.json`)

The harness is the same as REVIEW.md §1.3, plus `-0.0` token counts (`E/scripts/rv127_bytes_v2.rs`). It ran in a fresh debug target in the registered profile, on the same 67 inputs, against REVIEW.md's B rows (same commit, same harness and toolchain).

| Set | Rows | All 9 fields equal to B | W1 successor / ordinary | Rows with `-0.0` (ordinary) | `-0.0` tokens: ordinary / export |
|---|---|---|---|---|---|
| E | 32 | **32** | 0 / 32 | 32 | 4,861 / 12,050 |
| F | 50 | **50** | 2 / 48 | 24 | 5,655 / 13,386 |
| B1 | 16 | **16** | **10 / 6** | 12 | 1,084 / 252 |
| P (nonzero legacy, refused) | 10 | **10** | 0 / 10 | 0 | 0 / 0 |

- **The refusal probes** (R1–R8, 26 rows) give the same outcomes as at Stage 1. The scope removal opened no route.
- **The H-1 mutant** (`E/scripts/h1_mutant.txt`, `E/bytes_h1mut.jsonl`, `E/compare_h1mut.json`) differs from the head on 0 of 134 rows (A1-N-5).
- **The other removed terms** were all absent for pressure-free models, as I checked by reading:
  - the thrust ledger entries;
  - `pressure_for_pipe`;
  - the hoop and longitudinal rows;
  - the W2 family;
  - the exact-sum `axial_loads` in `exact_straight_end_forces`, now thermal only;
  - `capture_case_source`'s `!pressure.is_empty()`;
  - the retained successor's `DerivedSection.membrane_radius`.

## 3. The B1 re-pin (`9930cfe6db`; `E/atoms_{base,cand}.txt`, `E/add_{base,cand}_pp.log`)

- **The two type changes:**
  - `StressComponents` loses two `Option<f64>`: 6 × 16 → 4 × 16 bytes. So `StressRecoveryResult` (components 96 → 64, `Option<StressSummary>`, two `Vec`s) and `(&str, StressRecoveryResult)` go from 192 to 160.
  - `DerivedSection` loses `membrane_radius`, so `(String, DerivedSection)` goes from 88 to 80.
- **The atoms:** the in-build atom values printed by `profile_in_build_record` differ between B and the head in exactly those two lines. The other 245 atoms, and every atom's assumed value, are identical.
- **The phases:** every phase falls by 800 in the requested part, with moving unchanged, in both modes.
  - 800 = 9 × 32 + 64 × 8, so the profile forms count those atoms 9 and 64 times per phase.
- **The pins:**
  - `PINNED_RECORD`: old − 800 in all 14 entries;
  - `W1_PHASE_BYTES`: the record's W1 per mode;
  - `MAX_PHASE_BYTES`: the record's W3, the maximum per mode;
  - `PINNED_RECORD_IDENTITY`: unchanged.
- **The tests:** `profile_in_build_record` asserted, not skipped, and `challenge_bounds_are_the_profile` pass at both B and the head.
- **The effect on M:** E_mov + R falls by 800 B (sparse 9,800,676,166 → 9,800,675,366); the fraction of M is unchanged at 0.8693 / 0.8745.
- This is the code's own maintenance rule ("regenerate the record with the profile, never one without the other") applied to a layout change, and nothing else. QUAL_B1's figures are historical; the possible merge conflict with I101's B1 lane is WORKING_ITEMS' to handle, as I110 says.

## 4. The consequential validation changes

| Change | Legacy oracle and nothing more? |
|---|---|
| `STRESS-PRESSURE-MEMBRANE-ORIGINAL` removed (benchmark, runner arm, hand calc, manual page, index rows) | **Yes.** Its two values were `p·r/t` and half of it, from `PressureBasis(100, 3, 0.5)`, the deleted membrane |
| `MECH-CURVED-BEND-PRESSURE-THRUST-ARC` removed (benchmark, 12 values, hand calc, README rows, 2 tests) | **Yes.** It solved an anchored arc under the end-cap pair plus `consistent_radial_pressure_nodal_loads` and read `arc_section_resultants_with_radial_pressure`, the deleted radial API. Curved-bend stiffness and section coverage remain in `MECH-EXPANSION-LOOP-CURVED-BEND-THERMAL`, `MECH-CURVED-BEND-DISTRIBUTED-FIXED-END` and the CB unit tests (19 pass). It had no manual page, so the mechanics page count is unchanged. The suite's "original 11 cases, 91 values" pin is unchanged; the new-case count goes 14 → 13 and the values 115 → 103 |
| `STRESS-TP-PMM-P3-MILLTOL-EFFECTIVE-WALL-STRESS` loses `pressure_hoop`/`pressure_longitudinal` | **Yes.** They came from the same deleted membrane, on the effective wall. The case keeps its 4 mechanics values, so the effective wall still feeds A, Z and J. The hand calculation records the removal |
| `complete_stress_input` loses its `PressureBasis` | **Yes.** It fed only the membrane values. The 4 governed quantities are unchanged, and no expected value reads `summary` |
| Manual 64 → 63 pages | **Yes:** only `stress-pressure-membrane-original.md`. The index is updated |
| Stress-recovery and CB tests removed (`non_finite_pressure_is_reported`, `stress_range_blocks_asymmetric_optional_components`, 6 radial-API tests) | **Yes.** Each built a pressure basis or a radial load. `range_optional`'s mismatch arm (`stress_recovery/src/lib.rs:835-855`) is now reachable only defensively: a missing resultant blocks the state first. No live behaviour loses its test |

Two caveats, both in the findings table:
- the stale references in A1-S-2;
- the surviving `primitive_loads` thrust in A1-S-1.

The validation crates pass at the head:
- stress benchmarks: 21;
- mechanics benchmarks: 39;
- `stress_recovery`: 46;
- `curved_bend`: 19;
- the runner binary: 20, including the suite-count and multi-case benchmark tests.

## 5. G11 (`6b6543dc1e`)

- **Defect confirmed at B** (`E/add_base_pp.log`, probe `rv127_probe_g11_before_fix`). The demo had its legacy pressures removed and C-150 lacked its lateral value. It gave `MECHANICS_SOLVED`, 628 rows, and 3 `component_user_stiffness_macro_element_review` rows that say "consumed", with no blocking diagnostic. This matches I110's `g11_confirm_before_fix.txt`.
- **The fix is right.** `refuse_unqualified_joint_elements` (`PP/src/preview_physics.rs:119-150`) checks all four user values before M07's lateral check. The builder (`PP/src/lib.rs:7542-7553`) skips the joint if any value is missing, and `modifiers: None` counts as all four missing. The refs are the joint and its pipe.
- **Tests:** at the head, the committed G11 test passes. My zero-lateral probe is refused for axial, angular and torsional (A1-N-4).
- **No committed document is affected.** I scanned 267 model documents in `P`, `P/apps` included: 4 flexibility joints, all with four values and a nonzero lateral value.
- **The new code `JOINT_ELEMENT_STIFFNESS_INCOMPLETE`** is within the brief ("the existing joint refusal or a precise one").

## 6. T4's holdings

- `git diff 4c0d5d7c00..6b6543dc1e` touches no FK source and nothing under `core/solver/nonlinear_integration`, `fixtures/`, `previewService.ts` or `core/product_preview`. In FK, only two `s11_site_table.rs` rows for the deleted CB functions change.
- The joint element's code (`user_stiffness_local_matrix` and its plumbing) is unchanged.
- The C-150 oracles O1–O4 are deleted. The added tests assert refusals only, and no copy of the old element's numbers is introduced.
- FK's and NI's existing unit tests of the element remain; they go with the code in T4's PR.
- A user-flexibility joint with lateral = 0 is admitted by M07, by design ("Axial, angular and torsional joint stiffness alone are unaffected"), and still reaches the element. RR's "after 1–3 nothing reaches it" holds for the flawed lateral configuration.

## 7. Host

- **Commands:** every cargo command went through `WT/tools/t3_cargo.sh` (`--locked --offline`), in fresh targets `WT/targets/rv127-{cand2,h1mut,base-pp,cand2-pp,cand2-x}`, with `TMPDIR` under `S`.
- **No Git writes,** no DEC-025 and no installs. `WT/t3-pret` was read only.
- **Deleted afterwards:** the archive copies `WT/rv127/` and the targets. `S` is kept.

## Records (`_run_records/addendum_01/`)

- **`scripts/`:**
  - `rv127_bytes_v2.rs`;
  - `run_bytes2.sh`;
  - `run_addendum_tests.sh`;
  - `run_g11_zero.sh`;
  - `probe_g11_before.rs.txt`;
  - `probe_g11_zero_lateral.rs.txt`;
  - `h1_mutant.txt`.
- **Byte evidence:**
  - `bytes_cand2.jsonl` and `bytes_h1mut.jsonl`;
  - `compare_stage2.json` and `compare_h1mut.json`.
- **Profile atoms:** `atoms_base.txt` and `atoms_cand.txt`.
- **Logs** (progress and result lines only):
  - `add_*.log`;
  - `g11_zero_{base,cand}.log`;
  - `bytes_{cand2,h1mut}.log`.

Sums are in the folder's `SHA256SUMS`. Paths use placeholders only.
