#!/bin/zsh
# usage: preflight.sh <repo> <table.tsv> <operation> <audit-stem> <run-root-stem>
repo=$1; table=$2; op=$3; audit=$4; runroot=$5
cd "$repo/projects/pec" || exit 9
targets=()
while IFS=$'\t' read -r p rest; do targets+=("${p#projects/pec/}"); done < "$table"
targets+=("execution/_Evaluation/DecompCoverage/_LATEST.md" "$audit" "$runroot")
n=0; allow=0
for t in "${targets[@]}"; do
  out=$(PYTHONDONTWRITEBYTECODE=1 python3 execution/_Scripts/pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --operation "$op" --target "$t")
  rc=$?
  n=$((n+1)); [[ $rc == 0 && $out == *'"ALLOW"'* ]] && allow=$((allow+1))
  print -r -- "$rc	$out	$t"
done
print -r -- "TOTAL $n ALLOW $allow"
