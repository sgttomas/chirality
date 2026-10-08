#!/bin/bash
# I101 addendum 01: assemble the addendum's files through sanitize.py (I101_APPWT set). Usage: assemble_a1.sh <records dir>
S=WT/scratch/i101_b1_sc_pins
R=$1; A=$R/_run_records/addendum_01
san() { python3 -I "$S/harness/sanitize.py" "$@"; }
rm -rf "$A"; mkdir -p "$A"
san "$S/records_stage/ADDENDUM_01.md" "$R/ADDENDUM_01.md"
san "$S/records_stage/commit_a1.txt" "$A/commit.txt"
san "$S/records_stage/commit_a1.diff" "$A/commit.diff"
san "$S/harness/chain_n6b_head.sh" "$A/chain_n6b_head.sh"
san "$S/harness/assemble_a1.sh" "$A/assemble_a1.sh"
for f in chain_a1.out a1_rs_carriers.log a1_ts_integration.log a1_py_carriers.log; do san "$S/logs/$f" "$A/$f"; done
san "$S/records_stage/py_bins.sha256" "$A/py_bins.sha256"
san "$S/records_stage/cargo_jobs_a1.log" "$A/cargo_jobs_a1.log"
san "$S/out/wasm_n6.sha256" "$A/wasm_n6.sha256"
echo "assembled $(find "$A" -type f | wc -l) files"
