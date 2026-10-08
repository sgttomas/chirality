#!/bin/bash
# RV126 addendum 01: the two edited tests at 0c7490e1be (archive copy), fresh target, through t3_cargo.sh.
set -u
WT=WT; S=$WT/scratch/rv126_n; P=$WT/rv126/projects/chirality-piping
export TMPDIR=$S/tmp CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4
L=$S/logs/r1_chain.log; : > "$L"
( cd "$P/core/solver/frame_kernel" && "$WT/tools/t3_cargo.sh" test --locked --offline --target-dir "$WT/targets/rv126-r1" --lib -- i51_support_hypot_identity_order_zero_subnormal_and_failed_prefixes correct_norm ) > "$S/logs/r1_fk.log" 2>&1
echo "fk rc=$? $(grep -E '^test result:' "$S/logs/r1_fk.log" | tail -1)" >> "$L"
( cd "$P/core/product_physics" && "$WT/tools/t3_cargo.sh" test --locked --offline --target-dir "$WT/targets/rv126-r1" --test preview_physics_runtime ) > "$S/logs/r1_pp.log" 2>&1
echo "pp rc=$? $(grep -E '^test result:' "$S/logs/r1_pp.log" | tail -1)" >> "$L"
echo CHAIN-DONE >> "$L"
