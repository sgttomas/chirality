#!/bin/bash
# I101: the suites in a clean copy (make_copy.sh mode s), one heavy job at a time.
# Usage: chain_suites.sh <label> <copy> <rs|ts|both>
#   rs: RE's whole cargo test (through t3_cargo.sh)
#   ts: the whole desktop vitest suite (JSON report) and tsc --noEmit (each through t3_slot.sh)
WT=WT
S=$WT/scratch/i101_b1_i4p_rs_ts
J=$S/harness/job.sh
lab=$1; P=$S/copies/$2/projects/chirality-piping; which=$3
O=$S/out/$lab; mkdir -p "$O"
if [ "$which" != ts ]; then
  RUST_TEST_THREADS=4 $J cargo ${lab}_re_suite "$P/core/reporting/result_export" "$WT/targets/i101-b1-i4p-rs-ts/$lab-re" \
    test --locked --offline
  echo "re rc=$?"
fi
if [ "$which" != rs ]; then
  $J slot ${lab}_vitest "$P/apps/desktop" "$P/node_modules/.bin/vitest" run --reporter=dot --reporter=json --outputFile.json="$O/vitest.json"
  echo "vitest rc=$?"
  $J slot ${lab}_tsc "$P/apps/desktop" "$P/node_modules/.bin/tsc" --noEmit -p tsconfig.json
  echo "tsc rc=$?"
fi
