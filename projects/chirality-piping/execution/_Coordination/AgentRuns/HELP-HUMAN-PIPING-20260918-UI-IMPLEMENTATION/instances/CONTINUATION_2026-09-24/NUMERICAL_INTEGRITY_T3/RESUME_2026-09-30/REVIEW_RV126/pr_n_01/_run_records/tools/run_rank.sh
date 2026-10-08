#!/bin/bash
# RV126: build and run the rank-screen differential harness (head vs parent) through t3_cargo.sh.
set -u
WT=WT; S=$WT/scratch/rv126_n
export TMPDIR=$S/tmp CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=4
L=$S/logs/rank_chain.log; : > "$L"
( cd "$S/rank" && "$WT/tools/t3_cargo.sh" build --locked --offline --release --target-dir "$WT/targets/rv126-rank" ) > "$S/logs/rank_build.log" 2>&1; echo "build rc=$?" >> "$L"
# Round 1 ran: "$WT/targets/rv126-rank/release/rv126_rank" 300000 > "$S/logs/rank_random.txt" (results/rank_random.txt), then the hunt
# without the direction and band counters (same seed; identical first-line counts). Round 2 (this file) reran the hunt only.
echo "random skipped (round 1 kept)" >> "$L"
"$WT/targets/rv126-rank/release/rv126_rank" hunt 2000 > "$S/logs/rank_hunt2.txt" 2>&1; echo "hunt rc=$?" >> "$L"
echo CHAIN-DONE >> "$L"
