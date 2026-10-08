#!/bin/bash
# RV123 phase 2 (after phase 1): RE-side fixture checks, exploratory variants, the byte harness on
# both trees, and the candidate's PP dependents compiled. One cargo job at a time.
WT=WT
S=$WT/scratch/rv123_rvp2
J=$S/tools/runjob.sh
until grep -q 'CHAIN-DONE phase1' $S/logs/chain.log 2>/dev/null; do sleep 30; done
C=$S/chk/projects/chirality-piping/core
CB=$S/chkb/projects/chirality-piping/core
D=$S/cand/projects/chirality-piping
export RV123_IN=$S/i99_inputs
$J re_chk $C/reporting/result_export rv123-re-chk 0 test --locked --offline --no-fail-fast --test rv123_exact_check -- --nocapture
$J pp_chk_explore $C/product_physics rv123-pp-chk 0 test --locked --offline --no-fail-fast --lib rv123_ -- --nocapture --test-threads=1
RV123_OUT=$S/bytes/cand $J pp_chk_bytes $C/product_physics rv123-pp-chk 0 test --locked --offline --no-fail-fast --test rv123_bytes -- --nocapture
RV123_OUT=$S/bytes/base $J pp_chkb_bytes $CB/product_physics rv123-pp-chkb 0 test --locked --offline --no-fail-fast --test rv123_bytes -- --nocapture
$J dep_operation_applier $D/core/model_operations/operation_applier rv123-dep-operation_applier 0 check --locked --offline --all-targets
$J dep_self_weight_wasm $D/core/loads/self_weight_wasm rv123-dep-self_weight_wasm 0 check --locked --offline --all-targets
$J dep_physics_audit $D/validation/benchmarks/physics_audit_regression rv123-dep-physics_audit 0 check --locked --offline --all-targets
$J dep_numerical_integrity $D/validation/benchmarks/numerical_integrity rv123-dep-numerical_integrity 0 check --locked --offline --all-targets
$J dep_tauri $D/apps/desktop/src-tauri rv123-dep-tauri 0 check --locked --offline --all-targets
echo "CHAIN-DONE phase2 $(date -u '+%FT%TZ')" >> $S/logs/chain.log
