#!/bin/bash
# RV120: PY's heavy jobs at I4 and at PY's head, one at a time, each through WT/tools/t3_slot.sh: RV113's PY harness
# (07m census and my 435 probes) on the head; then the three retained reader test files at I4 and at the head (junit;
# the host attribute is removed when the record is sealed).
# Usage: run_py_chain.sh   (expects copies/py-i4 and copies/py-head, and the authority binaries in WT/targets/rv120-pybins)
WT=WT
S=$WT/scratch/rv120_rvr
J=$S/tools/rv120_job.sh
B=$WT/targets/rv120-pybins/release
ENV="OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units PYTHONDONTWRITEBYTECODE=1"
P() { echo $S/copies/$1/projects/chirality-piping; }
$J slot py_head_census $(P py-head) /usr/bin/env $ENV $WT/venv/bin/python $S/tools/rv113_py_harness.py $(P py-head) census $S/census/py_head.jsonl; echo "py_head_census rc=$?"
$J slot py_head_probes $(P py-head) /usr/bin/env $ENV $WT/venv/bin/python $S/tools/rv113_py_harness.py $(P py-head) probes $S/probes/probes_rv120_all.json $S/probes/py_head.jsonl; echo "py_head_probes rc=$?"
for c in i4 head; do
  mkdir -p $S/tmp/py_$c
  $J slot py_${c}_tests $(P py-$c) /usr/bin/env $ENV $WT/venv/bin/python -m pytest -p no:cacheprovider --basetemp=$S/tmp/py_$c/basetemp -q -rf --junitxml=$S/suites/py_${c}_retained.xml tests/test_retained_precision_contract.py tests/test_retained_precision_carriers.py tests/test_retained_precision_schema.py; echo "py_${c}_tests rc=$?"
done
echo py-chain-done
