#!/bin/bash
# RV124 (Pass B confirmation): the uncommitted test-only change applied in the mut copy; the affected PP tests run once.
S=WT/scratch/rv124_rvq; WT=WT; LOG=$S/logs/passb_testchange.log
export TMPDIR=$S/tmp
cd $S/mut && patch -p1 < $S/passb/wt_test_change.diff > $LOG 2>&1
cd $S/mut/projects/chirality-piping/core/product_physics
$WT/tools/t3_cargo.sh test --locked --offline --lib --target-dir $WT/targets/rv124-mut -- retained_memory::law_tests b1_sq_inputs_are_i86s_and_the_committed_helpers b1_t4_w2b_and_w6_phys_r4_inputs_are_no_triggered_case_pins b1_sp_w_c2_fixtures_are_the_live_successors b1_sp_sf2_selected_not_first_and_two_selected_pins --test-threads=4 >> $LOG 2>&1
echo "tests rc=$?" >> $LOG
$WT/tools/t3_cargo.sh test --locked --offline --test retained_memory_challenge --target-dir $WT/targets/rv124-mut -- --test-threads=1 >> $LOG 2>&1
echo "challenge default rc=$?" >> $LOG
cd $S/mut && patch -p1 -R < $S/passb/wt_test_change.diff >> $LOG 2>&1
diff -rq $S/reg/projects/chirality-piping/core $S/mut/projects/chirality-piping/core >> $LOG 2>&1 && echo "mut copy restored CLEAN" >> $LOG
echo "CHAIN-DONE" >> $LOG
