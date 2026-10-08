#!/bin/bash
# RV120: the PY authority binaries (two cargo builds, from the I4 copy), then RV113's PY harness on PY at I4:
# the 07m census and my 435 probes. One heavy job at a time.
WT=WT
S=$WT/scratch/rv120_rvr
J=$S/tools/rv120_job.sh
P=$S/copies/py-i4/projects/chirality-piping
T=$WT/targets/rv120-pybins
$J cargo pybins_jcs $P/core/serialization/canonical_json $T build --locked --offline --release --features checked-cli --bin openpipestress_jcs_ijson --bin openpipestress_jcs_binary64; echo "pybins_jcs rc=$?"
$J cargo pybins_units $P/core/units $T build --locked --offline --release --features cli --bin openpipestress_units; echo "pybins_units rc=$?"
B=$T/release
ENV="OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units PYTHONDONTWRITEBYTECODE=1"
$J slot py_i4_census $P /usr/bin/env $ENV $WT/venv/bin/python $S/tools/rv113_py_harness.py $P census $S/census/py_i4.jsonl; echo "py_i4_census rc=$?"
$J slot py_i4_probes $P /usr/bin/env $ENV $WT/venv/bin/python $S/tools/rv113_py_harness.py $P probes $S/probes/probes_rv120_all.json $S/probes/py_i4.jsonl; echo "py_i4_probes rc=$?"
echo py-i4-done
