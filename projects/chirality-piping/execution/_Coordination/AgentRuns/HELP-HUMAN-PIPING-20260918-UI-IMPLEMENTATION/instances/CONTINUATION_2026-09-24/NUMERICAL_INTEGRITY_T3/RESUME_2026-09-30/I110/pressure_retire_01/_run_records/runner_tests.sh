#!/bin/bash
# I110 probe: headless runner crate tests (lib, bins, integration targets) at the probe tree's current state.
set -u
WT=WT
S=$WT/scratch/i110_pret
cd $WT/t3-pret/P/core/runner/headless || exit 2
export TMPDIR=$S/tmp; mkdir -p $TMPDIR
echo "# start $(date -u +%FT%TZ) head $(GIT_OPTIONAL_LOCKS=0 git rev-parse --short=10 HEAD) diff $(GIT_OPTIONAL_LOCKS=0 git diff --stat | tail -1)"
$WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast --target-dir $WT/targets/i110-pret-runner -- --test-threads=4
echo "# end $(date -u +%FT%TZ) rc=$?"
