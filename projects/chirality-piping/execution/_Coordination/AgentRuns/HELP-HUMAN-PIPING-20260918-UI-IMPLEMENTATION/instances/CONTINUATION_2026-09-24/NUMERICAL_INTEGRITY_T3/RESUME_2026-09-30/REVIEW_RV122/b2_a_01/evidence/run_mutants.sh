#!/bin/bash
# RV122: each mutant on a git-archive copy of the candidate head, PP --lib in full, one job at a time.
# Usage: run_mutants.sh [ids...]   (default: every id in mutants_def.py)
set -u
WT=WT
S=$WT/scratch/rv122_rvq2
PY=$WT/venv/bin/python
A=$S/arch_mut/projects/chirality-piping
PRISTINE=$S/arch_head/projects/chirality-piping/core/product_physics/src/retained_memory.rs
TARGET=$A/core/product_physics/src/retained_memory.rs
O=$S/runs/mutants; mkdir -p "$O"
export TMPDIR=$S/tmp RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4
unset RUSTFLAGS CARGO_ENCODED_RUSTFLAGS
IDS=${*:-$($PY -I $S/scripts/mutant_apply.py $S/scripts/mutants_def.py $PRISTINE /dev/null LIST)}
cd "$A" || exit 9
for id in $IDS; do
  $PY -I $S/scripts/mutant_apply.py $S/scripts/mutants_def.py "$PRISTINE" "$TARGET" "$id" > "$O/$id.check" || { echo "$id APPLY_FAILED" >> "$O/meta.txt"; continue; }
  $WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast --manifest-path core/product_physics/Cargo.toml \
    --target-dir "$WT/targets/rv122-pp" --lib > "$O/$id.log" 2>&1; rc=$?
  echo "$id rc=$rc $(date -u +%FT%TZ)" >> "$O/meta.txt"
done
cp "$PRISTINE" "$TARGET"
echo "DONE $(date -u +%FT%TZ)" >> "$O/meta.txt"
