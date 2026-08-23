# Sealed brief — A2-PKG09-R18-IMPLEMENT-04

## Identity and accepted basis

- RequestedBy / Parent: `WI-PKG09-R18-STAGING-01`
- RunID: `APPDEV_LOGIN_PROOF_R18_STAGING_2026-08-22`
- ChildInstanceID: `A2-PKG09-R18-IMPLEMENT-04`
- Fresh ephemeral generalist Agent 2; no delegation
- Package / deliverable: `PKG-09` / `DEL-09-04`
- Required branch/HEAD:
  `codex/app-login-proof-r18-staging` /
  `f59105ddb606bd46397c3b1aafa41b50ab4e9e8d`
- Required HEAD parents:
  `166efa82748133e90674be62304b81f8a0a8c1b4` and
  `b143444bd497eae1b1b638670a33e6df756d9084`
- No network authority. No nested delegation.

## Objective and write ownership

Implement the Electron supply freeze, validate it, run exactly one offline
evidence package command, author R18 and minimal status, and return frozen
candidate bytes for fresh review.

Sole allowed overlapping writes:

- `frontend/scripts/verify-electron-dist.mjs`;
- one robust `frontend/scripts/` pack wrapper if needed;
- `frontend/package.json` and only mechanically required lock consistency;
- focused tests under `frontend/src/__tests__/scripts/` and/or existing
  packaging-policy tests;
- DEL-09-04 `_run_records/R18_ELECTRON_SUPPLY_FREEZE_AND_OFFLINE_BUILD_2026-08-22.md`;
- minimal DEL-09-04 `_STATUS.md` amendment;
- unique `instances/WI-PKG09-R18-STAGING-01/executor-4/` evidence/return.

Preserve attempts 1/2, network-3, all v1-v4 manager files, R16/R17, prior
records, receipts, and other source. Do not write Receipt 189.

## Accepted evidence and required inspection

- Official full SHASUMS response:
  `executor-3/SHASUMS256.txt`, SHA-256
  `823ec97893f00c3ab2a4d44811bc75f7dd582ff6086407109a179c2184c5702d`.
- Exact official line:
  `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28 *electron-v43.2.0-darwin-arm64.zip`.
- Source URL is the exact GitHub URL recorded in owner direction.
- Owner-staged default directory:
  `/Users/ryan/Library/Caches/chirality/electron-dist`; inspect read-only and
  require archive regular/non-symlink, size `122090802`, streaming SHA-256
  `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`.
- Resolve the active nested
  `frontend/node_modules/app-builder-lib/node_modules/@electron/get` package;
  require version 3.1.0 and record exact source file SHA-256/line region showing
  SHASUMS retrieval with `cacheMode: Bypass`. Record that top-level 5.0.0 is
  unrelated to Electron Builder's active path.

## Implementation

1. Add `frontend/scripts/verify-electron-dist.mjs`. Production constants pin
   Electron 43.2.0, exact filename, 122090802 bytes, official hash, verbatim
   official line and source URL. Read package.json and fail on any Electron
   devDependency version drift. Resolve explicit `CHIRALITY_ELECTRON_DIST_DIR`
   literally; otherwise use `os.homedir()` plus fixed
   `Library/Caches/chirality/electron-dist`. Reject empty/NUL/malformed/unsafe
   path conditions. Require directory/archive lstat-safe, regular,
   non-symlink, containment/realpath safe, exact size/hash. Stream hash; never
   buffer the 122 MB archive. Success stdout is only the resolved directory;
   failures are stderr/nonzero.
2. Tests may use safe internal seams/fixtures only if production constants and
   CLI cannot be overridden. Cover success stdout-only plus missing, archive
   symlink, wrong size, wrong hash, Electron version drift, unsafe path and no
   pin bypass without repeatedly hashing 122 MB.
3. Keep npm script name `desktop:pack` and its existing build,
   dependency-boundary, and instruction-root gates. Add
   `electron:supply-chain`. Use a robust wrapper/argv construction that first
   obtains the verified directory and passes exactly one
   `-c.electronDist=<directory>` argument to electron-builder, including paths
   with spaces. No shell interpolation/injection. Add a focused test proving
   exact argv/path-space behavior. Do not broaden `desktop:dist`.

## Checks and exactly one offline evidence build

Before build run focused new tests, syntax and typecheck sufficient to catch
implementation defects. Run production verifier against the staged default.
Initialize full build log/exit evidence before executing exactly one new:

```text
npm run desktop:pack
```

Run in the ordinary network-denied sandbox, no escalation, no retry. Require
exit zero, exact `using custom electronDist directory` evidence, no download
indicator, and embedded dependency-boundary/instruction-root gates. The
ignored `dist` output is evidence only: do not adopt it, package-identity it,
or stage a proof procedure.

After build run focused tests, syntax, typecheck, full frontend suite,
package JSON/lock consistency, instruction-root integrity, APP-HOLD,
self-check, practitioner suite, prior-ledger receipt validator, candidate/new
file whitespace, `git diff --check`, App-only containment, exact inventory/
hashes, and empty index. No second pack attempt even if it fails.

## Records

R18 must record: first cache-miss attempt and incomplete-log limitation;
attempt-2 terminal redirect; accepted attempt-3 official full-body hash/exact
line/two-host chain; synced merge basis; active local `@electron/get` cause;
staged archive gates; verifier/wrapper/tests; one offline evidence build and
full log; explicit non-adoption/no-proof posture; R19 separate after merge.

Update status minimally: R17 repair merged; R18 is supply-freeze precursor and
offline evidence only; DEL remains `IN_PROGRESS`/unproved; R19 requires
separate post-merge authorization. No owner procedure or proof acceptance.

## Fences and return

No network, second build, artifact/source update beyond allowed files, package
or proof adoption, R19 procedure, GUI, prepare/capture/logout/login,
bootstrap/kickstart, operator/default job/plist/launcher action,
sign/notarize/deploy/distribute/release/proof claim, Receipt 189,
stage/commit/push/PR/merge, or delegation.

Return exact changed paths/hashes, source citation/hash/lines, tests/checks,
build command/log/exit and no-download proof, blockers/reruns, derivative
status, and fresh-review requirement.
