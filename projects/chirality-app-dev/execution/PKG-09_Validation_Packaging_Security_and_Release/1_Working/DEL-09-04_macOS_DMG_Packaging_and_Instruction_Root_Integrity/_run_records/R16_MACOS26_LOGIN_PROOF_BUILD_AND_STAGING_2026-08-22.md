# DEL-09-04 exact-merge macOS 26 login-proof build and owner staging

- Date: `2026-08-22`
- Run: `APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22`
- Exact source revision: `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`
- Branch: `codex/app-login-proof-r16-staging`
- Result: `PASS — UNSIGNED EXACT-MERGE PACKAGE REBUILT; OWNER PROCEDURE STAGED ONLY`
- Deliverable state: `IN_PROGRESS`

This record is new derivative evidence authored only from the exact-merge
rebuild and the current read-only checks named below. An earlier approximately
`12:50` local rebuild and superseded R16 material occurred under prior
authorization, remained unadopted, and are superseded by this exact-merge
rebuild and this new record. No byte or identity from that earlier material is
adopted or cited here.

No GUI launch, proof preparation, capture, logout/login, bootstrap, kickstart,
operator deployment, signing, notarization, distribution, publication,
release-readiness, issuance, or reliance act occurred.

## Exact build and package

Initial fail-closed checks established:

- `HEAD` and `origin/main` both exactly
  `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`;
- branch `codex/app-login-proof-r16-staging`;
- empty index and no tracked worktree change;
- empty scoped frontend porcelain;
- absent proposed proof root and exact proof plist; and
- the exact proof label was not loaded (`launchctl` exit `113`, not found).

The exact command ran from the exact cwd:

```text
cwd: /Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend
command: npm run desktop:pack
```

The first attempt compiled the Next, Electron, and CLI outputs, then exited `1`
when Electron Builder's cache miss for pinned Electron `43.2.0` arm64 met the
sandbox DNS failure `getaddrinfo ENOTFOUND github.com`. Under locked amendment
01, the same tracked command was rerun once with network permission limited by
purpose to that exact pinned artifact retrieval. No dependency, manifest,
lockfile, source, or provider changed. The retry exited `0` and its complete
combined output is preserved at:

```text
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R16_STAGING_2026-08-22/instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/desktop-pack.log
```

- retry log SHA-256:
  `67f9c2de21de732f819e59cad4f4b94429cd654c227fc27653ed676d9937ce62`
- retry exit-status file SHA-256:
  `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`
- initial failed log SHA-256:
  `827459042c5115f7b0e1ac14d9a25d9550bc48ddf1b1cf5442adafc4d1975ee5`

The tracked command itself ran and passed both embedded terminal gates:

- `desktop:verify-dependencies`: `PASS`; zero monorepo-local package entries,
  no forbidden development package, all required packages present, packaged
  desktop/CLI runtime-source proof `PASS`, and no failures;
- `instruction-root:integrity`: `pass`; exact Git SHA
  `06f60e42e35ea5c39abf9e33c4d3e877d77c4497` and `43` checked files.

Current package:

```text
/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app
```

Independent read-only package checks established:

| Field | Exact value |
|---|---|
| bundle identifier | `com.chirality.app` |
| short version | `2.0.0` |
| bundle version | `2.0.0` |
| executable name | `Chirality` |
| minimum macOS | `15.0.0` |
| `file` | `Mach-O 64-bit executable arm64` |
| `lipo -archs` | `arm64` |
| main executable SHA-256 | `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874` |

The main executable is readable and executable. `codesign -dv --verbose=4`
reports only `flags=0x20002(adhoc,linker-signed)`, `Signature=adhoc`,
`TeamIdentifier=not set`, `Sealed Resources=none`, and no internal
requirements. Read-only strict verification exits `1` with the calibrated
diagnostic that the code has no resources although its linker signature
indicates they must be present. This is not a sealed application signature:
Electron Builder explicitly skipped application signing under
`CSC_IDENTITY_AUTO_DISCOVERY=false`. There is no Team ID, Developer ID,
signing action, notarization, or distribution claim.

The packaged CLI exists and is readable at:

```text
/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/runtime-cli/chirality-cli.mjs
```

Its SHA-256 is
`0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`.

## Instruction-root evidence

Current generated files:

```text
/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/artifacts/harness/instruction-root-integrity/latest/summary.json
/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/artifacts/harness/instruction-root-integrity/latest/manifest.json
```

- generated: `2026-08-22T21:48:15.883Z`;
- summary status: `pass`;
- exact Git SHA: `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`;
- checked files / manifest files: `43` / `43`;
- missing, mismatched, or unexpected bundle-agent files: none;
- summary SHA-256:
  `89ba0e597190205fd50e1216e9efeb9f6ea9dd53e920a27f31251ad8cfb5b468`;
- manifest SHA-256:
  `dfea68cf9b550848d5573a02c73b6647700e0543b6376bb61831c3d38d1c75d1`.

The existing calibrated `sourceCompleteness.status: needs_remediation` remains
because the candidate `examples` source asset is absent. It is not upgraded by
this record and does not alter the explicit source-to-bundle integrity status
`pass`.

## Exact source and Git proof

After packaging, `HEAD` and `origin/main` remained the exact revision above.
The following required command returned no output:

```sh
git diff --stat 06f60e42e35ea5c39abf9e33c4d3e877d77c4497..HEAD -- projects/chirality-app-dev/frontend
```

This required command also returned no output:

```sh
git status --porcelain=v1 --untracked-files=all -- projects/chirality-app-dev/frontend
```

The index was empty, and explicit tracked checks found no source, manifest,
lockfile, dependency, Electron, package, or test change.

## Live optionless read-only preflight

Immediately before preflight, the proposed root and exact proof plist were
absent and the exact proof job was not loaded. From the frontend cwd, only the
committed optionless command ran:

```sh
node scripts/run-packaged-launchagent-login-proof.mjs preflight
```

It exited `0` and returned schema
`chirality-packaged-launchagent-login-proof-preflight/v1`, status `PASS`, mode
`READ_ONLY_PREFLIGHT`, all five account/domain consistency checks true,
`mutationsPerformed: false`, `sessionRootCreated: false`, and
`serviceOrJobInspection: false`. The public result contained no raw username or
session handle. Its complete log SHA-256 is
`61337ccf4dc63ff98578f37dce3bcfcb812881d97e15ec5823104fb87855b5c0`.

After preflight, the proposed root and exact proof plist remained absent and
the exact proof job remained not loaded. No default operator job, plist, or
launcher was queried or touched.

## Concrete staged owner procedure — documentation only

**DO NOT manually open `Chirality.app`, bootstrap or kickstart any label, or
continue after any error.** Run each block exactly and stop if it does not print
the stated success output. This record stages commands only; none ran here.

### Step 0 — exact package and preflight gates

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
REPO_ROOT="/Users/ryan/.codex/worktrees/ef5e/chirality"
PROOF_APP="/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app"
PROOF_EXECUTABLE="/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality"
PROOF_EXECUTABLE_SHA256="79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874"
PROOF_REVISION="06f60e42e35ea5c39abf9e33c4d3e877d77c4497"
PROOF_ROOT="/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20"
PROOF_LABEL="com.chirality.ci.runatload.login.owner.macos26.00bc8f1a-0045-48a2-970f-be120cf7fc20"
PROOF_PLIST="/Users/ryan/Library/LaunchAgents/com.chirality.ci.runatload.login.owner.macos26.00bc8f1a-0045-48a2-970f-be120cf7fc20.plist"
PROOF_SERVICE="gui/501/com.chirality.ci.runatload.login.owner.macos26.00bc8f1a-0045-48a2-970f-be120cf7fc20"
PUBLIC_EVIDENCE="/Users/ryan/Desktop/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20-public-evidence"
test "$(git rev-parse --show-toplevel)" = "$REPO_ROOT"
test -d "$PROOF_APP"
test -r "$PROOF_EXECUTABLE"
test -x "$PROOF_EXECUTABLE"
test "$(/usr/bin/shasum -a 256 "$PROOF_EXECUTABLE" | /usr/bin/awk '{print $1}')" = "$PROOF_EXECUTABLE_SHA256"
FRONTEND_DIFF="$(git diff --stat "$PROOF_REVISION"..HEAD -- projects/chirality-app-dev/frontend)"
test -z "$FRONTEND_DIFF"
test ! -e "$PROOF_ROOT"
test ! -e "$PROOF_PLIST"
set +e
PROOF_JOB_OUTPUT="$(/bin/launchctl print "$PROOF_SERVICE" 2>&1)"
PROOF_JOB_EXIT=$?
set -e
EXPECTED_PROOF_JOB_NOT_FOUND="$(printf '%s\n%s' 'Bad request.' 'Could not find service "com.chirality.ci.runatload.login.owner.macos26.00bc8f1a-0045-48a2-970f-be120cf7fc20" in domain for user gui: 501')"
test "$PROOF_JOB_EXIT" -eq 113
test "$PROOF_JOB_OUTPUT" = "$EXPECTED_PROOF_JOB_NOT_FOUND"
node projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs preflight
test ! -e "$PROOF_ROOT"
printf '%s\n' 'PASS — exact package and frontend tree, unique absent proof identity, and read-only preflight verified'
```

Do not continue unless Step 0 exits `0` and prints the final `PASS` line.
The empty frontend diff, rather than equality between current `HEAD` and the
build revision, is the authoritative source gate. This keeps the block valid
after a documentation-only staging commit or merge whose frontend tree remains
identical to the build revision.

### Post-commit source-gate portability backcheck

A temporary scratch Git copy created synthetic later commit
`22e689882f0e99d78e24cbd1fa98911077259cf3` with exact parent/build revision
`06f60e42e35ea5c39abf9e33c4d3e877d77c4497`. Its only tree change was the
synthetic documentation path
`projects/chirality-app-dev/execution/_Coordination/R16_SYNTHETIC_DOC_ONLY.md`.
The current-HEAD-equality assertion was absent; the authoritative command

```sh
git diff --stat "$PROOF_REVISION"..HEAD -- projects/chirality-app-dev/frontend
```

returned empty from that distinct later `HEAD`, and the source gate exited
`0`. The test did not execute preflight or any host mutation. The scratch copy
was removed after the check; the live branch/ref/index were unchanged. Complete
output is preserved at `executor-attempt-2/post-commit-portability.log`,
SHA-256
`f2866bcb9f8c12aa1ba8dcf728aeeda87a64ff8db3917e0625d3f3b9a28e3c28`.
The separate read-only exact-absence backcheck also passed the root/plist
absence, `launchctl` exit-`113`, and exact two-line not-found gates without
running preflight or performing a host mutation; its log SHA-256 is
`014b8e2d588ba4275525c5e298283ecbc6b1ffa12a680904a2617bdbacc3bc56`.

### Step 1 — prepare only

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_APP="/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app"
PROOF_ROOT="/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20"
PROOF_LABEL="com.chirality.ci.runatload.login.owner.macos26.00bc8f1a-0045-48a2-970f-be120cf7fc20"
PROOF_REVISION="06f60e42e35ea5c39abf9e33c4d3e877d77c4497"
node projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs prepare --app-path "$PROOF_APP" --session-root "$PROOF_ROOT" --label "$PROOF_LABEL" --source-revision "$PROOF_REVISION"
```

### Prepared check — accept only the exact prepared state

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_ROOT="/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20"
PROOF_REVISION="06f60e42e35ea5c39abf9e33c4d3e877d77c4497"
node -e 'const fs = require("fs"); const value = JSON.parse(fs.readFileSync(process.argv[1], "utf8")); if (value.status !== "PREPARED" || value.proofClaimed !== false || value.sourceRevision !== process.argv[2]) throw new Error("Prepared state is not accepted"); console.log(JSON.stringify({status: value.status, proofClaimed: value.proofClaimed, sourceRevision: value.sourceRevision}, null, 2));' "$PROOF_ROOT/prepared.json" "$PROOF_REVISION"
```

Accept only output showing exactly `status: PREPARED`, `proofClaimed: false`,
and the exact source revision. Only after both Step 1 and the prepared check
exit `0`, perform one ordinary logout and later login on the same GUI account.
Manually opening `Chirality.app` is forbidden and is not part of the RunAtLoad
proof. Do not bootstrap or kickstart the label.

### Capture — only after the later login

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_ROOT="/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20"
node projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs capture --session-root "$PROOF_ROOT"
```

### PASS and exact-revision check

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_ROOT="/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20"
PROOF_REVISION="06f60e42e35ea5c39abf9e33c4d3e877d77c4497"
node -e 'const fs = require("fs"); const revision = process.argv[3]; const summary = JSON.parse(fs.readFileSync(process.argv[1], "utf8")); const evidence = JSON.parse(fs.readFileSync(process.argv[2], "utf8")); if (summary.status !== "PASS" || evidence.status !== "PASS") throw new Error("Login proof did not PASS"); if (summary.sourceRevision !== revision || evidence.sourceRevision !== revision) throw new Error("Login proof revision mismatch"); console.log(JSON.stringify({summaryStatus: summary.status, evidenceStatus: evidence.status, sourceRevision: revision}, null, 2));' "$PROOF_ROOT/summary.json" "$PROOF_ROOT/evidence-package.json" "$PROOF_REVISION"
```

### Preserve only the three public files and verify their hashes

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_ROOT="/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20"
PUBLIC_EVIDENCE="/Users/ryan/Desktop/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20-public-evidence"
test ! -e "$PUBLIC_EVIDENCE"
/bin/mkdir -m 700 "$PUBLIC_EVIDENCE"
/usr/bin/install -m 600 "$PROOF_ROOT/prepared.json" "$PUBLIC_EVIDENCE/prepared.json"
/usr/bin/install -m 600 "$PROOF_ROOT/summary.json" "$PUBLIC_EVIDENCE/summary.json"
/usr/bin/install -m 600 "$PROOF_ROOT/evidence-package.json" "$PUBLIC_EVIDENCE/evidence-package.json"
test "$(/usr/bin/stat -f %Lp "$PUBLIC_EVIDENCE")" = "700"
test "$(/usr/bin/stat -f %Lp "$PUBLIC_EVIDENCE/prepared.json")" = "600"
test "$(/usr/bin/stat -f %Lp "$PUBLIC_EVIDENCE/summary.json")" = "600"
test "$(/usr/bin/stat -f %Lp "$PUBLIC_EVIDENCE/evidence-package.json")" = "600"
HASH_LINES="$(cd "$PUBLIC_EVIDENCE" && /usr/bin/shasum -a 256 prepared.json summary.json evidence-package.json)"
printf '%s\n' "$HASH_LINES"
(cd "$PUBLIC_EVIDENCE" && printf '%s\n' "$HASH_LINES" | /usr/bin/shasum -a 256 -c -)
printf '%s\n' 'PASS — exactly three public files preserved mode 0600 and SHA-256 verified'
```

This block refuses an existing destination. It copies only `prepared.json`,
`summary.json`, and `evidence-package.json`; never copy or publish
`.capture-state.json`, `.capture-state.consumed.json`, runtime data, a plist,
or any other private proof state.

### Owner handoff — display and return verbatim

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
set -euo pipefail
PROOF_REVISION="06f60e42e35ea5c39abf9e33c4d3e877d77c4497"
PROOF_LABEL="com.chirality.ci.runatload.login.owner.macos26.00bc8f1a-0045-48a2-970f-be120cf7fc20"
PUBLIC_EVIDENCE="/Users/ryan/Desktop/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20-public-evidence"
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
  "$EVIDENCE_SHA256  evidence-package.json"
```

Paste the complete displayed handoff back verbatim. Do not paraphrase it or
omit any of the three exact hash lines.

## Derivative status, fences, and handoff

This R16 record, the ignored package, instruction-root artifacts, preflight
output, and executor logs are derivative evidence bound to exact source
snapshot `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`; they do not replace source
truth. The unsigned `--dir` package is local build evidence only. No artifact
proof label, DMG, release candidate, release readiness, signing, notarization,
distribution, publication, issuance, certification, or reliance claim exists.

DEL-09-04 remains `IN_PROGRESS` and unproved. Preparation, the ordinary owner
logout/login, capture, returning the complete owner handoff, and owner
acceptance of a passing proof remain open owner acts. Any frontend-tree change,
app-executable hash change, non-absent root/plist/label, nonzero preflight, or
failed procedure gate invalidates this staged procedure and requires a fresh
bounded staging decision. Fresh evidence-only review of this record and status
amendment is required before Git integration.
