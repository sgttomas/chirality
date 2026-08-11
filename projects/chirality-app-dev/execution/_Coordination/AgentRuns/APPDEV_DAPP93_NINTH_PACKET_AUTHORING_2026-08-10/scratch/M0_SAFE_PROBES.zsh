#!/bin/zsh
set -u
ROOT='projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_NINTH_PACKET_AUTHORING_2026-08-10'
/usr/bin/printf 'P01|printf|BEGIN\n'
/usr/bin/printf 'P01_OK\n'; /usr/bin/printf 'P01|exit=%s\n' "$?"
/bin/test -x /bin/zsh; /usr/bin/printf 'P02|test|exit=%s\n' "$?"
/bin/mkdir -p "$ROOT/scratch/probe-dir"; /usr/bin/printf 'P03|mkdir|exit=%s\n' "$?"
/usr/bin/sw_vers -productVersion; /usr/bin/printf 'P04|sw_vers|exit=%s\n' "$?"
/usr/bin/uname -m; /usr/bin/printf 'P05|uname|exit=%s\n' "$?"
/usr/bin/shasum -a 256 "$ROOT/scratch/M0_SYNTAX_PROBE.zsh"; /usr/bin/printf 'P06|shasum-perl|exit=%s\n' "$?"
/usr/bin/security help; /usr/bin/printf 'P07|security-help|exit=%s\n' "$?"
/bin/ps -p $$ -o pid=,ppid=,comm=; /usr/bin/printf 'P08|ps|exit=%s\n' "$?"
/usr/bin/awk 'BEGIN { print "P09_AWK_OK" }'; /usr/bin/printf 'P09|awk|exit=%s\n' "$?"
/bin/date -u '+%Y-%m-%dT%H:%M:%SZ'; /usr/bin/printf 'P10|date|exit=%s\n' "$?"
/usr/bin/xcrun /Applications/Xcode.app/Contents/Developer/usr/bin/lldb --version; /usr/bin/printf 'P11|xcrun-lldb|exit=%s\n' "$?"
/usr/bin/printf 'P12_TEE_OK\n' | /usr/bin/tee "$ROOT/scratch/probe-dir/tee.txt"; /usr/bin/printf 'P12|tee|exit=%s\n' "$?"
/bin/kill -0 $$; /usr/bin/printf 'P13|kill-zero|exit=%s\n' "$?"
/bin/sleep 0; /usr/bin/printf 'P14|sleep|exit=%s\n' "$?"
/bin/rm "$ROOT/scratch/probe-dir/tee.txt"; /usr/bin/printf 'P15|rm-file|exit=%s\n' "$?"
/bin/rm -d "$ROOT/scratch/probe-dir"; /usr/bin/printf 'P16|rm-dir|exit=%s\n' "$?"
/usr/bin/printf 'M0_PROBES_COMPLETE\n'
