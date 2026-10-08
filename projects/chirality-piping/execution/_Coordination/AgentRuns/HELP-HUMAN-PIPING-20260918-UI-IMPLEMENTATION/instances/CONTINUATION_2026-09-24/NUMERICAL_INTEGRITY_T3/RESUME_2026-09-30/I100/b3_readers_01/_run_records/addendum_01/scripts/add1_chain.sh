#!/bin/bash
# I100 B3 addendum 01: one heavy job at a time. The three readers on the probes with the aligned RS and TS (I101's lane
# heads plus the two diffs) and PY at b7721d27e9; the 07m and 07n censuses at b7721d27e9; the suites there; the mutants.
source WT/scratch/i100_b3r/tools/env.sh
ARCH=$S/add1/arch2 TGSUF=-aligned $S/tools/add1_readers.sh aligned
for a in "c_add1 b7721d27e9 07m" "c_add107n b7721d27e9 07n"; do $S/tools/census_head.sh $a; done
EXTRA=tests/test_retained_precision_b3.py $S/tools/suites.sh add1 $S/head5/projects/chirality-piping
P=$S/add1/mut/projects/chirality-piping
for id in NONE C1 C2 C3; do
  O=$S/add1/mutants/runs/$id; mkdir -p $O; MUT=$id; [ "$id" = NONE ] && MUT=
  $S/tools/job.sh slot add1_mut_$id $P /usr/bin/env I100_MUT=$MUT $VENV/bin/python -m pytest -p no:cacheprovider --basetemp=$S/tmp/add1_mut_$id/basetemp -q -rf --junitxml=$O/junit.xml tests/test_retained_precision_b3.py > $O/pytest.log 2>&1
  echo "mutant $id rc=$?"
done
