#!/bin/bash
# usage: deps_suite.sh <rev>: every FK dependent except PP (run separately), cargo test each, own target per lockfile
S=WT/scratch/rv121_rvk
for c in core/loads/load_case_algebra core/loads/primitive_loads core/loads/self_weight_wasm core/loads/stress_recovery \
  core/loads/user_loads core/model_operations/operation_applier core/runner/headless core/solver/curved_bend \
  core/solver/diagnostics core/solver/linear_supports core/solver/nonlinear_integration core/solver/nonlinear_supports \
  core/solver/performance_harness core/solver/sparse_direct core/solver/straight_pipe validation/benchmarks/mechanics \
  validation/benchmarks/nonlinear validation/benchmarks/numerical_integrity validation/benchmarks/numerical_robustness \
  validation/benchmarks/physics_audit_regression validation/benchmarks/stress apps/desktop/src-tauri; do
  $S/scripts/crate_suite.sh $1 $c test
done
