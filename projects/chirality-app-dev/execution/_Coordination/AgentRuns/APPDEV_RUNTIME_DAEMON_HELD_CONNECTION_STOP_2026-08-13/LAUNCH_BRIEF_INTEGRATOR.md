# Sealed Agent 2 brief — shipped Electron signal integration

- RequestedBy: `HELP_HUMAN -> WORKING_ITEMS`
- RunID: `APPDEV_RUNTIME_DAEMON_HELD_CONNECTION_STOP_2026-08-13`
- ParentInstanceID: `WORKING_ITEMS-runtime-stop-fix`
- ChildInstanceID: `A2-RUNTIME-STOP-INTEGRATE-01`
- PackageID: `PKG-09`
- DeliverableID: `DEL-09-04`
- ScopePath: `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_RUNTIME_DAEMON_HELD_CONNECTION_STOP_2026-08-13`
- Objective: integrate the frozen shared runtime signal-shutdown binder into the shipped Electron runtime-daemon helper path, preserving the existing shutdown funnel and GUI behavior without duplicate signal handlers or double stop.
- AcceptedBasis: frozen v1 runtime implementation at the current worktree paths `runtime/packages/daemon/src/{signal-shutdown.ts,index.ts}` and its focused test/fixture; HELP_HUMAN amendment v2 in `BRIEF_AMENDMENT_V2.md`; current Electron `main.ts` signal loop and `runtime-host.ts` interfaces.
- Dependencies: accepted terminal return of `A2-RUNTIME-STOP-IMPLEMENT-01`.
- DeclaredReads: `AGENTS.md`, `agents/AGENT_TASK.md`, `docs/SOFTWARE_WORKFLOW_PROFILE.md`, `projects/chirality-app-dev/software-workflow.json`, this brief and amendment, `runtime/packages/daemon/src/**`, `projects/chirality-app-dev/frontend/electron/{main.ts,runtime-host.ts}`, and relevant existing focused tests under `projects/chirality-app-dev/frontend/src/__tests__/electron/**`.
- AllowedTools: repository reads/search, `apply_patch`, and exact local checks from `projects/chirality-app-dev/frontend`: focused `npm test -- --run <one focused test>`, `npm run typecheck`. Use the existing canonical checkout dependency tree read-only if this worktree lacks node_modules; no install/network/build/package/app execution.
- ApplyEdits: true.
- AllowedWriteTargets: `projects/chirality-app-dev/frontend/electron/main.ts`; exactly one new or existing focused test under `projects/chirality-app-dev/frontend/src/__tests__/electron/**`; `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_RUNTIME_DAEMON_HELD_CONNECTION_STOP_2026-08-13/_run_records/TASK_RUN_INTEGRATOR.md`.
- ExpectedOutputs: production Electron integration; focused integration pin; run record with exact checks and rationale.
- AcceptanceCriteria:
  1. The shipped `--runtime-daemon` mode genuinely installs and uses `installRuntimeDaemonSignalShutdown` against the active runtime host/daemon stop contract.
  2. Existing manual `SIGINT`/`SIGTERM` wiring is removed or coherently reconciled; no duplicate signal-driven `shutdown()`/`runtimeHost.stop()` and no GUI-mode signal behavior regression.
  3. `before-quit`, initialize-failure, retire-after-spawn, and explicit app shutdown continue through the existing funnel.
  4. Focused test statically/deterministically pins conditional daemon-only binder installation and absence of the duplicate loop or otherwise proves equivalent behavior without launching Electron.
  5. Focused test and frontend typecheck pass; no config edit is needed.
- EXCLUSIONS: do not edit runtime bytes, runtime tests, configs, package/lockfiles, other Electron/source files, packet/evidence/foreign loops/decision register/receipt/DEL state; no app or packaged helper execution; no D-APP disposition or Git operations.
- Escalation: return a precise blocker before touching any build/type config or any file beyond the exact targets.
- ExpectedReturn: code-first integration summary, exact changed paths/check outputs, scope proof, residual risks.
