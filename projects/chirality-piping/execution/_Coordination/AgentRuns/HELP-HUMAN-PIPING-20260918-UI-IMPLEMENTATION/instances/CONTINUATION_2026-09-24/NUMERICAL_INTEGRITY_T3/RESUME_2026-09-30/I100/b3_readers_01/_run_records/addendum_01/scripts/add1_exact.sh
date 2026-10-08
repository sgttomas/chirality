#!/bin/bash
# I100 B3 addendum 01: the exact-route shapes (x08, p02 and the bases, on m3x and m3xp, both modes) through the three
# readers in RV113's census mode, the archive's corpus replaced by add1_exact_corpus.py (bases are read raw, so the
# exact route's preparation hash stands). One heavy job at a time. Env ARCH, TGT (RS target name).
# Usage: add1_exact.sh <label>
set -u
source WT/scratch/i100_b3r/tools/env.sh
L=$1; P=$ARCH/projects/chirality-piping; O=$S/add1/runs/$L; mkdir -p $O
NMS=$WT/sweep-skewpin/projects/chirality-piping/node_modules
shasum -a 256 $P/fixtures/results/retained_precision_cases.json > $O/corpus.sha256
$S/tools/job.sh slot add1_${L}_py $S $VENV/bin/python $S/tools/rv113_py_harness.py $P census $O/py.jsonl; echo "py rc=$?"
export RV113_OUT=$O/rs.jsonl
$S/tools/job.sh cargo add1_${L}_rs $P/core/reporting/result_export $WT/targets/$TGT test --locked --offline --test rv113_census rv113_census -- --exact
echo "rs rc=$?"; unset RV113_OUT
cmp $P/package-lock.json $NMS/../package-lock.json || { echo "package-lock differs"; exit 5; }
ln -s $NMS $P/node_modules
for d in self-weight-engine wasm-engine; do mkdir -p $P/apps/desktop/public/$d; cp $WT/sweep-skewpin/projects/chirality-piping/apps/desktop/public/$d/* $P/apps/desktop/public/$d/; done
$S/tools/job.sh slot add1_${L}_ts $P/apps/desktop /usr/bin/env RV113_OUT=$O/ts.jsonl $NMS/.bin/vitest run src/features/results/rv113Census.test.ts; echo "ts rc=$?"
rm $P/node_modules; rm -rf $P/apps/desktop/node_modules/.vite
