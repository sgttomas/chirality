#!/bin/bash
# I103 repair 01: PP and runner suites at the new head (fresh targets, tag r1), then the repairs' mutants.
S=WT/scratch/i103_b2_a
$S/bin/run_suites.sh $S/r1 r1 pp runner
WT/venv/bin/python -I $S/bin/repair_mutants.py $S/r1mut_old $S/r1mut_new $S/runs/r1mut > $S/runs/r1mut_driver.log 2>&1
echo "mutants rc=$? $(date -u +%FT%TZ)" >> $S/runs/r1/meta.txt
echo "NEXT4-DONE" >> $S/runs/r1/meta.txt
