# Sealed brief — A2-PKG09-MACOS26-REVIEW-01

- RequestedBy: `WI-PKG09-MACOS26-LOGIN-REPAIR-01`
- RunID: `APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22`
- ParentInstanceID: `WI-PKG09-MACOS26-LOGIN-REPAIR-01`
- ChildInstanceID: `A2-PKG09-MACOS26-REVIEW-01`
- AgentType: fresh ephemeral generalist Agent 2; no delegation
- PackageID / DeliverableID: `PKG-09` / `DEL-09-04`
- AcceptedBasis: `9bfe529352afb8bb43a8f0c6afd9a4b3945453b1`
- Mode: evidence-only software code review; no repair

## Objective

Review 100% of the frozen source/test/status/R14/R15 diff and executor evidence
against the owner authorization, run plan, R12/R13 basis, current software
profile, and the full implementation brief. Return `PASS` or specific
actionable findings.

## Declared reads

Root and WORKING_ITEMS instructions; run plan/graph/transcription/activation;
implementation brief and executor return; current source and full test file;
DEL-09-04 status/R12/R13/R14/R15; validation/build docs; current Git state;
live read-only `/dev/console` and top-level `launchctl print gui/<uid>` only as
needed to rerun preflight.

## Tools and write target

Use read-only shell checks. You may independently run syntax, focused Vitest,
typecheck, the optionless preflight, APP-HOLD, practitioner self-check,
forbidden-source scans, hashes, and diff/containment checks. Do not run full
suite unless a finding requires it; the executor's retained full-suite evidence
is in scope. Write only `review/REVIEW.md` in this manager instance.

No source, test, status, run-record, build-output, proof-root, LaunchAgents,
service/job, launcher, Git, shared, or outside-App write is authorized. Do not
run prepare/capture/build/package/GUI or any mutating `launchctl` command.

## Review matrix

1. R14 accurately records the owner-reported exact error and no-plist/no-job
   claim, separately from the manager's read-only confirmation that the old
   R13 root is an empty mode-0700 directory; no acceptance is inferred.
2. JXA/CoreGraphics/`CGSessionCopyCurrentDictionary` is absent from product
   code and is not used at runtime.
3. The replacement executes exactly read-only `/usr/bin/stat` on
   `/dev/console` and top-level `/bin/launchctl print gui/<uid>` for session
   identity; it never targets a service/job in preflight.
4. Account validation fails closed for non-Darwin/root/invalid accounts and
   console username/UID mismatch, including loginwindow/setup identities.
5. Domain parsing is top-level/nesting-aware and rejects malformed/trailing,
   duplicate/ambiguous, unsafe, wrong UID, non-login, non-Aqua, and mismatched
   handle/security-`asid` evidence.
6. Prepare and capture use the same private nonempty random salt, public
   identities are non-reversible SHA-256 digests, the digest changes with the
   session identifier, and unchanged capture identity still fails closed.
7. `preflight` is optionless, resolves before any session-root operation,
   emits no raw username/handle, performs no mutation, and reports calibrated
   read-only fields without claiming proof.
8. Comprehensive tests cover every owner-enumerated success/failure class and
   existing prepare/capture/cleanup/default-protection behavior remains green.
9. Independent syntax/focused/typecheck/live-preflight checks pass; executor
   full-suite evidence is coherent, including the sandbox EPERM diagnostic and
   exact unrestricted PASS without intervening source changes.
10. Live preflight succeeds on macOS 26.6.2 and the proposed new root remains
    absent before/after; no LaunchAgents/operator/proof path is accessed.
11. R15 and `_STATUS.md` truthfully remain `IN_PROGRESS`, unproved, uncommitted,
    unbuilt, and without exact `PROOF_REVISION`/`PROOF_APP`; proposed root/label
    are not executable procedure authority.
12. No build/package, GUI, prepare/capture, bootstrap/kickstart, logout/login,
    deployment, signing/notarization/distribution/publication/release/issuance,
    provider/network, stage/commit/push/PR/receipt/merge action occurred.
13. Exact persistent writes are limited to two frontend paths, status, R14,
    R15, and this unique run root, all under `projects/chirality-app-dev/`; index
    is empty and diff/whitespace/hashes resolve.
14. Derivative status, blockers, rerun requirements, and next committed-build
    handoff are explicit and calibrated.

Write a concise evidence matrix and final verdict. A finding must name the
file/line and required repair. Do not repair it.
