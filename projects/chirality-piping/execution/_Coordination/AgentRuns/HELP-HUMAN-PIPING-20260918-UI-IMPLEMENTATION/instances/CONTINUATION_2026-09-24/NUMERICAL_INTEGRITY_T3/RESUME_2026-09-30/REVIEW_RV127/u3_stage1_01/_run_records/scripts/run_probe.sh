#!/bin/bash
# RV127: PP unit/integration spot checks in the probe copy (candidate + one probe-only test).
set -u
WT=WT; S=$WT/scratch/rv127_u3
export TMPDIR=$S/tmp
cd $WT/rv127/probe/projects/chirality-piping/core/product_physics || exit 2
$WT/tools/t3_cargo.sh test --locked --offline --target-dir $WT/targets/rv127-probe --lib -- --nocapture \
  rv127_probe profile_dispatch_requires_explicit_regions_and_refuses_legacy_pressure retired_legacy_pressure_label \
  t6a_collinear_runs_are_silent_with_the_floor current_composite_derived_normal_friction_and_reversal \
  valid_invented_model_exposes_nonlinear_support_loop_evidence_historical_pressure_premise \
  expansion_joint_user_stiffness_emits_macro_element_review_rows \
  expansion_joint_pressure_thrust_uses_user_effective_area_as_load_side_evidence_historical_pressure_premise \
  private_historical_pressure_scope_restores_public_refusal_and_rejects_exact \
  _without_pressure operation_authored_primitive_categories_map_to_preview_mechanics > $S/ev/probe_lib.log 2>&1
echo "lib rc=$?"
$WT/tools/t3_cargo.sh test --locked --offline --target-dir $WT/targets/rv127-probe --test pressure_runtime --test f1b_w2_runtime -- \
  retired_legacy_pressure f1b_w2_admission_refuses_each_reachable_family_by_name > $S/ev/probe_int.log 2>&1
echo "int rc=$?"
