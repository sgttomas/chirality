#!/bin/bash
# I104 SQ: the witnesses in the registered dev/test build, then in the release build, then QUAL §11's sweep.
set -uo pipefail
T=WT; S=$T/scratch/i104_b1_sq; LOG=$S/logs/chain_wit.log; : > $LOG
$S/bin/witness_chain.sh $T/targets/i104-sq-reg/debug/deps/open_pipe_stress_product_physics-43b1b61f11b799a3 dev; echo "dev witnesses done" >> $LOG
$S/bin/witness_chain.sh $T/targets/i104-sq-rel/release/deps/open_pipe_stress_product_physics-a1f79725a9648498 rel; echo "release witnesses done" >> $LOG
$T/tools/t3_slot.sh $S/bin/noncand_b1.sh > $S/logs/noncand.log 2>&1; echo "noncand exit $?" >> $LOG
for b in "dev $T/targets/i104-sq-reg/debug/deps/open_pipe_stress_product_physics-43b1b61f11b799a3" "rel $T/targets/i104-sq-rel/release/deps/open_pipe_stress_product_physics-a1f79725a9648498"; do
  set -- $b
  $T/tools/t3_slot.sh $2 retained_memory::law_tests --test-threads=1 --nocapture > $S/logs/law_$1.log 2>&1; echo "law $1 exit $?" >> $LOG
done
echo "CHAIN-DONE" >> $LOG
