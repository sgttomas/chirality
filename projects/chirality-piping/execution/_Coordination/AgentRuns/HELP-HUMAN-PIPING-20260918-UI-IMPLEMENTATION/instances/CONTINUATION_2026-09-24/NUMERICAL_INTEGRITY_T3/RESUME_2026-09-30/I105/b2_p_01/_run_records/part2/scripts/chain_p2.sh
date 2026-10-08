#!/bin/bash
# I105 Part 2: lane A proposal check (law tests on a scratch archive of the head with the proposal),
# then the 46 B2-P mutants on another archive of the head. One heavy job at a time.
WT=WT
S=$WT/scratch/i105_b2_p
export TMPDIR=$S/tmp RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=1 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4
unset RUSTFLAGS CARGO_ENCODED_RUSTFLAGS
cd $S/propcheck2/projects/chirality-piping/core/product_physics || exit 9
CARGO_TARGET_DIR=$WT/targets/i105-b2-p-mut $WT/tools/t3_cargo.sh test --locked --offline --lib -- retained_memory::law_tests > $S/runs/propcheck2.log 2>&1
echo "CHAIN-STEP propcheck2 rc=$? $(date -u +%FT%TZ)" >> $S/runs/chain.log
python3 $S/bin/mutants.py $S/mut_spec/p2.json $S/mut2 $S/runs/mut_p2 > $S/runs/mut_p2_driver.log 2>&1
echo "CHAIN-DONE p2_propcheck_mut rc=$? $(date -u +%FT%TZ)" >> $S/runs/chain.log
