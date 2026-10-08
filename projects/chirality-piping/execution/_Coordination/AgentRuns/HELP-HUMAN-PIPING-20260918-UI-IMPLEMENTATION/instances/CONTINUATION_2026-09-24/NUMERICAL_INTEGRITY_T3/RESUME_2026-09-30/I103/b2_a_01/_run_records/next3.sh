#!/bin/bash
# I103: Part 2's suites (B3a-A head: PP; B2-A head and B3b-A head: PP and runner), the registered-build
# evidence at the B3b-A head, then the mutants. One heavy job at a time.
S=WT/scratch/i103_b2_a
$S/bin/run_suites.sh $S/b3a b3a pp
$S/bin/run_suites.sh $S/b2a2 b2a2 pp runner
$S/bin/run_suites.sh $S/b3b b3b pp runner
export TMPDIR=$S/tmp RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=1
unset RUSTFLAGS CARGO_ENCODED_RUSTFLAGS
cd $S/b3b/projects/chirality-piping
CARGO_TARGET_DIR=WT/targets/i103-b2-a-b3b-pp WT/tools/t3_cargo.sh test --locked --offline \
  --manifest-path core/product_physics/Cargo.toml --lib -- --nocapture profile_in_build_record reviewed_inputs_bind_the_lock \
  the_registered_profile_is_the_only_permit_source b3a_direct_entry_oracles b2_a_g_c_bounds > $S/runs/b3b/registered.log 2>&1
echo "registered rc=$? $(date -u +%FT%TZ)" >> $S/runs/b3b/meta.txt
WT/venv/bin/python -I $S/bin/mutants.py $S/mut $S/runs/mut > $S/runs/mut_driver.log 2>&1
echo "mutants rc=$? $(date -u +%FT%TZ)" >> $S/runs/b3b/meta.txt
echo "NEXT3-DONE" >> $S/runs/b3b/meta.txt
