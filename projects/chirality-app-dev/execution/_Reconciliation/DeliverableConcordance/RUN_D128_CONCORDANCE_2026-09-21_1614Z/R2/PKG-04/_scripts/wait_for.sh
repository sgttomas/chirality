#!/bin/bash
# Usage: wait_for.sh <file-that-must-exist-and-end-#END> [max_iterations]; polls every 45 s.
F="$1"; N="${2:-12}"
for i in $(seq 1 $N); do
  if [ -f "$F" ] && [ "$(tail -n 1 "$F" | tr -d '\r\n ')" = "#END" ]; then sleep 20; echo READY "$F"; exit 0; fi
  sleep 45
done
echo WAITING "$F"
