#!/bin/bash
# RV123 phase 4 (after phase 3): scratch follow-ups in the check copy.
WT=WT
S=$WT/scratch/rv123_rvp2
until grep -q 'CHAIN-DONE phase3' $S/logs/chain.log 2>/dev/null; do sleep 30; done
$S/tools/runjob.sh pp_chk_followup $S/chk/projects/chirality-piping/core/product_physics rv123-pp-chk 0 test --locked --offline --no-fail-fast --lib rv123_followup -- --nocapture --test-threads=1
echo "CHAIN-DONE phase4 $(date -u '+%FT%TZ')" >> $S/logs/chain.log
