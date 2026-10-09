# T4-I8 RETURN: rebuilt straight-case references (frozen; repair round 01)

- **Who:** TASK T4-I8 (Type 2), for T4's WORKING_ITEMS. Brief `R4/BRIEFS/T4-I8_U2_STRAIGHT_REBUILT_REFERENCES.md` (sha256 `1f294de5…`); terms `R4/BRIEFS/T4_WI_COMMON.md` (sha256 `7d44afd0…`).
- **Status:**
  - Frozen at `61b4e0b460`. T4-RV4 refuted it: PASS WITH FINDINGS, nothing blocking.
  - This is repair round 01 (`REPAIR_01.md`), which closes S-1 to S-4 and N-2 to N-4.
  - **No frozen value changed:** all 235 round-00 quantities are identical.
- **What was done:** closed forms in exact arithmetic. The product was read for conventions only (`ed012c7ccf`), and the retired cases at `ec5d397359`. There were no builds, product runs, cargo or Git writes.

## Plan, stop rules, T3 conditions

- **No stop rule (SP-1 to SP-4) is triggered, and no T3 condition is touched.**
- **D-6 against SP-1 (T4-U8 planning point, from S-2).** If Timoshenko becomes the exact-route default, a straight v3 document cannot stay bit-equal to its Euler–Bernoulli v2 twin, unless the v3 side selects Euler–Bernoulli or SP-1's straight-v3 clause is scoped to that selection. Case 2's uy rows and the twin's tip deflection are tagged for re-freeze in T4-U8.
- **Partial-span loads cannot be authored on the exact route.** The 009 rebuild uses a three-member chain; RV4 confirmed this is forced and sound.
- **MILLTOL:** the allowance is folded into the authored wall (0.008 m), and the mill tolerance stays in its slot. Re-freeze in T4-U6 if D-5 changes the basis.
- **Package generator:** T1's generator accepts every row through its own functions except:
  - 150 MPa stress rows, which need the exact factor Pa→MPa added;
  - 3 symbolic rows, which need the forms `sqrt((a*pi)^2 + (b)^2)` and `a + (b)/pi`.

  Add these, or leave the rows out.
- **Proposals:** the v3 wire and the case ids remain proposals, pending T4-U2a.

## Cases

| New id | Rebuilds | Key reference values |
|---|---|---|
| `EXACT-PRESSURE-MILLTOL-LAME-MEMBRANE-001` | MILLTOL membrane values | σh 28664.558478271286 / 26664.558478271286 Pa; σz (= maximum) 13332.279239135643 free, 7999.3675434813857 restrained |
| `EXACT-PRESSURE-THERMAL-TRANSVERSE-MIXED-001` | TP-PHYS-008/009 pressure halves | Pressure half Nw = +9720π N; combined Nw = −13080π, S = −29280π N; uy(D) = −1701/(137560π) m; anchor Fy 900 N, Mz 2700 N·m; bending stress M/Z; maxima to 16880566.358781446 Pa |
| `EXACT-PRESSURE-LAME-THIN-WALL-LIMIT-001` | PRESSURE-MEMBRANE | σh 3625/6, 3025/6; σz 3025/12 Pa; thin-wall differences −1/145, +23/121, +23/121 |
| `EXACT-PRESSURE-V3-STRAIGHT-TWIN-ODWALL-001` | SP-1 twin (SOURCE_ODWALL case 0) | `/sp1_pair_scope`; the fixture's values |
| `EXACT-PRESSURE-V3-STRAIGHT-TWIN-SEPARATE-CLOSURES-001` (new) | SP-1 twin with separate closures (six-state document) | Nw = 3000π, S = −2000π N, root Fx −3000π |

**`/sp1_pair_scope`** has three clauses, applies to every pair, and is restricted to p ≥ 0:
1. the v2 envelope is byte-identical to the base revision's;
2. every numeric leaf of v3 is bit-equal to v2's, with non-numeric leaves equal except the closed list E1–E5;
3. per mode and per schema version.

## Checks

| Script | Result |
|---|---|
| `derive_rebuilt_references.py` | 177 checks pass |
| `check_reference_json.py` | 284 quantities, 956 rows (582 zero rows), 25 discriminators, T1 key sets and pointers, re-freeze tags, documents, and the comparison with the frozen file (235 equal); PASS |
| `t1_generator_probe.py` | 803 rows accepted by T1's functions, with exact values and tolerances; only the declared 153 refusals; PASS |

## Files (under `R4/T4-I8/`)

- `REBUILT_REFERENCE.md`, `rebuilt_reference_cases.json`, `RETURN.md`, `REPAIR_01.md`, `SHA256SUMS`
- `_run_records/derive_rebuilt_references.py`, `check_reference_json.py` and `t1_generator_probe.py`, each with its `.stdout.txt`

## Not done

- No product run. Admission of `line_stop`, `weight` N/m loads and the 0.4.0 sketches is read from code.
- No bend cases (T4-I7).
