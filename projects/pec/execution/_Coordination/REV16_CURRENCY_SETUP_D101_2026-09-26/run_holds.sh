#!/bin/sh
# Usage (from projects/pec): sh execution/_Coordination/REV16_CURRENCY_SETUP_D101_2026-09-26/run_holds.sh <operation>
# Runs the PEC reliance-hold preflight for every target in checks/hold_targets.txt.
op="$1"; rr=execution/_Coordination/REV16_CURRENCY_SETUP_D101_2026-09-26
n=0; allow=0
while IFS= read -r t; do
  out=$(python3 execution/_Scripts/pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target "$t" --operation "$op"); rc=$?
  printf '%s\t%s\t%s\n' "$t" "$rc" "$out"
  n=$((n+1)); [ "$rc" -eq 0 ] && echo "$out" | grep -q '"ALLOW"' && allow=$((allow+1))
done < "$rr/checks/hold_targets.txt"
echo "SUMMARY $op $allow/$n ALLOW"
[ "$allow" -eq "$n" ]
