# T4-I1 RETURN: the exact pressure contract and its extension surface

TASK T4-I1 (Type 2, research only), for T4's HELPS_HUMANS. Brief: `R4/BRIEFS/T4-I1_EXACT_PRESSURE_SURFACE.md`. Nothing was built or run, and no tracked file was changed.

**Citations** are `path:line@commit`, with four aliases:
- `@u3` = `70e7f49ced`, U3's head. It is the basis for every file U3 touched.
- `@m` = `ec5d397359`, main. It is used for files U3 did not touch; those are byte-identical at `@u3` unless noted.
- `@num` = `db763ed75c`, T3's NUM branch. It is used for ROOT's rulings of 2026-10-08/09.
- `@pre` = `7eae707bb7`, U3's merge base. It is used for retired prior art.

`P`, `PP`, `FK` and `I` are as defined in the brief, and `RE` = `P/core/reporting/result_export`. **F** marks a fact read from the cited bytes; **I** marks an inference.

U3 branches from `@pre`, not `@m`. Main's PR-N `hypot`→`norm3` edits in `pressure_runtime.rs`, `preview_physics.rs`, `lib.rs` and `case_state/resolve.rs` are absent at `@u3`. Line numbers can therefore differ by a few lines between `@u3` and `@m`, but no finding depends on that difference.

## 0. Findings most likely to change T4's plan

1. **Lifting the component refusal alone is unsafe** (§5.2). Suppose a bend pipe joins a pressure region. It passes traversal and gets straight chord loads. Its recovery then hits an `.expect` that panics (`PP/src/lib.rs:5483-5492@u3`). Even a bend outside every region would publish a straight-statics "maximum" on its chord: the exact branch has no bend guard (`lib.rs:5397-5398@u3`).
2. **Every reader has a straight premise hard-coded:** the Rust, Python and TypeScript readers and the physics-1 table (§3.2). Examples: pressure moments in the right-hand side must be zero, only two RHS term kinds are accepted, the `long_straight_annulus_small_strain_v2` text is required, and so is `"Straight circular members … only"`. So pressure on a bend is a contract change. Extending `2.0.0/exact_straight_pressure_v2` in place, versus taking a new (version, mode) or the reserved `…/pressure-1` successor, is the first decision.
3. **The producer and its readers disagree on signed pressure.** The producer admits negative internal pressure; all three readers refuse `p_pa < 0` (§2). I (not executed): a negative-pressure case would publish an envelope its own readers reject.
4. **Pressure is per load case.** In 0.4.0 that means per resolved state, and pressure is not factored by `load_sources`. Combinations are refused, so "pressure combined with load states" does not yet exist across cases. Hydrotest can only be authored as a pressure region; the `hydrotest` primitive is refused on every route (§4).
5. **A simpler bend formulation may exist** (I, §5.4). For a tangent-continuous region whose closures transfer to the wall, today's loads are equivalent member by member to a uniform axial eigenstrain `ε_p = (1−2ν)pAi/(E·As)`, with recovery `N_w = N_el + pAi`. That would let a bend reuse the existing thermal free-expansion identity. It needs an independent derivation before anyone relies on it.
6. **Premises that could invalidate later work** (§5.5):
   - the hoop stress on a torus is not the straight Lamé value;
   - the curved element is not rotation-consistent in binary64 and not objective at large coordinates;
   - the arc centre is rounded, so tangency with the neighbouring straights is only approximate;
   - the flexibility factor is per component, while pressure is per case;
   - one effective-wall section basis serves stiffness, pressure, stress and mass (M30).
7. **No test names three refusal codes:** `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED`, `EXACT_PRESSURE_COMBINATION_UNSUPPORTED` and `OBJECTIVE_CONNECTOR_NOT_IMPLEMENTED` (§2). Pin the refusal surface before widening it.
8. **The desktop cannot author a curved-bend macro element through operations** (M02). Retained precision covers no pressure at all, and T3's planned B3b admits only empty regions with no curved members (§3).

## 1. What the contract computes

### 1.1 Authored input and where it is validated (F)

| Input | Declared | Validated |
|---|---|---|
| `pressure_contract {version:"2.0.0", mode:"exact_straight_pressure_v2"}` on model 0.3.0 or 0.4.0 | `PP/src/pressure_runtime.rs:18-24,28-33,80-86@u3` | `validate_profile` `:114-153`, called from `PP/src/lib.rs:2363@u3` and again at `pressure_runtime.rs:437` |
| Case `pressure_regions`: `id`, `member_pipe_ids`, `pressure_basis = internal_differential_zero_external_v1`, `pressure` (finite, signed), exactly two `terminals {node_ref, closure_transfer ∈ {transfers_to_wall, separately_supported_or_compensated}, provenance}` and `provenance`. An explicit `[]` is required for an unpressurized case. | `lib.rs:560-561@u3`; `pressure_runtime.rs:35-53` | Inputs `:243-357`. Units are converted to Pa at `:373-405`, via `lib.rs:8150@u3`. Topology and geometry are checked per case in `traverse_region` `:946-1117`. |
| Material `constitutive_basis = homogeneous_isotropic_E_nu_v1`, `E`, `ν` (unit `1`), with G derived. An authored G produces the warning `EXACT_PRESSURE_REDUNDANT_G_IGNORED`. Optional temperature points are selected per case by `modulus_basis_ref` or by interpolation (E and ν are interpolated linearly, then G is derived). | `lib.rs:704-745@u3`; `PP/src/pressure_material.rs:19-94,101-259@m` | `resolve_base` at `lib.rs:2408@u3` (0.3.0 only); `resolve_case` via `lib.rs:9738-9739@u3`; per region at `pressure_runtime.rs:542-592@u3` |
| Section: `outside_diameter`, `wall_thickness`, optional `mill_tolerance` (an absolute thickness reduction) | `lib.rs:319-341@u3` | `derive_pipe_section` `lib.rs:10192-10230@u3` gives the effective wall `t − mill`; then `SourceAnnulus::from_od_wall(OD, t_eff)` (`lib.rs:7242-7258@u3`; `PP/src/pressure_exact/source_geometry.rs:28-64@m`) |
| Corrosion allowance | absent from PP's DTO; it exists only in `P/core/section_properties/calculator.py:45@m` | — |

**One section basis serves everything (F).** The effective wall sets:
- the stiffness properties A, I, J and Z (`lib.rs:7252-7257@u3`);
- the pressure areas Ai and As, and the Lamé surface values;
- the self-weight metal and bore areas (`PP/src/self_weight.rs:460-477@m`).

The outside diameter is kept, so mill tolerance thins the wall from the inside and enlarges Ai.

### 1.2 What enters the solve (F)

- **Two pressure effects only:**
  - the Poisson axial eigenload `[2νpAi, −2νpAi]` along each member's chord (`PP/src/pressure_exact.rs:388-406@m`; thermal 0 at `pressure_runtime.rs:607@u3`);
  - the closed-end cap pair `[−pAi, +pAi]` (`pressure_exact.rs:411-420@m`).
- **Caps apply only at the region's two terminals,** and only where `transfers_to_wall` (`pressure_runtime.rs:668-695@u3`). A `separately_supported_or_compensated` terminal leaves the cap out of the pipe solve and reports a remote reaction of −cap in evidence.
- **Form:** nodal translational forces Fx, Fy and Fz only. No element load vector, initial-strain field or moment entry is used. They are pushed as operands into the case's exact force ledger (`lib.rs:3842-3877,3895-3920@u3`), next to the nodal, uniform, thermal and constant-effort producers.
- **Arithmetic:**
  - Terms are grouped by (DOF, the bits of p, the exact source-bore two-sum key of OD/2 − t, |direction component|). The coefficients are ±2ν for `poisson_eigen` and ∓1 for `terminal_cap` (`pressure_runtime.rs:697-735,788-836@u3`).
  - Each group's coefficient sum is one correctly rounded exact sum (`PP/src/pressure_sum.rs:16-22@m` → FK `exact_sum`). The value p·Ai·c·d is formed in extended-exponent `Scaled` arithmetic and rounded once (`source_geometry.rs:116-134@m`).
  - Poisson terms at interior nodes cancel exactly.
  - A cancellation screen of 32ε·ratio ≤ 1e-9 applies; otherwise the solve stops with `PRESSURE_ASSEMBLY_CANCELLATION_UNRESOLVED` (`pressure_runtime.rs:897-927@u3`).
  - Each ledger operand carries the formation bound γ₂₀ (`lib.rs:3922-3929@u3`).
- **Not modelled:**
  - external pressure, hydrostatic head and non-uniform pressure within a region;
  - pressure on bends, joints and components;
  - pressure stiffening, Bourdon rotation, ovalization and radial wall displacement.

  Sources: the profile limitations at `lib.rs:1039-1052@u3`, and the code.

### 1.3 Recovery and published outputs (F)

- **Recovery formulas:**
  - wall force N_w = N_mech + 2νpAi;
  - effective force S = N_mech + (2ν−1)pAi;
  - membrane stress N_w/As.

  These are computed in `source_geometry.rs:135-165@m`. N_mech is the mechanical/thermal force from `exact_straight_end_forces` (`lib.rs:10827-10859@u3`). The formulas are applied to the end rows (`lib.rs:5021-5050@u3`) and per station (`lib.rs:11519-11552@u3`).
- **Lamé values are published at the surfaces only** (`source_geometry.rs:166-186@m`):
  - inner radial stress −p, outer 0;
  - hoop stress 2pAi/As + p inside, 2pAi/As outside.

  The interior-radius `lame_at_radius` and `axial_state` functions are unused in production (`pressure_exact` is `#[allow(dead_code)]`, `lib.rs:107-108@u3`).
- **Rows** for each region member and case, at `end_i`, `end_j`, `quarter_1`, `midspan` and `quarter_3` (`lib.rs:11436-11568@u3`):
  - `pipe_wall_endpoint_action_v2` (end locations only);
  - `pipe_wall_axial_force_v2`;
  - `pipe_effective_axial_force_v2`;
  - `pipe_axial_membrane_stress_v2`;
  - `pipe_lame_radial_stress_v2` and `pipe_lame_hoop_stress_v2`, each with an inner and an outer component.

  IDs have the form `result:pressure-exact:{len}:{case}:{len}:{pipe}:{location}:{component}` (`:11474`). The member's `element_local_axial_force` and `element_local_axial_normal_stress` rows are removed (`:11460-11469`).
- **Every exact-route member also gets:**
  - `pipe_elastic_normal_stress_maximum_v2` = |N_w/As| + hypot(My, Mz)/Z, bounded over straight statics intervals (`lib.rs:10338-10421,5397-5450@u3`);
  - the signed support rows (`:11398-11430`).

  If any member's maximum is unavailable, the case's headline is withheld (`:5558-5560`).
- **Evidence:** `contract_evidence = {pressure:[regions], connector:[], exact_cases:[…, pipe_sections, pipe_materials, pipe_stress_extrema, stress_maximum_coverage, pressure_rhs_assembly]}` (`pressure_runtime.rs:743-749,928-935`; `lib.rs:5533-5590@u3`). The producer contract is `physics-1` (`lib.rs:989-997@u3`).
- **`membrane_publication_range.rs` is test code:** a `#[cfg(test)]` regression module (`lib.rs:105-107@u3`), not production.

## 2. Every refusal

Sites are `PP/src/pressure_runtime.rs@u3` unless noted.

| Code (site) | Trigger | Narrowest admitting change (I) |
|---|---|---|
| `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED` (`:174-177`) | Any component, including a metadata-only fitting | Admit only `is_curved_bend_macro_component` (`lib.rs:7602-7606@u3`), and only together with §5.3. Joints, tees, reducers and valves stay refused. |
| same (`:178-183`) | A nonlinear or constant-effort support | The constant-effort load already enters the shared ledger (`lib.rs:3871-3875@u3`), and the nonlinear loop uses the same ledger. What remains is the readers' linear-only support attribution and the evidence. This belongs to T5. |
| same (`:229-235`) | `equivalent_static` on an exact case | The generators emit uniform element loads that exact recovery already consumes, so the remaining work is evidence, readers and validation. This is possibly cheap. |
| `EXACT_PRESSURE_COMBINATION_UNSUPPORTED` (`:204-207`) | Any combination | The v2 rows are linear in p, but the maxima must be recomputed per combination and region evidence carried. This belongs to T6, and also interacts with B3b's ruling 4 (`ROOT_RULINGS_V1.md:14723@num`). |
| `EXACT_PRESSURE_REQUIRES_REGION` (`:236-242`) | Any pressure-category or pressure-dimension primitive, zero included | By design: regions are the only pressure selector. Keep. |
| `PRESSURE_MODEL_REAUTHOR_REQUIRED` (`:139-142`, `:210-224`) | The retired `1.0.0/legacy_pressure_v1` label, or any pressure primitive in a non-exact document | The owner's retirement. Keep. |
| `PRESSURE_CONTRACT_REQUIRED` / `_UNSUPPORTED`, `PREVIEW_CONTRACT_VERSION_MISMATCH`, `PREVIEW_SCHEMA_VERSION_UNSUPPORTED` (`:115-153,211-215`) | Version dispatch | Keep. A bend profile that changes the contract's meaning would add a new (version, mode) arm here. |
| `EXACT_PRESSURE_REGIONS_REQUIRED` (`:243-247,441-447`) | An exact case without `pressure_regions` | Keep. |
| `PRESSURE_REGION_INPUT_MISSING`, `_ID_DUPLICATE`, `_BASIS_UNSUPPORTED`, `_MEMBERS_INVALID`, `_PIPE_OVERLAP`, `PRESSURE_TERMINAL_INPUT_MISSING`, `_CLOSURE_INVALID`, `PRESSURE_TERMINALS_INVALID` (`:248-357,732-739`) | Region inputs | Keep. External pressure would need a new `pressure_basis`. |
| `PRESSURE_TERMINAL_NODE_UNKNOWN`, `PRESSURE_REGION_MEMBER_UNKNOWN`, `_TOPOLOGY_INVALID`, `_INTERNAL_BRANCH`, `_GEOMETRY_INVALID`, `_NONCOLLINEAR` (64ε guard) (`:946-1117`) | Region topology and geometry | `_NONCOLLINEAR` (`:1080-1115`) is the one a bend must change, to a tangent-continuous chain. `_INTERNAL_BRANCH` is the tee refusal (T7). |
| `PRESSURE_REGION_BORE_MISMATCH` (`:529-538`) | Unequal inner radius within 64ε | Reducers need the cap difference at the junction (T7). |
| `EXACT_PRESSURE_MATERIAL_AMBIGUOUS` / `_MISSING` / `_BASIS_REQUIRED` / `_POISSON_RATIO_REQUIRED` / `_INVALID`, `LOAD_STATE_MEMBER_MATERIAL_MISSING`, `THERMAL_EXPANSION_INPUT_MISSING`, `MODULUS_BASIS_*` (`:461-605`; `pressure_material.rs:25-58,120-233@m`) | Missing or invalid E/ν, or ambiguous material selection | By design: the Poisson term needs ν. Keep. |
| `EXACT_SECTION_GEOMETRY_UNREPRESENTABLE` (`lib.rs:7246-7251@u3`), `PRESSURE_REGION_NOT_NORMALIZED` / `_PRESSURE_INVALID`, `EXACT_PRESSURE_OUTPUT_UNREPRESENTABLE`, `PRESSURE_LEDGER_SUM_UNREPRESENTABLE`, `PRESSURE_ASSEMBLY_*`, `EXACT_PRESSURE_RECOVERY_FAILED` (`lib.rs:5043-5049,11448-11456,11526-11550@u3`), `EXACT_STRESS_GOVERNING_MAXIMUM_UNAVAILABLE` (a warning that withholds the headline) | Representability | Keep. |
| `EXACT_PRESSURE_RESULT_ID_COLLISION` (`:185-203,359-371`) | ID suffix collision | Keep. |
| `OBJECTIVE_CONNECTOR_*` (`:157-168`, every version) | `objective_connector` | T7 and M07. |
| `JOINT_ELEMENT_STIFFNESS_INCOMPLETE` / `_MAPPING_UNRESOLVED` / `_EQUILIBRIUM_UNQUALIFIED` (`PP/src/preview_physics.rs:113-215@u3`, every route) | User-stiffness joints | M07; see T4-I3. |
| `HYDROTEST_PRESSURE_UNSUPPORTED` (`PP/src/validation.rs:30-39@u3`) | A `hydrotest`/`pressure` primitive on any route | T2 (§4). |
| `LOAD_STATE_MASS_STATE_UNSUPPORTED` (`PP/src/case_state/resolve.rs:271@m`) | `mass_state_ref` | T2. |
| Retained-source "unsupported" (`PP/src/source_recovery.rs:578-599@u3`) | An exact case with non-empty regions, or any curved, component or user-matrix element | Keep until T3's W1c and F2b. |
| W1 D1.3 (`PP/src/retained_memory.rs:727-732@m`); exact and 0.4.0 models fall back to ordinary (`lib.rs:2961-2963@u3`) | Any `pressure_contract` | T3's B3b (§3.3). |

**Untested refusals (F).** A git grep of P at `@u3`, excluding `execution/`, finds `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED`, `EXACT_PRESSURE_COMBINATION_UNSUPPORTED` and `OBJECTIVE_CONNECTOR_NOT_IMPLEMENTED` only at their emitting lines. No test names these refusals.

**Signed pressure.**
- **F:** the producer accepts a finite signed pressure (`:280-292`; `pressure_exact.rs:274-279@m`). Its own assembly test uses p = −3 (`:1292-1306`), and it publishes the signed `p_pa` (`:745`).
- **F:** every reader requires `p_pa >= 0`: `RE/src/physics_evidence.rs:627@m`, `P/core/analysis_runs/physics_evidence.py:158@m` and `P/apps/desktop/src/features/results/physicsResultEvidence.ts:138@m`.
- **I (not executed):** a negative-differential case publishes physics-1 that all three readers refuse.

## 3. Routes and readers

### 3.1 Routes (F)

- **Ordinary exact route** (0.3.0 → `physics-1`, profile `exact_straight_pressure_v2`; `lib.rs:989-997,1039-1052@u3`). Straight members and linear supports only.
- **`physics-source-1` (composite).** Only explicitly empty regions are admitted, with no curved or component elements (`source_recovery.rs:578-599@u3`). A pressurized case is therefore always ordinary. A rejected pressurized case blocks the whole invocation (T3's F-P2: `I/NUMERICAL_INTEGRITY_T3/DESIGN_STANDING/DESIGN.md:1170-1176@m`).
- **`load-reference-1` and `-source-1` (0.4.0).**
  - These require the exact contract (`pressure_runtime.rs:122-129@u3`).
  - They use the same builder, with each member's resolved E/ν pair (`:542-551`).
  - The reader projects to physics-1 and reuses `validate_physics_evidence` (`RE/src/load_reference.rs:365@m`).
- **`preview-physics-1` (0.1.0/0.2.0).**
  - Every pressure primitive is refused, and the render step is skipped on the exact route (`lib.rs:2685@u3`).
  - The text "Nonzero pressure is refused on this route" (`preview_physics.rs:75@u3`) is kept until the next corpus generation (`ROOT_RULINGS_V1.md:16518@num`).
- **Retained precision W1.**
  - It refuses any contract today.
  - Planned B3b admits the exact route only with `pressure_regions == []`, base E/ν, and no combinations, components or curved members (`I/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/I96/b3_d_01/DESIGN.md:15,24,41,75-77,274-276@m`).
  - Its P-4 rule says W1 never calls the pressure builders (`:45,327`).
- **Headless runner.** It passes the request to PP unchanged; its tests pair the exact fixture with physics-1 (`P/core/runner/headless/src/lib.rs:1497-1511,1544-1560@u3`).
- **Desktop.**
  - The Tauri `run_preview_mechanics*` commands call `run_linear_static_preview_value_with_mode` with `materials: []` (`P/apps/desktop/src-tauri/src/lib.rs:1557-1584@u3`). That shared entry never selects the retained profile (`PP/src/lib.rs:2132-2141@u3`).
  - Pressure is authored in `PressureAuthoringPanel`: the profile, E/ν and per-case regions (`.../pressure-authoring/PressureAuthoringPanel.tsx:5,93-146@u3`), through the applier's `pressure_profile` and `pressure_regions` fields (`P/core/model_operations/operation_applier/src/lib.rs:1212-1213@u3`).

### 3.2 Readers (F)

The Rust (`RE/src/physics_evidence.rs@m`), Python (`P/core/analysis_runs/physics_evidence.py@m`) and TypeScript (`.../results/physicsResultEvidence.ts@m`) readers all pin:
- **Profile and approximation:** profile `exact_straight_pressure_v2` (rs `:7`; `RE/src/semantic_contract.rs:403@m`), and region `approximation == long_straight_annulus_small_strain_v2` (rs `:620-625`, py `:159`, ts `:139`).
- **Right-hand-side shape:**
  - zero moment entries (`RHS_PRESSURE_MOMENT`: rs `:888-896`, ts `:267`);
  - groups limited to Fx, Fy and Fz (rs `:918-921`);
  - term kinds only `poisson_eigen` with |c| = 2ν and `terminal_cap` with |c| = 1 (rs `:984-995`; py `:247,303`; ts `:284-286`).
- **Fixed sign-convention strings:**
  - the hoop row says "…for long straight annulus…" (rs `:296`, ts `:69`);
  - the extremum's `approximation` must be `piecewise_quadratic_straight_section_statics` (rs `:508`).
- **Station names:** the five straight station names (rs `:32`).
- **Pressure sign:** `p_pa >= 0`.

**The physics-1 table** (`P/fixtures/results/semantic_contract_v0_3_physics_1.json@m`):
- 57 kinds, including the six pressure v2 kinds and `curved_bend_macro_element_review`;
- the limitation "Straight circular members and linear restraints or springs only." (`:1242`);
- reserved successors `…/pressure-1` and `…/stress-1` (`:1231-1237`).

**Desktop path:**
- The Results panel lists rows by kind family, using the pinned table (`resultSemantics.ts:4@m`).
- It prints `formulation_basis.limitations` (`ResultsPanel.tsx:107@m`).
- `validatePhysicsEvidence` gates numerical standing, export and run records (`numericalResultQuality.ts:167`; `resultExportAdapter.ts:64,137`; `analysisRunCompatibility.ts:99@m`).

**I:** new kinds and limitation text reach users through this path with no bespoke view. A new semantic contract id would need dispatch in each of these places.

### 3.3 What T3 expects from T4

**F (records):**
- **The curved element:**
  - W1c on curved elements waits for T4;
  - T4 must confirm that the curved construction keeps the rigid-motion null space;
  - T4 must repair the element's binary64 rotation-consistency and objectivity (`P/execution/_Coordination/WorkGraphs/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/WORK_GRAPH.md:36@m`; `ROOT_RULINGS_V1.md:344@num`).
- **D2's coverage rules:**
  - The Lamé rows are `input_derived`.
  - The membrane stress and the maximum are `not_covered` where a member carries pressure, because the membrane is "rebuilt from the span-statics axial force…, not taken from a published, stop-rule-checked wall-force row" (`DESIGN_STANDING/DESIGN.md:589,700-706@m`).
  - Reaction zero-proofs exclude the DOFs of pressure-region families (R5-1, `:25`).
- **F2b runs per family**, only after S-I1/S-I2 and the gate's row- and check-level conditions (`:838-839`), and after T3-B8 (`WORK_GRAPH.md:586@m`).
- **"Element by element" is the T4 brief's phrase** (`PRESSURE_STRESS_T4/BRIEFS/HELPS_HUMANS_T4_PLAN.md:26@a0c5f6e6d4`); I found no T3 record that uses it for pressure.

**I:** for each family T4 admits under pressure, T3 will need:
1. a published wall-force basis that W1 can certify, so that the carve-out can lift;
2. a pressure assembly that W1 can call (P-4 forbids this today);
3. for bends, the objective formation first.

## 4. Load states (T1) and hydrotest (M21)

**F:**
- **Ownership.**
  - Regions belong to `PreviewLoadCase` (`lib.rs:560-561@u3`), with identity (case, region) (`pressure_runtime.rs:247-249`).
  - In 0.4.0 each case has exactly one `analysis_state`, so pressure is per resolved state.
  - Pressure is not a factored load source. The resolver records `pressure_region:<id>` with `factor: null` and class `pressure_eigen_and_closure` (`case_state/resolve.rs:1079-1082@m`); factors apply only to stored primitives (`:1064-1077`).
- **Materials and thermal strain in 0.4.0.**
  - Pressure uses each member's resolved E/ν pair (`pressure_runtime.rs:542-551@u3`).
  - Thermal strain is owned by the resolved eigenstrain, not by primitives (`:594-599`).
  - The same rows publish under load-reference-1.
- **Combinations** are refused on both routes (`:204-207`).
- **Hydrotest:**
  - the `hydrotest`/`pressure` primitive is refused (`validation.rs:30-39@u3`), and on the exact route `EXACT_PRESSURE_REQUIRES_REGION` refuses it as well;
  - a per-case mass state is refused (`case_state/input.rs:260-262@m`; `resolve.rs:271@m`);
  - the limitation texts state that there is no hydrostatic head, no contents-weight state and no locked or inactive support (`lib.rs:1019-1020,1046@u3`).

**I:**
- T2's test pressure can only be authored as a pressure region in an exact or 0.4.0 case.
- Realistic hydrotest layouts contain bends, so T2 depends on T4's bend coverage.

## 5. The first path: pressure on one curved bend

### 5.1 Today's bend (F)

- **Authoring shape.** A bend is a pipe segment (the chord) plus a `bend` component with:
  - `geometry.bend_pipe_ref`, `bend_radius` and an optional `bend_angle`;
  - `modifiers.flexibility_factor_user_value`;
  - `mechanics_interface.solver_consumption = curved_bend_macro_element`.

  Sources: `lib.rs:359-477,7602-7606,7628-7870@u3`.
- **Geometry and members.**
  - The arc centre is built in binary64 from the chord, `y_reference` and R (`:7764-7846`).
  - The chord stays in `built.pipes`, with its stiffness skipped (`:7324`), so regions can name the bend by pipe id.
- **Element and loads.**
  - The macro element is a Castigliano 12×12 with one user factor k (`P/core/solver/curved_bend/src/lib.rs:84-150@u3`).
  - Thermal load on a bend is K_macro·u_free, a rotation-free scaling about node i (`lib.rs:10766-10821@u3`).
- **Recovery.**
  - End forces are K(d − u_free) minus the uniform equivalents, rotated to the chord frame (`:10877-10999`).
  - Station values come from arc equilibrium in the tangent frame (`:11013-11092`; `curved_bend/src/lib.rs:476`).
- **Material.** The bend reads `material.elastic_modulus` and `shear_modulus` (`lib.rs:7849-7861@u3`), not 0.4.0's per-member pair; the 0.4.0 fit uses the chord length (`case_state/resolve.rs:899@m`).
- **Retired prior art.** U3 deleted the radial pressure path and its hand calculation (commit `9930cfe6db`):
  - code: `consistent_radial_pressure_nodal_loads`, `arc_section_resultants_with_radial_pressure` and `tip_deflection_under_radial_pressure` (`curved_bend/src/lib.rs:490,569,663@pre`);
  - hand calculation: `P/validation/hand_calcs/mechanics/curved_bend_pressure_thrust_arc.md@pre`, with the cap/wall decomposition (§1-3), why a consistent vector is required (§4) and the membrane-state station identity (§6).
- **Stale comments still describe the deleted treatment** (`lib.rs:10864-10876,10902,11003-11012,11047@u3`).
- **Who rebuilds it.** Rebuilding the validation is T4's job (`ROOT_RULINGS_V1.md:16498@num`). The prior design says curved composition "must independently reconcile existing radial wall loads and cap transfer with wall/effective-force recovery" (`I/CORRECTNESS_DESIGN/PRESSURE_INTEGRATION.md:25@m`).

### 5.2 If only the component refusal were lifted

**F, read from the code:**
- A bend pipe in a region passes traversal. A one-member region passes `_NONCOLLINEAR` trivially.
- It then gets eigen and cap pairs along its chord (`pressure_runtime.rs:607-638@u3`).
- Its recovery takes the macro branch (`lib.rs:4956-4977@u3`), so `exact_mechanical_local_forces` stays `None`; it is set only at `:5025`.
- `append_exact_pressure_results` is then reached through `.expect("exact region member retains mechanical/thermal recovery")` (`:5483-5492`).
- `exact_straight_summary_extrema` runs for every exact member with no bend guard (`:5397-5398`), unlike the non-exact path (`:5357`).

**I (not executed):** the solve panics for a bend in a region, and a bend outside any region publishes a wrong, straight-labelled maximum.

### 5.3 Touch points for pressure on a single curved bend (I, from the code)

| # | Where (`@u3` unless noted) | Change |
|---|---|---|
| 1 | Contract identity: `pressure_runtime.rs:18-24,80-86,114-153`; `lib.rs:1039-1052`; the readers' pinned strings (§3.2); the physics-1 table | Decide whether to extend in place or create a new (version, mode, profile), possibly using the reserved `pressure-1`. Every pin in §3.2 follows from this choice. |
| 2 | Authoring: `componentIntent.ts:3@m` (bend creation sets no `solver_consumption`); no file under `P/core/model_operations` mentions `mechanics_interface` (F, grep); `PressureAuthoringPanel.tsx:93,127` ("straightness" text) | Add an operation path for the macro bend (M02) and a region member picker that accepts a bend. Today a macro bend can be authored only by editing the document. |
| 3 | `pressure_runtime.rs:174-177` | Admit `is_curved_bend_macro_component` only. |
| 4 | `traverse_region` `:1080-1115` | Replace collinearity with a tangent-continuous chain, using `end_tangents` (`curved_bend/src/lib.rs:457`). Refuse a mitre (kink) by name. |
| 5 | Member state, caps, terms and groups: `:520-660`, `:668-695`, `:697-735`, `:838-935` | A cap at a bend terminal acts along the arc end tangent. A bend's Poisson and wall-load contributions are K_macro-based terms that include moments, which needs a new term family and RHS method. |
| 6 | Ledger: `lib.rs:3869-3870,3895-3929` | Formation bounds for K_rc·fl(ε·chord_c) products, as the thermal path already does (`:10773-10802`). |
| 7 | Bend recovery: `lib.rs:4956-4977,10877-10999` | Subtract the pressure free field (§5.4) and remove the `.expect` hazard at `:5492`. |
| 8 | `append_exact_pressure_results` `lib.rs:11436-11568` (straight statics at `:11524`) | Use `curved_bend_section_resultants` (`:11013`) for stations. Publish the bend's end wall action in the tangent frame: the chord-frame end rows are not wall actions on an arc. |
| 9 | Hoop and radial rows: `source_geometry.rs:166-186@m`; `lib.rs:11555-11566` | Publish a new kind or basis for the toroidal hoop, or withhold hoop on bends (P2). |
| 10 | Maximum and headline: `lib.rs:5397-5450,10338-10421` | Build an arc maximum, or withhold it; withholding blanks the case headline (`:5558-5560`). |
| 11 | Evidence: `pressure_runtime.rs:743-749` (`approximation`, `local_x_global`); `lib.rs:5561-5590` | Record per bend: R, Φ, the centre, the end tangents and k. |
| 12 | 0.4.0: `lib.rs:7849-7861`; `case_state/resolve.rs:899@m` | Pass the per-member E/ν pair to the macro element, and use the arc length for the fit. |
| 13 | The three readers (§3.2) and their parity tests | Accept moment RHS entries, the new term kinds, the bend approximation, tangent-frame rows and the new basis strings. |
| 14 | Published text: the curved review row's `pressure_thrust_treatment=none_pressure_refused_outside_the_exact_straight_contract` (`lib.rs:12028`); `preview_physics.rs:75-76` | Must change under ROOT's published-text rule (`ROOT_RULINGS_V1.md:16500-16504@num`), with blast radius in the pinned corpora. |
| 15 | Validation | Rebuild `MECH-CURVED-BEND-PRESSURE-THRUST-ARC` under E/ν. Example: an anchored–free quarter bend with closed terminals should give tip translation (1−2ν)pAi/(E·As)·chord, zero tip rotation, wall force pAi along the tangent at every station, and S = 0 (I, §5.4). |
| 16 | Deliberately unchanged: `source_recovery.rs:578-599`; `retained_memory.rs:727-761@m` | A pressurized bend stays on the ordinary route only, until T3's W1c and F2b. |

### 5.4 A candidate formulation (I; derive and review it independently)

Consider a region whose members' tangents are continuous and whose terminals transfer their caps to the wall.

- **Straight members.** The current loads equal, member by member, a uniform axial eigenstrain `ε_p = (1−2ν)pAi/(E·As)`. For a straight member, K·u_free(ε_p) = [−(1−2ν)pAi, +(1−2ν)pAi], which is the cap pair plus the eigen pair; the interior caps cancel.
- **Bend members.**
  - The wall load plus its two virtual caps is self-equilibrated and in a pure membrane state (hand calculation §6@pre).
  - Its free deformation is the rotation-free scaling field, so its consistent vector is K_macro·u_free(pAi/(E·As)).
  - The virtual caps cancel against those of the neighbouring members wherever the tangents agree.
- **Total right-hand side:** Σ_m K_m·u_free(ε_p), minus the cap at each terminal that does not transfer to the wall.
- **Recovery:** N_w = N_el + pAi and S = N_el, where N_el comes from K(d − u_free(ε_p + ε_th)).

This reuses the bend's thermal identity and T1's eigenstrain plumbing. A straight-only region reproduces today's values in exact arithmetic, but not bit-for-bit, because the rounding differs from today's source grouping. The formulation excludes:
- Bourdon-type bend rotation;
- the circumferential variation of hoop and Poisson strain on a torus;
- ovalization;
- a pressure-dependent flexibility factor k.

### 5.5 Premises likely to invalidate later work (I)

- **P1 — the contract's identity.** In-place versus new (version, mode) decides the scope of every reader, table, fixture and corpus re-pin (§3.2).
- **P2 — hoop stress on a bend.** The membrane hoop stress of a toroidal shell varies around the circumference. At the intrados it is about (2R−r)/(2(R−r)) times the straight value, for example 1.25 at R = 3r. `pipe_lame_hoop_stress_v2` ("…long straight annulus") would be false on a bend. This is external engineering knowledge, not taken from code; see T4-I2.
- **P3 — the bend's numerics.** The curved element is not rotation-consistent in binary64 and not objective at UTM-scale coordinates (`WORK_GRAPH.md:36@m`). The exact cancellation and "exact" claims do not carry over to K_macro terms. T4 must decide whether the objective formation (W1c) comes before or after pressure on bends.
- **P4 — tangency.** The arc centre is rounded (`lib.rs:7836-7846@u3`), so a bend is only approximately tangent to its neighbours. The tangency guard must be designed, either as a representation guard or as an engineering tolerance.
- **P5 — a pressure-dependent flexibility factor.** k is per component while pressure is per case, so a pressure-corrected k cannot be expressed per case.
- **P6 — M30.** Splitting the section bases changes every exact number, including the `STRESS-TP-PMM-P3` membrane values that T4 must rebuild.
- **P7 — signed pressure.** See §2.
- **P8 — the headline.** Any bend without an arc maximum withholds the case's stress headline, as preview-physics-1 already does for arcs (`preview_physics.rs:76@u3`).

## 6. Limits of this record

- No build or run was performed.
- The negative-pressure publication and the panic path (§2, §5.2) are read from code, not executed.
- The formulation in §5.4 and the toroidal hoop factor are inferences for T4's design and independent review.
- The validation inventory (T4-I4), curved-element stress (T4-I2) and joint deletion (T4-I3) are not covered here.
