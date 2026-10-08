#!/bin/bash
# I100 B3: build a light P tree (core, fixtures, schemas) from a lane commit's archive, with 07m (as committed) or
# 07n (from git, ea113e7b...), and run the PY census over it. Usage: census_head.sh <label> <commit> 07m|07n
set -u
source WT/scratch/i100_b3r/tools/env.sh
L=$1; C=$2; K=$3; T=$S/trees/$L; rm -rf $T; mkdir -p $T
git -C $WT/b2-p archive $C projects/chirality-piping/core projects/chirality-piping/fixtures projects/chirality-piping/schemas | tar -x -C $T
PR=$T/projects/chirality-piping
[ "$K" = 07n ] && cp $S/inputs/c07n.json $PR/fixtures/results/retained_precision_cases.json
$S/tools/census.sh $L $PR
