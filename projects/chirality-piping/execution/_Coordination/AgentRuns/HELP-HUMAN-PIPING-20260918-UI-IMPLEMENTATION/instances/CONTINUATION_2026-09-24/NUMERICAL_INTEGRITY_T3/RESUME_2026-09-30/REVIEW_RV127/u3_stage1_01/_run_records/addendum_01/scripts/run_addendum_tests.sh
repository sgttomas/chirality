#!/bin/bash
# RV127 addendum: PP lib spot checks at B (with the G11-before probe) and at the head; the head's
# changed validation and solver crates. Every cargo through t3_cargo.sh.
set -u
WT=WT; S=$WT/scratch/rv127_u3; C=$WT/tools/t3_cargo.sh
export TMPDIR=$S/tmp
P=projects/chirality-piping
cd $WT/rv127/base/$P/core/product_physics && $C test --locked --offline --target-dir $WT/targets/rv127-base-pp --lib -- --nocapture \
  rv127_probe_g11_before_fix profile_in_build_record challenge_bounds_are_the_profile > $S/ev/add_base_pp.log 2>&1; echo "base pp rc=$?"
cd $WT/rv127/cand2/$P/core/product_physics && $C test --locked --offline --target-dir $WT/targets/rv127-cand2-pp --lib -- --nocapture \
  flexibility_joint_missing_a_user_stiffness_is_refused_not_dropped endpoint_section_cut_fixed_and_free_thermal_match_uniform_stations \
  non_exact_source_blocks_gate zero_legacy_pressure_primitive profile_dispatch_requires_explicit_regions \
  profile_in_build_record challenge_bounds_are_the_profile bundled_demo_with_legacy_nonzero_pressure \
  realized_user_stiffness_joint_is_refused retired_legacy_pressure_label > $S/ev/add_cand_pp.log 2>&1; echo "cand pp rc=$?"
for crate in core/loads/stress_recovery core/solver/curved_bend validation/benchmarks/stress validation/benchmarks/mechanics; do
  n=$(echo $crate | tr '/' '_')
  cd $WT/rv127/cand2/$P/$crate && $C test --locked --offline --target-dir $WT/targets/rv127-cand2-x > $S/ev/add_cand_$n.log 2>&1; echo "$crate rc=$?"
done
cd $WT/rv127/cand2/$P/core/runner/headless && $C test --locked --offline --target-dir $WT/targets/rv127-cand2 --bin openpipestress-runner > $S/ev/add_cand_runner_bin.log 2>&1; echo "runner bin rc=$?"
