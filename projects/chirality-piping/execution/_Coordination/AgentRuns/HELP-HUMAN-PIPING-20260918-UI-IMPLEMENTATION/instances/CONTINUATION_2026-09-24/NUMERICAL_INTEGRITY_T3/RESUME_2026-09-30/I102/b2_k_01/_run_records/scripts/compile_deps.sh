#!/bin/bash
# usage: compile_deps.sh <label> <P-root> <target-dir>
# Compiles every FK dependent (except PP, whose suite runs separately) with all
# targets, one cargo at a time through the T3 wrapper; one log line per crate.
WT=WT
label=$1; root=$2; target=$3
log=$WT/scratch/i102_b2_k/logs/$label.log; : > "$log"
export TMPDIR=$WT/scratch/i102_b2_k/tmp CARGO_TARGET_DIR=$target
CRATES="core/loads/load_case_algebra core/loads/primitive_loads core/loads/user_loads core/loads/stress_recovery
core/loads/self_weight_wasm core/model_operations/operation_applier core/runner/headless core/solver/curved_bend
core/solver/diagnostics core/solver/linear_supports core/solver/nonlinear_integration core/solver/nonlinear_supports
core/solver/performance_harness core/solver/sparse_direct core/solver/straight_pipe validation/benchmarks/mechanics
validation/benchmarks/nonlinear validation/benchmarks/numerical_integrity validation/benchmarks/numerical_robustness
validation/benchmarks/physics_audit_regression validation/benchmarks/stress apps/desktop/src-tauri"
fails=0
run() { # crate, extra args
  local c=$1; shift
  ( cd "$root/$c" && "$WT/tools/t3_cargo.sh" test --no-run --all-targets --locked --offline "$@" ) > "$log.$(echo $c | tr / _)$(echo "$*" | tr -d ' -').txt" 2>&1
  local rc=$?; echo "COMPILE crate=$c extra=[$*] rc=$rc" | tee -a "$log"; [ $rc -eq 0 ] || fails=$((fails+1))
}
for c in $CRATES; do run $c; done
run validation/benchmarks/numerical_robustness --features seeded-faults
run core/solver/frame_kernel --features mutation-controls
echo "COMPILE_DONE label=$label failures=$fails $(date -u +%FT%TZ)" | tee -a "$log"
