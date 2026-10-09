# T4-I8: independent references for T4-U2's rebuilt straight cases (freeze)

- **Role:** TASK (Type 2) for T4's WORKING_ITEMS. Brief `R4/BRIEFS/T4-I8_U2_STRAIGHT_REBUILT_REFERENCES.md` (sha256 `1f294de5…a7aa134`); common terms `R4/BRIEFS/T4_WI_COMMON.md` (sha256 `7d44afd0…02cb`); both at `0c17c8d352`.
- **Status:** frozen before any T4 code; awaiting the refuting TASK. Not product evidence.
- **Independence:** every value is a closed form (Lamé, Hooke with the Poisson term, beam statics) in exact rational arithmetic, rational × π^k. The product was read only for conventions (§1) at `ed012c7ccf`. The retired cases were read at `ec5d397359`. No product build, run, test or output was used.
- **Files:** `rebuilt_reference_cases.json` (authoritative values: 85-digit decimals, exact forms, binary64 projections, rows, zero scales, discriminators, document sketches); `_run_records/derive_rebuilt_references.py` and its stdout (162 checks, all pass); `_run_records/check_reference_json.py` and its stdout (consumer-side re-evaluation of all 235 quantities and 690 rows; PASS).
- **Reproduce:** from `R4/T4-I8/_run_records/`, run `WT/venv/bin/python -I derive_rebuilt_references.py <SOURCE_ODWALL_EXPECTATIONS.json at ed012c7ccf> ../rebuilt_reference_cases.json`, then run `check_reference_json.py ../rebuilt_reference_cases.json`.

## 0. Findings for the plan

1. **No stop rule is triggered.** SP-1 is carried as case 4's expectation and as the v2/v3 pairing of every case.
2. **The exact route cannot author a partial-span load (fact).** Partial extents exist only for `equivalent_static` wind (`PP/src/lib.rs:633-651, 10259-10260`), and the exact route refuses that. Case 2 therefore represents 009's loaded interval [0.25 L, 0.75 L] exactly, with a three-member collinear chain that carries a uniform load on its middle member. A one-member 009 would need a new primitive field, which no unit plans.
3. **MILLTOL has no corrosion-allowance input (fact; `PP/src/lib.rs:320-330`).** The allowance is folded into the authored wall (0.01 − 0.002 = 0.008 m), and the mill tolerance (0.00125 m) stays in its own slot. The case is marked for re-freeze in T4-U6 if D-5 changes the basis.
4. **Two shape points for the package.**
   - The force magnitude of case 2's combined root support has the form sqrt((29280π)² + 900²). It is recorded as `symbolic` (sqrt), which T1's generator does not evaluate. Extend the generator, or leave that row out of the package.
   - The twin's values stay in their own fixture, whose format is `{decimal, f64, exact_rational_with_bounded_pi}`. A package adapter reads that format, not this file's.
5. **The case ids and the v3 wire are proposals (inference).** The ids are proposals. The v3 contract patch `3.0.0/exact_pressure_v3` (H-1) is provisional until T4-U2a fixes the wire.

## 1. Conventions read from the product (fact, `@ed012c7ccf`)

| Item | Convention | Source |
|---|---|---|
| Section | Effective wall = `wall_thickness − mill_tolerance` (an absent slot means no reduction). ro = OD/2, ri = ro − t. As = πt(OD − t). Ai = π ri² (reduced bore). I = As(ro² + ri²)/4, J = 2I, Z = I/ro | `PP/src/lib.rs:10213-10230, 7244-7258`; `annulus_geometry.rs:34-45`; `pressure_exact/source_geometry.rs:28-46` |
| Pressure rows | `pipe_wall_axial_force_v2`, `pipe_effective_axial_force_v2` (N, element_local); `pipe_axial_membrane_stress_v2`, `pipe_lame_{radial,hoop}_stress_v2` inner/outer (Pa, pipe_section). All at end_i, quarter_1, midspan, quarter_3, end_j. Nw = (mechanical section axial) + 2νP; S = Nw − pAi; σz = Nw/As | `PP/src/lib.rs:11512-11590`; `source_geometry.rs:135-150` |
| Endpoint wall action | `pipe_wall_endpoint_action_v2`: end_i = −Nw, end_j = +Nw (node-on-element, +local x) | `PP/src/lib.rs:11512-11517` |
| Removed on pressurized members | `element_local_axial_force`, `element_local_axial_normal_stress`, `pipe_section_pressure_{hoop,longitudinal}_stress` | `PP/src/lib.rs:11462-11471` |
| Transverse rows | `element_local_{shear_force_y,z, torsional_moment, bending_moment_y,z}`. At end_i and end_j: node-on-element end forces. At quarter_1, midspan and quarter_3: the section-cut action on the +x face of the i-side segment, which is the negated i-side helper sum (the "j-side cut") | `PP/src/lib.rs:5077-5078, 10302-10331, 11100-11180`; `straight_pipe/src/lib.rs:1049-1090, 1501-1530` |
| Frame | local x = i→j; y = y_reference ⟂ x; z = x × y | `frame_kernel/src/lib.rs:526-540` |
| Displacements | `global_nodal_displacement_*` in mm; `global_nodal_rotation_*` in rad, global, right-hand | `PP/src/lib.rs:11182-11260` |
| Reactions | `support_reaction_component_v2` Fx…Mz, global, support-on-pipe. All six are published for every support; unrestrained DOFs are exactly 0 | `PP/src/lib.rs:4806-4835, 11400-11422` |
| Supports and loads | `line_stop` with `["UX"]`; linear restraints and springs only on the exact route. Category `weight` with N/m on an element is a distributed force; negative magnitudes are accepted. 0.4.0 refuses thermal primitives: thermal strain belongs to the element `thermal_state` | `PP/src/lib.rs:7428-7470, 13510-13521, 9126`; `PP/src/pressure_runtime.rs:179-183`; `case_state/resolve.rs:384-385` |

## 2. Closed forms common to all cases

The tube is long, straight, homogeneous and isotropic, with small strain. The internal pressure increment is p and the external increment is zero. Stresses are tension-positive.
- **Lamé:** σr = C − D/r², σh = C + D/r², with C = p ri²/(ro² − ri²) = P/As and D = C ro², so that σr(ri) = −p and σr(ro) = 0. Then σh(ri) = p(ro² + ri²)/(ro² − ri²) and σh(ro) = 2p ri²/(ro² − ri²).
- **Axial:** εz − εth = [σz − ν(σr + σh)]/E, which gives Nw = E As(εz − εth) + 2νP, S = Nw − P and σz = Nw/As.
- **Free tube, transferring closures:** Nw = P and S = 0. The tube extends by L[εth + (1 − 2ν)P/(E As)].
- **Axially held at both ends:** εz = 0, so Nw = 2νP − E As εth.
- **Reactions:** the root support-on-pipe Fx = P − Nw = −S; the far support gives Nw − P = S (the caps are applied ledger loads, `+P` outward at each transferring terminal).

The script first reproduces the qualified rational table (`PRESSURE_REFERENCE_QUALIFICATION.md` §2: radial [−3, 0], hoop [5, 2], and all five Nw/S/strain states) and the 6 m companion (`STRESS_REFERENCE.md` §8), using its own functions.

## 3. Case 1: `EXACT-PRESSURE-MILLTOL-LAME-MEMBRANE-001`

**What it rebuilds.** It rebuilds the membrane values of `STRESS-TP-PMM-P3-MILLTOL-EFFECTIVE-WALL-STRESS`: the retired `pressure_hoop` = p r_m/t_eff = 28629.62962962963 and `pressure_longitudinal` = hoop/2. The crate's axial, bending and torsion values are unchanged and outside this case.

**Inputs.**
- OD 0.2 m. Authored wall 0.008 m (= nominal 0.01 − allowance 0.002). `mill_tolerance` 0.00125 m. So t_eff = 27/4000 = 0.00675 m, the same as the retired t_eff.
- ri = 373/4000 = 0.09325 m; ro = 0.1 m.
- p = 2000 Pa (kept from the retired case); E = 200 GPa; ν = 0.3 (invented; the retired case had none); L = 2 m.
- One member A→B. Both terminals `transfers_to_wall`.

**Derived.** As = 20871/16 000 000 π; Ai = 139129/16 000 000 π; P = 139129/8000 π = 54.635830537661793 N.

| Row (all five stations) | Free (anchor A) | Axially restrained (anchors A, B) |
|---|---|---|
| Nw (N) | P = 54.635830537661793 | 2νP = 32.781498322597076 |
| S (N) | 0 (zero scale P) | (2ν−1)P = −21.854332215064717 |
| σz (Pa) | P/As = 13332.279239135643 | 7999.3675434813857 |
| σr inner / outer (Pa) | −2000 / 0 (scale P/As) | same |
| σh inner / outer (Pa) | 28664.558478271286 / 26664.558478271286 | same |
| Endpoint action end_i / end_j | ∓Nw | ∓Nw |
| uB,x | (1−2ν)PL/(E As) = 5.3329116956540e-8 m | 0 (zero scale: the free extension) |
| Reactions | all 0 | A: Fx = +21.854332215064717; B: Fx = −21.854332215064717; the rest 0 |

Transverse rows, the other displacements and the other reactions are 0, with zero scales P, PL, the free extension and the free extension/L.

**Discriminators** (values a correct product must not produce):
- the retired thin-wall hoop 28629.630 and the retired hoop/2 14314.815;
- allowance not folded (t = 0.00875): inner hoop 21902.894, free σz 9951.4472;
- mill tolerance ignored (t = 0.008): 24041.667 and 11020.833;
- Ai from the nominal bore with the reduced As: σz 12419.146;
- a longitudinal P/As added to Nw/As: 26664.558;
- the Poisson sign reversed (restrained Nw −32.781).

**Re-freeze (T4-U6).** The case is re-frozen if D-5 changes the cap-area, eigenstrain-area, stiffness or stress basis. Under D-5 as recommended, the document would carry wall 0.01, a corrosion-allowance input and the mill tolerance. **Inference:**
- the displacements and any nominal-section stress row move;
- Nw, S and the reduced-section σz and Lamé rows stay.

## 4. Case 2: `EXACT-PRESSURE-THERMAL-TRANSVERSE-MIXED-001`

**What it rebuilds.** It rebuilds the pressure halves of `MECH-TP-PHYS-008-…` and `MECH-TP-PHYS-009-…`. The retired premise was F = pAi = 9 N, added with the same sign as the thermal 3 N, on non-annular sections. The crate fixtures keep their ids and their non-pressure halves.

**Model.**
- **Section and material:** OD 0.2 m, wall 0.01 m (ri 0.09); E 200 GPa; ν 0.3; α 1.2e-5 /degC; ΔT +5 degC (εth = 6e-5); p 2 MPa.
- **Nodes:** A (x = 0), B (1.5), C (4.5), D (6), on global X. Members A-B, B-C, C-D, with y_reference (0, 1, 0), so local = global.
- **Supports:** an anchor at A; a `line_stop` UX at D (the mixed restraint). This is 009's "node 0 fixed, node 1 Ux restrained".
- **Pressure:** one region over all three members, terminals A and D `transfers_to_wall`. The interior caps cancel (equal bore).
- **Load cases:**
  - `case:pressure-half`: pressure only;
  - `case:combined`: pressure, plus thermal on all three members, plus q = −300 N/m in global Y on B-C. This is 009's loaded interval [a, b] = [1.5, 4.5] m.

**Axial.** Both ends are held in UX, so the strain in every member is 0 and interior UX = 0.
- Nw = 2νP − E As εth. Here 2νP = 9720π = +30536.280592892790 N (tension) and E As εth = 22800π = 71628.312501847286 N (compression).

| Quantity | pressure-half | combined |
|---|---|---|
| Nw (N), every station of every member | +9720π = 30536.280592892790 | −13080π = −41092.031908954496 |
| S = Nw − P (N) | −6480π = −20357.520395261860 | −29280π = −91985.832897109146 |
| σz (Pa) | 97 200 000/19 = 5115789.4736842105 | −130 800 000/19 = −6884210.5263157895 |
| σr inner / outer; σh inner / outer (Pa) | −2e6 / 0; 362e6/19 = 19052631.578947368 / 324e6/19 = 17052631.578947368 | same |
| anchor A Fx = P − Nw; stop D Fx = Nw − P | ±6480π = ±20357.520395261860 | ±29280π = ±91985.832897109146 |

**Transverse (combined only).** The beam is a cantilever from A; D is free in Y and RZ.
- **Statics:** V(x) = q(b − max(x, a)) for x < b, and 0 beyond. M(x) = q(b − a)(a + b − 2x)/2 on [0, a], q(b − x)²/2 on [a, b], and 0 on [b, L].
- **Deflection:** EI v″ = M, with v(0) = v′(0) = 0. EI = 1 719 500π N·m².
- **Anchor:** Fy = −V(0) = 900 N and Mz = −M(0) = 2700 N·m; Fz = Mx = My = 0. The line stop carries Fx only.

| Member | end_i (node-on-element) Vy, Mz | quarter_1 | midspan | quarter_3 | end_j (node-on-element) |
|---|---|---|---|---|---|
| A-B | 900, 2700 | −900, −2362.5 | −900, −2025 | −900, −1687.5 | −900, −1350 |
| B-C | 900, 1350 | −675, −759.375 | −450, −337.5 | −225, −84.375 | 0, 0 |
| C-D | 0, 0 | 0, 0 | 0, 0 | 0, 0 | 0, 0 |

**Displacements.**

| Node | uy (m) | rz (rad) |
|---|---|---|
| B | −81/(55024π) = −4.6857917964682760e-4 | −243/(137560π) = −5.6229501557619310e-4 |
| C | −2349/(275120π) = −2.7177592419516003e-3 | −351/(137560π) = −8.1220391138783455e-4 |
| D | −1701/(137560π) = −3.9360651090333522e-3 | −8.1220391138783455e-4 |

UX, UZ, RX and RY are 0 at every node.

**Second method and convention checks.**
- An exact direct-stiffness solve (Euler–Bernoulli, consistent loads, end-force recovery and station statics) reproduces every nodal value and every station V and M identically.
- At 009's own q = −2 N/m and EI = 2000, the closed form gives the retired hand calculation's unchanged transverse half: u_y = −0.070875 m and θ_z = −0.014625 rad. Its i-side stations (6, 9) are the negated j-side cut.

**Zero scales.**
- Axial zeros: P, and L(εth + (1 − 2ν)P/(E As)).
- Transverse zeros: 900 N, 2700 N·m, |uy(D)| and |rz(D)|. The pressure-half case uses P, PL and the free extension.

**Discriminators.**
- On Nw: the legacy same-sign thrust −E As εth − P = −122522.11; the Poisson term as compression −102164.59; the Poisson term omitted −71628.313; caps subtracted −91985.833.
- S sign reversed.
- Legacy root reaction 122522.11.
- Pressure-half: −2νP, −P, and 2νP − P.
- i-side station sign at A-B midspan: +2025.
- The same total load over the full span: uy(D) = −4.4983601e-3 m. The root Fy and Mz are identical, so they cannot discriminate.

## 5. Case 3: `EXACT-PRESSURE-LAME-THIN-WALL-LIMIT-001`

**What it rebuilds.** It rebuilds `STRESS-PRESSURE-MEMBRANE-ORIGINAL`: p 100 Pa, r_m 3 m, t 0.5 m, retired hoop 600 and longitudinal 300.

**Model.** OD = 2r_m + t = 6.5 m and wall 0.5 m, so ro = 13/4 and ri = 11/4. E 200 GPa, ν 0.3, L 65 m. Anchor at A, B free, both terminals transferring. As = 3π, P = 756.25π.

**Lamé reference.**
- σh(ri) = 3625/6 = 604.16666666666667; σh(ro) = 3025/6 = 504.16666666666667.
- σr = −100 / 0.
- σz = Nw/As = 3025/12 = 252.08333333333333; Nw = P and S = 0.
- uB = 1573/48 000 000 000 = 3.2770833333333e-8 m.

**Thin-wall comparison** (Lamé is the reference). The limit forms are exact:
- σh(ri) = p r_m/t + pt/(4r_m);
- σh(ro) = p r_m/t − p + pt/(4r_m);
- σz = p r_m/(2t) − p/2 + pt/(8r_m).

The differences are O(p) against O(p r_m/t), so they vanish relatively as t/r_m → 0. The relative differences (thin − Lamé)/Lamé are:

| Thin-wall value | vs | Relative difference |
|---|---|---|
| hoop 600 | σh(ri) | −1/145 = −0.69% |
| hoop 600 | σh(ro) | 23/121 = +19.0% |
| hoop 600 | mean hoop p ri/t = 550 | 1/11 = +9.09% |
| longitudinal 300 | σz free | 23/121 = +19.0% |

**Discriminators:** 600, 300, and 550 used as a surface value.

## 6. Case 4: `EXACT-PRESSURE-V3-STRAIGHT-TWIN-ODWALL-001`

**Chosen fixture.** `PP/tests/fixtures/pressure_reference/SOURCE_ODWALL_EXPECTATIONS.json` (sha256 `7e51ecb3…1ab1` at `ed012c7ccf`), case 0 `ordinary`: OD 0.12, wall 0.01, p 2 MPa, E 200 GPa, ν 0.3, L 6, tip Fy 100 N, tip Mx 1 N·m, an anchored cantilever with transferring closures.
- **Its v2 consumer** is `PP/tests/pressure_section_geometry.rs` (`fixture()`, `ordinary_source_annulus_properties_and_all_responses`).
- **Why this one.** It exercises every v2 row family in one document: extension, bending, torsion, the five-station pressure rows, the endpoint actions, the elastic normal maximum, the reactions and the section evidence.
- **The documents.** The v2 0.3.0 document is that test's `fixture()` output field for field. A 0.4.0 form and the v3 patch are included.

**What "bit-equal" covers.** For each solver mode separately (SP-1), every quantity below is compared for identical f64 bits, including the sign of zero:
- every published row value, matched on (kind, entity, component, location, case) through the declared kind correspondence. That correspondence is the identity unless T4-U2a renames kinds;
- the row set (the same keys);
- the summary maxima and their targets;
- the numeric section and pressure evidence (OD, wall, ri, ro, Ai, As, I, J, Z, assembled cap forces);
- the status, the diagnostics and the per-case standing.

It does **not** cover: contract-identity strings and formulation text, any id that embeds the contract (to be declared by T4-U2a), cross-mode equality, or 0.3.0 against 0.4.0.

**Independent values.** The v3 run must also meet the fixture's frozen values at relative 1e-9. As an extra check, T4-I8 re-derived 21 of them exactly from the binary64 inputs (P, extension, tip bending and rotations, membrane, Lamé, maximum, torsional shear, reactions, section properties). Each rounds to the fixture's binary64 value.

## 7. Document sketches (in the JSON, per case)

- `v2_model_0.3.0`: runnable today on `2.0.0/exact_straight_pressure_v2` (straight only). Thermal is a per-member `thermal` primitive in degC, with α on the material.
- `v2_model_0.4.0`:
  - the same geometry, supports and regions, plus `reference_configurations` (`direct_strain_reference`, fit none);
  - each case's `analysis_state` (explicit base properties; thermal as `constant_alpha_interval` α = 1.2e-5 /degC, ΔT = 5 degC, or `unchanged_reference`; every support `active_model_device`; every remaining primitive in `load_sources` with factor 1);
  - no thermal primitive.
- `v3_patch_for_both`: **provisional**. It replaces `/model/pressure_contract` with `3.0.0/exact_pressure_v3`. Straight members are expected to need no field beyond v2's.

## 8. Criteria

- **Modes:** both modes (`sparse_interactive`, `dense_scrutiny`), against one reference.
- **Nonzero values:** |obs − exp| ≤ 1e-9 |exp|.
- **Zero values:** |obs| ≤ 1e-9 |zero_scale|. Each row names its scale, and the absolute tolerance is precomputed in the reference unit. The comparison is made after the row transform (displacements are published in mm, so m_to_mm applies).
- **Negative assertions:** |obs − wrong| > 1e-9 max(|obs|, |wrong|). Each discriminator is distinct from its correct value (checked).
- **No new threshold.**
- **Structural expectations:** MECHANICS_SOLVED with no blocking diagnostic; the removed legacy kinds are absent; each pressure row appears exactly once in its region's `result_ids`.

## 9. Limits and points for the refuter

- **Scope:** linear, small-strain, long straight annuli with zero external increment. The values are invented and are not library or code data. Tiny invented pressures (2000 Pa, 100 Pa) are kept from the retired cases for traceability.
- **ν = 0.3 and decimal inputs** are not binary64-exact. The 1e-9 relative criterion absorbs this.
- **Case 2's chain** relies on the exact route's handling of interior chain nodes. The product's tests cover that for two spans (`PP/tests/pressure_runtime.rs:572-603`).
- **Not frozen here:** the elastic stress maxima for cases 1–3 and the bend cases (T4-I7).
- **Inference, not run:** that `line_stop`, the `weight` N/m element load and the 0.4.0 sketches pass admission on the exact route. This is read from code; the implementer confirms it on the first run.
