#!/bin/bash
# I105 J0b: the PY sessions' three helper binaries (checked JSON, binary64 JSON, units), built once through
# WT/tools/t3_cargo.sh from a copy's crates (canonical_json and units are byte-identical at all three heads).
# Usage: py_helpers.sh <copy name>
WT=WT
S=$WT/scratch/i105_j0b
C=$S/copies/$1/projects/chirality-piping; T=$WT/targets/i105-j0b-pyh
$S/bin/job.sh cargo pyh_cj $C/core/serialization/canonical_json $T/cj build --locked --offline --release --features checked-cli --bin openpipestress_jcs_ijson || exit 1
$S/bin/job.sh cargo pyh_cj64 $C/core/serialization/canonical_json $T/cj64 build --locked --offline --release --features checked-cli --bin openpipestress_jcs_binary64 || exit 1
$S/bin/job.sh cargo pyh_units $C/core/units $T/units build --locked --offline --release --features cli --bin openpipestress_units
