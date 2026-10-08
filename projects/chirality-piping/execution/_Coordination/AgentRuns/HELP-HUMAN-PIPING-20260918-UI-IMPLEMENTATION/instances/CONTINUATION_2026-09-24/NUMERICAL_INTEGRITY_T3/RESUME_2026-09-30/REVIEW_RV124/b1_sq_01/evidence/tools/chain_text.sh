#!/bin/bash
# RV124: the TEXT + cap-priced chain points (I104's chain, rebuilt byte-identically), after the reg suite chain ends.
S=WT/scratch/rv124_rvq; WT=WT; LOG=$S/logs/chain_text.log
export TMPDIR=$S/tmp
WAITPID=$1
echo "waiting for pid $WAITPID $(date -u +%FT%TZ)" >> $LOG
while kill -0 $WAITPID 2>/dev/null; do sleep 20; done
echo "start $(date -u +%FT%TZ)" >> $LOG
W=$S/base/projects/chirality-piping; C=$S/chain
run() { # chain tag caps
  $WT/tools/t3_slot.sh $S/bin/run_point_rv.sh $C/$1 $C/runs/$2 "$3" $W > $S/logs/point_$2.txt 2>&1; rc=$?
  echo "point $2 rc=$rc $(date -u +%FT%TZ)" >> $LOG; return $rc
}
run mcr_b1q g5_c3 '{"l": 128, "c": 3}' || { echo "CHAIN-FAILED g5_c3" >> $LOG; exit 1; }
for c in 1 2 3; do run mcn_b1q n5_c$c "{\"l\": 128, \"c\": $c}" || { echo "CHAIN-FAILED n5_c$c" >> $LOG; exit 1; }; done
echo "CHAIN-DONE" >> $LOG
