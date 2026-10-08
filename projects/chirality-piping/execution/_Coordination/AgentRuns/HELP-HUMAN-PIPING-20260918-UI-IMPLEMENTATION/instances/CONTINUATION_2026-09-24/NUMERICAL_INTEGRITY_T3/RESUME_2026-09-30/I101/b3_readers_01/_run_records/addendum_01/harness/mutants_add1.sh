#!/bin/bash
# I101 addendum 01: the sourced-case clause mutants (with a control) at the new heads, and B3's five survivors rerun there
# (shapes 23b and 25b added). One heavy job at a time. Usage: mutants_add1.sh <rs commit> <ts commit>
WT=WT
S=$WT/scratch/i101_b3r
O=$S/out/mutants; mkdir -p $O
$S/harness/make_copy.sh b2-r "$1" mut_r3 s > $O/copy_r3.txt && $S/harness/make_copy.sh b2-t "$2" mut_t3 s > $O/copy_t3.txt || { echo "copies failed"; exit 1; }
rm -f $O/add1_rs.jsonl $O/add1_ts.jsonl $O/survivors_rs.jsonl $O/survivors_ts.jsonl
/usr/bin/python3 -I $S/harness/mutate.py rs mut_r3 $S/mutants/add1_rs_mutants.py $O/add1_rs.jsonl; echo "add1 rs rc=$?"
/usr/bin/python3 -I $S/harness/mutate.py rs mut_r3 $S/mutants/rs_mutants.py $O/survivors_rs.jsonl B06b B25 B28 B29 B30; echo "survivors rs rc=$?"
/usr/bin/python3 -I $S/harness/mutate.py ts mut_t3 $S/mutants/add1_ts_mutants.py $O/add1_ts.jsonl; echo "add1 ts rc=$?"
/usr/bin/python3 -I $S/harness/mutate.py ts mut_t3 $S/mutants/ts_mutants.py $O/survivors_ts.jsonl B06b B25 B28 B29 B30; echo "survivors ts rc=$?"
