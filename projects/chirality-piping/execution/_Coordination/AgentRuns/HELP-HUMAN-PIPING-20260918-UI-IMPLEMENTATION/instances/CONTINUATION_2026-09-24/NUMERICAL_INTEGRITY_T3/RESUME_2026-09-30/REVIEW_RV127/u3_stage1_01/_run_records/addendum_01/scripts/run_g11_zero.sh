#!/bin/bash
# RV127 addendum: the G11 zero-lateral probe at B and at the head (PP lib, debug).
set -u
WT=WT; S=$WT/scratch/rv127_u3; C=$WT/tools/t3_cargo.sh
export TMPDIR=$S/tmp
P=projects/chirality-piping/core/product_physics
cd $WT/rv127/base/$P && $C test --locked --offline --target-dir $WT/targets/rv127-base-pp --lib -- --nocapture rv127_probe_g11_zero_lateral > $S/ev/g11_zero_base.log 2>&1; echo "base rc=$?"
cd $WT/rv127/cand2/$P && $C test --locked --offline --target-dir $WT/targets/rv127-cand2-pp --lib -- --nocapture rv127_probe_g11_zero_lateral > $S/ev/g11_zero_cand.log 2>&1; echo "cand rc=$?"
