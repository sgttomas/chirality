#!/bin/bash
# I101: PY's three readings of the B3b shapes on the Rust inputs, in an archive copy of I100's committed PY head.
# Usage: py_shapes.sh <copy name> <inputs> <out>
WT=WT
S=$WT/scratch/i101_b3r
# The helper binaries built once through t3_cargo.sh (py_helpers.sh), if the reader's hashing needs them.
export OPENPIPESTRESS_CHECKED_JSON_BIN=$WT/targets/i101-b3r-pyh/cj/release/openpipestress_jcs_ijson
export OPENPIPESTRESS_UNITS_BIN=$WT/targets/i101-b3r-pyh/units/release/openpipestress_units
cd $S/copies/$1/projects/chirality-piping && $WT/venv/bin/python -I $S/harness/py_shapes.py "$2" "$3"
