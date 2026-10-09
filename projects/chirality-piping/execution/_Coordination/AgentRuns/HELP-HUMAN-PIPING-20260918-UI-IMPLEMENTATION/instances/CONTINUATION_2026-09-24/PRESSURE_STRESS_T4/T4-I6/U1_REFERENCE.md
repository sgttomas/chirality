# T4-I6 Part B: frozen references for T4-U1 (the objective curved formation)

TASK T4-I6 (Type 2) for T4's WORKING_ITEMS. Brief `R4/BRIEFS/T4-I6_U0_U1_REFERENCES.md`; terms `R4/BRIEFS/T4_WI_COMMON.md`. Frozen for refutation before any T4-U1 code is read.

- **Values:** `R4/T4-I6/u1_reference_cases.json`. **Scripts and outputs:** `R4/T4-I6/_run_records/`.
- **Citations:** code `path:line@ed012c7ccf`; T3 records at NUM `70aa51b076` (`RR` = T3's rulings at that commit).
- `CB` = `P/core/solver/curved_bend/src/lib.rs`; `KM` = `NI/src/structural_adapter/kd5_models.rs`; `KT` = `NI/src/structural_adapter/kd5_tests.rs`; `FCR` = `PP/tests/formation_check_runtime.rs`.
- **F** = read from bytes or computed by the recorded scripts. **I** = inference.
- **Independence.** The element below is derived from first principles and checked by an independent quadrature. Product code was read for conventions only: frames, DOF order, PP's `y_reference` side, inputs and stations. Comparisons with today's code, with CB's longhand and with T3's D1 references are labelled cross-checks.

## B1. The intended element, defined mathematically

**Inputs (all binary64, used as exact reals):**
- the nodes x_i, x_j: i is the pipe's `from` node, j its `to` node;
- the user radius R;
- the plane reference y: the pipe `y_reference`;
- E, and G = E/(2(1+ν)) on the exact route (the product's binary64 G differs by at most 1 ulp, a relative effect below 1e-16);
- A, and I (the same about both bending axes), and J;
- k_in and k_out (PP passes the one user factor as both).

**Geometry (exact).** Nothing else enters; no absolute centre is formed.

| Quantity | Definition | Condition |
|---|---|---|
| d, L | d = x_j − x_i (exact in binary64 when the coordinates are within a factor 2, or on a common grid, B3), L = \|d\| | L > 0 |
| s = sin(φ/2) | L/(2R) | R > L/2 (PP refuses R ≤ L/2 today, `PPL:7783-7793`) |
| c = cos(φ/2) | √((2R−L)(2R+L)) / (2R) | — |
| φ | 2·atan2(s, c) ∈ (0, π) | product domain `[1e-9, π−1e-9]` (`CB:27,165-169`) |
| d̂, n̂ | d̂ = d/L; n̂ = (y − (y·d̂)d̂)/\|…\| | \|y − (y·d̂)d̂\| > 0 (PP's tolerance 1e-9, `PPL:7830-7837`) |
| local axes (rows of A) | e_x = −s·d̂ + c·n̂ (radial at i, outward); e_y = c·d̂ + s·n̂ (tangent at i, toward j); e_z = n̂ × d̂ (plane normal) | the arc bows toward +n̂, PP's convention (`PPL:7760-7765`) |
| chord in the local frame | c_loc = A·d = (−sL, cL, 0) | identical to R(cos φ − 1, sin φ, 0), proved in B5.3 |
| trigonometry | sin φ = 2sc; cos φ = 1 − 2s²; sin 2φ = 2 sin φ cos φ | square roots only; one arctangent, for φ itself |

**F:** these axes equal today's `CB:171-177` frame (x = r_i/R, z ∝ r_i × r_j) in exact arithmetic. The cross-check is `selftest.stdout.txt`, axes for CB's quarter circle.

**The tip flexibility F (6×6, node i clamped, local frame, DOF order [ux, uy, uz, rx, ry, rz]).**
- Arc point P(θ) = R(cos θ, sin θ, 0) about the (virtual) centre, θ ∈ [0, φ], with node j at θ = φ.
- For a unit generalized load f_a at j (force F or moment M), the section at θ carries the force F and the moment M(θ) = M + (P(φ) − P(θ)) × F.
- The actions are N = F·t, T = M(θ)·t, M_ip = M(θ)·ẑ and M_op = M(θ)·e_r, with t = (−sin θ, cos θ, 0) and e_r = (cos θ, sin θ, 0). Shear deformation is excluded, as the CB README declares.
- Each action is a coefficient triple on the basis b(θ) = (1, cos θ, sin θ):

| Load | N | M_ip | M_op | T |
|---|---|---|---|---|
| Fx | (0, 0, −1) | (−R sin φ, 0, R) | 0 | 0 |
| Fy | (0, 1, 0) | (R cos φ, −R, 0) | 0 | 0 |
| Fz | 0 | 0 | (0, R sin φ, −R cos φ) | (R, −R cos φ, −R sin φ) |
| Mx | 0 | 0 | (0, 1, 0) | (0, 0, −1) |
| My | 0 | 0 | (0, 0, 1) | (0, 1, 0) |
| Mz | 0 | (1, 0, 0) | 0 | 0 |

- F_ab = R · [k_in·q(M_ip,a, M_ip,b)/(EI) + k_out·q(M_op,a, M_op,b)/(EI) + q(T_a, T_b)/(GJ) + q(N_a, N_b)/(EA)], where q(u, v) = uᵀ𝒢v.
- 𝒢 = ∫₀^φ b bᵀ dθ:

  | | 1 | cos θ | sin θ |
  |---|---|---|---|
  | **1** | φ | sin φ | 1 − cos φ |
  | **cos θ** | sin φ | φ/2 + sin 2φ/4 | sin²φ/2 |
  | **sin θ** | 1 − cos φ | sin²φ/2 | φ/2 − sin 2φ/4 |

- **Stiffness:** K_t = F⁻¹. The local 12×12 is K_loc = [[H K_t Hᵀ, −H K_t], [−K_t Hᵀ, K_t]], with H = [[I₃, 0], [skew(c_loc), I₃]] and skew(c)v = c × v.
- **Global:** K = Tᵀ K_loc T, with T = diag(A, A, A, A). This is FK's convention (`FK/src/lib.rs:542-552,1279-1285,1780-1799`). Order: node i then node j.

**Properties (exact).**
1. K is symmetric positive semidefinite with rank 6. For any K_t, its null space is exactly the six rigid motions of the actual nodes.
   - Proof: for a rigid motion (t + ω × x, ω), Hᵀ u_i − u_j = (ω × (c_loc − A d), 0) = 0, because c_loc = A·d and A is orthogonal.
2. K depends on (d, R, y) only, so it is invariant under translation.
3. K(Qx, Qy) = Q K(x, y) Qᵀ for every proper rotation Q.
4. At k = 1, as φ → 0 with fixed L, K tends to the Euler–Bernoulli frame on the chord. The difference is O(φ): 2.4e-10 at φ = 1e-8 (`freeze_u1.stdout.txt`, column "straight").

**Checks.**
- **F, longhand:** F agrees with CB's quarter-circle longhand (`CB:1093-1175`) to 1e-110 (labelled cross-check).
- **F, quadrature:** F agrees with an independent 40-point Gauss–Legendre quadrature that forms the actions directly from vectors, to 1e-110 (`selftest.py`).
- **F, T3's references:** T3's D1 objective re-formation (`KM` u_int) is reproduced. Old against new reference: E1 5.0e-8, E6 6.8e-8 and CSKEW_8_5 5.8e-8 of the criterion (labelled cross-check; B4).

**For K-D5 and W1c to re-form it.**
- The input set changes from today's `center` (`FC:47-60`; `CurvedFormation`) to (R, y_reference). SA's slot matching and its `curved_formation` trace change with it (T4-I2 §1.5–1.6).
- H must use c_loc = A·d. The formula form is identical only in exact arithmetic (B5.3).
- **F, precision at p = 128:** the closed forms above at about 128 bits (decimal 38) give these relative errors in K (`p128_closed_form_precision.stdout.txt`):

  | φ | Relative K error |
  |---|---|
  | 1e-4 | 1.8e-26 |
  | 1e-8 | 4.0e-14 |
  | 1e-9 (the lower limit) | 4.5e-11 |

- **I:** at 1e-9 that error, multiplied by a model's condition number (about 2e3 for B5's cantilever), can reach the criterion. A K-D5 re-formation near the lower limit (φ ≲ 3e-9) then risks a false demotion unless it uses series or a higher p (open point O4). At 1e-8 the effect is about 0.1 of the criterion.

**Numerical requirements this definition puts on the product.** These are inferences from a naive binary64 evaluation of this definition, done by this record's own code, not product code (`freeze_u1.stdout.txt` "naive sweep").
- **Small angles.** The closed-form Gram cancels.
  - A naive binary64 evaluation misses the 1e-9 matrix-scale agreement below about φ ≈ 4e-3 rad: 2.8e-10 at 5e-3, 2.2e-9 at 3e-3, 3.0e-4 at 1e-4 and 4.2 at 1e-8.
  - T4-U1 must evaluate F without cancellation at small φ, for example by series. B2's 1e-4 and 1e-8 cases and B5's kill model require it.
- **Near π.** A naive evaluation meets the criterion at π − 1e-6 and π − 1e-7 (1.2e-10 and 3.9e-10).
  - With binary64 L, ε = π − φ cannot be formed reliably below about √(8u) ≈ 3e-8, because s rounds toward 1.
  - Forming 4R² − |d|² exactly (d is exact) removes this.

## B2. Frozen values (`u1_reference_cases.json`, `cases`)

- **49 elements:**
  - 6 angles: 90°, 45°, 5°, 1e-4 rad, 1e-8 rad (ten times the lower limit) and π − 1e-6;
  - × 2 planes: IP = global XY (d̂ ∝ (cos 30°, sin 30°, 0), y = (0,1,0)); SK = skew (d̂ ∝ (1,2,2)/3, y = (1,−1,0.5), normal ∝ (−2,−1,2));
  - × k ∈ {1, 2.5} (k_in = k_out);
  - × {base, rotated};
  - plus `CB_Q90_TOY-k2.5-1.75`, CB's toy quarter circle, the only case with k_in ≠ k_out.
- **Inputs:** E = 2e11 Pa; ν = 0.25, so G = 8e10 Pa exactly; A = 0.005969026041820614 m², I = 2.700984283923829e-05 m⁴ and J = 5.401968567847658e-05 m⁴ (`KM`'s section, from OD 0.2 m and t 0.01 m).
  - For 90°, 45° and 5°, R = 0.3 m.
  - For 1e-4 and 1e-8, |d| ≈ 0.3 m and R is derived (≈ 3000 m and ≈ 3e7 m).
  - For π − 1e-6, |d| ≈ 0.6 m and R is derived.
  - The actual φ follows from the binary64 inputs (field `derived.phi`); the angle labels are nominal.
- **Coordinates.**
  - Every d component and every translation is a multiple of 2⁻³⁰ m, with |coordinate| < 2²³ m.
  - The nodes are given at X ∈ {0, 5e5, 2e6, 5e6, 7.3e6} m with t_X = (X, 0.7X, 0) (`nodes_by_X`).
  - d is bit-identical at every X, so **one K holds at all five X**. The script recomputes K from the X = 7.3e6 coordinates and finds it bit-identical (field `checks`).
- **Rotated copies:** d_rot = grid(Q d), y_rot = binary64(Q y), with Q the rotation about (1, −2, 3) by 0.7 rad (`generic_rotation_Q_rows`). For the derived-R angles, R is re-derived from |d_rot|.
  - Each rotated copy is its own frozen reference, valid at all five X.
  - Grid rounding of d_rot makes K_rot differ from Q K Qᵀ by 6.6e-10 to 3.7e-8 of max|K| (`generic_rotation_pairs`). That is geometry, not error, so a generic-rotation test compares each copy with its own reference.
- **Exact rotation:** P maps (x,y,z) to (z,x,y). Applying P to d and y gives exactly P K Pᵀ (checked per case: at most 2e-110).
- **Values:**
  - `K_global`: 12×12, 20 significant digits.
  - `derived`: φ, π − φ, s, c, axes, c_loc and the 6×6 F.
  - **Digits:** 110-digit arithmetic, rechecked at 140. The worst agreement is 5e-86 of max|K| (the 1e-8 cases), 7e-98 (the 1e-4 cases) and 2e-104 elsewhere.

## B3. Properties T4-U1 must meet

| # | Property | Criterion | Zero-scale floor | Reference evidence |
|---|---|---|---|---|
| P1 | Null space: the six rigid motions of the actual nodes (translations; rotations about node i with node-j swing ω × d, formed exactly from binary64 d) | for each mode m and row r: \|(K_b r_m)_r\| ≤ 1e-11·Σ_c \|K_b,rc·r_m,c\|, the products and sums evaluated exactly (or in double-double), on every B2 case at every X and on B5.4's controls | where Σ_c \|K r\| = 0 the row must be exactly 0 | reference ≤ 2e-108 |
| P2 | Rotation covariance | exact rotation P: max\|K_b(Px, Py) − P K_b(x, y) Pᵀ\| ≤ 1e-12·max\|K_ref\|; generic rotations: each copy satisfies P4 against its own reference | max\|K_ref\| > 0 always | P: ≤ 2e-110 |
| P3 | Translation equality | bit-equal K (all 144 entries) between X = 0 and every other X for every B2 case | — | exact by construction |
| P4 | Agreement with the frozen K | \|K_b,ij − K_ref,ij\| ≤ 1e-9·max_kl\|K_ref,kl\| for all i, j, on every B2 case (base and rotated), at every X, and on B5.4's controls; informative: the diagonal-scaled \|ΔK_ij\|/√(K_ii K_jj) | max\|K_ref\| > 0 always | — |
| P5 | No radius refusal | 0 refusals across: every B2 case at all five X; the 8 B5.4 controls (refused today by emulation); and a seeded generator of N ≥ 2,000 elbows per X ∈ {0, 5e5, 2e6, 5e6, 7.3e6} (T4-I2 §1.4's column) | — | T4-I2: 321 of 2,000 refused at 5e6 today; this record's emulation: 7 of 43 at 5e6 and 9 of 27 at 7.3e6 |

**Why P1's 1e-11 (I).**
- A correct binary64 assembly leaves about 10–100 u (1e-15 to 1e-14) in the row-relative residual.
- Today's absolute-centre defect is 2e-10 at 5e5 m and about 1e-9 at 5e6 m (T4-I2 §1.4). The threshold separates the two by more than 20× on each side.
- The plan's 1e-9 is the outer bound for model-level references; this is a property test.

**How to construct translations that leave binary64 node differences unchanged (P3).**
- Choose every coordinate and every translation component as a multiple of 2⁻ᵠ, with |x + t| < 2^(53−q). Then every translated coordinate is exact, and x_j − x_i is identical bit for bit.
- Here q = 30 covers |x| < 8.39e6 m.
- A product that forms K only from d, R and y is then bit-equal. Any use of absolute coordinates breaks P3.

**Model-level criterion (VP-STATIC models in B4/B5).**
- The criterion is T3's actual-error measure, `KT:204-229`: max over free rows of |u − u_int| / (1e-9·max(|u_int|, S*_kind)), with tr = max(st, L_b·sr) and ro = max(sr, st/L_b).
- It runs in both solver modes; `FCR:295-328` is the PP-level form.

## B4. T3's recorded breaches and the K-D5/CB models

**Fact.** Re-derived reference quantities are in the JSON field `t3_models.u_int_new`: the exact free displacements under B1, at 20 digits. They come from each model's regenerated bend inputs: R = 0.3 and the stated y_reference.

**Comparison columns:**
- **old→new** is T3's committed u_int, measured against the new reference with B3's model criterion, in units of the criterion.
- **crK** is a formation estimate: each element matrix correctly rounded to binary64, then solved exactly. It is a floor-type indicator for any binary64 product. It is not a bound and not a run.

| Case (definition) | Recorded on main | old→new | crK | Reference after T4-U1 and expected outcome |
|---|---|---|---|---|
| **R5_4's four Passed breaches** (`R5_4_CURVED.md` §3; RR R5-4: "4 curved Passed breaches on main, up to 1.48×"). Skew elbow cantilever: nodes (0,0,0) and (0.3,0,0.3), R 0.3, φ 90°, k 1; N0 translations rigid; N0 springs (k_X, 1e6, 1e6); tip rx load k_X·1e-6. Committed as `KM` `CSKEW_8_5` (y (1/3, −4/3, −1/3)); k_X = 10 and 9 are built the same way here | k_X 10 dense 1.076; 9 sparse 1.035; 8.5 dense 1.481 and sparse 1.096 | CSKEW_8_5: 5.8e-8 | 8.5: 9.9e-3; 9: 9.3e-3; 10: 8.4e-3 | `u_int_new` for CSKEW_8_5, CSKEW_9 and CSKEW_10. **Not settled by reading.** R5_4's EF_shared (solve error on the product's own matrix) was 0.254 dense and 0.640 sparse; crK is 0.01. **I:** after T4-U1 the actual error is likely below 1 and may fall below 0.5 in dense, so `KT:400` ("demotes in both modes") probably fails by design. T4-U1 runs it and T3 agrees the outcome. The dependants are NI `k1_tests.rs:336,:1313`. The gate stays "no Passed breach" |
| **RV5's M31b counterexamples** (RR, "M31b: equivalence withdrawn"; `rv5_models.rs.txt`): CANT60_PLANAR, CANT30_SKEW (= `KM` CSKEW_30_N122), CANT10_SKEW, PP_UTM (5e6, φ 5°). Root rigid; springs 1e6; tip moment (1,1,1) | actual 1.10, 1.90, 6.48 and 1.126, all Passed without K-D5 (caused by the formula chord) | 0.035, 0.027, 0.031, 0.0027 | ≤ 4.2e-4 | `u_int_new`. Expected after T4-U1: Passed, actual < 0.5, not demoted (controls). The designed centre mismatch cannot be constructed any more |
| `KM` CPLANAR_60, CSKEW_30_N122, CSKEW_30_RADIUS_MISMATCH (`KT:419,:447`) | demoted; the M31a and M31b kills | 0.035, 0.027, 5.7e-7 | ≤ 2.8e-3 | regenerated as ordinary elbows: `u_int_new`, not demoted. **The member y_reference in `KM` does not describe these arcs:** `[0,1,0]` bows to the opposite side, and RV5's `[1,0,0]` is a placeholder. Regeneration must use the stated y_reference (bow vector), or it builds a different arc |
| `KM` E1, E6 (`KT:378`) | not demoted | 5.0e-8, 6.8e-8 | ≤ 2e-6 | `u_int_new` (the old values stay valid to 7e-8); not demoted |
| `KM` PP_UTM_2 = `FCR` PP_UTM_5E5 (`FCR:358`; `KT:484`) | Passed; actual 0.044 | 4.1e-5 | 7.4e-4 | `u_int_new`; Passed, actual < 0.5 |
| `FCR` PP_UTM_5E6 (`FCR:379`) | Sensitive; actual 1.126 | 0.0027 | 4.2e-4 | `u_int_new`. After T4-U1: Passed, actual < 0.5. **`:379`'s precondition actual > 1 fails by design** (B5) |
| Review UTM elbows (K5 run records): PP-UTM-5e6-φ2 and PP-UTM-7.3e6-φ10 (plan C2's "X = 5e6 and 7.3e6") | Sensitive; actual 3.12 and 2.28 | — | ≤ 7e-4 | `u_int_new`. After T4-U1: Passed, actual < 0.5 (C2 controls) |

**Regeneration (I).**
- `KM` is regenerated by T3's committed generator with bend inputs (R, k) and the member y_reference set as in `t3_models.regenerated_bend_inputs`. The `KT` builder then passes R and y to the new constructor.
- These values are this record's independent re-derivations, for T3's check of the regenerated u_int (T3 condition 3).

## B5. Negative controls

### B5.1 The formula-chord mutant and M31b: where a kill exists

**Analysis (F, computed).**
- Under B1, the formula chord evaluated exactly equals A·d (B5.3). So the mutant differs from the definition only by the binary64 rounding of R, φ_b, cos φ_b and sin φ_b.
- **Mutant form.** The product mutant is today's chord line `CB:246-250`, inside T4-U1's element. M31b is the same chord inside K-D5's intended element.
- **Size of the defect.** A chord error δc gives a first-order translation error θ·δc at node j. Against S*'s translation scale (≥ L·θ), the ratio is at most 1e9·|δc|/L.
  - |δc_y| is a few u·L.
  - |δc_x| ≈ R·|fl(cos φ_b) − cos φ|, up to 2⁻⁵⁴R, which is visible only when it is large against L = 2R sin(φ/2).
- **Measured on the RV5-B1 cantilever** (N0 rigid, springs 1e6, tip moment (1,1,1)), the mutant's own error in criterion units (`m31b_kill_and_mutant`):

  | φ | 1e-8 | 2e-8 | 5e-8 | 1e-6 | 1e-4 | 5° | 90° | π − 1e-6 | π − 1e-7 |
  |---|---|---|---|---|---|---|---|---|---|
  | IP | **6.37** | 1.40 | 0.73 | 0.057 | 3.3e-4 | 1.7e-7 | 1.9e-7 | 0.063 | 0.21 |
  | SK | **6.23** | 1.37 | 0.72 | 0.055 | 3.3e-4 | 1.6e-7 | 3.5e-7 | — | — |

  The emulation uses exact axes and the binary64 chord.
  - For φ ≤ 1e-4 the chord error comes from fl(cos φ_b) − 1, so these numbers hold for both the product mutant and M31b.
  - **Near π (I).** The π columns describe M31b (K-D5's axes at p, with φ_b in binary64). In the product mutant, axes and chord share φ_b, so the effect there is about u.

- **So a constructible kill exists only for φ ≲ 2e-8.** At φ = 1e-8, cos φ = 1 − 5e-17, so fl(cos φ_b) is 1 for a correctly rounded cos, or 1 − 2⁻⁵³ for a faithful one.
  - Then |δc_x|/L is 5.0e-9 or 6.1e-9, and the ratio is 6.4 (computed) or about 7.8 (I: linear scaling, not computed).
  - The result is robust to libm. This platform's libm and a correctly rounded cos give the same value.

**Kill model K1** (JSON `m31b_kill_and_mutant`, ids `K1-IP-1E-8-X0`, `K1-SK-1E-8-X0`, and the PP form `…-X5e6`):
- **Supports and load:** RV5-B1's cantilever (`FCR:185-235`): N0 translations rigid, N0 rotational springs 1e6 N·m/rad, tip moment (1,1,1) N·m at N1; E 2e11, G 8e10; OD 0.2 m, t 0.01 m; k = 1.
- **K1-IP:** d = (0.25980762112885714, 0.15000000037252903, 0) m; R = 30000000.018065747 m; y = (0,1,0); φ = 1.0000000000000000076e-8.
- **K1-SK:** d = (0.09999999962747097, 0.20000000018626451, 0.20000000018626451) m; R = 30000000.012417633 m; y = (1,−1,0.5).
- **PP form:** N0 = (5e6, 3.5e6, 0). d is exact on the grid, so u_int is the same.
- **Conditioning:** the equilibrated cond₁ is 2.2e3 to 2.4e3 (Passed band).
- **Formation estimate:** crK is 9e-6 and 7e-6, so a correct, accurately formed product publishes well inside 0.5.
- **Values:** u_int and u_mut are in the JSON.
- **Outcomes:**

| Configuration | Expected |
|---|---|
| Correct product, correct K-D5 | Passed; actual < 0.5; not demoted. This needs B1's small-angle accuracy (open point O1). K-D5's own p = 128 error here is about 4e-14 relative, ≤ 0.1 of the criterion after conditioning |
| Product formula-chord mutant | actual ≈ 6.4 / 6.2 → K-D5 demotes (trigger ≈ 12.7 / 12.5); the "actual < 0.5" precondition fails |
| M31b in K-D5 (product correct) | EF ≈ u_int − u_mut → trigger ≈ 12.7 / 12.5 → a false demotion; the "not demoted" assertion fails, so M31b is killed |
| M31b0 in K-D5 | identical to the correct check (B5.3): **not killable** |

**Element-level kills of the product mutant (F, `mutant_element_level`).**
- At B2's 1e-8 cases, P1's row-relative residual is 4.8e-9 to 7.5e-9, against the 1e-11 criterion: a strong kill.
- P4 is 1.1e-9 to 1.6e-9 of max|K| (diagonal-scaled 1.0e-8 to 1.7e-8): a marginal kill.
- From 1e-4 upward, away from π, the mutant passes P1 and P4.
- **Near π (I).** The emulation shows P1 residuals of 4.3e-11 to 6.3e-11. That figure mixes φ_b's rounding into the chord alone, with exact axes. A product whose axes and chord share φ_b sees about u there, so no element-level kill is claimed near π.

**Kernel-level kill K2** (T3's "or an equivalent kernel-level kill"):
- **Construction.** An FK `formation_check` test on K1. The `StructuralSystem` matrix is K1's binary64 formula-chord element: the correct tip stiffness assembled with the formula chord through a test-only chord override. The `FormationSource` carries the correct B1 inputs (x_i, x_j, R, y, E, G, A, I, J, k).
- **Expected:** demoted with reason `Estimate`; EF ≈ u_mut − u_int; ratio ≈ 6.4, trigger ≈ 12.7.
- **Mutants it kills:**
  - M31b: the intended element equals the system's element, so there is no demotion;
  - M31a: K_int is the slot matrix, so there is no demotion;
  - M31 in general.
- **What it guarantees.** It gives "a curved demotion by K-D5" by construction, independent of the product's rounding. M31b0 still demotes, which is consistent with B5.3.

### B5.2 How the required kills are replaced or re-derived (T3's note via WORKING_ITEMS)

| Required test today | After T4-U1 |
|---|---|
| `KT:447` (`kd5_admissible_centre_mismatch_demotes_where_the_product_chord_hides_the_error`; CPLANAR_60 and CSKEW_30_N122) | A centre mismatch cannot be constructed. **Replace** with an SA test on K1-IP and K1-SK at X = 0: plain Passed; actual < 0.5; checked unchanged (`assert_unchanged`). Kills M31b (false demotion, trigger ≈ 12.5–12.7) and the product mutant. Keep CPLANAR_60 and CSKEW_30_N122, regenerated, as no-demotion controls |
| `FCR:379` (PP_UTM_5E6 demotes; precondition actual > 1) | Becomes the C2 control at X = 5e6 (`u_int_new`, Passed, `NUMERICAL_INTEGRITY_CHECKS_PASSED`, actual < 0.5). Add PP-UTM-7.3e6-φ10 as the 7.3e6 control. **The M31b role moves to a new PP test:** K1-IP at N0 = (5e6, 3.5e6, 0), through `pp_route_elbow_request` with `bend_radius` = 30000000.018065747 m and x₁ = (5000000.259807621, 3500000.1500000004, 0). Expected CHECKS_PASSED with actual < 0.5 on both entries and in both modes; M31b gives SENSITIVE, so it is killed |
| `FCR:358` (PP_UTM_5E5 control) | Unchanged in role; u_int regenerated (it moves by 4.1e-5 of the criterion) |
| `KT:419` (M31a; CSKEW_30_RADIUS_MISMATCH) | A mismatch cannot be constructed; regenerate as an ordinary k_X = 30 elbow (control). M31a's kill moves to K2, and to CSKEW_8_5 if it still demotes |
| T3's condition: "at least one constructible curved model still demoted by K-D5, or an equivalent kernel-level kill" | **K2** (by construction). CSKEW_8_5 is product-dependent (B4). **I:** no product-level model demotes robustly once the formation is accurate: correctly rounded formation errors stay below about 0.01 of the criterion within the Passed band, so a demotion would rest on the solve error or the implementation's accumulated rounding |

**Dependency (I).**
- K1 and K2 need angles φ ≤ 2e-8 to stay admissible. Today's lower limit is 1e-9 (`CB:27`).
- If T4-U1 raises the limit above about 2e-8, M31b becomes unobservable at the criterion for every constructible input. It would then need the same narrowing as M31b0.

### B5.3 M31b0: equivalence by construction — **a narrowing for ROOT, not settled**

**Claim.** Under B1's definition, the chord R(cos φ − 1, R sin φ, 0), evaluated at the definition's φ, equals c_loc = A·d for every admissible input.

**Derivation.**
1. Let θ = φ/2. By B1, sin θ = s = L/(2R) and cos θ = c = √(1 − s²) > 0, since θ ∈ (0, π/2).
2. Expand A·d:
   - e_x·d = (−s·d̂ + c·n̂)·d = −sL, because n̂·d = 0;
   - e_y·d = (c·d̂ + s·n̂)·d = cL;
   - e_z·d = (n̂ × d̂)·d = 0.
3. Expand the formula:
   - R(cos 2θ − 1) = −2R·sin²θ = −2Rs² = −sL, using 2Rs = L;
   - R·sin 2θ = 2Rsc = cL;
   - the third component is 0.
4. So H_formula = H for every admissible (x_i, x_j, R, y), and M31b0's intended element is identically the correct one.

**Numerically at p.** Both are formed at p (K-D5's `Wide<2>`, p = 128). The worst case is c_x formed as cos φ − 1 by series, where they differ by p-rounding only: |δc|/L ≲ 2⁻¹²⁷/φ ≤ 6e-30 at φ = 1e-9. That is 21 orders below the criterion.
- **F:** ≤ 4.4e-73 relative at 80 digits on K1 (`m31b0_formula_at_p_minus_actual_over_L`). In every B2 case, the local chord equals the formula to within 3.7e-103 of L at 110 digits (field `checks.formula_chord_at_p_minus_actual_chord_over_L`).

**Status.**
- RR "M31b: equivalence withdrawn" requires M31b and M31b0 to be killed by a required test. Under T4-U1's definition, M31b0 cannot be.
- Per RR:1217 ("an equivalence is accepted only when derived and checked, never by assertion"), this derivation needs an independent check by the refuting TASK or T3's reviewer.
- It goes to ROOT through HELP_HUMAN as a **narrowing**. M31b (binary64) does have a kill (K1, K2).

### B5.4 Large-coordinate controls for CB's tests (`utm_controls_refused_today`)

- **Eight elbows.** Four at X ≈ 5e6 m and four at X ≈ 7.3e6 m, each with Y ≈ 0.7X.
  - Generator: decimal coordinates with mm resolution at i and 1e-9 m at j; R = 0.3; φ from 86° to 175°; seeded `random.Random(20261009)`.
  - **F:** today's PP centre and CB radius check, emulated in binary64 in source order (`PPL:7766-7846`; `CB:150-163`; a labelled emulation), refuse all eight. The radius mismatches are 2.0e-9 to 4.6e-9, above the 1e-9 tolerance with margin.
  - **After T4-U1:** formed (P5), meeting P1 and P4 against the frozen K. Each control carries its own K at 20 digits; the reference P1 residual is ≤ 3e-79.
- **CB's toy quarter circle** (`CB_Q90_TOY-k2.5-1.75`, E 100, G 40, A 3, I 5, J 7, R 2, y (1,1,0)) at the origin and at (7300002, 5110000, 0) → (7300000, 5110002, 0): K bit-identical (P3).
  - **I:** today's code also passes this one, because its centre is exact. It is a cheap translation control, not a discriminator. The eight elbows discriminate.

## B6. SSLL101 (Hovgaard)

**Not matching.** No formulation-matched comparison is possible from the repository.
- **Assets.** `VALIDATION_FOUNDATION/STATIC_REFERENCE_BASIS/ACQUISITION.json` records `"source_assets_vendored": false`. The mesh, decks and reference results were inspected privately and are not in the repository (`APPLICABILITY.md`, "SSLL101 Hovgaard"; T4-I4 §4).
- **Formulation.** Model A is 92 straight `POU_D_T` (Timoshenko) segments, 40 per bend, with reduced bending inertias and inverse shear factors AY = AZ = 2. It is a shear-deformable polygon, not the Euler–Bernoulli arc with k on bending. Models C, D and E (`TUYAU`) carry Fourier ovalization modes.
- **Reference quality.** The references are POUX/ADL/TITUS/ABAQUS values of reported lineage, ±2%. That cannot support a 1e-9 comparison, and there is no pressure case.

## B7. Open points (for WORKING_ITEMS)

- **O1.** T4-U1 needs a cancellation-free small-angle F; the naive form fails below about 4e-3 rad. B2's 1e-4 and 1e-8 cases and K1 depend on it.
- **O2.** M31b0 is a narrowing (B5.3). It needs an independent check and ROOT's decision.
- **O3.** K1 and K2 need T4-U1 to keep φ ≤ 2e-8 admissible (today 1e-9).
- **O4.** K-D5's closed forms at p = 128 lose about 4.5e-11 relative at φ = 1e-9. That risks a false demotion at the lower limit. This is a T3 point: series or a higher p.
- **O5.** The CSKEW_8_5 outcome is open (B4). K2 meets T3's demotion condition by construction.
- **O6.** Regenerated `KM` bends need the stated y_reference. The committed member y_reference is wrong for CPLANAR_60 and CSKEW_30_N122, and a placeholder in RV5's models.
- **O7.** Near π, |d| must be used exactly (4R² − |d|²) for ε ≲ 3e-8. B2 stops at π − 1e-6.
