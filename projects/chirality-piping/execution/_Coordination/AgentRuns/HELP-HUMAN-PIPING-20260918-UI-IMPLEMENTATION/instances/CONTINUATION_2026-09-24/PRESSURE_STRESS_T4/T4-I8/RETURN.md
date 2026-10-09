# T4-I8 RETURN: rebuilt straight-case references (frozen)

- **Who:** TASK T4-I8 (Type 2), for T4's WORKING_ITEMS. Brief `R4/BRIEFS/T4-I8_U2_STRAIGHT_REBUILT_REFERENCES.md` (sha256 `1f294de5…`); terms `R4/BRIEFS/T4_WI_COMMON.md` (sha256 `7d44afd0…`).
- **Status:** frozen before code; ready for the refuting TASK.
- **What was done:** closed forms in exact arithmetic. The product was read for conventions only (`ed012c7ccf`), and the retired cases at `ec5d397359`. There were no builds, runs, cargo or Git writes.

## Plan, stop rules, T3 conditions

- **No stop rule (SP-1 to SP-4) is triggered, and no T3 condition is touched.** SP-1 is carried by case 4 and by the v2/v3 document pair of every case.
- **Partial-span loads cannot be authored on the exact route** (extents exist only for the refused `equivalent_static` wind). The 009 rebuild therefore uses a three-member chain that carries a uniform load on its middle member. The reference is exact.
- **MILLTOL:** the corrosion allowance is folded into the authored wall (0.008 m), with the mill tolerance in its slot (0.00125 m), so t_eff = 0.00675 m as before. The case is marked for re-freeze in T4-U6 if D-5 changes the basis.
- **Generator:** the combined root support's force magnitude, sqrt((29280π)² + 900²), needs a small extension of T1's generator, or must be left out of the package. The twin's values stay in their own fixture format.
- **Proposals:** the v3 wire (`3.0.0/exact_pressure_v3` patch) and the case ids are proposals, pending T4-U2a.

## Cases

| New id | Rebuilds | Content | Key reference values |
|---|---|---|---|
| `EXACT-PRESSURE-MILLTOL-LAME-MEMBRANE-001` | `STRESS-TP-PMM-P3-MILLTOL-EFFECTIVE-WALL-STRESS` (membrane values) | One member; free and axially restrained; transferring closures | σh 28664.558478271286 / 26664.558478271286 Pa; σz free 13332.279239135643, restrained 7999.3675434813857 Pa |
| `EXACT-PRESSURE-THERMAL-TRANSVERSE-MIXED-001` | `MECH-TP-PHYS-008/009` pressure halves | OD 0.2 / wall 0.01; anchor and UX line stop; p 2 MPa, ΔT 5 degC, q −300 N/m on [1.5, 4.5] m | Pressure half Nw = +9720π N (tension 2νP); combined Nw = −13080π N, S = −29280π N; uy(D) = −1701/(137560π) m; anchor Fy 900 N, Mz 2700 N·m |
| `EXACT-PRESSURE-LAME-THIN-WALL-LIMIT-001` | `STRESS-PRESSURE-MEMBRANE-ORIGINAL` | OD 6.5 / wall 0.5, free closed tube | σh 3625/6 and 3025/6, σz 3025/12 Pa. Thin-wall 600 / 300 differ by −1/145 (inner hoop), +23/121 (outer hoop) and +23/121 (σz) |
| `EXACT-PRESSURE-V3-STRAIGHT-TWIN-ODWALL-001` | — (SP-1 twin) | Twin of `SOURCE_ODWALL_EXPECTATIONS.json` case 0 `ordinary` | Bit-equal per mode: every row value, the row set, the maxima, the section and pressure evidence, the standing |

**What each case carries:**
- complete inputs and exact derived section values;
- five-station rows (Nw, S, σz, Lamé, endpoint actions) and transverse rows, with frames and signs;
- displacements and six-component reactions;
- a named zero scale for every zero;
- wrong-result discriminators;
- v2 0.3.0 and 0.4.0 documents plus the provisional v3 patch.

The criterion is relative 1e-9 in both modes.

## Checks

- **`derive_rebuilt_references.py`: 162 checks pass.** They include:
  - the qualified rational table and the 6 m companion, reproduced by the script's own functions;
  - the general Lamé family against the closed forms;
  - an exact direct-stiffness solve against the beam closed form, at every node and station;
  - the retired 009 hand calculation's transverse half (−0.070875 m, −0.014625 rad);
  - 21 twin values against the fixture, each binary64-identical.
- **`check_reference_json.py`:** re-evaluates 235 quantities (decimal to 1e-80, value bitwise), checks 690 rows (378 zero rows with valid scales) and 24 distinct discriminators, and cross-checks the 0.3.0 and 0.4.0 documents. Result: PASS.

## Files (under `R4/T4-I8/`)

`REBUILT_REFERENCE.md`, `rebuilt_reference_cases.json`, `RETURN.md`, `_run_records/derive_rebuilt_references.py` and `.stdout.txt`, `_run_records/check_reference_json.py` and `.stdout.txt`, `SHA256SUMS`.

## Not done

- No product run. The admission of `line_stop`, `weight` N/m element loads and the 0.4.0 sketches on the exact route is read from code, not exercised.
- No elastic stress maxima for cases 1–3.
- No bend cases (T4-I7).
