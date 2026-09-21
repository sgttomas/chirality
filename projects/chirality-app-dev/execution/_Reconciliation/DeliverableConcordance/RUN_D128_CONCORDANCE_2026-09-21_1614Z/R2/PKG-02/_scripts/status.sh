#!/bin/bash
# Print one status line per deliverable (files present, #END, sizes), including DEL-02-01 halves. Usage: status.sh
P="$(cd "$(dirname "$0")/.." && pwd)"
for d in DEL-02-01 DEL-02-01/A DEL-02-01/B DEL-02-02 DEL-02-03 DEL-02-04 DEL-02-05; do
  b=${d%%/*}; line="$d:"
  for f in PREGATHER.md ${b}_claims.csv ${b}_notes.md ${b}_reverse.csv ${b}_errata.csv ${b}_reverse_notes.md; do
    x="$P/$d/$f"; [ -f "$x" ] || continue
    e=$(tail -c 8 "$x" | grep -c '#END'); line="$line $f($(wc -c <"$x" | tr -d ' ')b,END=$e)"
  done
  echo "$line"
done
