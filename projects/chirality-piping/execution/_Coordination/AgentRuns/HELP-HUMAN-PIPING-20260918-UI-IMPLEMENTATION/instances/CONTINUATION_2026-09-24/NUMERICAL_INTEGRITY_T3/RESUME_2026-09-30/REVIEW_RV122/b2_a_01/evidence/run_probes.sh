#!/bin/bash
# RV122: the probe tests (head copy with three appended probes) and the build-record tests with
# their output, at base and at the probe copy. One job at a time.
set -u
WT=WT
S=$WT/scratch/rv122_rvq2
O=$S/runs/probes; mkdir -p "$O"
export TMPDIR=$S/tmp RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4
unset RUSTFLAGS CARGO_ENCODED_RUSTFLAGS
for tag in probe; do
  cd "$S/arch_$tag/projects/chirality-piping" || exit 9
  for f in rv122_probe profile_in_build_record the_registered_profile_is_the_only_permit_source reviewed_inputs_bind_the_lock b3a_direct_entry_oracles b2_a_g_c_bounds; do
    $WT/tools/t3_cargo.sh test --locked --offline --manifest-path core/product_physics/Cargo.toml \
      --target-dir "$WT/targets/rv122-pp-$tag" --lib "$f" -- --nocapture --test-threads=1 > "$O/${tag}_$f.log" 2>&1
    echo "$tag $f rc=$? $(date -u +%FT%TZ)" >> "$O/meta.txt"
  done
done
echo "DONE $(date -u +%FT%TZ)" >> "$O/meta.txt"
