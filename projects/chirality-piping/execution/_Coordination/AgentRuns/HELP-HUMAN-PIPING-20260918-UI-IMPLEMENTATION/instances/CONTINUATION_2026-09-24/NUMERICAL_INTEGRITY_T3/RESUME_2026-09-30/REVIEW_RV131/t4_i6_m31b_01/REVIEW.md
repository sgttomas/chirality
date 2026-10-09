# RV131: T3's check of T4-I6's M31b kills and M31b0's equivalence (T4-U1)

- **Who:** RV131, independent reviewer (Type 2), a fresh instance. Dispatched by WORKING_ITEMS for T3 (Agent 1), the return path. No delegation.
- **Brief:** `R/BRIEFS/RV131_T4_I6_M31B.md`, sha256 `b89325dc…7a5e` (NUM `784ccdd399`), with `R/BRIEFS/B1_COMMON.md`'s host and records rules (WORKING_ITEMS in ROOT's place).
- **Material:** `R4/T4-I6/` at `4a5c65e38a` (`U1_REFERENCE.md` `9c1de142…`, `u1_reference_cases.json`, `_run_records/`; `SHA256SUMS` `146f734a…` verifies all 16 files). Context read: `R4/T4_RULINGS.md` (T3's seven items; HELP_HUMAN's small-bend ruling), `RR` "M31b" sections (RR:526-559, :689-706, :1217), `R/I115/t4_annex_check_01/RETURN.md` §5 item 2.
- **Code basis:** `ed012c7ccf`. K-D5 = FK `structural/formation_check.rs` (cited `FC`), NI `structural_adapter/kd5_tests.rs` (`KT`) and `kd5_models.rs` (`KM`), PP `tests/formation_check_runtime.rs` (`FCR`); CB `curved_bend/src/lib.rs`.
- **Method:** standard-library Python (`_run_records/RUN.txt`). An independent B1 element (global-frame quadrature, not T4-I6's local closed form) and a binary p-bit emulation of K-D5's re-formation. No cargo, no product code run, no Git writes.
- **F** = computed or read; **I** = inference.

## Verdicts

| Item | Verdict |
|---|---|
| **M31b0** (§B5.3) | **HOLDS.** Exact identity re-derived; p = 128 rounding bound re-derived and emulated; no admissible input makes the difference observable. Two conditions and corrections to the record's numerical step (N-1, N-2) go with the narrowing |
| **K1** (§B5.1-B5.2) | **MEETS** the M31b-kill requirement, **conditionally**: it needs T4-U1's product to be accurate at φ = 1e-8, which the proposed acceptance (φ ≥ 1e-4) and P4 (1e-9) do not guarantee (S-1). Margins are real at both coordinates |
| **K2** (§B5.1) | **DOES NOT MEET** T3's condition as the brief and HELP_HUMAN state it (a constructible curved model demoted from conditioning, not small angles): it is a test-only matrix override whose demotion comes from an injected small-angle chord defect at cond ≈ 2.2e3 (B-1). It is a valid kernel-level M31b kill if its system matrix is built from an accurate tip stiffness (S-2); its M31a kill is unverified (S-3) |
| **The pair, in substance** | M31b: killed (K1 conditional, K2 conditional). M31b0: a valid narrowing. M31a: only K2, conditional on wiring. **A constructible conditioning-driven curved demotion: not provided** — and T4-I6's inference that none exists is refuted (S-4); a candidate is given |
| **O4** | Real, but not where T4-I6 puts it. K1 is unaffected (trigger ≤ 2e-7 at φ = 1e-9). Long, axially loaded, nearly straight bends at the floor falsely demote (L = 30 m: trigger 47-198). **Remedy: the stable form (1 − cos φ = 2s² at p = 128)**; no change of p (S-5) |
| **O5** | Reasoning sound in direction. T3 should agree to a decision rule, not a number (below) |
| **O6** | **Confirmed** from code, and regenerating from the bow vectors is right; the regenerated u_int reproduce independently |
| **Re-run** | T4-I6's four scripts reproduce byte for byte, and so do PART1 and the JSON |

## 1. M31b0: equivalence by construction (§B5.3)

**The admissible domain (F, code).** L > 0; R > L/2 (PPL:7783, binary64 test, which near π refuses more than the exact domain); φ ∈ [1e-9, π − 1e-9] (CB:27); |y − (y·d̂)d̂| > 1e-9 (PPL:168, :7830). The last test is **absolute**, on the unnormalized y, so |y|/|y_⊥| is unbounded.

**Exact identity (re-derived).**
1. s = L/(2R) ∈ (0,1) and c = √((2R−L)(2R+L))/(2R) > 0 satisfy s² + c² = 1. So atan2(s, c) = θ ∈ (0, π/2) with sin θ = s and cos θ = c, and φ = 2θ ∈ (0, π).
2. n̂ ⊥ d̂, |n̂| = 1. Then e_x = −s d̂ + c n̂, e_y = c d̂ + s n̂, e_z = n̂ × d̂ is orthonormal and right-handed (e_x × e_y = (s² + c²) n̂ × d̂ = e_z).
3. A·d = (−sL, cL, 0), because d = L d̂ and n̂·d = 0.
4. R(cos 2θ − 1) = −2R s² = −sL (using 2Rs = L), and R sin 2θ = 2Rsc = cL.
5. Hence (R(cos φ − 1), R sin φ, 0) = A·d for every admissible (x_i, x_j, R, y), and M31b0's H is the definition's H.

The frame is CB's convention (x radial outward at i, y tangent toward j). The centre x_i − R e_x = mid − Rc n̂ lies on the −n̂ side, matching PP's bow (PPL:7760-7765). **The identity holds.**

**The rounding bound at p = 128 (re-derived).** M31b0 and the correct K-D5 share d_p, L, s, c, φ and the axes. They differ only in H's chord.
- **c_x.** The correct form is a dot product, with abs error about u·L. The formula R(fl_p(cos φ) − 1) inherits cos φ's absolute rounding (≤ k·2^-129 near 1, k ulps). So |δc_x|/L ≲ k·2^-129/(2 sin(φ/2)) ≈ k·2^-129/φ. **The worst case is the cancelling form fl_p(cos φ) − 1.** A series for cos φ − 1 is the benign case.
- **c_y.** The error is a few u, including near π.
- **The y-projection.** n̂_p·d̂ ≈ u·|y|/|y_⊥| enters A_p·d but not the formula.
- **Bound:** |δc|/L ≲ (c₀ + c₁/φ + c₂|y|/|y_⊥|)·u_p, with small constants.
- **Sensitivity.** EF tracks about κ·1e9·|δc|/L, with κ ≈ 1.27 on K1 (6.37 at δc/L = 5.0e-9; also at 2e-8 and 1e-4, F).

**Emulated at p = 128 (F, `rv_m31b0_attack`, `rv_m31b0_yscale`).** 353 admissible inputs: random, near π to ε = 1e-9, the 1e-9 floor, X up to 7.3e6 with ordinary coordinates, and y with relative y_⊥ down to 1e-9. Two spellings of the formula: 1 − 2s², and cos/sin of φ_p.
- The maximum |δc|/L is 1.3e-30 at the floor, 1.0e-30 random, 3e-38 near π and 4.4e-30 for nearly parallel y. **EF ≤ 6e-21 of the criterion.**
- With |y|/|y_⊥| = 1e15 to 1e30, |δc|/L ≤ 2e-21 and EF ≤ 3e-12.
- **Beyond that (I)** (|y|/|y_⊥| ≳ 1e28 with only n̂ inexact; binary64 rounding of y usually caps the effective ratio near 1e16), the two forms could differ at the criterion. But there the binary64 product cannot resolve the plane (u₆₄·|y|/|y_⊥| ≫ 1e-9), so every K-D5 variant demotes and no kill is possible.

**In K-D5 (F, `rv_o4_kd5_emulation`, `rv_k2_emulation`).** M31b0's trigger equals the correct check's to 4+ digits on K1 (both planes; φ from 1e-9 to 5°) and in K2 (12.743 / 12.450).

**Verdict: HOLDS** to RR:1217's standard: derived step by step and independently checked. Conditions and corrections for the narrowing:
- **N-2:** it holds only once K-D5's `CurvedFormation` carries (R, y) and forms φ and the chord at p from (d, R, y). If any binary64 centre, derived radius or φ survives into K-D5's inputs, M31b0 is killable again, as it was before T4-U1.
- **N-1:** B5.3's numerical paragraph has three problems:
  - its worst-case wording ("formed as cos φ − 1 by series") is inverted;
  - its bound 2^-127/φ omits the constant term (exceeded 2.5× near φ ~ 1, harmless) and the y-projection term;
  - its evidence is decimal-precision (4.4e-73 at 80 digits; 3.7e-103 at 110), not p = 128.

  The corrected bound and this emulation should travel with the narrowing to HELP_HUMAN.

## 2. M31b's kills (§B5.1, §B5.2)

### K1

**Inputs (F, `rv_k1_inputs`).**
- The stated literals equal the JSON: d (IP and SK), R = 30000000.018065747 and 30000000.012417633, PP x₁ = (5000000.259807621, 3500000.1500000004, 0).
- d is on the 2^-30 grid. PP's binary64 x₁ − x₀ equals d exactly, so u_int is identical at X = 0 and (5e6, 3.5e6).
- φ = 1.0000000000000000076e-8. cos φ = 1 − 5.0e-17, which is 5.5e-18 above the rounding midpoint 1 − 2^-54. So a correctly rounded cos gives 1, and a faithful one gives 1 − 2^-53. That makes δc/L 5.0e-9 or 6.1e-9: robust to libm. This platform gives 1.

**The independent check (F, `rv_check_refs`).** RV131's element reproduces all 49 frozen K to ≤ 3.7e-20 of max|K| (the 20-digit storage) and φ to 1e-25. It reproduces K1's u_int to ≤ 4.2e-11 of the criterion, and the product mutant's error, 6.3716 (IP) and 6.2249 (SK).

**The mutant side (F, `rv_o4_kd5_emulation`).** M31b inside K-D5 on the correct product gives trigger 12.743 (IP) and 12.450 (SK). That is 12× over the threshold. At 2e-8 it is 2.8, at 1e-9 1.27 (fl(cos) = 1 makes δc/L = φ/2), and at 1e-6 0.11. So φ = 1e-8 sits near the optimum (cos rounds to 1 until φ ≈ 1.05e-8).

**The correct side.**
- K-D5's own p = 128 error adds nothing on K1: the trigger is 1.3e-7 (IP) to 2.0e-7 (SK) at 1e-8 and 1e-9, the floor set by u's binary64 representation, for the closed form, the stable form and p = 192 alike. T4-I6's "≤ 0.1 of the criterion" is pessimistic (S-5).
- The product's share is the formation (crK 9.4e-6 / 7.0e-6 if correctly rounded) plus the solve (cond₁ 2.2e3 to 2.4e3, Passed band).

**What K1 depends on (I, with T4_RULINGS' small-bend ruling).** K1's correct pair must publish Passed with actual < 0.5 at φ = 1e-8.
- **The stable form must be accurate at 1e-8.** The naive closed form is wrong by O(1) there (T4-I6 naive sweep: 4.24).
- **The acceptance does not cover it.** The proposed acceptance covers "φ = 1e-4 rad up to π − ε" only.
- **P4 does not guarantee it.** P4's 1e-9 matrix-scale tolerance admits a null-space-breaking error (1.4e-9) that gives 6.4 on this very model.
- **The fallback and the stop rule.** A "Sensitive demotion as the fallback" reaching 1e-8 removes K1's precondition, and so does the stop rule moving the stable form to T4-U1c.
- **φ = 1e-8 must stay admissible** (O3; HELP_HUMAN advises against a minimum-angle refusal).
- **PP's builder needs a radius parameter.** `pp_route_elbow_request` hard-codes bend_radius 0.3 m (FCR:220; N-8).

**Verdict: MEETS** the M31b-kill requirement, conditionally (S-1). K1 is not a curved demotion: its correct pair stays Passed.

### K2

**Emulated (F, `rv_k2_emulation`).** The system element is K1's exact tip stiffness with H from the binary64 formula chord, rounded once. u is that system's solution. K-D5 then gives:
- correct: **12.743 / 12.450** (demotes);
- M31b: 3.1e-5 / 1.4e-5 (killed);
- M31b0: 12.743 / 12.450 (equal to correct, consistent with §1);
- M31a, with K_int = the system's own element: 1.7e-7 (killed).

The construction works.

**Dependencies.**
- **S-2.** If the system's tip stiffness comes from CB's binary64 evaluation at φ = 1e-8, it is O(1) wrong without the stable form. M31b then demotes too and is not killed. "Independent of the product's rounding" holds only if K2's matrix is built from the frozen reference or K-D5's own p re-formation, rounded once.
- **S-3.** The historical M31a patch (`T/IMPLEMENTATION/KD5/_run_records/addendum4/mutations/mutate.py.txt:83-98`) adds `shared` to `CurvedFormation`. It fills `shared` from SA's slot matrix and with **zeros in FK test sources**. In an FK-level K2, M31a's K_int would lack the curved element, so the test would demote and M31a would survive. The M31a kill needs one of two things:
  - an SA-level K2 (the slot matrix overridden);
  - an FK expression of M31a that hands K_int the system's own element.

  Either way it must be confirmed by running the patch. B5.2's ":419" row also says M31a's kill moves "to CSKEW_8_5 if it still demotes". That is wrong after T4-U1: with an accurate product formation, CSKEW_8_5's EF is its solve error, which the shared-matrix mutant sees equally.

**Against T3's condition.** HELP_HUMAN (`R4/T4_RULINGS.md`, small-bend ruling): "A constructible curved model must still be demoted by K-D5 after T4-U1, from conditioning rather than from small angles." T3's item 2 (same file) had allowed "or an equivalent kernel-level kill".
- K2 is that kernel-level kill.
- K2 is not constructible, and its demotion comes from an injected small-angle defect at cond ≈ 2.2e3.

**Verdict: DOES NOT MEET** the condition as stated in the brief and the later ruling (B-1). It serves as the kernel-level M31b kill (S-2) and possibly the M31a kill (S-3).

### The pair, in substance

M31b is killed. M31b0 is a valid narrowing. M31a hangs on K2's wiring. The constructible, conditioning-driven curved demotion is missing.

**T4-I6's inference** (B5.2, last row): "no product-level model demotes robustly once the formation is accurate: correctly rounded formation errors stay below about 0.01 of the criterion within the Passed band". This generalizes from CSKEW's short 90° elbow, and it is **refuted** (F, `rv_o5_curved122`):
- Take F122's supports and loads, with its 3 m skew member realized as a B1 bend.
- At R = 10 m (φ = 0.30 rad), crK is **0.77** (y (1,0,0)) and 0.36 (y (0,1,−1)), with exact equilibrated cond₁ 4.1e7 / 4.0e7.
- At R = 100 m, crK is 0.41 / 0.81.
- F122 itself has cond₁ 3.9e7 and crK 0.64, and its product publishes Passed with a breach of 2.43 dense and 1.21 sparse (2-4× its floor).

**I:** a curved F122 analogue is a constructible candidate that is likely to breach, and so to demote, in both modes after T4-U1, from formation under conditioning at an ordinary angle. T4-U1 must confirm three things: Passed ordinarily (cond < 1/√ε, structural.rs:1758), the breach, and the demotion. That is B-1's remedy.

## 3. §B7's points on T3's side

### O4: K-D5's closed forms at the lower limit

**Where the loss is (F, `rv_o4_diag_cancel`; labelled cross-check).**
- It sits in the in-plane flexibility coupling F_xy. FC:681/689 forms 1 − cos φ from a cos already rounded at p, so cos's absolute error u enters q_in(Fx, Fy) with weight R², where the true value is O(R²φ⁴).
- That gives F_xy a diag-scaled error of about 8u/φ³: 3e-11 at decimal 38 and φ = 1e-9. Binary p = 128 relK is 6.5e-12 (IP) and 3.1e-12 (SK), against T4-I6's 4.5e-11 at decimal 38 (`rv_o4_kd5_emulation`).

**Why K1 is safe.** The error is in K_t, and H uses the actual chord, so the element's null space stays exact. The error is not amplified by the model's soft modes. The "relative K error × condition number" heuristic overstates it by more than 8 orders: K1's trigger is 1.3e-7 (IP) and 2.0e-7 (SK) at φ = 1e-9, the u floor.

**Where it bites (F, `rv_o4_axial`).** A rigidly rooted, axially loaded, nearly straight bend; the trigger scales as (L²A/I)·u/φ³.

| Chord L | φ | Trigger (closed form, p = 128) |
|---|---|---|
| 0.3 m | 1e-9 | 0.022 |
| 3 m | 1e-9 | **0.97** |
| 30 m | 1e-9 | **198 (false demotion)** |
| 30 m | 2e-9 | **47** |
| 30 m | 5e-9 | 0.93 |
| 30 m | 1e-8 | 0.46 |

These are admissible today: PP has no upper radius bound, and R = 3e10 m. The stable form (1 − cos φ = 2s² rounded once at p) and p = 192 both give ≤ 3e-6 on every case.

**Recommendation: the stable form.**
- K-D5's curved re-formation is being rewritten for (R, y) anyway, B1's own trigonometry implies it (cos φ = 1 − 2s²), and it keeps FORMATION_PRECISION = 128 (FC:39), a design constant. A higher p is unnecessary.
- G₃₃ = φ/2 − sin2φ/4 still loses u/φ², which is harmless at p = 128 (≤ 3e-6 above). A series is optional.
- Add a kernel-level K-D5 test with the system matrix from K-D5's own re-formation, rounded once (independent of CB): L = 30 m, φ = 1e-9, rigid root, axial load, not demoted. It kills a reversion to the cancelling form.

### O5: CSKEW_8_5 (KT:400)

**The reasoning is sound in direction** (F: crK 0.00986, reproduced; R5_4's EF_shared 0.254 / 0.640, `T/DESIGN_NUMERICS/R5_4_CURVED.md:111`). After T4-U1, the actual error is:
- the product's formation: floor 0.01, with F122's product/floor ratio 1.9-3.8 suggesting a few hundredths;
- plus the solve error, which is redrawn because the matrix bits change. R5_4's solve-only values across this family's Passed band are 0.03-0.70.

An actual > 1 in both modes is therefore unlikely, and KT:400's precondition most likely fails by design.

**Two qualifications.**
- The 0.25 / 0.64 will not persist as such.
- CSKEW_8_5 sits within about 5% of the ordinary Sensitive gate (cond 6.4e7 against 1/√ε = 6.7e7; N-7). The family has no headroom for more conditioning.

**The outcome T3 should agree, before T4-U1 runs it:**
1. **Gate.** No Passed breach: in each mode, actual > 1 implies demoted.
2. **D5C-1 form.** Demoted if and only if actual > 0.5, with EF/actual within 1e-3 when demoted and `assert_unchanged` otherwise. Keep the ±0.05 boundary guard of `kd5_d5c1_controls…`. If a mode lands in [0.45, 0.55], substitute CSKEW_9 or CSKEW_10 (references frozen in the JSON); do not relax the assertion.
3. **KT:400 is retired** as "demotes in both modes" and becomes that control.
4. **Its roles move:**
   - the curved true positive goes to B-1's model;
   - M31a's kill goes to K2 (S-3), not CSKEW_8_5;
   - NI `k1_tests.rs:336` (parity) and `:1313` (ledger split) need a curved model that demotes in both modes through SA. That is B-1's model, not K2 (FK level).

### O6: y_reference in the committed models

**Confirmed from code.** SA's builder takes the centre for bends and never reads the member y_reference (KT:66-130, `Some((center, factor))` at KT:97), and neither does K-D5's `CurvedFormation` (FC:47-61). The committed values were never exercised.

Measured against the arc each centre describes (F, `rv_o6_bow`):

| Model | Committed y | Against the bow |
|---|---|---|
| CPLANAR_60 | [0,1,0] | **opposite side** (cos −1) |
| CSKEW_30_N122 | [0,1,0] | **a different plane** (cos −0.745), not only the opposite side (N-5) |
| RV5_CANT30_SKEW, RV5_CANT10_SKEW, RV5_CSKEW30_* | RV5's placeholder [1,0,0] | a different plane |
| RV5_PP_UTM | [1,0,0] | opposite side |
| RV5's CANT90, CANT60 and NEARPI models | [1,0,0] | right by coincidence |
| E1, E6, CSKEW_8_5, CSKEW_30_RADIUS_MISMATCH, PP_UTM_2 | as committed | consistent |

**Regenerating from the bow vectors is right.**
- T4-I6's regenerated y has cos +1 to the old bow for all 13 regenerated members, so it builds the same plane and side with R = 0.3.
- Its u_int_new reproduce independently to ≤ 5.0e-11 of the criterion (`rv_o6_uint`).

**Two cautions.**
- `kd5_models.py` should take y per bend as an explicit, recorded input.
- The KT builder must pass exactly those binary64 (R, y) to the new constructor.

## 4. Re-run of T4-I6's scripts

`selftest`, `p128_closed_form_precision`, `freeze_u1` and `t3_models` reproduce byte for byte, and so do PART1 and `u1_reference_cases.json` (hashes in `RUN.txt`). `neg_scan.py` is Part A and was not run.

## Findings

**BLOCKING**
- **B-1. K1 and K2 do not meet the binding condition.** HELP_HUMAN: "a constructible curved model must still be demoted by K-D5 after T4-U1, from conditioning rather than from small angles". B5.2 says K2 meets T3's condition "by construction". Under the binding wording it does not: it is a test-only override, its defect is a small-angle one, and its cond is 2.2e3.
  - **Remedy:** T4-U1 builds and runs a conditioning-driven curved true positive. A candidate is F122 with its member realized as a bend, R = 10 m (crK 0.77, cond₁ 4.1e7), with references by T4-I6's method. It must publish Passed ordinarily and demote in both modes.
  - **Otherwise:** a narrowing to HELP_HUMAN, restoring item 2's "or an equivalent kernel-level kill" with K2.

**SHOULD-FIX**
- **S-1. Make K1's dependency explicit.** K1 depends on T4-U1's accuracy at φ = 1e-8, which the proposed acceptance (φ ≥ 1e-4) and P4 (1e-9) do not cover.
  - Make K1 an acceptance test of the stable form: SA at X = 0 in both planes, PP at (5e6, 3.5e6) for IP, both entries, both modes.
  - If the stable form slips to T4-U1c, K1 and the retirement of KT:447 and FCR:379 slip with it. At T4-U1, M31b is then killed by K2 alone.
- **S-2. Build K2's system matrix from an accurate tip stiffness.** Use the frozen reference or K-D5's p re-formation, rounded once, with the binary64 formula chord in H — not CB's binary64 small-angle path. Otherwise K2's M31b kill also needs the stable form.
- **S-3. "K2 also kills M31a" is unverified.** With the historical M31a patch (zeros in FK sources), an FK-level K2 does not kill it.
  - Make K2 SA-level, or wire M31a's FK form to the system's element, and run the patch.
  - Correct B5.2's ":419" row: CSKEW_8_5 cannot kill M31a after T4-U1.
- **S-4. Correct B5.2's inference.** The claim that no product-level curved model demotes once the formation is accurate (0.01 floor) is refuted: crK reaches 0.36-0.81 in a curved F122 analogue.
- **S-5. Correct O4's mechanism in the record.** The closed-form error does not break the null space and is not cond-amplified.
  - K1's trigger stays at the u floor (≤ 2e-7), not "about 0.1".
  - The real risk is axial loading of long nearly-straight bends at the floor (L = 30 m: 47-198).
  - Remedy: the stable form at p = 128.

**NOTE**
- **N-1. B5.3's numerical paragraph needs correcting.** Its worst-case wording is inverted. Its 2^-127/φ bound lacks the constant and y-projection terms. Its evidence is decimal, not p = 128. The conclusion stands.
- **N-2. The narrowing is conditional.** It requires K-D5 inputs (R, y) with no binary64 centre, derived radius or φ.
- **N-3. B5.1's bound is not a bound.** B5.1's "the ratio is at most 1e9·|δc|/L" is exceeded by 1.27× (6.37 at δc/L = 5e-9). Read "about 1.3 × 1e9·|δc|/L".
- **N-4. A notational slip.** "R(cos φ − 1, R sin φ, 0)" (RR, the brief, the B5.3 claim) means (R(cos φ − 1), R sin φ, 0), as B1's table has it.
- **N-5. CSKEW_30_N122's y is in another plane.** Its committed y lies in another plane, not on the opposite side. RV5's placeholder is right only by coincidence for some models.
- **N-6. Near π, M31b's effect grows.** It is 0.063 at π − 1e-6 and 0.21 at π − 1e-7. "A constructible kill exists only for φ ≲ 2e-8" is shown only to π − 1e-7. Today PP's binary64 radius test refuses ε ≲ 2e-8; with O7's exact 4R² − |d|², a near-π kill may also exist. Not needed.
- **N-7. CSKEW_8_5 sits near the gate.** It is within about 5% of the ordinary Sensitive gate (structural.rs:1758).
- **N-8. FCR's builder needs a radius parameter.** `pp_route_elbow_request` (FCR:191-235) fixes bend_radius at 0.3 m; K1's PP form needs it as a parameter.
- **N-9. PP's plane tolerance is absolute.** The 1e-9 test is on the unnormalized y (PPL:7830), so it admits arbitrarily ill-conditioned y. A relative tolerance would bound every chord-difference term above.
- **N-10. A path slip in the brief.** It calls `formation_check.rs` "SA's"; it is FK's (`frame_kernel/src/structural/formation_check.rs`).

## Evidence and host notes

- **`_run_records/`:** `RUN.txt`; the libraries `rv_element.py` and `rv_wide.py`; and 12 scripts with their stdout:
  - `rv_check_refs`, `rv_k1_inputs`, `rv_k2_emulation`;
  - `rv_m31b0_attack`, `rv_m31b0_yscale`;
  - `rv_o4_kd5_emulation`, `rv_o4_axial`, `rv_o4_diag_cancel`;
  - `rv_o5_floor`, `rv_o5_curved122`;
  - `rv_o6_bow`, `rv_o6_uint`.
- **Labelled cross-checks:** `rv_o4_diag_cancel` and the F122 lines import T4-I6's `curved_ref.py`. Everything else is independent of T4-I6's code.
- **Emulation limits:** `rv_wide.py` emulates Wide<2>'s arithmetic class (round to nearest even at p), not Rust bit for bit. The EF uses the exact intended reduced matrix for the attempt's factor.
- **Host:** Python only, under 2 s per script, no heavy job, so no slot. No cargo, no installs, no Git writes, and no job signalled. Scratch was in `WT/scratch/rv131/`. T4's worktree was not touched; its branch was read with `git show` and `git archive` from NUM.
