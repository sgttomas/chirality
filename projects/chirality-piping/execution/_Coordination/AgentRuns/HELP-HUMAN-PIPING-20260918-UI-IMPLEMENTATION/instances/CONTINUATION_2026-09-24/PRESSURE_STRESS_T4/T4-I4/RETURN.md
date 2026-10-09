# T4-I4 RETURN: validation inventory and the cases T4 rebuilds

- **Role:** TASK (Type 2), research only. Brief: `R4/BRIEFS/T4-I4_VALIDATION_INVENTORY.md`. Return path: T4's HELPS_HUMANS.
- **Basis:** main `ec5d397359` and U3 `70e7f49ced`. The merge base of the two is `7eae707bb7`, so `git diff ec5d397359 70e7f49ced` also shows main-only changes (PR-N's `correct_norm.rs`, the app-v4 files) as "removed". U3's own changes are `7eae707bb7..70e7f49ced`. All validation, benchmark, runner and hand-calculation files cited here are identical at `7eae707bb7` and `ec5d397359`.
- **Method:** read-only use of `git show`, `git diff` and `git grep`, and arithmetic in standard-library Python. There were no builds, cargo runs, test runs, commits or edits to tracked files. The only write is this file.
- **Notation:** "Fact" is read from the cited bytes. "Inference" is my reading or arithmetic and should be checked before reliance.

## 0. Findings most likely to change the plan

1. **U3 removed a fourth piece of validation that the plan does not list.** It deleted the whole `STRESS-PRESSURE-MEMBRANE-ORIGINAL` case: the benchmark, the runner binding, the hand calculation, the manual page and the index rows. It also deleted:
   - the test `stress_range_blocks_asymmetric_optional_pressure_components`;
   - two of the six quantities in the governed stress envelope;
   - MILLTOL's two values in the DEL-10-05 multi-case witness;
   - thirteen `*_historical_pressure_premise` product tests (eleven pressure-only ones in `390c882619`, then the two held with M07 in `cda85e06d5`). Several of these covered curved-bend pressure.
   
   Sources: commit `9930cfe6db` message; `git diff ec5d397359 70e7f49ced -- P/validation/benchmarks/stress/src/lib.rs`; `P/docs/validation_manual/index.md:78-80@70e7f49ced`.
2. **The mechanics count is 192 values, not 194.** At U3's head the mechanics whole suite is 24 cases and 192 values (`P/core/runner/headless/src/benchmark_binding.rs:1442-1456@70e7f49ced`). The figure 194 held between Stage 2 and `5bc6f269da`, which removed TP-PHYS-008/009's `pressure_thrust_force`. The commit message says "24 cases and 192 values (was 194)". The other counts are confirmed: stress 14 fixtures, 63 manual pages.
3. **No crate outside PP can carry pressure any more.** U3 removed every pressure API outside PP:
   - in `primitive_loads`, the Pressure arm of `prepare_straight_pipe_axial_effects`;
   - in `stress_recovery`, `PressureBasis` and the hoop and longitudinal components;
   - in `curved_bend`, the radial-pressure load and section API.

   The mechanics and stress benchmark crates do not depend on PP (`P/validation/benchmarks/{mechanics,stress}/Cargo.toml@70e7f49ced`). So each rebuilt case must either run PP's public entrypoint or re-add pressure arithmetic below PP. The second option conflicts with "Reuse `pressure_exact.rs`; do not fork its arithmetic" (`I/CORRECTNESS_DESIGN/PRESSURE_INTEGRATION.md:48`). There is a precedent for the first option: `physics_audit_regression` and `numerical_integrity` are benchmark crates that depend on PP.
4. **VP-STATIC has no pressure case, and the gate refuses pressure by construction.** The `ordinary_physics_1` gate is bound to the two first-static case IDs (`P/tools/validation/qualification_physics.py:54@70e7f49ced`). Its structure checks require:
   - `pressure_regions == []` (`P/tools/validation/qualification_physics_structure.py:231`);
   - empty pressure evidence (`:316`);
   - an all-zero pressure RHS (`:326`).

   All 14 load-reference runner inputs have zero pressure regions. T0 confirms that none of the VALIDATION_FOUNDATION comparisons has pressure (`I/T0_REASSESSMENT/RETURN.md:114`). A pressure case therefore needs its own VP-STATIC transport and package. T1's `load_reference_1` is the pattern to follow.
5. **Rebuilding under the exact contract changes the values, not just the plumbing.**
   - **CBPT:** the arc's membrane strain gains the Poisson term, so the tip displacement scales by (1−2ν). The fixture has no ν: it gave E and G separately. The wall force P stays. New rows appear: effective force S=0, the Lamé stresses and σz.
   - **MILLTOL:** thin-wall hoop and hoop/2 become Lamé surface values. The longitudinal value depends on the closures and restraints. The product has no corrosion-allowance input.
   - **TP-PHYS-008/009:** the legacy +pA had the same sign as the thermal force. In the exact contract the pressure contribution is wall tension 2νP, opposite to thermal compression. The invented sections (A=4 m², Ai=0.1 m², Iy=1.5≠Iz=2.0) are not annuli. The exact route derives its section from OD and wall, so every value changes.
6. **No admitted independent reference exists for pressure on bends.**
   - SSLL101 (Hovgaard) has no pressure load.
   - SSLL106's pressure assertions are radial and hoop values with no closure ledger, and carry a sign mismatch (MISMATCH-02).
   - SSLX102, the elbow and shell sources, and Hoesch are catalogued but unadmitted.
   - The Bourdon effect appears only as vendor terminology.

   The usable bases are project-original closed forms and the JOINT_REFERENCE J3/J4 cases for bellows thrust.
7. **Two outputs required for "full Q1" are not produced by the product.** These are direct transverse-shear stress and signed circumferential-fibre stress. An independent reference already exists for the first: the Saint-Venant annular shear field (`I/CORRECTNESS_DESIGN/SHEAR_REFERENCE/INDEPENDENT_REFUTATION.md:75-80`). The product is Euler–Bernoulli only, so SSLL106's transverse cases (Timoshenko) cannot be used yet.
8. **Hosted CI does not run the gate's Python tests.**
   - Hosted CI runs `cargo test` for every crate under `core/` and `validation/benchmarks/`.
   - Of the Piping Python tests, it runs only `test_ci_*.py`.
   - The qualification gate's own tests (`tests/test_qualification_*.py`) run only in the local DEC-025 sweep.
   
   A new VP-STATIC lane therefore needs either its recorded run or an explicit CI addition.

## 1. Where validation lives

### 1.1 Lanes (fact)

| Lane | Location | What it exercises | Pressure after U3 |
|---|---|---|---|
| Mechanics and stress benchmark crates (DEL-09-01/02) | `P/validation/benchmarks/{mechanics,stress}/src/lib.rs`; hand calculations in `P/validation/hand_calcs/{mechanics,stress}/` | Lower-level crates (`curved_bend`, `frame_kernel`, `primitive_loads`, `stress_recovery`, `straight_pipe`, …), not PP | None. Both crates' Cargo.toml list no PP dependency |
| Headless runner suites (DEL-10-05) | `P/core/runner/headless/src/benchmark_binding.rs` (`run-benchmark`, `run-regression`); witnesses in `P/validation/witness/{inputs,generated}/` | The same crate fixtures, bound by fixture ID; frozen original projection `P/validation/evidence/comparison_measurement/DEL0904_VD_20260811/CURRENT_25_FIXTURE_RUNNER_OUTPUT.json` (`benchmark_binding.rs:1405-1408`) | None |
| Validation manual (DEL-09-04) | `P/docs/validation_manual/cases/generate_validation_case_pages.py` (`MECHANICS_CASES` at :234, `STRESS_CASES` at :557, `--check` at :1146); `index.md` | Generated pages from hand calculations and suite tests | None |
| PP runtime tests (exact contract) | `P/core/product_physics/tests/pressure_*.rs`, `support_reactions_runtime.rs`, `stress_maximum_coverage.rs`, `elastic_extrema_runtime.rs`; fixtures under `tests/fixtures/pressure_reference/` | PP's public `run_linear_static_preview_with_mode`, both modes | The only pressure coverage (§5) |
| VP-HARNESS gate (VP-STATIC executions) | `P/tools/validation/qualification_gate.py` (transport `main_sparse_cli_1.0_raw0.1`), `qualification_physics.py` + `_structure.py` (`ordinary_physics_1_cli_1.0_raw0.2`), `qualification_load_reference.py` (`load_reference_1_cli_1.0_raw0.2`); packages in `P/validation/qualification/fixtures/{first_static,load_reference}/`; usage in `GATE_USAGE.md` | CLI `openpipestress-runner solve` against frozen selectors, references and criteria | None (finding 4) |
| Planning register | `P/validation/qualification/capability_inventory.json`, `check_inventory.py`, `README.md` | Q-profiles, VP mapping, source catalogue | Stale: its basis is `eec2855d`. T0's VP-SCOPE corrections are not applied (`I/T0_REASSESSMENT/RETURN.md:338-364`) |

### 1.2 The three programmes (fact; work graph at `ec5d397359`, unchanged by U3)

All rows below are in `P/execution/_Coordination/WorkGraphs/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/WORK_GRAPH.md`.

- **VP-STATIC** (`:275`): analytical mechanics and interacting static systems. Its completion check includes pressure, contents and head ownership, all six reactions and governing locations. Status: ACTIVE. Two runs are recorded:
  - the first static comparison: four case-mode runs with 292 scalar and 40 structural obligations, plus 36 nested section checks;
  - T1's load and reference states: 14 cases × 2 modes, 507 of 507 assertions per mode (`I/LOAD_STATE_IMPLEMENTATION/T1_VP_STATIC_RUN/RECORD.md`).
- **VP-PUBLISHED** (`:277`): formulation-matched published comparisons using SSLL106, Hovgaard or elbow variants. Status: PLANNED.
- **VP-SOURCES** (`:274`): complete source packages. Status: ACTIVE. Packets for SSLL106 and SSLL101 have been acquired, but four assertion subsets are still candidates. The Code_Aster assets were retrieved privately and are **not** in the repository (`I/VALIDATION_FOUNDATION/STATIC_REFERENCE_BASIS/RETURN.md`).
- **T4's row** (`:36`) assigns T4: "VP-STATIC: full Q1, including the missing direct transverse-shear and signed circumferential stress outputs. VP-PUBLISHED and VP-SOURCES: SSLL106, Hovgaard and elbow variants that match the formulation".

### 1.3 CI selection (fact)

- **Hosted numerical job.** It runs `cargo fetch` and `cargo test --offline --locked` for every `Cargo.toml` under `core/` and `validation/benchmarks/`, discovered automatically. A new crate there is picked up with no registration.
  - Workflow: `.github/workflows/piping-desktop-e2e.yml:171-195@ec5d397359`.
  - Driver: `P/tools/ci/numerical_ci.py:26-47`.
  - Discovery: `P/tools/release/check_release_readiness.py:28-31,70-81`.
- **When the job is selected.** Any change under `core/`, `validation/`, `fixtures/`, `schemas/` or `examples/` requires the numerical job (`P/tools/ci/e2e_plan.py:126-143`; `P/docs/CI_STRATEGY.md:7-13`).
- **Python tests.** The only Piping Python tests that hosted CI runs are `test_ci_*.py` (`piping-desktop-e2e.yml:54`). `pytest -q tests`, which includes the qualification-gate tests, runs only in the local DEC-025 sweep (`P/tools/release/run_evidence_sweep.py:191-194`).

### 1.4 How a new case is registered (fact)

**A mechanics fixture** (`P/validation/benchmarks/mechanics/src/lib.rs@70e7f49ced`):
- a constructor added to `fixture_inventory()` (:693);
- a `BenchmarkFamily` variant (:111), and an entry in `missing_required_families` (:1468) if the family is required;
- an observation arm in `fixture_observations` (:797), or an explicit runner arm;
- a custom comparison in `fixture_recorded_comparison_holds` (:1402) if the default 1e-9 is not used;
- count updates: `fixtures.len() == 24` (:6792), `VALUE_ADDRESSABLE_FIXTURE_IDS: [&str; 13]` (:6666) and `…_13_cases_and_103_names` (:6683);
- a hand calculation plus README rows in the hand-calculation and benchmark READMEs;
- runner coverage: any fixture without an explicit arm falls to `mechanics_suite_evaluation` (`benchmark_binding.rs:947`), and the whole-suite test asserts 24/192 (:1442-1456).

**A stress fixture:**
- `fixture_inventory()` (`stress/src/lib.rs:432`), the family enum (:73), `missing_required_families` (:463) and `fixtures.len() == 14` (:1863);
- the runner has **no** generic stress fallback: an unbound ID becomes `NotReusable` (`benchmark_binding.rs:1214`), and the whole-suite test pins exactly 3 blocked cases (:1625-1650). A new stress case therefore needs an explicit runner arm.

**A manual page:** add a `Case(...)` entry to the generator and regenerate. Pages are optional. Three mechanics fixtures have none: CONSTANT-EFFORT, CURVED-BEND-DISTRIBUTED and SUBSPAN-WIND. CBPT never had one.

**A VP-STATIC package** (T1's pattern):
- independent analytical references in PP test fixtures (`P/core/product_physics/tests/fixtures/load_reference_states/reference_cases.json`), consumed by PP runtime tests;
- a package under `P/validation/qualification/fixtures/<family>/` containing:
  - `MANIFEST.json` (`openpipestress.load_reference_qualification_manifest/1`, 14 cases);
  - `ADMISSION.json` and `PROVENANCE.json`;
  - per-case `runner_input`, `selectors`, `reference` and `criteria`;
  - a generator;
- an independent freeze before admission;
- an adapter `P/tools/validation/qualification_<family>.py` and its unittest;
- a recorded both-mode run in the undertaking records, with positive assertions and negative assertions (the negative ones check that the product does not reproduce the reference's wrong-result discriminators).

### 1.5 Counts after U3 (fact)

| Item | Main `ec5d397359` | U3 `70e7f49ced` | Source |
|---|---:|---:|---|
| Mechanics fixtures | 25 | 24 | `mechanics/src/lib.rs:6792` |
| Runner mechanics whole suite: cases / values | 25 / 206 | 24 / **192** | `benchmark_binding.rs:1442-1456` |
| Value-addressable mechanics: cases / names | 14 / 115 | 13 / 103 | `mechanics/src/lib.rs:6666-6723` |
| Stress fixtures | 15 | 14 | `stress/src/lib.rs:1863` |
| Governed complete stress envelope quantities | 6 | 4 | `stress/src/lib.rs:2473` |
| Manual pages: mechanics + stress + nonlinear | 64 (21+15+28) | 63 (21+14+28) | `index.md:78-80` |

## 2. The removed cases

### 2.1 `MECH-CURVED-BEND-PRESSURE-THRUST-ARC` (removed entirely)

**Model (fact):**
- Geometry: a quarter-circle arc, R=1.4 m, OD 0.2191 m, wall 0.0081 m; E=195 GPa and G=76 GPa given separately, with no ν; p=2.5 MPa.
- Supports: node A at (R,0,0) clamped; node B at (0,R,0) free.
- Flexibility factor: k ∈ {1,2}.
- Loads: the complete self-equilibrated system. This is the cap force +F_p t_B at B, plus the consistent nodal vector of the radial wall load q=(F_p/R)n, using the removed `consistent_radial_pressure_nodal_loads` (`mechanics/src/lib.rs:4013-4243@ec5d397359`).

**Reference (fact):** the project-original hand calculation `P/validation/hand_calcs/mechanics/curved_bend_pressure_thrust_arc.md@ec5d397359`, 374 lines. It derives:
- the cap and wall decomposition (§1);
- the wall-load integrals (§2) and exact self-equilibrium (§3);
- why static lumping cancels to zero (§4);
- the membrane identity, axial +pA with zero shear and moment (§6);
- the small-angle limit to the chord treatment (§7);
- the tip displacement u = (F_p R/(E A_s))(−(1−cosΦ), sinΦ, 0) (§8).

There is no external source. The hand calculation states that ovalization and Bourdon effects are outside the model (:367-372).

**Values and tolerance (fact):** 12 values: tip ux and uy = ∓1.080861534560850e-4 m; F_x(B) = −80833.98400998286 N; station axial +80833.98 N at fractions 0.25, 0.5 and 0.75; each for k=1 and k=2. The tolerance is relative 1e-9 with a 1.0 near-zero floor (`:4034-4035`, `:1484-1487`). The case had no manual page.

**What U3 removes (fact):**
- the fixture, the family, the observation and comparison arms, two tests (`:8104`, `:8123`), the hand calculation and the README rows;
- the `curved_bend` APIs it used: `consistent_radial_pressure_nodal_loads`, `arc_section_resultants_with_radial_pressure` and the radial load actions, with six crate tests;
- PP's curved-bend pressure-thrust assembly and its historical tests.

U3 keeps only `end_tangents` (`curved_bend/src/lib.rs:457@70e7f49ced`). The bend review row now says `pressure_thrust_treatment=none_pressure_refused_outside_the_exact_straight_contract` (PP `lib.rs:12028@70e7f49ced`).

**What a rebuild changes (inference, from `PRESSURE_REFERENCE_QUALIFICATION.md:22-36` applied to the arc):**
- **Strain.** With transferring closures the wall force is still Nw = P = pAi. The axial strain becomes (1−2ν)P/(E As) instead of P/(E As), so the tip displacement scales by (1−2ν). With ν=0.3 that gives ux = −4.3234461382434e-5 m and uy = +4.3234461382434e-5 m. With the ν implied by the legacy E and G (0.282895) it gives ±4.6932145579616e-5 m. The legacy value was ±1.0808615345608e-4.
- **ν becomes an explicit input.** The exact contract derives G from E and ν; it does not accept independent constants (`SHEAR_REFERENCE/CONTRACT.md:34`).
- **New rows are required:**
  - effective force S = Nw − P = 0;
  - σz = P/As = 1.5054857e7 Pa;
  - Lamé hoop stress 3.2609714e7 Pa inner and 3.0109714e7 Pa outer; radial stress −2.5e6 and 0 Pa.
- **k-independence still holds.** The membrane state has M=0.
- **Probable mechanism.** PP already applies thermal strain on curved bends through the "exact free-expansion identity" (`add_curved_bend_thermal_equivalent_load`, PP `lib.rs:10773@70e7f49ced`). I infer the Poisson eigenstrain could use the same mechanism. The `curved_bend` crate itself has no eigenstrain API.
- **Open design point.** The wall load and cap pair must be reconciled with wall-force and effective-force recovery. Simply adding or deleting the bend term is not acceptable (`PRESSURE_INTEGRATION.md:25`).
- **Same reference class.** This stays a beam-level closed form. A shell or elbow reference would differ because of Bourdon and ovalization effects.

### 2.2 The membrane values of `STRESS-TP-PMM-P3-MILLTOL-EFFECTIVE-WALL-STRESS` (case kept, two values removed)

**Before U3 (fact):**
- Inputs: OD 0.2; nominal wall 0.01; corrosion allowance c 0.002; mill tolerance m 0.00125, so t_eff = 0.00675; p = 2000 Pa.
- Formulas: hoop = p r_m/t_eff with r_m = (OD − t_eff)/2, giving 28629.62962962963 Pa; longitudinal = hoop/2 = 14314.814814814816 Pa (`stress/src/lib.rs:1626,1680-1750@ec5d397359`; hand calculation lines 43, 58, 73-82).
- Tolerance: the crate epsilon of 1e-9 absolute. No fixture-level policy applies.

**What U3 removes and keeps (fact):** U3 removes `MILLTOL_PRESSURE`, the `PressureBasis` in `milltol_stress_input`, the two expected values, the runner's two optional components and the two values in `del1005_payload_binding_benchmark_multi_case.json`. The axial, bending and torsion values and the manual page are unchanged.

**What a rebuild changes (inference, using the exact route's section rule at PP `lib.rs:7243-7256` and `:10211-10230@70e7f49ced`):**

Take ri = 0.09325 and ro = 0.1. The exact values are:

| Quantity | Value |
|---|---|
| Lamé radial | −2000 / 0 Pa |
| Lamé hoop, inner / outer | 28664.558478 / 26664.558478 Pa |
| σz, free with transferring closures (= P/As) | 13332.279239 Pa |
| σz, axially restrained, ν=0.3 (= 2νP/As) | 7999.367543 Pa |

The legacy "hoop/2" has no exact counterpart. On the exact route, `element_local_axial_normal_stress` is replaced by `pipe_axial_membrane_stress_v2` for pressurized members (`pressure_runtime.rs:268-362`), so the axial value also changes meaning.

Two section facts matter here:
- PP has **no corrosion-allowance input** (0 hits in `PP/src`; only `core/section_properties/calculator.py:45` has one). The fixture's c must therefore be folded into the authored wall.
- The exact geometry uses OD and (wall − mill tolerance) for both the stress section and the bore Ai.

Whether the pressure bore should follow the reduced wall is an M30 decision, not a validation detail. A rebuild in the `stress_recovery` crate would need a pressure API that U3 deleted. Rebuilding on PP keeps a single implementation of the arithmetic.

### 2.3 MECH-TP-PHYS-008/009: the pressure halves

**Before U3 (fact):** a `PrimitiveLoad` of category Pressure, 90 Pa, with `internal_area = 0.1 m²`, gave F = pA = 9 N through `primitive_loads::prepare_straight_pipe_axial_effects` (`mechanics/src/lib.rs:6072-6114@ec5d397359`). This was added with the **same sign** to the thermal force EAαΔT = 3 N, giving a total of 12 N: the equivalent loads were ∓12 and the stations 12. Tolerance: `INTERNAL_ASSERTION_EPSILON = 1e-9` absolute (`:52`).

Sections:
- 008: E=1000, A=4, J=1.
- 009: also G=400, Iy=1.5, Iz=2.0, a distributed transverse load, and node 1 restrained only in Ux.

**What U3 does (fact):**
- It removes the pressure loads, `internal_area`, `pressure_thrust_force` and the Pressure arm in `primitive_loads`, which now refuses pressure with `UnsupportedTargetForCategory` (commit `5bc6f269da`).
- Totals become 3 N, and 009's hook count goes from 2 to 1.
- The fixture IDs are kept.
- The runner compares the two cases with the frozen original projection by status and value names only (`RETIRED_PRESSURE_HALVES`, `benchmark_binding.rs:1436`).
- `PRESSURE_INTEGRATION.md:19` already said that "TP-008 remains archived as the former model premise".

**What a rebuild changes (inference):**
- **Physics.** For a fixed-fixed closed pipe with transferring closures, the pressure adds wall **tension** 2νP, with S = Nw − P and support reactions ±(P − Nw). The thermal force is compression. The legacy fixture summed them with the same sign.
- **Geometry.** The sections are not circular annuli (Iy≠Iz, and A and Ai are unrelated to I and J). The exact route derives the section from OD and wall. A rebuild therefore needs new geometry, and the thermal and transverse values change too, unless the old crate-level halves are kept and the pressure half becomes a separate exact-route case.
- **Overlap.** PP's `six_si_pressure_states_through_both_public_solver_modes` (`pressure_runtime.rs:432-478@70e7f49ced`) already covers fixed and free, transfer and separate closures, and thermal, with independently checked values (`PRESSURE_INTEGRATION.md:33-42`). The new content of a rebuilt 009 is pressure combined with a partial-span transverse load and a mixed restraint.

### 2.4 Validation U3 also removed, which the plan does not list (fact)

- **`STRESS-PRESSURE-MEMBRANE-ORIGINAL`:**
  - inputs p=100, r=3, t=0.5; hoop 600 and longitudinal 300 (`stress/src/lib.rs:576-607@ec5d397359`);
  - the hand calculation `pressure_membrane.md`, the manual page, two index rows, the generator entry and the runner arm.
- **`stress_range_blocks_asymmetric_optional_pressure_components`:** the blocking of asymmetric optional pressure in a stress range.
- **Governed stress envelope:** the `pressure-hoop` and `pressure-longitudinal` quantities (6 → 4).
- **PP:**
  - thirteen `*_historical_pressure_premise` tests (eleven pressure-only ones, then the two held with M07), including `endpoint_section_cut_curved_bend_pressure_shows_membrane_end_and_station_state…` and `curved_bend_macro_span_pressure_reaches_nonlinear_loop…`;
  - `pressure_thrust_on_macro_span_assembles_complete_self_equilibrated_arc_system`;
  - the joint thrust test `expansion_joint_pressure_thrust_uses_user_effective_area…`;
  - S11-F F10 and S11-G T6a's pressure run (commits `390c882619`, `cda85e06d5`, `9930cfe6db`).

Inference: these product tests encoded the legacy premise, so they are not targets to rebuild. Their station and membrane assertions do show which output shapes T4's curved composition should cover.

### 2.5 Summary of what changes under the exact contract

| Case | Treatment | Values | Reference |
|---|---|---|---|
| CBPT | Wall/effective ledger plus Poisson eigenstrain; S, σz and Lamé rows added | Tip ×(1−2ν); Nw unchanged; ν becomes an explicit input | Same beam-level closed form plus the Poisson term (needs a new freeze) |
| MILLTOL membrane | Lamé surface values; σz depends on boundary conditions; corrosion folded into the wall; bore follows the reduced wall | All change: inner hoop +0.12%, σz −6.9% (free) | Lamé (`PRESSURE_REFERENCE_QUALIFICATION.md:11-36`) |
| TP-PHYS-008/009 pressure | Pressure is wall tension 2νP, not an end load pair; caps are ledger loads | Sign and magnitude change; geometry must become annular | Already covered by PP's six-state oracle; new content is the combined transverse load |
| PRESSURE-MEMBRANE (not in plan) | Thin-wall membrane replaced by Lamé | All change | Lamé |

## 3. VP-STATIC's Q1

**Fact:**
- **The Q1 profile.** `Q1-STRAIGHT-STATIC` (`capability_inventory.json:1600-1628@70e7f49ced`) is `selected_preparation`. Its qualification is `not_run_under_programme` and its `required_case_inventory` is `not_frozen`.
  - Capabilities: straight static, load fields, `pressure_thermal`, linear restraints, self-weight, thermal material states, stress results and numerical integrity.
  - Required output sets: kinematics, load_inventory, material_state, member_actions, `pressure_state`, run_identity, `stress_fields` and support_actions.
- **The first development cut.** `STATIC-CORE-FIRST` lists axial, transverse/moment, torsion, uniform and partial distributed loads, free/fixed thermal and spring device force. It keeps prescribed motion mandatory for complete Q1. `STATIC-INTERACTIONS-FIRST` covers pressure with free, restrained and separate closures plus thermal, and the head column.
- **Executed so far:**
  - first-static axial and bending-torsion, unpressurized, both modes;
  - T1's 14 load/reference-state cases, unpressurized.
- **Missing for full Q1:**
  - every pressure_state case;
  - distributed loads, self-weight and spring device force as VP-STATIC cases (some exist only as PP tests or crate fixtures);
  - head and contents (T2);
  - the two outputs below.
- **Transverse-shear and circumferential outputs.** The product publishes neither direct transverse-shear stress nor signed circumferential-fibre stress.
  - `elastic_section.rs:8@70e7f49ced` states it does not produce hoop, radial or transverse-shear stresses.
  - The first-static package records `signed_circumferential_extrema` as "no separate producer rows exist. Not claimed direct scalar output coverage" (`first_static/STRUCTURAL_EXPECTATIONS.json`).
  - `GATE_USAGE.md:189-192` keeps both as separate obligations; T0 marks them unsupported (`T0_REASSESSMENT/RETURN.md:353`).
- **Euler–Bernoulli only.** The product is Euler–Bernoulli only (`T0_REASSESSMENT/RETURN.md`, VP-SCOPE delta item 3). SHEAR_REFERENCE is a design, not an implementation.

**Inference:**
- **Transverse shear.** A direct transverse-shear stress output can be validated against the Saint-Venant annular field (`SHEAR_REFERENCE/INDEPENDENT_REFUTATION.md:75-80`), not V/(κA) (`SHEAR_REFERENCE/CONTRACT.md:44`).
- **Circumferential fibres.** Signed circumferential-fibre values can be validated against σx(y,z) = N/A + My z/I − Mz y/I (`elastic_section.rs:5`) at declared fibres, with Lamé hoop/radial stresses kept as separate surface quantities.
- **Ownership.** Both are T4 product outputs (M14/M37/M31) before they are validation items.

## 4. Independent references in the repository for pressure on bends, joints and stress

| Reference | What is qualified | Limits and formulation match |
|---|---|---|
| Lamé/Hooke straight annulus (`I/CORRECTNESS_DESIGN/PRESSURE_REFERENCE_QUALIFICATION.md`; frozen oracle `P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260914-RESULT-COMPATIBILITY-PRESSURE/instances/PRESSURE_ORACLE/`) | PASS for a long, straight, homogeneous-isotropic, small-strain annulus with zero external increment: five rational states (:44-50) and the 6 m SI companion (:52) | Straight only. External pressure needs (pi·Ai − po·Ao)/As (:85). No ovalization, stability or local end stress. Matches the exact contract |
| Welded-bend free body (same file, :61-62) | Fluid-on-wall resultant P(tin − tout); with wall cuts, the sum is S(tout − tin). There is no universal extra bend thrust | An illustration, "not a complete elbow constitutive model". Usable as a check on equilibrium and the reaction ledger only |
| Removed CBPT derivation (§2.1) | Beam-level statics of the arc | Lacks the Poisson term. Never independently re-qualified as an exact-contract oracle. Excludes ovalization and Bourdon effects |
| STRESS_REFERENCE (`I/CORRECTNESS_DESIGN/STRESS_REFERENCE.md`) | Annulus normal and torsion extrema S1/S2 (:99-173); pressure companion §8 (:392-431), matching the six states | Excludes transverse shear, ovalization and pressure hoop/radial in the extrema (:129-134). Line :536 calls for literature acceptance by an integrating reviewer before production use |
| SHEAR_REFERENCE | Energy-normalized annular Timoshenko Ks; Saint-Venant shear-stress field (:75-80) | Straight prismatic only. Excludes elbow flexibility, ovalization and pressure stiffening (`CONTRACT.md:44`). Not implemented in the product |
| JOINT_REFERENCE (`CONTRACT.md`) | Midpoint connector; pressure work with effective area Ae (:54-69); J3 tied/untied/free/anchored cases (:126-136); J4 double-count mutation (:138) | Equal-bore, coaxial, linear. Ae must be supplied by the user. No bellows local stress or stability, no pressure-balanced or limit-rod hardware. The pipe-only pressure region cannot yet represent a joint interface (`RETURN.md:10`) |
| SSLL106 (Code_Aster; `STATIC_REFERENCE_BASIS/APPLICABILITY.md`) | Candidate subsets only: axial, torsion and the two pure moments (:13-15) | Transverse cases include Timoshenko shear (:27), so they do not match Euler–Bernoulli. Pressure (`FORCE_TUYAU/PRES`) tests WO and hoop stress/strain with no closure or effective-force ledger (:31). MISMATCH-02 pressure sign (:46). Assets are not in the repository |
| SSLL101 Hovgaard (same file, :35-41) | A later assembled-system numerical comparison | **No pressure load.** Reduced bend inertias and shear coefficients must match. ±2% published lineage; not independent physical evidence |
| SSLX102 elbow ovalization; Abaqus elbow; Hoesch 2024 (`capability_inventory.json` source catalogue; `PRESSURE_REFERENCE_QUALIFICATION.md:75-76`) | Catalogued or deferred only | Shell and enriched effects differ from the macro-element. Not retrieved or admitted |
| Bourdon effect (CAESAR II v12, Bentley KB; `PRESSURE_REFERENCE_QUALIFICATION.md:77`) | Terminology only, "adopt neither" | Vendor "Bourdon" combines straight-pipe pressure extension (the exact contract always includes it through 2νP) with bend opening. Beyond the beam membrane stretch, bend opening needs a shell reference. T0: "separately qualified options (T4, if selected)" (`T0_REASSESSMENT/RETURN.md:126`) |
| Elbow flexibility and pressure stiffening | None | The product takes a user-entered k (no code formula). Pressure stiffening has no reference in the repository and is deferred to a nonlinear/prestress contract (`PRESSURE_REFERENCE_QUALIFICATION.md:73-75`) |

Mismatches to note:
- SSLL106 pressure (radial/plane-stress, no closures) does not match the exact contract.
- SSLL106 transverse cases (Timoshenko) do not match the Euler–Bernoulli product.
- Neither SSLL101 nor the CBPT closed form tests pressure-dependent elbow flexibility.
- Any shell or elbow reference will include Bourdon and ovalization effects that a beam formulation cannot reproduce. A comparison would have to separate them, or the scope would have to declare them excluded.

## 5. Exact-contract validation that exists today, and the pattern to follow

**What exists (fact; all straight pipe, all in PP, all in hosted CI as `core/` crate tests):**

| Test file | Tests | Covers |
|---|---:|---|
| `P/core/product_physics/tests/pressure_runtime.rs` | 15 | Six SI states, both modes (:432); rotation and mm/MPa normalization (:480); equal-bore unequal wall/E chains; mixed closures and support reactions; distributed load versus eigenload; signed pressure, ν=0 and thermal reversal; contract and region refusals; legacy refusal (:823) |
| `pressure_section_geometry.rs`, with `tests/fixtures/pressure_reference/*.json` | 9 | Five frozen expectation files: source OD/wall, near-incompressible, two-span, rotation |
| `pressure_grouping_limits.rs` | 1 | Explicit range refusal |
| `pressure_membrane_range.rs` | 2 | Explicit range refusal |
| `support_reactions_runtime.rs` | 4 | Signed six-component reactions |
| `stress_maximum_coverage.rs` | 4 | Coverage and tie controls for maxima |
| `elastic_extrema_runtime.rs` | 2 | X1 extrema |

There is also a native witness of 51 checks per mode (`I/_run_records/JOINED_ENGINE_NATIVE/RETURN.md`, cited by `T0_REASSESSMENT/RETURN.md:112`).

One gap: `pressure_runtime.rs:3` cites `PHYSICS_MANAGER/ASSEMBLY_ORACLE/FROZEN_RUNTIME_EXPECTATIONS.json`, which is in no commit (`git log --all` finds none). Its values are reproduced in `PRESSURE_INTEGRATION.md:33-42` and STRESS_REFERENCE §8.

**The pattern (fact, from those files):**
- Build a JSON model with a 0.3.0 document, `pressure_contract {2.0.0, exact_straight_pressure_v2}`, materials with E and ν, `pressure_regions` with explicit `closure_transfer` terminals, and OD and wall.
- Call `run_linear_static_preview_with_mode` in both modes.
- Assert `MECHANICS_SOLVED` with no blocking diagnostics.
- Compare, at five stations, the rows `pipe_wall_axial_force_v2`, `pipe_effective_axial_force_v2`, `pipe_axial_membrane_stress_v2`, `pipe_lame_radial_stress_v2` (inner and outer), `pipe_lame_hoop_stress_v2` (inner and outer) and `pipe_wall_endpoint_action_v2`, together with the units, frames and case basis.
- Assert that no legacy `element_local_axial_*` or `pressure_hoop`/`pressure_longitudinal` rows are present (:268-362).
- Check six-component support reactions and displacements.
- Tolerance: relative 1e-9, with an explicit zero-scale absolute for zero targets (:37-49). This is the same as T1's VP-STATIC criteria.

**Recommended path for T4's rebuilt cases (inference):**
1. Freeze an independent reference first: a hand calculation plus a reference JSON under `PP/tests/fixtures/<family>/`, with an independent check.
2. Add a PP runtime test on the public entrypoint (it runs in CI).
3. Add a VP-STATIC package and transport that admit pressure kinds and nonzero pressure evidence, modelled on `load_reference_1`, and record both-mode runs.
4. Keep the crate-level cases (TP-PHYS-008/009, MILLTOL) pressure-free unless the plan decides to give the benchmark crates a PP dependency.
5. Add manual pages through the generator where the case lives in a benchmark crate. PP-only cases have no manual lane today. That is a decision for DEL-09-04.

## 6. Not done here

- No runner, test or build was executed. All counts come from source assertions and commit messages.
- I did not read the T3 worktree. I did not verify the native witness or the T1 run records beyond their summaries.
- The numbers in §2 marked as inference are arithmetic on the cited formulas. They are not frozen references.
