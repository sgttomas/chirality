#!/bin/bash
# wait_sealed.sh <n> <timeout>: wait until at least n units report SEALED (or FAIL), then print.
H="$(cd "$(dirname "$0")" && pwd)"; n=$1; lim=${2:-570}; t=0
until [ "$(python3 "$H/sealed.py" | grep -cE 'SEALED|FAIL')" -ge "$n" ] || [ $t -ge $lim ]; do sleep 45; t=$((t+45)); done
python3 "$H/sealed.py"
