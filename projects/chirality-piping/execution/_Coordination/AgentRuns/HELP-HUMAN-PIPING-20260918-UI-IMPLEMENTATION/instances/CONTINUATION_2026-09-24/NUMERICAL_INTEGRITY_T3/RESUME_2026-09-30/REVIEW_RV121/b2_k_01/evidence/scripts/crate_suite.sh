#!/bin/bash
# usage: crate_suite.sh <rev> <relative crate path> [mode]; mode=test (default) or norun
set -u
S=WT/scratch/rv121_rvk
rev=$1; crate=$2; mode=${3:-test}
name=$(echo "$crate" | tr '/' '_')
export TMPDIR=$S/tmp
export CARGO_TARGET_DIR=WT/targets/rv121-$rev-$name
cd $S/$rev/projects/chirality-piping/$crate || exit 3
log=$S/logs/suite_${rev}_${name}_${mode}.log
start=$(date +%s)
if [ "$mode" = norun ]; then
  WT/tools/t3_cargo.sh test --locked --offline --no-run > $log 2>&1
else
  WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast > $log 2>&1
fi
rc=$?
echo "rc=$rc seconds=$(( $(date +%s) - start ))" >> $log
echo "$rev $crate $mode rc=$rc seconds=$(( $(date +%s) - start ))" >> $S/logs/suites_summary.txt
