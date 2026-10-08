#!/bin/bash
# Batch 2 (one heavy job, sequential): the norm probe unmutated and under I102's p2m29; K-13 on the
# remaining modules (kf1_tracker, method, publication) at J2k and head; PP's profile test with
# --nocapture at main and head.
S=WT/scratch/rv121_rvk
$S/scripts/fk_filtered.sh rv fk-rv norm_rv rv121_norm_probe --nocapture --test-threads=1
$S/scripts/fk_filtered.sh rv2 fk-rv2 norm_rv2_p2m29 rv121_norm_probe --nocapture --test-threads=1
F="kf1_tracker_tests method_tests publication_tests"
$S/scripts/fk_filtered.sh p1x fk-p1x k13b_p1x $F --nocapture --test-threads=1
$S/scripts/fk_filtered.sh head fk-head k13b_head $F --nocapture --test-threads=1
for rev in main head; do
  export TMPDIR=$S/tmp CARGO_TARGET_DIR=WT/targets/rv121-$rev-core_product_physics
  ( cd $S/$rev/projects/chirality-piping/core/product_physics && WT/tools/t3_cargo.sh test --locked --offline --lib -- retained_memory::law_tests --nocapture --test-threads=1 > $S/logs/pp_law_$rev.log 2>&1; echo "rc=$?" >> $S/logs/pp_law_$rev.log )
done
# m36 (RV121): (ii) applied to case owners too; does any case-path test see it?
$S/scripts/fk_filtered.sh rv3 fk-rv3 m36_case_ii_full_lib
# m18 (RV121): slot 20 exempt for case owners too; does the whole FK lib suite see it?
$S/scripts/fk_filtered.sh rv4 fk-rv4 m18_full_lib
# m35 (RV121): recorded imports name the last selected operand; does the whole FK lib suite see it?
$S/scripts/fk_filtered.sh rv5 fk-rv5 m35_full_lib
