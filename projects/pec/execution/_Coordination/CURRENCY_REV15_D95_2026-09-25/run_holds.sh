#!/bin/sh
# Reliance-hold preflight for every D-PEC-95 act target.
# Usage (from projects/pec): sh <run root>/run_holds.sh <operation> <targets file> <output tsv>
op="$1"; targets="$2"; out="$3"
: > "$out"
fails=0
while IFS= read -r t; do
  res=$(python3 execution/_Scripts/pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target "$t" --operation "$op")
  rc=$?
  printf '%s\t%s\t%s\n' "$t" "$rc" "$res" >> "$out"
  [ "$rc" -ne 0 ] && fails=$((fails+1))
done < "$targets"
echo "targets=$(wc -l < "$targets" | tr -d ' ') nonzero_exits=$fails"
