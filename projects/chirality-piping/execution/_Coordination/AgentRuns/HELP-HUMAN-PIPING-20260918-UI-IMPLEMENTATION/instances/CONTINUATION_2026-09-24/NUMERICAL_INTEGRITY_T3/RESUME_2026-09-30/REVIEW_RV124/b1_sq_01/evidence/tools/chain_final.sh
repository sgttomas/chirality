#!/bin/bash
# RV124: the registered law tests with output, then a few RSS/time reproductions (exclusive), after the given pid.
S=WT/scratch/rv124_rvq; WT=WT; LOG=$S/logs/chain_final.log
export TMPDIR=$S/tmp
WAITPID=$1
echo "waiting for pid $WAITPID $(date -u +%FT%TZ)" >> $LOG
while kill -0 $WAITPID 2>/dev/null; do sleep 20; done
echo "start $(date -u +%FT%TZ)" >> $LOG
LIB=$WT/targets/rv124-reg/debug/deps/open_pipe_stress_product_physics-5dc81c9f25711477
cd $S/reg/projects/chirality-piping/core/product_physics
$WT/tools/t3_slot.sh $LIB retained_memory::law_tests --test-threads=1 --nocapture > $S/logs/law_registered_nocapture.log 2>&1
echo "law rc=$? $(date -u +%FT%TZ)" >> $LOG
$WT/tools/t3_exclusive.sh $S/bin/rss_batch_rv.sh
echo "rss exclusive rc=$? $(date -u +%FT%TZ)" >> $LOG
echo "CHAIN-DONE" >> $LOG
