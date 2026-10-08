#!/bin/bash
# I104 SQ G6: the registered scratch copy of b1-q's head; PP's whole suite in it (dev/test, fresh
# target i104-sq-reg); then the release lib test binary (fresh target i104-sq-rel). Cargo through t3_cargo.sh.
set -uo pipefail
T=WT; S=$T/scratch/i104_b1_sq; LOG=$S/logs/chain_reg.log; : > $LOG
export TMPDIR=$S/tmp CARGO_BUILD_JOBS=8
$S/bin/mk_regcopy.sh $1 >> $LOG 2>&1 || { echo "CHAIN-FAILED regcopy" >> $LOG; exit 1; }
cd $S/regcopy/projects/chirality-piping/core/product_physics
RUST_TEST_THREADS=4 $T/tools/t3_cargo.sh test --locked --offline --no-fail-fast --target-dir $T/targets/i104-sq-reg > $S/logs/reg_pp_suite.log 2>&1
echo "pp suite exit $?" >> $LOG
$T/tools/t3_cargo.sh test --release --locked --offline --no-run --lib --target-dir $T/targets/i104-sq-rel > $S/logs/rel_build.log 2>&1
rc=$?; echo "release build exit $rc" >> $LOG
[ $rc -eq 0 ] && echo "CHAIN-DONE" >> $LOG || echo "CHAIN-FAILED release build" >> $LOG
