#!/bin/bash
# Part 1 mutants against the committed Part 1 tree (806424c6de) copied into scratch.
WT=WT; S=$WT/scratch/i102_b2_k; D=$S/mut_defs
PY=$WT/venv/bin/python
export MUT_SRC=$S/p1_tree/projects/chirality-piping/core/solver/frame_kernel
R=src/structural/retained
$PY -I $S/mutate.py p1m1 $R/product_certificate/final_case.rs $D/p1m1.old $D/p1m1.new product_certificate
$PY -I $S/mutate.py p1m2 $R/product_certificate.rs $D/p1m2.old $D/p1m2.new product_certificate
$PY -I $S/mutate.py p1m3 $R/product_certificate.rs $D/p1m3.old $D/p1m3.new product_certificate
$PY -I $S/mutate.py p1m4 $R/product_certificate.rs $D/p1m4.old $D/p1m4.new product_certificate
echo P1_MUTANTS_DONE
