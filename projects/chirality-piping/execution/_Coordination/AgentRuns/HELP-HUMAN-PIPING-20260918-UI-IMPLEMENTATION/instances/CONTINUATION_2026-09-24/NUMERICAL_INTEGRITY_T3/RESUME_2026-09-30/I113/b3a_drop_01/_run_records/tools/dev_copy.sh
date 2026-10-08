#!/bin/bash
# I113: a development copy: make_copy.sh at WT/b2's HEAD (mode s), then WT/b2's uncommitted changes under P copied over
# it (development runs only; recorded suite runs use committed heads). Usage: dev_copy.sh <name>
set -e
WT=WT
S=$WT/scratch/i113_b3a
$S/tools/make_copy.sh HEAD "$1" s
C=$S/copies/$1
(cd "$WT/b2" && GIT_OPTIONAL_LOCKS=0 git diff --name-only HEAD -- projects/chirality-piping | grep -v '^projects/chirality-piping/execution/' | while read -r f; do
  cp "$f" "$C/$f"; echo "overlay: $f"; done)
