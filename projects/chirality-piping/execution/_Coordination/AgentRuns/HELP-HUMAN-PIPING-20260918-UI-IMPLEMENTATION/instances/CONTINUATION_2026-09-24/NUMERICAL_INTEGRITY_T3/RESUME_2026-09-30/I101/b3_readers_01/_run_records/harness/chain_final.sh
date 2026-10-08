#!/bin/bash
# I101 B3 readers, the final chain at the lane heads, one heavy job at a time:
#  1. chain_head.sh: the census (RS at the RS head, TS at the TS head), the RE suite at the RS head, vitest and tsc at the TS head;
#  2. the RE suite at the TS head (b2-t holds b2-r and the golden);
#  3. the PY carrier-schema set at the TS head (helpers prebuilt by py_helpers.sh);
#  4. PP's B3 tests at the TS head with --nocapture: the producer's own m3x and m3l witnesses through these readers;
#  5. the three readers' shapes: RS (RS head) and TS (TS head) readings and inputs, then PY (I100's head) on the RS inputs.
# Usage: chain_final.sh <label> <rs commit> <ts commit> <py commit>
WT=WT
S=$WT/scratch/i101_b3r
J=$S/harness/job.sh
L=$1; RC=$2; TC=$3; PYC=$4
O=$S/out; mkdir -p $O/$L
$S/harness/chain_head.sh $L $RC $TC
TS=$S/copies/${L}_ts/projects/chirality-piping; RS=$S/copies/${L}_rs/projects/chirality-piping
RUST_TEST_THREADS=4 $J cargo ${L}_re_suite_t "$TS/core/reporting/result_export" "$WT/targets/i101-b3r-b2s" test --locked --offline --no-fail-fast
echo "re at ts rc=$?"
$J slot ${L}_py_schema $S /bin/bash $S/harness/py_schema.sh ${L}_ts ${L}_py_schema
echo "py schema rc=$?"
RUST_TEST_THREADS=4 $J cargo ${L}_pp_b3 "$TS/core/product_physics" "$WT/targets/i101-b3r-pp" test --locked --offline --lib b3 -- --nocapture
echo "pp b3 rc=$?"
B3B_SHAPES_OUT=$O/$L/rs_shapes.jsonl B3B_INPUTS_OUT=$O/$L/rs_inputs.jsonl RUST_TEST_THREADS=4 \
  $J cargo ${L}_rs_shapes "$RS/core/reporting/result_export" "$WT/targets/i101-b3r-b2s" test --locked --offline --test retained_precision_contract b3b_exact_successor_shapes
echo "rs shapes rc=$?"
$J slot ${L}_ts_shapes "$TS/apps/desktop" /usr/bin/env B3B_SHAPES_OUT=$O/$L/ts_shapes.jsonl B3B_INPUTS_OUT=$O/$L/ts_inputs.jsonl \
  "$TS/node_modules/.bin/vitest" run src/features/results/retainedPrecision.test.ts -t "165 shapes"
echo "ts shapes rc=$?"
$S/harness/make_copy.sh b2-p "$PYC" ${L}_p s > $O/$L/copy_p.txt || { echo "py copy failed"; exit 1; }
$J slot ${L}_py_shapes $S /bin/bash $S/harness/py_shapes.sh ${L}_p $O/$L/rs_inputs.jsonl $O/$L/py_shapes.jsonl
echo "py shapes rc=$?"
