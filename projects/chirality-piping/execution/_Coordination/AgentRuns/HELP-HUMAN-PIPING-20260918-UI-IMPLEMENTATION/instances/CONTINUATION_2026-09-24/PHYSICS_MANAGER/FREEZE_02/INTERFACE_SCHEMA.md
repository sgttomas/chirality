# Frozen core interface and qualification limits

This describes FREEZE_01 source, not an active canonical consumer registration. ROOT selected physics-1 within raw0.2/producer0.2/canonical0.3. Exact profile emits raw0.2 at full binary64 precision. Legacy fresh nonzero primitive pressure blocks; legacy zero-pressure raw0.1 retains its existing output route/rounding. The existing old assertion/fixture bytes remain unchanged except Rust structural adaptations for newly optional fields.

Every direct result uses basis_ref {ref_type:load_case,ref_id:actual case ID}. No combination is accepted in this first exact profile; EXACT_PRESSURE_COMBINATION_UNSUPPORTED makes that capability explicit. Derived combination/difference semantics and scalar-operation repair remain programme work.

Pressure kind/component signatures (locations end_i,end_j,quarter_1,midspan,quarter_3 except endpoint action end_i/end_j):

| Kind | Component(s) | Unit / frame |
|---|---|---|
| pipe_wall_endpoint_action_v2 | wall_axial_end_action | N / element_local |
| pipe_wall_axial_force_v2 | wall_axial_force | N / element_local |
| pipe_effective_axial_force_v2 | effective_axial_force | N / element_local |
| pipe_axial_membrane_stress_v2 | axial_membrane_stress | Pa / pipe_section |
| pipe_lame_radial_stress_v2 | lame_inner_radial_stress, lame_outer_radial_stress | Pa / pipe_section |
| pipe_lame_hoop_stress_v2 | lame_inner_hoop_stress, lame_outer_hoop_stress | Pa / pipe_section |
| support_reaction_component_v2 | Fx,Fy,Fz; Mx,My,Mz | N; N*m / global, node |
| support_reaction_force_magnitude_v2 | force_magnitude | N / global, node |
| support_reaction_moment_magnitude_v2 | moment_magnitude | N*m / global, node |
| pipe_elastic_normal_stress_maximum_v2 | maximum_absolute_normal_stress | Pa / pipe_section, governing_station |

Pressure action/force basis remains recovered_from_local_element_stiffness; pressure stress/normal maximum basis is recovered_from_open_mechanics_stress_components. Support basis is the prospectively nominated recovered_from_assembled_support_law. Wall endpoint action is node-on-element; section Nw is tension-positive; S=Nw-pAi is neither wall stress nor pipe-support reaction. Support action is support-on-pipe with positive global forces and right-hand couples about its attachment node. Torsion remains signed separate shear. No six-component mixed-unit norm or piping-code stress is defined.

New pressure/support/normal-maximum source IDs use exact length-prefixed case/entity IDs. Generic legacy-named direct rows still use their original ID algorithm, so exact profile blocks pipe/case/node/support suffix collisions. The frozen implementation has no synthetic source or region identity.

`contract_evidence` has `pressure` (region entries), `connector` (empty), and `exact_cases` (all solved exact cases). Pressure entries contain exactly the producer shape in pressure_runtime.rs: region_id, load_case_id, profile_version, profile_mode, member_pipe_ids, terminals, pressure_basis, p_pa, geometry, materials, applied_loads, provenance, approximation, external_pressure_increment_pa, geometry_representation_guard; facade adds result_ids. Region key is (case,region); duplicate within case blocks. Each pressure row maps to exactly one member/region/case entry. Remote closure support reactions are explicitly outside the pipe load ledger.

Geometry objects: pipe_id,ri_m,ro_m,Ai_m2,As_m2,traversal_forward. Material objects: pipe_id,material_id,E_pa,nu,G_pa,constitutive_basis,temperature_basis,provenance,thermal_consumed,alpha_per_kelvin. Per-member load objects contain pipe_id,eigenload_pair_local_n,mathematical_cap_pair_local_n,local_x_global,thermal_included (false: thermal is assembled separately). Terminals retain node_ref,closure_transfer,provenance,closure_pressure_load_global_n,pipe_cap_transfer_global_n,remote_closure_support_reaction_global_n (null when transferred),remote_closure_excluded_from_pipe_solve. temperature_basis is {selection:base_material}, {selection:exact_point,point_id}, or {selection:interpolation,temperature_value,temperature_unit}; the exact_cases material_basis string additionally records the actual selected bracket IDs.

Each exact_cases entry contains load_case_id,profile_mode,material_basis,pipe_materials,pipe_stress_extrema. Every active member appears in pipe_materials, including unpressurized members. Objects contain pipe_id,material_id,E_pa,nu,G_pa,constitutive_basis,thermal_consumed,alpha_per_kelvin,provenance. Alpha is null when not consumed; no zero is fabricated. The selected material comes from the same normalized actual case array as region assembly. material_basis identifies the selected base or common point/bracket and interpolation, including alpha source. Source/consumer consistency validation is still required at joined fan-in; successful serialization alone cannot qualify Current.

Normal-extrema records bind pipe_id,result_id,station_fraction,span_index,local_fraction,value_lower_pa,value_upper_pa,global_upper_bound_pa,certified_gap_pa,subdivisions,approximation,coefficient_basis,enclosure_scope. The station is an approximate maximizing witness, not an exact or unique governing coordinate. The witness objective lies in [value_lower_pa,value_upper_pa]; the global maximum of the supplied binary64 Bernstein polynomial lies in [value_lower_pa,global_upper_bound_pa]. Reported row value is the midpoint of the witness interval. The interval search stops at 1e-12 Pa + 1e-12*value_lower with at most 131072 subdivisions/depth 48. Unrepresentable/invalid/unresolved extrema emit EXACT_STRESS_GOVERNING_MAXIMUM_UNAVAILABLE and omit the maximum rather than substitute a sample or zero. The interval proof does not enclose solver or coefficient-formation error; the actual X1 assembly fixture separately checks physical/reference agreement at the unchanged 1e-9 tolerance.

The all-case maximum resolves to its actual result row, with deterministic case/location tie handling. Current native authoring, consumer schema/table registration, persistence, export and history qualification remain outside this bounded source freeze. M01 bent/jointed and nonlinear pressure composition, M05 general nonlinear reaction attribution, M08 directional factors, M15 signed combinations and broader M33 basis semantics remain open. Fifty historical/current-fixture regression failures are retained for individually reviewed disposition; this candidate is not merge-ready.

## Reviewed-finding repair delta in FREEZE_02

Each exact_cases entry additionally contains stress_maximum_coverage {complete:boolean,unavailable_pipe_ids:actual pipe ID array}. A failed/unrepresentable member maximum withholds that case maximum; any unavailable requested case maximum withholds the overall summary. Valid individual rows and diagnostics remain. Node/member ties inside a case now use lexicographically smallest actual location ID, exact profile only. These semantics are tested by genuine two-member/two-case unrepresentable aggregate controls and zero-state node/member permutations. New signed-support controls cover six nonzero force/moment components under a proper 3D rotation, explicit rigid/two-spring load partition and ambiguous/duplicate support rejection. Pure torque additionally asserts its nonzero support moment. No old physics expectation changed.
