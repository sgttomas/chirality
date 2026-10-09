# T4-RV3 ADDENDUM 01: confirmation of T4-I7's repair round 01

**Who.** T4-RV3 (TASK, Type 2), at the request of T4's WORKING_ITEMS. I made no Git writes and ran no cargo.

**What I checked.** T4-I7's repair round 01 at `fa0b43f3c1`, with SHA256SUMS `daada386…` (all 16 files verify OK) and `R4/T4-I7/REPAIR_01.md`. I compared it against round 00 at `80b1e97e2b`, which `REVIEW.md` refuted.

**The engine is unchanged.** `u2_engine.py` is identical between the two rounds.

## Disposition: CONFIRMED

B-1 and S-1 to S-3 are repaired as I intended. Every new and changed value re-derives with my transfer-matrix solve, and nothing else changed. I have no open items. The round-01 reference set can serve as T4-U2's acceptance basis.

## Evidence

**1. Reproduction** (`rv3_r01_rerun.stdout.txt`). Run from a scratch copy:
- the generator reproduces both JSON files and its stdout byte for byte;
- the cross-check, the precision check, the RV1-seed comparison and `repair01_compare.py` reproduce their stdout byte for byte.

**2. Values** (`rv3_r01_check.stdout.txt`). These come from my round-00 solver, which is unchanged.
- All 79 cases that carry values agree: 34,599 leaves to ≤ 4.68e-20 normalized, which is the file's 20-digit rounding. The new cases and the elastic chord rows are included.
- Every zero_scale equals its group maximum, and every floor = 1e-9·zero_scale.
- For the identically-zero elastic group, the fallback is pAi, following the file's rule.
- `derived.junction_angles_rad` matches my angles to ≤ 4e-24 rad.

**3. B-1** (`rv3_r01_diff.stdout.txt`, my own diff; `rv3_r01_controls.stdout.txt`).
- **The 20 rows in surviving cases.** Of my 23 round-00 rows, the 20 in U2-L-FREE-P-K2 and CBPT-K2 are exactly the rows removed. Each is in `rows_dropped_repair_01` with a correct reason, and every other row is kept byte for byte.
- **The other 3.** They were in the kink control, which was regenerated with the new geometry. Its 3 dropped rows are the new control's support A Fz and Mx (0 = 0) and Fy (125 tolerances).
- **Every listed row now discriminates.** Round 01 lists 263 rows: all are at ≥ 1e3 tolerances (the least is 2.3e4), none prints a zero in exponent form, and each control's top row equals its `max_distance_in_tolerances`.
- **Wrong values re-derived.** My solver reproduces every listed wrong value to ≤ 1.1e-16, including the regenerated kink controls and the new U2-L-ANCH-PTW-K2 set.
- **Maxima unchanged.** The maximum distances of the surviving cases are unchanged.

**4. S-1** (`rv3_r01_elastic.stdout.txt`).

I re-formed `chord_frame_elastic` as K_b(d − u_free(ε_p + ε_th)) − p_w from my own pieces, not from wall − c_b:
- K_b, from the inverse of my transfer-matrix tip flexibility, assembled over the chord;
- my node motions;
- my clamped-clamped self-weight actions.

It agrees to ≤ 4.56e-20 over every arc in the 79 cases. The tangent-frame identity N_el = N_w − pAi holds to 5.2e-21.

**The mapping is right.**
- Today's arc rows `element_local_*` (`arc_chord_frame`) are K·d − K·u_free(thermal) − the consistent equivalents. They are node-on-element, in the pipe frame: x along the chord, y = `y_reference` projected, z = x × y (`PPL:10880-10958,11100-11160@ed012c7ccf`; `preview_physics.rs:25`).
- This holds provided T4-U2 treats the bend term's K_b·u_free(ε_p) like the thermal free expansion, and does not subtract c_b as an equivalent. That is the plan's N_w = N_el + pAi form, and the row map says so.

**A correction to REVIEW S-1.** The elastic value there is −396.08167949273772476 N, as the repair states, not "about −396.3 N" as I wrote.

**5. S-2** (`rv3_r01_kink.stdout.txt`).
- **Kink controls,** D.x = 3.248 (binary64 3.24800000000000022…):
  - θ = 4.9999995833328447e-4 rad;
  - it sits 5.0e-4 rad under α_tan by the atan2 measure, and below α_tan by the tan, sin and 1 − cos measures alike;
  - binary64 errs by 6e-20 rad.
- **Refusal control,** D.x = 3.242:
  - θ = 1.9999973333397350e-3 rad;
  - it sits 1.0e-3 rad over α_tan by every measure, and binary64 refuses it;
  - `expected_refusal` (blocking, `PRESSURE_REGION_MITRE_UNSUPPORTED`, refs [region, node:C, pipe:BEND, pipe:S2], no values) matches T4-I11's message design.

**6. S-3.**
- **13 new cases.** The PTW inputs and both sketches have both terminals `transfers_to_wall`, ΔT = 50 °C and w = 430.95… N/m.
- **Values.** They re-derive. Anchored PTW equals ALL except for R_D (shifted by −pAi·t_D) and the D terminal block, for both L and U.
- **Controls and transforms.** The PTW-K2 controls re-derive, with maxima from 8.4e6 to 1.25e11 tolerances. The six transforms agree.

**7. Nothing else changed** (`rv3_r01_diff.stdout.txt`).
- **Surviving cases.** Of the 36,463 round-00 leaves in the 65 surviving cases (expected, zero_scale, derived), none changed.
  - **Removed:** only the wall-basis chord block (1,356 leaves) and its 260 zero-scale fields.
  - **Added:** only `chord_frame_elastic`, its group, `alpha_tan_provisional_rad` and `junction_angles_rad`.
  - **Other fields:** no other case field differs.
- **The kink cases** differ only in node:D x (3.246 → 3.248), in both the inputs and the sketches.
- **Other files.** The 65 surviving sketches are identical. The 8 polygon entries are unchanged, with 2 added.
- **The header** changes only in author, revision, criteria (the listing rule), `tangency_rule`, sign_conventions, row_kind_map_today and the polygon additions.

**8. The floors** (`rv3_r01_float.stdout.txt`). A binary64 emulation of the H-2 path stays at ≤ 9.3e-4 of every floor in ten cases. These include the PTW cases, the kink cases, the UTM-skew PTW case and the elastic chord rows.

**Note, no action needed.** The refusal control's document sketches carry no refusal marker; its expectation lives only in `u2_reference_cases.json`.

## New records (`_run_records/`, run with `python -I -B`)

| Script | Output |
|---|---|
| `rv3_r01_rerun.py` | `rv3_r01_rerun.stdout.txt` |
| `rv3_r01_check.py` | `rv3_r01_check.stdout.txt` |
| `rv3_r01_elastic.py` | `rv3_r01_elastic.stdout.txt` |
| `rv3_r01_diff.py` | `rv3_r01_diff.stdout.txt` (the round-00 directory was extracted with `git -C NUM4 show 80b1e97e2b:<path>`) |
| `rv3_r01_controls.py` | `rv3_r01_controls.stdout.txt` |
| `rv3_r01_kink.py` | `rv3_r01_kink.stdout.txt` |
| `rv3_r01_float.py` | `rv3_r01_float.stdout.txt` |

Round-00 records are unchanged. `SHA256SUMS` covers every file.
