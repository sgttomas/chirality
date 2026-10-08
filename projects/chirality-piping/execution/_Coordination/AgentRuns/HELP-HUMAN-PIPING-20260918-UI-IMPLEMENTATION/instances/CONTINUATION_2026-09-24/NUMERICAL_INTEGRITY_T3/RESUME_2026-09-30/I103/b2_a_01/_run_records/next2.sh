#!/bin/bash
# I103: B3a-A + B2-A head (78c7cbba9b): PP and runner suites. One heavy job at a time.
S=WT/scratch/i103_b2_a
$S/bin/run_suites.sh $S/b2a b2a pp runner
echo "NEXT2-DONE" >> $S/runs/b2a/meta.txt
