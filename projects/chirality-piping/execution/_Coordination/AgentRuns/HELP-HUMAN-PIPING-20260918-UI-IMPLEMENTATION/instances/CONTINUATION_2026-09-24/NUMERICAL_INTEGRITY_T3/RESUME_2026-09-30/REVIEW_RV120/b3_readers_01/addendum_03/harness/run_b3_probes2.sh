#!/bin/bash
# RV120 B3: the three readers' raw readings of identical materialized inputs (one heavy job at a time).
# Usage: run_b3_probes.sh <label> <inputs.jsonl>   -> b3/probes/<label>_{rs,ts,py}.jsonl
WT=WT
S=$WT/scratch/rv120_rvr
B3=$S/b3
export RV120_LOGDIR=$B3/logs
J=$S/tools/rv120_job.sh
label=$1; IN=$2
P=$WT/rv120b3/${PROBECOPY:-probe}/projects/chirality-piping
PY=$WT/rv120b3/${PYCOPY:-py}/projects/chirality-piping
B=$WT/targets/rv120b3-pybins/release
ENV="OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units PYTHONDONTWRITEBYTECODE=1"
env RV120_IN=$IN RV120_OUT=$B3/probes/${label}_rs.jsonl $J cargo ${label}_rs $P/core/reporting/result_export $WT/targets/rv120b3-${PROBECOPY:-probe} test --locked --offline --test rv120_b3_raw; echo "${label}_rs rc=$?"
$J slot ${label}_ts $P/apps/desktop /usr/bin/env RV120_IN=$IN RV120_OUT=$B3/probes/${label}_ts.jsonl $P/node_modules/.bin/vitest run src/features/results/rv120B3Raw.test.ts; echo "${label}_ts rc=$?"
rm -rf $P/apps/desktop/node_modules/.vite
$J slot ${label}_py $PY /usr/bin/env $ENV $WT/venv/bin/python $S/tools/b3/rv120_b3_py_raw.py $PY $IN $B3/probes/${label}_py.jsonl; echo "${label}_py rc=$?"
echo "probes-$label-done"
