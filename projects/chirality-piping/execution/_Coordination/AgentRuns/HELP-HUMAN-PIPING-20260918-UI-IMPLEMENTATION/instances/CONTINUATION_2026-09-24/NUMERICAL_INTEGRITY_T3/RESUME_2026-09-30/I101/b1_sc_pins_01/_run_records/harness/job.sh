#!/bin/bash
# I101 (B1 I4' RS/TS): one heavy job, through the T3 four-slot wrappers. Usage:
#   job.sh cargo <label> <crate dir> <target dir> <cargo args...>   (through WT/tools/t3_cargo.sh)
#   job.sh slot  <label> <dir> <command...>                          (through WT/tools/t3_slot.sh)
# Logs to S/logs/<label>.log with queued/start/end stamps and the exit code.
WT=WT
S=$WT/scratch/i101_b1_sc_pins
kind=$1; label=$2; dir=$3; shift 3
log=$S/logs/$label.log; mkdir -p "$S/tmp/$label"
export TMPDIR=$S/tmp/$label
export RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8
echo "# i101 job $label ($kind) queued $(date -u '+%FT%TZ') dir=${dir#$WT/}" > "$log"
cd "$dir" || exit 90
if [ "$kind" = cargo ]; then
  target=$1; shift
  echo "# target=${target#$WT/} args: $*" >> "$log"
  CARGO_TARGET_DIR=$target "$WT/tools/t3_cargo.sh" "$@" >> "$log" 2>&1; rc=$?
else
  echo "# args: $*" >> "$log"
  "$WT/tools/t3_slot.sh" /bin/bash -c 'echo "# start $(date -u "+%FT%TZ")"; "$@"' _ "$@" >> "$log" 2>&1; rc=$?
fi
echo "# end $(date -u '+%FT%TZ') rc=$rc" >> "$log"
exit $rc
