#!/bin/bash
# I105 J0a: the evidence chain at the merged head (h), b2's start head (b) and main (m), one heavy job at a time.
WT=WT
S=$WT/scratch/i105_j0a
echo "# chain start $(date -u '+%FT%TZ')"
$S/bin/copy.sh 9f5cfbcd75 pyh_src && $S/bin/py_helpers.sh pyh_src; echo "# helpers rc=$?"
for x in "h 9f5cfbcd75" "b 7cc786285c" "m ec5d397359"; do set -- $x
  $S/bin/head_chain.sh $1 $2; echo "# head $1 rc=$?"
done
echo "# chain end $(date -u '+%FT%TZ')"
