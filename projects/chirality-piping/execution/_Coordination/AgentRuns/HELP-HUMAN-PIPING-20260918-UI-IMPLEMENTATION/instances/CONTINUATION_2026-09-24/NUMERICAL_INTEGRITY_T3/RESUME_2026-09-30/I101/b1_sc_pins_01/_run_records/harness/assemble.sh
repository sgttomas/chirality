#!/bin/bash
# I101 (07n pins): assemble the short record, every text file through sanitize.py's placeholders (I101_APPWT set).
S=WT/scratch/i101_b1_sc_pins
R=$1
san() { python3 -I "$S/harness/sanitize.py" "$@"; }
rm -rf "$R"; mkdir -p "$R/_run_records/harness" "$R/_run_records/results" "$R/_run_records/logs" "$R/_run_records/host"
san "$S/records_stage/RETURN.md" "$R/RETURN.md"
san "$S/records_stage/commits.txt" "$R/_run_records/commits.txt"
san "$S/records_stage/pins.diff" "$R/_run_records/pins.diff.gz" gz
san "$S/records_stage/N6B_PROPOSED.diff" "$R/_run_records/N6B_PROPOSED.diff"
for f in "$S"/harness/*; do san "$f" "$R/_run_records/harness/$(basename "$f")"; done
for f in CENSUS_CMP.json census_cmp.out T12_TS.json SUITE_RE_SC_VS_HEAD.json; do san "$S/out/$f" "$R/_run_records/results/$f"; done
san "$S/out/SUITE_VITEST_SC_VS_HEAD.json" "$R/_run_records/results/SUITE_VITEST_SC_VS_HEAD.json.gz" gz
for r in rs ts; do san "$S/out/${r}_census.jsonl" "$R/_run_records/results/${r}_census_head.jsonl.gz" gz; done
for f in "$S"/logs/*; do b=$(basename "$f"); if [ "$(wc -c < "$f")" -gt 20000 ]; then san "$f" "$R/_run_records/logs/$b.gz" gz; else san "$f" "$R/_run_records/logs/$b"; fi; done
san "$S/records_stage/cargo_jobs_i101.log" "$R/_run_records/host/cargo_jobs_i101.log"
for f in "$S"/out/wasm_*.sha256; do san "$f" "$R/_run_records/host/$(basename "$f")"; done
echo "assembled $(find "$R" -type f | wc -l) files"
