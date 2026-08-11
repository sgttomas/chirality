#!/bin/zsh
set -u
ROOT=/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_TENTH_PACKET_AUTHORING_2026-08-10
HOME_DIR=$ROOT/scratch/m0-home
TMP_DIR=$ROOT/scratch/m0-tmp
OUT=$ROOT/scratch/M0_SAFE_PROBE_OUTPUT.txt
exec > "$OUT" 2>&1
/usr/bin/printf 'M0_BEGIN\n'
/bin/mkdir -p "$HOME_DIR" "$TMP_DIR"; /usr/bin/printf 'mkdir=%d\n' $?
/usr/bin/printf 'printf=0\n'
/bin/test -x /bin/zsh; /usr/bin/printf 'test=%d\n' $?
/usr/bin/sw_vers -productVersion; /usr/bin/printf 'sw_vers=%d\n' $?
/usr/bin/uname -m; /usr/bin/printf 'uname=%d\n' $?
/usr/bin/shasum -a 256 "$ROOT/manager/STUB_CONTRACT.txt"; /usr/bin/printf 'shasum_perl=%d\n' $?
/usr/bin/security help; /usr/bin/printf 'security_help=%d\n' $?
/bin/ps -p $$ -o pid=,ppid=,comm=; /usr/bin/printf 'ps=%d\n' $?
/usr/bin/awk 'BEGIN { print "AWK_OK" }'; /usr/bin/printf 'awk=%d\n' $?
/bin/date -u '+%Y-%m-%dT%H:%M:%SZ'; /usr/bin/printf 'date=%d\n' $?
/usr/bin/xcrun /Applications/Xcode.app/Contents/Developer/usr/bin/lldb --version; /usr/bin/printf 'xcrun_lldb=%d\n' $?
/usr/bin/printf 'TEE_OK\n' | /usr/bin/tee /dev/null; /usr/bin/printf 'tee=%d\n' $?
/bin/kill -0 $$; /usr/bin/printf 'kill_zero=%d\n' $?
/bin/sleep 0; /usr/bin/printf 'sleep=%d\n' $?
/bin/rm -f "$TMP_DIR/xcrun_db"; /usr/bin/printf 'rm=%d\n' $?
/usr/bin/printf 'M0_END\n'
exit 0
