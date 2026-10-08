#!/bin/bash
# I101: the mutants at the final heads, one heavy job at a time: RS (b2-r head), TS and PY's carrier schemas (b2-t head).
# Usage: mutants_final.sh <rs commit> <ts commit>
WT=WT
S=$WT/scratch/i101_b3r
O=$S/out/mutants; mkdir -p $O
$S/harness/make_copy.sh b2-r "$1" mut_r s > $O/copy_r.txt && $S/harness/make_copy.sh b2-t "$2" mut_t s > $O/copy_t.txt || { echo "copies failed"; exit 1; }
rm -f $O/rs.jsonl $O/ts.jsonl $O/py.jsonl
/usr/bin/python3 -I $S/harness/mutate.py rs mut_r $S/mutants/rs_mutants.py $O/rs.jsonl; echo "rs done rc=$?"
/usr/bin/python3 -I $S/harness/mutate.py ts mut_t $S/mutants/ts_mutants.py $O/ts.jsonl; echo "ts done rc=$?"
/usr/bin/python3 -I $S/harness/mutate.py py mut_t $S/mutants/py_mutants.py $O/py.jsonl; echo "py done rc=$?"
