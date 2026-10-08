#!/bin/bash
# I104 SQ (PLAN_v2 §3.4): the S1 witnesses, the inputs pin and the DEF-O report, one process per
# entry point, each through t3_slot.sh (not a measurement). Usage: witness_chain.sh <lib test binary> <tag>
set -uo pipefail
T=WT; S=$T/scratch/i104_b1_sq; BIN=$1; TAG=$2
O=$S/wit/$TAG; mkdir -p $O; LOG=$S/logs/witness_$TAG.log; : > $LOG
export TMPDIR=$S/tmp
cd $S/regcopy/projects/chirality-piping/core/product_physics
names=$($BIN --list --ignored 2>/dev/null | sed -n 's/: test$//p' | grep -E "^retained_memory::witness_tests::(witness_|def_o_)")
names="$names retained_memory::witness_tests::b1_sq_inputs_are_i86s_and_the_committed_helpers retained_memory::witness_tests::b1_t4_w2b_and_w6_phys_r4_inputs_are_no_triggered_case_pins"
for n in $names; do
  f=$O/$(echo $n | sed 's/retained_memory::witness_tests:://; s/::/./g').out
  $T/tools/t3_slot.sh $BIN $n --exact --include-ignored --test-threads=1 --nocapture > $f 2>&1
  echo "RUN $n exit $?" >> $LOG
done
echo "CHAIN-DONE" >> $LOG
