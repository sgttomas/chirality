#!/bin/bash
# RV124: every witness/control/DEF-O entry (lib binary) and every challenge entry, registered dev/test build,
# one process per entry point and mode, each through t3_slot.sh. Runs after the given pid exits.
S=WT/scratch/rv124_rvq; WT=WT; LOG=$S/logs/chain_wit.log
export TMPDIR=$S/tmp
WAITPID=$1
echo "waiting for pid $WAITPID $(date -u +%FT%TZ)" >> $LOG
while kill -0 $WAITPID 2>/dev/null; do sleep 20; done
echo "start $(date -u +%FT%TZ)" >> $LOG
LIB=$WT/targets/rv124-reg/debug/deps/open_pipe_stress_product_physics-5dc81c9f25711477
CH=$WT/targets/rv124-reg/debug/deps/retained_memory_challenge-6e650466fd96943c
mkdir -p $S/logs/wit $S/logs/chal
cd $S/reg/projects/chirality-piping/core/product_physics
while read -r t; do
  [ -n "$t" ] || continue
  f=$S/logs/wit/$(echo "$t" | sed 's/retained_memory::witness_tests:://; s/::/__/g').log
  $WT/tools/t3_slot.sh $LIB "$t" --exact --ignored --test-threads=1 --nocapture > $f 2>&1; rc=$?
  echo "wit rc=$rc $t $(date -u +%FT%TZ)" >> $LOG
done < $S/logs/witness_entries.txt
$CH --list --ignored 2>/dev/null | sed -n 's/: test$//p' > $S/logs/challenge_entries.txt
while read -r t; do
  [ -n "$t" ] || continue
  f=$S/logs/chal/$(echo "$t" | sed 's/::/__/g').log
  $WT/tools/t3_slot.sh $CH "$t" --exact --ignored --test-threads=1 --nocapture > $f 2>&1; rc=$?
  echo "chal rc=$rc $t $(date -u +%FT%TZ)" >> $LOG
done < $S/logs/challenge_entries.txt
$WT/tools/t3_slot.sh $CH retained_direct_peak_is_within_the_profiles_bounds --exact --test-threads=1 --nocapture > $S/logs/chal/default.log 2>&1
echo "chal rc=$? default $(date -u +%FT%TZ)" >> $LOG
echo "CHAIN-DONE" >> $LOG
