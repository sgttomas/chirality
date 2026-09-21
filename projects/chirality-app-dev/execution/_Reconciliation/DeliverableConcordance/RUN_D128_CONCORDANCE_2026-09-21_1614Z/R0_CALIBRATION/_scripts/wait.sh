#!/bin/bash
# Wait until the poll output differs from the given baseline file (stable for one extra cycle), max ~9 min.
D="$(cd "$(dirname "$0")" && pwd)"; BASE="$1"
for i in $(seq 1 11); do
  python3 "$D/poll.py" > "$D/.poll_now" 2>&1
  if ! cmp -s "$D/.poll_now" "$BASE"; then sleep 40; python3 "$D/poll.py" > "$D/.poll_now2" 2>&1
    if cmp -s "$D/.poll_now" "$D/.poll_now2"; then cat "$D/.poll_now"; cp "$D/.poll_now" "$BASE"; exit 0; fi; fi
  sleep 45
done
echo TIMEOUT; cat "$D/.poll_now"
