# T4-I6 Part A: test specification for T4-U0 (exact-route hardening)

TASK T4-I6 (Type 2) for T4's WORKING_ITEMS. Brief `R4/BRIEFS/T4-I6_U0_U1_REFERENCES.md`; terms `R4/BRIEFS/T4_WI_COMMON.md`. Frozen for refutation before any T4-U0 code is read.

- **Code basis:** `ed012c7ccf` (T3's U3 PR head). Citations are `path:line@ed012c7ccf` unless marked. `PRT` = `PP/src/pressure_runtime.rs`, `PPL` = `PP/src/lib.rs`, `RE` = `P/core/reporting/result_export`, `HR` = `P/core/runner/headless/src/lib.rs`.
- **F** = read from the cited bytes. **I** = inference. Nothing here was built or run in cargo.
- **Base documents** (all invented, committed):
  - `X0` = `PP/tests/fixtures/exact_pressure_connected_request.json` (0.3.0, `2.0.0/exact_straight_pressure_v2`; nodes `node:fixture-root`, `node:fixture-tip`; pipe `pipe:fixture-span`; anchor `support:fixture-root`; cases `case:closed-pressure` (region `region:fixture-pressure`, 2000 kPa) and `case:six-component-load`; no components or combinations).
  - `Y0` = `P/fixtures/product_preview/load_reference/pressure.request.json` (0.4.0; nodes `node:root`, `node:middle`; pipe `pipe:first`; anchors `support:root`, `support:far`; cases `case:cold-pressure`, `case:hot-pressure`, each with region `region:closed` at 2 MPa).
- **Entries.** "Both entries" = PP's captured `run_linear_static_preview_value_with_mode` and typed `run_linear_static_preview_with_mode` (`PPL:2128-2146`). "Both modes" = `DenseScrutiny` and `SparseInteractive`. "Runner" = `HR` `run_preview_model_value_with_mode` (`HR:729`).

## A0. Facts every item relies on

- **F:** `validate_profile` (`PRT:115-353`) runs first, together with `case_state::resolve::validate_document`, `validate_model_inputs` and `validate_support_family_tokens` (`PPL:2365-2368`). Their diagnostics are concatenated in that order and the envelope returns blocked at the first `has_blocking` (`PPL:2387-2389`). Diagnostics are not sorted (`blocked_envelope`, `PPL:13285-13338`).
- **F:** a pressure-runtime diagnostic has `id = "diagnostic:pressure-runtime:" + refs.join(":").replace(':','-') + ":" + CODE`, severity `blocking`, `source = "core/product_physics/src/pressure_runtime.rs"` (`PRT:89-104`; `stable_suffix` `PPL:13653-13655`).
- **F:** a blocked exact envelope has `status.mechanics = "MODEL_INCOMPLETE"`, `results = []`, `contract_evidence = {"pressure":[],"connector":[],"exact_cases":[]}` (0.3.0) or the same plus `"load_reference_states":[]` (0.4.0), and producer `physics-1` (0.3.0) or `load-reference-1` (0.4.0) (`PPL:991-999,13285-13300`).
- **F:** the runner's blocked exact output has `canonical_export_unavailability = "SOURCE_NOT_SOLVED"`, no result document and no qualified evidence (`HR:1544-1575`).
- **Common expected outcome for every refusal below** ("blocked as A0"): both entries and both modes give the same diagnostics; the envelope is blocked as above; the named diagnostic is present with exactly the stated `affected_refs`, severity and source; no panic.

## A1. The three untested refusals

**F:** no test names `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED`, `EXACT_PRESSURE_COMBINATION_UNSUPPORTED` or `OBJECTIVE_CONNECTOR_NOT_IMPLEMENTED` (T4-I1 §2; the codes appear only at `PRT:165,176,181,206,230`).

| # | Trigger (patch on X0) | Code and refs (site) | 0.4.0 (patch on Y0) |
|---|---|---|---|
| A1.1 | `components += {"id":"component:valve","kind":"valve","node":"node:fixture-tip","provenance":"invented_u0_control"}` (metadata only: no geometry, modifiers or interface) | `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED`, refs `["component:valve"]`, id `diagnostic:pressure-runtime:component-valve:EXACT_PRESSURE_COMPOSITION_UNSUPPORTED` (`PRT:175-178`) | same, node `node:middle` |
| A1.2 | a realized bend: `components += {"id":"component:bend","kind":"bend","node":"node:fixture-tip","geometry":{"bend_pipe_ref":"pipe:fixture-span","bend_radius":{"value":1.0,"unit":"m"},"bend_plane_orientation":"invented","bend_geometry_source_reference":"invented"},"modifiers":{"flexibility_factor_user_value":{"value":1.0,"unit":"none"},"source_reference":"invented"},"mechanics_interface":{"solver_consumption":"curved_bend_macro_element"},"provenance":"invented_u0_control"}`; pipe `y_reference` `(0,1,0)` | same code, refs `["component:bend"]`. This is the plan's negative control "a bend in an exact model is refused, not a panic" | same, `pipe:first`, chord 1 m |
| A1.3 | `supports += {"id":"support:gap","node":"node:fixture-tip","family":"nonlinear","restraints":[],"nonlinear":{"behavior":"gap","dof":"UZ","initial_state":"inactive","closes_when":"positive_displacement","gap":{"value":1000.0,"unit":"mm"}},"provenance":"invented_u0_control"}` | same code, refs `["support:gap"]` (`PRT:179-184`) | same; also add `{"support_ref":"support:gap","participation":{"kind":"active_model_device"}}` to every case's `support_states` so that no load-state code is added |
| A1.4 | `supports += {"id":"support:ce","node":"node:fixture-tip","family":"constant_effort_support","restraints":["UY"],"hanger":{"hanger_type":"constant_effort_support","constant_load":{"value":375.0,"unit":"N"},"travel_range":{"value":0.05,"unit":"m"},"source_reference":"invented"},"provenance":"invented_u0_control"}` (shape from `PP/tests/f1b_w2_runtime.rs:344-347`) | same code, refs `["support:ce"]` | as A1.3 |
| A1.5 | `load_cases["case:six-component-load"].equivalent_static = {"provenance":"invented_u0_control"}` (every field is optional, `PPL:596-603`; presence alone triggers) | same code, refs `["case:six-component-load","equivalent_static"]`, id `...:case-six-component-load-equivalent_static:EXACT_PRESSURE_COMPOSITION_UNSUPPORTED` (`PRT:227-234`) | on `case:cold-pressure` |
| A1.6 | `combinations = [{"id":"combination:sum","basis":"mechanics","terms":[{"load_case":"case:closed-pressure","factor":1.0},{"load_case":"case:six-component-load","factor":1.0}],"provenance":"invented_u0_control"}]` | `EXACT_PRESSURE_COMBINATION_UNSUPPORTED`, refs `["combination:sum"]` (`PRT:205-208`) | terms on `case:cold-pressure` and `case:hot-pressure` |
| A1.7 | `components += {"id":"component:connector","kind":"expansion_joint","node":"node:fixture-tip","objective_connector":{"version":"1.0.0"},"provenance":"invented_u0_control"}` | `OBJECTIVE_CONNECTOR_NOT_IMPLEMENTED`, refs `["component:connector","objective_connector"]` (`PRT:158-170`), then `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED`, refs `["component:connector"]`. `validate_components` adds the warning `EXPANSION_JOINT_MECHANICS_INTERFACE_UNSUPPORTED` (`PP/src/validation.rs:1146-1162`) | same |
| A1.8 | A1.7 with `"objective_connector":{"version":"2.0.0"}` | `OBJECTIVE_CONNECTOR_VERSION_UNSUPPORTED`, same refs, then the composition code | same |
| A1.9 | A1.7's component in a 0.2.0 document without `pressure_contract` (the pressure-free route) | `PREVIEW_CONTRACT_VERSION_MISMATCH`, refs `["component:connector","objective_connector"]` (`PRT:160-161`); no composition code (not exact) | n/a |

**Precedence where two apply (F, from emission order; all applicable codes are emitted, none suppresses another):**
1. Contract dispatch (`PRT:116-153`) before connector codes.
2. Connector codes (`PRT:158-170`, component order) before composition codes.
3. Exact-profile codes in this order: component composition (component order), then support composition (support order), then `EXACT_PRESSURE_RESULT_ID_COLLISION` (`PRT:185-204`), then combinations (`PRT:205-208`).
4. Then, per case in case order: `equivalent_static` composition (`PRT:227-234`), `EXACT_PRESSURE_REQUIRES_REGION`, `EXACT_PRESSURE_REGIONS_REQUIRED`, then each region's input codes (`PRT:248-352`).
5. Then `validate_document` (0.4.0 load-state codes), `validate_model_inputs` and `validate_support_family_tokens`.

**Required precedence tests** (assert the index of the first code is below the index of the second):
- A1.7: connector code before composition code for the same component.
- A1.1 + A1.6 together: composition before combination.
- A1.1 + A1.3: component before support.
- A1.5 + A1.6: combination before `equivalent_static`.
- A2's negative pressure + A1.1: composition before the negative-pressure code.
- On Y0, A1.3 without its `support_states` entry: the support's composition code before `LOAD_STATE_SUPPORT_STATE_MISSING`. That code comes from `validate_document` → `validate_case` (`PP/src/case_state/resolve.rs:212,338-342`), in the same first batch.

**I:** T4-U3's `LEGACY_FINITE_CONNECTOR_REAUTHOR_REQUIRED` is specified to come before the composition code (plan §6). That is not T4-U0's, and no U0 test should pin a legacy-joint order.

**Runner:** A1.1 and A1.6 through `HR` in both modes: blocked as A0, `SOURCE_NOT_SOLVED`.

## A2. v2 refuses p < 0 at the producer

**Facts.**
- **F:** the producer admits any finite signed pressure: `PRT:274-285` ("explicit finite signed pressure quantity"); `InternalDifferentialPressure::new` refuses only non-finite values (`PP/src/pressure_exact.rs:274-279`).
- **F:** the three readers refuse `p_pa < 0` on the published region evidence:

  | Reader | Check | Error |
  |---|---|---|
  | Rust | `RE/src/physics_evidence.rs:627` `number(p_pa) >= 0.0` | `SOURCE_PHYSICS_PRESSURE_RANGE` (`:34-40`) |
  | Python | `P/core/analysis_runs/physics_evidence.py:158` `region["p_pa"] >= 0` | `SOURCE_PHYSICS_EVIDENCE_INVALID: region pressure basis` (`:38-40`) |
  | TypeScript | `P/apps/desktop/src/features/results/physicsResultEvidence.ts:138` `r.p_pa >= 0` | `PHYSICS_EVIDENCE_PRESSURE_INVALID` (`:7-9`) |
- **F:** every pressure unit converts to Pa by a positive linear factor of at least 1: Pa, kPa, MPa, GPa, bar, psi, ksi (`P/core/units/src/lib.rs:412-413,528-545`; `PPL:8979-9019`). So the authored value and `p_pa` have the same sign, and a negative value cannot underflow to −0.0.
- **F:** no committed JSON with `pressure_regions` carries a negative or signed-zero region pressure: 0 of 166 files (`_run_records/neg_scan.py`, `neg_scan.stdout.txt`).

**The proposed refusal.**
- **Code:** `PRESSURE_REGION_PRESSURE_NEGATIVE`, severity `blocking`, refs `[case.id, region id, "pressure"]`. It sits next to the existing `PRESSURE_REGION_PRESSURE_INVALID`, and mirrors the Rust reader's `PRESSURE_RANGE`.
- **Message:** "the 2.0.0/exact_straight_pressure_v2 profile admits internal differential pressure p >= 0 only, and its result readers refuse p_pa < 0; a negative differential (external pressure exceeding internal) is refused, not published; external-pressure stability and collapse are not assessed by this profile".
- **Site:** in `validate_profile`'s region loop, immediately after the finite check (`PRT:274-285`). Condition: `pressure.value.is_finite() && pressure.value < 0.0`. Because it is in `validate_profile`, it fires on every entry, both modes and 0.3.0 and 0.4.0, and also inside `build_pressure_case_with_members` (`PRT:434-437`).
- **Signed zero (F + I):** −0.0 ≥ 0 is true in all three readers (Rust `f64`, Python `float`, JavaScript `number`), so the readers admit `p_pa = -0.0`. The producer must match: the strict IEEE test `value < 0.0` admits −0.0 and +0.0. Today's producer admits −0.0 and publishes it unchanged (serde writes `-0.0`). Under this rule a −0.0 document is untouched, so its bytes stay identical.

**Tests.**

| # | Input | Entry | Expected |
|---|---|---|---|
| A2.1 | X0, `case:closed-pressure` region pressure `{"value":-2000,"unit":"kPa"}` | both entries, both modes; runner both modes | blocked as A0; `PRESSURE_REGION_PRESSURE_NEGATIVE`, refs `["case:closed-pressure","region:fixture-pressure","pressure"]`, id `diagnostic:pressure-runtime:case-closed-pressure-region-fixture-pressure-pressure:PRESSURE_REGION_PRESSURE_NEGATIVE`; runner `SOURCE_NOT_SOLVED` |
| A2.2 | Y0, `case:cold-pressure` `region:closed` `{"value":-2,"unit":"MPa"}` | both entries, both modes | as A2.1, refs `["case:cold-pressure","region:closed","pressure"]`, producer `load-reference-1` |
| A2.3 | X0 with `{"value":-5e-324,"unit":"Pa"}` (smallest negative subnormal) | PP | refused, A2.1's code |
| A2.4 | X0 with `{"value":-0.0,"unit":"kPa"}` | both entries, both modes, base and candidate | admitted, `MECHANICS_SOLVED`; candidate bytes equal base bytes; the three readers accept the envelope (`p_pa` is `-0.0`) |
| A2.5 | X0 with `{"value":0.0,"unit":"kPa"}` | as A2.4 | admitted; bytes equal base |
| A2.6 | Unit level, `PRT` tests: `assemble` with p = −3 | crate test | `PRESSURE_REGION_PRESSURE_NEGATIVE` (replaces the signed half of `PRT:1289-1302`, below) |

**Tests that change (F; derived, not executed):**
- **`PRT:1289-1302`** (`signed_pressure_and_zero_poisson_limit_do_not_include_thermal_load`) uses p = −3.
  - Keep the zero-Poisson and thermal-exclusion assertions with p = +3. Then `cap_loads[0]` is −3π (from `−pAi`, Ai = π).
  - Move the signed case to A2.6.
- **`PP/tests/pressure_grouping_limits.rs:97-122`** gets its cancellation from a second region at p₂ = −2e6·(25/36)·(1+1e-13). Under T4-U0 it would be refused early by A2's code, so the cancellation guard `PRESSURE_ASSEMBLY_CANCELLATION_UNRESOLVED` would lose its only public test.
  - **Re-derivation with p ≥ 0.** Region 2 (the parallel pipe, OD 0.16 m, t 0.02 m, Ai₂ = π·0.0036) gets both terminals `separately_supported_or_compensated`, and p₂ = 2e6·(25/36)·((1−2ν)/(2ν))·(1+1e-13) with ν = 0.3.
  - At node B (and mirrored at A), region 1's groups are cap +p₁Ai₁ and Poisson −2νp₁Ai₁. Region 2's only group is Poisson −2νp₂Ai₂ (no cap at a separately supported terminal; T4-I1 §1.2).
  - The sum is p₁Ai₁(1−2ν) − 2νp₂Ai₂ ≈ 1e-13 relative, so the screen ratio is about 1e13, far above the 1.4e5 that `32ε·ratio > 1e-9` needs.
  - Assert the same code in both modes.

**SP-1 byte evidence (T3's U3 form, CHANGE_RECORD §7 at `98733368f9`).**
- A probe-only harness hashes every output of every exact document, base main (T3's U3 merged) against the candidate, in both modes: PP's envelope, the runner's mechanics envelope, the export document and the unavailability. The set is T3's E (48 exact documents and 96 rows at T3's U3; re-enumerate it at the base).
- **Pass:** every row is byte-equal, and the count of `-0.0` tokens per row is unchanged (T3's H-1 check).
- **Also equal:** the pressure-free set F and B1.
- **Declared differences:** only documents with p < 0 (none committed, A2 facts) and the two re-derived tests above.
- **I:** A3's two changes are unreachable through the public entry before T4-U2a (A3), so they add no byte difference.

## A3. The `.expect` and the straight-statics maximum on non-straight members

**Facts.**
- **F:** `exact_mechanical_local_forces` is set only in the straight branch (`PPL:5027`). The macro branch (`PPL:4958-4982`) leaves it `None`.
- **F:** for a region member, `append_exact_pressure_results` is then reached through `.expect("exact region member retains mechanical/thermal recovery")` (`PPL:5481-5497`; the expect is at `:5494`).
- **F:** the exact maximum branch calls `exact_straight_summary_extrema` for every exact member (`PPL:5399-5452`). The non-exact branch is guarded by `macro_bend.is_none()` (`PPL:5359`).
- **F:** neither site is reachable through the public entry today. `validate_profile` refuses every component in an exact model (A1.1/A1.2), and `build_pressure_case_with_members` re-runs it (`PRT:434-437`). Both sites become reachable when T4-U2a lifts the component refusal.

**Required behaviour.**
- **`.expect` → named refusal.**
  - A region member without straight mechanical recovery (a realized curved bend) gives the blocking `EXACT_PRESSURE_REGION_MEMBER_NOT_STRAIGHT`, refs `[case.id, region id, pipe id]`. The region id is in `ExactPressurePipeState::region_id`.
  - Message: "a curved (realized) bend member in an exact pressure region has no straight-member pressure recovery under 2.0.0/exact_straight_pressure_v2; it is refused, not recovered on its chord".
  - No pressure rows are published for that member. The case is blocked.
- **Maximum on a non-straight member → withheld.**
  - For a macro (arc) member on the exact route, `exact_straight_summary_extrema` is not called.
  - The member is pushed to `unavailable_stress_maximum_members` with the existing warning `EXACT_STRESS_GOVERNING_MAXIMUM_UNAVAILABLE`. The message ends ": the straight-statics bound does not apply to a curved (arc) member".
  - **Observable:** no `pipe_elastic_normal_stress_maximum_v2` row for that member; `stress_maximum_coverage = {"complete": false, "unavailable_pipe_ids": [pipe]}`; the case's governing stress (`max_stress`) withheld (`PPL:5560-5562`).
  - This is the plan's "until T4-U4 the case headline is withheld for cases with bends".

**How a test reaches each before T4-U2a (unit level, in PP's crate tests):**
- **Option 1 (recommended).** Factor the two decisions into crate-private pure functions. For example:
  - `exact_member_recovery(kind, pressure_state: Option<&ExactPressurePipeState>, mechanical: Option<&[f64]>) -> Result<…, Diagnostic>`;
  - `exact_member_maximum_policy(is_arc: bool) -> Compute | Withhold(reason)`.

  Then call them in `#[cfg(test)]` tests with a curved member, an `ExactPressurePipeState` literal and `mechanical = None`. Assert the named code with the stated refs, and `Withhold`. T4-U2 replaces both sites with arc recovery anyway.
- **Option 2.** A crate test that builds a 0.3.0 exact model with A1.2's bend inside `region:fixture-pressure`. It calls `build_model_for_members` (which does not run `validate_profile`), constructs the `ExactPressureCase` for the bend pipe directly, and drives the per-member recovery. It asserts no panic, the named code, and no maximum row.
- **In both options, the precondition shows the hazard:** with the fix reverted, Option 2 panics at `PPL:5494`, and Option 1's mechanical `None` would have reached the `.expect`.
- **Public-entry control (now):** A1.2 is refused by `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED` in both entries and both modes, with no panic. It stays green until T4-U2a, which then owns the end-to-end form.

## A4. Not covered here

- Removing the stale comments on the deleted radial treatment (plan §3.1) changes no behaviour and needs no test.
- Native (Tauri) entry: not needed for U0. The refusals are PP diagnostics carried unchanged.
