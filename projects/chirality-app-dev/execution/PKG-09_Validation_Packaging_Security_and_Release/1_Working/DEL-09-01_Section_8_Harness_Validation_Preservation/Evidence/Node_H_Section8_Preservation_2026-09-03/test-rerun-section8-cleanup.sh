#!/usr/bin/env bash
# Deterministic adversarial proof for the layered Section 8 teardown.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEST_ROOT="$(mktemp -d /private/tmp/chirality-s8-cleanup-test.XXXXXX)"
UNRELATED_A=""
UNRELATED_B=""
ACTIVE_CONTROLLER=""
ESCAPED_TEST_PGID=""

cleanup_test_processes() {
  set +e
  if [ -n "$ACTIVE_CONTROLLER" ]; then
    kill -KILL -- "-$ACTIVE_CONTROLLER" 2>/dev/null || true
    wait "$ACTIVE_CONTROLLER" 2>/dev/null || true
  fi
  if [ -n "$ESCAPED_TEST_PGID" ]; then
    kill -KILL -- "-$ESCAPED_TEST_PGID" 2>/dev/null || true
  fi
  if [ -n "$UNRELATED_A" ]; then kill -KILL "$UNRELATED_A" 2>/dev/null || true; wait "$UNRELATED_A" 2>/dev/null || true; fi
  if [ -n "$UNRELATED_B" ]; then kill -KILL "$UNRELATED_B" 2>/dev/null || true; wait "$UNRELATED_B" 2>/dev/null || true; fi
  rm -rf "$TEST_ROOT"
}
trap cleanup_test_processes EXIT

export RUN_ROOT="$TEST_ROOT/source-init"
export USER_DATA="$TEST_ROOT/source-user-data"
export RERUN_SECTION8_LIBRARY_MODE=1
# shellcheck source=rerun-section8-local.sh
source "$SCRIPT_DIR/rerun-section8-local.sh"
unset RERUN_SECTION8_LIBRARY_MODE
REAL_FRONTEND="$FRONTEND"

start_test_group() {
  local name="$1"
  shift
  local ready_file="$TEST_ROOT/${name}.ready.json"
  TEST_AUDIT_FILE="$TEST_ROOT/${name}.audit.json"
  python3 "$GROUP_CONTROLLER" --ready-file "$ready_file" --audit-file "$TEST_AUDIT_FILE" -- "$@" \
    > "$TEST_ROOT/${name}.log" 2>&1 &
  ACTIVE_CONTROLLER=$!
  await_controller_ready "$ready_file" "$ACTIVE_CONTROLLER"
  read -r TEST_CONTROLLER TEST_PGID TEST_CHILD <<< "$(read_controller_ready "$ready_file")"
  [ "$TEST_CONTROLLER" = "$ACTIVE_CONTROLLER" ]
  [ "$TEST_PGID" = "$ACTIVE_CONTROLLER" ]
  for _ in $(seq 1 100); do
    [ -f "$TEST_AUDIT_FILE" ] && break
    sleep 0.02
  done
}

finish_test_group() {
  send_anchored_group_signal "$TEST_CONTROLLER" "$TEST_PGID" KILL
  wait "$TEST_CONTROLLER" 2>/dev/null || true
  ACTIVE_CONTROLLER=""
  [ "$(process_group_member_count "$TEST_PGID")" = "0" ]
}

# Two distinct same-command processes launched within the same start-second are
# adversarial foreign PIDs. They are never signal targets: only the anchored
# controlled PGID below is signalled.
for _ in 1 2 3; do
  /bin/sleep 30 & UNRELATED_A=$!
  /bin/sleep 30 & UNRELATED_B=$!
  start_a="$(ps -p "$UNRELATED_A" -o lstart=)"
  start_b="$(ps -p "$UNRELATED_B" -o lstart=)"
  [ "$start_a" = "$start_b" ] && break
  kill -KILL "$UNRELATED_A" "$UNRELATED_B"
  wait "$UNRELATED_A" 2>/dev/null || true
  wait "$UNRELATED_B" 2>/dev/null || true
  UNRELATED_A=""
  UNRELATED_B=""
done
[ -n "$UNRELATED_A" ] && [ "$start_a" = "$start_b" ]

start_test_group normal-child /bin/sleep 30
assert_controller_contained "$TEST_AUDIT_FILE" "$TEST_CONTROLLER" "$TEST_PGID"
send_anchored_group_signal "$TEST_CONTROLLER" "$TEST_PGID" TERM
sleep 0.2
finish_test_group
kill -0 "$UNRELATED_A"
kill -0 "$UNRELATED_B"

# A TERM-resistant descendant remains visible before escalation and is removed
# by the atomic group KILL while the controller still anchors the PGID.
start_test_group term-resistant-child python3 -c \
  'import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(30)'
sleep 0.3
assert_controller_contained "$TEST_AUDIT_FILE" "$TEST_CONTROLLER" "$TEST_PGID"
send_anchored_group_signal "$TEST_CONTROLLER" "$TEST_PGID" TERM
sleep 0.2
survivor_count="$(process_group_noncontroller_count "$TEST_PGID" "$TEST_CONTROLLER")"
[ "$survivor_count" -ge 1 ]
finish_test_group

reset_teardown_state() {
  local name="$1"
  export RUN_ROOT="$TEST_ROOT/$name"
  export LOGS="$RUN_ROOT/logs"
  export ART="$RUN_ROOT/artifacts"
  export USER_DATA="$TEST_ROOT/${name}-user-data"
  export USER_DATA_CREATED=0
  export HARNESS_TMP_ROOT="$TEST_ROOT/${name}-harness-tmp"
  export CHIRALITY_RUNTIME_SOCKET_PATH="$TEST_ROOT/${name}.sock"
  export FRONTEND="$TEST_ROOT/frontend"
  export PORT=65534
  export KEEP=1
  export DAEMON_CONTROLLER_PID=""
  export DAEMON_PGID=""
  export DAEMON_CHILD_PID=""
  export NEXT_CONTROLLER_PID=""
  export NEXT_PGID=""
  export NEXT_CHILD_PID=""
  export DAEMON_AUDIT_FILE=""
  export NEXT_AUDIT_FILE=""
  mkdir -p "$LOGS" "$ART" "$RUN_ROOT/private"
}

# A process-table failure while a controlled child is live must produce UNKNOWN
# and exit 74. Group signalling remains safe because it does not depend on the
# failed inspection.
start_test_group process-inspection-failure python3 -c \
  'import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(30)'
sleep 0.3
reset_teardown_state process-inspection-failure-run
NEXT_CONTROLLER_PID="$TEST_CONTROLLER"
NEXT_PGID="$TEST_PGID"
NEXT_CHILD_PID="$TEST_CHILD"
NEXT_AUDIT_FILE="$TEST_AUDIT_FILE"
read_process_table() { return 2; }
set +e
( true; teardown )
process_inspection_status=$?
set -e
[ "$process_inspection_status" = "74" ]
grep -Fqx 'next_group_survivors_before_kill=UNKNOWN' "$LOGS/teardown.txt"
grep -Fqx 'next_process_group_remaining=UNKNOWN' "$LOGS/teardown.txt"
wait "$TEST_CONTROLLER" 2>/dev/null || true
ACTIVE_CONTROLLER=""
read_process_table() { ps -axo pid=,pgid= 2>/dev/null; }
( cd "$RUN_ROOT" && shasum -a 256 -c MANIFEST.sha256 >/dev/null )

# A controlled descendant that creates a new session escapes the inner PGID
# layer. That layer must retain the violation and fail closed rather than claim
# zero-descendant success. The outer LaunchAgent-coalition test below proves
# that the authoritative cleanup still removes this class safely.
start_test_group setsid-escape python3 -c \
  'import os,time; os.setsid(); time.sleep(30)'
ESCAPED_TEST_PGID="$TEST_CHILD"
for _ in $(seq 1 100); do
  [ "$(controller_audit_state "$TEST_AUDIT_FILE" 2>/dev/null || true)" = "violation" ] && break
  sleep 0.02
done
[ "$(controller_audit_state "$TEST_AUDIT_FILE")" = "violation" ]
python3 - "$TEST_AUDIT_FILE" "$TEST_CHILD" <<'PY'
import json
import sys

audit = json.load(open(sys.argv[1], encoding="utf-8"))
child = int(sys.argv[2])
assert audit["state"] == "violation"
assert any(item["pid"] == child and item["pgid"] == child for item in audit["violations"])
PY
reset_teardown_state setsid-escape-run
NEXT_CONTROLLER_PID="$TEST_CONTROLLER"
NEXT_PGID="$TEST_PGID"
NEXT_CHILD_PID="$TEST_CHILD"
NEXT_AUDIT_FILE="$TEST_AUDIT_FILE"
set +e
( true; teardown )
setsid_escape_status=$?
set -e
[ "$setsid_escape_status" = "74" ]
grep -Fqx 'next_descendant_audit=violation' "$LOGS/teardown.txt"
kill -0 "$TEST_CHILD"
kill -KILL -- "-$ESCAPED_TEST_PGID"
for _ in $(seq 1 100); do
  kill -0 "$TEST_CHILD" 2>/dev/null || break
  sleep 0.02
done
! kill -0 "$TEST_CHILD" 2>/dev/null
ESCAPED_TEST_PGID=""
wait "$TEST_CONTROLLER" 2>/dev/null || true
ACTIVE_CONTROLLER=""
( cd "$RUN_ROOT" && shasum -a 256 -c MANIFEST.sha256 >/dev/null )

# A real lsof command failure is not interpreted as zero listeners.
reset_teardown_state lsof-inspection-failure-run
lsof() { return 1; }
set +e
( true; teardown )
lsof_inspection_status=$?
set -e
[ "$lsof_inspection_status" = "74" ]
grep -Fqx 'port_65534_listeners_after_stop=UNKNOWN' "$LOGS/teardown.txt"
( cd "$RUN_ROOT" && shasum -a 256 -c MANIFEST.sha256 >/dev/null )

# An existing proof failure remains authoritative when lsof also fails.
reset_teardown_state incoming-failure-run
set +e
( set +e; ( exit 23 ); teardown )
incoming_failure_status=$?
set -e
[ "$incoming_failure_status" = "23" ]
( cd "$RUN_ROOT" && shasum -a 256 -c MANIFEST.sha256 >/dev/null )
unset -f lsof

# Exercise the host-pinned authoritative boundary. The harmless LaunchAgent
# fixture creates TERM-resistant setsid descendants, including a forker that
# creates another setsid descendant. Ordinary bootout leaves those processes
# alive; audit-token-bound coalition TERM/STOP/KILL sweeps remove all of them,
# while an unrelated same-command/same-second process survives. Every required
# observation/launch/signal failure must return nonzero and remove probe state.
COALITION_TEST_ROOT="$TEST_ROOT/coalition"
COALITION_TARGETS=(
  --target-binary /bin/bash
  --target-binary "$(command -v python3)"
  --target-binary "$(command -v node)"
  --target-binary "$REAL_FRONTEND/node_modules/electron/dist/Electron.app"
)
python3 "$COALITION_SUPERVISOR" self-test \
  --root "$COALITION_TEST_ROOT" "${COALITION_TARGETS[@]}"
python3 - "$COALITION_TEST_ROOT/coalition-capability.json" <<'PY'
import json
import sys

report = json.load(open(sys.argv[1], encoding="utf-8"))
probe = report["capability"]["launchAgentProbe"]
assert report["status"] == "PASS" and report["exitCode"] == 0
assert len(probe["setsidChildren"]) >= 6
assert len(probe["setsidChildrenAfterBootout"]) == len(probe["setsidChildren"])
assert probe["stalePidversion"] == "ESRCH"
assert probe["sweep"]["status"] == "PASS"
assert probe["sweep"]["consecutiveEmptyScans"] >= 3
assert probe["foreignBefore"]["uniqueId"] == probe["foreignAfterSweep"]["uniqueId"]
assert any(
    child["command"] == probe["foreignBefore"]["command"]
    and child["startSec"] == probe["foreignBefore"]["startSec"]
    for child in probe["setsidChildren"]
)
PY
for failure in enumeration unique coalition signal bootstrap bootout; do
  set +e
  python3 "$COALITION_SUPERVISOR" self-test \
    --root "$COALITION_TEST_ROOT" "${COALITION_TARGETS[@]}" \
    --inject-failure "$failure"
  failure_status=$?
  set -e
  [ "$failure_status" = "74" ]
  python3 - "$COALITION_TEST_ROOT/coalition-capability-${failure}-failure.json" <<'PY'
import json
import sys

report = json.load(open(sys.argv[1], encoding="utf-8"))
assert report["status"] == "FAIL"
assert report["exitCode"] == 74
assert report["temporaryRootRemoved"] is True
assert "error" in report
PY
done

kill -KILL "$UNRELATED_A" "$UNRELATED_B"
wait "$UNRELATED_A" 2>/dev/null || true
wait "$UNRELATED_B" 2>/dev/null || true
UNRELATED_A=""
UNRELATED_B=""

echo "same_command_same_second_foreign_processes=survived"
echo "individual_pid_signal_authority=absent"
echo "signal_boundary=controller_anchored_atomic_process_group"
echo "term_resistant_descendants_before_kill=$survivor_count"
echo "term_resistant_descendants_after_kill=0"
echo "setsid_escape_audit=violation"
echo "setsid_escape_cleanup_exit=$setsid_escape_status"
echo "setsid_escape_after_automatic_group_kill=alive"
echo "setsid_escape_after_explicit_test_group_kill=0"
echo "launchagent_coalition_preflight=PASS"
echo "setsid_escape_after_bootout=alive"
echo "setsid_escape_after_coalition_sweep=0"
echo "forked_setsid_descendant_after_coalition_sweep=0"
echo "audit_token_stale_pidversion=ESRCH"
echo "same_command_same_second_foreign_after_coalition_sweep=alive"
echo "coalition_empty_scans=3"
echo "coalition_fault_injections=enumeration,unique,coalition,signal,bootstrap,bootout:exit-74"
echo "process_inspection_failure_exit=$process_inspection_status"
echo "process_inspection_diagnostic=UNKNOWN"
echo "lsof_inspection_failure_exit=$lsof_inspection_status"
echo "lsof_inspection_diagnostic=UNKNOWN"
echo "incoming_failure_status_preserved=$incoming_failure_status"
echo "failure_manifests=verified"
echo "CLEANUP_HARDENING_PROOF=PASS"
