#!/bin/bash
# I101 repair 02: PY's census (I100's RV113 harness, rv113_py_harness.py, unchanged) over 07m and 07n in an archive copy of a
# b2-p commit; 07n's corpus bytes replace the copy's for the second run. Helper binaries built once through t3_cargo.sh.
# Usage: py_census.sh <copy name> <label>
WT=WT
S=$WT/scratch/i101_b3r
C=$S/copies/$1/projects/chirality-piping
export OPENPIPESTRESS_CHECKED_JSON_BIN=$WT/targets/i101-b3r-pyh/cj/release/openpipestress_jcs_ijson
export OPENPIPESTRESS_BINARY64_JSON_BIN=$WT/targets/i101-b3r-pyh/cj64/release/openpipestress_jcs_binary64
export OPENPIPESTRESS_UNITS_BIN=$WT/targets/i101-b3r-pyh/units/release/openpipestress_units
O=$S/repair2/pycensus
shasum -a 256 $C/fixtures/results/retained_precision_cases.json | sed "s#$WT#WT#" > $O/$2_07m.corpus.sha256
$WT/venv/bin/python -I $O/rv113_py_harness.py $C census $O/$2_07m.py.jsonl; echo "07m rc=$?"
cp $S/add1/c07n/retained_precision_cases.07n.json $C/fixtures/results/retained_precision_cases.json
shasum -a 256 $C/fixtures/results/retained_precision_cases.json | sed "s#$WT#WT#" > $O/$2_07n.corpus.sha256
$WT/venv/bin/python -I $O/rv113_py_harness.py $C census $O/$2_07n.py.jsonl; echo "07n rc=$?"
