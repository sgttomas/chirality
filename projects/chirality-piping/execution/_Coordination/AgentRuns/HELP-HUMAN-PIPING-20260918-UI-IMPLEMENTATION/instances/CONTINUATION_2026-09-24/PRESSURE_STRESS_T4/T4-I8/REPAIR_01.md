# T4-I8 repair round 01: changes against T4-RV4's findings

**Request.** T4's WORKING_ITEMS asked for this round against `R4/T4-RV4/REVIEW.md` (at `19c54f6f4a`; PASS WITH FINDINGS, nothing blocking). The brief and the common terms are unchanged.

**Basis.** The frozen version is `61b4e0b460` (SHA256SUMS `8246ea4e…2d6`); Git keeps it.

**No frozen value changed.** `check_reference_json.py` compares the repaired file with the frozen one. All 235 round-00 quantities are identical in exact form and binary64: 227 under unchanged pointers, and 8 support norms that moved from case 2's side block into rows.

| Finding | Change | Where |
|---|---|---|
| **S-1 transport** | **Zero scales:** each `zero_scales` entry is now a pure maintained quantity `{unit, exact, decimal, value}`. Every definition, including those that exist nowhere else, moved to the sibling map `zero_scale_definitions`. **Row shape:** every row carries T1's `reference_origin` {analytical, pointer, reference_unit, transform identity}, plus T1's `zero_scale` {tag, base {pointer, reference_unit}, scale_unit} on zero rows. **Units:** `m_to_mm` is replaced by T1's convention: the reference is converted into the row unit by an exact factor, and the tolerances are in the row unit. **Proof:** `t1_generator_probe.py` runs T1's unmodified `origin_value` and `zero_scale_value` on every row. It accepts 803 and reproduces each value and zero tolerance exactly. Its only refusals are the new MPa stress rows (Pa→MPa, needing one added factor) and three symbolic rows (needing two added forms) | JSON top `criteria`; every `rows[]`; `_run_records/t1_generator_probe.py` |
| **S-2 Euler–Bernoulli re-freeze** | The nonzero uy rows at B, C and D in case 2 (combined) carry `refreeze: T4-U8 …`. Case 2 has a `refreeze` block, and the twin's expectation has one for `tip_bending_y_m`. Statics, reactions, pressure rows, stresses and maxima stay. The rz rows stay if the published rotation is the section rotation. The block also records the D-6/SP-1 interaction: the v3 side must select Euler–Bernoulli, or SP-1's straight-v3 clause must be scoped (a T4-U8 planning point) | `cases.tp_phys_pressure_halves.refreeze`; `cases.v3_straight_twin.expectation.refreeze`; rows |
| **S-3 control** | **Added** `cap_area_on_authored_bore`: Ai from the authored bore (ri 0.092) with the reduced As, giving σz = 270848000/20871 = 12977.241148004408 Pa (`producible_today: true`). **Kept** `cap_area_on_nominal_bore`, marked `producible_today: false` and `active_from: T4-U6`. Reason: the folded document never carries the 0.01 wall, but once D-5 adds the nominal wall and an allowance input, this error becomes producible. It is appended last, so the frozen discriminator indices are unchanged | `cases.milltol_lame_membrane.wrong_result_discriminators` |
| **S-4 (a)** | **Inverted:** every numeric leaf of the envelope compares bit-equal; non-numeric leaves compare equal too, except the closed list E1–E5 (contract identity, formulation text, contract-naming messages, declared kind correspondence). **No numeric exclusion:** this covers material, eigenload, cap, terminal and assembly evidence, `pipe_stress_extrema` and the 0.4.0 evidence. **Diagnostics:** compared by id, code, severity and refs | JSON `sp1_pair_scope` |
| **S-4 (b)** | Clause 1: the candidate's v2 envelope is byte-identical to the base revision's (the PR's merge base on main) for the same document and mode | `sp1_pair_scope.clause_1_v2_anchor` |
| **S-4 (c)** | The same scope applies to every case's v2/v3 pair, through `documents.sp1_pair`. It is restricted to p ≥ 0; every document checks p ≥ 0 | `sp1_pair_scope.inputs`; each case's `documents` |
| **N-1** | No change needed (it notes three-member traversal) | — |
| **N-2** | `allowance_not_folded` is relabelled as guarding the document's authoring, not the product. The D-5 inference is conditioned on the As of ε_p being the stiffness As (RV1 N-5) | case 1 discriminators; `refreeze.after_D5_as_recommended` |
| **N-3** | **Frozen as rows:** the support force and moment norms for every support of every case (case 2's side block moved into rows, values unchanged); the bending-normal y/z and torsional-shear stress rows at all five locations (MPa; section M/Z at the ends too); and the straight `pipe_elastic_normal_stress_maximum_v2` per member, including case 2's \|Nw/As\| + max\|M\|/Z. **Attribution corrected:** the straight maximum is pressure-coupled today; T4-U4's is the arc maximum | rows; top-level `row_kinds`; case 2 `limits` |
| **N-4** | **Added** twin B, `EXACT-PRESSURE-V3-STRAIGHT-TWIN-SEPARATE-CLOSURES-001`. No `pressure_reference/` fixture has separate closures, so the existing v2 document `PP/tests/pressure_runtime.rs` `model(true, false, 0.0)` serves, with full rows. **Recommended:** applying the pair scope to every existing p ≥ 0 v2 exact document in PP's tests | `cases.v3_straight_twin_separate_closures`; `sp1_pair_scope.applies_to` |
| **N-5** | No change needed | — |

**Counts.**

| Item | Round 00 | Round 01 |
|---|---|---|
| Rows | 690 | 956 |
| Quantities | 235 | 284 |
| Derivation checks | 162 | 177 |
| Discriminators | 24 | 25 |

All scripts pass.

**Changed files.** `rebuilt_reference_cases.json`, `REBUILT_REFERENCE.md`, `RETURN.md`, the two scripts and their stdouts, the new `_run_records/t1_generator_probe.py` with its stdout, this file, and `SHA256SUMS`.
