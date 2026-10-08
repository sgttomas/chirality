#!/bin/bash
# RV120 B3: RV113's three harnesses (corpus from RV120_CORPUS; otherwise unchanged) over 07n at the base (e67c364680)
# and the heads (RS/TS: the probe copy of 77aaaa61d1; PY: b7721d27e9), one heavy job at a time.
WT=WT
S=$WT/scratch/rv120_rvr
B3=$S/b3
export RV120_LOGDIR=$B3/logs
J=$S/tools/rv120_job.sh
N=$S/copies/sc-head/projects/chirality-piping/fixtures/results/retained_precision_cases.json
B=$WT/targets/rv120b3-pybins/release
ENV="OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units PYTHONDONTWRITEBYTECODE=1"
for spec in "base base" "probe ts"; do
  set -- $spec; P=$WT/rv120b3/$1/projects/chirality-piping
  env RV120_CORPUS=$N RV113_OUT=$B3/census/rs_${2}_07n.jsonl $J cargo n07_rs_$2 $P/core/reporting/result_export $WT/targets/rv120b3-$1 test --locked --offline --test rv120_census_env -- rv120_census_env --exact; echo "n07_rs_$2 rc=$?"
  $J slot n07_ts_$2 $P/apps/desktop /usr/bin/env RV120_CORPUS=$N RV113_OUT=$B3/census/ts_${2}_07n.jsonl $P/node_modules/.bin/vitest run src/features/results/rv120CensusEnv.test.ts -t "rv120 census env"; echo "n07_ts_$2 rc=$?"
  rm -rf $P/apps/desktop/node_modules/.vite
done
for c in base py; do P=$WT/rv120b3/$c/projects/chirality-piping
  $J slot n07_py_$c $P /usr/bin/env $ENV RV120_CORPUS=$N $WT/venv/bin/python $S/tools/b3/rv120_py_harness_env.py $P census $B3/census/py_${c}_07n.jsonl; echo "n07_py_$c rc=$?"
done
echo n07-done
