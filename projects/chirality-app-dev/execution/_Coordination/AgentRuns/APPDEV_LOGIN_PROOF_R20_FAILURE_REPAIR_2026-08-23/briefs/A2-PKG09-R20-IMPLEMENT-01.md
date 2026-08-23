# Sealed brief — A2-PKG09-R20-IMPLEMENT-01

- RequestedBy: `WI-PKG09-R20-REPAIR-01`
- RunID: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`
- ParentInstanceID: `WI-PKG09-R20-REPAIR-01`
- ChildInstanceID: `A2-PKG09-R20-IMPLEMENT-01`
- Role: ephemeral generalist Agent 2 through delegated-harness-native execution; `role not mechanically enforced`; evidence `instruction-asserted`.
- K-SUBAGENT: do not delegate or spawn descendants; instruction+config asserted.
- PackageID / DeliverableID: `PKG-09 / DEL-09-04`
- Objective: confirm the R19 cleanup failure root cause from the verified real launchctl fixture plus current source, then implement and validate only the owner-specified parser, cleanup-preservation, and failed-log behavior.
- AcceptedBasis: branch/HEAD/origin-main `a702dd6ec5005b361c8c023b12b599a425e5e2b8`; frontend tree `9c1b1d9cec8c45a2a74e78c79ce37d784938a6e4`; clean at dispatch; APP-HOLD `ALLOW`.
- DeclaredReads: root and App AGENTS; this sealed brief; run CHAT/activation/plan/graph; `docs/SOFTWARE_WORKFLOW_PROFILE.md`; App `software-workflow.json`; DEL-09-04 status and R17-R19 public run records; the two target frontend files; directly relevant imported helpers; `/private/tmp/ch-r19-fixture/launchctl-print-r19-never-exited.txt` only.
- FixtureGate: before copying or relying, independently require regular non-symlink 3,049-byte source with SHA-256 `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531`; copy verbatim using repository editing discipline to `projects/chirality-app-dev/frontend/src/__tests__/scripts/fixtures/launchctl-print-r19-never-exited.txt`; require target bytes/hash identical.
- AllowedTools: repository read/search, `apply_patch`, `git diff/status/hash`, syntax check, exact focused Vitest target, `npm run typecheck`, proportional deterministic read-only checks. No network, installs, build/package, full `npm test`, Git integration, launchd mutation, GUI, or proof execution.
- AllowedWriteTargets: exactly `projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs`; `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`; `projects/chirality-app-dev/frontend/src/__tests__/scripts/fixtures/launchctl-print-r19-never-exited.txt`; and `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-IMPLEMENT-01/**`.
- ProhibitedReads: do not read, stat recursively, traverse, list, or inspect `/private/tmp/ch-r18-91499728-51dd` or any owner Desktop evidence. Do not query/read default `com.chirality.runtime`, its plist, or `~/.local/bin/chirality`.
- RequiredImplementation:
  1. Parse exact `(never exited)` only as `lastExitCode: undefined` plus `neverExited: true`; every other noninteger last-exit form throws. A running exact-owned PID with runs 1 and never-exited proceeds to bootout.
  2. `cleanupProof` must not unlink the plist or remove runtime-data when bootout is refused, the job remains loaded, or a process is alive; report refusal and preserve diagnostic state.
  3. On every non-PASS, before any allowed removal, preserve `daemon.stdout.log` and `daemon.stderr.log` under `<session-root>/failed-logs/` only after confirming neither contains the known auth token. If either contains it, copy neither and retain logs only in the private root. Never place a token or private state in repo evidence.
  4. Use the real fixture to assert running/PID 34924/runs 1/never-exited true. Preserve integer and crash-loop parsing; reject malformed forms. Cover cleanup ordering, refusal preservation, failure-log copies, token fail-closed behavior, and every non-PASS route proportionally. No unrelated frontend/daemon/package/socket-guard change.
- RequiredChecks: `node --check` on the script; exact focused Vitest file only; `npm run typecheck`; fixture identity; `git diff --check`; App-only containment; empty index. Do not run full `npm test` or build.
- ExpectedOutputs: implementation and tests; verbatim fixture; instance `ROOT_CAUSE.md`, `CHECKS.md`, and `RETURN.md` with exact commands/exits/counts, hashes, candidate inventory, prohibitions observed, and explicit PASS/BLOCKED.
- AcceptanceCriteria: root cause is source/fixture-grounded; all required behaviors and focused checks pass; exact fixture fidelity; no token/private content in repo evidence; only allowed writes; index empty.
- Escalation: stop on fixture mismatch, private/auth ambiguity, unrelated source need, forbidden-surface need, failed command, scope drift, or any request for build/full suite/network/Git/proof/operator mutation.
