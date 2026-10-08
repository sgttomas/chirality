#!/bin/bash
# I106 SG: compare an extracted archive copy with the commit's blobs (git hash-object without -w).
# Usage: verify_tree.sh <commit> <tree dir> ; prints differing / extra / missing paths and the blob count.
c=$1; d=$2; NUM=NUM
export GIT_OPTIONAL_LOCKS=0
cd $NUM
git ls-tree -r $c projects/chirality-piping/core projects/chirality-piping/fixtures projects/chirality-piping/schemas | awk '{print $3"\t"$4}' | sort -k2 > $d.lstree
n=$(wc -l < $d.lstree | tr -d ' ')
( cd $d && find projects -type f | sort ) > $d.files
cut -f2 $d.lstree > $d.gitfiles
echo "commit $(git rev-parse $c): blobs $n"
comm -13 $d.gitfiles $d.files | sed 's/^/EXTRA /'
comm -23 $d.gitfiles $d.files | sed 's/^/MISSING /'
cut -f2 $d.lstree | (cd $d && git hash-object --stdin-paths --no-filters) > $d.hashes
paste $d.lstree $d.hashes | awk -F'\t' '$1!=$3 {print "DIFFERS "$2}'
