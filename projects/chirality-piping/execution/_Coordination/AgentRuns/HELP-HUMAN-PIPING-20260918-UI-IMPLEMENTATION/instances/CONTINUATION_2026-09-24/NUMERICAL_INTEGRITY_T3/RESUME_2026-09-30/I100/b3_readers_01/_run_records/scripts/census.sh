#!/bin/bash
# I100 B3: the PY census over the corpus in a tree (RV113's harness, as I4''s m07m run). Usage: census.sh <label> <P root>
source WT/scratch/i100_b3r/tools/env.sh
L=$1; PR=$2; O=$S/runs/$L; mkdir -p $O
shasum -a 256 $PR/fixtures/results/retained_precision_cases.json > $O/corpus.sha256
$S/tools/job.sh slot census_$L $S $VENV/bin/python $S/tools/rv113_py_harness.py $PR census $O/py.jsonl; echo "py rc=$?"
