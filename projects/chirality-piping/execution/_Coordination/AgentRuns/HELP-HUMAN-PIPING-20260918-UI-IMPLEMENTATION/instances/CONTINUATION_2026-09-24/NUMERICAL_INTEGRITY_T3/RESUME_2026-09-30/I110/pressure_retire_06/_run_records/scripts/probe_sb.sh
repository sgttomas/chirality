#!/bin/bash
# I110 round 6: probe the source-block rows at hb (no T2) and hc (final head) with dumps.
set -u
WT=WT; S=$WT/scratch/i110_pret
export TMPDIR=$S/tmp
export I110_TEXTS="$(python3 -I -c 'import json,sys; print(json.dumps(json.load(open(sys.argv[1]))))' $S/r4/text_pairs.json)"
for T in hb hc; do
  mkdir -p $S/r6/probe/$T; rm -f $S/r6/probe/$T/*
  cd $WT/t3-pret-$T/projects/chirality-piping/core/runner/headless || exit 2
  I110_INPUTS=$S/r6/harness/inputs_sb.json I110_OUT=$S/r6/probe/$T.jsonl I110_SETS=F I110_DUMP_DIR=$S/r6/probe/$T I110_DUMP_MATCH=/ \
    $WT/tools/t3_cargo.sh test --locked --offline --release --target-dir $WT/targets/i110-bytes-$T --test i110_bytes_harness -- --nocapture > $S/r6/probe/$T.log 2>&1
  echo "$T rc=$?"
done
