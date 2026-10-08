#!/bin/bash
# K-13: the existing case-path and legacy-combination tests' printed output,
# single-threaded with --nocapture, for one tree. usage: k13_capture.sh <label> <tree> <target>
WT=WT
label=$1; tree=$2; target=$3
"$WT/scratch/i102_b2_k/run_cargo.sh" k13_$label "$tree/projects/chirality-piping/core/solver/frame_kernel" "$target" \
  test --locked --offline --lib -- --nocapture --test-threads=1 \
  adaptive::source_bridge_tests adaptive::source_residual_tests product_final_case_tests product_certificate::tests \
  combine::tests origins::tests kf1_tracker_tests method_tests publication_tests
