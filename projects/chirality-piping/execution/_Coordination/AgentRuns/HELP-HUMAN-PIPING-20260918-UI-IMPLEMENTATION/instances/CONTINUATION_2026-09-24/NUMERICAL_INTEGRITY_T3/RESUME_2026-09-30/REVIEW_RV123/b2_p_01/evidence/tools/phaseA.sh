#!/bin/bash
# RV123 round 2, phase A: suites on pristine base (a09e24b44c) and candidate (72b3e5d9ea), the byte
# harness on both trees, and the candidate's PP dependents compiled. One cargo job at a time.
WT=WT
S2=$WT/scratch/rv123_rvp2/r2
J=$S2/tools/runjob.sh
W=$WT/rv123
export RV123_IN=$WT/scratch/rv123_rvp2/i99_inputs RV123_EXTRA=S/i98_inputs/builtin_case_c.json,S/i98_inputs/builtin_l0_isolated_node.json,S/i98_inputs/builtin_milestone.json,S/i98_inputs/builtin_two_body_case_a.json,S/i98_inputs/builtin_two_body_case_b.json,S/i98_inputs/cause_milestone_reversed.json,S/i98_inputs/cb1_a_halfb_canonical.json,S/i98_inputs/cb1_ab.json,S/i98_inputs/cb1_ab_canonical.json,S/i98_inputs/cb1_ac_canonical.json,S/i98_inputs/cb2_case_c.json,S/i98_inputs/cb3_a.json,S/i98_inputs/cb3_v1_ab.json,S/i98_inputs/cb3_v1_b.json,S/i98_inputs/r7_cb1.json,S/i98_inputs/r7_cb1_halfb.json,S/i98_inputs/r7_cb2.json,S/i98_inputs/r7_cb3_v1.json,
$J pp_reg_cand   $W/cand/projects/chirality-piping/core/product_physics rv123-r2-pp-cand 0 test --locked --offline --no-fail-fast
$J pp_reg_base   $W/base/projects/chirality-piping/core/product_physics rv123-r2-pp-base 0 test --locked --offline --no-fail-fast
RV123_OUT=$S2/bytes/cand $J bytes_cand $W/chk/projects/chirality-piping/core/product_physics rv123-r2-pp-chk 0 test --locked --offline --no-fail-fast --test rv123_bytes -- --nocapture
RV123_OUT=$S2/bytes/base $J bytes_base $W/chkb/projects/chirality-piping/core/product_physics rv123-r2-pp-chkb 0 test --locked --offline --no-fail-fast --test rv123_bytes -- --nocapture
$J pp_stale_cand $W/cand/projects/chirality-piping/core/product_physics rv123-r2-pp-cand-stale 1 test --locked --offline --no-fail-fast --lib
$J pp_stale_base $W/base/projects/chirality-piping/core/product_physics rv123-r2-pp-base-stale 1 test --locked --offline --no-fail-fast --lib
$J runner_cand   $W/cand/projects/chirality-piping/core/runner/headless rv123-r2-runner-cand 0 test --locked --offline --no-fail-fast
$J runner_base   $W/base/projects/chirality-piping/core/runner/headless rv123-r2-runner-base 0 test --locked --offline --no-fail-fast
$J dep_operation_applier $W/cand/projects/chirality-piping/core/model_operations/operation_applier rv123-r2-dep-oa 0 check --locked --offline --all-targets
$J dep_self_weight_wasm $W/cand/projects/chirality-piping/core/loads/self_weight_wasm rv123-r2-dep-sw 0 check --locked --offline --all-targets
$J dep_tauri $W/cand/projects/chirality-piping/apps/desktop/src-tauri rv123-r2-dep-tauri 0 check --locked --offline --all-targets
echo "CHAIN-DONE phaseA $(date -u '+%FT%TZ')" >> $S2/logs/chain.log
