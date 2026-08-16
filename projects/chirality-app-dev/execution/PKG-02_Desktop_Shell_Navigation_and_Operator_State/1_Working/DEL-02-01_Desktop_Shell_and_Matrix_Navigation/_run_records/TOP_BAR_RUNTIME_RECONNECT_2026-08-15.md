# Top-bar runtime reconnect — implementation and rationale evidence

## Result

The snapshot-backed top-bar runtime-connectivity chip is now a native accessible button. One guarded activation invokes the existing preload daemon `status()` action; a reachable daemon follows the existing main-process `daemonSnapshot -> onDaemonAvailable -> bindingSupervisor.refreshNow()` path. The chip never starts/stops the daemon, creates a renderer polling loop, or optimistically changes connectivity state. Probe failures appear as secondary visible and live-region feedback while supervisor snapshots remain the visual truth.

Changed product files:

- `frontend/src/components/shell/shell-frame.tsx`
- `frontend/src/app/globals.css`
- `frontend/src/__tests__/components/shell-frame-runtime-connectivity.test.tsx`
- `frontend/src/__tests__/electron/runtime-control-ipc.test.ts`

## D-APP-64 disposition-class exercise

Fast-reject result: PASS. The choice is bounded and reversible and changes no purpose/scope, acceptance criteria, professional/safety/legal posture, spending/external commitment, lifecycle/release/issuance state, protected data, destructive history, hard fence, or authority attribution.

- OwnerStandingApproval: `D-APP-64 §3`
- AgentJudgment: `SELECT_AND_ADVANCE`
- SelectedOutcome: make the snapshot-backed connectivity chip an accessible guarded status-probe button; preserve snapshot truth and report probe failures separately.
- JudgedBy: `WORKING_ITEMS / APPDEV_TOPBAR_RUNTIME_RECONNECT_2026-08-15 / A1-PKG02-RECONNECT-01`, informed by the implementation and verifier returns.
- OwnerCaseSelection: `NONE`
- RejectedAlternatives: start/restart from the chip (adds lifecycle semantics and authority); renderer polling (duplicates the main-process retry loop); optimistic local connectivity mutation (falsifies observable truth); retain the Runtime Settings detour (does not close the authorized top-bar gap).
- RationaleArtifact: this file.
- IndependentVerifier: `execution/_Coordination/AgentRuns/APPDEV_TOPBAR_RUNTIME_RECONNECT_2026-08-15/instances/A2-PKG02-RECONNECT-REVIEW-02/RETURN.md` — `COMMIT-SAFE` after remediation.
- EffectStatus: `EFFECTIVE` in the validated candidate; Git closeout remains with CHANGE and owner merge remains external.
- PreservedGates: every D-APP-64 §5.1 fast-reject class; no lifecycle, release, approval-SHA, provider/network, domain, dependency, public-contract, or Git act.

Four lenses: ontology keeps the chip a shell presentation/control over an existing bridge; epistemology leaves supervisor snapshots authoritative; praxeology uses one bounded status request to reach the existing immediate-refresh callback; axiology favors the smallest accessible reversible recovery affordance.

## Verification

- APP-HOLD-1 dispatch preflight: `DEL-02-01` CLEAR / NOT_HELD / ALLOW at `4dfa1b4c1a894b309185702c013f8728fa444079`.
- Focused component/render suite after remediation: 13/13 PASS.
- Main-process control coverage proves reachable daemon status invokes `onDaemonAvailable`; production binds it to supervisor `refreshNow()`.
- Registered full frontend test: PASS — 143 files passed, 1 skipped; 1,121 tests passed, 4 skipped.
- Registered frontend typecheck: PASS.
- Registered frontend build: PASS. A temporary worktree-correct type/dependency overlay was used because the reusable dependency checkout's daemon declaration output predates the landed signal-shutdown export; all temporary files/symlinks were removed.
- First independent review: `BLOCK` because `{ ok: true, daemon.running: false }` was reported as successful secondary feedback. Bounded remediation added the production response shape and regression. Fresh post-repair review: `COMMIT-SAFE`, no findings.
- Premerge: not applicable to this chip-only Electron control/UI change; no browser-facing session, SSE, turn, exposed-tool, or harness API behavior changed. D-APP-36 is satisfied by component-level render/state/disabled/active/error coverage; layout/viewport risk is low and does not require browser screenshots.

Residual non-blocking risk: an in-flight status promise can settle after unmount and call setters on the disposed React instance. No user-visible state crosses into a remounted instance; rerun/review if the chip's lifetime or status bridge cancellation contract changes.

No waiver, owner decision, lifecycle transition, release claim, provider call, network expansion, or derivative-package regeneration is required. Managed evidence is derivative and remains bound to the baseline and final candidate diff; it does not replace decomposition truth.
