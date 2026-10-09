# T4-I6 return: references for T4-U0 and T4-U1 (frozen)

- **Who:** TASK T4-I6 (Type 2), for T4's WORKING_ITEMS.
- **Brief and terms:** `R4/BRIEFS/T4-I6_U0_U1_REFERENCES.md` (sha256 `71f6ab04…`), with `T4_WI_COMMON.md` (`7d44afd0…`), both at `0c17c8d352`.
- **Code basis:** `ed012c7ccf`.
- **T3 records:** NUM `70aa51b076`.
- **WORKING_ITEMS' note:** its added note on M31b is answered in `U1_REFERENCE.md` §B5.
- **Method:** standard-library Python only (`_run_records/RUN.txt`). No cargo, no product code run, and no Git writes.

## Leading items: T3 conditions, plan effects and stop rules

1. **M31b has a constructible kill only at tiny angles; M31b0 has none (T3 conditions 1 and 2).**
   - **Why.** Under T4-U1's definition, the formula chord equals the actual chord exactly. So M31b differs only by binary64 rounding, which is visible only where cos φ − 1 cancels: φ ≲ 2e-8.
   - **K1.** A PP-admissible cantilever with a φ = 1e-8 bend (R ≈ 3e7 m, chord 0.3 m), at X = 0 and at (5e6, 3.5e6).
     - The product's formula-chord mutant errs by 6.4 (in-plane) and 6.2 (skew) times the criterion.
     - M31b falsely demotes the correct product (trigger about 12.7).
     - The correct pair stays Passed and is not demoted.
   - **K2.** A kernel-level `formation_check` kill: system matrix = the mutant, source = the correct inputs.
     - It gives a curved K-D5 demotion by construction.
     - It kills M31b and M31a.
   - **The required tests.**
     - `kd5_tests.rs:447` is replaced by K1 at the SA level.
     - `formation_check_runtime.rs:379` becomes a UTM control, and its M31b role moves to K1 at the PP level.
     - `:358` stays, with u_int regenerated.
   - **M31b0** is equivalent by construction. The derivation is in §B5.3. **This is a narrowing for ROOT, not settled.** Under RR:1217 it needs an independent check.
2. **Plan effect on T4-U1: small-angle accuracy.**
   - A naive binary64 evaluation of the closed-form flexibility misses the 1e-9 agreement below about 4e-3 rad: 3e-4 at 1e-4, and 4 at 1e-8.
   - The briefed 1e-4 and near-limit references, and K1, require a cancellation-free evaluation (series). That is likely more than today's CB does.
   - The effort estimate of 2–4 days may grow.
3. **CSKEW_8_5 (T3 condition 2) is not settled by reading.**
   - Correctly rounded formation contributes about 0.01 of the criterion. R5_4's solve-only figures were 0.25 (dense) and 0.64 (sparse).
   - **I:** `kd5_tests.rs:400` ("demotes in both modes") probably fails by design. T4-U1 runs it and T3 agrees the outcome. K2 meets the condition "a curved model is still demoted".
4. **T3 point.** K-D5's closed forms at p = 128 err by 4.5e-11 relative at φ = 1e-9, the product's lower limit. That risks a false demotion there (4e-14 at 1e-8).
5. **Regeneration (T3 condition 3).** The member `y_reference` in `kd5_models.rs` does not describe the arcs of CPLANAR_60 and CSKEW_30_N122, and RV5's is a placeholder. Regeneration must use the bow vectors given in `t3_models.regenerated_bend_inputs`.
6. **T4-U0 and SP-1.**
   - The p < 0 refusal changes no committed document: 0 of 166 JSON files carry p < 0.
   - It does take away the only public test of the cancellation guard (`pressure_grouping_limits.rs:97-122`, which uses p < 0). A re-derivation with p ≥ 0 is given in `U0_REFERENCE.md` §A2.
   - −0.0 is admitted, matching all three readers, so its bytes are unchanged.
7. **No stop rule (SP-1 to SP-4) is triggered by these references.**

## Index

| Record | Content |
|---|---|
| `U0_REFERENCE.md` | A0 shared facts; A1 the three untested refusals (each trigger, the 0.4.0 form, precedence tests, runner); A2 the p < 0 refusal (proposed code `PRESSURE_REGION_PRESSURE_NEGATIVE`, the signed-zero rule, the readers' codes, the two tests to re-derive, the byte evidence); A3 the `.expect` refusal (`EXACT_PRESSURE_REGION_MEMBER_NOT_STRAIGHT`) and the withheld arc maximum, with how unit tests reach them before T4-U2a |
| `U1_REFERENCE.md` | B1 the element defined mathematically (inputs, objective geometry, action table, Gram, H from A·d), with the numerical requirements; B2 the frozen set; B3 properties P1–P5 with criteria and floors, and the translation construction; B4 T3's breaches and the K-D5/CB models; B5 negative controls (K1, K2, the test mapping, the M31b0 narrowing, the large-coordinate controls); B6 SSLL101; B7 open points |
| `u1_reference_cases.json` | `cases` (49 elements, each K at 20 digits and valid at X = 0, 5e5, 2e6, 5e6 and 7.3e6 m); `generic_rotation_pairs`; `naive_binary64_emulation_sweep`; `t3_models` (re-derived u_int); `m31b_kill_and_mutant` (K1, with the angle sweep); `mutant_element_level`; `utm_controls_refused_today` (8 elbows with K) |
| `_run_records/` | `curved_ref.py`, `freeze_u1.py`, `t3_models.py`, `selftest.py`, `p128_closed_form_precision.py` and `neg_scan.py`, each with its stdout; `RUN.txt` |

**SSLL101:** not matching. The assets are not vendored. Model A is shear-deformable straight segments with reduced inertias. The references are ±2%. There is no pressure case (§B6).

## Open points

O1 to O7 are in `U1_REFERENCE.md` §B7:
- O1: small-angle F;
- O2: the M31b0 narrowing;
- O3: keep φ ≤ 2e-8 admissible;
- O4: K-D5's precision at 1e-9;
- O5: CSKEW_8_5;
- O6: y_reference on regeneration;
- O7: near π, form 4R² − |d|² exactly.

From Part A: the factoring choice for A3's unit tests (Option 1 recommended).
