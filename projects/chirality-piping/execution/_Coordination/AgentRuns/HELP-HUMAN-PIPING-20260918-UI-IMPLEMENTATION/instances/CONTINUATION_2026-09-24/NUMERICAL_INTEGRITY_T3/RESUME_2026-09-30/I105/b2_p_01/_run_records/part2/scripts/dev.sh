#!/bin/bash
# I105 (lane P): a dev cargo job in WT/b2's PP, through the T3 slot wrapper, one at a time.
# Usage: dev.sh <log-name> <cargo args...>   (run in PP; target WT/targets/i105-b2-p-dev)
set -u
WT=WT
S=$WT/scratch/i105_b2_p
LOG=$S/runs/dev/$1.log; shift
mkdir -p "$S/runs/dev" "$S/tmp"
export TMPDIR=$S/tmp RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=1 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4
unset RUSTFLAGS CARGO_ENCODED_RUSTFLAGS
cd $WT/b2/projects/chirality-piping/core/product_physics || exit 9
CARGO_TARGET_DIR=$WT/targets/i105-b2-p-dev $WT/tools/t3_cargo.sh "$@" > "$LOG" 2>&1
rc=$?
echo "rc=$rc" >> "$LOG"
exit $rc
