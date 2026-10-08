#!/bin/bash
# RV123 round 2, phase B (after phase A): the witness dump (check copy), then the mutants.
WT=WT
S2=$WT/scratch/rv123_rvp2/r2
until grep -q 'CHAIN-DONE phaseA2' $S2/logs/chain.log 2>/dev/null; do sleep 20; done
RV123_DUMP=$S2/dump $S2/tools/runjob.sh dump $WT/rv123/chk/projects/chirality-piping/core/product_physics rv123-r2-pp-chk 0 test --locked --offline --no-fail-fast --lib rv123_r2_dump -- --nocapture --test-threads=1
$S2/tools/runjob.sh mut_control $WT/rv123/mut/projects/chirality-piping/core/product_physics rv123-r2-mut 0 test --locked --offline --no-fail-fast --lib -- b2p_ b3b_ b1_sp_ u3_permitted_path u3g2_ u1_constants i51_c0 --skip b2p_w_cb1_ --skip t13_committed_fallback_uz_is_byte_identical --test-threads=2
$WT/venv/bin/python -I $S2/tools/mutants.py $S2/tools/mutants.json > $S2/logs/mutants.out 2>&1
echo "CHAIN-DONE phaseB $(date -u '+%FT%TZ')" >> $S2/logs/chain.log
