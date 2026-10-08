#!/bin/bash
# RV126: PP and result_export suites on the archive copy of 8dd64c1835, fresh target, through t3_cargo.sh.
set -u
WT=WT; S=$WT/scratch/rv126_n; P=$WT/rv126/projects/chirality-piping
export TMPDIR=$S/tmp CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4
L=$S/logs/crates_chain.log; : > "$L"
for c in product_physics reporting/result_export solver/frame_kernel; do
  n=$(basename $c)
  if [ "$n" = frame_kernel ]; then
    ( cd "$P/core/$c" && "$WT/tools/t3_cargo.sh" test --locked --offline --no-fail-fast --target-dir "$WT/targets/rv126-crates" --lib --test correct_norm_oracle --test k5_constrained_bodies ) > "$S/logs/crate_$n.log" 2>&1
  else
    ( cd "$P/core/$c" && "$WT/tools/t3_cargo.sh" test --locked --offline --no-fail-fast --target-dir "$WT/targets/rv126-crates" ) > "$S/logs/crate_$n.log" 2>&1
  fi
  rc=$?
  echo "crate $n rc=$rc $(grep -E '^test result:' "$S/logs/crate_$n.log" | awk '{p+=$4; f+=$6; i+=$8} END {print "passed=" p " failed=" f " ignored=" i}')" >> "$L"
done
echo CHAIN-DONE >> "$L"
