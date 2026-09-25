# Concrete input and resolved interface

This is an implementable field proposal for [DESIGN.md](DESIGN.md), not a production schema or allocated semantic version. ROOT owns final public names/versions; one product manager owns the facade. Quantity objects use the existing `{value, unit}` shape, with the existing dimensional converter and strict finite checks. IDs refer to actual model records. Unknown discriminants or fields in the new namespace block qualification rather than disappearing on a typed round trip.

## Authored records

The first useful implementation needs only these additional owners:

- A model `reference_configurations` collection, each with `id`, `label`, `geometry_ref`, explicit `member_references`, and provenance. `geometry_ref` binds a retained normalized geometry projection (nodes/connectivity/element frames), not a self-referential hash of the whole model. `member_references` supplies `pipe_ref` and one of: `temperature_reference {installation_temperature, fit_length_change?}` or `direct_strain_reference {fit_strain?}`. Absence of fit is explicitly selected `none`, not inferred from an unrecognized old field. The direct-strain route supports explicit interval inputs without an invented absolute temperature. A reference does not imply initially zero stress when fit or constraints create stress.
- Each existing user material may own named `expansion_laws`. A law has an explicit definition, source/provenance and data; no values are supplied by the application. Definition/data unions follow below. It can be reused across members at different temperatures.
- The load case owns `analysis_state`, pressure regions and its existing primitive load records. `analysis_state` refers to those records, resolves element/support/mass choices, and declares an independent equilibrium or actual continuation. Support/device and geometry definitions stay in their existing owners.

Use these closed unions, rather than string options interpreted ad hoc:

```text
MaterialSelection =
  {kind: explicit_base_properties, material_ref, applicability_reference}
| {kind: exact_point, material_ref, point_ref}
| {kind: temperature_interpolation, material_ref, temperature,
   interpolation: piecewise_linear, extrapolation: forbidden}

ThermalState =
  {kind: constant_alpha_interval, coefficient, temperature_change,
   coefficient_meaning: engineering_interval, provenance}
| {kind: explicit_interval_strain, strain, interval_reference, provenance}
| {kind: free_length_state, expansion_law_ref}
| {kind: unchanged_reference, provenance}

ExpansionLaw =
  {id, definition: engineering_secant, datum_temperature,
   data: {kind: constant, coefficient}
       | {kind: table, interpolation: linear_coefficient, points}, provenance}
| {id, definition: engineering_dilation, datum_temperature,
   data: {kind: table, interpolation: linear_dilation, points}, provenance}
| {id, definition: differential_per_datum_length, datum_temperature,
   data: {kind: table, interpolation: linear_coefficient, points}, provenance}
| {id, definition: logarithmic_per_current_length, datum_temperature,
   data: {kind: table, interpolation: linear_coefficient, points}, provenance}
```

`unchanged_reference` sets the thermal contribution to zero, not an unentered ambient temperature. Direct interval engineering strain gives `lambda_th=1+epsilon_interval`; the actual fit composition uses `lambda_fit*lambda_th-1`, as with a free-length state. Do not apply a direct interval twice through both a legacy thermal primitive and this field. A direct-strain reference cannot supply a temperature required by a temperature-dependent property/law; the user must enter that missing information or select explicit applicable fixed data. A direct fit strain and a fit length change are alternative representations, not simultaneous inputs. Both carry reference and provenance.

Exact property points are bound to the actual material, not a globally reused point label. If a point's explicit temperature differs from the operating temperature, require an explicit `analysis_basis_override {reason, provenance}`; show it in results. A property point lacking a temperature can still be a deliberately selected explicit basis, but cannot prove it is a property at an operating temperature. The expansion-law data definition/datum is not inherited from E/nu points unless actually supplied. Valid exact endpoints are handled explicitly; no extrapolation is allowed. Alpha per absolute-temperature unit uses an inverse temperature interval, with no Celsius offset applied to the coefficient.

Per-element case record:

```text
{pipe_ref, operating_temperature?, material_selection, thermal_state,
 mass_state_ref, analysis_basis_override?}
```

The per-element `operating_temperature` is the actual physical temperature, distinct from a temperature selecting a deliberately overridden material basis. It is required for `free_length_state` and any actual-temperature-dependent physics; direct interval/fixed-data cases may omit it when no consumed physics needs it. They may also retain a known actual temperature without changing the direct interval strain. Do not infer actual T from a selected material point. If a migration or adapter carries an additional temperature in thermal data, require exact normalized agreement with this single actual-temperature field rather than choosing one.

Resolved coverage is one record per active element. For reusable authoring groups, retain a frozen explicit entity list and declaration precedence; overlapping declarations block. Changing a group changes the authored model and result dependency identity.

Per-support record:

```text
{support_ref,
 participation: {kind: active_model_device}
              | {kind: inactive}
              | {kind: locked_equivalent_support,
                 components: [{dof, position_source}]},
 boundary_motion?: [{dof, value, meaning: absolute_reference_displacement}],
 base_motion?: [{dof, value, meaning: absolute_reference_displacement}],
 device_reference?: {kind: force_at_reference, reference_position, force}
                  | {kind: unloaded_reference, reference_position}}

position_source = {kind: entered, value}
                | {kind: predecessor_value, case_ref, state_hash,
                   support_ref, dof}
```

`boundary_motion` applies only to already declared rigid/prescribed DOFs; `base_motion` applies only to an implemented spring/contact reference law. Both on the same device DOF are invalid. `device_reference` uses each device's actual component/frame and is first bounded to one scalar supported direction; the existing spring stiffness stays with that device or an explicit case-specific selection. Inactive devices cannot simultaneously supply active motions/preload. Locked-equivalent output means total support-assembly force/moment; it does not resolve internal pin and spring shares. A motion on another active DOF remains in effect. The numerical assembly retains per-DOF device ownership and reports unknown/overlapping participation rather than dropping it.

Mass records remain owned by the M35/M30 implementation. Required selected fields are explicit metal mass/section basis, contents `{kind: drained}` or `{kind: full, density, density_basis}`, insulation `{kind: excluded}` or an explicit included input basis, and gravity. An imported value is not overridden by a case label. Property-dependent density may cite its actual temperature/pressure selection; a directly entered density has no invented dependency. Attachments/components reference their own supported mass/CG methods. Unsupported partial fill or component mass must not be advertised as consumed. Uniform-pressure/full-fluid selection also validates zero axial gravity projection on each pressure-region member; otherwise the pressure-head/mass successor is required. The source ledger identifies whether contents gravity is wall traction or an effective-force body term and cannot consume both. This is a formulation check, not a user-data default.

The physical source ledger uses the existing stable primitive source IDs with explicit factors. Each source is an actual stored physical action, not a result row. Exact case inclusion records every ID once; no recursive case/result expression is evaluated as loads. Pressure/eigenstrain/device actions are separately generated from their named state owners. A case can retain unused authored primitives for editing; the preview must show they are excluded.

## Producer and downstream contract

The private resolver returns either `ResolvedAnalysisCase` or typed diagnostics, never a partially plausible case. Resolve normalization, geometry references, per-element E/nu/G and thermal definition, prescribed/support state, pressure/section compatibility, mass receipts, source membership and predecessor compatibility before assembly. Incomplete documents remain valid for editing/save; analysis qualification fails only the affected cases and dependent results.

Resolved record fields include these actual consumed facts:

```text
case_id, model_hash, reference_configuration_id, reference_geometry_hash;
members[{pipe_id, material_id, material_selection_input_refs,
         selected_E_Pa, selected_nu, derived_G_Pa,
         operating_temperature_K?, material_selection_temperature_K?,
         installation_temperature_K?,
         thermal_definition, coefficient_datum_K?, source_point_refs,
         interpolation_segments, thermal_stretch, fit_stretch,
         total_eigenstrain, section_basis_refs}];
support_components[{support_id,node_id,dof,frame,law_kind,
                    prescribed_value?,base_value?,reference_value?,preload?,
                    selected_stiffness?,physical_state_source}];
contributions[{source_id,owner_kind,classification,factor,consumed_input_refs}];
mass_receipt_refs;
history {kind, predecessor_raw_state_hash?, physical_internal_state_hash?,
         requested_path?, actual_accepted_steps?};
method_profile;
```

Question marks denote a tagged branch's absence, not an unknown fabricated zero. `interpolation_segments` means material/thermal data segments, not solver time steps. Preserve input quantities and normalized selected values through existing raw evidence, not only a hash with no recoverable source. Repeated material/pressure evidence must agree. Numerical method/source receipts and actual requested mode retain their existing ownership. User-entered source IDs, receipts or hashes alone never authenticate a solve.

Compilation adds actual prescribed tuples to the existing boundary/reconstruction/residual path, per-element stiffness and eigenstrain to the same element assembly, selected supports to nonlinear/device assembly, and physical sources once to the RHS. Recovery consumes that same resolved object; it must not re-read a later mutable model or select a different material. Result rows retain case/result IDs and point to their resolved member/device record. State differences and envelopes retain authentic operand state references and cannot pretend to have one synthesized equilibrium state.

Any source-recovery method's eligibility test covers the new actual input set. The numerical manager confirms its core/private adapter already retains nonzero prescribed tuples and source operands, while its present product facade remains zero-only. Wire the new product route and test it; do not claim M10 from existing kernel coverage or disable the conservative Sensitive gate.

## Authoring and persistence acceptance

Additions must cross UI types, validated operations, native serializers/migration, model snapshots, review/apply, Undo/Redo and portable package schemas together. A user should see what is assumed unchanged, what is explicitly entered, and what remains required before Solve. Normalization and mutation must preserve user material/density fields; do not reintroduce the already diagnosed create-pipe optional-input loss.

Persist original authored record plus actual consumed resolution/evidence. Undo restores source identity and recomputes applicability; it does not relabel a result from a different reference. Reopening old models does not invent coefficient definitions, support locks, fit mismatch or predecessor state. The selected public namespace/version receives adversarial unknown-field, cross-case, stale-predecessor, material-point and forged-evidence checks before it can qualify Current/rules/export. Old raw contracts and their hashes remain immutable.
