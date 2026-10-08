#!/bin/bash
# RV125 on the recut head d07006c2f0: a fresh git-archive copy (WT/rv125/head2), the same harness and lib.rs delta, the
# registered build in the same target as before; then RE's two N-5 direct tests. One job at a time, each through
# the T3 cargo wrapper. reg_d07006c2f0.json and probe_d07006c2f0.json are byte-identical to reg.json and probe.json.
WT=WT; S=$WT/scratch/rv125_b1_x
E="env -u RUSTFLAGS -u CARGO_ENCODED_RUSTFLAGS TMPDIR=$S/tmp RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8"
cd $WT/rv125/head2/projects/chirality-piping/core/product_physics && $E RUST_TEST_THREADS=2 RV125_OUT=$S/out/reg3.json RV125_PROBE_OUT=$S/out/probe3.json \
  perl -e 'alarm shift; exec @ARGV' 3000 $WT/tools/t3_cargo.sh test --locked --offline --lib --target-dir $WT/targets/rv125-reg zz_rv125_ -- --ignored --nocapture
cd $WT/rv125/head2/projects/chirality-piping/core/reporting/result_export && $E \
  perl -e 'alarm shift; exec @ARGV' 1800 $WT/tools/t3_cargo.sh test --locked --offline --lib --target-dir $WT/targets/rv125-re rv95_n5
