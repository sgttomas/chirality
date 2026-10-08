#!/bin/bash
# RV120 B3 repair 01: the heavy jobs at the repaired heads, one at a time. TS head 65c04cd0c7 (copies ts2, probe2, mut2;
# RE src = RS head 81d41baebf); PY head 6d3d4cdca6 (py2).
WT=WT
S=$WT/scratch/rv120_rvr
B3=$S/b3
export RV120_LOGDIR=$B3/logs
J=$S/tools/rv120_job.sh
B=$WT/targets/rv120b3-pybins/release
ENV="OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units PYTHONDONTWRITEBYTECODE=1"
N=$S/copies/sc-head/projects/chirality-piping/fixtures/results/retained_precision_cases.json
PYT="tests/test_retained_precision_contract.py tests/test_retained_precision_carriers.py tests/test_retained_precision_schema.py tests/test_load_reference_schema.py tests/test_load_reference_source_schema.py tests/test_source_block_schema_contract.py"
# 1. TS head: RE suite (shape and input dumps), RS and TS census (07m), vitest, tsc, PY's schema files.
$S/tools/run_b3_ts.sh ts2
# 2. PY head: census (07m) and the seven files.
P=$WT/rv120b3/py2/projects/chirality-piping; mkdir -p $B3/tmp/py_py2
$J slot py2_census $P /usr/bin/env $ENV $WT/venv/bin/python $S/tools/rv113_py_harness.py $P census $B3/census/py_py2.jsonl; echo "py2_census rc=$?"
$J slot py2_tests $P /usr/bin/env $ENV $WT/venv/bin/python -m pytest -p no:cacheprovider --basetemp=$B3/tmp/py_py2/basetemp -q -rf --junitxml=$B3/suites/py_py2.xml $PYT tests/test_retained_precision_b3.py; echo "py2_tests rc=$?"
# 3. 07n census at the heads.
P=$WT/rv120b3/probe2/projects/chirality-piping
env RV120_CORPUS=$N RV113_OUT=$B3/census/rs_ts2_07n.jsonl $J cargo n07_rs_ts2 $P/core/reporting/result_export $WT/targets/rv120b3-probe2 test --locked --offline --test rv120_census_env -- rv120_census_env --exact; echo "n07_rs_ts2 rc=$?"
$J slot n07_ts_ts2 $P/apps/desktop /usr/bin/env RV120_CORPUS=$N RV113_OUT=$B3/census/ts_ts2_07n.jsonl $P/node_modules/.bin/vitest run src/features/results/rv120CensusEnv.test.ts -t "rv120 census env"; echo "n07_ts_ts2 rc=$?"
rm -rf $P/apps/desktop/node_modules/.vite
P=$WT/rv120b3/py2/projects/chirality-piping
$J slot n07_py_py2 $P /usr/bin/env $ENV RV120_CORPUS=$N $WT/venv/bin/python $S/tools/b3/rv120_py_harness_env.py $P census $B3/census/py_py2_07n.jsonl; echo "n07_py_py2 rc=$?"
# 4. Three-reader raw readings at the heads.
python3 - "$B3" <<'PY'
import json, sys
b3 = sys.argv[1]
with open(f"{b3}/inputs/i101_169.jsonl", "w") as f:
    for l in open(f"{b3}/shapes/rs_ts2_inputs.jsonl"):
        d = json.loads(l); w = d["expected_bound"]
        f.write(json.dumps({"name": d["name"] + " [" + d["base"] + "]", "want": (w["gate"] + " " + w["code"]) if w else "eligible", "source": d["source"], "invocation": d["invocation"]}) + "\n")
PY
for spec in "r1probes $B3/probes/b3_probes.jsonl" "r1forge $B3/inputs/forge_eg.jsonl" "r1s169 $B3/inputs/i101_169.jsonl" "r1s52 $B3/inputs/i100_52.jsonl" "r1s318 $B3/inputs/i100_318.jsonl"; do
  set -- $spec; PROBECOPY=probe2 PYCOPY=py2 $S/tools/b3/run_b3_probes2.sh $1 $2
done
# 5. I101's B28 and B29 against the repaired RS and TS tests (mut2 = the TS head).
P=$WT/rv120b3/mut2/projects/chirality-piping; O=$WT/rv120b3/mut2.orig/projects/chirality-piping
for m in B28 B29; do
  python3 $S/tools/b3/mutate_b3.py $P $O $m apply
  $J cargo mut2_${m}_rs $P/core/reporting/result_export $WT/targets/rv120b3-mut test --locked --offline --test retained_precision_contract; echo "mut2_${m}_rs rc=$?"
  $J slot mut2_${m}_ts $P/apps/desktop $P/node_modules/.bin/vitest run --reporter=dot --reporter=json --outputFile.json=$B3/suites/mut2_${m}_ts.json src/features/results/retainedPrecision.test.ts; echo "mut2_${m}_ts rc=$?"
  rm -rf $P/apps/desktop/node_modules/.vite
  python3 $S/tools/b3/mutate_b3.py $P $O $m revert
done
cmp $P/core/reporting/result_export/src/retained_precision.rs $O/core/reporting/result_export/src/retained_precision.rs && cmp $P/apps/desktop/src/features/results/retainedPrecision.ts $O/apps/desktop/src/features/results/retainedPrecision.ts && echo reverted
echo r1-done
