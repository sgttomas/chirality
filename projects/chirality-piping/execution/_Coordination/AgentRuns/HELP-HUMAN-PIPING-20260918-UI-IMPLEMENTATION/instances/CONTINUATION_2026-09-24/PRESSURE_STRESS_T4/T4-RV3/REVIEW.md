# T4-RV3 REVIEW: refutation of T4-I7's bend references for T4-U2

**Who.** T4-RV3, an independent reviewer (TASK, Type 2) for T4's WORKING_ITEMS. It ran as a harness-native subagent, with no delegation, no Git writes and no cargo.

**Brief.** `R4/BRIEFS/T4-RV_REFERENCE_REFUTATION.md` (`816c20ab…`), with the common terms `R4/BRIEFS/T4_WI_COMMON.md` (`7d44afd0…`).

**Under review.** `R4/T4-I7/` at `80b1e97e2b`. Its brief is `R4/BRIEFS/T4-I7_U2_BEND_REFERENCES.md` (`cee2f2dd…`).

**Code basis.** `ed012c7ccf`. It was read for conventions only.

**Integrity.** `R4/T4-I7/SHA256SUMS` (`c6269caf…`) verifies all 13 files OK. I re-ran T4-I7's four scripts from a scratch copy:
- the generator reproduces both JSON files and its stdout byte for byte;
- the cross-check, the precision check and the RV1-seed comparison reproduce their stdout byte for byte (`rv3_rerun_i7.stdout.txt`).

## Disposition: BLOCKING, on B-1 only

- **The reference values pass.** Every expected value in all 67 cases was re-derived by a different method.
- **What blocks.** 23 negative-control rows that a test is meant to assert cannot be satisfied by a correct product (B-1). The repair is mechanical.
- **What else should change.** Three SHOULD-FIX items:
  - S-1: the chord-frame end rows;
  - S-2: the placement of the kink controls;
  - S-3: the plan's headline case is missing.
- **Nothing changes the plan.** No stop rule fires, and no T3 condition is touched.

## 1. Independent method

**The engine (`rv3_lib.py`, `rv3_solve.py`).** It is a strong-form transfer-matrix solve in Python `decimal` at 50 digits.
- **The equations.** The linear Euler–Bernoulli beam equations are written in the co-rotating member frame (t, n inward, b):
  - F′ = −ω×F − q
  - M′ = −ω×M − t×F
  - u′ = −ω×u + θ×t + t(N/EA + ε0)
  - θ′ = −ω×θ + (T/GJ)t + k(M − Tt)/EI

  Here ω = (0, 0, 1/R) on arcs. This system has constant coefficients on a circular arc.
- **Propagation.** The state [F, M, u, θ, g, 1] is propagated by the matrix exponential of the 16×16 system matrix (Taylor series). Self-weight enters through the rotating image g of global −Z, and the wall load as (P/R) along −n.
- **Solution.** Each line is solved by shooting from anchor A, with six unknown section actions. The end conditions at D are either zero action beyond D or zero motion.
- **Numerics.** π by the AGM; sin and cos by halving and doubling; the included angle by Newton's method on atan2.
- **What it shares with T4-I7.** Only the physics statement. There is no flexibility integral, no quadrature, no stiffness matrix and no K·u_free.
- **Inputs.** Each case is built only from its own `inputs` block, with the coordinate strings parsed to binary64 first. This is also a transport check.

**The second view (`rv3_float_noise.py`).** A plain binary64 direct-stiffness emulation of the H-2 product path:
- my own arc element, inverted in binary64;
- the bend term K_b·u_free(ε_p) − c_b, the Poisson pairs and the caps;
- recovery N_w = N_el + pAi.

It is used to judge the floors, not as a reference.

## 2. Results against the seven checks

| # | Check | Result |
|---|---|---|
| 1 | Values | All 67 cases and every family: free L, anchored L, U-loop, CBPT, kink, reversed, skew, UTM and mm/MPa. 29,565 expected leaves (nodes, six-component reactions, terminals, stations, end rows in both frames, Lamé values, arc and frame geometry) agree to ≤ **4.68e-20**, normalized by max(\|ref\|, zero_scale). That is the file's 20-digit rounding (`rv3_check.stdout.txt`). Every traversal flag matches. Every expected group has a zero_scale; each zero_scale equals its group maximum, and each floor = 1e-9·zero_scale. The tangency kinks are: numerically zero at the origin; ≤ 1.5e-15 rad when skewed at the origin; 9e-11 to 8.7e-10 rad at UTM-skew (binary64 input rounding); and 9.999996666668677e-4 rad in the kink cases |
| 2 | Independence | The engine forms no stiffness and no K·u_free, and my different method agrees. No value comes from the product. The retired CBPT tip appears only as the "old" column and as the mutant; I re-derived it as −1.4·P/(E·As) = −1.0808615345608499e-4 m, which matches the retired hand calculation (`P/validation/hand_calcs/mechanics/curved_bend_pressure_thrust_arc.md:311-325@ec5d397359`) |
| 3 | Formulation | Matches the plan and today's conventions; see N-1 |
| 4 | Coverage | Every item of the I7 brief is present. Plan §2's headline case is not (S-3); limits in N-6 |
| 5 | Discrimination | Every listed control's wrong values were re-derived by my solver to ≤ 1.1e-16 (`rv3_controls.stdout.txt`), and each control's maximum distance is confirmed. 23 rows fail (B-1). Seven extra plausible defects are each caught at ≥ 1.5e7 tolerances (N-2). The floors are not tight against binary64 (N-2) |
| 6 | Transport | The inputs suffice to rebuild every case. The UTM coordinates are usable as written (N-3). The provisional sketch fields are marked |
| 7 | Hygiene | Placeholders only, in all 13 files |

## 3. Findings

**B-1 (BLOCKING). 23 of the 241 `wrong_result_discriminators` rows do not discriminate.**
- **Claim.** These rows are "the discriminating values a test asserts the product does not produce" (I7 brief). U2_REFERENCE §8 says every mutant lies at ≥ 8e6 tolerances.
- **Evidence.** In U2-L-FREE-P-K2 and CBPT-K2, the bend-term-omitted, c_b-added and Poisson-missing controls carry rows where the wrong value equals the reference:
  - support A Fz and Mx, which are 0 in both;
  - Poisson-missing rows whose "wrong values" are 60-digit noise (1e-54, 1e-60, 4.6e-56) against 0.

  U2-L-KINK-FREE-P-K2 has the same at support A Fz and Mx. The distances print as `0.000e-504`, `0.000e-806` or 1e-47. In addition, KINK-FREE support A Fy discriminates by only 500 tolerances.
- **Consequence.** A test built from these rows fails every correct product. Under SP-3 such a mismatch goes to the implementer and can never change the reference, so the rows must be repaired before acceptance.
- **Repair.**
  - Keep only rows at ≥ 1e3 tolerances (the controls' maxima, 8.4e6 to 8.1e12, are unaffected), or flag each row's status.
  - Format exact zeros as `0`.
  - Restate §8's claim per control maximum.

**S-1 (SHOULD-FIX). The chord-frame arc end rows are wall actions with no stated basis, inside the asserted `expected` tree.**
- **Evidence.**
  - `end_rows/*/chord_frame` is the physical node-on-element action, f_el + c_b.
  - Today's chord-frame arc rows are K·d − p, which are "not wall actions on an arc" (I1 §5.3 #8; RV1 S-7).
  - Under H-2 the elastic chord row differs by c_b's chord components. In U2-L-ANCH-ALL-K2, BEND end_i, the chord F_y is −67,849.36 N on the wall basis against about −396.3 N on the elastic basis, roughly 1e9 tolerances apart.
- **Consequence.** A correct product that keeps elastic chord rows fails a test that asserts these leaves.
- **Repair.** Either move the chord-frame block out of `expected` (as information), or label it "wall (physical) = elastic + c_b" and add the elastic rows, naming the product row each one maps to. The tangent-frame rows are unaffected: c_b is purely axial there.

**S-2 (SHOULD-FIX). The kink controls sit on the α_tan boundary.**
- **Evidence.** From the binary64 inputs (D.x = 3.245999999999999996…):
  - θ = 9.999996666668677e-4 rad;
  - α_tan − θ = 3.33e-10 rad, which is 3.3e-7 relative.
- **Safe against α_tan = 1e-3 rad?** Yes, under T4-I11's rule θ = atan2(\|t_in×t_out\|, t_in·t_out) ≤ α_tan:
  - binary64 evaluation errs by 1e-19 rad;
  - sin θ and 1 − cos θ also pass.
- **But fragile.**
  - tan θ − 1e-3 = +8.9e-19, so a small-angle "tan θ ≤ α_tan" check refuses the case.
  - Any downward revision of the provisional α_tan (D-D) refuses it.
- **Repair.**
  - Place the kink near α_tan/2. For example, D.x = 3.248 gives tan θ = 5e-4. Then regenerate the two cases and their discriminators.
  - Pair it with a refusal control at about 2α_tan among T4-U2's refusal tests (`PRESSURE_REGION_MITRE_UNSUPPORTED`).

**S-3 (SHOULD-FIX). Plan §2's headline case is absent.**
- **Evidence.** Plan §2 calls for closed, wall-transferring terminals at both ends, anchored, with a free-ended variant, carrying pressure, weight and temperature in one case. The file's "ALL" is SEPD + T + W, following the I7 brief's literal "all three together". No case combines both terminals transferring with P+T+W.
- **Consequence.** The value is derivable (anchored: ALL with R_D shifted by −pAi·t_D; free: PT + PW − P), but the first usable path's own end-to-end case has no reference or documents.
- **Repair.** Add U2-L-ANCH-PTW-K1/K2 and U2-L-FREE-PTW-K1/K2, and preferably make the anchored one a core case with the skew, UTM and mm/MPa transforms.

**N-1. The formulation matches; facts read at `ed012c7ccf`.**
- **Arc energy.** Axial plus torsion plus k·(in-plane and out-of-plane bending), with no shear, and torsion and axial unscaled (`CB:205-239`). PP passes one k to both planes (`PPL:7848-7865`).
- **Straights.** Euler–Bernoulli: FK has no shear term.
- **Loads.**
  - The wall load is pAi/R outward with no distributed moment, which is exact for the fluid column.
  - The caps act along the end tangents.
  - The Poisson eigenstrain is −2νpAi/(E·As), a contraction.
  - Arc self-weight is per unit arc length. PP uses the primitive's N/m directly as the per-arc-length intensity (`PPL:10971-11002`), and the self-weight operation emits per-pipe `distributed_force` N/m.
- **Rows.**
  - Stations are the j-side action in the tangent frame (x toward j, y inward, z = (x_i−c)×(x_j−c)), matching CB `arc_section_resultants` and `PPL:10961-10964`.
  - Straight end rows are node-on-element, with end_i = −N_w as in `PPL:5027-5043,11516`.
  - Arc end rows are in the tangent frame (RV1 S-7).
  - The reversed case agrees.

**N-2. The floors and discrimination are sound.**
- **Floors.**
  - The binary64 emulation of H-2 stays at ≤ 9.5e-4 of every floor in ten representative cases (`rv3_float_noise.stdout.txt`). These include the identically-zero groups of the free P, PT, CBPT and kink cases, U-loop ALL, and UTM-skew. So no floor is tight against rounding.
  - The bending-stress fallback (pAi/As) is 137× tighter than the moment fallback implies (L family). That is harmless: the margin inferred from the emulated moments is about 2e5.
- **Mutants outside I7's list.** Each is caught at ≥ 1.5e7 tolerances by some case in the file (`rv3_controls.stdout.txt`):
  - k also on torsion;
  - k in-plane only;
  - the Poisson sign flipped;
  - the wall load inward;
  - arc weight per unit chord;
  - a separately supported closure still capped;
  - caps along chords.

**N-3. The UTM coordinates are what a test can use.**
- All coordinate and y_reference strings are round-trip binary64 reprs, and the sketches carry the identical binary64 values.
- PP parses with serde_json `float_roundtrip` (`PP/Cargo.toml:29`), and Rust, Python and JS parsers round correctly.
- Taking the short decimals as exact instead shifts values by up to 2.7e-10 (the CBPT cap at X = 5e6) and geometry leaves by up to 7.3e-10. So tests must not re-round UTM coordinates (no mm or f32 detour).

**N-4. At UTM-skew the representation remainders are load-bearing.**
- Their size is pAi·θ ≈ 6e-5 N, with θ ≤ 8.7e-10 rad.
- Dropping them moves U2-L-FREE-P-K2-SKEW-X5E6/X7P3E6 by 1.05e3 tolerances, ANCH-ALL by 41 and U-ANCH-ALL by 24 (`rv3_utm_remainder.stdout.txt`).
- This is consistent with H-2 and I11, under which θ ≤ α_tan is carried exactly by the remainder. T4-U2 must never snap sub-tolerance kinks to exact tangency.

**N-5. Free SEPD and ALL move about 1 m and 0.24 rad.**
- No small-rotation guard was found in PP at `ed012c7ccf`.
- The cases are valid linear references. Keeping them or scaling p is the WI's choice.

**N-6. Coverage and transport limits.**
- C1's guides and linear springs are not in T4-U2's VP-STATIC list. Plan §5 does not require them; the WI decides.
- The supports are free text ("support:D anchor at node:D").
- The sketches have not been deserialized by the product (I7 limit 7).

## 4. Records (`R4/T4-RV3/_run_records/`, run with `python -I -B`)

| Script | What it does | Output |
|---|---|---|
| `rv3_lib.py`, `rv3_solve.py` | The independent engine | — |
| `rv3_check.py` | All 67 cases, all leaves | `rv3_check.stdout.txt` (arcs list `lame_surface` as missing because it is withheld on arcs) |
| `rv3_controls.py` | I7's controls re-derived, plus the extra mutants | `rv3_controls.stdout.txt` |
| `rv3_float_noise.py` | The floors against the binary64 H-2 path | `rv3_float_noise.stdout.txt` |
| `rv3_kink_utm.py` | The kink margins and the UTM transport | `rv3_kink_utm.stdout.txt` |
| `rv3_utm_remainder.py` | The representation remainders | `rv3_utm_remainder.stdout.txt` |
| `rv3_rerun_i7.py` | T4-I7's scripts, byte for byte | `rv3_rerun_i7.stdout.txt` |

I will confirm the repair of B-1 and S-1 to S-3 on request.
