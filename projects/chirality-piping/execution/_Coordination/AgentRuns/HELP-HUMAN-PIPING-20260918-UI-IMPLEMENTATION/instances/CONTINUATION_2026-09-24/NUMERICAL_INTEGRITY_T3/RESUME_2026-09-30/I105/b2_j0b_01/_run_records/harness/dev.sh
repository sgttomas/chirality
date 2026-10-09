#!/bin/bash
# I105 J0b: a dev cargo job in WT/b2-j0b's PP through the T3 slot wrapper. Usage: dev.sh <log-name> <cargo args...>
set -u
WT=WT
S=$WT/scratch/i105_j0b
LOG=$S/runs/dev/$1.log; shift
mkdir -p "$S/runs/dev" "$S/tmp"
export TMPDIR=$S/tmp RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=1 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4
unset RUSTFLAGS CARGO_ENCODED_RUSTFLAGS
cd $WT/b2-j0b/projects/chirality-piping/core/product_physics || exit 9
echo "# queued $(date -u +%FT%TZ)" > "$LOG"
CARGO_TARGET_DIR=$WT/targets/i105-j0b-dev $WT/tools/t3_cargo.sh "$@" >> "$LOG" 2>&1
rc=$?
echo "# end $(date -u +%FT%TZ) rc=$rc" >> "$LOG"
exit $rc
