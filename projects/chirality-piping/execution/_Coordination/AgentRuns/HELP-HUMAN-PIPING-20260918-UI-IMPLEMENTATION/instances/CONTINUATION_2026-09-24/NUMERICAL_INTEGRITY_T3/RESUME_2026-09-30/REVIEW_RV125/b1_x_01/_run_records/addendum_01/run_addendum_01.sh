#!/bin/bash
# RV125 ADDENDUM_01: a git-archive copy of 7f5f72912e (WT/rv125/head3, P without execution/), zz_rv125_glibc.rs added
# with two lines appended to lib.rs (`#[cfg(test)] mod zz_rv125_glibc;`); the registered build (debug, 1.97.1, no
# RUSTFLAGS). One job at a time through the T3 cargo wrapper. Then the challenge test compiled only (no RSS run).
WT=WT; S=$WT/scratch/rv125_b1_x
cd $WT/rv125/head3/projects/chirality-piping/core/product_physics
env -u RUSTFLAGS -u CARGO_ENCODED_RUSTFLAGS TMPDIR=$S/tmp RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 \
  RUST_TEST_THREADS=2 RV125_GLIBC_OUT=$S/out/glibc.json perl -e 'alarm shift; exec @ARGV' 3000 $WT/tools/t3_cargo.sh test --locked --offline \
  --lib --target-dir $WT/targets/rv125-reg3 -- --include-ignored zz_rv125_glibc cap_maximal_ring b1_sq_inputs_are_i86s b1_t4_w2b_and_w6 b1_sp_w_c2 b1_sp_sf2
env -u RUSTFLAGS -u CARGO_ENCODED_RUSTFLAGS TMPDIR=$S/tmp RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 \
  perl -e 'alarm shift; exec @ARGV' 3000 $WT/tools/t3_cargo.sh test --locked --offline --test retained_memory_challenge --target-dir $WT/targets/rv125-reg3 --no-run
