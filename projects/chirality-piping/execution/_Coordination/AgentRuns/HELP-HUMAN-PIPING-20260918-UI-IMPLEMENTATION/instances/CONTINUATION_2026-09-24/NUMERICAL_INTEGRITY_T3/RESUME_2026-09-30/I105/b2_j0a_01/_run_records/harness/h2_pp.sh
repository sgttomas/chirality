#!/bin/bash
# I105 J0a: PP's suite (all targets) at the final head e582b61f9e (the rule-8 table row), in an archive copy.
WT=WT
S=$WT/scratch/i105_j0a
$S/bin/copy.sh e582b61f9e h2 || exit 1
P=$S/copies/h2/projects/chirality-piping
RUST_TEST_THREADS=4 $S/bin/job.sh cargo h2_pp "$P/core/product_physics" "$WT/targets/i105-j0a-h2-pp" test --locked --offline --no-fail-fast; echo "h2 pp rc=$?"
