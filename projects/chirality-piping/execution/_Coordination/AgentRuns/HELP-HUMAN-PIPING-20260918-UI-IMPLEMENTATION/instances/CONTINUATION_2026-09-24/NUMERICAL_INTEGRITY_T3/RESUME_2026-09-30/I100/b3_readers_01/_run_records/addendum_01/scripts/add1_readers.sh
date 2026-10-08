#!/bin/bash
# I100 B3 addendum 01: the three readers on the probes, one heavy job at a time, in the scratch archive
# (WT/scratch/i100_b3r/add1/arch). PY: RV113's PY harness. RS: RV113's census test (rv113_probes), fresh target.
# TS: RV113's vitest harness, node_modules linked from WT/sweep-skewpin (package-lock compared), the wasm assets copied.
# Usage: add1_readers.sh <label> [py|rs|ts ...]
set -u
source WT/scratch/i100_b3r/tools/env.sh
L=$1; shift; WHICH=${*:-py rs ts}
A=${ARCH:-$S/add1/arch}; P=$A/projects/chirality-piping; O=$S/add1/runs/$L; mkdir -p $O
NMS=$WT/sweep-skewpin/projects/chirality-piping/node_modules
for r in $WHICH; do case $r in
 py) $S/tools/job.sh slot add1_${L}_py $S $VENV/bin/python $S/tools/rv113_py_harness.py $P probes $S/add1/probes.json $O/py.jsonl; echo "py rc=$?";;
 rs) export RV113_PROBES=$S/add1/probes.json RV113_PROBES_OUT=$O/rs.jsonl
     $S/tools/job.sh cargo add1_${L}_rs $P/core/reporting/result_export $WT/targets/i100-b3r-rs${TGSUF:-} test --locked --offline --test rv113_census rv113_probes -- --exact
     echo "rs rc=$?"; unset RV113_PROBES RV113_PROBES_OUT;;
 ts) cmp $P/package-lock.json $NMS/../package-lock.json || { echo "package-lock differs"; exit 5; }
     ln -s $NMS $P/node_modules
     for d in self-weight-engine wasm-engine; do mkdir -p $P/apps/desktop/public/$d; cp $WT/sweep-skewpin/projects/chirality-piping/apps/desktop/public/$d/* $P/apps/desktop/public/$d/; done
     (cd $P/apps/desktop/public && shasum -a 256 self-weight-engine/* wasm-engine/*) > $O/ts_wasm_assets.sha256
     $S/tools/job.sh slot add1_${L}_ts $P/apps/desktop /usr/bin/env RV113_PROBES=$S/add1/probes.json RV113_PROBES_OUT=$O/ts.jsonl $NMS/.bin/vitest run src/features/results/rv113Census.test.ts; echo "ts rc=$?"
     rm $P/node_modules; rm -rf $P/apps/desktop/node_modules/.vite;;
esac; done
