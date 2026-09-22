#!/bin/bash
# Print one status line per deliverable (files present, #END, sizes). Usage: status.sh
P="$(cd "$(dirname "$0")/.." && pwd)"
for d in DEL-08-01 DEL-08-02 DEL-08-03 DEL-08-04 DEL-08-05; do
  line="$d:"
  for f in PREGATHER.md ${d}_claims.csv ${d}_notes.md ${d}_reverse.csv ${d}_errata.csv ${d}_reverse_notes.md; do
    x="$P/$d/$f"; [ -f "$x" ] || continue
    e=$(tail -c 8 "$x" | grep -c '#END'); line="$line $f($(wc -c <"$x" | tr -d ' ')b,END=$e)"
  done
  echo "$line"
done
