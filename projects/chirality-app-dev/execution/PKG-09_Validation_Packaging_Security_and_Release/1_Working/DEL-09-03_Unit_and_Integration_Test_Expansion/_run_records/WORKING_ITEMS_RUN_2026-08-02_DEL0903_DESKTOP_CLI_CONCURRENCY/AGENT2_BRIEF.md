# Sealed Agent 2 Brief — DEL-09-03 Shared-Daemon Proof

RequestedBy: `HELP_HUMAN` through `WORKING_ITEMS`

RunID: `WORKING_ITEMS_RUN_2026-08-02_DEL0903_DESKTOP_CLI_CONCURRENCY`

ParentInstanceID: `appdev_del0903_shared_daemon_proof`

ChildInstanceID: `A2-DEL0903`

PackageID: `PKG-09`

DeliverableID: `DEL-09-03`

Objective: implement a test-only direct fake-oMLX Desktop/CLI concurrency proof
against one generic daemon/session using the existing public runtime and App
adapter seams.

ScopePath: `projects/chirality-app-dev` with writes limited exactly below.

AcceptedBasis: `HEAD` `72300e75a688b2ef2d1d0c86865577d7d8d2779c`;
DEL-09-03 SOW/context/status/memory/dependencies; D-APP-85 C04/C16 evidence and
execution closeout; Root C06 notice.

Dependencies: the generic daemon-owned lock and current App runtime adapter are
already implemented. Root C06 is explicitly not a dependency and not in scope.

DeclaredReads:

- `projects/chirality-app-dev/frontend/**`
- `runtime/packages/**` and `runtime/tests/**`
- this DEL-09-03 folder
- the cited D-APP-85 and Root C06 records
- App validation documents and software workflow profile

AllowedTools: repository reads; `apply_patch`; Bash for focused/full tests and
read-only validation. This Bash-bearing child is the serialized integration
owner for the stage.

AllowedWriteTargets:

- one new or existing test under
  `projects/chirality-app-dev/frontend/src/__tests__/integration/**`
- `projects/chirality-app-dev/frontend/src/__tests__/integration/fake-openai-loopback.ts`
  only if an indispensable test-fixture extension is required
- this run directory
- DEL-09-03 `_STATUS.md`
- DEL-09-03 `MEMORY.md`

ExpectedOutputs:

1. A direct executable integration test, or a blocker explaining why existing
   public seams cannot support it and proposing the smallest App-owned seam.
2. `AGENT2_RETURN.md` in this run directory with exact claims, paths, tests,
   preservation, and residuals.
3. If and only if all five conjuncts are directly proved, remove only the
   fake-oMLX Desktop/CLI concurrency bullet from `## Remaining`, add dated status
   history, and append a concise evidence entry to `MEMORY.md`.

AcceptanceCriteria:

- Prove both Desktop's `RuntimeDaemonHarnessPort` and a generic CLI-side
  `RuntimeClient` resolve/use the same daemon/socket identity and the same
  runtime session.
- Prove a competing same-session turn is rejected by the generic client with
  code `SESSION_TURN_IN_PROGRESS` while the Desktop turn is active.
- Prove a second `RuntimeDaemon` cannot become owner of the live socket.
- Prove Desktop cancellation results in exactly one durable terminal outcome.
- Prove distinct-session turns can coexist.
- Exercise fake oMLX through the existing Pi/oMLX adapter and fake loopback; do
  not replace the provider interaction with a generic stub.
- Modify no implementation source and make no daemon-crash/model-drain recovery
  claim.
- Run the focused test, full frontend test/typecheck/build, applicable runtime
  tests and premerge, receipt/corpus/53-status/self-check/practitioner checks,
  and whitespace/containment/preservation checks. If a check is environment-
  blocked, record the exact blocker without weakening it.

Escalation: stop without expanding scope if existing public seams cannot prove
the complete conjunct, if a runtime/App implementation change is required, or
if any preservation boundary would be crossed.

Prohibitions: no delegation; no commits, pushes, merges, network expansion, or
writes outside AllowedWriteTargets. Do not touch `runtime/**`, Electron/App
implementation source, dependencies, decomposition, lifecycle/Checking
Approval, decisions, Task Management, parity, D-APP-84, UNKNOWN relations,
other packages, loop receipts, or completion log.
