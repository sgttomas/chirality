#!/bin/bash
# I101 B3 readers: at a lane head, the census over the corpus (RV113's harnesses) in RS (b2-r) and TS (b2-t), then the
# suites (RE all targets at the RS head; desktop vitest whole and tsc at the TS head). One heavy job at a time.
# Usage: chain_head.sh <label> <rs commit> <ts commit>
WT=WT
S=$WT/scratch/i101_b3r
J=$S/harness/job.sh
L=$1; RC=$2; TC=$3
O=$S/out; mkdir -p $O
# A commit given as "-" skips that lane.
if [ "$RC" != - ]; then $S/harness/make_copy.sh b2-r "$RC" ${L}_rh h && $S/harness/make_copy.sh b2-r "$RC" ${L}_rs s || { echo "copies failed"; exit 1; }; fi
if [ "$TC" != - ]; then $S/harness/make_copy.sh b2-t "$TC" ${L}_th h && $S/harness/make_copy.sh b2-t "$TC" ${L}_ts s || { echo "copies failed"; exit 1; }; fi
RH=$S/copies/${L}_rh/projects/chirality-piping; RS=$S/copies/${L}_rs/projects/chirality-piping
TH=$S/copies/${L}_th/projects/chirality-piping; TS=$S/copies/${L}_ts/projects/chirality-piping
if [ "$RC" != - ]; then
RV113_OUT=$O/${L}_rs_census.jsonl RUST_TEST_THREADS=2 $J cargo ${L}_rs_census "$RH/core/reporting/result_export" "$WT/targets/i101-b3r-b2h" test --locked --offline --test rv113_census
echo "rs census rc=$?"
fi
if [ "$TC" != - ]; then
$J slot ${L}_ts_census "$TH/apps/desktop" /usr/bin/env RV113_OUT=$O/${L}_ts_census.jsonl "$TH/node_modules/.bin/vitest" run src/features/results/rv113Census.test.ts
echo "ts census rc=$?"
fi
if [ "$RC" != - ]; then
RUST_TEST_THREADS=4 $J cargo ${L}_re_suite "$RS/core/reporting/result_export" "$WT/targets/i101-b3r-b2s" test --locked --offline --no-fail-fast
echo "re rc=$?"
fi
if [ "$TC" != - ]; then
$J slot ${L}_vitest "$TS/apps/desktop" "$TS/node_modules/.bin/vitest" run --reporter=dot --reporter=json --outputFile.json=$O/${L}_vitest.json
echo "vitest rc=$?"
$J slot ${L}_tsc "$TS/apps/desktop" "$TS/node_modules/.bin/tsc" --noEmit -p tsconfig.json
echo "tsc rc=$?"
fi
