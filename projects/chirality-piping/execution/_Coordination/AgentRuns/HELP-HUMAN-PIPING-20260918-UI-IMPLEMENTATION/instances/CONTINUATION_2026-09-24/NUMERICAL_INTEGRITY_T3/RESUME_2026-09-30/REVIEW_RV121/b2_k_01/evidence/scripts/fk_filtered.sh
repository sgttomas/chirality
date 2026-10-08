#!/bin/bash
# usage: fk_filtered.sh <rev> <target-suffix> <logname> [extra test args...]; runs FK lib tests with filters, nocapture
set -u
S=WT/scratch/rv121_rvk
rev=$1; tgt=$2; log=$3; shift 3
export TMPDIR=$S/tmp
export CARGO_TARGET_DIR=WT/targets/rv121-$tgt
cd $S/$rev/projects/chirality-piping/core/solver/frame_kernel || exit 3
WT/tools/t3_cargo.sh test --locked --offline --lib -- "$@" > $S/logs/$log.log 2>&1
echo "rc=$?" >> $S/logs/$log.log
