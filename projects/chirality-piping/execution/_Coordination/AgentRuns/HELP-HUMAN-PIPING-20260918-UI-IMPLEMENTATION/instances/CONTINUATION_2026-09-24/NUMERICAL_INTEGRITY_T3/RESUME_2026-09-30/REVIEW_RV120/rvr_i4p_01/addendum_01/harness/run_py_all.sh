#!/bin/bash
# RV120: PY's confirmation, every heavy job one at a time: the authority binaries and PY at I4 (run_py_i4.sh); PY's head
# census, probes and the three retained test files at I4 and head (run_py_chain.sh); the I100-note probes on RS, TS
# and PY heads; then the PY mutants (control, P31, P35, P36, Q01-Q05).
WT=WT
S=$WT/scratch/rv120_rvr
J=$S/tools/rv120_job.sh
$S/tools/run_py_i4.sh
$S/tools/run_py_chain.sh
REL=projects/chirality-piping/core/reporting/result_export
D=$WT/targets/rv120-rs-head/debug/deps; RSB=$D/$(ls $D | grep -E '^rv113_census-[0-9a-f]+$' | head -1)
for f in arrays span_safe span_2p53 span_2p60; do
  $J slot rsx_$f $S/copies/rs-head/$REL /usr/bin/env RV113_PROBES=$S/probes/x/probes_x_$f.json RV113_PROBES_OUT=$S/probes/x/rs_head_$f.jsonl RUST_TEST_THREADS=2 "$RSB" rv113_probes --exact; echo "rsx_$f rc=$?"
done
DT=$S/copies/ts-head/projects/chirality-piping/apps/desktop
$J slot tsx_all $DT /usr/bin/env RV113_PROBES=$S/probes/x/probes_x_all.json RV113_PROBES_OUT=$S/probes/x/ts_head_all.jsonl $S/copies/ts-head/projects/chirality-piping/node_modules/.bin/vitest run src/features/results/rv113Census.test.ts; echo "tsx_all rc=$?"
rm -rf $DT/node_modules/.vite
B=$WT/targets/rv120-pybins/release
ENV="OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units PYTHONDONTWRITEBYTECODE=1"
P=$S/copies/py-head/projects/chirality-piping
$J slot pyx_all $P /usr/bin/env $ENV $WT/venv/bin/python $S/tools/rv113_py_harness.py $P probes $S/probes/x/probes_x_all.json $S/probes/x/py_head_all.jsonl; echo "pyx_all rc=$?"
$S/tools/run_py_mutants.sh NONE P31 P35 P36 Q01 Q02 Q03 Q04 Q05
echo py-all-done
