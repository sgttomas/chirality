#!/bin/bash
# I107 SB, item 5 of B1's Pass B: I65's run_cargo_a.sh (as I72 retargeted it), retargeted to B1. The jobs:
#   1. PP's whole suite on the basis (registered: the PR head carries the registration), fresh target;
#   2. the runner/headless suite on the basis, and on SQ's registered tree (b1 ddc8eaaf54) as its reference;
#   3. SQ's 40 witness entry points (R/I104/.../g6/witnesses/table_dev.json; SQ's witness_chain.sh form:
#      `--exact --include-ignored --test-threads=1 --nocapture`), one process each;
#   4. the challenge: every ignored entry and the default test, one process each (RV124's chain_wit.sh form).
# Every cargo through t3_cargo.sh (--locked --offline); every test binary through t3_slot.sh; one at a time.
# Outcomes are I65's extraction (awk/sed/sort). Not a measurement: no time -l, nothing through t3_exclusive.sh.
# Usage: I107_WT=<WT> run_cargo_b1.sh <tag> <work copy dir> <SQ registered tree dir> <pass out dir>
set -u
T=${I107_WT:?}; TAG=$1; WK=$2; SQREG=$3; O=$4
R0=$T/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30
SQ=$R0/I104/b1_sq_01/_run_records
C=$WK/projects/chirality-piping/core; L=$O/logs; TGT=$T/targets/i107-sb-$TAG
export TMPDIR=$T/scratch/i107_b1_sb/tmp PATH=$T/venv/bin:$PATH
guard() { pgrep -f memguard.sh >/dev/null || { echo "MEMGUARD NOT RUNNING"; exit 9; }; }
outcomes() { awk '/^ *Running /{t=$2} /^test .* \.\.\. (ok|FAILED|ignored)/{sub(/ \(.*\)/,""); print t" :: "$0}' $L/$1.log | sed -E 's#target/[^ ]*/deps/##; s#-[0-9a-f]{16}##' | sort > $L/$1.outcomes; }
count() { echo "$1: $(grep -c ' ok$' $L/$1.outcomes) passed, $(grep -c FAILED $L/$1.outcomes) failed, $(grep -c ignored $L/$1.outcomes) ignored"; grep FAILED $L/$1.outcomes; }
run() { # run <log name> <manifest> <target dir>
  guard; echo "== $1 start $(date -u +%FT%TZ)"
  ( cd $(dirname $2) && env CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4 $T/tools/t3_cargo.sh test --locked --offline --no-fail-fast --manifest-path $2 --target-dir $3 > $L/$1.log 2>&1 )
  echo "== $1 exit=$? $(date -u +%FT%TZ)"; outcomes $1; count $1; }
run ${TAG}_pp $C/product_physics/Cargo.toml $TGT
run ${TAG}_runner $C/runner/headless/Cargo.toml $TGT-runner
run sq_runner $SQREG/projects/chirality-piping/core/runner/headless/Cargo.toml $TGT-runner-sq
LIB=$(sed -n 's#^ *Running unittests src/lib.rs (\(.*\))$#\1#p' $L/${TAG}_pp.log | head -1)
CH=$(sed -n 's#^ *Running tests/retained_memory_challenge.rs (\(.*\))$#\1#p' $L/${TAG}_pp.log | head -1)
echo "== binaries lib=$(basename "$LIB") challenge=$(basename "$CH")"
[ -x "$LIB" ] && [ -x "$CH" ] || { echo "== binaries missing"; exit 1; }
mkdir -p $O/wit $O/chal; cd $C/product_physics
python3 -c "import json,sys; [print(k) for k in sorted(json.load(open(sys.argv[1])))]" $SQ/g6/witnesses/table_dev.json > $L/witness_entries.txt
while read -r k; do
  guard
  $T/tools/t3_slot.sh $LIB "retained_memory::witness_tests::$(echo $k | sed 's/\./::/g')" --exact --include-ignored --test-threads=1 --nocapture > $O/wit/$k.out 2>&1
  echo "== witness $k exit=$?"
done < $L/witness_entries.txt
$CH --list --ignored 2>/dev/null | sed -n 's/: test$//p' > $L/challenge_entries.txt
while read -r t; do
  guard
  $T/tools/t3_slot.sh $CH "$t" --exact --ignored --test-threads=1 --nocapture > $O/chal/$(echo "$t" | sed 's/::/__/g').log 2>&1
  echo "== challenge $t exit=$?"
done < $L/challenge_entries.txt
guard
$T/tools/t3_slot.sh $CH retained_direct_peak_is_within_the_profiles_bounds --exact --test-threads=1 --nocapture > $O/chal/default.log 2>&1
echo "== challenge default exit=$?"
echo "== done $(date -u +%FT%TZ)"
