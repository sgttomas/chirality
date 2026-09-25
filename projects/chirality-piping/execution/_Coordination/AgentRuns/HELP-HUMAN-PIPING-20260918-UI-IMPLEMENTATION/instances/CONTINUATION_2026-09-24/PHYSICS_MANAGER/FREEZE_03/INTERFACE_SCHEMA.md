# Frozen successor core pressure/stress interface

ROOT selected prospective raw0.2/producer0.2/canonical0.3 physics-1. This source freeze does not register the joined consumer table or qualify Current/native/persistence. Legacy raw0.1/history and the radii-only scalar constructor/arithmetic remain unchanged. Fresh nonzero legacy primitive pressure blocks; legacy zero-pressure behavior remains its original route. No historical test is routed through a bypass.

Model0.3 exact profile is pressure_contract version2.0.0/mode exact_straight_pressure_v2. It requires explicit pressure_regions on every case, explicit closure paths and a common E/nu material basis. Selected G is derived from the common normalized E/nu pair; a nonempty request material list replaces the model list. Missing or unsupported inputs block without inferred values. First composition remains straight circular members/linear restraints and springs. Pressure bends/joints/nonlinear composition, generators and exact combinations remain explicit unsupported programme work.

Every physical row keeps its actual load_case basis_ref; pressure-region evidence never replaces it. Direct pressure rows resolve exactly once through contract_evidence.pressure entries keyed by (load_case_id,region_id), actual member and result_ids. Derived combinations are not fabricated; later eligible combinations need genuine operand refs and recomputation from signed actions.

| Kind | Component(s) | Unit / frame / location |
|---|---|---|
| pipe_wall_endpoint_action_v2 | wall_axial_end_action | N / element_local / end_i,end_j |
| pipe_wall_axial_force_v2 | wall_axial_force | N / element_local / five stations |
| pipe_effective_axial_force_v2 | effective_axial_force | N / element_local / five stations |
| pipe_axial_membrane_stress_v2 | axial_membrane_stress | Pa / pipe_section / five stations |
| pipe_lame_radial_stress_v2 | lame_inner_radial_stress,lame_outer_radial_stress | Pa / pipe_section / five stations |
| pipe_lame_hoop_stress_v2 | lame_inner_hoop_stress,lame_outer_hoop_stress | Pa / pipe_section / five stations |
| support_reaction_component_v2 | Fx,Fy,Fz; Mx,My,Mz | N; N*m / global / node |
| support_reaction_force_magnitude_v2 | force_magnitude | N / global / node |
| support_reaction_moment_magnitude_v2 | moment_magnitude | N*m / global / node |
| pipe_elastic_normal_stress_maximum_v2 | maximum_absolute_normal_stress | Pa / pipe_section / governing_station |

Five stations are end_i,end_j,quarter_1,midspan,quarter_3. Forces/actions use recovered_from_local_element_stiffness; stresses/max use recovered_from_open_mechanics_stress_components; support rows use prospectively selected recovered_from_assembled_support_law. Endpoint actions are node-on-element; wall Nw is tension-positive; S is effective wall/fluid force, not support reaction or material stress. Reactions are support-on-pipe, positive global force/right-hand couple at the attachment node. Force/moment norms remain separate. New IDs use exact length-prefixed case/entity identities; generic rows retain original IDs with explicit collision rejection in exact profile.

## One source geometry

SourceAnnulus is a new active wrapper; the original radii-only constructor and functions remain separate. It reuses the original scaled arithmetic and cap/eigen functions. One owned annulus_geometry helper supplies source wall/bore/insulation areas, with no E/nu inputs. Mass v2 consumes those exact helper bytes separately; pure-area validity does not inherit pressure/frame admission. The active frame still rejects nonpositive/coincident represented bore radii and nonrepresentable final section properties.

K, thermal/pressure recovery and normal/torsional stresses use source OD and effective wall (after existing normalized mill deduction), not a subtraction of squared rounded radii. As=pi*t*(OD-t); Ai/I/J/Z are coherent with that source. Named source-surface radial stresses are [-p,0], outer hoop2pAi/As, inner hoop outer+p. Rounded ri/ro are derived observations, not replacement source inputs. No interpolation/geometry authority is fabricated.

Both pressure.geometry entries and exact_cases.pipe_sections carry pipe_id,geometry_basis=authored_normalized_od_wall_v1,outside_diameter_m,effective_wall_thickness_m,ri_m,ro_m,Ai_m2,As_m2,I_m4,J_m4,Z_m3. Region geometry additionally carries traversal_forward. All active exact members have pipe_sections, including unpressurized members without a fabricated region. Region/case duplicates come from the same built SourceAnnulus object.

## Source pressure assembly and recovery

Physical cap transfer and Poisson/thermal eigenloads retain separate ledgers. Pressure RHS groups only matching source pressure bits, exact source OD/2-wall two-difference identity and magnitude bits of the same derived global direction component at the same node/axis. It sums signed cap±1 and eigen±2nu coefficients exactly, then multiplies the common pAi and direction. Derived zero directions are omitted from groups; original directions/source values remain recorded. Member/terminal reversal and proper spatial rotation are tested.

The actual source-grouped pressure RHS is used in the solver. Rounded cap/eigen ledger sums are observational and must not be substituted for it. The narrow exact sum operates on finite represented F64 operands only and does not recover already rounded products. Unshared source factors can remain ill conditioned: the declared32*epsilon cancellation screen uses the maximum absolute group-value sum divided by the maximum actual pressure-force RHS. Magnitudes are normalized before summation to avoid a spurious intermediate overflow. Above1e-9 (or unresolved range/zero cases) the solve blocks explicitly. This screen is not a numerical passing receipt or a certified displacement/stress error bound.

Pressure recovery retains mechanical/thermal section force Nm from the actual stiffness state and existing distributed-load section equilibrium. It forms wall Nm+2nuP and effective Nm+(2nu-1)P before publication; it does not subtract rounded published wall/P rows. A two-difference retains a low term in the effective pressure coefficient. Cap transfer is never subtracted again from wall recovery. Existing nonaxial/cut conventions stay intact.

Each exact_cases entry contains load_case_id,profile_mode,material_basis,pipe_materials,pipe_sections,pipe_stress_extrema,stress_maximum_coverage and pressure_rhs_assembly. Material objects contain pipe/material IDs,E_pa,nu,G_pa,constitutive_basis,thermal_consumed,alpha_per_kelvin,provenance. Alpha is null when unused, never invented as zero. material_basis records actual base/point/bracket selection; region material records include its corresponding temperature_basis.

pressure_rhs_assembly contains method=source_factor_grouped_pressure_rhs_v1,load_case_id,node_order,dof_order,dof_units,assembled_pressure_rhs_global,groups,rounded_cap_rhs_global,rounded_poisson_rhs_global,rounded_cap_and_eigen_ledgers_are_observational,cancellation_screen,screen_limit,screen_roundoff_multiplier,screen_is_not_numerical_qualification. Each group binds node_ref,component,pressure_bits,source_inner_radius_hi_bits,source_inner_radius_lo_bits,direction_component_magnitude,coefficient_sum,assembled_force_n and terms. Terms bind coefficient,region_id,pipe_id,kind(poisson_eigen or terminal_cap). Pressure moments are zero in this supported composition; screening concerns force components only.

## Coverage and extrema

The normal maximum uses |Nw/As|+hypot(My,Mz)/Z over direct piecewise quadratic section statics. It is not code/equivalent stress; torsional shear remains separate. Each pipe_stress_extrema record binds pipe/result IDs,approximate witness station/span/local fraction,witness lower/upper,global upper bound,certified gap,subdivisions and coefficient/enclosure basis. The proof bounds supplied binary64 polynomial coefficients; solver/coefficient-formation error is separate. No exact/unique governing coordinate is claimed. Gap limit is1e-12Pa+1e-12*lower, with at most131072 subdivisions/depth48; unresolved maxima remain unavailable. stress_maximum_coverage identifies missing member IDs; any incomplete member/case domain withholds its overall headline while valid individual rows remain. Exact per-case/global ties use stable case/location identities.

Remaining boundaries: independent successor source/consumer review,50 legacy regression dispositions, NUM/physics-1 union, registered checks/CI, native authoring/solve/inspect/save/reopen/export and broader pressure/stress/reaction findings. No merge readiness, engineering acceptance or release follows this freeze.
