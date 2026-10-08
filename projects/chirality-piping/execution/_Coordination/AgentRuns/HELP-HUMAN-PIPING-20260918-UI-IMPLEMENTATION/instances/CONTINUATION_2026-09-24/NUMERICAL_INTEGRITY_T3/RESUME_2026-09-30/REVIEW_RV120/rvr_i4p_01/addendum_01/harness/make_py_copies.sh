#!/bin/bash
# RV120: PY archive copies (P without execution/, plus PKG-15's execution folder, which a retained test reads), as
# RV113 made them. Usage: make_py_copies.sh <label> <commit>   (e.g. py-i4 30f3d1b24a...)
set -e
export GIT_OPTIONAL_LOCKS=0
WT=WT
S=$WT/scratch/rv120_rvr
C=$S/copies/$1
rm -rf $C; mkdir -p $C
(cd $WT/b1-p && git archive --format=tar "$2" -- projects/chirality-piping ':(exclude)projects/chirality-piping/execution') | tar -x -C $C
(cd $WT/b1-p && git archive --format=tar "$2" -- "projects/chirality-piping/execution/PKG-15_Handoff and External Prover Workflow") | tar -x -C $C
cd $WT/b1-p
for f in core/analysis_runs/retained_precision.py core/analysis_runs/compatibility.py core/analysis_runs/preview_physics_evidence.py tests/test_retained_precision_contract.py tests/test_retained_precision_carriers.py tests/test_retained_precision_schema.py fixtures/results/retained_precision_cases.json; do
  echo "$(git show $2:projects/chirality-piping/$f | shasum -a 256 | cut -c1-64) $(shasum -a 256 $C/projects/chirality-piping/$f | cut -c1-64) $1 $f"
done >> $S/static/copies_py.txt
echo "$1 done"
