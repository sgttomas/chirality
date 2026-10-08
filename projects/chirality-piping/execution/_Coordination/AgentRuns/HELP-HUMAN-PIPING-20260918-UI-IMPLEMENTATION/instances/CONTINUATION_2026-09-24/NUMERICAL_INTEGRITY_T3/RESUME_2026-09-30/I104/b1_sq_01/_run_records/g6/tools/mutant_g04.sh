#!/bin/bash
# I104 SQ (RV112 N-2): RV112's mutant G04 (the reader folds the first parked slot only) on a copy of the
# registered scratch copy; the old two-case test and the new C = 3 test, run against it.
set -uo pipefail
T=WT; S=$T/scratch/i104_b1_sq; M=$S/mutcopy; LOG=$S/logs/mutant_g04.log; : > $LOG
rm -rf $M; cp -R $S/regcopy $M
F=$M/projects/chirality-piping/core/product_physics/src/retained_memory.rs
$T/venv/bin/python - $F <<'PY' >> $LOG
import sys
p = sys.argv[1]; t = open(p).read()
old = "capture.parked_cases().iter().fold(own,"
assert t.count(old) == 1
open(p, "w").write(t.replace(old, "capture.parked_cases().iter().take(1).fold(own,"))
print("G04 applied: parked_cases().iter().take(1)")
PY
cd $M/projects/chirality-piping/core/product_physics
export TMPDIR=$S/tmp CARGO_BUILD_JOBS=8
$T/tools/t3_cargo.sh test --locked --offline --lib --target-dir $T/targets/i104-sq-mut -- retained_error_text --test-threads=1 >> $LOG 2>&1
echo "MUTANT-RUN exit $?" >> $LOG
