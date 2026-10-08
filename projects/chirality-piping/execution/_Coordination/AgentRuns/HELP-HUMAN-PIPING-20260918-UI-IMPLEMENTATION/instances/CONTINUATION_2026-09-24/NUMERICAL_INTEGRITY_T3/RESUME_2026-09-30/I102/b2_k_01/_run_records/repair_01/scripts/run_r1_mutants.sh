#!/bin/bash
# Repair 01 mutants: each on a scratch copy of FK's committed tree, one cargo job at a time.
# At the repair head: filter b2k. At ef51a2d295 (before the repair): the whole lib.
WT=WT; S=$WT/scratch/i102_b2_k; D=$S/mut_defs_r1
PY=$WT/venv/bin/python; F=src/structural/retained/product_certificate/final_case.rs
for id in p2m29 m36 m18 mrk4; do
  MUT_SRC=$WT/b2-k/projects/chirality-piping/core/solver/frame_kernel $PY -I -B $S/mutate.py r1_head_$id $F $D/$id.old $D/$id.new b2k
done
MUT_SRC=$S/r1_ef51_tree/projects/chirality-piping/core/solver/frame_kernel $PY -I -B $S/mutate.py r1_ef51_mrk4 $F $D/mrk4.old $D/mrk4.new ""
echo R1_MUTANTS_DONE
