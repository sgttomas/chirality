#!/bin/bash
# I101: the PY test session's two helper binaries (checked JSON, units), built once through WT/tools/t3_cargo.sh
# (--locked --offline) from a copy's crates into WT/targets/i101-b3r-pyh, so later pytest sessions build nothing.
# Usage: py_helpers.sh <copy name>
WT=WT
S=$WT/scratch/i101_b3r
C=$S/copies/$1/projects/chirality-piping
$S/harness/job.sh cargo pyh_cj $C/core/serialization/canonical_json $WT/targets/i101-b3r-pyh/cj build --locked --offline --release --features checked-cli --bin openpipestress_jcs_ijson || exit 1
$S/harness/job.sh cargo pyh_units $C/core/units $WT/targets/i101-b3r-pyh/units build --locked --offline --release --features cli --bin openpipestress_units
