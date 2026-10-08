#!/bin/bash
# I110 round 2: byte-equality passes at one harness tree (hb = base, hc = candidate).
# Pass R: release build, sets E, F and B1, ordinary entry and runner, both modes.
# Pass W: debug build (the registered profile), set B1, plus the retained direct entry (W1).
set -u
WT=WT; S=$WT/scratch/i110_pret; T=$1
export TMPDIR=$S/tmp
cd $WT/t3-pret-$T/projects/chirality-piping/core/runner/headless || exit 2
I110_INPUTS=$S/harness/inputs.json I110_OUT=$S/ev/bytes_${T}_release.jsonl I110_SETS=E,F,B1 \
  $WT/tools/t3_cargo.sh test --locked --offline --release --target-dir $WT/targets/i110-bytes-$T --test i110_bytes_harness -- --nocapture > $S/ev/bytes_${T}_release.log 2>&1
echo "release rc=$?"
I110_INPUTS=$S/harness/inputs.json I110_OUT=$S/ev/bytes_${T}_w1.jsonl I110_SETS=B1 I110_RETAINED=1 \
  $WT/tools/t3_cargo.sh test --locked --offline --target-dir $WT/targets/i110-bytes-$T --test i110_bytes_harness -- --nocapture > $S/ev/bytes_${T}_w1.log 2>&1
echo "w1 rc=$?"
