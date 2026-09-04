#!/usr/bin/env bash
# rerun-section8-local.sh — bounded local rerun of the Section 8 premerge
# evidence under the shared-runtime binding lifecycle that
# .github/workflows/harness-premerge.yml performs in CI.
#
# What it does (mirrors the workflow step for step, on macOS without xvfb):
#   1. refuses to start unless the requested dev-server port is free
#   2. builds the Electron runtime host + bundled CLI (npm run build:electron)
#   3. starts dist-electron/main.js --runtime-daemon under a DISPOSABLE
#      --user-data-dir (never the operator's real userData / LaunchAgent daemon)
#      with Chromium's --use-mock-keychain so the dev binary never blocks on the
#      operator's macOS Keychain (see the comment at the launch line)
#   4. registers projects/chirality-app-dev/chirality.project.json with that
#      daemon through dist-runtime/chirality-cli.mjs project register
#   5. starts `next dev` bound to the daemon (CHIRALITY_RUNTIME_* env)
#   6. waits for /api/harness/session/list readiness
#   7. runs `npm run harness:validate:premerge` (Section 8 + report-only Section 9)
#      and, with WITH_RELEASE_QUALITY=1, `npm run validate:release-quality`
#   8. records containment observations (daemon listeners, socket mode, git status)
#   9. requires continuous descendant audits to show that no process left its
#      anchored group, atomically signals both groups, removes state
#      (KEEP=1 keeps it), and — as the LAST act of teardown, after
#      teardown.txt/cleanup.txt exist and both processes are gone — writes
#      RUN_ROOT/MANIFEST.sha256 over artifacts/** and logs/** (LC_ALL=C sorted)
#
# It changes no product source and no tracked file. The only writes inside the
# checkout are the gitignored stable artifacts under frontend/artifacts/harness/**
# and the gitignored frontend/.chirality/sessions directory the manifest's
# legacySessionRoots entry requires at registration (same as CI).
#
# Inputs (environment):
#   RUN_ROOT   (required) absolute, disposable output directory for logs/artifacts
#   PORT       dev-server port (default 51840; CI uses 3000)
#   TMPDIR     left as the host default (the Section 8 run tree lives under it)
#   USER_DATA  daemon user-data dir; default mktemp under /private/tmp because
#              macOS caps Unix socket paths at 104 bytes and the daemon derives
#              <userData>/runtime/control.sock from it. A caller-supplied
#              USER_DATA is never removed by this script (only a mktemp-created
#              one is); the harness's own run tree
#              $TMPDIR/chirality-harness-validation/latest is SHARED with any
#              other Section 8 run on the host — the Section 8 script recreates
#              it and this script removes it, so do not run two concurrently.
#   PORT must be free at start; the script fails fast (exit 72) if anything
#              already listens on it, and only ever stops the controller-
#              anchored process groups it started, never a foreign listener.
#   WITH_RELEASE_QUALITY=1  also run npm run validate:release-quality
#   KEEP=1     keep USER_DATA and the harness TMP root after the run
#   SKIP_BUILD=1  reuse an existing dist-electron/main.js
#   APPROVED_BY / APPROVAL_REF  registration attribution strings (recorded only
#              in the disposable daemon registry; not a project-authority act)
#
# Exit status: the premerge wrapper's exit status (0 pass / 1 fail), or the
# release-quality wrapper's when WITH_RELEASE_QUALITY=1 and premerge passed.
# Teardown preserves an incoming nonzero status and returns 74 when the proof
# passed but any cleanup command or post-cleanup invariant failed.
set -euo pipefail

REPO_ROOT="${REPO_ROOT:-$(git rev-parse --show-toplevel)}"
WORKING_ROOT="$REPO_ROOT/projects/chirality-app-dev"
FRONTEND="$WORKING_ROOT/frontend"
RUN_ROOT="${RUN_ROOT:?set RUN_ROOT to an absolute disposable directory}"
PORT="${PORT:-51840}"
WITH_RELEASE_QUALITY="${WITH_RELEASE_QUALITY:-0}"
KEEP="${KEEP:-0}"
SKIP_BUILD="${SKIP_BUILD:-0}"
APPROVED_BY="${APPROVED_BY:-rerun-section8-local}"
APPROVAL_REF="${APPROVAL_REF:-DEL-09-01-V3-01}"

mkdir -p "$RUN_ROOT/logs" "$RUN_ROOT/artifacts" "$RUN_ROOT/private"
LOGS="$RUN_ROOT/logs"
ART="$RUN_ROOT/artifacts"
: > "$LOGS/driver.log"

if [ -n "${USER_DATA:-}" ]; then
  USER_DATA_CREATED=0
else
  USER_DATA="$(mktemp -d /private/tmp/chirality-s8.XXXXXX)"
  USER_DATA_CREATED=1
fi
# TMPDIR is deliberately NOT redirected under RUN_ROOT: the Vitest daemon
# integration tests (run by validate:release-quality) bind Unix sockets under
# TMPDIR and fail with `listen EINVAL` past the 104-byte macOS limit. The
# Section 8 script writes its run tree to $TMPDIR/chirality-harness-validation/
# latest; it is copied into RUN_ROOT/artifacts and removed at teardown.
HARNESS_TMP_BASE="${TMPDIR:-/tmp}"
HARNESS_TMP_ROOT="${HARNESS_TMP_BASE%/}/chirality-harness-validation/latest"

export CHIRALITY_HARNESS_PROVIDER=stub
export NEXT_TELEMETRY_DISABLED=1
# The proof's supported process contract forbids detachment. The application
# basis has one known detach route: daemon activation can spawn an unreferenced
# GUI in a new session. Disable it explicitly; a continuous controller audit
# independently fails the proof if any daemon/Next descendant changes PGID.
export CHIRALITY_DAEMON_GUI_SPAWN=0
export CHIRALITY_DAEMON_ACTIVATION_POLICY=prohibited
export HARNESS_BASE_URL="http://127.0.0.1:$PORT"
export CHIRALITY_RUNTIME_SOCKET_PATH="$USER_DATA/runtime/control.sock"
export CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE="$USER_DATA/runtime/auth/tokens/operator.token"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GROUP_CONTROLLER="$SCRIPT_DIR/section8-process-group-controller.py"
DAEMON_CONTROLLER_PID=""
DAEMON_PGID=""
DAEMON_CHILD_PID=""
DAEMON_ELECTRON_PID=""
DAEMON_AUDIT_FILE=""
NEXT_CONTROLLER_PID=""
NEXT_PGID=""
NEXT_CHILD_PID=""
NEXT_AUDIT_FILE=""
STARTED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

log() { printf '[%s] %s\n' "$(date -u +%H:%M:%S)" "$*" | tee -a "$LOGS/driver.log" >&2; }

# Each command tree runs in its own POSIX session/process group. A Python child
# is the session leader and remains alive even after its command exits. The
# parent shell does not wait/reap that controller until after group signalling,
# so its PID/PGID cannot be reallocated across the TERM/KILL boundary. Signals
# target the kernel-owned group atomically; individual descendant PIDs are
# diagnostic only and are never signal authority.
await_controller_ready() {
  local ready_file="$1"
  local controller_pid="$2"
  for _ in $(seq 1 100); do
    [ -f "$ready_file" ] && return 0
    kill -0 "$controller_pid" 2>/dev/null || return 1
    sleep 0.1
  done
  return 1
}

read_controller_ready() {
  local ready_file="$1"
  python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); print(d["controllerPid"], d["processGroupId"], d["childPid"])' "$ready_file"
}

# Validate a controller's continuously written descendant audit. Any missing,
# malformed, inspection-error, or escaped-descendant state is a hard failure.
# Individual PIDs in the audit are evidence only; they are never signal input.
assert_controller_contained() {
  local audit_file="$1"
  local controller_pid="$2"
  local process_group_id="$3"
  python3 - "$audit_file" "$controller_pid" "$process_group_id" <<'PY'
import json
import sys

path, controller, pgid = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
try:
    with open(path, encoding="utf-8") as handle:
        audit = json.load(handle)
    valid = (
        audit["schema"] == "chirality-section8-descendant-audit/v1"
        and audit["controllerPid"] == controller
        and audit["processGroupId"] == pgid
        and audit["state"] == "ok"
        and audit["violations"] == []
        and audit["samples"] > 0
        and all(item["pgid"] == pgid for item in audit["liveControlled"])
    )
except (OSError, KeyError, TypeError, ValueError):
    valid = False
raise SystemExit(0 if valid else 1)
PY
}

controller_audit_state() {
  local audit_file="$1"
  python3 -c 'import json,sys; print(json.load(open(sys.argv[1], encoding="utf-8"))["state"])' "$audit_file"
}

read_process_table() {
  ps -axo pid=,pgid= 2>/dev/null
}

inspect_process_group_members() {
  local process_group_id="$1"
  local process_table
  process_table="$(read_process_table)" || return 2
  printf '%s\n' "$process_table" | awk -v wanted="$process_group_id" '$2 == wanted { print $1 }'
}

process_group_member_count() {
  local process_group_id="$1"
  local members
  members="$(inspect_process_group_members "$process_group_id")" || return 2
  printf '%s\n' "$members" | awk 'NF { count++ } END { print count + 0 }'
}

process_group_noncontroller_count() {
  local process_group_id="$1"
  local controller_pid="$2"
  local members
  members="$(inspect_process_group_members "$process_group_id")" || return 2
  printf '%s\n' "$members" | awk -v controller="$controller_pid" 'NF && $1 != controller { count++ } END { print count + 0 }'
}

send_anchored_group_signal() {
  local controller_pid="$1"
  local process_group_id="$2"
  local signal_name="$3"
  local members
  [ -n "$controller_pid" ] && [ "$controller_pid" = "$process_group_id" ] || return 2
  if kill "-$signal_name" -- "-$process_group_id" 2>/dev/null; then
    return 0
  fi
  members="$(inspect_process_group_members "$process_group_id")" || return 2
  [ -z "$members" ] && return 0
  return 1
}

# Print a verified listener count. `lsof` returns 1 both for no matches and for
# some command failures, so first verify the inspection capability and then
# require an empty stderr for the no-match case. Return 2 means UNKNOWN/error.
inspect_port_listener_count() {
  local requested_port="$1"
  local error_file="$RUN_ROOT/private/lsof-port-${requested_port}.stderr"
  local output
  local status
  mkdir -p "$RUN_ROOT/private" || return 2
  lsof -v >/dev/null 2>&1 || return 2
  if output="$(lsof -nP -t -iTCP:"$requested_port" -sTCP:LISTEN 2>"$error_file")"; then
    status=0
  else
    status=$?
  fi
  if [ "$status" = "0" ]; then
    [ ! -s "$error_file" ] || return 2
    printf '%s\n' "$output" | awk 'NF { if ($1 !~ /^[0-9]+$/) exit 2; count++ } END { print count + 0 }'
    return $?
  fi
  if [ "$status" = "1" ] && [ -z "$output" ] && [ ! -s "$error_file" ]; then
    printf '0\n'
    return 0
  fi
  return 2
}

teardown() {
  local incoming_status=$?
  local cleanup_failed=0
  local daemon_survivors="UNKNOWN"
  local next_survivors="UNKNOWN"
  local daemon_remaining="UNKNOWN"
  local next_remaining="UNKNOWN"
  local socket_remaining=no
  local port_listener_count="UNKNOWN"
  local daemon_audit_state="NOT_STARTED"
  local next_audit_state="NOT_STARTED"
  local final_status
  trap - EXIT
  set +e
  log "teardown begin (incoming status $incoming_status)" || cleanup_failed=1
  if [ -n "$DAEMON_CONTROLLER_PID" ]; then
    daemon_audit_state="$(controller_audit_state "$DAEMON_AUDIT_FILE")" || {
      daemon_audit_state="UNKNOWN"; cleanup_failed=1;
    }
    assert_controller_contained "$DAEMON_AUDIT_FILE" "$DAEMON_CONTROLLER_PID" "$DAEMON_PGID" \
      || cleanup_failed=1
  fi
  if [ -n "$NEXT_CONTROLLER_PID" ]; then
    next_audit_state="$(controller_audit_state "$NEXT_AUDIT_FILE")" || {
      next_audit_state="UNKNOWN"; cleanup_failed=1;
    }
    assert_controller_contained "$NEXT_AUDIT_FILE" "$NEXT_CONTROLLER_PID" "$NEXT_PGID" \
      || cleanup_failed=1
  fi
  if [ -n "$NEXT_CONTROLLER_PID" ]; then
    send_anchored_group_signal "$NEXT_CONTROLLER_PID" "$NEXT_PGID" TERM || cleanup_failed=1
  fi
  if [ -n "$DAEMON_CONTROLLER_PID" ]; then
    send_anchored_group_signal "$DAEMON_CONTROLLER_PID" "$DAEMON_PGID" TERM || cleanup_failed=1
  fi
  for _ in $(seq 1 30); do
    if [ -n "$DAEMON_CONTROLLER_PID" ]; then
      daemon_survivors="$(process_group_noncontroller_count "$DAEMON_PGID" "$DAEMON_CONTROLLER_PID")" || {
        daemon_survivors="UNKNOWN"; cleanup_failed=1;
      }
    else
      daemon_survivors=0
    fi
    if [ -n "$NEXT_CONTROLLER_PID" ]; then
      next_survivors="$(process_group_noncontroller_count "$NEXT_PGID" "$NEXT_CONTROLLER_PID")" || {
        next_survivors="UNKNOWN"; cleanup_failed=1;
      }
    else
      next_survivors=0
    fi
    if [ "$daemon_survivors" = "0" ] && [ "$next_survivors" = "0" ]; then
      break
    fi
    if [ "$daemon_survivors" = "UNKNOWN" ] || [ "$next_survivors" = "UNKNOWN" ]; then break; fi
    sleep 1 || cleanup_failed=1
  done
  # Re-read after the TERM grace period. A descendant that changed group while
  # the run was live or while TERM was pending remains a permanent violation.
  if [ -n "$DAEMON_CONTROLLER_PID" ]; then
    daemon_audit_state="$(controller_audit_state "$DAEMON_AUDIT_FILE")" || {
      daemon_audit_state="UNKNOWN"; cleanup_failed=1;
    }
    assert_controller_contained "$DAEMON_AUDIT_FILE" "$DAEMON_CONTROLLER_PID" "$DAEMON_PGID" \
      || cleanup_failed=1
  fi
  if [ -n "$NEXT_CONTROLLER_PID" ]; then
    next_audit_state="$(controller_audit_state "$NEXT_AUDIT_FILE")" || {
      next_audit_state="UNKNOWN"; cleanup_failed=1;
    }
    assert_controller_contained "$NEXT_AUDIT_FILE" "$NEXT_CONTROLLER_PID" "$NEXT_PGID" \
      || cleanup_failed=1
  fi
  # The retained controller keeps each PGID allocated until this atomic KILL.
  # The group signal reaches every descendant still in the controlled group and
  # the controller itself. No individual PID is checked then signalled.
  if [ -n "$DAEMON_CONTROLLER_PID" ]; then
    send_anchored_group_signal "$DAEMON_CONTROLLER_PID" "$DAEMON_PGID" KILL || cleanup_failed=1
    wait "$DAEMON_CONTROLLER_PID" 2>/dev/null || true
  fi
  if [ -n "$NEXT_CONTROLLER_PID" ]; then
    send_anchored_group_signal "$NEXT_CONTROLLER_PID" "$NEXT_PGID" KILL || cleanup_failed=1
    wait "$NEXT_CONTROLLER_PID" 2>/dev/null || true
  fi
  for _ in $(seq 1 10); do
    if [ -n "$DAEMON_PGID" ]; then
      daemon_remaining="$(process_group_member_count "$DAEMON_PGID")" || {
        daemon_remaining="UNKNOWN"; cleanup_failed=1;
      }
    else
      daemon_remaining=0
    fi
    if [ -n "$NEXT_PGID" ]; then
      next_remaining="$(process_group_member_count "$NEXT_PGID")" || {
        next_remaining="UNKNOWN"; cleanup_failed=1;
      }
    else
      next_remaining=0
    fi
    socket_remaining=no
    [ -S "$CHIRALITY_RUNTIME_SOCKET_PATH" ] && socket_remaining=yes
    port_listener_count="$(inspect_port_listener_count "$PORT")" || {
      port_listener_count="UNKNOWN"; cleanup_failed=1;
    }
    if [ "$daemon_remaining" = "0" ] && [ "$next_remaining" = "0" ] \
       && [ "$socket_remaining" = "no" ] && [ "$port_listener_count" = "0" ]; then
      break
    fi
    if [ "$daemon_remaining" = "UNKNOWN" ] || [ "$next_remaining" = "UNKNOWN" ] \
       || [ "$port_listener_count" = "UNKNOWN" ]; then break; fi
    sleep 1 || cleanup_failed=1
  done
  if [ -n "$DAEMON_PGID" ]; then
    daemon_remaining="$(process_group_member_count "$DAEMON_PGID")" || {
      daemon_remaining="UNKNOWN"; cleanup_failed=1;
    }
  else
    daemon_remaining=0
  fi
  if [ -n "$NEXT_PGID" ]; then
    next_remaining="$(process_group_member_count "$NEXT_PGID")" || {
      next_remaining="UNKNOWN"; cleanup_failed=1;
    }
  else
    next_remaining=0
  fi
  [ -S "$CHIRALITY_RUNTIME_SOCKET_PATH" ] && socket_remaining=yes
  port_listener_count="$(inspect_port_listener_count "$PORT")" || {
    port_listener_count="UNKNOWN"; cleanup_failed=1;
  }
  [ "$daemon_remaining" = "0" ] || cleanup_failed=1
  [ "$next_remaining" = "0" ] || cleanup_failed=1
  [ "$socket_remaining" = "no" ] || cleanup_failed=1
  [ "$port_listener_count" = "0" ] || cleanup_failed=1
  [ "${RERUN_SECTION8_TEST_FORCE_CLEANUP_FAILURE:-0}" != "1" ] || cleanup_failed=1
  {
    echo "daemon_group_survivors_before_kill=$daemon_survivors"
    echo "next_group_survivors_before_kill=$next_survivors"
    echo "daemon_process_group_remaining=$daemon_remaining"
    echo "next_process_group_remaining=$next_remaining"
    echo "daemon_controller_pid=$DAEMON_CONTROLLER_PID pgid=$DAEMON_PGID"
    echo "next_controller_pid=$NEXT_CONTROLLER_PID pgid=$NEXT_PGID"
    echo "daemon_descendant_audit=$daemon_audit_state"
    echo "next_descendant_audit=$next_audit_state"
    echo "socket_present_after_stop=$socket_remaining"
    echo "port_${PORT}_listeners_after_stop=$port_listener_count"
    echo "forced_test_cleanup_failure=${RERUN_SECTION8_TEST_FORCE_CLEANUP_FAILURE:-0}"
  } > "$LOGS/teardown.txt" || cleanup_failed=1
  if [ "$KEEP" != "1" ]; then
    if [ "$USER_DATA_CREATED" = "1" ]; then
      rm -rf "$USER_DATA" || cleanup_failed=1
    fi
    rm -rf "$HARNESS_TMP_ROOT" || cleanup_failed=1
    if [ "$USER_DATA_CREATED" = "1" ] && [ -e "$USER_DATA" ]; then cleanup_failed=1; fi
    if [ -e "$HARNESS_TMP_ROOT" ]; then cleanup_failed=1; fi
    rm -rf "$RUN_ROOT/private" || cleanup_failed=1
    if [ -e "$RUN_ROOT/private" ]; then cleanup_failed=1; fi
    {
      if [ "$USER_DATA_CREATED" = "1" ]; then
        echo "user_data_removed=$([ -e "$USER_DATA" ] && echo no || echo yes) path=$USER_DATA"
      else
        echo "user_data_retained=caller-supplied path=$USER_DATA"
      fi
      echo "harness_tmp_root_removed=$([ -e "$HARNESS_TMP_ROOT" ] && echo no || echo yes) path=$HARNESS_TMP_ROOT"
      echo "private_dir_removed=$([ ! -e "$RUN_ROOT/private" ] && echo yes || echo no)"
      echo "checkout_leftovers=gitignored, intentionally not removed: $FRONTEND/artifacts/harness/** (stable artifacts; the deliverable surface) and $FRONTEND/.chirality/sessions (legacySessionRoots entry required at registration)"
    } > "$LOGS/cleanup.txt" || cleanup_failed=1
  else
    echo "KEEP=1: disposable state retained at $USER_DATA and $HARNESS_TMP_ROOT" > "$LOGS/cleanup.txt" || cleanup_failed=1
  fi
  log "teardown done (cleanup_failed=$cleanup_failed)" || cleanup_failed=1
  # Last act: the per-run manifest, so it pins the final bytes of every log
  # (including this teardown's own lines) and includes teardown.txt/cleanup.txt.
  if [ -d "$RUN_ROOT/artifacts" ] || [ -d "$RUN_ROOT/logs" ]; then
    ( cd "$RUN_ROOT" && find artifacts logs -type f 2>/dev/null | LC_ALL=C sort | xargs shasum -a 256 ) > "$RUN_ROOT/MANIFEST.sha256" || cleanup_failed=1
  else
    cleanup_failed=1
  fi
  if [ "$incoming_status" != "0" ]; then
    final_status="$incoming_status"
  elif [ "$cleanup_failed" != "0" ]; then
    final_status=74
  else
    final_status=0
  fi
  exit "$final_status"
}

# Enables the deterministic cleanup regression test to source the exact helper
# and teardown implementation without executing the runtime proof lifecycle.
if [ "${RERUN_SECTION8_LIBRARY_MODE:-0}" = "1" ]; then
  return 0 2>/dev/null || exit 0
fi
trap teardown EXIT

if [ "$CHIRALITY_DAEMON_GUI_SPAWN" != "0" ] \
   || [ "$CHIRALITY_DAEMON_ACTIVATION_POLICY" != "prohibited" ]; then
  log "required no-detach daemon policy is not active; refusing to start"; exit 69
fi

# --- precondition: port is free before any build or daemon start -------------
if ! INITIAL_PORT_LISTENER_COUNT="$(inspect_port_listener_count "$PORT")"; then
  log "could not inspect port $PORT; refusing to start"; exit 73
fi
if [ "$INITIAL_PORT_LISTENER_COUNT" != "0" ]; then
  log "port $PORT is already in use; refusing to start (set PORT to a free port)"; exit 72
fi

# --- 0. environment record ---------------------------------------------------
cd "$FRONTEND"
{
  echo "started_at=$STARTED_AT"
  echo "repo_root=$REPO_ROOT"
  echo "head=$(git -C "$REPO_ROOT" rev-parse HEAD)"
  echo "git_status_before=$(git -C "$REPO_ROOT" status --porcelain | wc -l | tr -d ' ') dirty paths"
  echo "platform=$(uname -srm)"
  echo "node=$(node --version)"
  echo "npm=$(npm --version)"
  echo "electron=$(node -p "require('electron/package.json').version")"
  echo "next=$(node -p "require('next/package.json').version")"
  echo "vitest=$(node -p "require('vitest/package.json').version")"
  echo "port=$PORT"
  echo "user_data=$USER_DATA"
  echo "user_data_created_by_script=$USER_DATA_CREATED"
  echo "tmpdir=${TMPDIR:-/tmp}"
  echo "harness_tmp_root=$HARNESS_TMP_ROOT"
  echo "CHIRALITY_HARNESS_PROVIDER=$CHIRALITY_HARNESS_PROVIDER"
  echo "HARNESS_BASE_URL=$HARNESS_BASE_URL"
  echo "CHIRALITY_RUNTIME_SOCKET_PATH=$CHIRALITY_RUNTIME_SOCKET_PATH"
  echo "CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE=$CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE"
  echo "CHIRALITY_DAEMON_GUI_SPAWN=$CHIRALITY_DAEMON_GUI_SPAWN"
  echo "CHIRALITY_DAEMON_ACTIVATION_POLICY=$CHIRALITY_DAEMON_ACTIVATION_POLICY"
  echo "with_release_quality=$WITH_RELEASE_QUALITY"
  echo "daemon_switches=--use-mock-keychain --user-data-dir=<USER_DATA> --runtime-daemon"
  echo "process_lifecycle=retained POSIX session/process-group controllers plus continuous stable-identity descendant audit; detachment fails closed; no individual PID signalling"
} > "$LOGS/environment.txt"
git -C "$REPO_ROOT" status --porcelain > "$LOGS/git-status-before.txt" || true

# --- 1. build runtime host + CLI ----------------------------------------------
if [ "$SKIP_BUILD" != "1" ] || [ ! -f dist-electron/main.js ]; then
  log "npm run build:electron"
  npm run build:electron > "$LOGS/build-electron.log" 2>&1
fi
shasum -a 256 dist-electron/main.js dist-runtime/chirality-cli.mjs > "$LOGS/built-bundles.sha256"

# legacySessionRoots entry must exist at registration (gitignored; same as CI)
mkdir -p "$FRONTEND/.chirality/sessions"

# --- 2. daemon ----------------------------------------------------------------
mkdir -p "$USER_DATA"
log "starting runtime daemon under $USER_DATA"
# --use-mock-keychain: the unsigned development Electron.app otherwise blocks
# forever inside safeStorage.isEncryptionAvailable() on the macOS Keychain
# "Safe Storage" item (a prompt a headless daemon cannot show), which wedges the
# daemon on its first session/create. The disposable evidence daemon must never
# touch the operator's real Keychain; CI's Linux runner has no real keychain
# either, so the switch keeps the evidence class identical. Chromium consumes
# the switch; product code is unchanged.
DAEMON_READY_FILE="$RUN_ROOT/private/daemon-controller-ready.json"
DAEMON_AUDIT_FILE="$LOGS/daemon-descendant-audit.json"
python3 "$GROUP_CONTROLLER" --ready-file "$DAEMON_READY_FILE" --audit-file "$DAEMON_AUDIT_FILE" -- \
  ./node_modules/.bin/electron --use-mock-keychain "--user-data-dir=$USER_DATA" \
  dist-electron/main.js --runtime-daemon > "$LOGS/daemon.log" 2>&1 &
DAEMON_CONTROLLER_PID=$!
await_controller_ready "$DAEMON_READY_FILE" "$DAEMON_CONTROLLER_PID" || {
  log "runtime-daemon process-group controller did not become ready"; exit 70;
}
read -r ready_controller ready_pgid DAEMON_CHILD_PID <<< "$(read_controller_ready "$DAEMON_READY_FILE")"
if [ "$ready_controller" != "$DAEMON_CONTROLLER_PID" ] || [ "$ready_pgid" != "$DAEMON_CONTROLLER_PID" ]; then
  log "runtime-daemon controller identity/PGID mismatch"; exit 70
fi
DAEMON_PGID="$ready_pgid"
for _ in $(seq 1 100); do
  [ -f "$DAEMON_AUDIT_FILE" ] && break
  sleep 0.1
done
assert_controller_contained "$DAEMON_AUDIT_FILE" "$DAEMON_CONTROLLER_PID" "$DAEMON_PGID" || {
  log "runtime-daemon descendant audit did not establish containment"; exit 70;
}
for _ in $(seq 1 90); do
  if [ -S "$CHIRALITY_RUNTIME_SOCKET_PATH" ] && [ -f "$CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE" ]; then
    break
  fi
  sleep 1
done
if [ ! -S "$CHIRALITY_RUNTIME_SOCKET_PATH" ] || [ ! -f "$CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE" ]; then
  log "daemon did not become ready"; exit 70
fi
# The controller's direct child is the node shim; the Electron process that
# actually owns the socket is another group member. Observe that exact owner.
DAEMON_ELECTRON_PID="$(lsof -nP -t "$CHIRALITY_RUNTIME_SOCKET_PATH" 2>/dev/null | head -n 1 || true)"
[ -n "$DAEMON_ELECTRON_PID" ] || { log "could not inspect daemon socket owner"; exit 70; }
log "daemon ready (controller/pgid $DAEMON_PGID, child $DAEMON_CHILD_PID, electron pid $DAEMON_ELECTRON_PID)"

# --- 3. register the project -------------------------------------------------
CHIRALITY_RUNTIME_TOKEN_FILE="$CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE" \
  node dist-runtime/chirality-cli.mjs project register \
    --manifest "$WORKING_ROOT/chirality.project.json" \
    --approved-by "$APPROVED_BY" \
    --approval-reference "$APPROVAL_REF" \
    --json > "$RUN_ROOT/private/registration.json"
PROJECT_TOKEN_FILE="$(node -e 'const v=JSON.parse(require("fs").readFileSync(process.argv[1],"utf8")); if(!v.tokenFile) process.exit(1); process.stdout.write(v.tokenFile)' "$RUN_ROOT/private/registration.json")"
# Only the token-file PATH and non-secret registration fields are retained.
node -e 'const v=JSON.parse(require("fs").readFileSync(process.argv[1],"utf8")); const keep={}; for (const k of Object.keys(v)) { if (/token$|secret|credential/i.test(k) && k!=="tokenFile") continue; keep[k]=v[k]; } process.stdout.write(JSON.stringify(keep,null,2)+"\n")' \
  "$RUN_ROOT/private/registration.json" > "$LOGS/registration.redacted.json"
export CHIRALITY_RUNTIME_TOKEN_FILE="$PROJECT_TOKEN_FILE"
export CHIRALITY_RUNTIME_PROJECT_ID=chirality-app-dev
export CHIRALITY_RUNTIME_PROJECT_ROOT="$WORKING_ROOT"
export HARNESS_PROJECT_ROOT="$WORKING_ROOT"
log "project registered; token file $PROJECT_TOKEN_FILE"

# --- 4. dev server bound to the daemon ---------------------------------------
log "starting next dev on $HARNESS_BASE_URL"
NEXT_READY_FILE="$RUN_ROOT/private/next-controller-ready.json"
NEXT_AUDIT_FILE="$LOGS/next-descendant-audit.json"
python3 "$GROUP_CONTROLLER" --ready-file "$NEXT_READY_FILE" --audit-file "$NEXT_AUDIT_FILE" -- \
  npm run dev:next -- --hostname 127.0.0.1 --port "$PORT" > "$LOGS/next-dev.log" 2>&1 &
NEXT_CONTROLLER_PID=$!
await_controller_ready "$NEXT_READY_FILE" "$NEXT_CONTROLLER_PID" || {
  log "Next process-group controller did not become ready"; exit 71;
}
read -r ready_controller ready_pgid NEXT_CHILD_PID <<< "$(read_controller_ready "$NEXT_READY_FILE")"
if [ "$ready_controller" != "$NEXT_CONTROLLER_PID" ] || [ "$ready_pgid" != "$NEXT_CONTROLLER_PID" ]; then
  log "Next controller identity/PGID mismatch"; exit 71
fi
NEXT_PGID="$ready_pgid"
for _ in $(seq 1 100); do
  [ -f "$NEXT_AUDIT_FILE" ] && break
  sleep 0.1
done
assert_controller_contained "$NEXT_AUDIT_FILE" "$NEXT_CONTROLLER_PID" "$NEXT_PGID" || {
  log "Next descendant audit did not establish containment"; exit 71;
}
READY=0
for _ in $(seq 1 90); do
  status="$(curl -sS -o "$LOGS/harness-ready.json" -w "%{http_code}" --get \
    --data-urlencode "projectRoot=$HARNESS_PROJECT_ROOT" \
    "$HARNESS_BASE_URL/api/harness/session/list" || true)"
  if [ "$status" = "200" ]; then READY=1; break; fi
  sleep 2
done
if [ "$READY" != "1" ]; then log "harness API did not become ready"; exit 71; fi
log "harness API ready (controller/pgid $NEXT_PGID, child $NEXT_CHILD_PID)"

# --- 5. containment observations (before) ------------------------------------
DAEMON_GROUP_MEMBERS_BEFORE="$(inspect_process_group_members "$DAEMON_PGID")" || {
  log "could not inspect daemon process group before validation"; exit 70;
}
assert_controller_contained "$DAEMON_AUDIT_FILE" "$DAEMON_CONTROLLER_PID" "$DAEMON_PGID" || {
  log "daemon descendant left its anchored group before validation"; exit 70;
}
assert_controller_contained "$NEXT_AUDIT_FILE" "$NEXT_CONTROLLER_PID" "$NEXT_PGID" || {
  log "Next descendant left its anchored group before validation"; exit 71;
}
lsof -v >/dev/null 2>&1 || { log "lsof inspection unavailable"; exit 70; }
{
  echo "# daemon electron pid $DAEMON_ELECTRON_PID (controller/pgid $DAEMON_PGID) — TCP sockets (expect none):"
  lsof -nP -a -p "$DAEMON_ELECTRON_PID" -iTCP 2>/dev/null || true
  echo "# daemon electron pid $DAEMON_ELECTRON_PID — Unix sockets under the disposable user-data root:"
  lsof -nP -a -p "$DAEMON_ELECTRON_PID" -U 2>/dev/null | grep -F "$USER_DATA" || true
  echo "# all TCP listeners owned by daemon process-group members (expect none):"
  while IFS= read -r process_id; do
    [ -n "$process_id" ] || continue
    lsof -nP -a -p "$process_id" -iTCP -sTCP:LISTEN 2>/dev/null | tail -n +2 || true
  done <<< "$DAEMON_GROUP_MEMBERS_BEFORE"
  echo "# control socket mode:"
  ls -l "$CHIRALITY_RUNTIME_SOCKET_PATH"
  echo "# runtime directory mode:"
  ls -ld "$USER_DATA/runtime"
  echo "# listeners on port $PORT (expect the next dev server only):"
  lsof -nP -iTCP:"$PORT" -sTCP:LISTEN 2>/dev/null || true
} > "$LOGS/containment-before.txt"

# --- 6. premerge --------------------------------------------------------------
set +e
log "npm run harness:validate:premerge"
npm run harness:validate:premerge > "$LOGS/premerge.stdout.log" 2> "$LOGS/premerge.stderr.log"
PREMERGE_EXIT=$?
set -e
log "premerge exit $PREMERGE_EXIT"
grep -E '^HARNESS_' "$LOGS/premerge.stdout.log" > "$LOGS/premerge.machine-lines.txt" || true

mkdir -p "$ART/section8-run" "$ART/stable"
if [ -f artifacts/harness/section8/latest/summary.json ]; then
  cp artifacts/harness/section8/latest/summary.json "$ART/stable/section8-latest-summary.json"
fi
if [ -f artifacts/harness/section9/latest/summary.json ]; then
  cp artifacts/harness/section9/latest/summary.json "$ART/stable/section9-latest-summary.json"
fi
if [ -f artifacts/harness/section9/latest/manifest.json ]; then
  cp artifacts/harness/section9/latest/manifest.json "$ART/stable/section9-latest-manifest.json"
fi
if [ -d "$HARNESS_TMP_ROOT" ]; then
  for d in api sse logs cleanup; do
    if [ -d "$HARNESS_TMP_ROOT/$d" ]; then
      rm -rf "$ART/section8-run/$d"
      cp -R "$HARNESS_TMP_ROOT/$d" "$ART/section8-run/$d"
    fi
  done
  [ -f "$HARNESS_TMP_ROOT/summary.json" ] && cp "$HARNESS_TMP_ROOT/summary.json" "$ART/section8-run/summary.json"
fi

# --- 7. optional release-quality wrapper --------------------------------------
RQ_EXIT=""
if [ "$WITH_RELEASE_QUALITY" = "1" ]; then
  set +e
  log "npm run validate:release-quality"
  npm run validate:release-quality > "$LOGS/release-quality.stdout.log" 2> "$LOGS/release-quality.stderr.log"
  RQ_EXIT=$?
  set -e
  log "release-quality exit $RQ_EXIT"
  grep -E '^RELEASE_QUALITY_' "$LOGS/release-quality.stdout.log" > "$LOGS/release-quality.machine-lines.txt" || true
  if [ -d artifacts/harness/release-quality/latest ]; then
    mkdir -p "$ART/release-quality"
    cp artifacts/harness/release-quality/latest/summary.json "$ART/release-quality/summary.json"
    [ -d artifacts/harness/release-quality/latest/logs ] && cp -R artifacts/harness/release-quality/latest/logs "$ART/release-quality/logs"
  fi
  # the wrapper re-runs premerge and rewrites the stable artifact; retain that copy too
  if [ -f artifacts/harness/section8/latest/summary.json ]; then
    cp artifacts/harness/section8/latest/summary.json "$ART/stable/section8-latest-summary.after-release-quality.json"
  fi
fi

# --- 8. containment observations (after) -------------------------------------
DAEMON_GROUP_MEMBERS_AFTER="$(inspect_process_group_members "$DAEMON_PGID")" || {
  log "could not inspect daemon process group after validation"; exit 70;
}
assert_controller_contained "$DAEMON_AUDIT_FILE" "$DAEMON_CONTROLLER_PID" "$DAEMON_PGID" || {
  log "daemon descendant left its anchored group during validation"; exit 70;
}
assert_controller_contained "$NEXT_AUDIT_FILE" "$NEXT_CONTROLLER_PID" "$NEXT_PGID" || {
  log "Next descendant left its anchored group during validation"; exit 71;
}
lsof -v >/dev/null 2>&1 || { log "lsof inspection unavailable after validation"; exit 70; }
{
  echo "# daemon electron pid $DAEMON_ELECTRON_PID — TCP sockets after the run (expect none):"
  lsof -nP -a -p "$DAEMON_ELECTRON_PID" -iTCP 2>/dev/null || true
  echo "# TCP listeners owned by daemon process-group members after the run (expect none):"
  while IFS= read -r process_id; do
    [ -n "$process_id" ] || continue
    lsof -nP -a -p "$process_id" -iTCP -sTCP:LISTEN 2>/dev/null | tail -n +2 || true
  done <<< "$DAEMON_GROUP_MEMBERS_AFTER"
} > "$LOGS/containment-after.txt"
git -C "$REPO_ROOT" status --porcelain > "$LOGS/git-status-after.txt" || true
{
  echo "premerge_exit=$PREMERGE_EXIT"
  echo "release_quality_exit=${RQ_EXIT:-not-run}"
  echo "ended_at=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "git_status_after=$(wc -l < "$LOGS/git-status-after.txt" | tr -d ' ') dirty paths"
} > "$LOGS/result.txt"

if [ "$PREMERGE_EXIT" != "0" ]; then exit "$PREMERGE_EXIT"; fi
if [ -n "$RQ_EXIT" ]; then exit "$RQ_EXIT"; fi
exit 0
