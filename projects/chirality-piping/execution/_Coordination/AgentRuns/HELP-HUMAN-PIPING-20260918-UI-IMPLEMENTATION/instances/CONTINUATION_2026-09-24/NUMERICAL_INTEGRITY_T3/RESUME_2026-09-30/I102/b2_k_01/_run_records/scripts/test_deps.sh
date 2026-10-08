#!/bin/bash
# usage: test_deps.sh <label> <P-root> <target-dir>
# Runs every FK dependent's own test suite (except PP's, run separately),
# one cargo at a time through the T3 wrapper; one summary line per crate.
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
for c in $CRATES; do
  out="$log.$(echo $c | tr / _).txt"
  ( cd "$root/$c" && "$WT/tools/t3_cargo.sh" test --locked --offline --no-fail-fast ) > "$out" 2>&1
  rc=$?
  passed=$(grep -E "^test result" "$out" | awk '{p+=$4; f+=$6; i+=$8} END {print p"/"f"/"i}')
  echo "TEST crate=$c rc=$rc passed/failed/ignored=$passed" | tee -a "$log"
done
echo "TEST_DONE label=$label $(date -u +%FT%TZ)" | tee -a "$log"
