#!/bin/bash
# RV123 addendum 02: the byte harness at b2's merge parent 7cc786285c (after phaseJ0a).
WT=WT
S2=$WT/scratch/rv123_rvp2/r2
until grep -q 'CHAIN-DONE phaseJ0a' $S2/logs/chain.log 2>/dev/null; do sleep 20; done
export RV123_IN=$WT/scratch/rv123_rvp2/i99_inputs RV123_EXTRA=S/i98_inputs/builtin_case_c.json,S/i98_inputs/builtin_l0_isolated_node.json,S/i98_inputs/builtin_milestone.json,S/i98_inputs/builtin_two_body_case_a.json,S/i98_inputs/builtin_two_body_case_b.json,S/i98_inputs/cause_milestone_reversed.json,S/i98_inputs/cb1_a_halfb_canonical.json,S/i98_inputs/cb1_ab.json,S/i98_inputs/cb1_ab_canonical.json,S/i98_inputs/cb1_ac_canonical.json,S/i98_inputs/cb2_case_c.json,S/i98_inputs/cb3_a.json,S/i98_inputs/cb3_v1_ab.json,S/i98_inputs/cb3_v1_b.json,S/i98_inputs/r7_cb1.json,S/i98_inputs/r7_cb1_halfb.json,S/i98_inputs/r7_cb2.json,S/i98_inputs/r7_cb3_v1.json,
mkdir -p $S2/bytes/b
RV123_OUT=$S2/bytes/b $S2/tools/runjob.sh b_bytes $WT/rv123/bchk/projects/chirality-piping/core/product_physics rv123-r2-bchk 0 test --locked --offline --no-fail-fast --test rv123_bytes -- --nocapture
echo "CHAIN-DONE phaseJ0a_b $(date -u '+%FT%TZ')" >> $S2/logs/chain.log
