---
run-id: TASK_RUN_DEL-09-06_2026-09-03_NODE_A
timestamp: 2026-09-03
run-status: SUCCESS (frozen for independent review; closure recorded at closeout)
control-surface: FILE
scope-path: projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks
task-profile: NONE
task-skill: software-bounded-implementation
resolved-skill-path: skills/software-bounded-implementation
resolved-skill-version: "1"
parent-run: execution/_Coordination/AgentRuns/APPDEV_V3_NODE_A_2026-09-03
executor: Claude Fable 5.1 (claude-fable-5-1), ephemeral Agent 2 under HELP_HUMAN
item: DEL-09-06-V3-01
basis: 0c683fb1657706316272951e4c3a0f7781b46009
---

## Requested Tasks

- Adopt the `runtime-control-ipc.ts` sender-origin policy on all six credential IPC
  handlers through one shared module; plumb `rendererOrigin` from `main.ts`; deny with a
  typed secret-free result and a desktop-log line.
- Unit-test every channel with authorized and unauthorized senders.
- Inventory G-CSP renderer-hardening test coverage; add unit-level tests only where
  missing and testable; weaken nothing.

## Outputs Produced

- `frontend/electron/ipc-sender-policy.ts` (new shared policy + `describeIpcSender`);
  `api-key-ipc.ts` (six guarded channels, `ApiKeyHandlerOptions { rendererOrigin, log }`);
  `runtime-control-ipc.ts` (imports the shared policy); `main.ts` (registers credential
  handlers after the renderer URL is known, passing origin and logger).
- Tests: `ipc-sender-policy.test.ts` (17), `api-key-ipc.test.ts` (58, six-channel
  authorization matrix), contract pins for context isolation / sandbox / egress
  registration / shared-policy adoption.
- Evidence: `Evidence/Node_A_Credential_IPC_Sender_Authorization_2026-09-03/`
  (`EVIDENCE.md`, packaged-security-proof bytes + `MANIFEST.sha256`).

## Checks

Recorded with exact commands, cwd, exit status, and summaries in the parent run's
`CHECKS.json`: typecheck pass; full Vitest pass (157 files / 1364 tests, 4 skipped);
focused 151 pass; build pass; premerge FAIL in the absent-runtime-daemon-bindings
class (deferred to PR CI, no pass inferred); desktop:pack pass; packaged security proof
pass in-sandbox; diff --check, self-check, pytest (350), APP-HOLD scan, scope validation
pass.

## A1 re-stage declaration

Recorded in the parent run's `STEP0_DISCOVERY.md` §3: this tranche's `frontend/`
mutation invalidates the staged R20 procedure for any future proof claim and requires a
newly staged revision and a fresh owner-executed proof; the 2026-08-23 R20 PASS stands
as historical evidence only.

## Residuals surfaced to the parent

Window-open denial, navigation constraint, and a renderer CSP are absent from source
and outside this brief's write locus; they are reported in the parent `RETURN.md` as a
scope need, not silently added.
