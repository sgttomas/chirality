# Sealed brief — A2-PKG09-R18-WP02-EXECUTE-02

## Identity and objective

- RequestedBy / ParentInstanceID: `WI-PKG09-R18-STAGING-01`
- RunID: `APPDEV_LOGIN_PROOF_R18_STAGING_2026-08-22`
- ChildInstanceID: `A2-PKG09-R18-WP02-EXECUTE-02`
- Agent type: fresh ephemeral generalist Agent 2; no delegation
- Package / deliverable: `PKG-09` / `DEL-09-04`
- Basis: branch `codex/app-login-proof-r18-staging`, exact unchanged
  `HEAD == origin/main == 166efa82748133e90674be62304b81f8a0a8c1b4`, plus
  only this existing untracked run root.
- Objective: freeze Electron 43.2.0 darwin-arm64 supply, prove one offline
  evidence build, and record R18/status without adopting a proof package or
  staging R19.

## Reads and write ownership

Read all v1/v2 run-root instructions and prior failure evidence; current
WORKING_ITEMS/TASK/App loop/profile; Receipt 188; DEL status/R16/R17; R17
source/tests; packaging docs/scripts/package manifests; verifier precedent
`frontend/scripts/verify-pi-supply-chain.mjs`; owner-staged exact dist; and
repo-local Electron Builder-resolved `@electron/get` source. No delegation.

Allowed repository writes are only:

- `frontend/scripts/verify-electron-dist.mjs`;
- one robust tracked pack wrapper under `frontend/scripts/` if needed;
- `frontend/package.json` and only mechanically required lock consistency;
- focused tests under `frontend/src/__tests__/scripts/` or the existing
  packaging-policy test;
- DEL-09-04 `_run_records/R18_ELECTRON_SUPPLY_FREEZE_AND_OFFLINE_BUILD_2026-08-22.md`;
- minimal DEL-09-04 `_STATUS.md` amendment;
- unique `instances/WI-PKG09-R18-STAGING-01/executor-2/` evidence/return.

Do not rewrite prior attempt evidence or any v1/v2 manager control file.

## Single network request

Before source edits, initialize `executor-2/` evidence. Then make exactly one
request using `/usr/bin/curl` to:

`https://github.com/electron/electron/releases/download/v43.2.0/SHASUMS256.txt`

Use HTTPS only, redirects disabled (no `-L`, max redirects zero), fail on HTTP
error/redirect, and write the complete text response from that single request
plus exit/headers metadata without a second request. Request escalation only
for this exact curl command. No other URL, host, or request; no artifact
download. If it fails or redirects, stop without implementation. On success,
require plausible text size near 7.4 KB, exactly one verbatim line for
`electron-v43.2.0-darwin-arm64.zip`, and exact expected SHA-256
`ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`.

## Supply verifier and pack integration

1. Independently `lstat` the default owner-staged
   `/Users/ryan/Library/Caches/chirality/electron-dist/electron-v43.2.0-darwin-arm64.zip`;
   require regular/non-symlink, exact `122090802` bytes, and streaming SHA-256
   equal to the official line. Do not alter it.
2. Resolve the actual nested `@electron/get` used by `app-builder-lib`; record
   version 3.1.0, source package/path, exact source SHA-256 and line region
   proving SHASUMS retrieval with `cacheMode: Bypass`. Distinguish top-level
   5.0.0 and do not cite it as the active cause.
3. Implement `verify-electron-dist.mjs`. Production constants include pinned
   Electron version, exact official line/source URL, filename, byte size and
   hash. Require package.json Electron devDependency exact match; default only
   from `os.homedir()` plus the fixed suffix; explicit env path is literal.
   Use lstat/realpath-safe regular/non-symlink validation, reject malformed or
   unsafe conditions, stream hash, print only resolved directory on success,
   stderr/nonzero on error. Caller/test inputs cannot bypass production pins.
4. Preserve `desktop:pack` name and all existing build, dependency-boundary,
   and instruction-root gates. Add `electron:supply-chain`. Use a wrapper or
   equivalent robust argv construction so the single verified directory is
   passed as one `-c.electronDist=<dir>` argument even with spaces. Tests must
   prove pack argv and path spaces. Do not change `desktop:dist` unless required
   by explicit scope (it is not authorized here).
5. Add focused fail-closed tests for missing, symlink, wrong size, wrong hash,
   version drift, no production-pin bypass, success stdout-only contract, and
   pack argument/path spaces. Avoid repeatedly hashing the 122 MB archive;
   test seams/fixtures must not weaken production pins.

## One offline evidence build and records

After implementation/tests pass, run the verifier against the staged default,
then run exactly one new `npm run desktop:pack` in the ordinary network-denied
sandbox, with no escalation/retry. Initialize and preserve its full combined
log and exit first. Require exit zero, `using custom electronDist directory`,
no download indicators, and embedded dependency/instruction-root checks. The
ignored build overwrites dist but is evidence only and is not adopted or
package-identity/proof verified.

Write R18 with: first cache-miss attempt and evidence limitation; verified
active-source cause and citation; exact official line/source/single-request
evidence; staged zip gates; implementation/tests; one offline build evidence;
non-adoption/no-proof posture; R19 separate after merge. Update status minimally:
R17 merged, R18 supply-freeze precursor/evidence only, DEL `IN_PROGRESS` and
unproved, R19 separate. Do not stage an owner procedure or write Receipt 189.

## Validation and return

Run focused tests, syntax, typecheck, full frontend, package JSON/lock
consistency, instruction-root integrity, APP-HOLD, self-check, practitioner
suite, prior-ledger receipt validator, candidate/new-file whitespace,
`git diff --check`, App-only containment, exact inventory/hashes, and empty
index. Return exact request/build counts, source citations, hashes, checks,
blockers/reruns, derivative posture, and frozen paths for fresh review.

## Fences

No second network request, redirect/other host, artifact download, second
build/retry, proof package adoption, R19 procedure, GUI, prepare, capture,
logout/login, bootstrap, kickstart, operator/default job/plist/launcher action,
sign/notarize/deploy/distribute/release/proof claim, Receipt 189, stage, commit,
push, PR, merge, or nested delegation.
