#!/bin/bash
# RV124: the size probe (test code only) in the mutant copy, after the given pid.
S=WT/scratch/rv124_rvq; WT=WT; LOG=$S/logs/chain_probe2.log
export TMPDIR=$S/tmp
WAITPID=$1
echo "waiting for pid $WAITPID $(date -u +%FT%TZ)" >> $LOG
while kill -0 $WAITPID 2>/dev/null; do sleep 20; done
echo "start $(date -u +%FT%TZ)" >> $LOG
$WT/venv/bin/python $S/bin/size_probe.py add >> $LOG 2>&1
cd $S/mut/projects/chirality-piping/core/product_physics
$WT/tools/t3_cargo.sh test --locked --offline --lib --target-dir $WT/targets/rv124-mut -- rv124_size_probe --exact --nocapture > $S/logs/size_probe.log 2>&1
echo "probe rc=$? $(date -u +%FT%TZ)" >> $LOG
$WT/venv/bin/python $S/bin/size_probe.py remove >> $LOG 2>&1
diff -rq $S/reg/projects/chirality-piping/core $S/mut/projects/chirality-piping/core >> $LOG 2>&1 && echo "mut copy CLEAN" >> $LOG
echo "CHAIN-DONE" >> $LOG
