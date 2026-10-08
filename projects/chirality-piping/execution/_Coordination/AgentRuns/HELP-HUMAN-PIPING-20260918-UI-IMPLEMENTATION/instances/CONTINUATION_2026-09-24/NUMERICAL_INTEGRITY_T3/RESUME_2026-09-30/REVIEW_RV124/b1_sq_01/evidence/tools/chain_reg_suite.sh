#!/bin/bash
# RV124: PP's suite on the candidate with the registration applied (registered dev/test build), fresh target.
S=WT/scratch/rv124_rvq; WT=WT
export TMPDIR=$S/tmp
LOG=$S/logs/chain_reg_suite.log
cd $S/reg/projects/chirality-piping/core/product_physics || { echo "CHAIN-FAILED cd" >> $LOG; exit 1; }
echo "start $(date -u +%FT%TZ)" >> $LOG
$WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast --target-dir $WT/targets/rv124-reg > $S/logs/reg_suite.out 2>&1; rc=$?
echo "reg suite rc=$rc $(date -u +%FT%TZ)" >> $LOG
echo "CHAIN-DONE rc=$rc" >> $LOG
