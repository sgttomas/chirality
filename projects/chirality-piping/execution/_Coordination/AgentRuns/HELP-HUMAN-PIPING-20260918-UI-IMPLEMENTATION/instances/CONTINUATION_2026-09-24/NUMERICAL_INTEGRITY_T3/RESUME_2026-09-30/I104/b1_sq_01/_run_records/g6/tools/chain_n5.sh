#!/bin/bash
# I104 SQ G6: the N-5 chain (mcn_b1q) at c = 1, 2, 3 on the b1-q snapshot, each point through t3_slot.sh.
set -uo pipefail
export I104_WT=WT I104_RUNS=runs_n5
S=$I104_WT/scratch/i104_b1_sq; LOG=$S/logs/chain_n5.log; : > $LOG
for c in 1 2 3; do
  $I104_WT/tools/t3_slot.sh $S/bin/run_point.sh $S/mcn_b1q g5_c$c "{\"l\": 128, \"c\": $c}" > $S/logs/run_n5_c$c.txt 2>&1
  rc=$?; echo "point c=$c exit $rc" >> $LOG
  [ $rc -eq 0 ] || { echo "CHAIN-FAILED at c=$c" >> $LOG; exit 1; }
done
echo "CHAIN-DONE" >> $LOG
