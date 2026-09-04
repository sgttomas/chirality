#!/usr/bin/env bash
# rerun-section8-local.sh — bounded local rerun of the Section 8 premerge
# evidence under the shared-runtime binding lifecycle that
# .github/workflows/harness-premerge.yml performs in CI.
#
# What it does (mirrors the workflow step for step, on macOS without xvfb):
#   1. builds the Electron runtime host + bundled CLI (npm run build:electron)
#   2. starts dist-electron/main.js --runtime-daemon under a DISPOSABLE
#      --user-data-dir (never the operator's real userData / LaunchAgent daemon)
#      with Chromium's --use-mock-keychain so the dev binary never blocks on the
#      operator's macOS Keychain (see the comment at the launch line)
#   3. registers projects/chirality-app-dev/chirality.project.json with that
#      daemon through dist-runtime/chirality-cli.mjs project register
#   4. starts `next dev` bound to the daemon (CHIRALITY_RUNTIME_* env)
#   5. waits for /api/harness/session/list readiness
#   6. runs `npm run harness:validate:premerge` (Section 8 + report-only Section 9)
#      and, with WITH_RELEASE_QUALITY=1, `npm run validate:release-quality`
#   7. records containment observations (daemon listeners, socket mode, git status)
#   8. tears both processes down and removes the disposable state (KEEP=1 keeps it)
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
#              <userData>/runtime/control.sock from it
#   WITH_RELEASE_QUALITY=1  also run npm run validate:release-quality
#   KEEP=1     keep USER_DATA and the harness TMP root after the run
#   SKIP_BUILD=1  reuse an existing dist-electron/main.js
#   APPROVED_BY / APPROVAL_REF  registration attribution strings (recorded only
#              in the disposable daemon registry; not a project-authority act)
#
# Exit status: the premerge wrapper's exit status (0 pass / 1 fail), or the
# release-quality wrapper's when WITH_RELEASE_QUALITY=1 and premerge passed.
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

USER_DATA="${USER_DATA:-$(mktemp -d /private/tmp/chirality-s8.XXXXXX)}"
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
NEXT_PID=""
STARTED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

log() { printf '[%s] %s\n' "$(date -u +%H:%M:%S)" "$*" | tee -a "$LOGS/driver.log" >&2; }

teardown() {
  local status=$?
  set +e
  log "teardown begin (status so far $status)"
  if [ -n "$NEXT_PID" ]; then
    kill "$NEXT_PID" 2>/dev/null; pkill -P "$NEXT_PID" 2>/dev/null
  fi
  if [ -n "$DAEMON_PID" ]; then
    kill "$DAEMON_PID" 2>/dev/null
  fi
  for _ in $(seq 1 30); do
    if ! { [ -n "$DAEMON_PID" ] && kill -0 "$DAEMON_PID" 2>/dev/null; } \
       && ! { [ -n "$NEXT_PID" ] && kill -0 "$NEXT_PID" 2>/dev/null; }; then
      break
    fi
    sleep 1
  done
  # A daemon wedged on a blocking host call ignores SIGTERM; never leave it behind.
  for p in $(pgrep -f -- "--user-data-dir=$USER_DATA" 2>/dev/null); do kill -9 "$p" 2>/dev/null || true; done
  [ -n "$NEXT_PID" ] && kill -9 "$NEXT_PID" 2>/dev/null || true
  for p in $(lsof -nP -t -iTCP:"$PORT" -sTCP:LISTEN 2>/dev/null); do kill -9 "$p" 2>/dev/null || true; done
  sleep 1
  {
    echo "daemon_process_tree_remaining=$(pgrep -f -- "--user-data-dir=$USER_DATA" 2>/dev/null | wc -l | tr -d ' ')"
    echo "daemon_pid=$DAEMON_PID alive=$([ -n "$DAEMON_PID" ] && kill -0 "$DAEMON_PID" 2>/dev/null && echo yes || echo no)"
    echo "next_pid=$NEXT_PID alive=$([ -n "$NEXT_PID" ] && kill -0 "$NEXT_PID" 2>/dev/null && echo yes || echo no)"
    echo "socket_present_after_stop=$([ -S "$CHIRALITY_RUNTIME_SOCKET_PATH" ] && echo yes || echo no)"
    echo "port_${PORT}_listeners_after_stop=$(lsof -nP -iTCP:"$PORT" -sTCP:LISTEN 2>/dev/null | tail -n +2 | wc -l | tr -d ' ')"
  } > "$LOGS/teardown.txt"
  if [ "$KEEP" != "1" ]; then
    rm -rf "$USER_DATA" "$HARNESS_TMP_ROOT"
    {
      echo "user_data_removed=$([ -e "$USER_DATA" ] && echo no || echo yes) path=$USER_DATA"
      echo "harness_tmp_root_removed=$([ -e "$HARNESS_TMP_ROOT" ] && echo no || echo yes) path=$HARNESS_TMP_ROOT"
      echo "private_dir_removed=$(rm -rf "$RUN_ROOT/private" && [ ! -e "$RUN_ROOT/private" ] && echo yes || echo no)"
    } > "$LOGS/cleanup.txt"
  else
    echo "KEEP=1: disposable state retained at $USER_DATA and $HARNESS_TMP_ROOT" > "$LOGS/cleanup.txt"
  fi
  log "teardown done"
}
trap teardown EXIT

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
  echo "tmpdir=${TMPDIR:-/tmp}"
  echo "harness_tmp_root=$HARNESS_TMP_ROOT"
  echo "CHIRALITY_HARNESS_PROVIDER=$CHIRALITY_HARNESS_PROVIDER"
  echo "HARNESS_BASE_URL=$HARNESS_BASE_URL"
  echo "CHIRALITY_RUNTIME_SOCKET_PATH=$CHIRALITY_RUNTIME_SOCKET_PATH"
  echo "CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE=$CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE"
  echo "with_release_quality=$WITH_RELEASE_QUALITY"
  echo "daemon_switches=--use-mock-keychain --user-data-dir=<USER_DATA> --runtime-daemon"
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
DAEMON_ELECTRON_PID="$(pgrep -f -- "Electron --use-mock-keychain --user-data-dir=$USER_DATA dist-electron/main.js --runtime-daemon" | head -n 1 || true)"
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
READY=0
for _ in $(seq 1 90); do
  status="$(curl -sS -o "$LOGS/harness-ready.json" -w "%{http_code}" --get \
    --data-urlencode "projectRoot=$HARNESS_PROJECT_ROOT" \
    "$HARNESS_BASE_URL/api/harness/session/list" || true)"
  if [ "$status" = "200" ]; then READY=1; break; fi
  sleep 2
done
if [ "$READY" != "1" ]; then log "harness API did not become ready"; exit 71; fi
log "harness API ready"

# --- 5. containment observations (before) ------------------------------------
{
  echo "# daemon electron pid ${DAEMON_ELECTRON_PID:-unknown} (shim $DAEMON_PID) — TCP sockets (expect none):"
  lsof -nP -a -p "${DAEMON_ELECTRON_PID:-$DAEMON_PID}" -iTCP 2>/dev/null || true
  echo "# daemon electron pid ${DAEMON_ELECTRON_PID:-unknown} — Unix sockets under the disposable user-data root:"
  lsof -nP -a -p "${DAEMON_ELECTRON_PID:-$DAEMON_PID}" -U 2>/dev/null | grep -F "$USER_DATA" || true
  echo "# all TCP listeners owned by any process under the disposable user-data root (expect none):"
  for p in $(pgrep -f -- "--user-data-dir=$USER_DATA" 2>/dev/null); do lsof -nP -a -p "$p" -iTCP -sTCP:LISTEN 2>/dev/null | tail -n +2 || true; done
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
    [ -d "$HARNESS_TMP_ROOT/$d" ] && cp -R "$HARNESS_TMP_ROOT/$d" "$ART/section8-run/$d"
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
  for p in $(pgrep -f -- "--user-data-dir=$USER_DATA" 2>/dev/null); do lsof -nP -a -p "$p" -iTCP -sTCP:LISTEN 2>/dev/null | tail -n +2 || true; done
} > "$LOGS/containment-after.txt"
git -C "$REPO_ROOT" status --porcelain > "$LOGS/git-status-after.txt" || true
{
  echo "premerge_exit=$PREMERGE_EXIT"
  echo "release_quality_exit=${RQ_EXIT:-not-run}"
  echo "ended_at=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "git_status_after=$(wc -l < "$LOGS/git-status-after.txt" | tr -d ' ') dirty paths"
} > "$LOGS/result.txt"

( cd "$RUN_ROOT" && find artifacts logs -type f | LC_ALL=C sort | xargs shasum -a 256 ) > "$RUN_ROOT/MANIFEST.sha256"

if [ "$PREMERGE_EXIT" != "0" ]; then exit "$PREMERGE_EXIT"; fi
if [ -n "$RQ_EXIT" ]; then exit "$RQ_EXIT"; fi
exit 0
