#!/bin/bash
# RV122 addendum 02: one mutant on the drop candidate (the label admitted again as branch L), targeted tests.
WT=WT; S=$WT/scratch/rv122_rvq2
export TMPDIR=$S/tmp RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4
unset RUSTFLAGS CARGO_ENCODED_RUSTFLAGS
cd $S/arch_a2mut/projects/chirality-piping || exit 9
$WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast --manifest-path core/product_physics/Cargo.toml \
  --target-dir "$WT/targets/rv122-a2mut-pp" --lib -- b3a_dropped b3b_witness_inputs_and_routes every_family_clause the_registered_profile > $S/runs/a2_mut.log 2>&1
echo "A2-M1 rc=$? $(date -u +%FT%TZ)" >> $S/runs/a2_mut_meta.txt
