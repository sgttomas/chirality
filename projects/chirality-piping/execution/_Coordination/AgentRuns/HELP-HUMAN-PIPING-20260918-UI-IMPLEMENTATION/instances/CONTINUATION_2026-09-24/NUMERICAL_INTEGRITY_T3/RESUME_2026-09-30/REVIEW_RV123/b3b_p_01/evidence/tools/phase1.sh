#!/bin/bash
# RV123 phase 1: suites on pristine base and candidate copies, one cargo job at a time.
WT=WT
S=$WT/scratch/rv123_rvp2
J=$S/tools/runjob.sh
PPB=$S/base/projects/chirality-piping/core/product_physics
PPC=$S/cand/projects/chirality-piping/core/product_physics
RNB=$S/base/projects/chirality-piping/core/runner/headless
RNC=$S/cand/projects/chirality-piping/core/runner/headless
$J pp_reg_cand   $PPC rv123-pp-cand 0 test --locked --offline --no-fail-fast
$J pp_reg_base   $PPB rv123-pp-base 0 test --locked --offline --no-fail-fast
$J pp_stale_cand $PPC rv123-pp-cand-stale 1 test --locked --offline --no-fail-fast --lib
$J pp_stale_base $PPB rv123-pp-base-stale 1 test --locked --offline --no-fail-fast --lib
$J runner_cand   $RNC rv123-runner-cand 0 test --locked --offline --no-fail-fast
$J runner_base   $RNB rv123-runner-base 0 test --locked --offline --no-fail-fast
echo "CHAIN-DONE phase1 $(date -u '+%FT%TZ')" >> $S/logs/chain.log
