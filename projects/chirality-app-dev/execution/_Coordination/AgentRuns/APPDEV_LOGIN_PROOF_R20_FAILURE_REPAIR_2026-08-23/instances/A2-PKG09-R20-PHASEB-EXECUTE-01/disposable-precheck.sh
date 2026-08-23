#!/bin/zsh
set -euo pipefail

ROOT='/private/tmp/ch-r18-91499728-51dd'
USER_DATA='/private/tmp/ch-r18-91499728-51dd/runtime-data'
SOCKET='/private/tmp/ch-r18-91499728-51dd/runtime-data/runtime/control.sock'
EXE='/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality'
CLI='/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/runtime-cli/chirality-cli.mjs'
EVIDENCE='/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-PHASEB-EXECUTE-01'
STDOUT_LOG="$EVIDENCE/disposable-daemon.stdout.log"
STDERR_LOG="$EVIDENCE/disposable-daemon.stderr.log"

test "$ROOT" = '/private/tmp/ch-r18-91499728-51dd'
test "$USER_DATA" = '/private/tmp/ch-r18-91499728-51dd/runtime-data'
test "$SOCKET" = '/private/tmp/ch-r18-91499728-51dd/runtime-data/runtime/control.sock'
test ! -e "$ROOT"
test ! -L "$ROOT"
test -r "$EXE"
test -x "$EXE"
test -r "$CLI"

: > "$STDOUT_LOG"
: > "$STDERR_LOG"

PID=''
cleanup() {
  local prior_status=$?
  set +e
  if test -n "$PID" && /bin/kill -0 "$PID" 2>/dev/null; then
    /bin/kill -TERM "$PID" 2>/dev/null
    local cleanup_poll=0
    while /bin/kill -0 "$PID" 2>/dev/null && test "$cleanup_poll" -lt 100; do
      /bin/sleep 0.05
      cleanup_poll=$((cleanup_poll + 1))
    done
    if /bin/kill -0 "$PID" 2>/dev/null; then
      /bin/kill -KILL "$PID" 2>/dev/null
    fi
    wait "$PID" 2>/dev/null
  fi
  if test -e "$USER_DATA" || test -L "$USER_DATA"; then
    /bin/rm -rf "$USER_DATA"
  fi
  if test -d "$ROOT" && test ! -L "$ROOT"; then
    /bin/rmdir "$ROOT" 2>/dev/null
  fi
  exit "$prior_status"
}
trap cleanup EXIT INT TERM HUP

STARTED_AT="$(/bin/date -u '+%Y-%m-%dT%H:%M:%SZ')"
env \
  CHIRALITY_USER_DATA="$USER_DATA" \
  CHIRALITY_SKIP_CLI_LAUNCHER=1 \
  CHIRALITY_DAEMON_GUI_SPAWN=0 \
  "$EXE" --runtime-daemon >"$STDOUT_LOG" 2>"$STDERR_LOG" &
PID=$!

printf 'started_at=%s\n' "$STARTED_AT"
printf 'executable=%s\n' "$EXE"
printf 'argv_0=%s\n' "$EXE"
printf 'argv_1=--runtime-daemon\n'
printf 'env_CHIRALITY_USER_DATA=%s\n' "$USER_DATA"
printf 'env_CHIRALITY_SKIP_CLI_LAUNCHER=1\n'
printf 'env_CHIRALITY_DAEMON_GUI_SPAWN=0\n'
printf 'pid=%s\n' "$PID"

socket_poll=0
while test ! -S "$SOCKET" && test "$socket_poll" -lt 200; do
  /bin/kill -0 "$PID"
  /bin/sleep 0.05
  socket_poll=$((socket_poll + 1))
done
test -S "$SOCKET"
/bin/kill -0 "$PID"

SOCKET_BYTES="$(LC_ALL=C printf '%s' "$SOCKET" | /usr/bin/wc -c | /usr/bin/tr -d ' ')"
test "$SOCKET_BYTES" = '67'
printf 'socket=%s\n' "$SOCKET"
printf 'socket_bytes=%s\n' "$SOCKET_BYTES"

PROCESS_COMMAND="$(/bin/ps -p "$PID" -o command=)"
case "$PROCESS_COMMAND" in
  "$EXE --runtime-daemon"*) ;;
  *) printf 'unexpected_process_command=%s\n' "$PROCESS_COMMAND" >&2; exit 1 ;;
esac
printf 'process_command=%s\n' "$PROCESS_COMMAND"

CLI_OUTPUT="$(env \
  CHIRALITY_USER_DATA="$USER_DATA" \
  CHIRALITY_SKIP_CLI_LAUNCHER=1 \
  CHIRALITY_DAEMON_GUI_SPAWN=0 \
  ELECTRON_RUN_AS_NODE=1 \
  "$EXE" "$CLI" project list --json)"
test "$CLI_OUTPUT" = '[]'
printf 'cli_command=%s %s project list --json\n' "$EXE" "$CLI"
printf 'cli_output=%s\n' "$CLI_OUTPUT"

STOP_REQUESTED_AT="$(/bin/date -u '+%Y-%m-%dT%H:%M:%SZ')"
/bin/kill -TERM "$PID"
stop_poll=0
while /bin/kill -0 "$PID" 2>/dev/null && test "$stop_poll" -lt 200; do
  /bin/sleep 0.05
  stop_poll=$((stop_poll + 1))
done
if /bin/kill -0 "$PID" 2>/dev/null; then
  printf 'daemon did not stop within the bounded wait\n' >&2
  exit 1
fi
set +e
wait "$PID"
DAEMON_EXIT=$?
set -e
test "$DAEMON_EXIT" -eq 0
test ! -S "$SOCKET"
test ! -e "$SOCKET"
printf 'stop_requested_at=%s\n' "$STOP_REQUESTED_AT"
printf 'daemon_exit=%s\n' "$DAEMON_EXIT"
printf 'stopped_at=%s\n' "$(/bin/date -u '+%Y-%m-%dT%H:%M:%SZ')"

/bin/rm -rf "$USER_DATA"
test ! -e "$USER_DATA"
test ! -L "$USER_DATA"
/bin/rmdir "$ROOT"
test ! -e "$ROOT"
test ! -L "$ROOT"
printf 'cleanup=PASS — process, socket, runtime-data, and exact root absent\n'

trap - EXIT INT TERM HUP
