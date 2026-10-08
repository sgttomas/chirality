#!/bin/bash
# I101 (07n pins): the evidence at the head (copy hd: harnesses; hs: clean) and SC's head (sc: clean), one heavy job at a time.
WT=WT
S=$WT/scratch/i101_b1_sc_pins
J=$S/harness/job.sh
T12=$WT/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/I85/b1_sp_01/_run_records/final/t12_bytes
H=$S/copies/hd/projects/chirality-piping; HS=$S/copies/hs/projects/chirality-piping; SC=$S/copies/sc/projects/chirality-piping
O=$S/out; mkdir -p $O
RV113_OUT=$O/rs_census.jsonl RUST_TEST_THREADS=2 $J cargo head_rs_census "$H/core/reporting/result_export" "$WT/targets/i101-b1-sc-pins/hd" test --locked --offline --test rv113_census
echo "rs census rc=$?"
$J slot head_ts_census "$H/apps/desktop" /usr/bin/env RV113_OUT=$O/ts_census.jsonl "$H/node_modules/.bin/vitest" run src/features/results/rv113Census.test.ts
echo "ts census rc=$?"
$J slot head_ts_t12 "$H/apps/desktop" /usr/bin/env I101_T12_DIR=$T12 I101_T12_OUT=$O/T12_TS.json "$H/node_modules/.bin/vitest" run src/features/results/i101T12.test.ts
echo "ts t12 rc=$?"
RUST_TEST_THREADS=4 $J cargo head_re_suite "$HS/core/reporting/result_export" "$WT/targets/i101-b1-sc-pins/hs" test --locked --offline --no-fail-fast
echo "head re rc=$?"
RUST_TEST_THREADS=4 $J cargo sc_re_suite "$SC/core/reporting/result_export" "$WT/targets/i101-b1-sc-pins/sc" test --locked --offline --no-fail-fast
echo "sc re rc=$?"
$J slot head_vitest "$HS/apps/desktop" "$HS/node_modules/.bin/vitest" run --reporter=dot --reporter=json --outputFile.json=$O/vitest_head.json
echo "head vitest rc=$?"
$J slot sc_vitest "$SC/apps/desktop" "$SC/node_modules/.bin/vitest" run --reporter=dot --reporter=json --outputFile.json=$O/vitest_sc.json
echo "sc vitest rc=$?"
$J slot head_tsc "$HS/apps/desktop" "$HS/node_modules/.bin/tsc" --noEmit -p tsconfig.json
echo "head tsc rc=$?"
