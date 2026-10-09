#!/bin/bash
# RV127 addendum 02: PP and RE spot checks at the PR code commit, and the PR's G11 tests at main.
set -u
WT=WT; S=$WT/scratch/rv127_u3; C=$WT/tools/t3_cargo.sh
export TMPDIR=$S/tmp
P=projects/chirality-piping
cd $WT/rv127/main_pp/$P/core/product_physics && $C test --locked --offline --target-dir $WT/targets/rv127-a2-main-pp --lib -- --nocapture rv127_before_ > $S/a2/t_main_g11.log 2>&1; echo "main g11 rc=$?"
cd $WT/rv127/pr_pp/$P/core/product_physics && $C test --locked --offline --target-dir $WT/targets/rv127-a2-pr-pp --lib -- --nocapture \
  flexibility_joint_ profile_in_build_record challenge_bounds_are_the_profile curved_bend_macro_element_emits \
  profile_dispatch_requires_explicit_regions zero_legacy_pressure_primitive retired_legacy_pressure_label \
  endpoint_section_cut_fixed_and_free_thermal non_exact_source_blocks_gate realized_user_stiffness_joint bundled_demo > $S/a2/t_pr_pp_lib.log 2>&1; echo "pr pp lib rc=$?"
cd $WT/rv127/pr_pp/$P/core/product_physics && $C test --locked --offline --target-dir $WT/targets/rv127-a2-pr-pp --test f1b_w2_runtime --test pressure_runtime > $S/a2/t_pr_pp_int.log 2>&1; echo "pr pp int rc=$?"
cd $WT/rv127/pr_pp/$P/core/reporting/result_export && $C test --locked --offline --target-dir $WT/targets/rv127-a2-pr-re --test source_blocks --test retained_precision_carriers --test physics_source_contract > $S/a2/t_pr_re.log 2>&1; echo "pr re rc=$?"
cd $WT/rv127/pr_pp/$P/core/loads/primitive_loads && $C test --locked --offline --target-dir $WT/targets/rv127-a2-pr-x > $S/a2/t_pr_primitive_loads.log 2>&1; echo "pr primitive_loads rc=$?"
cd $WT/rv127/pr_pp/$P/validation/benchmarks/mechanics && $C test --locked --offline --target-dir $WT/targets/rv127-a2-pr-x > $S/a2/t_pr_mech.log 2>&1; echo "pr mechanics rc=$?"
