#!/bin/bash
# I101: the census over 07m and RV113's probes, in RS (cargo, through t3_cargo.sh) and in TS (vitest, through
# t3_slot.sh), one heavy job at a time. Usage: chain_census.sh <label> <rs copy> <ts copy>
# (copies are S/copies/<name>, made with make_copy.sh mode h)
WT=WT
S=$WT/scratch/i101_b1_i4p_rs_ts
J=$S/harness/job.sh
lab=$1; rsc=$S/copies/$2/projects/chirality-piping; tsc=$S/copies/$3/projects/chirality-piping
O=$S/out/$lab; mkdir -p "$O"
RV113_OUT="$O/rs_census.jsonl" RV113_PROBES="$S/probes/probes_i101.json" RV113_PROBES_OUT="$O/rs_probes.jsonl" RUST_TEST_THREADS=2 \
  $J cargo ${lab}_rs_census "$rsc/core/reporting/result_export" "$WT/targets/i101-b1-i4p-rs-ts/$lab-rs" \
  test --locked --offline --test rv113_census
echo "rs rc=$?"
$J slot ${lab}_ts_census "$tsc/apps/desktop" /usr/bin/env RV113_OUT="$O/ts_census.jsonl" RV113_PROBES="$S/probes/probes_i101.json" \
  RV113_PROBES_OUT="$O/ts_probes.jsonl" "$tsc/node_modules/.bin/vitest" run src/features/results/rv113Census.test.ts
echo "ts rc=$?"
