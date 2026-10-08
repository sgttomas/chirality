#!/bin/bash
# usage: fk_suite.sh <rev> ; runs FK's full test suite for the scratch copy <rev> in a fresh target
set -u
S=WT/scratch/rv121_rvk
rev=$1
export TMPDIR=$S/tmp
export CARGO_TARGET_DIR=WT/targets/rv121-fk-$rev
cd $S/$rev/projects/chirality-piping/core/solver/frame_kernel || exit 3
WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast > $S/logs/fk_suite_$rev.log 2>&1
echo "rc=$?" >> $S/logs/fk_suite_$rev.log
