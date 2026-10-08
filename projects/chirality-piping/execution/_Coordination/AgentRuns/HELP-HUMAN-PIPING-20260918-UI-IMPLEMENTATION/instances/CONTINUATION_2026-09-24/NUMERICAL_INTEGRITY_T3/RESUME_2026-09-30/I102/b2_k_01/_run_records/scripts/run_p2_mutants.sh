#!/bin/bash
# Part 2 mutants against the committed Part 2 tree (f7494326f1) copied into scratch.
WT=WT; S=$WT/scratch/i102_b2_k; D=$S/mut_defs2
PY=$WT/venv/bin/python
export MUT_SRC=$S/p2_tree/projects/chirality-piping/core/solver/frame_kernel
for id in $(seq -f "p2m%02g" 1 35); do
  f=$($PY -I -c "import json;print(next(m['file'] for m in json.load(open('$D/index.json')) if m['id']=='$id'))")
  extra=""
  case $id in p2m10) extra="origins";; p2m19|p2m20|p2m21|p2m22|p2m23) extra="source_residual";; esac
  $PY -I $S/mutate.py $id $f $D/$id.old $D/$id.new b2k $extra
done
echo P2_MUTANTS_DONE
