# A2-PKG09-R18-REVIEW-01 fresh evidence review

Verdict: `VALIDATED_PASS_WITH_ENVIRONMENT_LIMITATION`

The complete frozen R18 candidate has no actionable finding. The one required
reviewer full-frontend run is explicitly **not PASS**: it exited 1 with exactly
21 failed tests, 1,246 passed tests, and 4 skipped tests. Every failed test is
independently bound to the ordinary sandbox's prohibition on local TCP or Unix
socket listening, before any R18 candidate path can participate.

## Basis, freeze, and containment

- Branch/HEAD: `codex/app-login-proof-r18-staging` /
  `f59105ddb606bd46397c3b1aafa41b50ab4e9e8d`.
- Exact parents: `166efa82748133e90674be62304b81f8a0a8c1b4` and
  `b143444bd497eae1b1b638670a33e6df756d9084`; current `origin/main` was the
  second parent at review start.
- The seven frozen candidate hashes in `MANAGER_CANDIDATE_FREEZE_V4.md` all
  match. `frontend/package-lock.json` remains unchanged at
  `717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458`.
- The non-review run root contains exactly 38 files. Candidate changes are the
  two tracked modifications plus five untracked candidate files named by the
  freeze; all are under `projects/chirality-app-dev/`. The index is empty.
- Candidate/new-file whitespace, `git diff --check`, App containment, and
  empty-index checks pass. Review writes are confined to `review-1/`.
- APP-HOLD scan reports 53 matching clear contracts; the exact DEL-09-04
  reliance gate returns `ALLOW` / `NOT_HELD`.

## Attempts and accepted official evidence

- Attempt 1 remains a calibrated failed cache-miss record: one offline
  `desktop:pack`, exit 1 at `getaddrinfo ENOTFOUND github.com`, incomplete full
  log explicitly disclosed, no retry or R18 adoption.
- Attempt 2 remains a calibrated terminal redirect record: one GitHub request,
  HTTP 302, no redirect followed, zero-byte body, sanitized retained headers,
  no implementation or build.
- Attempt 3 evidence proves one curl invocation and exactly two HTTPS requests:
  `github.com` 302 then `release-assets.githubusercontent.com` 200, one
  redirect, 7,610-byte ASCII body, SHA-256
  `823ec97893f00c3ab2a4d44811bc75f7dd582ff6086407109a179c2184c5702d`.
  The required arm64 line occurs exactly once. Retained headers replace the
  signed query with `[SIGNED_QUERY_REDACTED]`; no artifact or other-host
  request is recorded. The interrupted executor's pending prose is not used
  as a terminal claim; the manager's deterministic fan-in is calibrated.

## Supply input and active cause

- Read-only inspection establishes the owner-staged directory as a regular,
  non-symlink directory and its archive as a regular, non-symlink
  122,090,802-byte file. Streaming SHA-256 is
  `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`.
  Realpaths equal the literal paths; no mutation was performed.
- Electron Builder's resolved nested `@electron/get` is exactly 3.1.0. Its
  `dist/cjs/index.js` hash is
  `d81c9a2354bb2769b4d8205b04c991aef2e93b79e7e3d1e792663aee5813ac4f`;
  lines 59-70 retrieve `SHASUMS256.txt` with
  `ElectronDownloadCacheMode.Bypass`. The top-level 5.0.0 installation is not
  the nested dependency used by `app-builder-lib`.

## Security and package review

- Production pins cover Electron 43.2.0, exact filename, exact size, official
  hash, verbatim official line, and exact official URL; package Electron drift
  fails closed.
- Explicit `CHIRALITY_ELECTRON_DIST_DIR` is consumed literally; otherwise the
  fixed home-relative directory is used. Empty, NUL, relative, non-normalized,
  and root paths fail. Directory and archive lstat, realpath, containment,
  type, non-symlink, size, and streaming-hash gates are fail closed.
- CLI success writes only the verified directory to stdout. CLI failures write
  to stderr and return nonzero. No CLI pin or package-path override exists.
  Exported fixture seams cannot alter the production CLI or package-script
  call graph and are not an actionable bypass.
- Packaging verifies first, uses `shell: false`, and passes exactly one
  `-c.electronDist=<verified directory>` argv element; spaces remain in one
  argument. The package-script's npm context resolves the local
  `electron-builder`. `CSC_IDENTITY_AUTO_DISCOVERY=false` is preserved.
- `desktop:pack` keeps its name and its build, packaged-dependency, and
  instruction-root gates. `electron:supply-chain` is added; `desktop:dist` and
  the lockfile are unchanged. No production caller bypass is present.

## Independent checks

| Check | Reviewer result |
|---|---|
| verifier/wrapper syntax | PASS |
| focused verifier/wrapper tests | PASS, 9/9 |
| frontend typecheck | PASS |
| production staged-archive verifier | PASS |
| offline package/lock dry-run consistency | PASS, up to date |
| instruction-root integrity to review-owned output | PASS, 43 files, exact HEAD |
| APP-HOLD scan and DEL-09-04 reliance gate | PASS |
| practitioner self-check | PASS at its calibrated non-blocking baseline |
| practitioner pytest | PASS, 350/350 |
| prior-ledger receipt validator | PASS; ledger unchanged |
| whitespace/diff/containment/index | PASS |
| full frontend Vitest, exactly once | **NOT PASS — ENVIRONMENT-LIMITED**, exit 1; 21 failed, 1,246 passed, 4 skipped |

## Exact full-suite failure classification

All names below are copied from `full-vitest.log`.

`src/__tests__/integration/pi-omlx-wire.integration.test.ts` — each of these
11 tests fails at the fake provider's `server.listen(0, '127.0.0.1')` with
`Error: listen EPERM: operation not permitted 127.0.0.1`:

1. `discovers the exact model, executes one governed read tool, persists evidence, and finishes canonically`
2. `fails closed for bad authentication, empty/unknown models, malformed discovery, and redirects`
3. `maps 'malformed SSE JSON' to one redacted canonical failure and releases the turn`
4. `maps 'context exhaustion' to one redacted canonical failure and releases the turn`
5. `maps 'mid-stream disconnect' to one redacted canonical failure and releases the turn`
6. `maps 'completion redirect' to one redacted canonical failure and releases the turn`
7. `fails a malformed tool call without invoking the governed tool`
8. `interrupts a hung stream deterministically and emits one interrupted terminal outcome`
9. `times out a hung provider stream, aborts it, and releases the adapter for a later turn`
10. `recovers on a later turn after a disconnected provider and server restart`
11. `keeps a scripted Claude parent and real Pi child isolated during concurrent targeted interruption`

`src/__tests__/lib/omlx-provider-config.test.ts` — each of these six tests
fails at `server.listen(0, '127.0.0.1')` with the same TCP `listen EPERM`;
`Server is not running` is a secondary cleanup consequence of that denied
listen:

12. `discovers exact model IDs with the oMLX bearer key`
13. `refuses redirects before following them`
14. `returns a typed and redacted error for HTTP 401`
15. `returns a typed and redacted error for HTTP 403`
16. `returns a typed and redacted error for HTTP 500`
17. `types malformed, empty, unknown-model, and offline failures without key leakage`

The remaining four fail before their asserted behavior when local runtime
listening is denied:

18. `src/__tests__/integration/runtime-canonical-replay-restart.integration.test.ts` — `lazily preserves legacy manager/child records and replays one canonical hierarchy`: Unix control-socket `listen EPERM` at `RuntimeDaemon.start`.
19. `src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts` — `shares one daemon, project credential, and session across both public clients`: Unix control-socket `listen EPERM` at `RuntimeDaemon.start`.
20. Same file — `persists exactly one terminal outcome when daemon restart interrupts an in-flight model drain`: Unix control-socket `listen EPERM` at `RuntimeDaemon.start`.
21. Same file — `rejects a CLI turn with the typed shared-session lock while Desktop is active`: fake-provider TCP `listen EPERM 127.0.0.1` before daemon/session assertions.

None of the four failing files imports or executes either new supply script,
and the candidate modifies no runtime/provider/socket implementation. The
error sites are the same prior known local-bind class recorded by executor-4.
Therefore every failure is unrelated environment-only evidence; the suite is
not upgraded to PASS and no unsandboxed rerun is requested or performed.

## Single package evidence, records, and fences

- Executor-4 initialized evidence and made exactly one post-implementation
  `npm run desktop:pack` attempt. Exit is 0; the 15,849-byte complete log has
  SHA-256
  `e7f1ec32a50444c260697ca5bd9e4b10325cf4a1e61d95831331173f84f49b9f`.
  It records Electron Builder 26.15.3, Electron 43.2.0 arm64, the exact custom
  electronDist directory, dependency-boundary PASS, instruction-root pass,
  43 files, and exact HEAD. A case-insensitive scan has no `download`,
  `github.com`, or `release-assets.githubusercontent.com` indicator.
- Observed package/main/CLI hashes remain evidence-only and non-adopted. This
  reviewer did not rerun packaging.
- R18 and `_STATUS.md` accurately preserve attempts 1/2/3, official evidence,
  sync, implementation/checks/build, the local-bind limitation, R17 merged,
  `IN_PROGRESS`/unproved state, and R19 as a separate post-merge owner act.
  No owner procedure or proof is accepted.
- The retained corpus and candidate contain no post-attempt-3 network, second
  post-implementation pack, R19, GUI, prepare, capture, logout/login,
  bootstrap, kickstart, operator/default job mutation, signing, notarization,
  deployment, distribution, release claim, Receipt 189, staging, commit, push,
  PR, or merge act.

## Review evidence hashes

- `full-vitest.log`: `7e0907732af579802a927d09028b301cc167b1ec83fc490e7d1fc61bd1220dab`
- `focused-tests.log`: `580ad49f26036c10c70fb6b13fea8e4e8fb0d7244112d0c70885834cdc55338b`
- `typecheck.log`: `dc2149dec385adf46be71c88c67ddcf056f04bdcdba97507bdc9056781a90d1f`
- `production-verifier.log`: `5af72fdf79d96a79f68b7d81b118f437d266c0b73e803ac6b8e567cba1ce20ae`
- `package-lock-consistency.log`: `e9313dd7224771d4b9d5f9d0e545a3a83f5b7590e5ffde22cbde7834fdad3c06`
- `instruction-root-integrity.log`: `fc655ba608e142a236b03f3a52d6d5e31fb02f4d39d51f02328ae50e63c15bfa`
- `instruction-root-integrity/manifest.json`: `f773070b3117df247cf63ae31ca711b2e1e703636a14ad406722172b0597222e`
- `instruction-root-integrity/summary.json`: `cd46a37faebaf859a5163c9ced74c8798e61b6fd3fe77ba260d6540b352535eb`
- `app-hold.log`: `f39d3ffdb2ad410fe32420e0919ccdb7ee7c74ac3aef85e889e74ec16a14723d`
- `app-hold-reliance.log`: `76dd3a863c9237ea48a213fcec5300a6abf5e8213eebd4c346c4856ed54a3495`
- `self-check.log`: `67ac9305b5be5cc2b71e1c2a9b5f3b5bfb32173e803ac6b8e567cba1ce20ae`
- `practitioner-pytest.log`: `833377099f98a92f9293dbbd3354a3a84cc88aa50a27237333c925ce55e15ff8`
- `receipt-validator.log`: `f8409bcfe80bcd62109d9f6b58ab81437528f88c6d1d2c0f474b86268fcca924`

## Return and rerun requirements

No repair cycle is required. Manager fan-in may accept
`VALIDATED_PASS_WITH_ENVIRONMENT_LIMITATION` while preserving full Vitest as
not PASS. Any candidate-byte change requires affected deterministic checks and
a fresh evidence-only reviewer. The package command remains consumed and must
not be repeated. R19/proof preparation remains separately owner-authorized
after merge.
