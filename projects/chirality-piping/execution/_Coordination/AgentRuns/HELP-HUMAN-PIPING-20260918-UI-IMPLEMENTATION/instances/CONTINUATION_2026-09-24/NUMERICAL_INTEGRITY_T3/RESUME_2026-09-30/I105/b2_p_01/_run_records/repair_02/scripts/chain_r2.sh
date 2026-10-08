#!/bin/bash
# I105 RV123 round-2 repair: M2-03 on an archive of the repair head, then PP and the runner on archives of
# 72b3e5d9ea (base) and the repair head. One heavy job at a time. Usage: chain_r2.sh <head commit>
WT=WT
S=$WT/scratch/i105_b2_p
H=$1
export TMPDIR=$S/tmp
mkdir -p $S/r2mut $S/r2base $S/r2head
git -C $WT/b2 archive $H projects/chirality-piping | tar -x -C $S/r2mut
git -C $WT/b2 archive 72b3e5d9ea projects/chirality-piping | tar -x -C $S/r2base
git -C $WT/b2 archive $H projects/chirality-piping | tar -x -C $S/r2head
echo "CHAIN-STEP r2 archives $H $(date -u +%FT%TZ)" >> $S/runs/chain.log
python3 $S/bin/mutants.py $S/mut_spec/r2.json $S/r2mut $S/runs/mut_r2 > $S/runs/mut_r2_driver.log 2>&1
echo "CHAIN-STEP mut_r2 rc=$? $(date -u +%FT%TZ)" >> $S/runs/chain.log
$S/bin/run_suites.sh $S/r2base r2base pp runner
$S/bin/run_suites.sh $S/r2head r2head pp runner
echo "CHAIN-DONE r2 $(date -u +%FT%TZ)" >> $S/runs/chain.log
