#!/bin/bash
# RV123 phase 3 (after phase 2): the mutant copy's pristine control, then my mutants.
WT=WT
S=$WT/scratch/rv123_rvp2
until grep -q 'CHAIN-DONE phase2' $S/logs/chain.log 2>/dev/null; do sleep 30; done
PP=$S/mut/projects/chirality-piping/core/product_physics
$S/tools/runjob.sh mut_control $PP rv123-mut 0 test --locked --offline --no-fail-fast --lib -- b3b_ b3a_ b1_sp_ u3_permitted_path u3g2_ u1_constants --skip b3b_direct_entry_keeps_the_exact_ordinary_bytes --skip t13_committed_fallback_uz_is_byte_identical --test-threads=2
WT/venv/bin/python -I $S/tools/mutants.py $S/tools/mutants.json > $S/logs/mutants.out 2>&1
echo "CHAIN-DONE phase3 $(date -u '+%FT%TZ')" >> $S/logs/chain.log
