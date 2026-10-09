# T4-RV2: refutation of T4-I6's references for T4-U0 and T4-U1

TASK T4-RV2 (Type 2), for T4's WORKING_ITEMS.
- **Brief:** `R4/BRIEFS/T4-RV_REFERENCE_REFUTATION.md` (`816c20ab…`), with `T4_WI_COMMON.md` (`7d44afd0…`).
- **Target:** `R4/T4-I6/` at `4a5c65e38a`. Its SHA256SUMS digest `146f734a…` is verified, 16 files OK.
- **Bases:** code `ed012c7ccf`; T3's records at NUM `70aa51b076`. Abbreviations are T4-I6's (`CB`, `KM`, `KT`, `FCR`, `PRT`, `PPL`).
- **Labels:** **F** = read from bytes or computed by my scripts. **I** = inference. **Emulation** = my binary64 model of a plausible implementation, never product code.
- **Assumed decision:** the WI log's "Small bends settled" line (stable binary64 element; CB's 1e-9 floor kept).

## Disposition: PASS WITH FINDINGS

There are no BLOCKING findings.
- I re-derived every frozen value by a different method. Each one agrees to the JSON's 20-digit rounding.
- K1 and K2 discriminate under a stable evaluation, with large margins.
- The four SHOULD-FIX findings and the NOTEs are in §3. None changes a frozen number.

## 1. Method (different from T4-I6's)

- **T4-I6's own scripts.** I re-ran all six from their stated inputs. `u1_reference_cases.json`, PART1 (`b864c145…`) and all five stdout files are byte-identical.
- **An independent reference element (`rv2_lib.py`).**
  - The arc centre is formed exactly, at 100 digits, from d, R and the bow vector.
  - F is a 48-point Gauss–Legendre quadrature of the complementary energy. Moving to 64 points changes it by at most 8e-93. The section actions come from global vectors: M(θ) = M + (x_j − P(θ)) × F.
  - K = Bᵀ F⁻¹ B, with B the global compatibility matrix. There is no local frame, action table, Gram matrix, H or T.
  - π, sin, cos and the half angle are my own code.
  - Self-checks: Castigliano's quarter-circle closed forms (in-plane (3π/4 − 2)R³/EI and πR³/4EI; Roark's out-of-plane form) agree to 1e-40 and 1e-59; the straight limit is met; the null space holds to 8e-59.
- **Binary64 emulations of a stable T4-U1 element (`emu64.py`).**
  - Geometry from half angles. F either by 16-point Gauss–Legendre with cancellation-free arm differences ("GL") or as the exact F rounded once ("CR").
  - Then a binary64 inverse, H from (−sL, cL, 0) and the transform.
  - LU (with pivoting) and Cholesky solves.
  - **K-D5's estimate:** ρ exact, w with the product factor, FK's body scales, factor 2.

## 2. Results by attack

### 2.1 K1 and K2 under the stable evaluation (F: `kill_analysis`, `o4_check`)

**K1 at φ = 1e-8**, at X = 0 and X = 5e6, which give identical results. The ranges cover GL and CR, LU and Cholesky. A trigger above 1 demotes.

| Configuration | IP: actual / trigger | SK: actual / trigger |
|---|---|---|
| Correct product, correct check | 2.3e-5–3.0e-5 / 4.5e-5–6.1e-5 | 1.4e-5–2.8e-5 / 2.7e-5–5.7e-5 |
| M31b check, cos rounded to nearest (= 1.0) | — / **12.74** | — / **12.45** |
| M31b check, cos one ulp low | — / 15.55 | — / 15.19 |
| Product formula-chord mutant (correct check) | 6.37 / 12.74 | 6.23 / 12.45 |
| **K2:** system = mutant; checked by the correct check / M31b / M31a | — / 12.74 / ≤ 5.8e-5 / ≤ 2.6e-5 | — / 12.45 / ≤ 6.8e-5 / ≤ 6.1e-5 |

**K1's two conditions both hold.**
- **(a) The correct product stays Passed.** Actual and trigger are at most 6.1e-5, a margin of at least 1.6e4 against 0.5 and against 1. I6's crK figures (9.4e-6 and 7.0e-6) are consistent with this.
- **(b) M31b demotes it.** The trigger is 12.4 to 15.6 times the threshold, whichever way cos(φ_b) rounds.

**K1 is statically determinate in its element.** The root rotation is M/k exactly, and the element carries a pure moment. So only the chord and the moment columns of F reach u:
- K-D5's p ≈ 128 closed form leaves the K1 trigger at 6.07e-5 even at 1e-9, where its K error is 4.5e-11.
- On an indeterminate tip-spring model at 1e-9, the same error moves the trigger from 2.8e-7 to 5.1e-3 at 38 digits, and to 1.9e-4 at 39 digits. O4 is therefore real but far below 1 there.

**K2 meets T3's literal alternative,** "an equivalent kernel-level kill".
- It runs K-D5's curved re-formation, exact residual, correction solve, S* and rule, and demotes 12.5–12.7 times, independent of the product's rounding.
- It kills M31b and M31a: both leave the case undemoted.
- It kills M31b only if the system matrix's formula chord equals M31b's bit for bit. A system built with cos rounded to nearest, checked by an M31b with cos one ulp low, demotes at 28.3, and M31b survives (N-4).

**The kill angles do not form an interval.** M31b's trigger is 12.7 at 1e-8, 0.25 at 1.5e-8, 2.8 at 2e-8, 0.50 at 3e-8 and 1.47 at 5e-8. It follows the rounding error of fl(cos φ_b). 1e-8 is the strong point, where cos rounds to 1 with an error of 0.45 ulp.

### 2.2 The element definition and the frozen K (F: `compare_k`, `t3check`, `utm_legacy`)

- **All 49 cases**, at 1e-4, 1e-8 and π − 1e-6 and on the skew planes, base and rotated, including CB's toy with k_in ≠ k_out:
  - max|ΔK|/max|K| ≤ 3.7e-20 and entrywise ≤ 4.8e-20, which is the 20-digit rounding;
  - φ agrees to at most 3e-25 relative.
- **The 8 UTM controls** agree to 3.1e-20.
- **Coordinates.** Every node coordinate lies on the 2⁻³⁰ grid with |x| < 2²³, and binary64 x_j − x_i equals d at every X. For the controls, binary64 d is exact, and my emulation of today's PP centre and CB check refuses all 8, with I6's mismatches to 4 digits.
- **T3's models (19) and the K1 sweep (32):** I6's u_int agrees with my independent solves to at most 5.0e-11 of the criterion. I6's "old→new" column is reproduced to 4 digits.
- **O6 is confirmed.** The cosine between the member y_reference and the old arc's bow is −1 for CPLANAR_60 and −0.745 for CSKEW_30_N122. For RV5's models it is +0.59 (CANT30), +0.24 (CANT10) and −1 (PP_UTM).
- **B1's conventions** (frames, bow side, DOF order, k_in on M·z and k_out on M·e_r, no shear) are confirmed by the agreement of my global derivation.

### 2.3 Properties P1–P5 (F: `props_check`, `p4_looseness`)

**Stable emulation, all B2 cases and controls:**

| Property | Result | Criterion |
|---|---|---|
| P1 | ≤ 1.4e-14 (margin ≥ 700) | 1e-11 |
| P2 (exact P) | ≤ 4.7e-16 | — |
| P4 | ≤ 2.1e-15, except π − 1e-6 IP and rotated: up to 3.7e-10 (diagonal-scaled 5.3e-10) | 1e-9 |

- **The near-π residue** comes from c = √((2R − L)(2R + L))/2R with a binary64 L: its relative error is about 7e-4 there. This is O7's mechanism, already active at 1e-6 (N-2).
- **The 2⁻³⁰ translation construction is correct.** P3 follows for any product that forms K from (d, R, y).
- **Today's path (emulated):**
  - P1 is 3.8e-10 to 1.1e-9 at 5e6 and 7.3e6 where it is not refused;
  - at 5e5 and 2e6 it is as low as 2.0e-12 (B90-SK) and 1.6e-16 (B90-IP, where the centre happens to be exact);
  - its P4 is mostly below 1e-9 (N-3).
- **P4's matrix scale:** max|K|/min K_ii reaches 1.13e4 (B5-IP) (S-4).

### 2.4 T4-U0 (F: read at `ed012c7ccf`)

**Confirmed:**
- **The three readers:** Rust `RE/src/physics_evidence.rs:627` gives `SOURCE_PHYSICS_PRESSURE_RANGE`; Python `physics_evidence.py:158` gives `…EVIDENCE_INVALID: region pressure basis`; TypeScript `physicsResultEvidence.ts` (the `PRESSURE_INVALID` demand) gives `PHYSICS_EVIDENCE_PRESSURE_INVALID`. All three test `>= 0`, so all three admit −0.0. `value < 0.0` matches them.
- **Units.** There are seven pressure units, all with linear factors ≥ 1.
- **Code naming.** `PRESSURE_REGION_PRESSURE_INVALID` exists (`PRT:382,493`). The refs and ids follow `stable_suffix` (`PPL:13653`).
- **Order.** The order `validate_profile` → `validate_document` → `validate_model_inputs` → `validate_support_family_tokens` (`PPL:2365-2368`) holds. All six precedence claims hold as emission order.
- **The A1 shapes deserialize** (no `deny_unknown_fields`).
- **The untested codes.** No test names the composition, combination or connector codes.
- **A2.6** reaches the refusal through `assemble` → `build_pressure_case_with_members` → `validate_profile` (`PRT:434`).
- **Both flagged re-derivations are right:**
  - `pressure_grouping_limits.rs`: the group sums are cap −sign and Poisson sign·2ν per region (`PRT:700-725`), so p₁Ai₁(1−2ν) − 2νp₂Ai₂ ≈ −1e-13·p₁Ai₁(1−2ν). The screen is about 0.14, against 1e-9.
  - `PRT:1289`: with p = +3, `cap_loads[0]` is −3π.

**Problems:**
- Two more tests use p < 0 (S-2).
- A3's Option 2 cannot be built (S-3).

### 2.5 Re-mapping of T3's required kills (`KT`, `FCR` at `ed012c7ccf`)

| Test | Reading |
|---|---|
| `KT:447` | Preconditions are actual > 1 and demotion, which become unconstructible. The replacement by SA K1 (Passed, actual < 0.5, `assert_unchanged`, in both modes) kills M31b and the product mutant (§2.1) |
| `FCR:379` | `actual > 1` fails by design. The 5e6 control plus a PP K1 at (5e6, 3.5e6, 0) is sound: x₁ and R parse to the exact grid values. But `pp_route_elbow_request` hard-codes R = 0.3 m (N-5) |
| `FCR:358` | Correct as stated |
| `KT:419` | Correct as stated; M31a moves to K2 |
| Expansion-joint and E1/E6 tests | Unaffected |

The FK curved tests (`formation_check_tests.rs:69,276`) and SA's matching tests (`KT:504,523`) change with the input set. They are not T3's required kills (N-6).

## 3. Findings

### S-1 (SHOULD-FIX). T3's demotion condition is answered with a small-angle construct, contrary to HELP_HUMAN's restatement

- **Affected claim:** B5.2's last row and RETURN item 3, "K2 meets the condition", and B4's inference that the actual error is likely below 1, with no product model demoting robustly.
- **What the rulings require.** HELP_HUMAN's ruling (T4_RULINGS, "Very small realized bends") says the demotion must come "from conditioning rather than from small angles". The WI log adds: "T4-U1's reference work confirms one exists". K2 relies on fl(cos 1e-8) = 1, and it is not a product model.
- **The evidence.**
  - crK (correct rounding) is not what a product does.
  - Emulated stable products on the CSKEW cantilever at the rcond edge (equilibrated cond 5.5e7, 6.2e7 and 6.5e7 for k_X = 10, 9 and 8.5; R5_4's estimator gives 5.5e7, 6.1e7 and 6.4e7) show actual 0.02–2.30. K-D5 demotes in 9 of 12 configurations, with EF = actual (`cond_tp`).
  - At k_X = 8, cond 6.9e7 is already above 1/√ε.
- **Consequence.** As written, T4-U1 could close T3's condition on K2 alone, against the ruling. At the same time, `KT:400` may in fact still pass.
- **Repair.**
  - State the ruling's qualifier.
  - Name CSKEW_8_5, _9 and _10 in both modes (u_int already frozen) as the conditioning candidates. T4-U1's acceptance: at least one demotes with actual > 0.5 and EF/actual within 1e-3. If none does, sweep k_X toward the rcond limit.
  - Keep K2 as the robust M31a/M31b kill.
  - Route "K2 alone" to WI/HELP_HUMAN if no candidate demotes.

### S-2 (SHOULD-FIX). Two more tests break under the p < 0 refusal

- **Affected claim:** U0 §A2, "Tests that change", and the SP-1 list of declared differences (only two tests).
- **The tests:**
  - `PP/tests/pressure_runtime.rs:649` `signed_pressure_zero_poisson_and_thermal_reversal_preserve_the_selected_equations`: rows (−2e6, 0.3, free/fixed) at `:653-654` assert a solved result.
  - `:1047` `same_region_id_in_distinct_cases_has_unique_binding_and_order_independent_maximum`: `case:a-negative` uses −2e6/−4e6 at `:1057`, with signed wall-force and displacement checks.
- **Consequence:** an incomplete declared-difference list and test plan.
- **Repair.**
  - Replace the first test's rows with +2e6, ν = 0.3, free and fixed, so that ν-with-pressure coverage stays.
  - Re-derive the second with p ≥ 0: tied = equal p; untied = 2e6/4e6. Note that the signed discriminator of the tied variant is lost.
  - Extend `neg_scan` with a code grep: it reads `.json` only and skips unparsable files silently.

### S-3 (SHOULD-FIX). A3's Option 2 cannot be built, and its "precondition shows the hazard" is wrong

- **Affected claim:** U0 §A3, "How a test reaches each".
- **Why.** `solve_load_case_observed` builds the exact case itself through `build_pressure_case_with_members` (`PPL:4038`). That re-runs `validate_profile` (`PRT:434`), which refuses the bend. The solve then returns early with no results (`PPL:4057-4072`).
- **So:** no seam accepts a constructed `ExactPressureCase`, and with the fix reverted nothing reaches `:5494`.
- **Repair.**
  - Specify Option 1, or a `#[cfg(test)]` seam that bypasses the component refusal inside the builder.
  - State that Option 1 pins only the decision functions.
  - The call-site wiring is then pinned by the end-to-end no-panic, no-maximum test, which must land in the PR where T4-U2a lifts the refusal.

### S-4 (SHOULD-FIX). P4's matrix-scale criterion can hide real errors

- **Affected claim:** B3 P4, |ΔK_ij| ≤ 1e-9·max|K_ref|, with the diagonal-scaled measure informative only.
- **Why.** max|K|/min K_ii reaches 1.1e4 (B5) and 180 (1e-8). A relative error of up to 1e-5 in the rotational stiffness of a 5° bend passes P4. No model-level acceptance reference covers 1e-4.
- **Floors.** My stable emulations give a diagonal-scaled error ≤ 3e-15 everywhere except π − 1e-6 (5.3e-10, removed by O7).
- **Repair:**
  - make |ΔK_ij| ≤ 1e-9·√(K_ii K_jj) normative alongside P4, with O7 applied near π;
  - or declare the K1 sweep's 1e-4 and 1e-6 models as model-level acceptance.

### NOTEs

- **N-1.** O4 does not touch K1 (§2.1). I6's "≤ 0.1 of the criterion" is a conservative bound, not a measured effect. K1 does not exercise the stable force–force flexibility; only P4 and S-4 do.
- **N-2.** O7's remedy (4R² − |d|² with an accurate |d|²) is needed from about π − 1e-6, not only below 3e-8. Without it, P4 has about 2.7 times margin at B2's π − 1e-6 IP case.
- **N-3.** B3's rationale that the 1e-11 threshold "separates by more than 20× on each side" overstates the defect at 5e5 and 2e6 (§2.3). The criterion is fine. Today's path fails the set through P1 at 5e6 and 7.3e6, and through P5.
- **N-4.** K2 transport.
  - CB depends on FK, so an FK test cannot call CB's chord override. Freeze the binary64 system matrix in the JSON, or form it in the test independently of the patched code.
  - Pin fl(cos φ_b) = 1.0 as a precondition (§2.1).
  - The JSON carries no K2 matrix.
- **N-5.** The PP K1 needs `pp_route_elbow_request` to take the radius, and its y and z are fixed at +y and 0. So only K1-IP can use it, as specified.
- **N-6.** The FK and SA curved tests that change with the input set (§2.5) belong in T4-U1's re-agreement list.
- **N-7.** U0's A1.7 and A1.8 pin connector codes that T4-U3 will change (the live connector and the legacy code first). Mark them as T4-U3 re-agreements.
- **N-8.** P5's seeded generator must state its angle range. Angles outside [1e-9, π − 1e-9] are legitimately refused.
- **N-9.** B5.1 says "only for φ ≲ 2e-8". A kill also exists at 5e-8 (1.47), and none at 1.5e-8 (§2.1). O3's dependency is unchanged.
- **B5.3 (out of scope).** I noticed nothing in passing.

## 4. Records

`R4/T4-RV2/_run_records/` holds the scripts, each with its stdout, and `RUN.txt` with the commands and inputs. `R4/T4-RV2/SHA256SUMS` covers every file written. Nothing is committed.
