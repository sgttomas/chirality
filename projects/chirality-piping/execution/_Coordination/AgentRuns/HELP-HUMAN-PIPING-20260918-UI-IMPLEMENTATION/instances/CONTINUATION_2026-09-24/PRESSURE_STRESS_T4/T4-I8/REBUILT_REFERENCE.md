# T4-I8: independent references for T4-U2's rebuilt straight cases (freeze, repair round 01)

- **Role:** TASK (Type 2) for T4's WORKING_ITEMS. Brief `R4/BRIEFS/T4-I8_U2_STRAIGHT_REBUILT_REFERENCES.md` (sha256 `1f294de5…a7aa134`); common terms `R4/BRIEFS/T4_WI_COMMON.md` (sha256 `7d44afd0…02cb`); both at `0c17c8d352`.
- **Status:** frozen at `61b4e0b460` and refuted by T4-RV4 (`R4/T4-RV4/REVIEW.md` at `19c54f6f4a`: PASS WITH FINDINGS, nothing blocking). This is repair round 01; `REPAIR_01.md` maps each change to its finding. **No frozen value changed:** all 235 round-00 quantities compare equal by exact form and binary64. Not product evidence.
- **Independence:** every value is a closed form (Lamé, Hooke with the Poisson term, beam statics) in exact rational arithmetic, rational × π^k, or one of two named symbolic sums. The product was read only for conventions (§1) at `ed012c7ccf`. The retired cases were read at `ec5d397359`. No product build, run, test or output was used.
- **Files:**
  - `rebuilt_reference_cases.json`: authoritative values, rows in T1's selector shape, zero scales, discriminators, document sketches, and the SP-1 pair scope;
  - `_run_records/derive_rebuilt_references.py` and its stdout: 177 checks pass;
  - `_run_records/check_reference_json.py` and its stdout: re-evaluates 284 quantities and 956 rows, checks the transport, tags, discriminators and documents, and compares with the frozen file; PASS;
  - `_run_records/t1_generator_probe.py` and its stdout: runs every row through T1's unmodified generator functions. 803 rows are accepted; the 153 refusals are only the declared ones (§8).
- **Reproduce:** from `R4/T4-I8/_run_records/`, run each script with `WT/venv/bin/python -I`:
  - `derive_rebuilt_references.py <SOURCE_ODWALL_EXPECTATIONS.json at ed012c7ccf> ../rebuilt_reference_cases.json`
  - `check_reference_json.py ../rebuilt_reference_cases.json <the file at 61b4e0b460>`
  - `t1_generator_probe.py <load_reference/generate_reference_values.py at ed012c7ccf> ../rebuilt_reference_cases.json`

## 0. Findings for the plan

1. **No stop rule (SP-1 to SP-4) is triggered, and no T3 condition is touched.**
2. **D-6 against SP-1 (from T4-RV4 S-2; a T4-U8 planning point).** H-1 keeps v2 byte-identical, and v2 is Euler–Bernoulli. If D-6 makes Timoshenko the exact-route default, a straight-only v3 document can no longer be bit-equal to its v2 twin. Two ways out:
   - the v3 side of each SP-1 pair selects Euler–Bernoulli explicitly (D-6 keeps that by selection);
   - SP-1's straight-v3 clause is scoped to Euler–Bernoulli selections.

   Case 2's lateral deflections and the twin's tip deflection are marked for re-freeze in T4-U8.
3. **The exact route cannot author a partial-span load (fact).** Partial extents exist only for `equivalent_static` wind (`PP/src/lib.rs:633-651, 10259-10260`), which the exact route refuses. Case 2 therefore represents 009's loaded interval [0.25 L, 0.75 L] exactly, with a three-member chain that carries a uniform load on its middle member. T4-RV4 confirmed this choice is forced and sound.
4. **MILLTOL has no corrosion-allowance input (fact; `PP/src/lib.rs:320-330`).** The allowance is folded into the authored wall (0.01 − 0.002 = 0.008 m), and the mill tolerance (0.00125 m) stays in its own slot. The case is re-frozen in T4-U6 if D-5 changes the basis.
5. **Package generator: two one-line extensions, or omissions.** T1's generator needs:
   - the exact factor Pa → MPa, for the 150 bending and torsional stress rows, which are published in MPa;
   - two symbolic forms, for three rows: `sqrt((a*pi)^2 + (b)^2)` (one support force norm) and `a + (b)/pi` (two elastic maxima).

   Every other row passes T1's functions unchanged.
6. **The ids and the v3 wire are proposals (inference).** The case ids are proposals. The v3 patch `3.0.0/exact_pressure_v3` (H-1) stays provisional until T4-U2a.

## 1. Conventions read from the product (fact, `@ed012c7ccf`)

| Item | Convention | Source |
|---|---|---|
| Section | Effective wall = `wall_thickness − mill_tolerance` (an absent slot means no reduction). ro = OD/2, ri = ro − t. As = πt(OD − t). Ai = π ri² (reduced bore). I = As(ro² + ri²)/4, J = 2I, Z = I/ro | `PP/src/lib.rs:10213-10230, 7244-7258`; `annulus_geometry.rs:34-45`; `pressure_exact/source_geometry.rs:28-46` |
| Pressure rows | `pipe_wall_axial_force_v2` and `pipe_effective_axial_force_v2` (N, element_local); `pipe_axial_membrane_stress_v2` and `pipe_lame_{radial,hoop}_stress_v2` inner and outer (Pa, pipe_section). All at end_i, quarter_1, midspan, quarter_3 and end_j. Nw = (mechanical section axial) + 2νP; S = Nw − pAi; σz = Nw/As | `PP/src/lib.rs:11512-11590`; `source_geometry.rs:135-150` |
| Endpoint wall action | `pipe_wall_endpoint_action_v2`: end_i = −Nw, end_j = +Nw | `PP/src/lib.rs:11512-11517` |
| Removed on pressurized members | `element_local_axial_force`, `element_local_axial_normal_stress`, `pipe_section_pressure_{hoop,longitudinal}_stress` | `PP/src/lib.rs:11462-11471` |
| Transverse force rows | `element_local_{shear_force_y,z, torsional_moment, bending_moment_y,z}`. At end_i and end_j: node-on-element end forces. At quarter_1, midspan and quarter_3: the section-cut action on the +x face of the i-side segment (the "j-side cut") | `PP/src/lib.rs:5077-5078, 10302-10331, 11100-11180`; `straight_pipe/src/lib.rs:1049-1090, 1501-1530` |
| Stress rows | `element_local_bending_normal_stress_{y,z}` = M/Z and `element_local_torsional_shear_stress` = T·ro/J, from the j-side section action at all five locations, ends included. Published in **MPa** | `PP/src/lib.rs:5179-5199, 5243-5345, 12555-12735`; `stress_recovery/src/lib.rs:431-460` |
| Elastic maximum | `pipe_elastic_normal_stress_maximum_v2`, per member, at governing_station, in Pa: the maximum over the member of \|Nw/As\| + hypot(My, Mz)/Z. It is pressure-coupled through Nw today. (T4-U4's maximum is the arc maximum) | `PP/src/lib.rs:5399-5446, 10340-10420` |
| Frame | local x = i→j; y = y_reference ⟂ x; z = x × y | `frame_kernel/src/lib.rs:526-540` |
| Displacements | `global_nodal_displacement_*` in mm; `global_nodal_rotation_*` in rad, global, right-hand | `PP/src/lib.rs:11182-11260` |
| Reactions | `support_reaction_component_v2` Fx…Mz, global, support-on-pipe, with unrestrained DOFs exactly 0. Also `support_reaction_{force,moment}_magnitude_v2`, the norms | `PP/src/lib.rs:4806-4835, 11400-11435` |
| Supports and loads | `line_stop` `["UX"]`; linear restraints and springs only. `weight` N/m on an element is a distributed force. 0.4.0 refuses thermal primitives (thermal belongs to the element `thermal_state`) | `PP/src/lib.rs:7428-7470, 13510-13521`; `PP/src/pressure_runtime.rs:179-183`; `case_state/resolve.rs:384-385` |

## 2. Closed forms common to all cases

The tube is long, straight, homogeneous and isotropic, with small strain. The internal pressure increment is p and the external increment is zero. Stresses are tension-positive.
- **Lamé:** σr = C − D/r², σh = C + D/r², with C = p ri²/(ro² − ri²) = P/As and D = C ro².
- **Axial:** εz − εth = [σz − ν(σr + σh)]/E, which gives Nw = E As(εz − εth) + 2νP, S = Nw − P and σz = Nw/As.
- **Free tube, transferring closures:** Nw = P and S = 0.
- **Held in UX at both ends:** Nw = 2νP − E As εth.
- **Reactions:** root Fx = P − Nw, far Fx = Nw − P. The caps are applied ledger loads. With separate closures there is no cap, so root Fx = −Nw.

The script first reproduces the qualified rational table and the 6 m companion (`PRESSURE_REFERENCE_QUALIFICATION.md` §2, `STRESS_REFERENCE.md` §8).

## 3. Case 1: `EXACT-PRESSURE-MILLTOL-LAME-MEMBRANE-001`

**What it rebuilds.** It rebuilds MILLTOL's retired `pressure_hoop` (p r_m/t_eff = 28629.62962962963) and `pressure_longitudinal` (hoop/2).

**Inputs.**
- OD 0.2 m. Authored wall 0.008 m. `mill_tolerance` 0.00125 m. So t_eff = 0.00675 m and ri = 0.09325 m.
- p = 2000 Pa; E = 200 GPa; ν = 0.3; L = 2 m.
- One member. Both closures transfer.

**Derived.** P = 139129/8000 π = 54.635830537661793 N.

| Row | Free (anchor A) | Restrained (anchors A, B) |
|---|---|---|
| Nw, S (N) | P, 0 | 2νP = 32.781498322597076, −21.854332215064717 |
| σz (Pa) = elastic maximum | 13332.279239135643 | 7999.3675434813857 |
| σr inner / outer; σh inner / outer (Pa) | −2000 / 0; 28664.558478271286 / 26664.558478271286 | same |
| uB,x | 5.3329116956540e-8 m | 0 |
| Reactions and norms | all 0 | A Fx = +21.854332215064717, B Fx = −21.854332215064717; force norms 21.854332215064717; moment norms 0 |

The transverse force rows and the bending and torsional stress rows are 0.

**Discriminators.**
- Retired values: hoop 28629.630; hoop/2 14314.815.
- `cap_area_on_authored_bore` (new, producible): the mill reduction applied to As, but Ai taken from the authored bore (ri = 0.092). σz = 270848000/20871 = 12977.241148004408 Pa.
- `cap_area_on_nominal_bore` (ri = 0.09, σz 12419.146): kept, marked `producible_today: false` and active from T4-U6. The folded document never carries the 0.01 wall; after D-5 it can.
- Allowance not folded (21902.894 and 9951.4472): these guard the document's authoring, not the product.
- Mill tolerance ignored (24041.667 and 11020.833).
- Longitudinal P/As added to σz (26664.558).
- Poisson sign reversed (restrained Nw −32.781).

**Re-freeze (T4-U6).** The case is re-frozen if D-5 changes the cap-area, eigenstrain-area, stiffness or stress basis. **Inference:** under D-5 as recommended, Nw, S and the reduced-section σz and Lamé rows stay, but only if the As of ε_p equals the stiffness As (RV1 N-5).

## 4. Case 2: `EXACT-PRESSURE-THERMAL-TRANSVERSE-MIXED-001`

**What it rebuilds.** It rebuilds the pressure halves of `MECH-TP-PHYS-008/009`.

**Model.**
- **Section and material:** OD 0.2 m, wall 0.01 m; E 200 GPa; ν 0.3; α 1.2e-5 /degC; ΔT 5 degC; p 2 MPa.
- **Nodes:** A (0), B (1.5), C (4.5), D (6), on X. Local axes = global.
- **Supports:** an anchor at A; a `line_stop` UX at D.
- **Pressure:** one region, A and D transferring.
- **Load cases:**
  - `case:pressure-half`: pressure only;
  - `case:combined`: pressure, plus thermal on every member, plus q = −300 N/m in Y on B-C.

**Axial.** The strain is 0 everywhere. 2νP = 9720π N (tension); E As εth = 22800π N.

| Quantity | pressure-half | combined |
|---|---|---|
| Nw (N) | +9720π = 30536.280592892790 | −13080π = −41092.031908954496 |
| S (N) | −6480π | −29280π = −91985.832897109146 |
| σz (Pa) | 5115789.4736842105 | −6884210.5263157895 |
| Lamé: σr inner / outer; σh inner / outer (Pa) | −2e6 / 0; 19052631.578947368 / 17052631.578947368 | same |
| Anchor A Fx; stop D Fx | ±6480π | ±29280π |
| Elastic maximum A-B; B-C; C-D (Pa) | 5115789.4736842105 each | 130800000/19 + (108000000000/3439)/π = 16880566.358781446; 130800000/19 + (54000000000/3439)/π = 11882388.442548618; 6884210.5263157895 |
| Support norms | A, D: 6480π; moments 0 | A: sqrt((29280π)² + 900²) = 91990.235643653437 N and 2700 N·m; D: 29280π, 0 |

**Transverse (combined).** The beam is a cantilever from A.
- V(x) = q(b − max(x, a)) for x < b. M(x) = q(b − a)(a + b − 2x)/2 on [0, a] and q(b − x)²/2 on [a, b].
- EI v″ = M; EI = 1 719 500π.
- Anchor: Fy = 900 N, Mz = 2700 N·m.

| Member | end_i (node-on-element) Vy, Mz | quarter_1 | midspan | quarter_3 | end_j (node-on-element) |
|---|---|---|---|---|---|
| A-B | 900, 2700 | −900, −2362.5 | −900, −2025 | −900, −1687.5 | −900, −1350 |
| B-C | 900, 1350 | −675, −759.375 | −450, −337.5 | −225, −84.375 | 0, 0 |
| C-D | 0, 0 | 0, 0 | 0, 0 | 0, 0 | 0, 0 |

**Bending stress σz,b = M/Z** at the five locations. These are section values at the ends too, published in MPa; the reference is in Pa.
- A-B: −2700/Z … −1350/Z, i.e. −9996355.8324656560 … −4998177.9162328282 Pa.
- B-C: −4998177.9162328282, −2811475.0778809659, −1249544.4790582071, −312386.11976455176, 0 Pa.
- C-D: 0.

The y-bending and torsional stresses are 0.

**Displacements** (EI v″ = M, Euler–Bernoulli):

| Node | uy (m) | rz (rad) |
|---|---|---|
| B | −81/(55024π) = −4.6857917964682760e-4 | −243/(137560π) |
| C | −2349/(275120π) = −2.7177592419516003e-3 | −351/(137560π) |
| D | −1701/(137560π) = −3.9360651090333522e-3 | −351/(137560π) = −8.1220391138783455e-4 |

**Re-freeze (T4-U8).** The three nonzero uy rows carry a `refreeze` tag: they are re-frozen if D-6 makes Timoshenko the default. The statics, the stresses, the maxima, the reactions, the pressure and axial rows all stay. The rz rows stay if the published rotation is the section rotation.

**Checks.**
- An exact direct-stiffness solve reproduces every nodal value and every station value.
- At 009's own q and EI, the retired transverse half is reproduced (−0.070875 m, −0.014625 rad).
- |M| peaks at a member end on every member, which the script checks.

**Discriminators:** as frozen. They include the legacy same-sign thrust (−122522.11), the Poisson term as compression or omitted, caps subtracted, the i-side station sign, and the full-span load (uy(D) −4.4983601e-3).

## 5. Case 3: `EXACT-PRESSURE-LAME-THIN-WALL-LIMIT-001`

**What it rebuilds.** It rebuilds `STRESS-PRESSURE-MEMBRANE-ORIGINAL` (p 100 Pa, r_m 3, t 0.5; retired hoop 600, longitudinal 300).

**Model.** OD 6.5, wall 0.5, L 65, free closed tube.

**Lamé reference.**
- σh = 3625/6 (inner) and 3025/6 (outer).
- σz = elastic maximum = 3025/12 = 252.08333333333333.
- σr = −100 / 0.
- The reactions and their norms are 0.

**Thin-wall comparison** (Lamé is the reference). The relative differences (thin − Lamé)/Lamé are:
- −1/145 against the inner hoop;
- +23/121 against the outer hoop;
- +1/11 against the mean hoop p ri/t;
- +23/121 for σz.

The exact limit forms are σh(ri) = p r_m/t + pt/(4r_m), σh(ro) = p r_m/t − p + pt/(4r_m) and σz = p r_m/(2t) − p/2 + pt/(8r_m).

## 6. SP-1 twins and the pair scope

**`/sp1_pair_scope` (S-4) governs every v2/v3 pair in the file.**
- **Inputs:** only p ≥ 0 inputs, which v2 admits. A p < 0 v3 document has no v2 twin.
- **Clause 1:** the candidate's serialized v2 envelope is byte-identical to the base revision's (the PR's merge base on main), per document and mode.
- **Clause 2:** every numeric JSON leaf of the v3 envelope is bit-equal to the v2 leaf at the same path, with the sign of zero included and arrays in order. Every non-numeric leaf is equal too, except a closed exclusion list:
  - E1: `producer.semantic_contract_id`;
  - E2: `formulation_basis.profile_id` and `limitations`;
  - E3: contract_evidence strings that state the contract, the semantics or the admitted families, with their paths enumerated by T4-U2a;
  - E4: diagnostic message text that names the contract;
  - E5: kind strings, only through a declared one-to-one correspondence.

  No numeric leaf is excluded, including material, eigenload, cap, assembly, section, `pipe_stress_extrema` and 0.4.0 evidence.
- **Clause 3:** per mode and per schema version separately.
- **Recommendation:** apply the same check mechanically to every existing v2 exact document in PP's tests with p ≥ 0 (T4-RV4 N-4).

**Twin A, `EXACT-PRESSURE-V3-STRAIGHT-TWIN-ODWALL-001`.** It is unchanged in substance. Its documents are `SOURCE_ODWALL_EXPECTATIONS.json` case 0 `ordinary` (sha256 `7e51ecb3…1ab1`) with the `pressure_section_geometry.rs` `fixture()` document.
- **Expectation:** `/sp1_pair_scope`.
- **Independent values:** the fixture's, at 1e-9. 21 are re-derived exactly, each binary64-identical.
- **Re-freeze in T4-U8:** the fixture's `tip_bending_y_m` as an independent value, if D-6 changes the default.

**Twin B, `EXACT-PRESSURE-V3-STRAIGHT-TWIN-SEPARATE-CLOSURES-001` (new, N-4).** No fixture under `pressure_reference/` has separately supported closures, so the existing v2 document `PP/tests/pressure_runtime.rs` `model(true, false, 0.0)` serves (state 4 of the six-state test).
- **Model:** OD 0.12 m, wall 0.01 m, both ends anchored, p 2 MPa, separate closures, y_reference (0, 0, 1).
- **Rows:**
  - Nw = 3000π, S = −2000π, σz = maximum = 30 000 000/11;
  - Lamé −2e6 / 0 and 122e6/11 / 100e6/11;
  - root Fx = −3000π, far +3000π, norms 3000π;
  - displacements 0 (zero scale: the free-wall contraction 9/110000 m).
- **Cross-checks:** equal to the test's frozen values, and to `PRESSURE_REFERENCE_QUALIFICATION.md` §3 item 2.

## 7. Document sketches

For every case:
- `v2_model_0.3.0`: runnable today.
- `v2_model_0.4.0`: `reference_configurations` plus each case's `analysis_state`. Thermal is a `constant_alpha_interval`; every primitive is listed in `load_sources`.
- `v3_patch_for_both`: provisional.
- `sp1_pair`: points to `/sp1_pair_scope`.

The twins' 0.3.0 documents equal their test builders' output field for field.

## 8. Criteria and transport

- **Modes:** both modes, one reference.
- **Nonzero values:** |obs − exp| ≤ 1e-9 |exp|.
- **Zero values:** |obs| ≤ 1e-9 |scale|.
- **Negative assertions:** |obs − wrong| > 1e-9 max(|obs|, |wrong|).
- **No new threshold.**
- **T1 shape (S-1).** Every row carries `reference_origin` {analytical, RFC 6901 pointer, reference_unit, transform identity}. Each zero row adds T1's `zero_scale` {tag, base {pointer, reference_unit}, scale_unit}.
  - The reference is converted into the row unit by an exact factor (m → mm, Pa → MPa). Tolerances are precomputed in the row unit.
  - The `zero_scales` entries are pure maintained quantities; their definitions are in the sibling `zero_scale_definitions`.
  - The probe confirms that T1's own `origin_value` and `zero_scale_value` reproduce every accepted value and every tolerance exactly.

## 9. Limits

- **Scope:** linear, small strain, long straight annuli, zero external increment. The values are invented.
- **ν = 0.3 and decimal inputs** are absorbed by the 1e-9 criterion.
- **Admission is inferred, not run:** `line_stop`, the `weight` N/m element load and the 0.4.0 sketches are read from code as admitted on the exact route.
- **Bend cases** belong to T4-I7.
