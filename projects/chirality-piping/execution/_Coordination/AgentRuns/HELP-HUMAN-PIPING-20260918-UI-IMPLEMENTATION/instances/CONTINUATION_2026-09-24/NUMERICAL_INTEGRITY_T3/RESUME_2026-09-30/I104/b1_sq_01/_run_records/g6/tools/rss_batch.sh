#!/bin/bash
# I104 SQ (PLAN_v2 §3.6): one RSS/time batch. Run it under WT/tools/t3_exclusive.sh only.
# Each line of <list>: <tag> <binary> <exact test name>. Each runs <reps> times, one process each:
#   /usr/bin/time -l <binary> <test> --exact --ignored --test-threads=1 --nocapture
# Outputs: <out>/<tag>.r<k>.out (stdout+stderr of the test) and <out>/<tag>.r<k>.time (time -l).
# Usage: rss_batch.sh <list> <out dir> <reps> <log>
set -u
LIST=$1; OUT=$2; REPS=$3; LOG=$4
mkdir -p "$OUT"
cd WT/b1-q/projects/chirality-piping/core/product_physics
echo "BATCH-START $(date -u '+%FT%TZ') list=$(basename $LIST) reps=$REPS" >> "$LOG"
while read -r tag bin test; do
  [ -z "$tag" ] && continue
  case "$tag" in \#*) continue;; esac
  for k in $(seq 1 "$REPS"); do
    /usr/bin/time -l "$bin" "$test" --exact --ignored --test-threads=1 --nocapture > "$OUT/$tag.r$k.out" 2> "$OUT/$tag.r$k.time"
    rc=$?
    echo "RUN $(date -u '+%FT%TZ') tag=$tag rep=$k rc=$rc" >> "$LOG"
  done
done < "$LIST"
echo "BATCH-DONE $(date -u '+%FT%TZ') list=$(basename $LIST)" >> "$LOG"
