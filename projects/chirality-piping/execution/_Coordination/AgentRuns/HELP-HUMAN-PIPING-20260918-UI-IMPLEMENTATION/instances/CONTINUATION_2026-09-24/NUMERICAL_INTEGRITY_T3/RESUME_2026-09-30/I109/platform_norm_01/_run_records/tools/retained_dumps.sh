#!/bin/bash
# I109: the retained-route documents behind the moved pins, from one scratch tree patched by
# regen_patch.py: W-C2's successor documents (the test's own I85_WC2_OUT writer) and SF-2's
# successors (I109_SF2_OUT). The tests' asserts may fail on the candidate; the files are written
# before them. Cargo through WT/tools/t3_cargo.sh.
# Usage: I109_WT=<WT> retained_dumps.sh <tree holding projects/chirality-piping> <out dir> <target dir>
set -u
T=${I109_WT:?set I109_WT to WT}; TREE=$1; OUT=$2; TGT=$3
P=$TREE/projects/chirality-piping; mkdir -p "$OUT/wc2" "$OUT/sf2"
export TMPDIR=$T/scratch/i109_norm/tmp CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8
cd "$P/core/product_physics" || exit 1
env I85_WC2_OUT="$OUT/wc2" I109_SF2_OUT="$OUT/sf2" "$T/tools/t3_cargo.sh" test --locked --offline --lib --target-dir "$TGT" -- \
  --exact retained_facade_tests::b1_sp_w_c2_direct_entry_publishes_the_pinned_successor \
  retained_facade_tests::b1_sp_sf2_selected_not_first_and_two_selected_pins --test-threads=1 --nocapture > "$OUT/tests.log" 2>&1
echo "DUMPS-DONE rc=$?"
# m08's intensified rows against the test's libm expression (reported, not asserted, in the patched tree)
"$T/tools/t3_cargo.sh" test --locked --offline --test preview_physics_runtime --target-dir "$TGT" -- --test-threads=1 --nocapture > "$OUT/m08.log" 2>&1
echo "M08-DONE rc=$?"
