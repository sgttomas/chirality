#!/bin/bash
# I100 B3 repair 01: the guarded mutants (control, R1-R5) on the B3 module, in a fresh copy of <commit>, one at a time.
source WT/scratch/i100_b3r/tools/env.sh
C=$1; M=$S/rep1/mut2
mkdir -p $M && git -C $WT/b2-p archive $C projects/chirality-piping/core projects/chirality-piping/fixtures projects/chirality-piping/schemas projects/chirality-piping/tests | tar -x -C $M
$VENV/bin/python $S/tools/rep1_mutants.py $M/projects/chirality-piping
P=$M/projects/chirality-piping
for id in NONE R1 R2 R3 R4 R5; do
  O=$S/rep1/mutants2/runs/$id; mkdir -p $O; MUT=$id; [ "$id" = NONE ] && MUT=
  $S/tools/job.sh slot rep1_mut2_$id $P /usr/bin/env I100_MUT=$MUT $VENV/bin/python -m pytest -p no:cacheprovider --basetemp=$S/tmp/rep1_mut2_$id/basetemp -q -rf --junitxml=$O/junit.xml tests/test_retained_precision_b3.py > $O/pytest.log 2>&1
  echo "mutant $id rc=$?"
done
for m in NONE R2 R3 R4 R5; do echo "== $m"; $VENV/bin/python $S/tools/rep1_trace.py $P $S/rep1/inputs/forge_eg.jsonl $m; done > $S/rep1/mutants2/FORGE_TRACE.txt 2>&1
echo "mut2 done"
