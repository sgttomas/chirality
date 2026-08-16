# Sealed Agent 2 brief — top-bar runtime reconnect implementation

- RequestedBy: `HELP_HUMAN -> WORKING_ITEMS`
- RunID: `APPDEV_TOPBAR_RUNTIME_RECONNECT_2026-08-15`
- ParentInstanceID: `A1-PKG02-RECONNECT-01`
- ChildInstanceID: `A2-PKG02-RECONNECT-IMPLEMENT-01`
- AgentRole: `TASK` (Agent 2; no delegation)
- TaskSkill: `software-bounded-implementation`
- PackageID: `PKG-02`
- DeliverableIDs: `DEL-02-01`
- ScopePath: `projects/chirality-app-dev/frontend`
- WorkingRoot: `projects/chirality-app-dev`
- Objective: implement the smallest coherent accessible operator reconnect action on the top-bar runtime-connectivity chip, invoking the already-existing main-process daemon-status / `onDaemonAvailable` / supervisor `refreshNow()` path rather than inventing runtime semantics; prove it with automated component/render and behavior coverage.
- AcceptedBasis: clean branch `codex/app-dev-topbar-runtime-reconnect` at `4dfa1b4c1a894b309185702c013f8728fa444079`; valid Receipt 166; DEL-02-01 live Remaining item; D-APP-60 refined by D-APP-64; D-APP-36 component/render evidence bar; accepted software profile.
- Dependencies: current `ShellFrame` chip and connectivity provider/hook; preload runtime daemon control bridge; `runtime-control-ipc.ts` daemon `status` action and main-process `onDaemonAvailable -> bindingSupervisor.refreshNow()` callback; existing connectivity and runtime-control tests.
- DeclaredReads: `AGENTS.md`; `agents/AGENT_TASK.md`; `docs/SOFTWARE_WORKFLOW_PROFILE.md`; `skills/software-bounded-implementation/{SKILL.md,BRIEF_SCHEMA.md,TOOL_POLICY.md,QA_CHECKS.md}`; `projects/chirality-app-dev/software-workflow.json`; DEL-02-01 `ScopeOfWork.md`, `_STATUS.md`, `_DEPENDENCIES.md`; D-APP-64 packet §5; relevant `projects/chirality-app-dev/frontend/**`.
- PROFILE_PATH: `projects/chirality-app-dev/software-workflow.json`
- ApplyEdits: true
- AllowedWriteTargets: `projects/chirality-app-dev/frontend/**` only, including the TASK-required local run record at `projects/chirality-app-dev/frontend/_run_records/TASK_RUN_*.md`; keep that record concise. The manager will also persist the child's terminal return under the managed run root.
- AllowedTools: repository reads/search, `apply_patch`, and registered `frontend-test`, `frontend-typecheck`, `frontend-build`, or `frontend-premerge` checks as authorized below. No installs, network, GUI, provider calls, or Git operations.
- AuthorizedRegisteredChecks: focused `frontend-test` invocation during implementation; `frontend-typecheck` if efficient. Manager owns full-suite/build/premerge fan-in.
- ExpectedOutputs: product source and automated tests; exact changed paths; focused check results; behavior trace from operator action through preload/control handler to supervisor immediate refresh; accessible-name/state/error/reentrancy rationale; scope proof; D-APP-64 candidate design and materially important rejected alternatives for manager attribution.
- AcceptanceCriteria:
  1. The top-bar connectivity chip is an accessible interactive operator affordance in desktop contexts and remains absent when no connectivity bridge/snapshot exists.
  2. One activation invokes the existing runtime daemon `status` control path; a reachable daemon triggers the existing `onDaemonAvailable` callback and main-process supervisor `refreshNow()` path. No new daemon lifecycle action, IPC authority, polling loop, or runtime state semantics are introduced.
  3. The UI provides bounded in-flight/reentrancy handling and does not falsify connectivity state. Failure remains observable/accessibly represented without replacing the main-process connectivity snapshot as truth.
  4. Component/render coverage proves the chip's accessible action and visual state mapping; behavior coverage proves the bridge invocation and important success/failure/reentrancy behavior; main-process/control coverage proves or preserves the `status -> onDaemonAvailable` immediate-refresh link.
  5. Focused frontend tests pass; all changed paths remain under `projects/chirality-app-dev/frontend/**`; no unrelated cleanup.
  6. D-APP-64 fast-reject screen is explicit. If any boundary is touched, stop and return the exact owner gate. Otherwise provide all-four-lens concise rationale and material alternatives; attribute selection as Agent 2 advice for WORKING_ITEMS judgment, not owner case selection.
- EXCLUSIONS: no deliverable/governance/receipt/decision/dependency files; no new acceptance criteria; no release/lifecycle/approval-SHA/provider/domain/network behavior; no public runtime contract expansion outside the existing preload/control seam; no delegation; no commit/push/PR/merge.
- Escalation: return a precise blocker if the target requires new runtime semantics, public-contract expansion beyond the existing desktop bridge, any D-APP-64 fast-reject hit, unauthorized path, or owner choice.
- ExpectedReturn: `SUCCESS` or bounded failure; applied code/test summary; exact paths; checks and outcomes; scope proof; design rationale/alternatives; residual risks; no acceptance/lifecycle claims.
