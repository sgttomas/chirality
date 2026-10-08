#!/bin/bash
# The remaining evidence at Part 2's head, one cargo job at a time.
WT=WT; S=$WT/scratch/i102_b2_k; T=$WT/targets/i102-b2-k
P1=$S/p1_tree; P2=$S/p2f_tree
$S/k13_capture.sh p1 $P1 $T/p1
$S/k13_capture.sh p2 $P2 $T/p2f
$S/run_cargo.sh p2f_pp_nff $P2/projects/chirality-piping/core/product_physics $T/p2f test --locked --offline --no-fail-fast
$S/run_cargo.sh p2f_profile_record $P2/projects/chirality-piping/core/product_physics $T/p2f test --locked --offline --lib retained_memory -- --nocapture
$S/run_cargo.sh p2f_k09_rows $P2/projects/chirality-piping/core/solver/frame_kernel $T/p2f test --locked --offline --lib b2k_k09 -- --nocapture
$S/compile_deps.sh p2f_deps $P2/projects/chirality-piping $T/p2f
$S/test_deps.sh main_deps_tests $S/main_tree/projects/chirality-piping $T/main
$S/test_deps.sh p2f_deps_tests $P2/projects/chirality-piping $T/p2f
echo FINAL_EVIDENCE_DONE
