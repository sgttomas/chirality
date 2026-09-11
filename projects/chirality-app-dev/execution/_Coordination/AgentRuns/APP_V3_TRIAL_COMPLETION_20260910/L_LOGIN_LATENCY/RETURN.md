# L_LOGIN_LATENCY — RETURN (Type 2 TASK, Fable 5.1)

Branch: `worktree-agent-a4c13aa62ce7808de` (worktree `/Users/ryan/dev/chirality/.claude/worktrees/agent-a4c13aa62ce7808de`, branched from 457397f74).

Commits (all in the worktree, oldest first):

1. `786444477` Hash exact supply once per process and revalidate by filesystem identity
2. `b1d0802da` Revalidate the issued packaged basis by identity at a single boundary
3. `8c68e500e` Establish hosted admission without blocking the status poll
4. (this file) Record the L_LOGIN_LATENCY return

All paths below are under `projects/chirality-runtime`.

## 1. What changed per file

### `packages/core/src/exact-supply.ts`

- Added a per-process digest cache (`digestCache`, bounded to 4096 entries, keyed by canonical path) holding `{ identity, sha256 }`, where identity is the existing `FileIdentity` (dev, ino, size, mtimeNs, ctimeNs, mode).
- `inspect()` (used by `verifyExactSupply`, `createCustomSupplyVerifier.verify`, and the controlled fixture verifier): after the open, the before-`fstat`, and the size check, it looks the path up in the cache; on an identity match it takes the recorded sha256 and skips the read loop, otherwise it hashes as before. The after-`fstat`, path `lstat`, realpath comparison, size and sha256 comparison against the accepted profile all still run; a digest is remembered only after those checks pass.
- `inspectClosure()`: the same per-file cache for closure entries. The closure listing walk (readdir/lstat/realpath of every entry, unlisted-path detection) and every custody check (mode, uid, nlink, size, symlink) still run on every call.
- `revalidateExactSupply` and `verifier.revalidate` are unchanged in shape; because they call `verify`, they now cost one `open`+two `fstat`+`lstat`+`realpath` per file unless the identity changed, and then still require the accepted sha256/size.
- Added `exactSupplyHashPassCountForTests()` (count of full byte-hashing passes) for tests and timing.

### `packages/daemon/src/hosted-packaged-release-state.ts`

- `revalidate()` is now: `requireIssued` → `observePrivateState` → `observeOriginState` → `revalidateTrialSeal`. Removed the full `verifyPackagedRuntimeBasisV2` re-hash, its digest comparison, and the repeated after-observations (see §2).
- `issuedPackagedSupplyVerifierV2` no longer performs a live revalidation; it is the nominal issued-basis gate only (see §2).
- Exported `issuedFilesystemIdentityV2` / `sameIssuedFilesystemIdentityV2` (the registry's own identity record and exact comparison including times) so the loader's trial-seal revalidation uses the same identity model.
- Dropped the now-unused `verifyPackagedRuntimeBasisV2` value import.

### `packages/daemon/src/hosted-packaged-release.ts`

- `inspectTrialSeal` returns `{ observation, observedFiles }`; `observedFiles` is the signed-app inspection's list of file identities (empty for an injected inspector that reports none).
- `revalidateTrialSeal` now re-reads the small `trial-seal-observation.json` (bounded `stablePrivateFile`, sha256 must equal the issued observation) and compares each observed app file by `lstat` identity (`TRIAL_SEAL_SUBJECT_CHANGED` on any change, symlink, or non-file). It no longer re-runs codesign, the fuse scan, or the asar header check.
- Issuance (`loadBasis`) is unchanged: it still runs its initial and final full verification, snapshot, acceptance and signed-app inspection passes once per daemon process.

### `packages/daemon/src/host-account-release.ts`

- `inspectHostAccountSignedPeerIdentity` records `observedFiles`: the identity (via `runtimePhysicalFilesystem().lstat`, bigint) of the app executable, `Electron Framework`, `Info.plist` and `app.asar` after the codesign/fuse/asar checks pass. `VerifiedHostAccountPackagedIdentity.observedFiles` is optional in the type only because the controlled loader seam injects a stub inspector; the production inspector always records it.
- `verifyHostAccountPackagedIdentity`: removed the trailing revalidation after the inspection (see §2). `verifiedInputs` keeps its revalidation immediately before the native add-on load.

### `packages/daemon/src/runtime-conformance-v2-admission.ts`

- `verifyRuntimePurposeReleaseV2`, `revalidateRuntimePurposeReleaseV2`: one basis revalidation before `inspectAcceptedRelease`; the paired after-read is removed.
- `completeRuntimeWorkerInstanceV2FromP2`: removed the trailing `revalidateRuntimeWorkerInstancePreparationV2` + `revalidateRuntimeInstanceAdmissionV2` after `issueRuntimeInstanceAdmissionV2`.

### `packages/daemon/src/codex-login.ts`

- `requireQualifiedLoginPurpose` (v2 branch): structural checks only; the instance revalidation immediately before the grouped spawn in `launch()` is the retained boundary.
- `resolveModelCatalog`: the revalidation before each `model/list` page is kept; the one after the last page, before catalog selection, is removed.
- `status()`: the revalidation before `account/read` is kept; the one after it is removed. The keyring plaintext check after `account/read` is kept.

### `packages/daemon/src/hosted-private-composition.ts`

- Verifier staging path: `verify(source)` → copy if absent → closure custody checks → `verify(staged)` → `assertPackagedSourceFile` + `revalidate(source)`. The `revalidate(staged)` that immediately followed `verify(staged)` is removed.
- Legacy (non-verifier) path: the `revalidateExactSupply(existing)` / `revalidateExactSupply(staged)` that immediately followed `verifyExactSupply(destination)` are removed. `revalidateExactSupply(source)` after the copy is kept.
- `compose()` is textually unchanged; its entry `revalidateReleaseBasis` remains the single live read before `issuedPackagedSupplyVerifierV2`.

### `packages/daemon/src/hosted-bootstrap.ts`

- `status()`: when the ceremony completes with an account, establishment is started via the existing single-flight `establish()` and stored in `state.establishing`, but not awaited. The projection reports `admission: "establishing"` until it settles. A continuation logs `hosted.admission.established` (`elapsedMs`, resulting `admission`) on success, and on failure sets `admissionState = "unavailable"` and logs `hosted.admission.establish_failed` with `elapsedMs` (unchanged event/fields). `state.establishing` is cleared only if it is still the same promise. Sign-out, cancel, close and `invalidateState` still await `state.establishing`.
- `startLogin()`: logs `hosted.ceremony.started` with `elapsedMs` from operation entry to `ceremony.start()` resolving (this spans `createCeremony`, i.e. login startup validation and containment). Records `state.ceremonyStartedAt`.
- The completion poll logs `hosted.ceremony.completed` with `elapsedMs` since the ceremony started.
- Added a `note()` helper (logger `warn`) for non-failure timing events; the daemon logger has no informational level below warn.
- Frontend (`hosted-bootstrap-controller.tsx`): verified, not changed. It already polls every second while `ceremony === 'pending' || admission === 'establishing'` and stops otherwise.

## 2. Removed revalidation calls (each was a duplicate)

| # | Location | Removed call | Why it was a duplicate |
|---|---|---|---|
| 1 | `hosted-packaged-release-state.ts` `revalidate()` | `verifyPackagedRuntimeBasisV2({resourcesRoot})` + digest comparison | Full 1.4 GB re-hash. Owner decision: verify once at issuance, detect drift by identity. `observeOriginState` already covers every payload entry, both manifests, all governance files and the directories by identity. |
| 2 | same | second `observeOriginState`, second `observePrivateState`, second `revalidateTrialSeal` | The "after" half of a before/after pair around #1 with no effect between. |
| 3 | `hosted-packaged-release.ts` `revalidateTrialSeal` | full `inspectTrialSeal` (codesign `--verify --deep` on the app bundle, two `-R` verifications, full Electron Framework read, plutil + asar header) | The signed-app inspection is issuance evidence; per-call repetition is replaced by a small-file re-read plus identity comparison of the four files it read. Any change to them is `TRIAL_SEAL_SUBJECT_CHANGED`. |
| 4 | `hosted-packaged-release-state.ts` `issuedPackagedSupplyVerifierV2` | `revalidateIssuedPackagedReleaseBasisV2(basis)` | Its only caller (`compose()`) performs the same revalidation on the line immediately before; nothing runs between them. |
| 5 | `runtime-conformance-v2-admission.ts` `verifyRuntimePurposeReleaseV2` | trailing `revalidateIssuedPackagedReleaseBasisV2` | After-read of a before/after pair around `inspectAcceptedRelease` (a private-file read, not an effect). |
| 6 | same, `revalidateRuntimePurposeReleaseV2` | trailing `revalidateIssuedPackagedReleaseBasisV2` | Same pattern as #5. |
| 7 | same, `completeRuntimeWorkerInstanceV2FromP2` | trailing `revalidateRuntimeWorkerInstancePreparationV2(preparation)` and `revalidateRuntimeInstanceAdmissionV2(instanceInput, instanceAdmission)` | `issueRuntimeInstanceAdmissionV2` already revalidates the release and the host authority immediately before issuing; only in-memory freezing follows. The leading `revalidateRuntimeWorkerInstancePreparationV2` before authority issuance is kept. |
| 8 | `host-account-release.ts` `verifyHostAccountPackagedIdentity` | trailing `revalidateIssuedPackagedReleaseBasisV2` after the inspection | Its only caller (`verifiedInputs`) revalidates on the very next line before the native add-on load (kept, distinct effect). |
| 9 | `codex-login.ts` `requireQualifiedLoginPurpose` (v2) | `revalidateRuntimeInstanceAdmissionV2` | `launch()` revalidates the same admission immediately before `spawnGroupedSupplier`, with only launch-argument derivation between. The keyring, consent and containment checks are untouched. |
| 10 | `codex-login.ts` `resolveModelCatalog` | `revalidateRuntimeInstanceAdmissionV2` before catalog selection | No supplier effect follows it (selection is in-memory, then close). The pre-request revalidation of every `model/list` page is kept. |
| 11 | `codex-login.ts` `status()` | `revalidateRuntimeInstanceAdmissionV2` after `account/read` | After-read of the pair around `account/read`; the pre-read one is kept. |
| 12 | `hosted-private-composition.ts` staging (verifier path) | `supplyVerifier.revalidate(staged)` | Immediately follows `supplyVerifier.verify(staged)` on the same path with nothing between. |
| 13 | `hosted-private-composition.ts` staging (legacy path) | `revalidateExactSupply(existing)` and `revalidateExactSupply(staged)` | Each immediately follows `verifyExactSupply(destination)` with nothing between. |

Kept on purpose: every check that gates a distinct effect (native add-on load, worker/login spawn, `account/login/start`, `account/read`, each `model/list` page, materialization publication, logout). Also kept: the in-memory `revalidateHostedAccountAuthorityV2` before/after pairs inside `issueRuntimeInstanceAdmissionV2` and `revalidateRuntimeInstanceAdmissionV2` — they are lease-liveness comparisons, not filesystem reads, and the D36 liveness-during-final-read tests rely on them.

Not changed (left open): `loadBasis` still runs two full `verifyPackagedRuntimeBasisV2` passes and two signed-app inspections at issuance (one-time, about 4 s at daemon start); `createVerifiedHostAccountClient` / `createVerifiedHostAccountAuthority` still run the codesign inspection each time they are called.

## 3. Identity-cache design

**Packaged basis.** Nothing new is cached: the registry already stored, at issuance, the identity (`dev, ino, size, mode, uid, nlink, mtimeNs, ctimeNs`) of every payload entry (files and directories), both manifests, the governance files, the four directories, and the sha256 + identity of the private records (anchor, six purpose snapshots, seal observation). `revalidate()` now consists only of those observations: `realpath` + `lstat` per origin entry compared exactly (times included), the private directory chain custody checks, and a bounded `readIssuedPrivateFileV2` of each private record (sha256 and identity). Any difference is `PACKAGED_RELEASE_BASIS_CHANGED` exactly as before. The trial seal adds the observation record re-read and the identity of the four signed-app files recorded by the production inspector.

**Supplier.** `exact-supply.ts` keeps a process-wide `Map<canonicalPath, { identity, sha256 }>` (bounded, insertion-order eviction). `verify` for a given path hashes on the first call and on any identity change; a hit requires all six identity fields to match the recorded ones (ctimeNs cannot be set from user space, so in-place rewrites and metadata restoration are visible). A hashed digest is remembered only after the after-`fstat`/`lstat`/`realpath` identity checks and the accepted sha256/size comparison pass, so a rejected verification never seeds the cache. The source supplier and the private staged copy are different canonical paths, so each is hashed once per process. `revalidate(descriptor)` = `verify` (identity hit) + comparison of the descriptor's recorded identity/closure identities with the current ones, so a stale descriptor after a replacement is rejected without a byte read.

**Staging (item 3).** In the same daemon process a second ceremony calls `verify(source)` (identity hit), finds the staged file present, runs the closure custody checks, `verify(staged)` (identity hit), and `revalidate(source)` (identity hit): zero payload bytes read. A replaced or rewritten staged file changes identity: `verify(staged)` re-hashes it and, if the bytes differ from the accepted profile, rejects; if the bytes are identical the fresh verification passes and the login proceeds on those verified bytes, while any earlier descriptor for it is rejected on `revalidate`.

## 4. Test changes

| File | Change | Justification |
|---|---|---|
| `tests/exact-supply.test.ts` | New: "hashes a path once per process, answers later verifications from filesystem identity, and still detects a replaced executable" | Brief (b): same path twice reads once (hash-pass counter), replaced inode with different bytes re-hashes and rejects, rewrite re-hashes once, stale descriptor rejected without a read. |
| `tests/exact-supply.test.ts` | New: "re-uses custom closure digests by identity while still walking the closure and rejecting a rewritten closure file" | Closure cache: two hash passes on first verify, zero on repeat, unlisted file still rejected, same-length rewrite of a closure file re-hashed and rejected. |
| `tests/hosted-packaged-release.test.ts` | "retains and revalidates the signed-peer observation": `inspect` call count 4 → 2, and still 2 after the rejected revalidation | Single-boundary model: the inspector runs at issuance (initial + final pass) only; a changed observation record is still rejected without re-inspection. |
| `tests/hosted-packaged-release.test.ts` | Pass-through `vi.mock("node:fs/promises")` recording `open`/`readFile` paths while `reads.recording` is set | Needed to prove "no payload byte re-read" (the physical filesystem object is frozen and cannot be spied). All other tests in the file run through the unchanged pass-through. |
| `tests/hosted-packaged-release.test.ts` | New: "revalidates an issued basis by identity without re-reading payload bytes, and still rejects rewritten or replaced payload files" | Brief (a): two revalidations open nothing under the Resources root and never call `verifyPackagedRuntimeBasisV2`; an in-place rewrite of `supplier/codex` and a same-byte inode replacement of the native add-on are `PACKAGED_RELEASE_BASIS_CHANGED`. |
| `tests/helpers.ts` | New `settledHostedBootstrapStatus(client, projectId)` | Polls while `admission === "establishing"`, the loop the frontend controller runs. |
| `tests/hosted-bootstrap-integration.test.ts` | Eight first-poll-after-login assertions now go through `settledHostedBootstrapStatus` (sign-out test; native Plan test; multi-project: signed-in-only, first, second; manifest drift; catalog test twice) | Item 4: `ready`/`unavailable` is reached on a later poll, not inside the first status call. Assertions themselves are unchanged. |
| `tests/hosted-bootstrap-integration.test.ts` | New: "reports establishing without blocking the poll, ready once establishment settles, and unavailable after a failed establishment" | Brief (d): with establishment gated, the first two polls return `establishing` (a blocking call could not return), one establishment call, `ready` after release, `hosted.ceremony.started/completed` and `hosted.admission.established` with `elapsedMs`; a failed establishment shows `unavailable` on a later poll with `hosted.admission.establish_failed` + `elapsedMs`; no auth URL in the log. |
| `tests/codex-primary-chat-integration.test.ts` | One first-poll assertion → settled helper | Same as above. |
| `tests/hosted-private-composition.test.ts` | One first-poll assertion → settled helper | Same as above. |
| `tests/d36-v2-connected.test.ts` | One first-poll status read (concrete P2 lease test) → settled helper | Same as above. No D36 drift test was deleted or weakened: all 32 pass; their drift injection runs through the mocked `revalidateIssuedPackagedReleaseBasisV2`, which still fires at every retained boundary. |

## 5. Build, typecheck, suite

Run from `projects/chirality-runtime` with node 24.18.0 (`/Users/ryan/.local/share/mise/installs/node/24.18.0/bin`), dependencies installed offline (`npm ci --offline`).

- `npm run build`: passes.
- `npm run typecheck`: passes.
- `npx vitest run` (full): 82 files, 1085 passed, 2 failed, 14 skipped (26.96 s wall).
  - `tests/hosted-private-composition.test.ts` "connects public bootstrap through real same-actor admission…": timed out at 5000 ms under load — the known load-only flake named in the brief. Alone / in the six-file focused run the file passes 10/10.
  - `tests/d36-v2-connected.test.ts` "rejects retained same-actor account change after acquire before model effects": `ENOTEMPTY: directory not empty, rmdir …/runtime/private` — raised by the test's own `afterEach` `rm(root, { recursive: true })` racing a still-retiring worker under load. Alone the file passes 32/32 (three consecutive runs). Under a seven-file load loop with this branch it failed in 2 of 3 runs; the same loop against the unmodified baseline (457397f74 package and test trees checked out into this worktree, rebuilt) failed the same test with the same `ENOTEMPTY` in 1 of 3 runs, so the race is pre-existing and load-dependent, not introduced here. No test was changed to hide it.
  - `tests/supervisor.test.ts` "bounds worker lifetime…" (the other known flake) passed.
- Focused runs of the files touched by this work (`hosted-packaged-release`, `exact-supply`, `runtime-conformance-v2-admission`, `host-account-lifecycle`, `codex-login`, `hosted-private-composition`, `hosted-bootstrap-integration`, `d36-v2-connected`, `codex-primary-chat-integration`): all pass.

## 6. Before/after cost against the R8 resources root (read-only)

Measured with a scratch script importing the built `packages/core/dist` against `/Users/ryan/Applications/Chirality Trial 20260910 R8.app/Contents/Resources` (599 payload entries; supplier closure = directory + 757,506,928-byte `codex`). Nothing under the app, the R8 userdata or LaunchAgents was written or executed; no codesign was run (the trial-seal codesign cost is therefore not in these numbers).

| Operation | Before model | After model |
|---|---|---|
| Packaged release: one `verifyPackagedRuntimeBasisV2` full re-hash | 1912 ms cold, 1790 ms warm (each previous `revalidate()` ran it once, plus two rounds of observations and two signed-app inspections) | not run |
| Packaged release: identity walk over all 610 origin entries (what `revalidate()` now does, besides the small private-record reads) | (also ran, twice) | 4.6–5.2 ms |
| Supplier: first `verify` of the packaged 757 MB closure (hashes) | 500 ms warm page cache (brief measured about 2 s cold) | 500 ms, once per process per path |
| Supplier: second `verify` / `revalidate` of the same path | 500 ms each | 0.5 ms each, 0 hash passes |

So one `revalidate()` of the issued basis goes from roughly two full re-hash passes plus two signed-app inspections (about 4 s plus codesign) to about 5 ms plus eight small-file reads, and one supply `verify()` after the first goes from about 0.5–2 s to about 0.5 ms.

## 7. Left open

- `loadBasis` still hashes the release twice and inspects the signed app twice at issuance (one-time, about 4 s of daemon start).
- `createVerifiedHostAccountClient` / `createVerifiedHostAccountAuthority` still run the codesign inspection on each call; caching it by the same file identities would be a further, separate change.
- The D36 `ENOTEMPTY` afterEach race under load (see §5).
- No timing was taken from a live daemon; the next trial's `hosted.ceremony.started` / `hosted.ceremony.completed` / `hosted.admission.established` logs will carry the end-to-end numbers.
