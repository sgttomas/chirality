#!/bin/bash
# RV124: a few RSS/time reproductions of RSS_TIME.md's dev/test runs. Run only under WT/tools/t3_exclusive.sh.
# One process per measurement, one mode per process, the binary run directly.
S=WT/scratch/rv124_rvq; WT=WT; OUT=$S/logs/rss; LOG=$OUT/batch.log
CH=$WT/targets/rv124-reg/debug/deps/retained_memory_challenge-6e650466fd96943c
mkdir -p $OUT; cd $S/reg/projects/chirality-piping/core/product_physics
echo "BATCH-START $(date -u +%FT%TZ)" >> $LOG
for spec in "i3_three_case::dense::direct 3" "c1::sparse::direct 3" "milestone::dense::direct 1" "process_floor 1"; do
  set -- $spec; t=$1; n=$2; tag=$(echo $t | sed 's/::/./g')
  for k in $(seq 1 $n); do
    /usr/bin/time -l $CH $t --exact --ignored --test-threads=1 --nocapture > $OUT/$tag.r$k.out 2> $OUT/$tag.r$k.time
    echo "RUN $(date -u +%FT%TZ) $tag r$k rc=$?" >> $LOG
  done
done
echo "BATCH-DONE $(date -u +%FT%TZ)" >> $LOG
