#!/bin/bash
# RV127 addendum 02: build and run the byte harness v3 (full-output dumps) in one archive copy (debug). Arg: main|pr
set -u
WT=WT; S=$WT/scratch/rv127_u3; T=$1
export TMPDIR=$S/tmp
cd $WT/rv127/$T/projects/chirality-piping/core/runner/headless || exit 2
RV127_INPUTS=$S/a2/inputs.json RV127_OUT=$S/a2/bytes_$T.jsonl RV127_DUMP=$S/a2/dump_$T \
  $WT/tools/t3_cargo.sh test --locked --offline --target-dir $WT/targets/rv127-a2-$T --test rv127_bytes -- --nocapture > $S/a2/bytes_$T.log 2>&1
echo "$T rc=$?"
