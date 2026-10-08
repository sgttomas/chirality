#!/bin/bash
# I101 repair 01: B28 and B29, with a control, at the repair heads (RV120's forgeries pinned). One heavy job at a time.
# Usage: mutants_repair1.sh <rs commit> <ts commit>
WT=WT
S=$WT/scratch/i101_b3r
O=$S/out/mutants; mkdir -p $O
$S/harness/make_copy.sh b2-r "$1" mut_r4 s > $O/copy_r4.txt && $S/harness/make_copy.sh b2-t "$2" mut_t4 s > $O/copy_t4.txt || { echo "copies failed"; exit 1; }
rm -f $O/repair1_rs.jsonl $O/repair1_ts.jsonl
/usr/bin/python3 -I $S/harness/mutate.py rs mut_r4 $S/mutants/rs_mutants.py $O/repair1_rs.jsonl control B28 B29; echo "rs rc=$?"
/usr/bin/python3 -I $S/harness/mutate.py ts mut_t4 $S/mutants/ts_mutants.py $O/repair1_ts.jsonl control B28 B29; echo "ts rc=$?"
