#!/bin/bash
# Wait until ANY of the given files exists and ends with #END; print which. Max <minutes>. Usage: wait.sh <minutes> <file>...
P="$(cd "$(dirname "$0")/.." && pwd)"; M=$1; shift; i=0
while :; do
  for f in "$@"; do x="$P/$f"; [ -f "$x" ] && tail -c 8 "$x" | grep -q '#END' && { echo "READY $f"; exit 0; }; done
  i=$((i+1)); [ $i -gt $((M*2)) ] && { echo TIMEOUT; exit 1; }; sleep 30
done
