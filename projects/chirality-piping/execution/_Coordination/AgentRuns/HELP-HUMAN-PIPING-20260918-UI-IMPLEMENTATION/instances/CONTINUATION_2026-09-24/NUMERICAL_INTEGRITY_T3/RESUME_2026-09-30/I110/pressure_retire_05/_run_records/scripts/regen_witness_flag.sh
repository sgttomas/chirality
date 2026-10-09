#!/bin/bash
# I110 round 4: regenerate the five DEL-10-05 payload-binding witness outputs at the tree's head (into r4/witness) and compare.
set -u
WT=WT; S=$WT/scratch/i110_pret; O=$S/r4/witness; mkdir -p $O
export TMPDIR=$S/tmp
cd $WT/t3-pret/projects/chirality-piping || exit 2
for spec in "run-benchmark benchmark_single_case" "run-benchmark benchmark_multi_case" "run-regression regression_full_suite" "run-benchmark benchmark_payload_missing" "run-regression regression_payload_missing"; do
  set -- $spec
  $WT/tools/t3_cargo.sh run --locked --offline --target-dir $WT/targets/i110-pret-runner --manifest-path core/runner/headless/Cargo.toml --bin openpipestress-runner -- $1 --explicit-local-private-intent --input validation/witness/inputs/del1005_payload_binding_$2_input.json --output $O/flag_$2.json > $O/flag_$2.log 2>&1
  rc=$?
  if cmp -s $O/flag_$2.json validation/witness/generated/del1005_payload_binding_$2.json; then same=same; else same=DIFFERS; fi
  echo "$2 rc=$rc $same"
done
