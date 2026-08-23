# Executor return — A2-PKG09-R18-EXECUTE-01

## Result

`FAILED — OFFLINE ELECTRON 43.2.0 CACHE MISS / DOWNLOAD ATTEMPT; R18 NOT STAGED`

- Parent: `WI-PKG09-R18-STAGING-01`
- Package / deliverable: `PKG-09` / `DEL-09-04`
- Branch: `codex/app-login-proof-r18-staging`
- required and unchanged `HEAD` / `origin/main`:
  `166efa82748133e90674be62304b81f8a0a8c1b4`
- index and tracked worktree: empty
- proof status: not run; DEL-09-04 remains `IN_PROGRESS` and unproved
- derivative status: failed local build evidence only; no R18 package or proof

## Terminal build failure

From exact cwd
`/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend`,
the exact tracked command `npm run desktop:pack` ran once under the ordinary
restricted sandbox with `npm_config_offline=true`. It completed the Next,
Electron, and runtime-CLI build stages. Electron Builder `26.15.3` then reached
packaging for pinned Electron `43.2.0`, macOS arm64, and exited `1` with
`getaddrinfo ENOTFOUND github.com`.

The transcript printed no retrieval URL. It identified only the DNS target
`github.com` and the exact error `getaddrinfo ENOTFOUND github.com`; no more
specific URL is inferred.

This is the sealed brief's terminal cache-miss/download-attempt condition. No
retry, network escalation, dependency/provider change, or alternate package
command occurred. The embedded `desktop:verify-dependencies` and
`instruction-root:integrity` stages were not reached.

The intended full combined log was not persisted: the tee destination did not
exist because the preceding evidence-initialization command stopped before
directory creation on an expected-service-text quoting defect. The full output
is retained only in the governed execution transcript. The bounded summary is
`executor/desktop-pack.failure-summary.log`; the exit file is
`executor/desktop-pack.exit-status.txt`. This evidence defect is explicit and
requires a fresh executor run after the cache condition is lawfully resolved.

## Package and integrity posture after failure

The ignored app path still exists, but it is **not adopted as R18**. Its current
main and CLI hashes are exactly the prior R16 identities:

- main executable:
  `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`;
  thin arm64 Mach-O;
- packaged runtime CLI:
  `0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`.

The current instruction-root outputs also remain the prior R16 evidence, not
R18: summary SHA-256
`89ba0e597190205fd50e1216e9efeb9f6ea9dd53e920a27f31251ad8cfb5b468`,
manifest SHA-256
`dfea68cf9b550848d5573a02c73b6647700e0543b6376bb61831c3d38d1c75d1`,
and summary Git SHA
`06f60e42e35ea5c39abf9e33c4d3e877d77c4497`. Therefore no exact-merge
package, CLI, instruction-root, codesign, or packaged-guard identity exists
for R18.

Post-failure bounded enumeration found the pre-existing ignored
`dist/mac-arm64/Chirality.app`, DMG, blockmap, and builder-debug entries. The
command reached `appOutDir=dist/mac-arm64`, but no pre-command whole-`dist`
inventory or tree hash was authorized or frozen, so this return cannot
determine whether arbitrary ignored `dist` entries were removed or partially
recreated. It can establish that the intended app's main executable and
runtime CLI still match the exact prior R16 hashes above. Those surviving
bytes are not an R18 rebuild and are not adopted.

Committed R17 source identities at the failed build basis remain:

| Path | SHA-256 |
|---|---|
| `frontend/electron/runtime-host.ts` | `39dfaa0e5acb70bf10bd0d58320bdf20f9d98ed7cc835f25123124201177dff7` |
| `frontend/scripts/run-packaged-launchagent-login-proof.mjs` | `141a2e52d9e65e8526f5203350fde5eb23a75f2020228dd5c1b37790763aba52` |
| `frontend/src/__tests__/electron/runtime-host-socket-path.test.ts` | `78c64ce5b676c40c4cc498afe279e2d3b58f46c8f6f23842f342e730c50d40b8` |
| `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` | `9338631ef1b295806e17f8be85ffd1a3600c51e68c27d014fc485278a500f595` |

These source hashes do not substitute for the required packaged R17-guard
proof.

## Host boundaries and prohibited acts

After the failure, all three exact candidate paths remained absent and
non-symlinks:

- `/private/tmp/ch-r18-91499728-51dd`;
- `/Users/ryan/Library/LaunchAgents/com.chirality.ci.runatload.login.owner.macos26.r18.1f16d830-4fd0-4647-a01b-a746e8a22cb4.plist`;
- `/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r18-1f16d830-4fd0-4647-a01b-a746e8a22cb4-public-evidence`.

The exact service
`gui/501/com.chirality.ci.runatload.login.owner.macos26.r18.1f16d830-4fd0-4647-a01b-a746e8a22cb4`
returned exit `113` and exactly:

```text
Bad request.
Could not find service "com.chirality.ci.runatload.login.owner.macos26.r18.1f16d830-4fd0-4647-a01b-a746e8a22cb4" in domain for user gui: 501
```

The proposed control socket remains a documented 67-byte path against the
103-byte maximum. Optionless preflight was not run because the build had
already reached a terminal failure. No GUI/open-app, prepare, capture,
logout/login, bootstrap, kickstart, root/plist/job/public-directory creation,
default operator query/mutation, signing, notarization, deployment,
distribution, publication, release/proof-acceptance, staging, commit, push,
PR, or merge occurred.

The owner's Desktop R16 failed-evidence directory and private R16 proof root
were not read, listed, traversed, hashed, copied, cited, adopted, or touched.
No default operator job, plist, launcher, `com.chirality.runtime`, or
`~/.local/bin/chirality` path was queried or touched.

## Outputs and checks

- PASS: required Git basis remained unchanged; empty index and tracked tree;
  empty scoped frontend porcelain and empty build-revision-to-HEAD frontend
  diff.
- PASS: exact proof root/plist/public destination remained absent and
  non-symlinks; exact proof service remained unloaded with exit `113` and the
  exact two-line text.
- FAIL: `npm run desktop:pack` exit `1`; cache miss/download attempt.
- NOT REACHED: embedded dependency boundary, instruction-root integrity,
  exact-merge package/signature/CLI identities, packaged R17 guard,
  optionless preflight, R18/status authorship, proportional validation and
  fresh review.

## Blocker and rerun

Blocker: the ordinary restricted build cannot obtain pinned Electron `43.2.0`
from the local cache and network access is forbidden. The manager/owner must
resolve this external cache condition or issue new authority. A lawful rerun
must use a fresh executor, re-prove all initial gates, initialize its evidence
directory before the build, preserve the complete combined log, and rebuild
from the exact required basis. This failed run authorizes no network retry and
no adoption of the surviving R16 package.

No deliverable R18 record or `_STATUS.md` amendment was written.

## Exact repository path inventory

Executor-written paths are exactly:

1. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R18_STAGING_2026-08-22/instances/WI-PKG09-R18-STAGING-01/executor/RETURN.md`
2. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R18_STAGING_2026-08-22/instances/WI-PKG09-R18-STAGING-01/executor/desktop-pack.exit-status.txt`
3. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R18_STAGING_2026-08-22/instances/WI-PKG09-R18-STAGING-01/executor/desktop-pack.failure-summary.log`

The only other porcelain entries are the five manager-created run-root control
files: `CHAT_TRANSCRIPTION.md`, `ORCHESTRATION_PLAN.md`, `WORK_GRAPH.json`,
`instances/WI-PKG09-R18-STAGING-01/ACTIVATION_AND_WORK_GRAPH.md`, and this
instance's sealed brief. All are beneath `projects/chirality-app-dev/`.
