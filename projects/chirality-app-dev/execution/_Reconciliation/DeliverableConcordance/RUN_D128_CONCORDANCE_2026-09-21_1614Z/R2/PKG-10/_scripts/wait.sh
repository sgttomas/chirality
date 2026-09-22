#!/bin/bash
# Wait until poll output changes from the given baseline file, or timeout (seconds) elapses.
H="$(cd "$(dirname "$0")" && pwd)"; base="$1"; lim="${2:-540}"; t=0
until [ "$(python3 "$H/poll.py")" != "$(cat "$base")" ] || [ $t -ge $lim ]; do sleep 45; t=$((t+45)); done
python3 "$H/poll.py"
