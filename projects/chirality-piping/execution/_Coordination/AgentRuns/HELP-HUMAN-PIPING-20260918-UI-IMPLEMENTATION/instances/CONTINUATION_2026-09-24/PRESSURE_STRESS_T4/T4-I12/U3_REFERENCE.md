# T4-I12: independent references for T4-U3, the corrected joint (freeze)

- **Role:** TASK (Type 2) for T4's WORKING_ITEMS. Brief `R4/BRIEFS/T4-I12_U3_REFERENCES.md` (sha256 `1c7bb2f1…eba873`); terms `R4/BRIEFS/T4_WI_COMMON.md` (sha256 `7d44afd0…902cb`), both at `471ad93f48`. Rulings applied: annotation-only joints are not admitted on the exact route; the connector topology is `replaces_span` only.
- **Status:** frozen before any T4-U3 code; awaiting the refuting TASK. Not product evidence.
- **Independence:** every connector value is re-derived from JR's definitions (`I/CORRECTNESS_DESIGN/JOINT_REFERENCE/CONTRACT.md` §2, sha256 `4f3fd302…`) in exact rationals. No connector code exists; no value is taken from the old element. The product was read only for conventions (`@ed012c7ccf`: section, frame, loads, reactions, supports) and, for item 8, for NI's active-set algorithm.
- **Files:** `u3_reference_cases.json` (authoritative; 18 cases), `_run_records/u3_reference.py` + stdout (761 checks pass; 75 JR comparisons), `_run_records/check_reference_json.py` + stdout (508 consumer checks pass, by a different formulation), `_run_records/probe_binary64.py` + stdout (informational).
- **Reproduce:** from `R4/T4-I12/_run_records/`: `WT/venv/bin/python -I u3_reference.py ../u3_reference_cases.json`, then `… check_reference_json.py ../u3_reference_cases.json` and `… probe_binary64.py ../u3_reference_cases.json`.

## 0. Findings for the plan

1. **No stop rule (SP-1 to SP-4) is triggered and no T3 condition is touched.** Nothing here changes a tolerance, a pin or a reviewed input.
2. **JR agrees (fact, 75 comparisons).** Every numerical statement re-derived here agrees exactly: J1, the common-rotation zero, J2 and its held variant, the refutation's end-moment and pure-qrz controls, the B oracle (12 end-block entries, q for d_k = (k−4)/17, virtual work 1567/170), the coupled H (0.075 J, 0.25 N, 1 N·m), the Ls 2 → 1 rescaling (1, 0.5, 9), the preload residual ([+0.25, −0.25] N, [+1, −1] N·m), the historical six components and the historical raw mutation (0.4 N, 0.004 J).
   **One partial agreement (a finding, not a mathematical disagreement):** the refutation's finite-rotation decimals at L = 2 m, φ = 0.1 (`−0.00999166944394836`, `−0.000333166706343702`) agree to 13 significant digits only. They carry binary64 cancellation error in cos φ − 1 and sin φ − φ (differences 1.1e-16 and 6.6e-18 m). The exact values, `−0.0099916694439484678…` and `−0.00033316670634369539…`, are frozen here.
3. **The 658.44 N·m is historical and not reproducible on the exact route (fact).** It came from the legacy demo's L-100, which carries pressure, nonlinear supports and the deleted element (`PP/tests/preview_physics_runtime.rs:1036-1043`). All of those are refused under v3. In the v3 re-authoring, the deleted element's raw-difference measure would leave **770 N·m about global X (L-100), 275 N·m (L-200) and 440 N·m about global Y (L-300)** unbalanced. The connector balances exactly. These are the case's discriminators.
4. **The demo must shed most of its content to run on the exact route (fact, from the profile).** Dropped: the bend, branch, valve and terminal markers (D-2; components refused), NL-140 and NL-130-FRIC (T5), CE-120 (constant effort), every pressure load (joint pressure is T4-U5), and the combination (T6). The demo's own cases load only q_tx, q_ty and q_rz. A labelled coverage case, **L-300**, is added so that all six coordinates pass through PP.
5. **Admission is inferred, not run.** The following are read from code and must be confirmed on the first run: a `variable_spring_hanger` as a linear spring, a 0.3.0 `thermal` primitive, nodal `occasional` forces and moments (`rotation_y`, `rotation_z`, dimension `moment`), and right-angle corners between straights in unpressurized v3 cases.
6. **NI's replacement keeps the fixture's own frame section (inference, proposed).** That section is `FrameSection::new(100, 40, 1, 1, 1, 1)`, `:3123`. Node 1 moves to (3, −4, 0), with cosines (3/5, −4/5). Every structural property of the four call sites is preserved: iteration counts, the sign flip, the cap and the zero coefficient. The constants change (§5).
7. **Out of scope:** JR J3 and J4 (pressure and ties) belong to T4-U5 and are not frozen here. Series and parallel topologies are refusals under the ruling. The historical oracle's series and parallel cases are therefore not frozen.
8. **Provisional wire:** `3.0.0/exact_pressure_v3` and the connector record's `calibration`, `hardware` and `pressure_model` field names are proposals. T4-U2a and T4-U3 fix them. The numeric content is binding.

## 1. Conventions (JR §2; the reference's sign choices)

| Item | Convention |
|---|---|
| DOFs | d = [uᵢ, θᵢ, uⱼ, θⱼ], global; m and infinitesimal rotation vectors (rad), right-handed |
| Q | row-major 3×3 whose **columns** are the connector axes; proper; for r ≠ 0, Q.x = r/\|r\| |
| r | r = (xⱼ + aⱼ) − (xᵢ + aᵢ); aₖ = Qₖ·offset_localₖ |
| q | qt = Qᵀ[(vⱼ − vᵢ) − θc × r], qr = Qᵀ(θⱼ − θᵢ), vₖ = uₖ + θₖ × aₖ, θc = (θᵢ + θⱼ)/2 |
| K, H | H = DKD, D = diag(Ls, Ls, Ls, 1, 1, 1); 21-entry upper triangle (0,0)…(0,5), (1,1)…(5,5); K = D⁻¹HD⁻¹ |
| g, U | g = K(q − q_ref) local; U = ½(q − q_ref)ᵀK(q − q_ref) |
| End actions | f = Bᵀg, **node-on-element** (the element's internal force vector); element-on-node is −f. F = Q g_t, M = Q g_r; Fᵢ = −F, Fⱼ = F, Mᵢ = −(aᵢ + r/2) × F − M, Mⱼ = (aⱼ − r/2) × F + M |
| Installed state | the RHS gets +BᵀKq_ref; the internal action at d = 0 is −BᵀKq_ref; Ke·d = f_ext + BᵀKq_ref + R |
| Reactions | support-on-pipe, global Fx…Mz; a spring's is −k·u |
| Reversal | J = diag(−1, 1, −1); Q′ = QJ; attachments and ids swapped; T = blockdiag(−J, −J); q′ = Tq, q_ref′ = Tq_ref, K′ = TKTᵀ, H′ = THTᵀ at the same Ls |
| Numbers | exact rationals as strings (authoritative) plus decimals; π-dependent and transcendental values as 30–40-digit decimals |

## 2. Method

- **Exact rationals throughout** (`fractions`). B is formed twice: once in closed form, and once column by column from the kinematic definition on the 12 basis vectors. They agree in all 72 entries for every geometry.
- **End actions are formed twice:** as Bᵀg and as the closed-form blocks. Each case checks:
  - rank B = 6;
  - B·(rigid motion) = 0 and Ke·(rigid motion) = 0 for the 6 rigid motions of the actual nodes, about origin 0 and about (7, −3, 5);
  - the end-action force and moment sums about three origins;
  - virtual work;
  - Ke·d − BᵀKq_ref = Bᵀg;
  - the self-equilibrium of BᵀKq_ref (S13: `self_equilibrated = true`).
- **The consumer check uses a third formulation.** It rebuilds q from rigid arms to a common midpoint and f from the transposed arms, using only the JSON inputs.
- **The system solve** (item 6) is a direct-stiffness solve in rationals, with π as a 125-decimal Machin rational. It is stable to 95 digits against a 115-decimal π. Frame-sign self-tests cover rigid modes in null(K), cantilever tip deflection and rotation under a point load, and consistent uniform load.
- **The product conventions read** (`@ed012c7ccf`):
  - section: As = πt(OD − t), I = As(ro² + ri²)/4, J = 2I (`PP/src/lib.rs:7244-7259`);
  - G = E/(2(1 + ν)) from the E/ν pair (`pressure_exact.rs:236-252`, applied at `pressure_material.rs:60-95`);
  - Euler–Bernoulli local stiffness (`FK/src/lib.rs:712-815`);
  - local axes from y_reference (`:526-540`);
  - thermal pair ±E·As·α·ΔT along local x (`PP/src/lib.rs:10668-10773`);
  - spring hanger as a linear spring (`:7388-7404`);
  - exact profile refusals (`pressure_runtime.rs:157-215`).

## 3. Cases (`u3_reference_cases.json`)

| Case | Item | Content and key values |
|---|---|---|
| `U3-J1-LATERAL` | 1 | r = 0.3 eₓ, Q = I, K = diag(2e5, 8e4, 1.2e5, 600, 900, 1200), Ls = 1 m; uⱼ_y = 1 mm → q_y = 0.001, g_y = 80 N, U = 0.04 J, Fᵢ_y = −80, Fⱼ_y = 80, Mᵢ_z = Mⱼ_z = −12 N·m |
| `U3-J1-COMMON-ROTATION` | 1, 7 | ω_z = 0.01 on both nodes, uⱼ_y = 0.003: q = 0, U = 0, actions 0. Raw difference: 0.003 m, 240 N, 0.36 J |
| `U3-J2-ROTATION` | 1 | θⱼ_z = 0.01, uⱼ_y = 1.5 mm: qt = 0, qr_z = 0.01, g_mz = 12 N·m, U = 0.06 J; Mᵢ_z = −12, Mⱼ_z = 12 |
| `U3-J2-ROTATION-HELD` | 1 | uⱼ_y = 0: qt_y = −1.5 mm, g_y = −120, g_mz = 12, U = 0.15 J; Mᵢ_z = 6, Mⱼ_z = 30 = (krz + ky L²/4)φ (refutation §1; the beam limit gives 4EI/L) |
| `U3-REF-ENDMOMENT` | 1 | refutation §1 (L = 2, ky = 20, krz = 60): Fⱼ_y = −0.2, Mᵢ_z = −0.4, Mⱼ_z = 0.8, 0.004 J; pure qrz: 0.6 N·m, 0.003 J |
| `U3-SIX-COMPONENTS` | 1 | historical base: L = 2, Kc = diag(10…60), Ls = 2 (H = 40, 80, 120, 40, 50, 60); each coordinate isolated at 0.01 |
| `U3-B-ORACLE` | 2 | refutation §6: B (72 entries), Fᵢ = (−2, 3, −5), Mᵢ = (−42/5, 87/5, −43/5), Fⱼ = (2, −3, 5), Mⱼ = (10, −9/2, 157/10); q(d_k) = (73/170, −26/85, 29/34, 6/17, 6/17, 6/17); work 1567/170 |
| `U3-GENERIC-SKEW-OFFSET-PRESTRESS` | 3, 4 | Q columns (1,2,2)/3, (2,1,−2)/3, (−2,2,−1)/3; aᵢ = (1/5, 2/5, −1/5), aⱼ = (−1/10, 3/10, 1/2), r = (1, 2, 2); a fully coupled PD K (exact pivots all > 0), Ls = 0.25; q_ref ≠ 0; a generic d. Gives B, Ke exactly, q, g, U = 22666357/3240000 J, the four blocks and the RHS. Discriminators: offsets ignored, Q transposed, residual omitted. S8: Ke(2ᵇK) = 2ᵇKe exactly |
| `U3-W4-LINK-RULE` | 3 | PD: rank Ke = 6, null = the 6 rigid modes (links). PSD (JR 4/1/9 only): rank 2, null dimension 10, with the non-rigid null vector d = [0, 0, Q.y, 0] (pure qt_y) → `ConnectorSemidefinite`. A null-coordinate q_ref is stress-free. Indefinite H (4, 5, 4): pivot −9/4 → reject, never project |
| `U3-FRAME-COVARIANCE` | 4 | the generic case under R = 90° about z, t = (7, −3, 5): q, g, U unchanged; the four blocks rotate with R |
| `U3-OFFSETS` | 4 | historical offset case: local offsets (0, 0.2, 0) at both ends with identity triads; q, g, U = 29347/2400000 J, blocks |
| `U3-COUPLED-H-SCALE-PRELOAD` | 4 | H00 = 4, H03 = 1, H33 = 9, Ls = 2: U = 0.075 J, g_tx = 0.25 N, g_rx = 1 N·m; Ls = 1 m: H′ = (1, 0.5, 9), the same K; 2000 mm ≡ 2 m. Preload q_ref = (0.2, 0, 0, 0.1, 0, 0) at d = 0: f = [+0.25, −0.25] N and [+1, −1] N·m, U = 0.075; RHS = −f |
| `U3-PRELOAD-RELIEF` | 4 | a PD variant: node i anchored, node j free → d_j = (1/5, 0, 0, 1/10, 0, 0), q = q_ref, g = 0, reactions 0. uⱼ_x held → q = (0, 0, 0, 1/9, 0, 0), g_tx = −7/36, U = 7/360. Both held → R = −BᵀKq_ref |
| `U3-REVERSAL` | 4 | the canonical reversal of the generic case: q′ = Tq, g′ = Tg, U′ = U, blocks exchanged, H′ = THTᵀ. Discriminator: ids swapped with K and q_ref untransformed |
| `U3-FINITE-ROTATION-NEGATIVE` | 5 | (L, φ) = (2, 0.1), (0.3, 0.01), (2, 0.5): qt = [L(cos φ − 1), L(sin φ − φ), 0] to 40 digits; never zero, never suppressed |
| `U3-RAW-DIFFERENCE-NEGATIVE` | 7 | analytical raw values the product must never produce (240 N, 0.36 J; 0.4 N, 0.004 J); the correct values are exact zeros with floors |
| `U3-SYS-DEMO-CONNECTOR-001` | 6, 7 | §4 |
| `U3-NI-FRICTION-FRAME` | 8 | §5 |

## 4. The system case (`U3-SYS-DEMO-CONNECTOR-001`)

**Model.** The JSON holds the full 0.3.0 v3 document.
- **Geometry:** the demo's nodes N-100 (0, 0, 0), N-110 (3.2, 0, 0), N-120 (3.2, 2.4, 0), N-130 (7.6, 2.4, 0) and N-140 (7.6, 2.4, 2.2); pipes P-100 to P-130 with OD 0.168 and wall 0.007.
- **Material:** E = 2e11 Pa, ν = 0.3 (the demo's G = 77 GPa is not used), α = 1.2e-5.
- **Supports:** S-100 anchor; S-120 guide UX, UZ; S-130 guide UY; SH-140 spring UZ, 42000 N/m.
- **Load cases** (`pressure_regions: []` in each):
  - L-100: −190 N/m on P-120 in z, 350 N at N-140 in y, and +12.5 °C on P-120;
  - L-200: −95 N/m and 125 N;
  - L-300 (added): at N-140, 200 N in x, −80 N·m about y and 150 N·m about z.

**Connector C-150.**
- `replaces_span pipe:P-130`; nodes i = N-130 and j = N-140; offsets 0.
- Q columns (e_z, e_y, −e_x): x along r = (0, 0, 2.2), y = P-130's y_reference.
- K = diag(3.2e6, 9e5, 9e5 N/m; 6.2e5, 4.8e5, 4.8e5 N·m/rad). This is the four demo rates, explicitly authored as an uncoupled isotropic law; it is not a migration.
- Ls = 0.5 m, so H = diag(800000, 225000, 225000, 620000, 480000, 480000) N·m.
- q_ref = 0, stress-free; untied; unpressurized.

**Results** (30 digits in the JSON; reactions are support-on-pipe, end actions node-on-element):

| | L-100 | L-200 | L-300 |
|---|---|---|---|
| S-100 Fx, Fy, Fz | 0, 0, −344.622942721 | 0, 0, −134.099169894 | 42.5156400206, 43.6411015547, −9.95791399949 |
| S-100 Mx, My, Mz | −57.0950625303, 379.226785186, 0 | −46.8380077445, 85.7032465471, 0 | −23.8989935988, −44.9433851844, 79.6348357665 |
| S-120 Fx, Fz | 0, 927.069904430 | 0, 421.147828328 | −242.515640021, −54.4037428226 |
| S-130 Fy | −350 | −125 | −43.6411015547 |
| SH-140 Fz | 253.553038291 | 130.951341565 | 64.3616568221 |
| g (local) | 253.553038291, 350, 0, 0, 0, 385 | 130.951341565, 125, 0, 0, 0, 137.5 | 64.3616568221, 0, −200, 150, 140, 0 |
| Fᵢ at N-130 / Mᵢ | (0, −350, −253.553…) / (770, 0, 0) | (0, −125, −130.951…) / (275, 0, 0) | (−200, 0, −64.3617…) / (0, −360, −150) |
| Fⱼ at N-140 / Mⱼ | (0, 350, 253.553…) / 0 | (0, 125, 130.951…) / 0 | (200, 0, 64.3617…) / (0, −80, 150) |
| U (J) | 0.232501775851 | 0.0310539806375 | 0.0614313037525 |

- **Balance:** applied loads plus reactions sum to zero, force and moment about the origin. The residual is below 1e-100 in the reference, and the consumer check reproduces it from the frozen 30-digit values to 1e-25. The thermal expansion of P-120 is unrestrained (N-130 moves exactly 0.66 mm in x), so it produces no connector force.
- **Discriminators:**
  - The raw-difference element (same K and Q) gives a global moment imbalance of −770 / −275 N·m about X and +440 N·m about Y, and different S-100 Fz, Mx, My, S-120 Fz and SH-140 Fz.
  - P-130 retained in parallel (no `replaces_span`) changes the same five components; for example, L-100 S-100 Fz becomes −344.0889.
  - Each discriminator is asserted only on its listed components.
- **Refusal variants:**
  - A weight or a thermal on P-130 → `JOINT_REPLACED_SPAN_LOAD_UNOWNED`, with refs including C-150, P-130 and the load. There is no result and no relocation.
  - Any non-empty `pressure_regions` → `JOINT_PRESSURE_INTERFACE_UNRESOLVED`.
  - C-150 as annotation-only → refused on the exact route, never analysed as pipe. The code is T4-U3's choice.
  - Series or parallel topology → `OBJECTIVE_CONNECTOR_TOPOLOGY_UNRESOLVED`.

## 5. NI's four friction call sites (item 8)

**Replacement.** In `coupled_normal_friction_problem`:
- `input.elements = vec![FrameElement::new(node0 (0, 0, 0), node1 (3, −4, 0), FrameSection::new(100.0, 40.0, 1.0, 1.0, 1.0, 1.0), [0.0, 1.0, 0.0])]`;
- the user element list becomes the empty connector list.

Everything else is unchanged: μ = 0.30, the derived normal from node 1 Uy, the restraints, the forces and the seeds. EA/L = 20 and 12EI/L³ = 48/5, so the node-1 block is Kxx = 1668/125 and Kxy = −624/125. The block is the same for y_reference (0, 0, 1), because Iy = Iz.

**Algorithm model.** The model was read from `NI/src/lib.rs@ed012c7ccf` (608-780, 1370-1500, 1560-1660, 1737-1771, 2348-2410) and `nonlinear_supports` 644-670. It reproduces all 20 values pinned for the old block (12 distinct magnitudes) (7/135, 200/27, …, −70/33), plus the iteration counts and the cap. The old block was used only for this validation.

| Call site | Asserted value | Old | **New (exact)** |
|---|---|---|---|
| :3770, (10, −10) | u, normal, friction | 7/135, 200/27, −20/9 | **4375/7404, 4350/617, −1305/617** |
| :3770, (−10, −10) | u, normal, friction | −7/165, 400/33, 40/11 | **−4375/9276, 9550/773, 2865/773** |
| :3907, (10, −1) retry | u, applied = Rx, Ry | 97/1350, 7/9, −70/27 | **12125/14808, 1143/1234, −1905/617** |
| :3907, (10, −1) final | u, friction, normal | 103/1650, −7/11, −70/33 | **12875/18552, −1143/1546, −1905/773** |
| :3907, (−10, 1) | all of the above | sign-reversed | **sign-reversed** |
| :3955 (cap 2) | not converged, blocked, 2 iterations, "derived-normal" | holds | **holds** |
| :4251 (μ = 0) | converged, no applied force | holds | **holds** (2 iterations; u = 625/834) |

Iteration counts are unchanged: 2 in test 1 for both seeds, and 3 in test 2. The test-2 retry is Sliding with a sign-flipped normal; the final iterate has friction·u < 0 and |friction| = 0.30·|normal|. The tolerance stays 1e-12. The JSON gives each value exact, as a decimal and as the nearest binary64.

## 6. Criteria

- **FK unit level:** the identities are exact in rationals (B, Ke, rank, null space, self-equilibrium, reversal, covariance). Product values are compared at relative 1e-12, bitwise where every operand is binary64-exact. Finite rotation: |obs − exp| ≤ 1e-12·L, because d comes from binary64 cos and sin.
- **System:** both modes, one reference. Each value must satisfy |obs − exp| ≤ 1e-9·max(|exp|, floor). The per-family floors are the case's largest magnitudes, listed in the JSON: force, moment, translation, rotation, q_t, q_r, g_t and g_r. Displacement rows are published in mm.
  - Balance: |ΣF| ≤ 1e-9 × the force floor, and |ΣM₀| ≤ 1e-9 × the force floor × 8.27 m.
  - The binary64 probe (naive elimination, no equilibration) meets the criterion with a worst normalized error of 3.1e-14.
- **NI:** absolute 1e-12, unchanged. No new threshold anywhere.

## 7. Limits and points for the refuter

- **The physical envelope is JR's:** small displacement and rotation, reference geometry, constant K, no geometric stiffness. Finite objectivity is explicitly not claimed (`U3-FINITE-ROTATION-NEGATIVE`).
- **The system values are rational functions of π, given to 30 digits.** The demo's inputs (0.168, 0.007, 3.2, 2.4, 2.2, 0.3, 1.2e-5) are not binary64-exact; the criterion absorbs this.
- **The system end actions follow §1's node-on-element sign.** T4-U3 maps them to its published rows (`connector_endpoint_*_v1`) and must state any sign change.
- **Inferred, not run:** that the v3 document passes admission (§0.5).
- **Not frozen here:**
  - J3 and J4;
  - series and parallel topologies;
  - a 0.4.0 form of the system case. Under load-reference-1, the replaced span's element state needs a T4-U3 decision.
- **The NI expectations depend on the algorithm model's reading of the code.** The model reproduces every old constant exactly; a refuter should re-derive it independently from the cited lines.
