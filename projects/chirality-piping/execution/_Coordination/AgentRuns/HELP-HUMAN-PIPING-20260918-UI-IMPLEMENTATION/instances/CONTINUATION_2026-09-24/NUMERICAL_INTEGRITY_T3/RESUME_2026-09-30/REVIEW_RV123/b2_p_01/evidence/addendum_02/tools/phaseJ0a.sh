#!/bin/bash
# RV123 round 2, addendum 02 (J0a, e582b61f9e): B2-P witness dump, byte harness on J0a and main
# (ec5d397359), then the pristine J0a PP registered suite. One cargo job at a time.
WT=WT
S2=$WT/scratch/rv123_rvp2/r2
J=$S2/tools/runjob.sh
W=$WT/rv123
export RV123_IN=$WT/scratch/rv123_rvp2/i99_inputs RV123_EXTRA=S/i98_inputs/builtin_case_c.json,S/i98_inputs/builtin_l0_isolated_node.json,S/i98_inputs/builtin_milestone.json,S/i98_inputs/builtin_two_body_case_a.json,S/i98_inputs/builtin_two_body_case_b.json,S/i98_inputs/cause_milestone_reversed.json,S/i98_inputs/cb1_a_halfb_canonical.json,S/i98_inputs/cb1_ab.json,S/i98_inputs/cb1_ab_canonical.json,S/i98_inputs/cb1_ac_canonical.json,S/i98_inputs/cb2_case_c.json,S/i98_inputs/cb3_a.json,S/i98_inputs/cb3_v1_ab.json,S/i98_inputs/cb3_v1_b.json,S/i98_inputs/r7_cb1.json,S/i98_inputs/r7_cb1_halfb.json,S/i98_inputs/r7_cb2.json,S/i98_inputs/r7_cb3_v1.json,
mkdir -p $S2/dump_j0a $S2/bytes/j0a $S2/bytes/main
RV123_DUMP=$S2/dump_j0a $J j0a_dump $W/j0achk/projects/chirality-piping/core/product_physics rv123-r2-j0achk 0 test --locked --offline --no-fail-fast --lib rv123_r2_dump -- --nocapture --test-threads=1
RV123_OUT=$S2/bytes/j0a $J j0a_bytes $W/j0achk/projects/chirality-piping/core/product_physics rv123-r2-j0achk 0 test --locked --offline --no-fail-fast --test rv123_bytes -- --nocapture
RV123_OUT=$S2/bytes/main $J main_bytes $W/mainchk/projects/chirality-piping/core/product_physics rv123-r2-mainchk 0 test --locked --offline --no-fail-fast --test rv123_bytes -- --nocapture
$J j0a_pp_reg $W/j0a/projects/chirality-piping/core/product_physics rv123-r2-j0a 0 test --locked --offline --no-fail-fast
echo "CHAIN-DONE phaseJ0a $(date -u '+%FT%TZ')" >> $S2/logs/chain.log
