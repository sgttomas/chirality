#!/bin/bash
# I110 round 6: evidence on the final product head (t3-pret) and the byte passes at hc.
set -u
WT=WT; S=$WT/scratch/i110_pret
export TMPDIR=$S/tmp
mkdir -p $S/ev6/final
( $WT/tools/t3_slot.sh $WT/scratch/calib/run_suites_nff.sh $WT/t3-pret $S/ev6/final/suites_cand $WT/targets/i110-suites-cand > $S/ev6/final/suites_cand.log 2>&1; echo "suites rc=$?" >> $S/ev6/final/status.log ) &
( $S/r6/app_py_chain.sh $WT/t3-pret final > $S/ev6/final/chain.log 2>&1; echo "chain rc=$?" >> $S/ev6/final/status.log ) &
( $S/r6/bytes_passes.sh hc final > $S/ev6/final/bytes_passes.log 2>&1; echo "bytes rc=$?" >> $S/ev6/final/status.log ) &
wait
echo "ALL-DONE $(date -u +%FT%TZ)" >> $S/ev6/final/status.log
