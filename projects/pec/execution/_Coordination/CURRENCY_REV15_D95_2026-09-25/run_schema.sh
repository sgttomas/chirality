#!/bin/sh
# Schema validation of the ten D-PEC-95 N3 registers (run from the repository root).
# Usage: sh <run root>/run_schema.sh <act report tsv> <output file>
report="$1"; out="$2"
: > "$out"
fails=0
for p in $(awk -F'\t' '$1=="WRITE" && $2 ~ /Dependencies\.csv$/ {print $2}' "$report"); do
  echo "== $p" >> "$out"
  PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py "$p" >> "$out" 2>&1
  rc=$?
  echo "exit=$rc" >> "$out"
  [ "$rc" -ne 0 ] && fails=$((fails+1))
done
echo "registers=$(grep -c '^== ' "$out") nonzero_exits=$fails"
