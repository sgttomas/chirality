# UID dataflow — confirmed source diagnosis

## Verdict

The prompt diagnosis is independently confirmed from source. The focused test supplies a mocked UID of `501`, while the filesystem objects examined by the product guard are created by the real test process and therefore carry the runner's real UID. The two identities coincide on the macOS development host and diverge on the Ubuntu CI runner. No product defect or product change is required.

This run did not execute the focused test or attempt a local reproduction. CI is the arbiter for the host-identity class because the current local process UID coincides with the old fixture constant.

## Exact flow

1. The test fixture creates a real temporary tree and real files/directories (`run-packaged-launchagent-login-proof.test.ts:28-36,83-89,120-133`). Those objects are owned by the OS identity running Vitest.
2. Independently, the fixture hardcodes its simulated identity to `501`: `state.consoleUid`, `state.securityUid`, `state.loadedService`, the exact launchctl-not-found stderr, the top-level `gui/501` dispatch/output, `deps.userInfo().uid`, and `deps.uid()` (`:47-48,60,94,140,147,195-196`).
3. Product `dependencies()` normally derives identity from `os.userInfo()` and `process.getuid()` (`run-packaged-launchagent-login-proof.mjs:176-183`). The test overrides both. `validateIdentityAccount()` accepts the mutually consistent mocked values and returns `uid = 501` (`:280-297`); `validateAccount()` preserves it (`:300-310`).
4. The fixture's `/usr/bin/stat` response, top-level login-domain identifier, security-context UID, and service routes also report `501`, so console/domain/service semantic validation remains internally coherent (`test:103-108,137-172`; product `:345-372,375-463`).
5. `prepare()` stores that mocked UID in private capture state and uses it in `gui/<uid>/...` service identities. The session/runtime directories and daemon-log/token fixtures remain real filesystem objects owned by the actual test process.
6. `capture()` validates the same mocked account and passes the resulting `uid` into `cleanupProof()`.
7. `cleanupProof()` passes it unchanged as `expectedUid` to `preserveFailureLogs()` (`product:920-933,990-998`).
8. `preserveFailureLogs()` passes `expectedUid` to `readFailureLogSnapshots()` (`:811-850`). That function validates every runtime ancestor, then each open descriptor and pathname before and after the race hook (`:726-805`).
9. `assertSafeSnapshotMetadata()` compares the real `lstat()`/descriptor-stat owner with the mocked UID: `metadata.uid !== expectedUid` (`:709-719`). On a runner UID other than `501`, the first real ancestor check therefore throws `Failure-log directory identity or permissions are unsafe`.
10. `preserveFailureLogs()` converts that throw into the observed first divergence: `Failure-log identity or auth snapshot is unsafe; retained only in private runtime data: Failure-log directory identity or permissions are unsafe` (`:837-849`). The affected capture/cleanup scenarios consequently diverge before their expected log-preservation assertions.

## Product disposition

Retain the product behavior byte-for-byte. In production, the default dependencies derive the process UID and account UID from the real host, require them to agree, require the console owner and GUI domain to agree, and compare protected failure-log metadata against that validated real account UID. The ownership comparison is an intentional security guard; weakening, deleting, or bypassing it would be incorrect.

No ambiguous real-state comparison and no required product edit was found.
