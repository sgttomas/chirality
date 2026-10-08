#!/bin/bash
# I105 Part 2: PY's retained reader on the combination fixtures, as it behaves today. Builds the checked-JSON
# authority the reader hashes with (its own lockfile, its own target) through t3_cargo.sh, then runs the reader
# through t3_slot.sh on the p2head archive (638214d8d8). One heavy job at a time.
WT=WT
S=$WT/scratch/i105_b2_p
P=$S/p2head/projects/chirality-piping
export TMPDIR=$S/tmp RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0
unset RUSTFLAGS CARGO_ENCODED_RUSTFLAGS
T=$WT/targets/i105-b2-p-cjson
(cd $P/core/serialization/canonical_json && $WT/tools/t3_cargo.sh build --locked --offline --release --features checked-cli \
  --bin openpipestress_jcs_ijson --target-dir $T) > $S/runs/cjson_build.log 2>&1
echo "CHAIN-STEP cjson_build rc=$? $(date -u +%FT%TZ)" >> $S/runs/chain.log
OPENPIPESTRESS_CHECKED_JSON_BIN=$T/release/openpipestress_jcs_ijson $WT/tools/t3_slot.sh $WT/venv/bin/python -I $S/bin/readers_today_py.py $P \
  $P/fixtures/results/retained_precision_combination_successor_sparse_interactive.json \
  $P/fixtures/results/retained_precision_combination_successor_dense_scrutiny.json > $S/runs/readers_py.log 2>&1
echo "CHAIN-DONE py_reader rc=$? $(date -u +%FT%TZ)" >> $S/runs/chain.log
