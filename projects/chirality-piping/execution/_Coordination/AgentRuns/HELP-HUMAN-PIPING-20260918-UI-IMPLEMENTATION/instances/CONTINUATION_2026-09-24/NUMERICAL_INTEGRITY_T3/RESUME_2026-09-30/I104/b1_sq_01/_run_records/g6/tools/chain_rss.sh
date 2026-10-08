#!/bin/bash
# I104 SQ (PLAN_v2 §3.6): RSS_TIME's measurements, each batch under WT/tools/t3_exclusive.sh (all four slots),
# 3 repetitions, one process per measurement and one mode per process, binaries run directly.
set -uo pipefail
T=WT; S=$T/scratch/i104_b1_sq; LOG=$S/logs/chain_rss.log; : > $LOG
export TMPDIR=$S/tmp
for b in ${@:-devA devB devC rel}; do
  $T/tools/t3_exclusive.sh $S/bin/rss_batch.sh $S/rss/lists/$b.list $S/rss/$b 3 $LOG
  echo "batch $b exit $?" >> $LOG
done
echo "CHAIN-DONE" >> $LOG
