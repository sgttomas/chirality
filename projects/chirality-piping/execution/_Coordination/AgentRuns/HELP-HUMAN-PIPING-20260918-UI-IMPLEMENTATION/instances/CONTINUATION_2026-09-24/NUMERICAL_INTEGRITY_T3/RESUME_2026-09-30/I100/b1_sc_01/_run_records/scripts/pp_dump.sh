#!/bin/bash
# I100: one cargo job: PP's two pinned-successor tests (RV109's SF-2 orderings; I98's reversed milestone), in M
# with a scratch-only dump added after each pin assertion (written only after the pin holds), into S/work/pp_dump.
source WT/scratch/i100_b1_sc/tools/env.sh
export I100_DUMP=$S/work/pp_dump
$S/tools/job.sh cargo pp_dump $P/core/product_physics $WT/targets/i100-b1-sc/pp test --locked --offline --lib -- b1_sp_sf2_selected_not_first_and_two_selected_pins b1_sp_constructor_ordinal_is_the_authored_index --nocapture
echo "pp rc=$?"
