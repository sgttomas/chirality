#!/bin/bash
# I100 B3: one pytest run as one T3 slot job. Usage: pyt.sh <label> <P root> <pytest args...>
set -u
source WT/scratch/i100_b3r/tools/env.sh
L=$1; PR=$2; shift 2; O=$S/runs/$L; mkdir -p $O
$S/tools/job.sh slot pyt_$L $PR /bin/bash -c "$VENV/bin/python -m pytest -p no:cacheprovider --basetemp=$S/tmp/pyt_$L/basetemp -q -rf --junitxml=$O/junit.xml $* > $O/pytest.log 2>&1"
echo "pyt $L rc=$?"; tail -3 $O/pytest.log
