#!/bin/bash
# I110 probe: PP lib + pressure-relevant integration tests (excludes the three memory tests), at the tree's current state.
# Usage: pp_tests.sh <label>
set -u
WT=WT
S=$WT/scratch/i110_pret
cd $WT/t3-pret/P/core/product_physics || exit 2
export TMPDIR=$S/tmp; mkdir -p $TMPDIR
TESTS=""
for t in elastic_extrema_runtime f1b_w2_runtime formation_check_runtime k2a_formation_range_runtime k5_curved_mechanism_runtime load_reference_state_runtime load_reference_state_runtime_extension physics_source_runtime pressure_grouping_limits pressure_membrane_range pressure_runtime pressure_section_geometry preview_physics_runtime represented_gap_publication retained_precision_admission s11f_site_test source_block_recovery stress_maximum_coverage support_reactions_runtime; do TESTS="$TESTS --test $t"; done
echo "# start $(date -u +%FT%TZ) head $(GIT_OPTIONAL_LOCKS=0 git rev-parse --short=10 HEAD) diff $(GIT_OPTIONAL_LOCKS=0 git diff --stat | tail -1)"
$WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast --target-dir $WT/targets/i110-pret --lib $TESTS -- --test-threads=4
echo "# end $(date -u +%FT%TZ) rc=$?"
