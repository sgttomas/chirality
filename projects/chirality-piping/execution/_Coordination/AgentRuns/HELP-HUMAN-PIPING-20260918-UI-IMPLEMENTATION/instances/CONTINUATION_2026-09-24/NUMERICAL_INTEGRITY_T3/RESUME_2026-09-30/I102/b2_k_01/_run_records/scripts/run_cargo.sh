#!/bin/bash
# usage: run_cargo.sh <label> <crate-dir> <target-dir> <cargo args...>
# Runs one cargo job through the T3 wrapper; logs stdout+stderr and the exit code.
WT=WT
label=$1; dir=$2; target=$3; shift 3
log=$WT/scratch/i102_b2_k/logs/$label.log
export TMPDIR=$WT/scratch/i102_b2_k/tmp CARGO_TARGET_DIR=$target
cd "$dir" || exit 90
start=$(date -u +%FT%TZ)
"$WT/tools/t3_cargo.sh" "$@" > "$log" 2>&1; rc=$?
echo "RUN label=$label start=$start end=$(date -u +%FT%TZ) rc=$rc args=$*" >> "$log"
echo "RUN label=$label rc=$rc"
exit $rc
