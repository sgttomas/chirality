#!/bin/bash
# RV123 round 2, phase A2 (after phase A): PP registered suites again, with validation/ in the copies.
WT=WT
S2=$WT/scratch/rv123_rvp2/r2
J=$S2/tools/runjob.sh
W=$WT/rv123
until grep -q 'CHAIN-DONE phaseA ' $S2/logs/chain.log 2>/dev/null; do sleep 20; done
$J pp_reg_cand2 $W/cand/projects/chirality-piping/core/product_physics rv123-r2-pp-cand 0 test --locked --offline --no-fail-fast
$J pp_reg_base2 $W/base/projects/chirality-piping/core/product_physics rv123-r2-pp-base 0 test --locked --offline --no-fail-fast
echo "CHAIN-DONE phaseA2 $(date -u '+%FT%TZ')" >> $S2/logs/chain.log
