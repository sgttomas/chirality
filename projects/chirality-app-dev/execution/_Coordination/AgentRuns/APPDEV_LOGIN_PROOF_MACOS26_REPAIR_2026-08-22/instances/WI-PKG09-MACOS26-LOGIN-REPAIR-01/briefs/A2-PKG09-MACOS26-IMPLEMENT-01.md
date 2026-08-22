# Sealed brief — A2-PKG09-MACOS26-IMPLEMENT-01

- RequestedBy: `WI-PKG09-MACOS26-LOGIN-REPAIR-01`
- RunID: `APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22`
- ParentInstanceID: `WI-PKG09-MACOS26-LOGIN-REPAIR-01`
- ChildInstanceID: `A2-PKG09-MACOS26-IMPLEMENT-01`
- AgentType: ephemeral generalist Agent 2; no delegation
- PackageID / DeliverableID: `PKG-09` / `DEL-09-04`
- AcceptedBasis: `9bfe529352afb8bb43a8f0c6afd9a4b3945453b1`
- Method: bounded software defect diagnosis and implementation

## Objective

Record the failed owner Terminal attempt, implement and test a live-compatible
macOS 26.6.2 login-session identity detector, run a strictly read-only live
preflight, and record the repair without rebuilding or executing the proof.

## Declared reads

Root instructions; current WORKING_ITEMS instructions; frozen run plan and
owner transcription; App loop plan/receipt cursor; `software-workflow.json`;
DEL-09-04 context/status/R12/R13; owner launcher ruling; build/validation docs;
current source and its complete test file; live read-only `/dev/console` and
top-level `launchctl print gui/<uid>` output.

## Allowed tools

Read/write/apply-patch and bounded shell checks. Authorized commands include
syntax check, focused/full Vitest, typecheck, APP-HOLD, practitioner self-check,
`sw_vers`, `/usr/bin/stat` on `/dev/console`, and top-level read-only
`/bin/launchctl print gui/<uid>`. No network.

## Allowed write targets

- `projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs`
- `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`
- DEL-09-04 `_STATUS.md`
- DEL-09-04 `_run_records/R14_MACOS26_LOGIN_IDENTITY_PREPARE_FAILURE_2026-08-22.md`
- DEL-09-04 `_run_records/R15_MACOS26_LOGIN_IDENTITY_REPAIR_2026-08-22.md`
- this manager instance's `executor/**`

Do not modify package manifests, lockfiles, other source/tests, memory, SOW,
shared loop/receipt/completion surfaces, or ignored build/artifact outputs.

## Product requirements

1. Remove the JXA/CoreGraphics `CGSessionCopyCurrentDictionary` dependency.
2. Derive identity only from `/dev/console` owner metadata and the top-level
   `launchctl print gui/<uid>` login domain. Do not inspect or mutate any
   service/job.
3. Fail closed unless console user is a real non-loginwindow user matching the
   current account, console UID equals the process/account UID, domain type is
   login, session is exactly Aqua, and the top-level domain contains one
   positive safe-integer handle plus one security-context UID and `asid`.
   Require identifier/UID consistency and reject duplicates, ambiguity,
   malformed output, command failure, or stderr-bearing partial success.
4. The stored identity must be a non-reversible digest that changes when the
   validated login-session handle/security identifier changes. Preserve the
   capture-side fail-closed unchanged-identity check.
5. Add a reproducible read-only preflight route that performs only these
   inspections, returns a calibrated PASS record without raw session handle or
   username, accepts no mutation-oriented options, and creates no session root.
6. Preserve all prepare/capture, proof ownership, cleanup, redaction, default
   protection, and no-bootstrap/no-kickstart behavior outside the detector.

## Test requirements

Add comprehensive tests for valid live-shaped output; malformed console/domain
output; wrong console or security UID; non-Aqua/non-login domain; duplicate or
ambiguous identifiers; mismatched handle/`asid`; console or launchctl command
failure/stderr; preflight option refusal/no mutation/no root creation; and
unchanged capture identity. Assert the detector never invokes `osascript` and
the preflight never issues service-level or mutating launchctl commands.

## Records

- R14: distinguish owner-reported evidence from live observation. Record exact
  error `Current GUI login-session identity is not valid JSON`; the attempt
  failed before preparation completed; no plist/job; only the old empty proof
  root from R13 exists; DEL stays `IN_PROGRESS` and unproved.
- R15: exact diff/check/live-preflight evidence, current macOS/build identity,
  and no-mutation boundary. Propose, without creating, the absent root
  `/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20`
  and label
  `com.chirality.ci.runatload.login.owner.macos26.00bc8f1a-0045-48a2-970f-be120cf7fc20`.
  Exact `PROOF_REVISION` and `PROOF_APP` remain unavailable until the repaired
  bytes are committed and the later unsigned rebuild passes; do not emit an
  executable prepare block.
- `_STATUS.md`: update only enough to point to R14/R15 and truthfully retain
  `IN_PROGRESS`, unproved, unbuilt-repair, owner acts, and all release fences.

## Acceptance checks

- `node --check scripts/run-packaged-launchagent-login-proof.mjs`
- focused Vitest file passes with all required cases
- full `npm test` and `npm run typecheck` pass
- read-only live preflight passes on macOS 26.6.2 and creates no state
- APP-HOLD and practitioner self-check pass at the existing baseline
- `git diff --check` and exact write containment pass
- no frontend build/package command and no forbidden path/action occurs

Write `executor/RETURN.md` with commands/results, live preflight, changed paths,
hashes, claim boundaries, blockers, derivative status, and rerun requirements.
Stop and escalate on any need to access LaunchAgents, an operator service or
launcher, proof prepare/capture, build/package, network, or an undeclared path.
