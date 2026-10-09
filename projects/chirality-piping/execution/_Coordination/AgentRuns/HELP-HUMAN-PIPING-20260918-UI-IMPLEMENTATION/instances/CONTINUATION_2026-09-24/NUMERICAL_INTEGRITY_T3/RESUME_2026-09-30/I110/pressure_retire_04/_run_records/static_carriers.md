## T1 curved-bend row treatment
old: pressure_thrust_treatment=arc_end_cap_tangent_pair_plus_consistent_radial_wall_load
new: pressure_thrust_treatment=none_pressure_refused_outside_the_exact_straight_contract
committed files carrying the old text: 1
- other fixture (1):
  - P/fixtures/results/invented/result_export_v0_2.json

## T3a joint row basis
old: pressure_thrust_generation=load_side_user_effective_area;pressure_thrust=
new: pressure_thrust_generation=none_pressure_refused_outside_the_exact_straight_contract;user_pressure_thrust_reference=
committed files carrying the old text: 14
- I114's demo fixtures (3):
  - P/fixtures/product_preview/invented_mechanics_result.json
  - P/fixtures/product_preview/invented_mechanics_result_precision_1_dense.json
  - P/fixtures/product_preview/invented_mechanics_result_precision_1_sparse.json
- historical evidence (not regenerated) (8):
  - P/validation/evidence/reproduction/REPRO_DEL0904_20260718T215424Z_f14fa77518a/outputs/tp_runner_015_solve.json
  - P/validation/evidence/reproduction/REPRO_DEL0904_20260718T215424Z_f14fa77518a/stdout/solve.txt
  - P/validation/evidence/reproduction/REPRO_DEL0904_20260719T033249Z_89a93d7ca21d/outputs/tp_runner_015_solve.json
  - P/validation/evidence/reproduction/REPRO_DEL0904_20260719T033249Z_89a93d7ca21d/stdout/solve.txt
  - P/validation/evidence/reproduction/REPRO_DEL0904_20260719T202023Z_23eeaabc9040/outputs/tp_runner_015_solve.json
  - P/validation/evidence/reproduction/REPRO_DEL0904_20260719T202023Z_23eeaabc9040/stdout/solve.txt
  - P/validation/evidence/reproduction/REPRO_DEL0904_20260720T074714Z_a5235340aae3/outputs/tp_runner_015_solve.json
  - P/validation/evidence/reproduction/REPRO_DEL0904_20260720T074714Z_a5235340aae3/stdout/cmd03_solve_case1.txt
- other fixture (1):
  - P/fixtures/results/invented/result_export_v0_2.json
- witness output (stale since C-150 is refused) (2):
  - P/validation/witness/generated/tp_runner_014_headless_entrypoint_preview_run.json
  - P/validation/witness/generated/tp_runner_015_final_cli_solve.json

## T3b joint row sign convention
old: ; pressure-thrust generation is load-side effective-area evidence and no compliance claim is made
new: ; no joint pressure thrust is generated and no compliance claim is made
committed files carrying the old text: 14
- I114's demo fixtures (3):
  - P/fixtures/product_preview/invented_mechanics_result.json
  - P/fixtures/product_preview/invented_mechanics_result_precision_1_dense.json
  - P/fixtures/product_preview/invented_mechanics_result_precision_1_sparse.json
- historical evidence (not regenerated) (8):
  - P/validation/evidence/reproduction/REPRO_DEL0904_20260718T215424Z_f14fa77518a/outputs/tp_runner_015_solve.json
  - P/validation/evidence/reproduction/REPRO_DEL0904_20260718T215424Z_f14fa77518a/stdout/solve.txt
  - P/validation/evidence/reproduction/REPRO_DEL0904_20260719T033249Z_89a93d7ca21d/outputs/tp_runner_015_solve.json
  - P/validation/evidence/reproduction/REPRO_DEL0904_20260719T033249Z_89a93d7ca21d/stdout/solve.txt
  - P/validation/evidence/reproduction/REPRO_DEL0904_20260719T202023Z_23eeaabc9040/outputs/tp_runner_015_solve.json
  - P/validation/evidence/reproduction/REPRO_DEL0904_20260719T202023Z_23eeaabc9040/stdout/solve.txt
  - P/validation/evidence/reproduction/REPRO_DEL0904_20260720T074714Z_a5235340aae3/outputs/tp_runner_015_solve.json
  - P/validation/evidence/reproduction/REPRO_DEL0904_20260720T074714Z_a5235340aae3/stdout/cmd03_solve_case1.txt
- other fixture (1):
  - P/fixtures/results/invented/result_export_v0_2.json
- witness output (stale since C-150 is refused) (2):
  - P/validation/witness/generated/tp_runner_014_headless_entrypoint_preview_run.json
  - P/validation/witness/generated/tp_runner_015_final_cli_solve.json

## T2 formulation limitation (preview_formulation_basis)
old: Pressure thrust and pressure stress retain the existing preview formulation and capability qualifications; pressure formulation qualification remains open.
new: Pressure is not solved on this profile: legacy pressure inputs are refused, and pressure is solved only on the exact straight-pressure profile, under that profile's own qualifications.
committed files carrying the old text: 19
- I114's demo fixtures (2):
  - P/fixtures/product_preview/invented_mechanics_result_precision_1_dense.json
  - P/fixtures/product_preview/invented_mechanics_result_precision_1_sparse.json
- other fixture (2):
  - P/fixtures/results/precision_connected_ui_mechanics_dense.json
  - P/fixtures/results/precision_connected_ui_mechanics_sparse.json
- product source (1):
  - P/core/product_physics/src/lib.rs
- source-blocks (retained-source) fixture (14):
  - P/fixtures/product_preview/source_blocks/multicase-dense_scrutiny.raw.json
  - P/fixtures/product_preview/source_blocks/multicase-sparse_interactive.raw.json
  - P/fixtures/product_preview/source_blocks/n05-dense_scrutiny.raw.json
  - P/fixtures/product_preview/source_blocks/n05-sparse_interactive.raw.json
  - P/fixtures/product_preview/source_blocks/n06-dense_scrutiny.raw.json
  - P/fixtures/product_preview/source_blocks/n06-sparse_interactive.raw.json
  - P/fixtures/product_preview/source_blocks/rejected_stress_range/dense_scrutiny.raw.json
  - P/fixtures/product_preview/source_blocks/rejected_stress_range/sparse_interactive.raw.json
  - P/fixtures/product_preview/source_blocks/ui/multicase-dense_scrutiny.raw.json
  - P/fixtures/product_preview/source_blocks/ui/multicase-sparse_interactive.raw.json
  - P/fixtures/product_preview/source_blocks/ui/n05-dense_scrutiny.raw.json
  - P/fixtures/product_preview/source_blocks/ui/n05-sparse_interactive.raw.json
  - P/fixtures/product_preview/source_blocks/ui/n06-dense_scrutiny.raw.json
  - P/fixtures/product_preview/source_blocks/ui/n06-sparse_interactive.raw.json

## T4 preview-physics-1 limitation [1]
old: Nonzero pressure is refused on this route, and so is legacy imposed_displacement.
new: Legacy pressure primitives are refused on this route, zero values included, and so is legacy imposed_displacement.
committed files carrying the old text: 20
- I114's demo fixtures (2):
  - P/fixtures/product_preview/invented_mechanics_result_preview_physics_1_dense.json
  - P/fixtures/product_preview/invented_mechanics_result_preview_physics_1_sparse.json
- other fixture (7):
  - P/fixtures/results/preview_physics_connected_dense.json
  - P/fixtures/results/preview_physics_connected_sparse.json
  - P/fixtures/results/preview_physics_invented_dense.json
  - P/fixtures/results/preview_physics_invented_sparse.json
  - P/fixtures/results/preview_physics_unicode_ids_sparse.json
  - P/fixtures/results/semantic_contract_v0_3_preview_physics_1.json
  - P/fixtures/results/semantic_contract_v0_3_preview_physics_retained_1.json
- product source (1):
  - P/core/product_physics/src/preview_physics.rs
- published schema const (1):
  - P/schemas/results.v0.3.schema.yaml
- readers corpus 07n (retained_precision_cases.json) (1):
  - P/fixtures/results/retained_precision_cases.json
- retained successor fixture (8):
  - P/fixtures/results/retained_precision_l0_successor_dense_scrutiny.json
  - P/fixtures/results/retained_precision_l0_successor_sparse_interactive.json
  - P/fixtures/results/retained_precision_milestone_successor_dense_scrutiny.json
  - P/fixtures/results/retained_precision_milestone_successor_sparse_interactive.json
  - P/fixtures/results/retained_precision_successor_derivative_dense_scrutiny.json
  - P/fixtures/results/retained_precision_successor_derivative_sparse_interactive.json
  - P/fixtures/results/retained_precision_w_c2_successor_dense_scrutiny.json
  - P/fixtures/results/retained_precision_w_c2_successor_sparse_interactive.json
