#!/bin/bash
# RV125: the second registered-build run (zz_rv125_spot again, plus zz_rv125_probe), in the same archive copy and target
# as run_chain.sh's step 1, one job through the T3 cargo wrapper. reg2.json reproduced reg.json byte for byte.
WT=WT; S=$WT/scratch/rv125_b1_x
cd $WT/rv125/cand/projects/chirality-piping/core/product_physics && env -u RUSTFLAGS -u CARGO_ENCODED_RUSTFLAGS TMPDIR=$S/tmp \
  RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=2 \
  RV125_OUT=$S/out/reg2.json RV125_PROBE_OUT=$S/out/probe.json perl -e 'alarm shift; exec @ARGV' 3000 \
  $WT/tools/t3_cargo.sh test --locked --offline --lib --target-dir $WT/targets/rv125-reg zz_rv125_ -- --ignored --nocapture
