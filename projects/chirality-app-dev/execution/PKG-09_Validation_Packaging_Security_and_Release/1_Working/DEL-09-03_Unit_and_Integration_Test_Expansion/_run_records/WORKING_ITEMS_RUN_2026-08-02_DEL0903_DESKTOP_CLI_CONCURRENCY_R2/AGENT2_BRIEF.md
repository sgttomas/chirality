# Sealed Agent 2 Brief — DEL-09-03 Shared-Daemon Proof R2

RequestedBy: `HELP_HUMAN` through `WORKING_ITEMS`

RunID: `WORKING_ITEMS_RUN_2026-08-02_DEL0903_DESKTOP_CLI_CONCURRENCY_R2`

ParentInstanceID: `appdev_del0903_shared_daemon_proof_r2`

ChildInstanceID: `A2-DEL0903-R2`

PackageID: `PKG-09`

DeliverableID: `DEL-09-03`

Objective: implement a test-only direct fake-oMLX Desktop/CLI concurrency proof
against one generic daemon/session using the existing public runtime and App
adapter seams.

ScopePath: `projects/chirality-app-dev`, with writes limited exactly below.

AcceptedBasis: `HEAD` `72300e75a688b2ef2d1d0c86865577d7d8d2779c`;
DEL-09-03 SOW/context/status/memory/dependencies; D-APP-85 C04/C16 evidence and
execution closeout; prior attempt records as process evidence only.

Dependencies: the generic daemon-owned lock and current App runtime adapter are
already implemented. Root C06 is explicitly not a dependency and not in scope.

DeclaredReads:

- `runtime/tests/daemon.test.ts`
- `runtime/tests/turn-hardening.test.ts`
- `runtime/packages/**`
- `projects/chirality-app-dev/frontend/src/__tests__/integration/pi-omlx-wire.integration.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/integration/fake-openai-loopback.ts`
- `projects/chirality-app-dev/frontend/src/lib/runtime-client/runtime-daemon-harness-port.ts`
- other directly imported App frontend files only as compiler errors require
- this DEL-09-03 folder, prior run records, and R2 run directory
- `projects/chirality-app-dev/software-workflow.json` and App validation docs

AllowedTools: repository reads; `apply_patch`; Bash for focused/full tests and
read-only validation. This Bash-bearing child is the serialized integration
owner for the stage. Do not delegate.

AllowedWriteTargets:

- exactly `projects/chirality-app-dev/frontend/src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/integration/fake-openai-loopback.ts`
  only if an indispensable test-fixture extension is required
- this R2 run directory
- DEL-09-03 `_STATUS.md` and `MEMORY.md`, but only after every required conjunct
  passes

ExecutionOrder:

1. Do not survey broadly. Immediately copy/adapt the fixture setup in
   `runtime/tests/daemon.test.ts` into the frozen target.
2. Milestone 1 must start one `RuntimeDaemon`, register project
   `chirality-app-dev`, create two `RuntimeClient` objects over the same socket
   and project credential, wrap one in `RuntimeDaemonHarnessPort`, and assert
   both sides see the same daemon status/project/session.
3. Run focused Vitest as soon as that smallest test compiles. Send the exact
   result to WORKING_ITEMS and wait for milestone acceptance before adding
   complexity.
4. After acceptance, refine in small patches using
   `runtime/tests/turn-hardening.test.ts`, the existing Pi/oMLX wire test, and
   `fake-openai-loopback.ts` to prove the remaining frozen conjuncts.
5. If an existing seam makes a conjunct impossible, stop with exact
   compiler/runtime evidence; do not propose or implement speculative source
   change.

ExpectedOutputs:

1. The frozen executable integration test or an exact evidence-backed blocker.
2. `AGENT2_RETURN.md` in this R2 run directory with exact claims, paths, tests,
   preservation, and residuals.
3. If and only if all required conjuncts are directly proved, remove only the
   fake-oMLX Desktop/CLI concurrency bullet from `## Remaining`, add dated
   status history, and append a concise evidence entry to `MEMORY.md`.

AcceptanceCriteria:

- Prove Desktop's `RuntimeDaemonHarnessPort` and a generic CLI-side
  `RuntimeClient` resolve/use the same daemon/socket identity and same project
  credential, and observe the same runtime session.
- Exercise the real `PiAgentEngineAdapter` against existing fake oMLX.
- Prove a competing same-session CLI turn is rejected with typed code
  `SESSION_TURN_IN_PROGRESS` while the Desktop turn is active.
- Prove a second `RuntimeDaemon` cannot become owner of the live socket.
- Prove Desktop cancellation results in exactly one replayed durable terminal
  outcome.
- Prove distinct-session turns can coexist.
- Modify no implementation source and make no C06 daemon-crash/model-drain
  recovery claim.
- Run focused Vitest, then full frontend test/typecheck/build, applicable
  runtime tests and App premerge, receipt/corpus/53-status/self-check/
  practitioner checks, plus whitespace/containment/preservation checks. Record
  any environment blocker exactly without weakening the check.
- If frontend-local dependencies are absent, a lock-matched temporary symlink
  to the primary frontend `node_modules` may be used only after verifying lock
  equality and must be removed before return.

MilestoneReturn: report the frozen target path, concise test shape, exact focused
command, exit status, and any compiler/runtime diagnostics before refinement.

Escalation: stop without expanding scope if an existing public seam cannot
prove the complete conjunct, if runtime/App implementation changes are
required, or if any preservation boundary would be crossed.

Prohibitions: no delegation; no commits, pushes, merges, network expansion, or
writes outside AllowedWriteTargets. Do not touch `runtime/**`, Electron/App
implementation source, dependencies, decomposition, lifecycle/Checking
Approval, decisions, Task Management, parity, D-APP-84, UNKNOWN relations,
other packages, shared loop receipts, or completion log.
