#!/bin/bash
# RV120 B3 ADDENDUM_02: (A) the B3a drop (b2 0ef9a8ace9) with (B) repair 02 applied as a patch (I101's b2-t
# 65c04cd0c7..d933514312 and b2-p 6d3d4cdca6..101ebcff76), the dry-merge equivalent, in copy m1; base m0 = b2 51f339a11e
# (PY's seven files; RE, vitest and the census at 51f339a11e equal my confirmed heads' runs). One heavy job at a time.
WT=WT
S=$WT/scratch/rv120_rvr
B3=$S/b3
export RV120_LOGDIR=$B3/logs
J=$S/tools/rv120_job.sh
B=$WT/targets/rv120b3-pybins/release
ENV="OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units PYTHONDONTWRITEBYTECODE=1"
N=$S/copies/sc-head/projects/chirality-piping/fixtures/results/retained_precision_cases.json
PYT="tests/test_retained_precision_contract.py tests/test_retained_precision_carriers.py tests/test_retained_precision_schema.py tests/test_load_reference_schema.py tests/test_load_reference_source_schema.py tests/test_source_block_schema_contract.py tests/test_retained_precision_b3.py"
P=$WT/rv120b3/m0/projects/chirality-piping; mkdir -p $B3/tmp/py_m0
$J slot m0_py_tests $P /usr/bin/env $ENV $WT/venv/bin/python -m pytest -p no:cacheprovider --basetemp=$B3/tmp/py_m0/basetemp -q -rf --junitxml=$B3/suites/py_m0.xml $PYT; echo "m0_py_tests rc=$?"
$S/tools/run_b3_ts.sh m1
P=$WT/rv120b3/m1/projects/chirality-piping
$J slot m1_py_census $P /usr/bin/env $ENV $WT/venv/bin/python $S/tools/rv113_py_harness.py $P census $B3/census/py_m1.jsonl; echo "m1_py_census rc=$?"
env RV120_CORPUS=$N RV113_OUT=$B3/census/rs_m1_07n.jsonl $J cargo n07_rs_m1 $P/core/reporting/result_export $WT/targets/rv120b3-m1 test --locked --offline --test rv120_census_env -- rv120_census_env --exact; echo "n07_rs_m1 rc=$?"
$J slot n07_ts_m1 $P/apps/desktop /usr/bin/env RV120_CORPUS=$N RV113_OUT=$B3/census/ts_m1_07n.jsonl $P/node_modules/.bin/vitest run src/features/results/rv120CensusEnv.test.ts -t "rv120 census env"; echo "n07_ts_m1 rc=$?"
rm -rf $P/apps/desktop/node_modules/.vite
$J slot n07_py_m1 $P /usr/bin/env $ENV RV120_CORPUS=$N $WT/venv/bin/python $S/tools/b3/rv120_py_harness_env.py $P census $B3/census/py_m1_07n.jsonl; echo "n07_py_m1 rc=$?"
python3 - "$B3" <<'PY'
import json, sys
b3 = sys.argv[1]
with open(f"{b3}/inputs/i101_m1.jsonl", "w") as f:
    for l in open(f"{b3}/shapes/rs_m1_inputs.jsonl"):
        d = json.loads(l); w = d["expected_bound"]
        f.write(json.dumps({"name": d["name"] + " [" + d["base"] + "]", "want": (w["gate"] + " " + w["code"]) if w else "eligible", "source": d["source"], "invocation": d["invocation"]}) + "\n")
PY
for spec in "a2probes $B3/probes/b3_probes.jsonl" "a2forge $B3/inputs/forge_eg.jsonl" "a2s $B3/inputs/i101_m1.jsonl" "a2s52 $B3/inputs/i100_52.jsonl" "a2s318 $B3/inputs/i100_318.jsonl"; do
  set -- $spec; PROBECOPY=m1 PYCOPY=m1 $S/tools/b3/run_b3_probes2.sh $1 $2
done
for i in 1 2 3 4 5; do env RV120_IN=$B3/inputs/rs_det.jsonl RV120_OUT=$B3/probes/a2_rs_det_$i.jsonl $J cargo a2_rs_det_$i $P/core/reporting/result_export $WT/targets/rv120b3-m1 test --locked --offline --test rv120_b3_raw; echo "a2_rs_det_$i rc=$?"; done
echo a2-done
