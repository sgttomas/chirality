# R20 — R19 failure record, cleanup-parser repair, offline rebuild, and staged login proof

- Date: `2026-08-23`
- Run: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`
- Exact build / proof revision: `cb008dc5d6aa9b249639c91f3453a18609530d0f`
- Parent: `a702dd6ec5005b361c8c023b12b599a425e5e2b8`
- Frontend tree: `b4c73edda1fe3346815ce75449b2327c80c79bf8`
- Branch: `codex/app-login-proof-r20-repair`
- Result: `R19 EXECUTED AND FAILED (OWNER-REPORTED); REPAIR/OFFLINE BUILD/PRECHECK PASS; R20 STAGED ONLY AND NOT EXECUTED`
- Deliverable state: `IN_PROGRESS`, unproved

## Claim boundary

R19 remains executed-and-failed and is not upgraded. R20 is documentation-only staging bound to the exact source commit and one ignored unsigned local arm64 package. No R20 procedure block ran in this tranche. No proof acceptance, lifecycle, release-readiness, reliance, signing, notarization, distribution, publication, issuance, or professional-approval claim is made. No GUI, logout/login, LaunchAgent/plist, bootstrap, kickstart, default-operator query/mutation, or proof capture occurred.

## R19 executed-and-failed — owner-reported facts only

The following facts are transcribed from the owner direction and were not authenticated by reading, listing, traversing, or statting the owner Desktop evidence or prior private root:

- The owner ran Step 0, Step 1, the prepared check, one logout/login, and capture on `2026-08-23`; capture timestamp `2026-08-23T08:15:26.231Z`.
- R19 package executable SHA-256 `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`; `PROOF_REVISION=d6861ae8251e2a81078577d4496e949735ff199d`; label `com.chirality.ci.runatload.login.owner.macos26.r19.3951dfe9-ec03-421b-b376-fd5f0d96992b`; root `/private/tmp/ch-r18-91499728-51dd`.
- Steps 0–1b passed exactly. Capture exited nonzero with `Loaded cleanup job last exit code is invalid`.
- Owner-reported `summary.json` status was `FAIL`. Every proof assertion was true: `preparedJobAbsent`, `loginDiscoveredJobObserved`, `loadedProgramMatches`, `loadedArgumentsMatch`, `identityTransitionObserved`, `pidObserved`, `executableIdentityMatches`, and all `defaultProtection` assertions. `bootstrapInvoked=false` and `kickstartInvoked=false`.
- Owner-reported cleanup fields: `jobMutationRefused=true`, `jobAbsent=false`, `processAbsent=false`, `plistAbsent=true`, `runtimeDataRemoved=true`.
- The owner reports three failed-evidence files, each mode `0600`, preserved under `/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r19-3951dfe9-ec03-421b-b376-fd5f0d96992b-failed-evidence`: `prepared.json` SHA-256 `06081eae6e918b264365787f4e6d3555ba7bd53cb903c6c59852fbf3fad7f1e7`; `summary.json` SHA-256 `7b91f8b81076a1349d70f8133bda0b23508dad67571366a5b313032f3944843f`; `evidence-package.json` SHA-256 `17251922acf6a939d6420ccbece4143f51e5b597ff4b220573e608636451966d`.
- The owner reports manually running `/bin/launchctl bootout gui/501/com.chirality.ci.runatload.login.owner.macos26.r19.3951dfe9-ec03-421b-b376-fd5f0d96992b` after a program-path guard. The raw command output was promised but was not supplied; this record does not reconstruct it.
- The owner reports that afterward exact proof-service `launchctl print` exited 113, `pgrep -f 'worktrees/ef5e/.*Chirality --runtime-daemon'` was empty, no R19 plist remained under `~/Library/LaunchAgents`, and the private root had been removed by the owner.
- The owner reports operator daemon `com.chirality.runtime` PID 34917, started `2026-08-23 02:15:06` local, `runs = 1`, `last exit code = (never exited)`. The owner attributes that ordinary restart to the logout/login GUI-session recycle, not a harness act, and reports its plist bytes and loaded state unchanged with `defaultProtection` true. This is a second owner-reported observation of the macOS 26 output form, not an agent query of the operator surface.

R19 is `EXECUTED AND FAILED`; DEL-09-04 remains `IN_PROGRESS` and unproved.

## Independently confirmed repair basis

The exact repository fixture is a regular 3,049-byte file with SHA-256 `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531`. Current source and focused tests independently establish that it parses as state `running`, PID `34924`, runs `1`, `lastExitCode=undefined`, and `neverExited=true`. The pre-repair integer-only cleanup parser rejected the exact `(never exited)` sentinel before exact-owned bootout, and destructive cleanup could then remove plist/runtime diagnostics while the job/process remained.

Exact source commit `cb008dc5d6aa9b249639c91f3453a18609530d0f` implements the bounded repair: only exact `(never exited)` is accepted as a first-class state; all other noninteger/empty forms fail closed; exact-owned running PID/runs-1/never-exited proceeds to bootout; destructive cleanup is refused if mutation was refused, the job remains loaded, or an observed proof process remains alive; and every non-PASS capture preserves both token-cleared daemon logs before any allowed runtime removal, otherwise retaining private runtime state. Source review passed with no actionable finding.

## One-shot offline build and package identity

`npm run electron:supply-chain` ran exactly once and exited 0, verifying `/Users/ryan/Library/Caches/chirality/electron-dist`. `npm run desktop:pack` then ran exactly once in the ordinary network-denied sandbox and exited 0 without escalation or retry. Its complete normalized 15,852-byte log has SHA-256 `d462b1efa4ab63a400b8e2efc96bd3b59a8eb9a0e173a6ff887aa9cb6f9fbdd2`, contains the exact custom `electronDist` line once, contains no case-insensitive download/GitHub/release-assets indicator, and records dependency-boundary `PASS` plus instruction-root `pass` for 43 files at the exact revision.

Package: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app`.

| Check | Exact observation |
|---|---|
| bundle ID | `com.chirality.app` |
| short / bundle version | `2.0.0` / `2.0.0` |
| minimum macOS | `15.0.0` |
| executable | `Chirality`, mode `0755`, Mach-O 64-bit arm64 |
| main SHA-256 | `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874` |
| R19 comparison | equal to the owner-reported R19 executable SHA-256 |
| runtime CLI | mode `0755`; SHA-256 `0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989` |
| signature posture | ad-hoc linker-only; no team, sealed resources, or internal requirements |

Strict codesign verification retained the calibrated exit 1 diagnostic `code has no resources but signature indicates they must be present`. Instruction summary / manifest SHA-256 are `3a9666d40235dfbaedf16dc3da29b0bc541b64298ae2faec05dcb27a202d3b36` / `c5b2bf101de6412ae63fd19ba76cac6c73cffa156357551c4203a54ce771135b`. The packaged `dist-electron/main.js` is 1,379,516 bytes at SHA-256 `bfcf16002fc5132d0d96c68a5574927bfd0593b1ce905e71bea72a957bfc4ce1` and contains the exact R17 103-byte macOS socket guard. The frontend diff from `PROOF_REVISION` to `HEAD` is empty.

## One direct disposable daemon precheck

Only after the exact root passed the non-following absent/non-symlink gate, exactly one local-Unix/loopback-only packaged-daemon precheck ran. PID 48351 matched the exact packaged executable and `--runtime-daemon`; the exact socket was a 67-byte Unix socket; authenticated packaged CLI `project list --json` returned exact `[]`; SIGTERM completed the product shutdown with exit 0; and process/socket/runtime-data/root cleanup passed. The exact root passed the metadata-only absent/non-symlink gate afterward. No LaunchAgent/plist/default-operator action or external network request occurred.

## R20 exact identity and live read-only gate

- UUID: `bf0d2e6c-f705-446e-8e4f-a073c6645933`.
- Label: `com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933`.
- Root: `/private/tmp/ch-r18-91499728-51dd`.
- Plist: `/Users/ryan/Library/LaunchAgents/com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933.plist`.
- Service: `gui/501/com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933`.
- Public destination: `/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r20-bf0d2e6c-f705-446e-8e4f-a073c6645933-public-evidence`.
- Failed destination: `/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r20-bf0d2e6c-f705-446e-8e4f-a073c6645933-failed-evidence`.

Exact non-following absence checks passed for root, plist, public destination, and failed destination. Read-only `launchctl print` of only the exact new service exited 113 with:

```text
Bad request.
Could not find service "com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933" in domain for user gui: 501
```

## Concrete staged owner procedure — documentation only

**No block below was executed in this tranche. Do not manually open the app, bootstrap or kickstart any label, or continue after any error. Each block is fresh-Terminal-tab safe.**

### Step 0 — exact package/source/identity/socket and read-only preflight

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
REPO_ROOT="/Users/ryan/.codex/worktrees/ef5e/chirality"
PROOF_APP="$REPO_ROOT/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app"
PROOF_EXECUTABLE="$PROOF_APP/Contents/MacOS/Chirality"
PROOF_EXECUTABLE_SHA256="79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874"
PROOF_REVISION="cb008dc5d6aa9b249639c91f3453a18609530d0f"
PROOF_ROOT="/private/tmp/ch-r18-91499728-51dd"
PROOF_SOCKET="$PROOF_ROOT/runtime-data/runtime/control.sock"
PROOF_LABEL="com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933"
PROOF_PLIST="/Users/ryan/Library/LaunchAgents/$PROOF_LABEL.plist"
PROOF_SERVICE="gui/501/$PROOF_LABEL"
PUBLIC_EVIDENCE="/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r20-bf0d2e6c-f705-446e-8e4f-a073c6645933-public-evidence"
FAILED_EVIDENCE="/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r20-bf0d2e6c-f705-446e-8e4f-a073c6645933-failed-evidence"
test "$(git rev-parse --show-toplevel)" = "$REPO_ROOT"
test -d "$PROOF_APP"
test -r "$PROOF_EXECUTABLE"
test -x "$PROOF_EXECUTABLE"
test "$(/usr/libexec/PlistBuddy -c 'Print :CFBundleIdentifier' "$PROOF_APP/Contents/Info.plist")" = "com.chirality.app"
test "$(/usr/bin/shasum -a 256 "$PROOF_EXECUTABLE" | /usr/bin/awk '{print $1}')" = "$PROOF_EXECUTABLE_SHA256"
FRONTEND_DIFF="$(git diff --stat "$PROOF_REVISION"..HEAD -- projects/chirality-app-dev/frontend)"
test -z "$FRONTEND_DIFF"
for TARGET in "$PROOF_ROOT" "$PROOF_PLIST" "$PUBLIC_EVIDENCE" "$FAILED_EVIDENCE"; do
  test ! -e "$TARGET"
  test ! -L "$TARGET"
done
PROOF_SOCKET_BYTES="$(LC_ALL=C printf '%s' "$PROOF_SOCKET" | /usr/bin/wc -c | /usr/bin/tr -d ' ')"
printf 'PROOF_SOCKET_UTF8_BYTES=%s\n' "$PROOF_SOCKET_BYTES"
printf 'PROOF_SOCKET_MAX_UTF8_BYTES=%s\n' '103'
test "$PROOF_SOCKET_BYTES" -eq 67
test "$PROOF_SOCKET_BYTES" -le 103
set +e
PROOF_JOB_OUTPUT="$(/bin/launchctl print "$PROOF_SERVICE" 2>&1)"
PROOF_JOB_EXIT=$?
set -e
EXPECTED_PROOF_JOB_NOT_FOUND="$(printf '%s\n%s' 'Bad request.' 'Could not find service "com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933" in domain for user gui: 501')"
test "$PROOF_JOB_EXIT" -eq 113
test "$PROOF_JOB_OUTPUT" = "$EXPECTED_PROOF_JOB_NOT_FOUND"
node projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs preflight
for TARGET in "$PROOF_ROOT" "$PROOF_PLIST" "$PUBLIC_EVIDENCE" "$FAILED_EVIDENCE"; do
  test ! -e "$TARGET"
  test ! -L "$TARGET"
done
set +e
PROOF_JOB_OUTPUT_AFTER="$(/bin/launchctl print "$PROOF_SERVICE" 2>&1)"
PROOF_JOB_EXIT_AFTER=$?
set -e
test "$PROOF_JOB_EXIT_AFTER" -eq 113
test "$PROOF_JOB_OUTPUT_AFTER" = "$EXPECTED_PROOF_JOB_NOT_FOUND"
printf '%s\n' 'PASS — exact R20 package/frontend tree, 67-byte socket, unique absent identity, and read-only preflight verified'
```

Do not continue unless Step 0 exits zero and prints its final PASS line. The source gate is the empty frontend diff from `PROOF_REVISION` to later `HEAD`; a documentation-only merge with the same frontend tree remains valid.

### Step 1 — prepare only

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_APP="/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app"
PROOF_ROOT="/private/tmp/ch-r18-91499728-51dd"
PROOF_LABEL="com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933"
PROOF_REVISION="cb008dc5d6aa9b249639c91f3453a18609530d0f"
node projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs prepare --app-path "$PROOF_APP" --session-root "$PROOF_ROOT" --label "$PROOF_LABEL" --source-revision "$PROOF_REVISION"
```

### Prepared check — exact non-claiming state

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_ROOT="/private/tmp/ch-r18-91499728-51dd"
PROOF_REVISION="cb008dc5d6aa9b249639c91f3453a18609530d0f"
node -e 'const fs = require("fs"); const value = JSON.parse(fs.readFileSync(process.argv[1], "utf8")); if (value.status !== "PREPARED" || value.proofClaimed !== false || value.sourceRevision !== process.argv[2]) throw new Error("Prepared state is not accepted"); console.log(JSON.stringify({status: value.status, proofClaimed: value.proofClaimed, sourceRevision: value.sourceRevision}, null, 2));' "$PROOF_ROOT/prepared.json" "$PROOF_REVISION"
```

Only after Step 1 and the prepared check pass, perform one ordinary owner logout and later login on the same GUI account. Do not manually open the app. Do not bootstrap or kickstart the label.

### Capture with claim-calibrated failure handling

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_ROOT="/private/tmp/ch-r18-91499728-51dd"
FAILED_EVIDENCE="/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r20-bf0d2e6c-f705-446e-8e4f-a073c6645933-failed-evidence"
set +e
CAPTURE_OUTPUT="$(node projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs capture --session-root "$PROOF_ROOT" 2>&1)"
CAPTURE_EXIT=$?
set -e
printf '%s\n' "$CAPTURE_OUTPUT"
if test "$CAPTURE_EXIT" -ne 0; then
  test ! -e "$FAILED_EVIDENCE"
  test ! -L "$FAILED_EVIDENCE"
  /bin/mkdir -m 700 "$FAILED_EVIDENCE"
  for NAME in prepared.json summary.json evidence-package.json; do
    if test -f "$PROOF_ROOT/$NAME" && test ! -L "$PROOF_ROOT/$NAME"; then
      /usr/bin/install -m 600 "$PROOF_ROOT/$NAME" "$FAILED_EVIDENCE/$NAME"
    else
      printf 'FAILED_JSON_UNAVAILABLE=%s\n' "$NAME"
    fi
  done
  LOG_DISPOSITION="PRIVATE"
  if test -f "$PROOF_ROOT/summary.json" && test ! -L "$PROOF_ROOT/summary.json"; then
    LOG_DISPOSITION="$(node -e 'const fs=require("fs"); const s=JSON.parse(fs.readFileSync(process.argv[1],"utf8")); process.stdout.write(s.cleanup?.failureLogsCopied === true && s.cleanup?.failureLogsPrivateOnly === false ? "COPY" : "PRIVATE");' "$PROOF_ROOT/summary.json")"
  fi
  if test "$LOG_DISPOSITION" = "COPY"; then
    FAILED_LOGS_SOURCE="$PROOF_ROOT/failed-logs"
    test -d "$FAILED_LOGS_SOURCE"
    test ! -L "$FAILED_LOGS_SOURCE"
    /bin/mkdir -m 700 "$FAILED_EVIDENCE/failed-logs"
    for NAME in daemon.stdout.log daemon.stderr.log; do
      test -f "$FAILED_LOGS_SOURCE/$NAME"
      test ! -L "$FAILED_LOGS_SOURCE/$NAME"
      /usr/bin/install -m 600 "$FAILED_LOGS_SOURCE/$NAME" "$FAILED_EVIDENCE/failed-logs/$NAME"
    done
    printf '%s\n' 'FAILED_LOGS=TOKEN_CLEARED_COPIES_PRESERVED'
  else
    printf '%s\n' 'FAILED_LOGS=PRIVATE_ROOT_ONLY_OR_UNAVAILABLE'
    printf '%s\n' 'OWNER_ACTION=Do not touch the private proof root; it must remain intact for diagnosis.'
  fi
  test "$(/usr/bin/stat -f %Lp "$FAILED_EVIDENCE")" = "700"
  if test -d "$FAILED_EVIDENCE/failed-logs"; then
    test "$(/usr/bin/stat -f %Lp "$FAILED_EVIDENCE/failed-logs")" = "700"
  fi
  BAD_MODE_COUNT="$(/usr/bin/find "$FAILED_EVIDENCE" -type f ! -perm 600 -print | /usr/bin/wc -l | /usr/bin/tr -d ' ')"
  test "$BAD_MODE_COUNT" = "0"
  /usr/bin/find "$FAILED_EVIDENCE" -type f -exec /usr/bin/shasum -a 256 '{}' \;
  printf 'CAPTURE_EXIT=%s\n' "$CAPTURE_EXIT"
  printf '%s\n' 'STATUS=FAIL — preserve failed evidence, make no proof claim, and stop.'
  exit "$CAPTURE_EXIT"
fi
printf '%s\n' 'CAPTURE_EXIT=0'
```

On any capture error, stop. Never copy `.capture-state.json`, `.capture-state.consumed.json`, runtime data, plist, token, or other private state. If the repaired harness reports private-only preservation or logs are absent/unsafe, do not copy logs and leave the private root untouched for diagnosis.

### PASS and exact-revision check

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_ROOT="/private/tmp/ch-r18-91499728-51dd"
PROOF_REVISION="cb008dc5d6aa9b249639c91f3453a18609530d0f"
node -e 'const fs = require("fs"); const revision = process.argv[3]; const summary = JSON.parse(fs.readFileSync(process.argv[1], "utf8")); const evidence = JSON.parse(fs.readFileSync(process.argv[2], "utf8")); if (summary.status !== "PASS" || evidence.status !== "PASS") throw new Error("Login proof did not PASS"); if (summary.sourceRevision !== revision || evidence.sourceRevision !== revision) throw new Error("Login proof revision mismatch"); console.log(JSON.stringify({summaryStatus: summary.status, evidenceStatus: evidence.status, sourceRevision: revision}, null, 2));' "$PROOF_ROOT/summary.json" "$PROOF_ROOT/evidence-package.json" "$PROOF_REVISION"
```

### Preserve exactly three PASS public files

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_ROOT="/private/tmp/ch-r18-91499728-51dd"
PUBLIC_EVIDENCE="/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r20-bf0d2e6c-f705-446e-8e4f-a073c6645933-public-evidence"
test ! -e "$PUBLIC_EVIDENCE"
test ! -L "$PUBLIC_EVIDENCE"
/bin/mkdir -m 700 "$PUBLIC_EVIDENCE"
/usr/bin/install -m 600 "$PROOF_ROOT/prepared.json" "$PUBLIC_EVIDENCE/prepared.json"
/usr/bin/install -m 600 "$PROOF_ROOT/summary.json" "$PUBLIC_EVIDENCE/summary.json"
/usr/bin/install -m 600 "$PROOF_ROOT/evidence-package.json" "$PUBLIC_EVIDENCE/evidence-package.json"
test "$(/usr/bin/stat -f %Lp "$PUBLIC_EVIDENCE")" = "700"
for NAME in prepared.json summary.json evidence-package.json; do
  test "$(/usr/bin/stat -f %Lp "$PUBLIC_EVIDENCE/$NAME")" = "600"
done
test "$(/usr/bin/find "$PUBLIC_EVIDENCE" -mindepth 1 -maxdepth 1 -type f | /usr/bin/wc -l | /usr/bin/tr -d ' ')" = "3"
HASH_LINES="$(cd "$PUBLIC_EVIDENCE" && /usr/bin/shasum -a 256 prepared.json summary.json evidence-package.json)"
printf '%s\n' "$HASH_LINES"
(cd "$PUBLIC_EVIDENCE" && printf '%s\n' "$HASH_LINES" | /usr/bin/shasum -a 256 -c -)
printf '%s\n' 'PASS — exactly three public JSON files preserved mode 0600 in a new mode-0700 directory'
```

### Owner handoff — print and return verbatim

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_REVISION="cb008dc5d6aa9b249639c91f3453a18609530d0f"
PROOF_LABEL="com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933"
PUBLIC_EVIDENCE="/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r20-bf0d2e6c-f705-446e-8e4f-a073c6645933-public-evidence"
node -e 'const fs = require("fs"); const revision = process.argv[3]; const summary = JSON.parse(fs.readFileSync(process.argv[1], "utf8")); const evidence = JSON.parse(fs.readFileSync(process.argv[2], "utf8")); if (summary.status !== "PASS" || evidence.status !== "PASS" || summary.sourceRevision !== revision || evidence.sourceRevision !== revision) throw new Error("Public evidence is not exact-revision PASS");' "$PUBLIC_EVIDENCE/summary.json" "$PUBLIC_EVIDENCE/evidence-package.json" "$PROOF_REVISION"
PREPARED_SHA256="$(/usr/bin/shasum -a 256 "$PUBLIC_EVIDENCE/prepared.json" | /usr/bin/awk '{print $1}')"
SUMMARY_SHA256="$(/usr/bin/shasum -a 256 "$PUBLIC_EVIDENCE/summary.json" | /usr/bin/awk '{print $1}')"
EVIDENCE_SHA256="$(/usr/bin/shasum -a 256 "$PUBLIC_EVIDENCE/evidence-package.json" | /usr/bin/awk '{print $1}')"
printf '%s\n' \
  'CHIRALITY LOGIN PROOF OWNER HANDOFF' \
  "PROOF_REVISION=$PROOF_REVISION" \
  "PROOF_LABEL=$PROOF_LABEL" \
  "PUBLIC_EVIDENCE=$PUBLIC_EVIDENCE" \
  'STATUS=PASS' \
  "$PREPARED_SHA256  prepared.json" \
  "$SUMMARY_SHA256  summary.json" \
  "$EVIDENCE_SHA256  evidence-package.json" \
  'OWNER_MESSAGE=R20 login-session proof returned for owner review; no acceptance or release claim is implied.'
```

Return the complete handoff verbatim. Preparation, owner logout/login, capture, evidence handling, handoff, and any acceptance remain future owner acts.

## Validation and derivative handoff

The Step 0 exact strings were re-tested live read-only for only the fresh R20 service: all four exact absence gates passed, service exit was 113, and the two-line not-found text matched. Procedure blocks were syntax/structured-safety checked without executing preflight, prepare, capture, preservation, or handoff.

The one ordinary-sandbox exact `npm test` diagnostic exited 1 at 21 failed / 1,261 passed / 4 skipped. All failures are the established local TCP/Unix `listen EPERM` set and remain classified `ENVIRONMENT_SANDBOX_SOCKET_DENIAL`, not PASS. The sole exact `npm test` cure, with local test-socket binding permitted and external network forbidden, exited 0 at 1,282 passed / 4 skipped. The Pi/oMLX 200 ms timing case did not recur. No full-suite rerun occurred. The exact frontend tree and every frozen source/test/package hash matched before and after. Future pre-merge harness `full_test` plus typecheck remains independent confirmation and is not yet observed.

This record, ignored package, generated instruction-root output, precheck evidence, and staged R20 procedure are derivative evidence bound to exact revision `cb008dc5d6aa9b249639c91f3453a18609530d0f`; they do not replace source truth. DEL-09-04 remains `IN_PROGRESS` and unproved.
