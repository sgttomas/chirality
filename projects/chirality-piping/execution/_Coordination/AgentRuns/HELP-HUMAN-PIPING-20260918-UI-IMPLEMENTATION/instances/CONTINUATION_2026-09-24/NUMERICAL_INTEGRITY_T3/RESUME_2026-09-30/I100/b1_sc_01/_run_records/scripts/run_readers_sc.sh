#!/bin/bash
# I100: the three readers over the corpus now in M's fixtures (RV113's census harnesses), one heavy job at a time:
# PY (slot), RS (one cargo job: build and run the census test), TS (slot, vitest). Usage: run_readers.sh <label> [py|rs|ts ...]
set -u
source WT/scratch/i100_b1_sc/tools/env_sc.sh
LABEL=$1; shift; WHICH=${*:-py rs ts}; O=$S/runs/$LABEL; mkdir -p $O
shasum -a 256 $P/fixtures/results/retained_precision_cases.json > $O/corpus.sha256
for r in $WHICH; do case $r in
 py) $S/tools/job.sh slot ${LABEL}_py $S $VENV/bin/python $S/tools/rv113_py_harness_cls.py $P census $O/py.jsonl; echo "py rc=$?";;
 rs) export RV113_OUT=$O/rs.jsonl; $S/tools/job.sh cargo ${LABEL}_rs $P/core/reporting/result_export $WT/targets/i100-b1-sc/rs test --locked --offline --test rv113_census rv113_census -- --exact; echo "rs rc=$?"; unset RV113_OUT;;
 ts) $S/tools/job.sh slot ${LABEL}_ts $P/apps/desktop /usr/bin/env RV113_OUT=$O/ts.jsonl $NMS/.bin/vitest run src/features/results/rv113Census.test.ts; echo "ts rc=$?"; rm -rf $P/apps/desktop/node_modules/.vite;;
esac; done
