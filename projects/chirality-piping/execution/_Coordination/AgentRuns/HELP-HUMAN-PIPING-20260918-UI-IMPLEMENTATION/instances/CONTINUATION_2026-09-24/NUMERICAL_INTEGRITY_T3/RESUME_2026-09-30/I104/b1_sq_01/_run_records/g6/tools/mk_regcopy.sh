#!/bin/bash
# I104 SQ G6: a scratch copy of b1-q's committed head (projects/chirality-piping without execution/)
# with registration.diff applied. Usage: mk_regcopy.sh <rev>
set -euo pipefail
T=WT; S=$T/scratch/i104_b1_sq; REV=$1; C=$S/regcopy
rm -rf $C; mkdir -p $C
GIT_OPTIONAL_LOCKS=0 git -C $T/b1-q archive $REV -- projects/chirality-piping ':(exclude)projects/chirality-piping/execution' | tar -x -C $C
cd $C && git apply --unsafe-paths -v $S/reg/registration.diff
grep -n "threshold_bytes: 11_274_289_152" $C/projects/chirality-piping/core/product_physics/src/retained_memory.rs
echo "REGCOPY rev=$REV"
