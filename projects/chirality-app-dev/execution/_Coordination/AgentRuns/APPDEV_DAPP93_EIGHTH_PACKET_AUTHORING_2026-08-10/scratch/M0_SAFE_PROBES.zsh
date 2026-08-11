#!/bin/zsh
set -eu

typeset RUN_ROOT='/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_EIGHTH_PACKET_AUTHORING_2026-08-10'
typeset NEUTRAL_DIR="$RUN_ROOT/scratch/m0-neutral-dir"

/bin/test "$PWD" = "$RUN_ROOT"
/bin/test "$PATH" = '/nonexistent'
/bin/test -x /bin/zsh
/bin/test -x /usr/bin/env
/bin/test -x /usr/bin/printf
/bin/test -x /bin/test
/bin/test -x /bin/mkdir
/bin/test -x /usr/bin/sw_vers
/bin/test -x /usr/bin/uname
/bin/test -x /usr/bin/shasum
/bin/test -x /usr/bin/perl
/bin/test -x /usr/bin/security
/bin/test -x /bin/ps
/bin/test -x /usr/bin/awk
/bin/test -x /bin/date
/bin/test -x /usr/bin/xcrun
/bin/test -x /Applications/Xcode.app/Contents/Developer/usr/bin/lldb
/bin/test -x /usr/bin/tee
/bin/test -x /bin/kill
/bin/test -x /bin/sleep
/bin/test -x /bin/rm

/bin/mkdir -p "$HOME" "$TMPDIR" "$NEUTRAL_DIR"
/usr/bin/printf 'printf:PASS\n'
/usr/bin/sw_vers -productVersion
/usr/bin/uname -m
/usr/bin/shasum -a 256 "$RUN_ROOT/scratch/preflight-probe.txt"
/usr/bin/security help >/dev/null 2>&1
/bin/ps -p $$ -o pid=,ppid=,comm=
/usr/bin/awk 'BEGIN { print "awk:PASS" }'
/bin/date -u '+%Y-%m-%dT%H:%M:%SZ'
/usr/bin/xcrun --find lldb
/usr/bin/xcrun lldb --version
/usr/bin/printf 'tee:PASS\n' | /usr/bin/tee /dev/null
/bin/kill -0 $$
/bin/sleep 0

typeset SAMPLE='assignment:PASS'
export SAMPLE
cd "$NEUTRAL_DIR"
/usr/bin/printf '%s\n' "$SAMPLE" > neutral.txt
/bin/test -s neutral.txt
/usr/bin/printf 'pipeline:PASS\n' | /usr/bin/awk '{ print $0 }'
/bin/test -s neutral.txt && /usr/bin/printf 'and:PASS\n'
/bin/test ! -e absent || /usr/bin/printf 'or:FAIL\n'
if /bin/test -s neutral.txt; then /usr/bin/printf 'if:PASS\n'; fi
for item in one; do /usr/bin/printf 'for:%s\n' "$item"; done
{ /usr/bin/printf 'braces:PASS\n'; }
trap '/usr/bin/printf trap:PASS\\n' EXIT
/bin/sleep 0 &
typeset bg_pid=$!
wait "$bg_pid"
/usr/bin/printf 'background-wait:PASS\n'
cd "$RUN_ROOT"
/bin/rm -r "$NEUTRAL_DIR"
/usr/bin/printf 'M0_SAFE_PROBES_COMPLETE\n'
