#!/bin/bash
# I101 B3 readers: the census over the corpus at b2 e67c364680 (07m) in RS and TS (RV113's harnesses), then b2's suites
# (RE all targets, desktop vitest whole, tsc) as the baseline. One heavy job at a time.
WT=WT
S=$WT/scratch/i101_b3r
J=$S/harness/job.sh
H=$S/copies/b2h/projects/chirality-piping; B=$S/copies/b2s/projects/chirality-piping
O=$S/out; mkdir -p $O
RV113_OUT=$O/b2_rs_census.jsonl RUST_TEST_THREADS=2 $J cargo b2_rs_census "$H/core/reporting/result_export" "$WT/targets/i101-b3r-b2h" test --locked --offline --test rv113_census
echo "rs census rc=$?"
$J slot b2_ts_census "$H/apps/desktop" /usr/bin/env RV113_OUT=$O/b2_ts_census.jsonl "$H/node_modules/.bin/vitest" run src/features/results/rv113Census.test.ts
echo "ts census rc=$?"
RUST_TEST_THREADS=4 $J cargo b2_re_suite "$B/core/reporting/result_export" "$WT/targets/i101-b3r-b2s" test --locked --offline --no-fail-fast
echo "re rc=$?"
$J slot b2_vitest "$B/apps/desktop" "$B/node_modules/.bin/vitest" run --reporter=dot --reporter=json --outputFile.json=$O/b2_vitest.json
echo "vitest rc=$?"
$J slot b2_tsc "$B/apps/desktop" "$B/node_modules/.bin/tsc" --noEmit -p tsconfig.json
echo "tsc rc=$?"
