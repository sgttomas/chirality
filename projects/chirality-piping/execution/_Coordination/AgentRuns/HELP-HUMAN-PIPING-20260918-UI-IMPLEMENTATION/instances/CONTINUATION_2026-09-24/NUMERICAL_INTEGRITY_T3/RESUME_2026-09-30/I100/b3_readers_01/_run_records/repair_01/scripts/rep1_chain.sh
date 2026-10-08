#!/bin/bash
# I100 B3 repair 01: one heavy job at a time, at the repaired head <commit>: the 07m and 07n censuses; the suites; the
# guarded mutants (control, R1-R3) on the B3 module; PY's raw readings of RV120's inputs (its 128 probes, its 4
# forgeries, and I101's 165, I100's 52 and 318 shapes) with RV120's own runner. Usage: rep1_chain.sh <commit>
source WT/scratch/i100_b3r/tools/env.sh
C=$1; H=$S/head6; M=$S/rep1/mut
mkdir -p $H $M && git -C $WT/b2-p archive $C projects/chirality-piping | tar -x -C $H
git -C $WT/b2-p archive $C projects/chirality-piping/core projects/chirality-piping/fixtures projects/chirality-piping/schemas projects/chirality-piping/tests | tar -x -C $M
$VENV/bin/python $S/tools/rep1_mutants.py $M/projects/chirality-piping
for a in "c_rep1 $C 07m" "c_rep107n $C 07n"; do $S/tools/census_head.sh $a; done
EXTRA=tests/test_retained_precision_b3.py $S/tools/suites.sh rep1 $H/projects/chirality-piping
P=$M/projects/chirality-piping
for id in NONE R1 R2 R3; do
  O=$S/rep1/mutants/runs/$id; mkdir -p $O; MUT=$id; [ "$id" = NONE ] && MUT=
  $S/tools/job.sh slot rep1_mut_$id $P /usr/bin/env I100_MUT=$MUT $VENV/bin/python -m pytest -p no:cacheprovider --basetemp=$S/tmp/rep1_mut_$id/basetemp -q -rf --junitxml=$O/junit.xml tests/test_retained_precision_b3.py > $O/pytest.log 2>&1
  echo "mutant $id rc=$?"
done
mkdir -p $S/rep1/agree
for x in "probes b3_probes" "forge forge_eg" "s52 i100_52" "s165 i101_165" "s318 i100_318"; do
  set -- $x
  $S/tools/job.sh slot rep1_py_$1 $S $VENV/bin/python $S/tools/rv120_b3_py_raw.py $H/projects/chirality-piping $S/rep1/inputs/$2.jsonl $S/rep1/agree/$1_py.jsonl
  echo "py $1 rc=$?"
done
echo "rep1 chain done"
