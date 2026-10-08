#!/bin/bash
# I103: after the first baseline pass, re-run base PP and runner with --no-fail-fast, then J1's suites,
# then J1's registered-build evidence (two law tests with their prints). One heavy job at a time.
S=WT/scratch/i103_b2_a
$S/bin/run_suites.sh $S/base base pp runner
$S/bin/run_suites.sh $S/j1 j1 bins re pp runner py ts
export TMPDIR=$S/tmp RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4
unset RUSTFLAGS CARGO_ENCODED_RUSTFLAGS
cd $S/j1/projects/chirality-piping
CARGO_TARGET_DIR=WT/targets/i103-b2-a-j1-pp WT/tools/t3_cargo.sh test --locked --offline \
  --manifest-path core/product_physics/Cargo.toml --lib -- --nocapture profile_in_build_record reviewed_inputs_bind_the_lock \
  the_registered_profile_is_the_only_permit_source > $S/runs/j1/registered.log 2>&1
echo "registered rc=$? $(date -u +%FT%TZ)" >> $S/runs/j1/meta.txt
echo "NEXT1-DONE" >> $S/runs/j1/meta.txt
