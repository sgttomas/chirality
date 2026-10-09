#!/bin/bash
# I105 J0b: the evidence chain at the merged head (h) and #1168's head (u), one heavy job at a time. b2's own side
# (e582b61f9e) is J0a's evidence (PP at e582b61f9e; the other suites and the census at 9f5cfbcd75, which differs only in
# PP's s11f test file).
WT=WT
S=$WT/scratch/i105_j0b
H=$1
echo "# chain start $(date -u '+%FT%TZ') h=$H"
$S/bin/copy.sh $H pyh_src && $S/bin/py_helpers.sh pyh_src; echo "# helpers rc=$?"
for x in "h $H" "u 37724dea27"; do set -- $x
  $S/bin/head_chain.sh $1 $2; echo "# head $1 rc=$?"
done
echo "# chain end $(date -u '+%FT%TZ')"
