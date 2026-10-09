# T4-I12 RETURN: T4-U3 references (frozen)

- **Who:** TASK T4-I12 (Type 2), for T4's WORKING_ITEMS. Brief `R4/BRIEFS/T4-I12_U3_REFERENCES.md` (sha256 `1c7bb2f1…`); terms `R4/BRIEFS/T4_WI_COMMON.md` (sha256 `7d44afd0…`). Rulings applied: annotation-only joints are not admitted on the exact route; topology `replaces_span` only.
- **Status:** frozen before code; ready for the refuting TASK.
- **What was done:** exact-rational derivations from JR §2. The product was read for conventions only (`ed012c7ccf`), and the NI algorithm was read for item 8. There were no builds, no cargo, no product runs and no Git writes.

## Plan, stop rules, T3 conditions

- **No stop rule (SP-1 to SP-4) is triggered, and no T3 condition is touched.**
- **JR: 75 of 75 comparisons agree exactly.** The one partial agreement is the refutation's finite-rotation decimals (L = 2, φ = 0.1), which match to 13 digits only, because of binary64 cancellation. The exact values are frozen instead.
- **The 658.44 N·m is not reproducible under v3.** It belongs to the legacy model: pressure, nonlinear supports and the old element. The v3 analogue of the old element's imbalance is 770 N·m (L-100), 275 N·m (L-200) and 440 N·m (L-300). These are discriminators; the connector balances exactly.
- **The demo re-authoring drops** the bend, branch, valve and terminal markers, the nonlinear and constant-effort supports, the pressure loads and the combination. **L-300** is added to cover all six connector coordinates. Admission of the document is inferred from code, not run (U3_REFERENCE §0.5).
- **NI:** the replacement keeps the fixture's own section (E 100, G 40, A 1, I 1, J 1), with node 1 at (3, −4, 0). The structure is preserved and the constants change (U3_REFERENCE §5).
- **Not frozen:** J3 and J4 (T4-U5), series and parallel topologies (refused under the ruling), and a 0.4.0 form of the system case.

## Cases (18; `u3_reference_cases.json`)

| Item | Cases | Key values |
|---|---|---|
| 1 | J1, J1 common rotation, J2, J2 held, refutation end moment, six components | 80 N, 0.04 J, Mᵢ_z = Mⱼ_z = −12; q = 0; 12 N·m, 0.06 J; Mⱼ_z = 30 = (krz + ky L²/4)φ |
| 2 | B oracle | Mᵢ = (−42/5, 87/5, −43/5), Mⱼ = (10, −9/2, 157/10); work 1567/170 |
| 3 | generic skew/offset/prestress; W4 link rule | rank B = 6; PD → null(Ke) = 6 rigid modes; PSD → rank 2, null dimension 10; indefinite → pivot −9/4, reject |
| 4 | offsets, covariance, coupled H/scale/preload, preload relief, reversal | 0.075 J; H′ = (1, 0.5, 9); RHS = +BᵀKq_ref; relief g = 0; reversal blocks exchanged |
| 5 | finite rotation | qt = [L(cos φ − 1), L(sin φ − φ), 0] at 3 (L, φ) pairs, to 40 digits |
| 6 | `U3-SYS-DEMO-CONNECTOR-001` | L-100 g = (253.553038291, 350, 0, 0, 0, 385); reactions to 30 digits; balance exact |
| 7 | raw difference; refusal variants | 240 N / 0.36 J; `JOINT_REPLACED_SPAN_LOAD_UNOWNED` (weight and thermal on P-130) |
| 8 | NI friction frame | (10, −10): u = 4375/7404, N = 4350/617, f = −1305/617; the retry and final values are in §5 |

## Checks

- `u3_reference.py`: 761 of 761 pass. They include:
  - closed-form B against kinematic B;
  - Bᵀg against the closed-form blocks;
  - rigid modes, ranks, balance and virtual work;
  - frame-sign self-tests;
  - system balance below 1e-100;
  - the NI model reproducing all 20 old pinned values (12 distinct magnitudes).
- `check_reference_json.py`: 508 of 508 pass. It is a rigid-arm reformulation from the JSON inputs, plus system statics from the frozen values.
- `probe_binary64.py`: a naive binary64 solve meets the system criterion with worst error 3.1e-14.

## Criteria

- FK identities: exact; product at relative 1e-12. Finite rotation: 1e-12·L.
- System: both modes, relative 1e-9 with per-family zero-scale floors.
- NI: 1e-12. No new threshold.

## Files (under `R4/T4-I12/`)

`U3_REFERENCE.md`, `u3_reference_cases.json`, `RETURN.md`, `_run_records/{u3_reference.py, u3_reference.stdout.txt, check_reference_json.py, check_reference_json.stdout.txt, probe_binary64.py, probe_binary64.stdout.txt}`, `SHA256SUMS`.
