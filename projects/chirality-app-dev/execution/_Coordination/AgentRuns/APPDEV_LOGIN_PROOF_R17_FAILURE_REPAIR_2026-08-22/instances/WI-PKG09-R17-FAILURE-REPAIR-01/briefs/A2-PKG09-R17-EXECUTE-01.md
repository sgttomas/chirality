# Sealed Agent 2 brief — R17 failure record and repair

- RequestedBy: WORKING_ITEMS
- RunID: `APPDEV_LOGIN_PROOF_R17_FAILURE_REPAIR_2026-08-22`
- ParentInstanceID: `WI-PKG09-R17-FAILURE-REPAIR-01`
- ChildInstanceID: `A2-PKG09-R17-EXECUTE-01`
- PackageID / DeliverableID: `PKG-09` / `DEL-09-04`
- Objective: one integrated write-owner implementation of R17 plus the
  harness cleanup/path guards and runtime-host socket-length diagnostic.
- AcceptedBasis: exact commit
  `6b0c5219b6a2653e2fc491b1d998abcf78fcf776`
- Delegation: prohibited.

## Declared reads

Root/App instructions and profile; DEL-09-04 status/R14-R16/Receipt 187;
current proof harness, runtime-host source and tests; run-root transcription,
plan, graph, activation, and manager preflight; the owner-preserved failed
evidence directory read-only. Do not copy private state or log bodies into the
repository and do not read inside the private proof root.

## Allowed write targets

1. `projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs`
2. `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`
3. `projects/chirality-app-dev/frontend/electron/runtime-host.ts`
4. the minimum appropriate runtime-host focused test file(s) under
   `projects/chirality-app-dev/frontend/src/__tests__/electron/`
5. DEL-09-04 `_run_records/R17_LOGIN_PROOF_FAILURE_AND_REPAIR_2026-08-22.md`
6. DEL-09-04 `_STATUS.md`
7. this instance's `executor/**` evidence and `RETURN.md`

No other writer may edit those overlapping targets during this node.

## Implementation contract

### R17

Create an executed-and-failed record that can never be read as proof
acceptance. Separate owner statements from independent observations. Bind all
six public evidence hashes and modes; PREPARED false-claim; summary/evidence
FAIL at source revision `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`;
RunAtLoad/job-spawn observation; owner-reported nonzero capture, runs `16`,
manual residual bootout; error `Loaded job has ambiguous process identity`;
cleanup plist absent/runtime data removed/job absent false/mutation refused;
repeated `runtime.daemon.initialize_failed` `listen EINVAL` evidence without
copying log bodies; independently computed R16 119-byte and R13 111-byte full
socket paths; current exact plist/job absence; private root present and
untouched. Record bounded secret scans without printing secret content. Keep
DEL `IN_PROGRESS` and unproved; minimally update status. Include evidence-only
recommendations and tradeoffs for a later short permission-contained,
symlink-safe per-user socket location and for later KeepAlive crash-loop
guard/backoff/proof-specific policy. Implement neither recommendation.

Propose only this absent future R18 root:
`/private/tmp/ch-r18-91499728-51dd`.
Its root is 33 UTF-8 bytes and its future control socket is 67 UTF-8 bytes,
leaving a 36-byte safety margin below the 103-byte maximum. Require read-only
absence/non-symlink confirmation. Do not stage R18 or create/query the root.

### Prepare-time guard

Before any session-root creation, LaunchAgents directory creation, app/plist
inspection, command, install, job/plist action, or other prepare mutation,
compute the exact full
`${sessionRoot}/runtime-data/runtime/control.sock` path and its UTF-8 byte
length. On macOS reject lengths greater than 103 with deterministic measured
and maximum byte counts and no secret. Preserve symlink/containment rules.
Tests must use actual path strings/filesystem-facing inputs and cover 103
accepted, 104 rejected, Unicode byte counting, R16 119 rejected, R13 111
rejected, and zero command/mutation/root creation on rejection.

### Proof-owned pid-less cleanup

Permit bootout of a loaded pid-less/crash-looping proof job only after all of
these independently match: exact non-default proof label/service; expected
plist path; verified regular non-symlink plist bytes with exact label and
runtime program arguments; launchctl program and arguments; packaged
executable. A missing PID skips lsof only after those matches. Any valid PID
retains strict process-executable inspection. Reject missing, mismatched, or
ambiguous label/plist/program/arguments and never query or touch the default
operator job beyond existing protected-state behavior already required by the
proof. Add realistic crash-loop launchctl fixtures including runs/nonzero last
exit where appropriate, an exact-owned pid-less bootout+cleanup success, and
fail-closed mismatch coverage.

### Runtime host

Before the runtime daemon can call `listen`, fail deterministically on macOS
when the exact socket path exceeds 103 UTF-8 bytes. Include measured/max bytes
in the error without secrets; do not relocate the socket. Export or factor the
minimum testable guard if needed. Test 103/104 boundaries, Unicode, and that
daemon/listen construction is not attempted on rejection.

## Checks and fences

Run syntax, focused harness/runtime-host tests, typecheck, full frontend tests,
APP-HOLD, repository self-check, practitioner pytest, receipt validator,
`git diff --check`, candidate whitespace including new files, exact App-only
containment, and empty index. Network/build/package/rebuild, R18, proof
prepare/capture/logout/login, GUI, bootstrap/kickstart, LaunchAgent/plist/job,
default operator, launcher, private-root, signing/notarization/deployment/
distribution/release, stage/commit/push/PR/merge acts are prohibited.

Return PASS or FAIL with exact changed paths/hashes, check commands/results,
evidence boundaries, recommendation conclusions, blockers, and rerun triggers.
Do not delegate. Fresh evidence-only review is mandatory after byte freeze.
