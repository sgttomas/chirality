#!/bin/bash
# RV113: archive copies for confirming SR-PY repair 02 (2843a59a16): the head, and the head for mutants. The tree
# without execution/, plus PKG-15's execution folder (a retained test reads it); the copies' files against `git show`.
# (Recorded as run, one command, in the reviewer's session; written out here as a script for the record.)
WT=WT; S=$WT/scratch/rv113_rvr_01
mkdir -p $S/pyr2/{static,logs,tmp,probes,census,suites,mutants}
for c in py2-head py2-mut; do mkdir -p $WT/rv113/$c
  (cd $WT/b1-p && GIT_OPTIONAL_LOCKS=0 git archive --format=tar 2843a59a16fabb76a8e55cabdb2133b0a3c0ec5f -- projects/chirality-piping ':(exclude)projects/chirality-piping/execution') | tar -x -C $WT/rv113/$c
  (cd $WT/b1-p && GIT_OPTIONAL_LOCKS=0 git archive --format=tar 2843a59a16fabb76a8e55cabdb2133b0a3c0ec5f -- "projects/chirality-piping/execution/PKG-15_Handoff and External Prover Workflow") | tar -x -C $WT/rv113/$c
done
cd $WT/b1-p
for f in core/analysis_runs/retained_precision.py core/analysis_runs/compatibility.py core/analysis_runs/preview_physics_evidence.py tests/test_retained_precision_contract.py tests/test_retained_precision_carriers.py fixtures/results/retained_precision_cases.json; do
  echo "$(GIT_OPTIONAL_LOCKS=0 git show 2843a59a16:projects/chirality-piping/$f | shasum -a 256 | cut -c1-64) $(shasum -a 256 $WT/rv113/py2-head/projects/chirality-piping/$f | cut -c1-64) $f"
done > $S/pyr2/static/copies.txt
GIT_OPTIONAL_LOCKS=0 git diff --name-only 11cc14e3e6 2843a59a16 >> $S/pyr2/static/copies.txt
