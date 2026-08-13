# Sealed Agent 2 brief — runtime held-connection SIGTERM implementation

- RequestedBy: `HELP_HUMAN -> WORKING_ITEMS`
- RunID: `APPDEV_RUNTIME_DAEMON_HELD_CONNECTION_STOP_2026-08-13`
- ParentInstanceID: `WORKING_ITEMS-runtime-stop-fix`
- ChildInstanceID: `A2-RUNTIME-STOP-IMPLEMENT-01`
- PackageID: `PKG-09`
- DeliverableID: `DEL-09-04`
- ScopePath: `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_RUNTIME_DAEMON_HELD_CONNECTION_STOP_2026-08-13`
- Objective: deliver a minimal production source change that makes reusable runtime-daemon process signal shutdown robust, plus a deterministic spawned-process regression proving `SIGTERM` tears down within a bounded time while a Unix-socket HTTP request has complete headers but an incomplete body.
- AcceptedBasis: current branch base `f84f7b03b49ce1397b556c8e03ccc5b11c955802`; existing `RuntimeDaemon.stop()` has a 2 s grace then force-closes residual transports and already has a direct-call partial-request test. Preserve that proven logic unless analysis finds a concrete defect. The D-APP-93 owner-trace root is ruled evidence to cite only; do not read, reverify, or edit it.
- Dependencies: none beyond checked-in runtime dependencies.
- DeclaredReads: `AGENTS.md`, `agents/AGENT_TASK.md`, `docs/SOFTWARE_WORKFLOW_PROFILE.md`, `projects/chirality-app-dev/software-workflow.json`, this brief, `runtime/package*.json`, `runtime/tsconfig*.json`, `runtime/packages/daemon/**`, `runtime/tests/**`, and read-only caller inspection under `projects/chirality-app-dev/frontend/electron/{main.ts,runtime-host.ts}`.
- AllowedTools: repository reads/search, `apply_patch`, and exact local commands under `runtime/`: `npm test -- --run runtime/tests/<focused-test-file>`, `npm test`, `npm run typecheck`. No installs, network, build packaging, app execution, or other commands.
- ApplyEdits: true.
- AllowedWriteTargets: `runtime/packages/daemon/src/**`; `runtime/tests/**`; `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_RUNTIME_DAEMON_HELD_CONNECTION_STOP_2026-08-13/_run_records/TASK_RUN_IMPLEMENTER.md`.
- ExpectedOutputs: production source change; deterministic process fixture/regression under `runtime/tests/**`; implementer run record containing design rationale, exact changed paths, test commands/results, and residual risks.
- AcceptanceCriteria:
  1. The regression spawns a real child process hosting `RuntimeDaemon`, arms a Unix-domain-socket partial HTTP request with complete headers and declared body longer than supplied bytes, receives durable confirmation that the holder is armed, sends OS `SIGTERM`, and asserts bounded child exit plus control socket and owner-record cleanup.
  2. The test would fail/hang on an implementation that merely awaits `server.close()` while the holder remains connected; bounded timers fail closed and clean up the child.
  3. Production source provides a coherent reusable signal-shutdown mechanism with one-shot/idempotent behavior, no premature `process.exit()`, and an explicit failure policy; do not modify the existing 2 s force-close semantics gratuitously.
  4. Focused regression, full runtime tests, and runtime typecheck pass.
  5. No path outside AllowedWriteTargets changes.
- EXCLUSIONS: no packet/evidence/foreign-loop/decision-register/receipt/DEL-09-04 state writes; no D-APP-93 or D-APP-88 disposition; no Git operations; no dependency or lockfile changes; no Electron product edits.
- Escalation: stop and return a precise blocker if satisfying the production path requires an Electron edit or new dependency.
- ExpectedReturn: concise code-first summary, exact tests/output, scope proof, and risks.
