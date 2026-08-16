# Sealed Agent 2 brief — reconnect BLOCK remediation

- RequestedBy: `WORKING_ITEMS`
- RunID: `APPDEV_TOPBAR_RUNTIME_RECONNECT_2026-08-15`
- ParentInstanceID: `A1-PKG02-RECONNECT-01`
- ChildInstanceID: `A2-PKG02-RECONNECT-REMEDIATE-01`
- AgentRole: `TASK` (fresh Agent 2; no delegation)
- TaskSkill: `software-bounded-implementation`
- PackageID: `PKG-02`
- DeliverableIDs: `DEL-02-01`
- ScopePath: `projects/chirality-app-dev/frontend`
- Objective: remediate exactly the fresh review blocker recorded at sibling review `RETURN.md`: model the production daemon-status response, treat `{ ok: true, daemon: { running: false } }` as a secondary check failure without mutating snapshot-derived connectivity truth, and add a component behavior test using the real response shape.
- AcceptedBasis: frozen four-file implementation diff at baseline `4dfa1b4c1a894b309185702c013f8728fa444079`; review verdict `BLOCK`; all original D-APP-64 and product fences remain unchanged.
- Dependencies: current changed `shell-frame.tsx` and component connectivity test; production `runtime-control-ipc.ts` response union and existing main-process immediate-refresh path.
- DeclaredReads: `AGENTS.md`; `agents/AGENT_TASK.md`; software-bounded-implementation skill/companions; original implementation brief/return; review brief/return; relevant current frontend source/tests.
- PROFILE_PATH: `projects/chirality-app-dev/software-workflow.json`
- ApplyEdits: true
- AllowedWriteTargets: `projects/chirality-app-dev/frontend/src/components/shell/shell-frame.tsx`, `projects/chirality-app-dev/frontend/src/__tests__/components/shell-frame-runtime-connectivity.test.tsx`, and a concise TASK local run record under `projects/chirality-app-dev/frontend/_run_records/**` (manager will preserve the material return under AgentRuns and remove transient local records before fan-in).
- AllowedTools: repository reads/search, `apply_patch`, registered frontend test/typecheck checks. No install/network/GUI/Git action.
- AcceptanceCriteria:
  1. Runtime status response type matches enough of the production union to inspect `daemon.running` on `ok: true`.
  2. `running: false` produces truthful secondary failure text such as daemon unreachable while leaving chip label/tone derived solely from the main-process snapshot.
  3. Component behavior test supplies production-shaped `{ ok: true, launchAgent, daemon: { running: false } }` and fails on the blocked behavior.
  4. Existing success/failure/reentrancy tests remain correct; no unrelated cleanup; exact allowed-path containment.
- EXCLUSIONS: no CSS/control-handler/runtime semantic change unless strictly required by the blocker (escalate instead); no deliverable/coordination/governance/receipt/lifecycle changes; no delegation; no Git action.
- Escalation: return blocked if the exact repair requires scope/public-contract/acceptance expansion.
- ExpectedReturn: exact repair and test result, scope proof, residual risk, rerun needs; no acceptance claim.
