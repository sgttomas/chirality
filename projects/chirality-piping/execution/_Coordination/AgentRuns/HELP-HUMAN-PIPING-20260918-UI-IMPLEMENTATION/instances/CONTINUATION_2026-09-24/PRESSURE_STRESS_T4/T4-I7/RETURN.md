# T4-I7 RETURN: U2 bend references (freeze)

**Who.** TASK T4-I7 (Type 2), for T4's WORKING_ITEMS. It ran as a harness-native background subagent. No delegation, no Git writes, no cargo.

**Brief.** `R4/BRIEFS/T4-I7_U2_BEND_REFERENCES.md` (`cee2f2dd…`), common terms `T4_WI_COMMON.md` (`7d44afd0…`), at `0c17c8d352`. Conventions were read at `ed012c7ccf`; no product values were used.

**Status.** Frozen, pending refutation by a second TASK.

## Plan, stop rules and T3 conditions

**Nothing changes the plan.** No stop rule fires, and no T3 condition is touched.
- The plan's H-2 ledger was emulated in exact arithmetic, with the arc recovery N_w = N_el + pAi, S = N_el and the station membrane +pAi.
- It reproduces the independent direct references to the file's 20-digit rounding (≤ 4.7e-20) in all 67 cases. That covers displacements, reactions, end rows and stations, including the kinked, reversed, skew and UTM cases.
- F1 and F2 are cross-checks only. The values come from the direct method.

## Delivered

- **`u2_reference_cases.json`:** 67 cases, with complete inputs, expected values, per-case zero-scale floors, negative controls and the polygon control.
  - L free: P, SEPA, SEPD, PT, PW and ALL. L anchored and the four-bend U-loop anchored: P, SEPD, PT, PW and ALL. Each at k = 1 and 2.
  - The rebuilt CBPT (new id `MECH-CURVED-BEND-EXACT-PRESSURE-ARC-K1/K2`, which records the retired id).
  - Two kink controls and one reversed-member control.
  - Five core cases, each also skewed, translated to X = 5e6 and 7.3e6 m (both with and without skew) and in mm/MPa.
- **`u2_document_sketches.json`:** a 0.3.0 and a 0.4.0 document per case, with the provisional pointers listed.
- **`U2_REFERENCE.md`:** derivations, conventions, cases, controls, criteria and limits.
- **`_run_records/`:** the engine, the generator, the cross-check, the precision check and the RV1-seed comparison, each with its stdout.

## How the values were derived

- **The method.** Unit-load flexibility over the whole line in 60-digit decimal:
  - the arc's wetted-wall load (pAi/R) along the outward normal;
  - caps along the end tangents at transferring terminals;
  - physical kink forces;
  - the uniform eigenstrain αΔT − 2νpAi/(E·As);
  - self-weight along −Z;
  - redundants solved at D.

  No curved-element stiffness and no K·u_free is used.
- **The polygon control** (n chords with kink forces) converges at exactly O(n⁻²): the ratio is 4.000 ± 0.003 per halving, and the Richardson limit agrees to ≤ 1e-11. It was run at k = 1 and, as an addition, at k = 2 with chord bending scaled.
- **T4-RV1's independent binary64 F3** agrees to ≤ 4.9e-13.
- **Recomputed at 90 digits with 50-point quadrature,** no written value changes.

## The rebuilt CBPT

- **Tip.** The old ∓1.080861534560850e-4 m becomes ∓4.3234461382433996858e-5 m (×(1−2ν)). The old value is exactly the "Poisson term missing on the arc" mutant.
- **Unchanged:** N_w = P = 80833.984009982862410 N at every station, and V = M = 0.
- **New rows:** S = 0 and σ_m = 1.5054857088526124861e7 Pa.
- **Withheld:** Lamé rows on the arc.

## For the implementer and the refuter

1. **Exact UTM coordinates.** Tests must use the exact binary64 coordinates in the file. A non-dyadic coordinate at 5e6 m moves results by up to 3e-10 relative. The dyadic L and U geometry is exact under any translation.
2. **Tangency tolerance.** The kink controls assume T4-U2 admits a 1e-3 rad kink (N-2). Otherwise regenerate them with a smaller kink.
3. **Anchored SEPD** differs from anchored P only in R_D. It discriminates only in the free family.
4. **Free SEPD and ALL** have linear tip motions of about 1 m and 0.24 rad. Keep them or scale them.
5. **Skewed cases with weight** keep gravity along global −Z. They are new problems, not rotations of their base.
6. **The zero-scale floor** is set per case and per quantity group (per support for reactions). Confirm that grouping.
7. **The provisional sketch fields:**
   - the v3 identity;
   - a bend in a region and on the exact route;
   - the bend's 0.4.0 per-member E/ν, which needs T4-U1.
8. **Not covered:**
   - guides, springs and nonlinear supports;
   - reducers and tees;
   - external pressure;
   - deserialization of the sketches by the product.
