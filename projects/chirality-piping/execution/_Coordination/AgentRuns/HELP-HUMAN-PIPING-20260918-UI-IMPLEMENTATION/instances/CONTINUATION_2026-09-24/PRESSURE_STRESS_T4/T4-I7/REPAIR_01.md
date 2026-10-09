# T4-I7 repair round 01 (after T4-RV3)

**Basis.** T4-RV3's `R4/T4-RV3/REVIEW.md` at `caef354082` refuted round 00 (`80b1e97e2b`, SHA256SUMS `c6269caf…`). RV3 found every value correct and blocked on B-1. T4's WORKING_ITEMS then sent its repair instructions on S-1, S-2 and S-3.

**Method.**
- The same engine produced the repair; `u2_engine.py` is unchanged.
- The generator, cross-check and precision check were edited in place.
- `_run_records/repair01_compare.py` compares round 00, extracted from `80b1e97e2b`, against round 01. Its output is `repair01_compare.stdout.txt`.

| Finding | Change | Evidence |
|---|---|---|
| **B-1** (blocking): 23 of 241 control rows did not discriminate | A control now lists only rows at ≥ 1e3 tolerances (at most 8, in round 00's order). A wrong value below 1e-40 of its group's zero scale is written as exact 0. Each control's maximum distance is computed over every row and is unchanged. The 23 failing round-00 rows sit in `rows_dropped_repair_01`, each with its reason, and are not assertions. Of those, 20 come from U2-L-FREE-P-K2 and CBPT-K2 (a wrong value equal to the reference, or 1e-54-level noise) and 3 from the kink case (two equal zeros, plus Fy below 1e3 tolerances). `U2_REFERENCE.md` §7 and §8 now state the claim per control maximum (8.4e6 to 8.1e12) | The compare output lists each dropped row and its reason. It confirms every maximum distance is unchanged and the 205 surviving round-00 rows are byte-identical |
| **S-1**: the chord-frame arc end rows were wall-basis | The arc chord-frame block is replaced by `end_rows/*/chord_frame_elastic`. Its forces are the elastic node-on-element action K·d − p, which is the wall action minus c_b = [−pAi·t_i, +pAi·t_j]. Its moments equal the wall moments. It is labelled and mapped to today's `element_local_*` end rows on arcs (`arc_chord_frame`). It has its own tolerance group, `elastic_end_force_chord_frame`. The tangent-frame wall rows are unchanged and stay asserted. Example: U2-L-ANCH-ALL-K2, BEND end_i, F_y = −396.08167949273772476 N | The cross-check computes K_b(d − u_free) − p from the stiffness solution independently and agrees to 4.6e-20. The 1,616 wall-chord leaves are removed and 1,356 elastic leaves added |
| **S-2**: the kink sat on the α_tan boundary | Both kink controls now use D.x = 3.248: θ = atan(5e-4) = 4.9999995833e-4 rad, about α_tan/2. The `interior_remainder_omitted` control was regenerated (3.3e8 to 3.4e8 tolerances). A new refusal control, `U2-L-MITRE-REFUSED-P-K2` (D.x = 3.242, θ = 1.9999973333e-3 rad, about 2α_tan), carries `expected_refusal` with code `PRESSURE_REGION_MITRE_UNSUPPORTED` (provisional) and no values. The rule θ = atan2(\|t_in × t_out\|, t_in·t_out) ≤ α_tan = 1e-3 rad (provisional) is in the header. Every case records θ per bend-adjacent node (`derived.junction_angles_rad`). The reversed-member control is kept | The two kink cases are excluded from the unchanged comparison as revised. The generator stdout prints both angles |
| **S-3**: plan §2's headline case was missing | New variant PTW: both terminals `transfers_to_wall`, carrying pressure, thermal and self-weight, for the L free and anchored and the U anchored, at k = 1 and 2. U2-L-ANCH-PTW-K2 is a core case with all six transforms. U2-L-ANCH-PTW-K2 carries the full negative-control set. U2-L-ANCH-PTW-K1 and U2-L-FREE-PTW-K1 are in the polygon control, whose ratio per halving is 4.000 ± 0.002 and whose Richardson limit agrees to ≤ 8.6e-12 | There are 13 new cases. The cross-check (F1, F2) and the 90-digit precision check cover them |

**Unchanged.** Except for these changes, every round-00 value of the 65 surviving cases is identical:
- 40,415 leaves compared and none changed;
- the eight round-00 polygon entries;
- the 65 document sketches of those cases.

**Additions only** to the surviving cases:
- `derived.alpha_tan_provisional_rad`;
- `derived.junction_angles_rad`;
- `chord_frame_elastic`;
- its zero-scale group.

**The header** adds `revision`, `tangency_rule` and the listing rule, and updates the end-row and row-map texts.

**Not changed.** Nothing is relaxed, and no tolerance or zero-scale rule moves. RV3's notes N-1 to N-6 needed no change.
- N-4 is now also in limit 2: never snap sub-tolerance kinks.
- N-5 (large linear motions in free SEPD and ALL) stays the WI's choice.
