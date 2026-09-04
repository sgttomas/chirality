#!/usr/bin/env bash
# Deterministic adversarial proof for the Section 8 process-group teardown.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEST_ROOT="$(mktemp -d /private/tmp/chirality-s8-cleanup-test.XXXXXX)"
UNRELATED_A=""
UNRELATED_B=""
ACTIVE_CONTROLLER=""

cleanup_test_processes() {
  set +e
  if [ -n "$ACTIVE_CONTROLLER" ]; then
    kill -KILL -- "-$ACTIVE_CONTROLLER" 2>/dev/null || true
    wait "$ACTIVE_CONTROLLER" 2>/dev/null || true
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

start_test_group() {
  local name="$1"
  shift
  local ready_file="$TEST_ROOT/${name}.ready.json"
  python3 "$GROUP_CONTROLLER" --ready-file "$ready_file" -- "$@" \
    > "$TEST_ROOT/${name}.log" 2>&1 &
  ACTIVE_CONTROLLER=$!
  await_controller_ready "$ready_file" "$ACTIVE_CONTROLLER"
  read -r TEST_CONTROLLER TEST_PGID TEST_CHILD <<< "$(read_controller_ready "$ready_file")"
  [ "$TEST_CONTROLLER" = "$ACTIVE_CONTROLLER" ]
  [ "$TEST_PGID" = "$ACTIVE_CONTROLLER" ]
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
echo "process_inspection_failure_exit=$process_inspection_status"
echo "process_inspection_diagnostic=UNKNOWN"
echo "lsof_inspection_failure_exit=$lsof_inspection_status"
echo "lsof_inspection_diagnostic=UNKNOWN"
echo "incoming_failure_status_preserved=$incoming_failure_status"
echo "failure_manifests=verified"
echo "CLEANUP_HARDENING_PROOF=PASS"
