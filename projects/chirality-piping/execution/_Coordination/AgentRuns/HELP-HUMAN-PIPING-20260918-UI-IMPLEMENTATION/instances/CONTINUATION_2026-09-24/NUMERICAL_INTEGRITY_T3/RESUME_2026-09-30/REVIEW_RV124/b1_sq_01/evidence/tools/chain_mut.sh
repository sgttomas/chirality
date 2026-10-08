#!/bin/bash
# RV124: mutants on SQ's gate bounds, re-pins and guards (registered copy), one build at a time through t3_cargo.sh.
S=WT/scratch/rv124_rvq; WT=WT; LOG=$S/logs/chain_mut.log
export TMPDIR=$S/tmp
PY=$WT/venv/bin/python; MUT="$PY $S/bin/mutants.py"; TGT=$WT/targets/rv124-mut
WAITPID=$1
echo "waiting for pid $WAITPID $(date -u +%FT%TZ)" >> $LOG
while kill -0 $WAITPID 2>/dev/null; do sleep 20; done
echo "start $(date -u +%FT%TZ)" >> $LOG
mkdir -p $S/logs/mut
cd $S/mut/projects/chirality-piping/core/product_physics
run_sel() { # id selector
  case $2 in
    law)  $WT/tools/t3_cargo.sh test --locked --offline --lib --target-dir $TGT -- retained_memory::law_tests --test-threads=4 ;;
    s11f) $WT/tools/t3_cargo.sh test --locked --offline --test s11f_site_test --target-dir $TGT ;;
    chal) $WT/tools/t3_cargo.sh test --locked --offline --test retained_memory_challenge --target-dir $TGT -- b2_k1e3::dense::direct --exact --ignored --test-threads=1 --nocapture ;;
  esac
}
for m in M00 M01 M02 M03 M04 M05 M06 M07 M08 M09 M10 M11 M12 M13 M14 M15 M16 M17 M18 M19 M20 M21; do
  sel=$($MUT list | awk -F'\t' -v m=$m '$1==m{print $2}')
  $MUT apply $m > $S/logs/mut/$m.log 2>&1 || { echo "$m APPLY-FAILED" >> $LOG; continue; }
  run_sel $m $sel >> $S/logs/mut/$m.log 2>&1; rc=$?
  if [ $m = M00 ]; then
    run_sel $m s11f >> $S/logs/mut/$m.s11f.log 2>&1; echo "M00 s11f rc=$?" >> $LOG
    for t in def_o_b2_k1e3::sparse def_o_b2_k1e3::dense; do
      $WT/tools/t3_cargo.sh test --locked --offline --lib --target-dir $TGT -- retained_memory::witness_tests::$t --exact --ignored --test-threads=1 --nocapture > $S/logs/mut/M00.$t.log 2>&1
      echo "M00 probe $t rc=$?" >> $LOG
    done
  fi
  $MUT restore $m >> $S/logs/mut/$m.log 2>&1
  echo "$m sel=$sel rc=$rc $(date -u +%FT%TZ)" >> $LOG
done
diff -rq $S/reg/projects/chirality-piping/core $S/mut/projects/chirality-piping/core >> $LOG 2>&1 && echo "mut copy restored CLEAN" >> $LOG
echo "CHAIN-DONE" >> $LOG
