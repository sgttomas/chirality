# T4-I7: independent VP-STATIC references for T4-U2 (pressure through realized bends)

**Status.** Frozen by T4-I7 (TASK, Type 2) for T4's WORKING_ITEMS, before any T4-U2 code exists.
- T4-RV3 refuted round 00 (`80b1e97e2b`). It found every value correct and blocked on B-1.
- **Repair round 01** applies B-1 and S-1 to S-3; `REPAIR_01.md` maps each change.
- The file is not accepted until RV3 confirms the repair.

**Brief.** `R4/BRIEFS/T4-I7_U2_BEND_REFERENCES.md` (`cee2f2dd…`), common terms `R4/BRIEFS/T4_WI_COMMON.md` (`7d44afd0…`), at `0c17c8d352`.

**Basis.** The product was read at `ed012c7ccf` for conventions only: DOF order, frames, station names, the section rule, how a document states self-weight and gravity. No value was taken from it. The values come from `_run_records/u2_engine.py` and `u2_generate.py`. They are written to `u2_reference_cases.json` (80 cases: 79 with values and one refusal control) and `u2_document_sketches.json`.

**Marks.** **F** is a fact read from cited bytes (`path:line@ed012c7ccf`, with `CB` = `P/core/solver/curved_bend/src/lib.rs` and `PPL` = `PP/src/lib.rs`). **I** is my inference or derivation.

## 1. The formulation matched

- **Straights:** Euler–Bernoulli, with axial, torsion and bending energy. No shear.
- **Arcs:** axial and torsion energy, plus in-plane and out-of-plane bending energy scaled by the user's k. No shear.
  - F: k scales only the two bending terms (`CB:205-239`).
  - F: PP passes one k to both planes (`PPL:7848-7863`).
- **Material and kinematics:** small strain and small displacement; linear elastic, homogeneous and isotropic; E and ν given, with G = E/(2(1+ν)).
- **Pressure:** static internal pressure only. These are excluded (D-3):
  - flow momentum and transient loads;
  - bend opening (Bourdon);
  - pressure stiffening of k and the SIF;
  - ovalization.
- **The Poisson eigenstrain on arcs** is −2νpAi/(E·As), the straight Lamé mean (RV1 S-5).
- **Recovery on straights is today's** (I): N_w = N_mech + 2νP and S = N_mech + (2ν−1)P, with P = pAi. N_w is the tension-positive section axial force, and S = N_w − P. The recovery identities below are therefore form-independent.

## 2. Method: direct unit-load flexibility over the whole line (I)

**The model.** The line is a chain A → D, treated as a cantilever from anchor A. These loads act on the pipe wall:

| Load | Where | Value |
|---|---|---|
| Wetted-wall load | every arc, at the centreline, with no distributed moment | (P/R)·e_r per unit arc length, outward |
| Terminal cap | A and D, only where the terminal `transfers_to_wall` | −P·t_A at A; +P·t_D at D (end tangents) |
| Kink force | each interior node | P(t_in − t_out); zero for exact tangency |
| Axial eigenstrain | every member, arcs included, uniform | ε0 = αΔT − 2νP/(E·As) |
| Self-weight | every member, per unit centreline length (arc length on bends) | w along global −Z |

**Section actions.** Positive N is tension. At a cut at x(s), the action is the resultant of everything beyond the cut, with moments taken about x(s): the distributed loads on the cut member's remainder, every later member, the point loads at later nodes, and the redundant at D.

The closed forms on an arc are written in traversal order: angle ψ, radial basis e1 and e2, n̂ = e1 × e2, Δ = Φ − ψ, and Er = (sin Φ − sin ψ)e1 + (cos ψ − cos Φ)e2.
- **Wall load:** F = P·Er and M = −RP(1 − cos Δ)·n̂.
- **Self-weight:** F = wRΔ·ĝ and M = R²(Er − Δ·e_r(ψ)) × wĝ.
- **On a straight remainder of length r:** F = wr·ĝ and M = (r/2)t × F.

**Compatibility (virtual work).** For a unit action at node n in direction a, with actions N_a, T_a and M_a on the members between A and n:

`δ_{n,a} = ∫ [N_a N/(E·As) + T_a T/(G·J) + k(M_a·M − T_a T)/(E·I) + N_a ε0] ds`

Here k = 1 on straights. Because the section is circular, M·m − Tt is the bending part.

**An anchored D.** The six redundants r (support-on-pipe at D) solve F_DD r = −δ0. The reaction at A follows from the equilibrium of node A: R_A = −(cut action just past A + the cap applied at A).

**What the method does not use** for any value: no stiffness matrix of a curved element, no K·u_free and no thermal analogy.

**Numerics.**
- Python `decimal` at 60 digits.
- Arc integrals by 30-point Gauss–Legendre. Recomputed at 90 digits with 50 points, every written 20-digit value is unchanged (8 cases, 4,394 values; `u2_precision_check.stdout.txt`). Straight integrands are cubic, so 4 points are exact.
- π by Machin's formula; sin, cos and atan by series.
- Global equilibrium residuals are ≤ 1e-54 N and 4e-48 N·m, the latter at X = 7.3e6 m.
- A value below 1e-40 of its group's characteristic scale is written as exact 0.

**The arc geometry follows the product's rule.**
- F (`PPL:7760-7846`): the centre is c = (x_i + x_j)/2 − √(R² − L²/4)·ŷ, with ŷ the pipe `y_reference` projected normal to the chord.
- F: Φ = 2 asin(L/2R), and the arc bows toward +`y_reference`.
- The engine forms the arc from node differences, R and ŷ, as T4-U1 intends. So the arc ends coincide with the input nodes exactly.

**Closed forms that fall out (I, each checked by the engine):**

| Case | Result | Engine agreement |
|---|---|---|
| Free closed L, both terminals transferring, no weight | Wall load plus caps is the membrane state at every cut: N_w = P, V = M = T = 0, S = 0, zero reactions. Every node moves by (ε_p + ε_th)(x − x_A) with zero rotation, where ε_p = (1−2ν)P/(E·As). This holds for any chain, including kinks, because the kink forces balance exactly | ≤ 1e-53 m, UTM cases included |
| Free L with the closure at A separately supported (SEPA) | The same membrane state, with R_A = −P·t_A and the remote closure reaction +P·t_A | — |
| Free L with the closure at D separately supported (SEPD) | The arc wall load is unbalanced: S2 carries N_w = 0 and S = −P. At an arc station, N = P(1 − cos(Φ−θ)), V_y = −P sin(Φ−θ) and M_z = −RP(1 − cos(Φ−θ)) | Agrees with the engine |
| Anchored D with a separately supported closure at D | The cap at an anchored node changes only R_D, by −P·t_D. Every other value equals the transferring case | So this variant discriminates only R_D (I) |

## 3. Conventions (F unless marked)

- **Frames.** Global X, Y and Z are right-handed. Gravity is along −Z: the self-weight primitive is `distributed_force` with direction `global_z` and magnitude −w N/m (`self_weight.rs:163,373`).
  - **Straight element-local frame:** x = (x_j − x_i)/L, y = `y_reference` projected normal to x, z = x × y (`FK/src/lib.rs:526-540`).
  - **Arc tangent frame at a station:** x is the tangent toward authored j, y points to the centre, z = (x_i − c) × (x_j − c) normalized (`CB:360-450`; `PPL:10964`).
- **Stations.** These are j-side section actions (`PPL:10963-10964`; `CB:406`) at end_i, quarter_1, midspan, quarter_3 and end_j. The fractions 0, ¼, ½, ¾ and 1 are of the authored length on straights, or of the included angle on arcs. The product uses the same names on both (`PPL:5114,11066`).
  - Each station carries N_w, S = N_w − P, σ_m = N_w/As, V_y, V_z, T, M_y and M_z.
  - It also carries σ_b,y = M_y/Z, σ_b,z = M_z/Z and τ_t = T·r_o/J: today's stress rows (`P/core/loads/stress_recovery/src/lib.rs:432-466,793`).
- **End rows** are node-on-element actions. At end_i the row is −(the j-side action at fraction 0); at end_j it is +(the j-side action at fraction 1).
  - On straights they are in the element-local frame, and `wall_axial_end_action` is today's `pipe_wall_endpoint_action_v2` (`PPL:11516`).
  - On arcs the asserted wall rows are in the tangent frame at that end (RV1 S-7).
  - **Arcs also carry `chord_frame_elastic`** (repair 01, S-1). This is the elastic node-on-element action K·d − p of the curved element, in the chord frame: x along the chord, y = `y_reference` projected, z = x × y.
    - It equals the wall action minus the bend's own cap pair c_b = [−pAi·t_i, +pAi·t_j] (H-2). The moments are the wall moments.
    - These are today's chord-frame component end rows on arcs (I1 §5.3 #8; I2 §3.4), which are not wall actions.
    - Example (U2-L-ANCH-ALL-K2, BEND end_i): F_y = −396.08167949273772476 N elastic, against −67,849 N on the wall basis.
    - The round-00 wall-basis chord block is removed.
- **Lamé surface values,** on straights only: radial −p (inner) and 0 (outer); hoop 2P/As + p (inner) and 2P/As (outer). They are withheld on arcs (plan §2 and §4.3 item 1).
- **Supports** are support-on-pipe, in global axes, with moments about the attached node (`PPL:11412`).
- **Terminals.** For each terminal the file carries `closure_pressure_load_global` (the outward cap), `pipe_cap_transfer_global`, and `remote_closure_support_reaction_global` = −cap where the closure is separately supported. These match the product's evidence fields (`pressure_runtime.rs:687-690`).
- **Units.** The references are in SI. The product publishes nodal translations in mm (`PPL:11193-11214`).
- **Section rule** (`PPL:10194-10241`):
  - t_eff = wall − mill;
  - ID = OD − 2t_eff;
  - As = π(OD² − ID²)/4 and Ai = π·ID²/4;
  - I = π(OD⁴ − ID⁴)/64, J = 2I, Z = I/(OD/2).
  - One basis serves stiffness, ε_p, the caps and the mass. This needs re-freezing in T4-U6 if D-5 changes the basis.

## 4. Cases (complete inputs are in each case's `inputs` block)

**Parameters** (invented; not library or code-rule data):

| Set | OD (m) | Wall (m) | Mill (m) | E (Pa) | ν | α (1/°C) | p (Pa) |
|---|---|---|---|---|---|---|---|
| L and U | 0.1683 | 0.00711 | 0.000889 | 2.0e11 | 0.3 | 1.2e-5 | 5.0e6 |
| CBPT | 0.2191 | 0.0081 | 0 | 1.95e11 | 0.3 | (unused) | 2.5e6 |

- **Thermal:** ΔT = 50 °C on every member.
- **Self-weight:** w = 430.95029961112000 N/m. It is derived from (As·7850 + Ai·1000)·9.80665 and authored directly.
- **Derived values for L and U:**
  - P = 95,393.346…;
  - ε_p = 6.0229777…e-5;
  - ε_ν = −9.0344666…e-5;
  - ε_th = 6.0e-4.

**Geometry** (bend radius R = 0.25 m; coordinates are dyadic, so they are exact at UTM scale):

| Name | Nodes in traversal order | Members | Bend `y_reference` |
|---|---|---|---|
| L | A(0,0,0), B(3,0,0), C(3.25,0.25,0), D(3.25,4.25,0) | S1 A→B, BEND B→C (90°), S2 C→D | (1,−1,0) |
| U | A(0,0), B1(4,0), C1(4.25,0.25), B2(4.25,2.75), C2(4.5,3), B3(6.5,3), C3(6.75,2.75), B4(6.75,0.25), C4(7,0), D(10,0), all at z = 0 | S1–S5 and BEND1–4: left, right, right, left turns | (1,−1,0), (−1,1,0), (1,1,0), (−1,−1,0) |
| CBPT | A(1.4,0,0), B(0,1.4,0); R = 1.4, centre at the origin | ARC A→B (90°) | (1,1,0) |
| L kink (repair 01, S-2) | As L, but D = (3.248, 4.25, 0): S2 is kinked at C by atan(5e-4) = 4.9999995833e-4 rad, about α_tan/2 | — | — |
| L mitre (refusal) | As L, but D = (3.242, 4.25, 0): kinked by atan(2e-3) = 1.9999973333e-3 rad, about 2α_tan | — | — |
| L reversed | As L, with BEND authored C→B and S2 authored D→C | — | — |

Straights use `y_reference` (0,0,1). Supports are anchors at A, and at D in the "ANCH" cases. One pressure region covers every member, with terminals at A and D.

**Case list.** Each case exists for k = 1 and k = 2 unless noted.

| Family | Variants |
|---|---|
| `U2-L-FREE-*` | P, SEPA, SEPD, PT, PW, ALL, PTW |
| `U2-L-ANCH-*` and `U2-U-ANCH-*` | P, SEPD, PT, PW, ALL, PTW |
| `MECH-CURVED-BEND-EXACT-PRESSURE-ARC-K1/K2` | — |
| `U2-L-KINK-FREE-P-K2`, `U2-L-KINK-ANCH-P-K2` | k = 2 only |
| `U2-L-MITRE-REFUSED-P-K2` | k = 2 only; a refusal control |
| `U2-L-ANCH-ALL-K2-REV` | k = 2 only |

The variants are:
- **P:** pressure only, both terminals transferring.
- **SEPA / SEPD:** the A or D closure `separately_supported_or_compensated`.
- **PT:** plus thermal.
- **PW:** plus self-weight.
- **ALL:** SEPD plus thermal plus self-weight.
- **PTW** (repair 01, S-3): both terminals `transfers_to_wall`, with pressure, thermal and self-weight in one case. This is plan §2's headline case.

**The refusal control** `U2-L-MITRE-REFUSED-P-K2` has `expected: null`. Its `expected_refusal` states:
- the blocking code `PRESSURE_REGION_MITRE_UNSUPPORTED` (provisional, T4-I11 D-D);
- refs `[region, node:C, pipe:BEND, pipe:S2]`;
- θ under the rule θ = atan2(|t_in × t_out|, t_in·t_out), against α_tan = 1e-3 rad (provisional);
- that no values may be published.

Every case records θ per bend-adjacent node in `derived.junction_angles_rad`.

**Transforms.** The core cases are U2-L-FREE-P-K2, U2-L-FREE-ALL-K2, U2-L-ANCH-ALL-K2, U2-U-ANCH-ALL-K2, the CBPT at k = 2, and (repair 01) U2-L-ANCH-PTW-K2. Each also comes as -SKEW, -X5E6, -X7P3E6, -SKEW-X5E6, -SKEW-X7P3E6 and -MM-MPA. In total there are 80 cases.
- **SKEW** rotates by the exact rational matrix (1/25)[[9,−12,20],[20,15,0],[−12,16,15]]. That is the quaternion (4,1,2,2)/5, a rotation of 73.74° about (1,2,2)/3.
- **X…** translates by +5e6 or +7.3e6 m along X.
- **Rounding.** Transformed node coordinates and `y_reference` components are rounded once to binary64. These binary64 values, written as round-trip decimal strings, are exact inputs, and the reference is computed from them.
  - This matters. In the CBPT at X = 5e6 m, the non-dyadic 5000001.4 m changes the tip ux by 2.7e-10 relative.
  - A test must therefore use exactly these coordinates.
- **Gravity stays global −Z.** So a skewed case with weight is a new problem, not a rotation of its base. Only the pressure and thermal parts are rotation-invariant.
  - Checked: u_skew = Q·u_base to 2e-20 m at the origin and 1e-14 m at UTM scale; this is input rounding.
  - The tangent-frame values are identical.
- **Equal to the base, string for string:** dyadic translations, and mm/MPa (whose document is in mm, MPa and N/mm).

**Selected values.**

| Case | Quantity | Value |
|---|---|---|
| U2-L-ANCH-P-K1 | R_A (Fx, Fy, Mz) | 93.887838911971227256 N, 148.44406079533216456 N, 261.55404922027307351 N·m |
| U2-L-ANCH-P-K2 | R_A (Fx, Fy, Mz) | 81.980927267267577685 N, 133.08033915692378938 N, 246.02807106207832682 N·m |
| U2-L-ANCH-P-K2 | BEND end_i: N_w, S, V_y, M_z | 95311.365377621273718 N, −81.980927267267577685 N, −133.08033915692378938 N, 153.21294640869304133 N·m |
| U2-L-FREE-P-K2 | D (ux, uy); every station | 1.9574677597159737203e-4 m, 2.5597655319362733266e-4 m; N_w = P, S = 0, M = 0 |

## 5. The rebuilt CBPT

The retired case is `MECH-CURVED-BEND-PRESSURE-THRUST-ARC`. Its new id, `MECH-CURVED-BEND-EXACT-PRESSURE-ARC-K1/-K2`, records the retired id in `rebuilds_retired_case_id`.

| Quantity | Old (retired fixture, E and G with no ν) | New (E/ν, ν = 0.3; G = 75 GPa derived) |
|---|---|---|
| Tip B: ux, uy (m) | ∓1.080861534560850e-4 | ∓4.3234461382433996858e-5, i.e. ×(1−2ν) = ×0.4 |
| Node-on-element force at B (global) | (−80833.98400998286, 0, 0) N | the same: P·t_B, with P = 80833.984009982862410 N |
| Station N_w (axial) at 0.25, 0.5, 0.75 | +80833.98400998286 N | +80833.984009982862410 N, at every station including the ends |
| S | none | 0 |
| σ_m = N_w/As | none | 1.5054857088526124861e7 Pa |
| V, M, T; reactions at A | 0 | 0 |

The values are k-independent: K1 and K2 are identical.

**Old values.** They are read from the retired hand calculation (`P/validation/hand_calcs/mechanics/curved_bend_pressure_thrust_arc.md:311-325@ec5d397359`). The old tip value is exactly the `poisson_term_missing_on_arc` mutant of the new case (§7).

**The node coordinates** are the binary64 values of 1.4. So the tip is ε_p·(x_B − x_A) for those values, and it differs from ε_p·R·(∓1, ±1) by 6e-17 relative.

**Hoop and radial rows** are withheld on the arc (T4-U2 rule). I4's suggested Lamé rows for this case are not expected.

## 6. Independence and controls

**Polygon limit, with no curved element.** Each arc is replaced by n straight Euler–Bernoulli chords, with kink forces P(t_in − t_out) at every vertex, B and C included, plus the Poisson eigenstrain, thermal and weight per chord. The same unit-load integration is used, on straights only.

At k = 1 this is the brief's control. At k = 2 the chords carry k on their bending energy only, an additional control.

The table gives the normwise difference against the reference, over R_A, R_D and the six displacements of the last node, at n = 8, 16, 32, 64 and 128:

| Case | n = 128 | Ratio per halving | Richardson (64, 128) |
|---|---|---|---|
| U2-L-ANCH-P-K1 | 1.39e-6 | 3.999–4.001 | 8.8e-12 |
| U2-L-ANCH-ALL-K1 | 9.26e-7 | 3.998–4.001 | 7.9e-12 |
| U2-L-FREE-ALL-K1 | 1.06e-7 | 3.997–4.002 | 1.9e-12 |
| U2-U-ANCH-ALL-K1 | 9.59e-7 | 3.998–4.001 | 9.8e-12 |
| U2-L-ANCH-P-K2 | 2.25e-6 | 3.999–4.001 | 6.0e-12 |
| U2-U-ANCH-ALL-K2 | 1.11e-6 | 3.999–4.001 | 5.0e-12 |
| U2-L-ANCH-ALL-K2-SKEW-X7P3E6 | 8.83e-7 | 3.999–4.000 | 4.0e-12 |
| CBPT-K1 (membrane, exact for any n) | 4e-57 | — | — |
| U2-L-ANCH-PTW-K1 (repair 01) | 1.36e-6 | 3.999–4.002 | 8.6e-12 |
| U2-L-FREE-PTW-K1 (repair 01) | 6.04e-7 | 3.998–4.000 | 5.2e-12 |

**Cross-checks only** (`u2_crosscheck.stdout.txt`). The curved-element stiffness is formed from the same arc flexibility and inverted, with H taken from the actual chord. Each check is compared with all 79 cases that carry values; the maximum normwise difference is 4.7e-20, the 20-digit rounding of the file.
- **F1, the plan's H-2 ledger:**
  - the straights' Poisson pairs;
  - the bend term K_b·u_free(ε_p) − c_b;
  - the interior remainders;
  - the caps at transferring terminals;
  - with recovery N_w = N_el + P on arcs and the station membrane +P.

  F1 is checked on displacements, reactions, end rows (straight, and arc in the tangent frame) and stations.
- **The elastic chord-frame rows** are computed directly as K_b(d − u_free(ε_p + ε_th)) − p_uniform from the stiffness solution, not as wall − c_b. They agree to 4.6e-20.
- **F2, Σ K_m·u_free(ε_p):** checked on displacements and reactions.
- **The thermal analogue:** reactions of the ε_p thermal problem against the anchored pressure-only cases, 2.3e-20.

**A second implementation.** T4-RV1's binary64 planar F3 script (`WT/scratch/t4_RV1/h2_check.py`, `5e31dc08…`) was run on its own geometry against this engine. They agree to ≤ 4.9e-13 for k = 1 and 2, anchored, D-separate and pressure plus thermal (`rv1_seed_comparison.stdout.txt`). That is binary64 agreement between two independent codes.

## 7. Negative controls (`wrong_result_discriminators`)

Each control gives its wrong values at JSON pointers into the case, with the distance in units of the case's tolerance. The cases are U2-L-FREE-P-K2, U2-L-ANCH-P-K2, U2-L-ANCH-ALL-K2, U2-U-ANCH-P-K2, CBPT-K2, U2-L-ANCH-PTW-K2 (repair 01), and the two kink cases.

**Listing rule (repair 01, B-1).**
- A control lists only rows at ≥ 1e3 tolerances from the reference: at most 8, ordered by distance as in round 00.
- A computed wrong value below 1e-40 of its group's zero scale is written as exact 0.
- `max_distance_in_tolerances` is the maximum over every row the control evaluated, and it is unchanged.
- The 23 round-00 rows that failed the rule are kept with their reasons in `rows_dropped_repair_01`. These are not assertions:
  - 20 rows in U2-L-FREE-P-K2 and CBPT-K2, where the wrong value equals the reference or differs from it only by 1e-54-level noise;
  - 3 rows in the kink case, where a 0 equals the reference or the Fy distance falls below 1e3 tolerances.

| Control (how it was emulated) | Maximum distance (tolerances) | Example (case: pointer, wrong vs reference) |
|---|---|---|
| Bend term omitted: no arc wall load or arc Poisson term. The residual of the applied set is −P(t_i − t_j), which the file records | 5.7e10 to 4.0e12 | L-ANCH-P: R_A Fx 95278.70 vs 81.98 N |
| c_b added instead of subtracted: +2c_b at the bend nodes | 1.1e11 to 8.1e12 | L-FREE-P: D ux −2.07 m vs 1.96e-4 m |
| Caps subtracted in recovery: published N_w = S | 1.0e9 | L-FREE-P: S1 N_w 0 vs 95393.35 N |
| Poisson term missing on the arc | 8.4e6 to 1.5e9 | CBPT: tip ux −1.0808615e-4 (the legacy value) vs −4.3234461e-5 m |
| Wall load double count (a): elastic end force, with the wall load in the station statics, plus P | 1.0e9 to 1.9e12 | L-ANCH-P: BEND end_i V_y −95526.43 vs −133.08 N |
| Wall load double count (b): wall end force, with the wall load in the statics, plus P again | 1.0e9 | N_w + P at every arc station |
| Non-tangent bend at atan(5e-4) rad, remainder omitted at C | 3.3e8 to 3.4e8 | L-KINK-FREE-P: D ux 1.1053e-4 vs 1.9563e-4 m; remainder (47.697, 0.01192, 0) N |

With the remainder in place, the kinked free L stays balanced, with zero reactions and the self-similar growth. This is the control the brief requires.

## 8. Criteria and transport

**The criterion.**
- In both solver modes: |observed − expected| ≤ 1e-9·max(|expected|, zero_scale).
- zero_scale is set per case and per group, and every case lists it with its floor.
- The groups are displacement, rotation, support force and moment per support, wall axial force, effective force, membrane stress, shear, section moment, bending and torsion stress, Lamé, and the elastic chord-frame end force.
- zero_scale is the group's maximum |expected| in the case. Where the group is identically zero, a characteristic scale is used instead: P (or W_total), P·L_c, |ε_p + ε_th|·L_c, |ε_p + ε_th|, or P/As.
- Each control's maximum distance is between 8.4e6 and 8.1e12 tolerances. Every listed row lies at ≥ 1e3 tolerances (B-1).
- The floors exceed binary64 noise in the product by an estimated three orders of magnitude or more (I).

**`u2_reference_cases.json`** (schema `independent.exact_pressure_bend_examples/1.0.0`).
- Values are decimal strings of 20 significant digits.
- Pointers follow `/cases/<id>/expected/{nodes,supports,terminals,members/<pipe>/{stations,end_rows,lame_surface,arc,frame}}`.
- A later `exact_pressure_1` generator can read them at pointers, as T1's `load_reference_1` reads `reference_cases.json`. Units are given by key in `units_by_key`.
- The file also holds the `polygon_limit_control` block and the negative controls.

**`u2_document_sketches.json`.** It holds a 0.3.0 and a 0.4.0 document per case, one case per line, built on the shapes of the T1 package and the PP exact-pressure tests.
- **0.3.0:** thermal is a `thermal` primitive (ΔT in °C), with the material's α.
- **0.4.0:** thermal is a `constant_alpha_interval` thermal state, weight is a load source with factor 1.0, and the member references use `direct_strain_reference` with no fit.
- **Provisional,** and listed per sketch:
  - the v3 `pressure_contract` spelling (T4-U2a);
  - a bend pipe in a region, and the bend component on the exact route (T4-U2a/U2);
  - the bend's per-member E/ν in 0.4.0 (T4-U1).

## 9. Limits and points for the refuter

1. **Linear and small-displacement.** U2-L-FREE-SEPD and -ALL give tip motions of about 1 m and 0.24 rad. That is valid linear algebra, but not physical. Keep the cases or scale p down; the values are linear in each load.
2. **The tangency tolerance** (repair 01). The kinks sit near α_tan/2 and the refusal control near 2α_tan, under the WI's rule with α_tan = 1e-3 rad (provisional).
   - If α_tan changes, edit `ALPHA_TAN` and `KINK_DX` in `u2_generate.py` and regenerate.
   - T4-U2 must not snap sub-tolerance kinks to tangency (RV3 N-4).
3. **Not covered here:**
   - guides, springs, nonlinear supports;
   - an S-shaped (out-of-plane) chain;
   - reducers and tees;
   - external pressure;
   - geometry-only bends, which are refused under D-2 and listed in the plan's U0/U2a controls.
4. **Symmetry.** The U-loop's anchors are asymmetric (D at x = 10 m), so no in-plane reaction component vanishes by mirror symmetry. Out-of-plane components vanish only in the planar pressure and thermal cases.
5. **Discrimination of SEPD.** With D anchored, a separately supported closure at D changes only R_D. The SEPD value discriminates only in the free family.
6. **The zero-scale grouping is my reading of I4 §5 and the brief.** Refute it if a per-member grouping is wanted.
7. **The sketches were not deserialized by the product.** No cargo was run, and the provisional fields have no DTO yet.
