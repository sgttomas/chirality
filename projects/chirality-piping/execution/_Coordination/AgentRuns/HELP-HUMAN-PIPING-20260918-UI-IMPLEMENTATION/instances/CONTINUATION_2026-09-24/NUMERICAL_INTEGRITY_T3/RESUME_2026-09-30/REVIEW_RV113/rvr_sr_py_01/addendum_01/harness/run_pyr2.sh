#!/bin/bash
# RV113 (SR-PY repair 02): the heavy jobs, one at a time, each through WT/tools/t3_slot.sh.
WT=WT
S=$WT/scratch/rv113_rvr_01
T=$S/pyr2
J=$S/tools/rsr2_job.sh
VENV=VENV
B=$WT/targets/rv113-pybins2/release
P=$WT/rv113/py2-head/projects/chirality-piping
ENV="OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units"
# 1. the census over 07m; 2. the 392 probes
$J slot py2_census $P /usr/bin/env $ENV TMPDIR=$T/tmp $VENV/bin/python $S/tools/rv113_py_harness.py $P census $T/census/py2_head.jsonl; echo "census rc=$?"
$J slot py2_probes $P /usr/bin/env $ENV TMPDIR=$T/tmp $VENV/bin/python $S/tools/rv113_py_harness.py $P probes $S/tsr1/probes/probes_ts1.json $T/probes/py2_head.jsonl; echo "probes rc=$?"
# 3. the two retained test files in full, at the head (junit, hostname removed afterwards)
$J slot py2_tests $P /usr/bin/env $ENV TMPDIR=$T/tmp $VENV/bin/python -m pytest -p no:cacheprovider --basetemp=$T/tmp/basetemp -q -rf --junitxml=$T/suites/py2_retained.xml tests/test_retained_precision_contract.py tests/test_retained_precision_carriers.py; echo "tests rc=$?"
echo done
