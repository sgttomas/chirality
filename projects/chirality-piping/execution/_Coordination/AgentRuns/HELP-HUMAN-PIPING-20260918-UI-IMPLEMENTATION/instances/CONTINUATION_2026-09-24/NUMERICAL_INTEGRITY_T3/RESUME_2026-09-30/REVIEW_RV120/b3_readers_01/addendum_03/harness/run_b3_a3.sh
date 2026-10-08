#!/bin/bash
# RV120 B3 ADDENDUM_03: (A) b2 0ef9a8ace9 with (B) repairs 02 and 03 applied as patches (I101's b2-t
# 65c04cd0c7..dc6b7359ba and b2-p 6d3d4cdca6..27c45da2ba), the dry-merge equivalent, in copy m2; the base
# is ADDENDUM_02's (m0 for PY; my confirmed heads' runs for RE, vitest and the census). One heavy job at a time.
WT=WT
S=$WT/scratch/rv120_rvr
B3=$S/b3
export RV120_LOGDIR=$B3/logs
J=$S/tools/rv120_job.sh
B=$WT/targets/rv120b3-pybins/release
ENV="OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units PYTHONDONTWRITEBYTECODE=1"
N=$S/copies/sc-head/projects/chirality-piping/fixtures/results/retained_precision_cases.json
PYT="tests/test_retained_precision_contract.py tests/test_retained_precision_carriers.py tests/test_retained_precision_schema.py tests/test_load_reference_schema.py tests/test_load_reference_source_schema.py tests/test_source_block_schema_contract.py tests/test_retained_precision_b3.py"
$S/tools/run_b3_ts.sh m2
P=$WT/rv120b3/m2/projects/chirality-piping
$J slot m2_py_census $P /usr/bin/env $ENV $WT/venv/bin/python $S/tools/rv113_py_harness.py $P census $B3/census/py_m2.jsonl; echo "m2_py_census rc=$?"
env RV120_CORPUS=$N RV113_OUT=$B3/census/rs_m2_07n.jsonl $J cargo n07_rs_m2 $P/core/reporting/result_export $WT/targets/rv120b3-m2 test --locked --offline --test rv120_census_env -- rv120_census_env --exact; echo "n07_rs_m2 rc=$?"
$J slot n07_ts_m2 $P/apps/desktop /usr/bin/env RV120_CORPUS=$N RV113_OUT=$B3/census/ts_m2_07n.jsonl $P/node_modules/.bin/vitest run src/features/results/rv120CensusEnv.test.ts -t "rv120 census env"; echo "n07_ts_m2 rc=$?"
rm -rf $P/apps/desktop/node_modules/.vite
$J slot n07_py_m2 $P /usr/bin/env $ENV RV120_CORPUS=$N $WT/venv/bin/python $S/tools/b3/rv120_py_harness_env.py $P census $B3/census/py_m2_07n.jsonl; echo "n07_py_m2 rc=$?"
python3 - "$B3" <<'PY'
import json, sys
b3 = sys.argv[1]
with open(f"{b3}/inputs/i101_m2.jsonl", "w") as f:
    for l in open(f"{b3}/shapes/rs_m2_inputs.jsonl"):
        d = json.loads(l); w = d["expected_bound"]
        f.write(json.dumps({"name": d["name"] + " [" + d["base"] + "]", "want": (w["gate"] + " " + w["code"]) if w else "eligible", "source": d["source"], "invocation": d["invocation"]}) + "\n")
PY
for spec in "a3probes $B3/probes/b3_probes.jsonl" "a3forge $B3/inputs/forge_eg.jsonl" "a3s $B3/inputs/i101_m2.jsonl" "a3s52 $B3/inputs/i100_52.jsonl" "a3s318 $B3/inputs/i100_318.jsonl"; do
  set -- $spec; PROBECOPY=m2 PYCOPY=m2 $S/tools/b3/run_b3_probes2.sh $1 $2
done
for i in 1 2 3 4 5; do env RV120_IN=$B3/inputs/rs_det.jsonl RV120_OUT=$B3/probes/a3_rs_det_$i.jsonl $J cargo a3_rs_det_$i $P/core/reporting/result_export $WT/targets/rv120b3-m2 test --locked --offline --test rv120_b3_raw; echo "a3_rs_det_$i rc=$?"; done
# Hash-order independence, broadly: every input above in one file; RS twice more (fresh processes) and PY under two
# fixed PYTHONHASHSEEDs; compared with the runs above.
cat $B3/probes/b3_probes.jsonl $B3/inputs/forge_eg.jsonl $B3/inputs/i101_m2.jsonl $B3/inputs/i100_52.jsonl $B3/inputs/i100_318.jsonl > $B3/inputs/all_m2.jsonl
for i in 1 2; do env RV120_IN=$B3/inputs/all_m2.jsonl RV120_OUT=$B3/probes/a3all_rs_$i.jsonl $J cargo a3all_rs_$i $P/core/reporting/result_export $WT/targets/rv120b3-m2 test --locked --offline --test rv120_b3_raw; echo "a3all_rs_$i rc=$?"; done
for seed in 1 2; do $J slot a3all_py_$seed $P /usr/bin/env $ENV PYTHONHASHSEED=$seed $WT/venv/bin/python $S/tools/b3/rv120_b3_py_raw.py $P $B3/inputs/all_m2.jsonl $B3/probes/a3all_py_$seed.jsonl; echo "a3all_py_$seed rc=$?"; done
echo a3-done
