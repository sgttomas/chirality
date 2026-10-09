#!/bin/bash
# I110 round 4: byte passes at one harness tree with the declared text pairs (r4/text_pairs.json).
# Usage: bytes_passes.sh <hb|hc> <label>. Pass R: release, sets E, F, B1 (ordinary + runner). Pass W: debug, B1 with the retained direct entry (W1).
set -u
WT=WT; S=$WT/scratch/i110_pret; T=$1; L=$2
export TMPDIR=$S/tmp
export I110_TEXTS="$(python3 -I -c 'import json,sys; print(json.dumps(json.load(open(sys.argv[1]))))' $S/r4/text_pairs.json)"
cd $WT/t3-pret-$T/projects/chirality-piping/core/runner/headless || exit 2
I110_INPUTS=$S/harness/inputs.json I110_OUT=$S/ev4/bytes_${L}_release.jsonl I110_SETS=E,F,B1 \
  $WT/tools/t3_cargo.sh test --locked --offline --release --target-dir $WT/targets/i110-bytes-$T --test i110_bytes_harness -- --nocapture > $S/ev4/bytes_${L}_release.log 2>&1
echo "release rc=$?"
I110_INPUTS=$S/harness/inputs.json I110_OUT=$S/ev4/bytes_${L}_w1.jsonl I110_SETS=B1 I110_RETAINED=1 \
  $WT/tools/t3_cargo.sh test --locked --offline --target-dir $WT/targets/i110-bytes-$T --test i110_bytes_harness -- --nocapture > $S/ev4/bytes_${L}_w1.log 2>&1
echo "w1 rc=$?"
