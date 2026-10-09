# I115: counts (git grep -l / -c, outside P/execution unless stated)

C = main `ec5d397359` + U3 `1e9724fb94` (tree `c64687a327`); B2U = `b2` `e582b61f9e` + U3 (tree `9ac081c25a`).

## H-4's radius

| Tree | Files with the summary key | Successor pins with it | Occurrences in 07n | Semantic contracts with the joint row kind | Files with LIMITATIONS `:75` | Files with LIMITATIONS `:77` |
|---|---|---|---|---|---|---|
| U3 at I5's basis `70e7f49ced` | 88 | 6 | 26 | 9 | 20 | 20 |
| C | 89 | 6 | 26 | 9 | 22 | 22 |
| `b2` `9f5cfbcd75` (I5's) | 92 | 10 | 26 | 10 | 22 | 22 |
| `b2` `e582b61f9e` | 92 | 10 | 26 | 10 | 22 | 22 |
| B2U (after J0b) | 93 | 10 | 26 | 10 | 24 | 24 |

- The key: `component_user_stiffness_macro_element_count`. Successor pins: `P/fixtures/results/retained_precision_*successor*`. 07n: `P/fixtures/results/retained_precision_cases.json`.
- The row kind: `component_user_stiffness_macro_element_review`. At `b2` all 10 semantic contracts that carry it are `REVIEWED_INPUTS` (the 9 on main plus `semantic_contract_v0_3_physics_retained_1.json`). It is in no successor pin and not in 07n.
- LIMITATIONS `:77` ("Endpoint force rows are in the chord frame") at C, the 22 files: `PP/src/preview_physics.rs`; 4 `P/fixtures/product_preview` envelopes; 5 `preview_physics_*` result fixtures; 07n; 8 successor pins; the schema `results.v0.3.schema.yaml`; and **two `REVIEWED_INPUTS`: `semantic_contract_v0_3_preview_physics_1.json` and `semantic_contract_v0_3_preview_physics_retained_1.json`** (`supported_profile_limitations`, the 7 strings verbatim at lines 1243–1249).

## `REVIEWED_INPUTS`

- main `ec5d397359` and U3 `1e9724fb94`: `PP/src/build_identity.rs:148-163`, 14 entries.
- `b2` `e582b61f9e`: `:149-170`, 17 entries (appended: `retained_precision_prepared_combination_v1.json`, `retained_precision_prepared_exact_v1.json`, `semantic_contract_v0_3_physics_retained_1.json`).
- No file in T4's planned edit set (`t4simA.txt`, `t4simB.txt`) is among them.

## Constructor sites

`CurvedBendMacroElement::new(` at C, outside records: 21 in 9 files (PP `lib.rs` 2; CB `lib.rs` 9, `s11k_tests.rs` 1; NI `lib.rs` 1, `k1_tests.rs` 2, `k2b_tests.rs` 1, `k5_tests.rs` 2, `kd5_tests.rs` 1; `validation/benchmarks/mechanics/src/lib.rs` 2). Annex A's count holds.

## `CSKEW_8_5` at C

NI `structural_adapter/kd5_models.rs:85` (definition); `kd5_tests.rs:401-408`; `k1_tests.rs:191` (KD5 corpus), `:342` (parity, demotes), `:1314` (RV8-3); `k2b_tests.rs:47` (corpus), `:1313` (S11-K under b); `k5_tests.rs:299` (kd5_curved list).
