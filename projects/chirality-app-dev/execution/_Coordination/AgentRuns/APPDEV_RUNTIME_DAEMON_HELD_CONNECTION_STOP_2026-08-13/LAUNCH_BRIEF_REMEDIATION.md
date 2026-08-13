# Sealed Agent 2 brief — Electron native quit race remediation

- RequestedBy: `HELP_HUMAN -> WORKING_ITEMS`
- RunID: `APPDEV_RUNTIME_DAEMON_HELD_CONNECTION_STOP_2026-08-13`
- ParentInstanceID: `WORKING_ITEMS-runtime-stop-fix`
- ChildInstanceID: `A2-RUNTIME-STOP-REMEDIATE-01`
- PackageID: `PKG-09`
- DeliverableID: `DEL-09-04`
- ScopePath: `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_RUNTIME_DAEMON_HELD_CONNECTION_STOP_2026-08-13`
- Objective: remediate review BLOCK by ensuring Electron native `before-quit` cannot exit the daemon while binder-started held-connection teardown is in flight; only the final owned exit after teardown may pass.
- AcceptedBasis: frozen runtime binder/process regression; frozen Electron integration; `REVIEW_RETURN_01.md`; `BRIEF_AMENDMENT_V3.md`.
- Dependencies: reviewer 01 terminal BLOCK accepted as remediation input.
- DeclaredReads: governing instructions/briefs/returns in this run root; exact three write targets; runtime binder API; existing relevant Electron tests.
- AllowedTools: repository reads/search, `apply_patch`, focused frontend test, frontend typecheck using manager-described disposable/canonical dependency approach if necessary. No installs/network/build/package/app execution/Git.
- ApplyEdits: true.
- AllowedWriteTargets: `projects/chirality-app-dev/frontend/electron/runtime-shutdown-policy.ts`; `projects/chirality-app-dev/frontend/electron/main.ts`; `projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-daemon-signal-integration.test.ts`; `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_RUNTIME_DAEMON_HELD_CONNECTION_STOP_2026-08-13/_run_records/TASK_RUN_REMEDIATION.md`.
- ExpectedOutputs: pure shutdown policy, integrated state handling, behavioral race test, run record.
- AcceptanceCriteria:
  1. Binder-first teardown followed by native `before-quit` is prevented until teardown settles.
  2. The final owned `app.exit()` after successful or failed teardown is allowed without recursion.
  3. Repeated binder/native events do not invoke runtime stop twice.
  4. GUI direct signal behavior and all other existing funnels remain intact.
  5. Focused behavioral tests and frontend typecheck pass; diff-check passes.
- EXCLUSIONS: no other source/test/config/package/lock/runtime/evidence/packet/foreign-loop/decision/receipt/DEL state writes; no D-APP disposition; no app execution; no Git.
- Escalation: stop before any out-of-scope write.
- ExpectedReturn: concise mechanism, exact tests, scope evidence, risks, `SUCCESS` or precise blocker.
