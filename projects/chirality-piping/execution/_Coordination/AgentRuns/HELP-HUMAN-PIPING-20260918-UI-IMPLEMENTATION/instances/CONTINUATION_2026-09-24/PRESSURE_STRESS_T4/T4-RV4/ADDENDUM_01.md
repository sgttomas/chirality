# T4-RV4 addendum 01: confirmation of T4-I8's repair round 01

- **Requested by:** T4's WORKING_ITEMS. This confirms the repair of `R4/T4-RV4/REVIEW.md` (at `19c54f6f4a`).
- **Object:** `R4/T4-I8/` at `5b07d85cf3`. SHA256SUMS digest `65bf2f50…5509`; all ten entries were verified OK before reading. The map of changes is `REPAIR_01.md`. The baseline is the frozen round 00 at `61b4e0b460`.
- **Method:** as in the review. No product build, run or output was used. Code was read at `ed012c7ccf`, for conventions only.

## Disposition: CONFIRMED

S-1 to S-4 and N-2 to N-4 are repaired as intended. The new rows are correct by my own methods. Nothing else changed. There are no open items.

## 1. Checks (facts)

| Check | Result |
|---|---|
| Reproduction | T4-I8's three scripts were re-run on the fixture (`7e51ecb3…1ab1`), the frozen JSON (`6b8b75bb…c511`) and T1's generator, each extracted at its revision. The JSON and all three stdouts are byte-equal |
| All rows, both ways | All 956 rows match an independent model, each recomputed from (kind, entity, component, location), and no independent row is missing: 98/106 (case 1), 274/274 (case 2), 98 (case 3), 106 (twin B). The model uses the same methods as the review: generalized plane strain, unit-load integrals, load integration and free bodies. Exact forms are compared exactly; symbolic forms as decimals to 1e-60, with binary64 projections checked. 7134 checks, 0 failures |
| Transport | Every pointer resolves to its row's quantity. Every origin is {analytical, identity}, with the reference unit equal to the quantity's unit. All 582 zero tolerances equal 1e-9·scale·factor in the row unit. Every zero scale is a pure maintained quantity and has a definition |
| Unchanged | All 690 round-00 rows survive with the same value, unit, frame and criterion kind; the displacement zero tolerances are ×1000, now in mm. All 235 round-00 quantities are identical: 198 at the same path, 29 zero scales that lost only `definition` (which moved to the sibling map unchanged), and 8 support norms moved from the side block into rows. The 0.3.0, 0.4.0 and v3-patch documents of all five round-00 document sets are identical; only `sp1_pair` was added. The round-00 discriminators keep their order and values. Every other non-quantity difference (14 removed, 13 changed, 275 added leaves) is one of the mapped repairs |

## 2. The findings

| Finding | Repair | Verdict |
|---|---|---|
| S-1 | Zero scales are pure maintained quantities, with definitions in `zero_scale_definitions`. Rows use T1's `reference_origin` and `zero_scale` shape. Units follow T1's convention (the reference is converted into the row unit). T1's unmodified `origin_value` and `zero_scale_value` accept 803 rows, reproducing each value and tolerance. The only refusals are the declared Pa→MPa factor (150 stress rows) and two symbolic forms (3 rows) | Repaired. The two generator extensions are declared in `criteria.unit_factors` and `numeric_representation` |
| S-2 | Exactly the three nonzero uy rows (B, C, D, case 2 combined) carry the T4-U8 tag. There is a case-2 `refreeze` block and a twin-A `tip_bending_y_m` re-freeze. The D-6/SP-1 interaction is recorded, and HELP_HUMAN carries it into D-6's presentation (`T4_RULINGS.md` at `76c177074d`) | Repaired |
| S-3 | `cap_area_on_authored_bore` = 270848000/20871 = 12977.241148004408 Pa, marked producible. The nominal-bore control is kept, marked `producible_today: false` and active from T4-U6 | Repaired. Keeping the T4-U6 control is better than my request |
| S-4 (a) | Every numeric leaf is compared. The non-numeric exclusions form a closed list, E1–E5. I checked that E1 and E2 name real envelope fields (`producer.semantic_contract_id`; `formulation_basis.{profile_id, limitations}`, which are FormulationBasis's only fields). `run_id` is a constant and `model_ref` is the project id, so neither differs within a pair. Diagnostics are compared by id, code, severity and refs | Repaired |
| S-4 (b) | Clause 1: the v2 envelope is byte-identical to the merge base's | Repaired |
| S-4 (c) | `sp1_pair` is on every document set, the inputs are limited to p ≥ 0, and the checker verifies p ≥ 0 on every document | Repaired |
| N-2 | The allowance controls are relabelled as authoring guards. The D-5 inference is conditioned on RV1 N-5 | Repaired |
| N-3 | Norms, stress rows and the straight maximum are frozen for every case; the attribution is corrected | Repaired (see §3) |
| N-4 | Twin B added (separate closures), with the recommendation recorded in `applies_to` | Repaired (see §3) |

## 3. New rows, re-derived independently

- **Support norms:** the norms of my free-body reactions match. They are |x| where one component is nonzero. Case 2's anchor is sqrt((29280π)² + 900²) = 91990.235643653437 N, with 2700 N·m. The product publishes `norm3` of the restrained-slot vector (`lib.rs:11423-11435@ed012c7ccf`).
- **Stress rows:** they match.
  - **Product convention:** `element_local_bending_normal_stress_z` is Mz/Z and torsional shear is T·r/J (`stress_recovery/src/lib.rs:431-460, 793-821`). The ends use the j-side section cut, not the node-on-element row (`lib.rs:5179-5199`, endpoint `straight_section_resultants` at 0 and 1). Values are published as Pa/1e6 in MPa (`lib.rs:12695, 12725`).
  - **My values:** Mz is the load-integrated j-side moment at each location, ends included, and Z = π(ro⁴ − ri⁴)/(4ro). For example, A-B end_i is −2700/Z = −108000000000/(3439π) Pa, and B-C quarter_1 is −2811475.0778809659 Pa.
- **Straight elastic maximum:** it matches. My value is |Nw/As| + max|M|/Z, with max|M| taken from the member ends and the interior stationary points (V = 0) and confirmed by a dense rational sweep. Case 2 combined: A-B 16880566.358781446 Pa, B-C 11882388.442548618 Pa, C-D 6884210.5263157895 Pa. Every other member equals its |σz|.
  - The product publishes the midpoint of a certified enclosure whose gap is at most 1e-12 Pa + 1e-12·value (`elastic_extrema.rs:66-67, 73, 202-205`), with objective |a| + hypot(|b|, |c|). A correct product therefore meets the exact maximum at 1e-9.
- **Authored-bore discriminator:** 12977.241148004408 Pa, confirmed. It is separated from the correct value by 2.7e7 criteria.
- **Twin B (separate closures):** all 106 rows match a closure-free nodal ledger.
  - Nw = 3000π, S = −2000π, σz = 30000000/11.
  - Lamé values are 122e6/11 and 100e6/11.
  - Root Fx = −3000π, far Fx = +3000π, with norms 3000π.
  - All displacements are 0.
  - These agree with the test's frozen six-state values (`pressure_runtime.rs:438-446@ed012c7ccf`). The 0.3.0 document equals `model(true, false, 0.0)` field for field, which I rebuilt from that test's helpers. The frame (local y = global Z) is correct, and all its transverse rows are 0.

## Run records (`R4/T4-RV4/_run_records/`)

- `reproduce_i8_r01.py` and its stdout: SHA256SUMS verification and the byte-for-byte re-run of all three T4-I8 scripts.
- `refute_r01.py` and its stdout: the independent row model, transport and unchanged checks. It loads `refute_values.py` (round 00, unchanged) from the same folder.

Reproduce from `_run_records/`, with the fixture, the frozen JSON (`61b4e0b460`) and T1's `generate_reference_values.py` (`ed012c7ccf`) extracted into scratch:

```
WT/venv/bin/python -I reproduce_i8_r01.py ../../T4-I8 <fixture> <frozen json> <T1 generator> <empty scratch dir>
WT/venv/bin/python -I refute_r01.py ../../T4-I8/rebuilt_reference_cases.json <frozen json> <fixture>
```
