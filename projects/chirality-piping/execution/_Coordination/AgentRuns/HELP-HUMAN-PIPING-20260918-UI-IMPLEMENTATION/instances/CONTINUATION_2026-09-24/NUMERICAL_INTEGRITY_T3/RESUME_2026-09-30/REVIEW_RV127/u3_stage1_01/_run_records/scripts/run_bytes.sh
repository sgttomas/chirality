#!/bin/bash
# RV127: build and run the byte harness in one archive copy (debug, the registered profile). Arg: base|cand
set -u
WT=WT; S=$WT/scratch/rv127_u3; T=$1
export TMPDIR=$S/tmp
cd $WT/rv127/$T/projects/chirality-piping/core/runner/headless || exit 2
RV127_INPUTS=$S/inputs.json RV127_OUT=$S/ev/bytes_$T.jsonl \
  $WT/tools/t3_cargo.sh test --locked --offline --target-dir $WT/targets/rv127-$T --test rv127_bytes -- --nocapture > $S/ev/bytes_$T.log 2>&1
echo "$T rc=$?"
