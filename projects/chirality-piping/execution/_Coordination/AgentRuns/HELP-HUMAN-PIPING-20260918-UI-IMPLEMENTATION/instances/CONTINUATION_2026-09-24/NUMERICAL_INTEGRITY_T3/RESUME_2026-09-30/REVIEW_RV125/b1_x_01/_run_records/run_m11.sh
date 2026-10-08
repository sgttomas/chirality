#!/bin/bash
# RV125: RV109 round 2's mutant M11 (N-1) on the recut copy: native_call moves the call's sources back in reverse.
# Applied with sed to WT/rv125/head2's retained_product.rs, the b1_sp_ tests run in a separate target, then the file is
# restored from its saved original (checked: no mutant line left). One job through the T3 cargo wrapper.
WT=WT; S=$WT/scratch/rv125_b1_x; F=$WT/rv125/head2/projects/chirality-piping/core/product_physics/src/retained_product.rs
cp $F $S/retained_product.rs.orig
sed -i '' 's/let mut back=sources.into_iter();/let mut back=sources.into_iter().rev(); \/\/ RV125 M11/' $F
cd $WT/rv125/head2/projects/chirality-piping/core/product_physics && env -u RUSTFLAGS -u CARGO_ENCODED_RUSTFLAGS TMPDIR=$S/tmp \
  RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=2 \
  perl -e 'alarm shift; exec @ARGV' 3000 $WT/tools/t3_cargo.sh test --locked --offline --lib --target-dir $WT/targets/rv125-mut b1_sp_ > $S/logs/m11.log 2>&1
cp $S/retained_product.rs.orig $F
