# R19 — offline exact-merge package and login-proof staging

- Date: `2026-08-23`
- Run: `APPDEV_LOGIN_PROOF_R19_STAGING_2026-08-23`
- Exact build revision: `d6861ae8251e2a81078577d4496e949735ff199d`
- Frontend tree: `9c1b1d9cec8c45a2a74e78c79ce37d784938a6e4`
- Branch: `codex/app-login-proof-r19-staging`
- Result: `SUBSCOPE PASS / TRANCHE VALIDATION NOT PASS — UNSIGNED OFFLINE PACKAGE, EMPIRICAL PRECHECK, AND OWNER-PROCEDURE STAGING PASSED; RETAINED FULL-SUITE CURE REMAINS NON-PASS`
- Deliverable state: `IN_PROGRESS`, unproved

## Claim boundary

This derivative record binds one locally rebuilt unsigned arm64 app-directory
package to the exact merged PR #623 revision and stages a fresh owner-only
login-session procedure. It does not execute or accept the procedure or proof.
No GUI, prepare, capture, logout/login, LaunchAgent/plist, bootstrap,
kickstart, default operator surface, launcher, signing, notarization,
deployment, distribution, publication, release-readiness, issuance, or
reliance act occurred. The existing R16 attempt remains failed evidence as
recorded by immutable R17; R19 does not upgrade it.

`origin/main` advanced to `8635e40995b05f494ae35c6083dabdd50068bb52`
after the owner selected this exact basis. The branch was not synchronized,
merged, rebased, or rewritten without owner authorization. The build revision
and frontend tree above remained exact.

## Exact supply and offline build

From the exact frontend cwd, `npm run electron:supply-chain` ran once and
exited zero. Its verifier child emitted only the exact verified directory
`/Users/ryan/Library/Caches/chirality/electron-dist`; the npm lifecycle layer
printed only its ordinary package/command preamble around that line.

After a prebuild ignored-artifact inventory was frozen, exactly one command
ran in the ordinary network-denied sandbox, without escalation or retry:

```text
cwd: /Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend
command: npm run desktop:pack
exit: 0
```

The complete durable command log is
`execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R19_STAGING_2026-08-23/instances/WI-PKG09-R19-STAGING-01/executor/desktop-pack.full.log`,
16,098 bytes at SHA-256
`2c0229474bad89dce1ced7e1303a2cd5b5bff0d0df3624dd5cd850baf1cb2db8`.
Repair cycle 1 restored its exact 9,588-byte Electron Builder
`duplicate dependency references` field byte-for-byte from the original R19
execution-tool transcript, without rerunning packaging; the field SHA-256 is
`0f1611f07c7a52900d89bd60f8702986555435a632305542e73b400f29e155b3`.
The log records Electron Builder 26.15.3, Electron 43.2.0 arm64, and the exact
line:

```text
using custom electronDist directory  electronDist=/Users/ryan/Library/Caches/chirality/electron-dist
```

The observed command output contains no case-insensitive `download`,
`github.com`, or `release-assets.githubusercontent.com` indicator. Embedded
packaged dependency verification returned `PASS`, and instruction-root
integrity returned `pass` for 43 files at exact Git SHA
`d6861ae8251e2a81078577d4496e949735ff199d`.

## Package identity and R17 guard

Package:

```text
/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app
```

| Check | Exact observation |
|---|---|
| bundle ID | `com.chirality.app` |
| short / bundle version | `2.0.0` / `2.0.0` |
| minimum macOS | `15.0.0` |
| executable | `Chirality`, mode `0755`, readable/executable |
| architecture | Mach-O 64-bit arm64; `lipo` arm64 |
| main SHA-256 | `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874` |
| runtime CLI SHA-256 | `0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989` |
| signature | ad-hoc linker-only; no team, sealed resources, or internal requirements |

The calibrated strict codesign diagnostic remains exit 1, `code has no
resources but signature indicates they must be present`. This is an unsigned
local `--dir` build, not a sealed distribution signature.

Instruction-root summary SHA-256 is
`1ff8adf9bccc1bd108a4321d4637b8d31b0f443f5fd1f1a8f75e120e54bc9c84`;
manifest SHA-256 is
`bd2e1e825f570bc8e77ad3b0e0a3093f12f9ac1005ef15f22bdfa3abc6dd340b`.
Both name the exact build revision; the manifest contains 43 files.

Read-only `app.asar` extraction found packaged `dist-electron/main.js` at
1,379,498 bytes with SHA-256
`64b99b9a0c661dc53fe71aa6fed184a52220d8c61b4cc41989149c8a672b2947`.
It contains exactly one 103-byte macOS maximum declaration and the committed
R17 `Buffer.byteLength(..., "utf8")` fail-closed overlong-socket diagnostic.
No package byte was changed.

The exact commands below returned empty:

```sh
git diff --stat d6861ae8251e2a81078577d4496e949735ff199d..HEAD -- projects/chirality-app-dev/frontend
git status --porcelain=v1 --untracked-files=all -- projects/chirality-app-dev/frontend
```

## One direct disposable packaged-daemon precheck

Only after proving `/private/tmp/ch-r18-91499728-51dd` absent and non-symlink,
the executor used one frozen fail-safe script through one execution-tool grant
restricted in purpose to local Unix/loopback socket binding. No external
network request or network tool was used. It directly started:

```text
/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality --runtime-daemon
```

with exact `CHIRALITY_USER_DATA=/private/tmp/ch-r18-91499728-51dd/runtime-data`,
`CHIRALITY_SKIP_CLI_LAUNCHER=1`, and
`CHIRALITY_DAEMON_GUI_SPAWN=0`. PID 16906 matched the exact executable and
argv. The exact 67-byte path
`/private/tmp/ch-r18-91499728-51dd/runtime-data/runtime/control.sock` existed as
a Unix socket. The packaged CLI, authenticated through the same disposable
runtime, ran the non-LaunchAgent action `project list --json` and returned
exact `[]`.

SIGTERM entered the product's `runtime-daemon-signal` shutdown funnel and the
daemon exited zero. The exact PID, socket, runtime-data directory, and then
empty proof root were absent after bounded cleanup. The proof plist and public
destination remained absent. There was no retry. The daemon's expected
unregistered-root instruction fallback did not affect authenticated control
health.

## Concrete staged owner procedure — documentation only

**DO NOT execute any block in this tranche. Do not manually open
`Chirality.app`, bootstrap or kickstart any label, or continue after any
error.** Every block is independently copy-paste-safe for a fresh Terminal
tab and begins at the exact repo root with `set -euo pipefail`.

### Step 0 — exact package, socket, uniqueness, and read-only preflight

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
REPO_ROOT="/Users/ryan/.codex/worktrees/ef5e/chirality"
PROOF_APP="/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app"
PROOF_EXECUTABLE="$PROOF_APP/Contents/MacOS/Chirality"
PROOF_EXECUTABLE_SHA256="79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874"
PROOF_REVISION="d6861ae8251e2a81078577d4496e949735ff199d"
PROOF_ROOT="/private/tmp/ch-r18-91499728-51dd"
PROOF_SOCKET="$PROOF_ROOT/runtime-data/runtime/control.sock"
PROOF_LABEL="com.chirality.ci.runatload.login.owner.macos26.r19.3951dfe9-ec03-421b-b376-fd5f0d96992b"
PROOF_PLIST="/Users/ryan/Library/LaunchAgents/com.chirality.ci.runatload.login.owner.macos26.r19.3951dfe9-ec03-421b-b376-fd5f0d96992b.plist"
PROOF_SERVICE="gui/501/com.chirality.ci.runatload.login.owner.macos26.r19.3951dfe9-ec03-421b-b376-fd5f0d96992b"
PUBLIC_EVIDENCE="/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r19-3951dfe9-ec03-421b-b376-fd5f0d96992b-public-evidence"
test "$(git rev-parse --show-toplevel)" = "$REPO_ROOT"
test -d "$PROOF_APP"
test -r "$PROOF_EXECUTABLE"
test -x "$PROOF_EXECUTABLE"
test "$(/usr/bin/shasum -a 256 "$PROOF_EXECUTABLE" | /usr/bin/awk '{print $1}')" = "$PROOF_EXECUTABLE_SHA256"
FRONTEND_DIFF="$(git diff --stat "$PROOF_REVISION"..HEAD -- projects/chirality-app-dev/frontend)"
test -z "$FRONTEND_DIFF"
test ! -e "$PROOF_ROOT"
test ! -L "$PROOF_ROOT"
test ! -e "$PROOF_PLIST"
test ! -L "$PROOF_PLIST"
test ! -e "$PUBLIC_EVIDENCE"
test ! -L "$PUBLIC_EVIDENCE"
PROOF_SOCKET_BYTES="$(LC_ALL=C printf '%s' "$PROOF_SOCKET" | /usr/bin/wc -c | /usr/bin/tr -d ' ')"
printf 'PROOF_SOCKET_UTF8_BYTES=%s\n' "$PROOF_SOCKET_BYTES"
printf 'PROOF_SOCKET_MAX_UTF8_BYTES=%s\n' '103'
test "$PROOF_SOCKET_BYTES" -eq 67
test "$PROOF_SOCKET_BYTES" -le 103
set +e
PROOF_JOB_OUTPUT="$(/bin/launchctl print "$PROOF_SERVICE" 2>&1)"
PROOF_JOB_EXIT=$?
set -e
EXPECTED_PROOF_JOB_NOT_FOUND="$(printf '%s\n%s' 'Bad request.' 'Could not find service "com.chirality.ci.runatload.login.owner.macos26.r19.3951dfe9-ec03-421b-b376-fd5f0d96992b" in domain for user gui: 501')"
test "$PROOF_JOB_EXIT" -eq 113
test "$PROOF_JOB_OUTPUT" = "$EXPECTED_PROOF_JOB_NOT_FOUND"
node projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs preflight
test ! -e "$PROOF_ROOT"
test ! -L "$PROOF_ROOT"
test ! -e "$PROOF_PLIST"
test ! -L "$PROOF_PLIST"
test ! -e "$PUBLIC_EVIDENCE"
test ! -L "$PUBLIC_EVIDENCE"
set +e
PROOF_JOB_OUTPUT_AFTER="$(/bin/launchctl print "$PROOF_SERVICE" 2>&1)"
PROOF_JOB_EXIT_AFTER=$?
set -e
test "$PROOF_JOB_EXIT_AFTER" -eq 113
test "$PROOF_JOB_OUTPUT_AFTER" = "$EXPECTED_PROOF_JOB_NOT_FOUND"
printf '%s\n' 'PASS — exact package/frontend tree, 67-byte socket, unique absent identity, and read-only preflight verified'
```

Do not continue unless Step 0 exits zero and prints the final `PASS` line. The
empty frontend diff—not current `HEAD` equality—is the source gate, so a later
documentation-only commit with an identical frontend tree remains valid.

### Step 1 — prepare only

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_APP="/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app"
PROOF_ROOT="/private/tmp/ch-r18-91499728-51dd"
PROOF_LABEL="com.chirality.ci.runatload.login.owner.macos26.r19.3951dfe9-ec03-421b-b376-fd5f0d96992b"
PROOF_REVISION="d6861ae8251e2a81078577d4496e949735ff199d"
node projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs prepare --app-path "$PROOF_APP" --session-root "$PROOF_ROOT" --label "$PROOF_LABEL" --source-revision "$PROOF_REVISION"
```

### Prepared check — accept only exact non-claiming state

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_ROOT="/private/tmp/ch-r18-91499728-51dd"
PROOF_REVISION="d6861ae8251e2a81078577d4496e949735ff199d"
node -e 'const fs = require("fs"); const value = JSON.parse(fs.readFileSync(process.argv[1], "utf8")); if (value.status !== "PREPARED" || value.proofClaimed !== false || value.sourceRevision !== process.argv[2]) throw new Error("Prepared state is not accepted"); console.log(JSON.stringify({status: value.status, proofClaimed: value.proofClaimed, sourceRevision: value.sourceRevision}, null, 2));' "$PROOF_ROOT/prepared.json" "$PROOF_REVISION"
```

Only after both Step 1 and the prepared check exit zero, perform one ordinary
owner logout and later login on the same GUI account. Do not manually open the
app. Do not bootstrap or kickstart the label.

### Capture — only after the later login

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_ROOT="/private/tmp/ch-r18-91499728-51dd"
node projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs capture --session-root "$PROOF_ROOT"
```

### PASS and exact-revision check

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_ROOT="/private/tmp/ch-r18-91499728-51dd"
PROOF_REVISION="d6861ae8251e2a81078577d4496e949735ff199d"
node -e 'const fs = require("fs"); const revision = process.argv[3]; const summary = JSON.parse(fs.readFileSync(process.argv[1], "utf8")); const evidence = JSON.parse(fs.readFileSync(process.argv[2], "utf8")); if (summary.status !== "PASS" || evidence.status !== "PASS") throw new Error("Login proof did not PASS"); if (summary.sourceRevision !== revision || evidence.sourceRevision !== revision) throw new Error("Login proof revision mismatch"); console.log(JSON.stringify({summaryStatus: summary.status, evidenceStatus: evidence.status, sourceRevision: revision}, null, 2));' "$PROOF_ROOT/summary.json" "$PROOF_ROOT/evidence-package.json" "$PROOF_REVISION"
```

### Preserve exactly three public files and verify their hashes

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_ROOT="/private/tmp/ch-r18-91499728-51dd"
PUBLIC_EVIDENCE="/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r19-3951dfe9-ec03-421b-b376-fd5f0d96992b-public-evidence"
test ! -e "$PUBLIC_EVIDENCE"
test ! -L "$PUBLIC_EVIDENCE"
/bin/mkdir -m 700 "$PUBLIC_EVIDENCE"
/usr/bin/install -m 600 "$PROOF_ROOT/prepared.json" "$PUBLIC_EVIDENCE/prepared.json"
/usr/bin/install -m 600 "$PROOF_ROOT/summary.json" "$PUBLIC_EVIDENCE/summary.json"
/usr/bin/install -m 600 "$PROOF_ROOT/evidence-package.json" "$PUBLIC_EVIDENCE/evidence-package.json"
test "$(/usr/bin/stat -f %Lp "$PUBLIC_EVIDENCE")" = "700"
test "$(/usr/bin/stat -f %Lp "$PUBLIC_EVIDENCE/prepared.json")" = "600"
test "$(/usr/bin/stat -f %Lp "$PUBLIC_EVIDENCE/summary.json")" = "600"
test "$(/usr/bin/stat -f %Lp "$PUBLIC_EVIDENCE/evidence-package.json")" = "600"
test "$(/usr/bin/find "$PUBLIC_EVIDENCE" -mindepth 1 -maxdepth 1 -type f | /usr/bin/wc -l | /usr/bin/tr -d ' ')" = "3"
HASH_LINES="$(cd "$PUBLIC_EVIDENCE" && /usr/bin/shasum -a 256 prepared.json summary.json evidence-package.json)"
printf '%s\n' "$HASH_LINES"
(cd "$PUBLIC_EVIDENCE" && printf '%s\n' "$HASH_LINES" | /usr/bin/shasum -a 256 -c -)
printf '%s\n' 'PASS — exactly three public files preserved mode 0600 in a new mode-0700 directory'
```

Never copy or publish `.capture-state.json`, `.capture-state.consumed.json`,
runtime data, a plist, logs, tokens, or any other private proof state.

### Owner handoff — print and return verbatim

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_REVISION="d6861ae8251e2a81078577d4496e949735ff199d"
PROOF_LABEL="com.chirality.ci.runatload.login.owner.macos26.r19.3951dfe9-ec03-421b-b376-fd5f0d96992b"
PUBLIC_EVIDENCE="/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r19-3951dfe9-ec03-421b-b376-fd5f0d96992b-public-evidence"
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
  'OWNER_MESSAGE=R19 login-session proof returned for owner review; no acceptance or release claim is implied.'
```

Return the complete displayed handoff verbatim, including all three hashes and
the exact owner-message line.

## Validation and derivative handoff

All procedure blocks were syntax checked without executing prepare, capture,
preservation, or handoff. Step 0's frontend-tree gate was inspected for later
documentation-only `HEAD` portability: it compares the build revision to
`HEAD` only under `projects/chirality-app-dev/frontend`, contains no HEAD
equality assertion, and therefore remains empty when only documentation bytes
change. The live ref/index were not changed for this simulation.

The one ordinary-sandbox exact `npm test` diagnostic exited 1 at 22 failed /
1,245 passed / 4 skipped. Twenty-one failures are the established local
TCP/Unix `listen EPERM` set and remain classified
`ENVIRONMENT_SANDBOX_SOCKET_DENIAL`; one separate synthetic-PID cleanup test
reported PID 4242 still alive after SIGKILL and was not assigned that
classification.

The sole exact `npm test` cure with permission restricted to local test-socket
binding also exited 1, at 1 failed / 1,266 passed / 4 skipped. It remains
`NOT PASS`. All 21 socket denials and the synthetic-PID failure cleared. The
remaining failure was the Pi/oMLX wire success case timing out mid-stream
before its expected `tool:result`, producing `PROVIDER_PROTOCOL_FAILURE`
status 504. Fresh review classified this retained result
`PRE_EXISTING_TEST_HARNESS_TIMING_FLAKE_ENVIRONMENT_LIMITATION`, not a product
or tranche-source defect; that classification does not upgrade the cure to
PASS. The full suite was not rerun. Pre/post frontend tree, all frozen source/test/package hashes,
and the 21,477-byte complete semantic candidate diff SHA-256
`9b1479182347b34f5624e852ab4a0b2070cc11f5457b8f390e73095523a69e44`
match exactly, proving no source change between runs.

This is retained non-PASS validation evidence accepted under the calibrated
environment-limitation classification, pending fresh repair-cycle review of
the complete candidate. It does not invalidate the already passed supply,
single package, package identity/guard, disposable daemon health, cleanup, or
procedure-syntax evidence. Proportional checks remain held as recorded.
Future PR-CI `full_test` plus typecheck is independent confirmation and is not
yet observed.

R19, the ignored package, instruction-root outputs, daemon-precheck evidence,
and staged procedure are derivative evidence bound to the exact build
revision. They do not replace source truth. DEL-09-04 remains `IN_PROGRESS`
and unproved. Preparation, logout/login, capture, public preservation, return,
and owner acceptance remain owner acts. Any frontend-tree or executable-hash
change, root/plist/service/public collision, nonzero preflight, or failed block
invalidates this staged procedure and requires a new bounded owner decision.
