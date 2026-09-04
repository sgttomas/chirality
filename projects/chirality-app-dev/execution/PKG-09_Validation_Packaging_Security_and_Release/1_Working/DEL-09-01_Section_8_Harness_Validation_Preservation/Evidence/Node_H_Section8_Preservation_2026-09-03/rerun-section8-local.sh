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
#   9. recursively signals both recorded process trees, removes disposable state
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
#              already listens on it, and only ever stops the dev server it
#              started (by pid), never a foreign listener.
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
export HARNESS_BASE_URL="http://127.0.0.1:$PORT"
export CHIRALITY_RUNTIME_SOCKET_PATH="$USER_DATA/runtime/control.sock"
export CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE="$USER_DATA/runtime/auth/tokens/operator.token"

DAEMON_PID=""
DAEMON_ELECTRON_PID=""
DAEMON_ROOT_IDENTITY=""
DAEMON_TREE_RECORDS=""
NEXT_PID=""
NEXT_ROOT_IDENTITY=""
NEXT_TREE_RECORDS=""
STARTED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

log() { printf '[%s] %s\n' "$(date -u +%H:%M:%S)" "$*" | tee -a "$LOGS/driver.log" >&2; }

# A process record is `<pid><TAB><identity>`, where identity hashes the process
# start timestamp, uid, and executable path. The start timestamp distinguishes
# PID reuse; the executable fingerprint prevents an unrelated same-second
# process from being accepted while remaining stable when a runtime changes its
# display title. Every signal re-reads and compares this identity immediately
# before dispatch. Tests may override these two narrow adapters after sourcing
# the script in library mode; production never does.
read_process_identity() {
  local process_id="$1"
  local identity_material
  local executable_path
  identity_material="$(ps -p "$process_id" -o lstart= -o uid= 2>/dev/null)" || return 1
  executable_path="$(lsof -a -p "$process_id" -d txt -Fn 2>/dev/null | sed -n 's/^n//p' | head -n 1)" || return 1
  [ -n "$identity_material" ] && [ -n "$executable_path" ] || return 1
  identity_material="${identity_material}"$'\n'"${executable_path}"
  printf '%s' "$identity_material" | shasum -a 256 | awk '{print $1}'
}

send_process_signal() {
  local signal_name="$1"
  local process_id="$2"
  kill "-$signal_name" "$process_id"
}

read_parent_pid() {
  local process_id="$1"
  ps -p "$process_id" -o ppid= 2>/dev/null | tr -d '[:space:]'
}

# Print identity records for every descendant of a verified parent, deepest
# first. Discovery is restricted to a parent identity already captured from a
# script-started tree; no command-line regex is used to find unrelated tasks.
descendant_identity_records() {
  local parent_pid="$1"
  local parent_identity="$2"
  local child_pid
  local child_identity
  local current_parent_identity
  current_parent_identity="$(read_process_identity "$parent_pid")" || return 0
  [ "$current_parent_identity" = "$parent_identity" ] || return 0
  while IFS= read -r child_pid; do
    [ -n "$child_pid" ] || continue
    child_identity="$(read_process_identity "$child_pid")" || continue
    current_parent_identity="$(read_process_identity "$parent_pid")" || return 0
    [ "$current_parent_identity" = "$parent_identity" ] || return 0
    [ "$(read_parent_pid "$child_pid")" = "$parent_pid" ] || continue
    descendant_identity_records "$child_pid" "$child_identity"
    [ "$(read_process_identity "$child_pid" 2>/dev/null || true)" = "$child_identity" ] || continue
    printf '%s\t%s\n' "$child_pid" "$child_identity"
  done < <(pgrep -P "$parent_pid" 2>/dev/null || true)
}

process_tree_identity_records() {
  local root_pid="$1"
  local root_identity="$2"
  [ "$(read_process_identity "$root_pid" 2>/dev/null || true)" = "$root_identity" ] || return 0
  descendant_identity_records "$root_pid" "$root_identity"
  [ "$(read_process_identity "$root_pid" 2>/dev/null || true)" = "$root_identity" ] || return 0
  printf '%s\t%s\n' "$root_pid" "$root_identity"
}

merge_identity_records() {
  awk -F '\t' 'NF >= 2 && !seen[$1 FS $2]++'
}

verified_live_identity_records() {
  local identity_records="$1"
  local process_id
  local expected_identity
  local current_identity
  while IFS=$'\t' read -r process_id expected_identity; do
    [ -n "$process_id" ] && [ -n "$expected_identity" ] || continue
    current_identity="$(read_process_identity "$process_id")" || continue
    [ "$current_identity" = "$expected_identity" ] || continue
    printf '%s\t%s\n' "$process_id" "$expected_identity"
  done <<< "$identity_records"
}

signal_identity_records() {
  local identity_records="$1"
  local signal_name="$2"
  local process_id
  local expected_identity
  local current_identity
  local failed=0
  while IFS=$'\t' read -r process_id expected_identity; do
    [ -n "$process_id" ] && [ -n "$expected_identity" ] || continue
    current_identity="$(read_process_identity "$process_id")" || continue
    [ "$current_identity" = "$expected_identity" ] || continue
    if ! send_process_signal "$signal_name" "$process_id" 2>/dev/null; then
      # A process that exited or changed identity in the final interval is no
      # longer ours and must not convert normal teardown into a false failure.
      # A still-live matching identity that could not be signalled is a real
      # cleanup failure.
      current_identity="$(read_process_identity "$process_id")" || continue
      [ "$current_identity" = "$expected_identity" ] && failed=1
    fi
  done <<< "$identity_records"
  return "$failed"
}

live_identity_count() {
  local identity_records="$1"
  verified_live_identity_records "$identity_records" | awk 'END { print NR + 0 }'
}

identity_is_live() {
  local process_id="$1"
  local expected_identity="$2"
  [ -n "$process_id" ] && [ -n "$expected_identity" ] \
    && [ "$(read_process_identity "$process_id" 2>/dev/null || true)" = "$expected_identity" ]
}

teardown() {
  local incoming_status=$?
  local cleanup_failed=0
  local daemon_survivors=""
  local next_survivors=""
  local daemon_remaining=0
  local next_remaining=0
  local socket_remaining=no
  local port_listener_count=0
  local daemon_alive=no
  local next_alive=no
  local final_status
  trap - EXIT
  set +e
  log "teardown begin (incoming status $incoming_status)" || cleanup_failed=1
  if [ -n "$NEXT_PID" ]; then
    NEXT_TREE_RECORDS="$(
      {
        printf '%s\n' "$NEXT_TREE_RECORDS"
        process_tree_identity_records "$NEXT_PID" "$NEXT_ROOT_IDENTITY"
      } | merge_identity_records
    )"
    signal_identity_records "$NEXT_TREE_RECORDS" TERM || cleanup_failed=1
  fi
  if [ -n "$DAEMON_PID" ]; then
    DAEMON_TREE_RECORDS="$(
      {
        printf '%s\n' "$DAEMON_TREE_RECORDS"
        process_tree_identity_records "$DAEMON_PID" "$DAEMON_ROOT_IDENTITY"
      } | merge_identity_records
    )"
    signal_identity_records "$DAEMON_TREE_RECORDS" TERM || cleanup_failed=1
  fi
  for _ in $(seq 1 30); do
    if [ "$(live_identity_count "$DAEMON_TREE_RECORDS")" = "0" ] \
       && [ "$(live_identity_count "$NEXT_TREE_RECORDS")" = "0" ]; then
      break
    fi
    sleep 1 || cleanup_failed=1
  done
  # A daemon or dev server wedged on a blocking host call may ignore SIGTERM.
  # Derive KILL targets only from identity-verified survivors after the grace
  # period, then revalidate each identity immediately before its KILL signal.
  # A stale or PID-reused record is therefore never signalled.
  daemon_survivors="$(verified_live_identity_records "$DAEMON_TREE_RECORDS")"
  next_survivors="$(verified_live_identity_records "$NEXT_TREE_RECORDS")"
  signal_identity_records "$daemon_survivors" KILL || cleanup_failed=1
  signal_identity_records "$next_survivors" KILL || cleanup_failed=1
  for _ in $(seq 1 10); do
    daemon_remaining="$(live_identity_count "$DAEMON_TREE_RECORDS")"
    next_remaining="$(live_identity_count "$NEXT_TREE_RECORDS")"
    socket_remaining=no
    [ -S "$CHIRALITY_RUNTIME_SOCKET_PATH" ] && socket_remaining=yes
    port_listener_count="$(lsof -nP -iTCP:"$PORT" -sTCP:LISTEN 2>/dev/null | tail -n +2 | wc -l | tr -d ' ')"
    if [ "$daemon_remaining" = "0" ] && [ "$next_remaining" = "0" ] \
       && [ "$socket_remaining" = "no" ] && [ "$port_listener_count" = "0" ]; then
      break
    fi
    sleep 1 || cleanup_failed=1
  done
  daemon_remaining="$(live_identity_count "$DAEMON_TREE_RECORDS")"
  next_remaining="$(live_identity_count "$NEXT_TREE_RECORDS")"
  identity_is_live "$DAEMON_PID" "$DAEMON_ROOT_IDENTITY" && daemon_alive=yes
  identity_is_live "$NEXT_PID" "$NEXT_ROOT_IDENTITY" && next_alive=yes
  [ -S "$CHIRALITY_RUNTIME_SOCKET_PATH" ] && socket_remaining=yes
  port_listener_count="$(lsof -nP -iTCP:"$PORT" -sTCP:LISTEN 2>/dev/null | tail -n +2 | wc -l | tr -d ' ')"
  [ "$daemon_remaining" = "0" ] || cleanup_failed=1
  [ "$next_remaining" = "0" ] || cleanup_failed=1
  [ "$daemon_alive" = "no" ] || cleanup_failed=1
  [ "$next_alive" = "no" ] || cleanup_failed=1
  [ "$socket_remaining" = "no" ] || cleanup_failed=1
  [ "$port_listener_count" = "0" ] || cleanup_failed=1
  [ "${RERUN_SECTION8_TEST_FORCE_CLEANUP_FAILURE:-0}" != "1" ] || cleanup_failed=1
  {
    echo "daemon_process_tree_remaining=$daemon_remaining"
    echo "next_process_tree_remaining=$next_remaining"
    echo "daemon_pid=$DAEMON_PID identity_alive=$daemon_alive"
    echo "next_pid=$NEXT_PID identity_alive=$next_alive"
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

# --- precondition: port is free before any build or daemon start -------------
if [ -n "$(lsof -nP -t -iTCP:"$PORT" -sTCP:LISTEN 2>/dev/null)" ]; then
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
  echo "with_release_quality=$WITH_RELEASE_QUALITY"
  echo "daemon_switches=--use-mock-keychain --user-data-dir=<USER_DATA> --runtime-daemon"
  echo "process_matching=recorded pid + start/uid/executable identity trees"
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
nohup ./node_modules/.bin/electron --use-mock-keychain "--user-data-dir=$USER_DATA" \
  dist-electron/main.js --runtime-daemon > "$LOGS/daemon.log" 2>&1 &
DAEMON_PID=$!
DAEMON_ROOT_IDENTITY="$(read_process_identity "$DAEMON_PID")" || {
  log "could not capture runtime-daemon root identity"; exit 70;
}
DAEMON_TREE_RECORDS="${DAEMON_PID}"$'\t'"${DAEMON_ROOT_IDENTITY}"
for _ in $(seq 1 90); do
  if [ -S "$CHIRALITY_RUNTIME_SOCKET_PATH" ] && [ -f "$CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE" ]; then
    break
  fi
  sleep 1
done
if [ ! -S "$CHIRALITY_RUNTIME_SOCKET_PATH" ] || [ ! -f "$CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE" ]; then
  log "daemon did not become ready"; exit 70
fi
# $DAEMON_PID is the node shim in node_modules/.bin/electron; the Electron
# process that actually owns the socket is its child. Observe that one.
DAEMON_TREE_RECORDS="$(
  {
    printf '%s\n' "$DAEMON_TREE_RECORDS"
    process_tree_identity_records "$DAEMON_PID" "$DAEMON_ROOT_IDENTITY"
  } | merge_identity_records
)"
DAEMON_ELECTRON_PID="$(lsof -nP -t "$CHIRALITY_RUNTIME_SOCKET_PATH" 2>/dev/null | head -n 1 || true)"
log "daemon ready (shim pid $DAEMON_PID, electron pid ${DAEMON_ELECTRON_PID:-unknown})"

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
nohup npm run dev:next -- --hostname 127.0.0.1 --port "$PORT" > "$LOGS/next-dev.log" 2>&1 &
NEXT_PID=$!
NEXT_ROOT_IDENTITY="$(read_process_identity "$NEXT_PID")" || {
  log "could not capture Next root identity"; exit 71;
}
NEXT_TREE_RECORDS="$(process_tree_identity_records "$NEXT_PID" "$NEXT_ROOT_IDENTITY" | merge_identity_records)"
READY=0
for _ in $(seq 1 90); do
  status="$(curl -sS -o "$LOGS/harness-ready.json" -w "%{http_code}" --get \
    --data-urlencode "projectRoot=$HARNESS_PROJECT_ROOT" \
    "$HARNESS_BASE_URL/api/harness/session/list" || true)"
  if [ "$status" = "200" ]; then READY=1; break; fi
  sleep 2
done
if [ "$READY" != "1" ]; then log "harness API did not become ready"; exit 71; fi
NEXT_TREE_RECORDS="$(
  {
    printf '%s\n' "$NEXT_TREE_RECORDS"
    process_tree_identity_records "$NEXT_PID" "$NEXT_ROOT_IDENTITY"
  } | merge_identity_records
)"
log "harness API ready"

# --- 5. containment observations (before) ------------------------------------
{
  echo "# daemon electron pid ${DAEMON_ELECTRON_PID:-unknown} (shim $DAEMON_PID) — TCP sockets (expect none):"
  lsof -nP -a -p "${DAEMON_ELECTRON_PID:-$DAEMON_PID}" -iTCP 2>/dev/null || true
  echo "# daemon electron pid ${DAEMON_ELECTRON_PID:-unknown} — Unix sockets under the disposable user-data root:"
  lsof -nP -a -p "${DAEMON_ELECTRON_PID:-$DAEMON_PID}" -U 2>/dev/null | grep -F "$USER_DATA" || true
  echo "# all TCP listeners owned by any process under the disposable user-data root (expect none):"
  while IFS=$'\t' read -r process_id _; do
    [ -n "$process_id" ] || continue
    lsof -nP -a -p "$process_id" -iTCP -sTCP:LISTEN 2>/dev/null | tail -n +2 || true
  done <<< "$DAEMON_TREE_RECORDS"
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
{
  echo "# daemon electron pid ${DAEMON_ELECTRON_PID:-unknown} — TCP sockets after the run (expect none):"
  lsof -nP -a -p "${DAEMON_ELECTRON_PID:-$DAEMON_PID}" -iTCP 2>/dev/null || true
  echo "# TCP listeners owned by any process under the disposable user-data root after the run (expect none):"
  while IFS=$'\t' read -r process_id _; do
    [ -n "$process_id" ] || continue
    lsof -nP -a -p "$process_id" -iTCP -sTCP:LISTEN 2>/dev/null | tail -n +2 || true
  done <<< "$DAEMON_TREE_RECORDS"
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
