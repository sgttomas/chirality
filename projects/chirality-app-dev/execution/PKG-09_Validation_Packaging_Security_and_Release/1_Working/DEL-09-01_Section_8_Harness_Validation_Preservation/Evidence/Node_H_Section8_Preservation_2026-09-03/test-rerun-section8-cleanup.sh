#!/usr/bin/env bash
# Deterministic regression proof for rerun-section8-local.sh cleanup safety.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEST_ROOT="$(mktemp -d /private/tmp/chirality-s8-cleanup-test.XXXXXX)"
trap 'rm -rf "$TEST_ROOT"' EXIT

export RUN_ROOT="$TEST_ROOT/source-init"
export USER_DATA="$TEST_ROOT/source-user-data"
export RERUN_SECTION8_LIBRARY_MODE=1
# shellcheck source=rerun-section8-local.sh
source "$SCRIPT_DIR/rerun-section8-local.sh"
unset RERUN_SECTION8_LIBRARY_MODE

SIGNAL_LOG="$TEST_ROOT/signals.txt"
FAKE_PHASE=term

# Override only the two adapters the production helpers deliberately expose.
# The helpers and teardown logic exercised below are the exact sourced bytes.
read_process_identity() {
  case "$FAKE_PHASE:$1" in
    term:101) printf '%s\n' reused-identity ;;
    term:202) printf '%s\n' live-identity ;;
    kill:101) printf '%s\n' reused-identity ;;
    kill:202) printf '%s\n' later-reused-identity ;;
    *) return 1 ;;
  esac
}

send_process_signal() {
  printf '%s:%s\n' "$1" "$2" >> "$SIGNAL_LOG"
}

records="$(printf '101\told-identity\n202\tlive-identity\n')"
signal_identity_records "$records" TERM
[ "$(cat "$SIGNAL_LOG")" = "TERM:202" ]

# KILL is constructed only from post-TERM verified survivors. PID 202 now has
# a different identity, simulating exit + PID reuse during the grace interval.
FAKE_PHASE="kill"
survivors="$(verified_live_identity_records "$records")"
[ -z "$survivors" ]
signal_identity_records "$survivors" KILL
[ "$(cat "$SIGNAL_LOG")" = "TERM:202" ]

# Early and teardown-time captures are combined, not overwritten.
merged_records="$(
  {
    printf '301\tearly-identity\n'
    printf '302\tteardown-identity\n'
  } | merge_identity_records
)"
[ "$(printf '%s\n' "$merged_records" | wc -l | tr -d ' ')" = "2" ]

# Drive the real teardown function through a controlled invariant failure. The
# test lsof adapter deterministically represents no listener; the explicit
# failure hook can only make cleanup stricter and is never set by a proof run.
lsof() { return 1; }
export DAEMON_PID=""
export DAEMON_ROOT_IDENTITY=""
export DAEMON_TREE_RECORDS=""
export NEXT_PID=""
export NEXT_ROOT_IDENTITY=""
export NEXT_TREE_RECORDS=""
export RUN_ROOT="$TEST_ROOT/failure-run"
export LOGS="$RUN_ROOT/logs"
export ART="$RUN_ROOT/artifacts"
export USER_DATA="$TEST_ROOT/failure-user-data"
export USER_DATA_CREATED=0
export HARNESS_TMP_ROOT="$TEST_ROOT/failure-harness-tmp"
export CHIRALITY_RUNTIME_SOCKET_PATH="$TEST_ROOT/nonexistent.sock"
export FRONTEND="$TEST_ROOT/frontend"
export PORT=65534
export KEEP=1
export RERUN_SECTION8_TEST_FORCE_CLEANUP_FAILURE=1
mkdir -p "$LOGS" "$ART" "$RUN_ROOT/private"

set +e
( true; teardown )
cleanup_status=$?
set -e
[ "$cleanup_status" = "74" ]
grep -Fqx 'forced_test_cleanup_failure=1' "$LOGS/teardown.txt"
( cd "$RUN_ROOT" && shasum -a 256 -c MANIFEST.sha256 >/dev/null )

# A pre-existing proof failure remains authoritative even when cleanup also
# fails; teardown must not flatten it to the cleanup-only status.
export RUN_ROOT="$TEST_ROOT/incoming-failure-run"
export LOGS="$RUN_ROOT/logs"
export ART="$RUN_ROOT/artifacts"
mkdir -p "$LOGS" "$ART" "$RUN_ROOT/private"
set +e
( set +e; ( exit 23 ); teardown )
incoming_failure_status=$?
set -e
[ "$incoming_failure_status" = "23" ]
( cd "$RUN_ROOT" && shasum -a 256 -c MANIFEST.sha256 >/dev/null )

echo "stale_identity_signalled=no"
echo "kill_targets=identity-verified-survivors-only"
echo "early_and_teardown_records=merged"
echo "forced_cleanup_failure_exit=$cleanup_status"
echo "incoming_failure_status_preserved=$incoming_failure_status"
echo "manifest_after_failure=verified"
echo "CLEANUP_HARDENING_PROOF=PASS"
