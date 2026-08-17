# Sealed Agent 2 brief — PKG-05 canonical replay restart implementation

- RequestedBy: `HELP_HUMAN -> WORKING_ITEMS`
- RunID: `APPDEV_CANONICAL_REPLAY_RESTART_2026-08-16`
- ParentInstanceID: `WI-PKG05-CANONICAL-REPLAY`
- ChildInstanceID: `A2-PKG05-CANONICAL-REPLAY-IMPLEMENT-01`
- AgentRole: `TASK`
- TaskSkill: `software-bounded-implementation`
- PackageID: `PKG-05`
- DeliverableID: `DEL-05-04`
- ScopePath: `projects/chirality-app-dev/frontend`
- WorkingRoot: `projects/chirality-app-dev`
- Objective: implement a dedicated App integration proof that Desktop and CLI replay the same daemon-owned canonical session across fresh-service daemon restart and lazy non-destructive legacy migration while preserving exact recorded manager/child attribution.
- AcceptedBasis: base `44903bc69cf56d4ca794fe9629f26793a82bf1b3`; D-APP-73; live Root runtime public seams; APP-HOLD reliance/consumption preflights `ALLOW`; the activation's live-state gate finding and D-APP-64 selection.
- Dependencies: accepted DEL-05-01 session migration, DEL-05-02 event replay, and DEL-08-05 exact recorded parentage semantics; Root runtime is read-only.
- DeclaredReads: root/App AGENTS; `agents/AGENT_TASK.md`; software workflow profile; `software-bounded-implementation` skill and companions; App profile/validation docs; DEL-05-04 ScopeOfWork/status/dependencies; relevant frontend runtime-client, Woven projection, and tests; relevant Root runtime daemon/client/session code and tests read-only.
- ApplyEdits: true.
- AllowedWriteTargets: `projects/chirality-app-dev/frontend/src/__tests__/integration/runtime-canonical-replay-restart.integration.test.ts`; if and only if the proof exposes an App defect, `projects/chirality-app-dev/frontend/src/lib/runtime-client/**` and/or `projects/chirality-app-dev/frontend/src/lib/woven-dialogue/**`.
- AllowedTools: repository reads/search, `apply_patch`, and bounded local frontend test/typecheck commands. No installs, network, provider calls, GUI, or Git operations.
- ExpectedOutputs: dedicated test and only any necessary App source repair; exact changed paths; focused test evidence; worktree-correct runtime resolution; scope proof; residual risks; actual engine/provider/model attribution when exposed.
- AcceptanceCriteria:
  1. Use a real `RuntimeDaemon`, authenticated `RuntimeClient`s representing Desktop compatibility and CLI, and the App `RuntimeDaemonHarnessPort`; do not construct an App-owned runtime.
  2. Seed legacy manager/child session metadata and events, including exact `agent1` manager, `agent2` child, and child `parentSessionId`; trigger lazy migration through public replay access and prove source records remain unchanged.
  3. Prove Desktop and CLI receive the same canonical session identity and ordered event replay, then stop and restart with a fresh runtime service over the same daemon state and prove the same results again.
  4. Exercise the Woven Dialogue/operator hierarchy projection over replayed canonical session records and prove manager/child attribution is recorded, available, and not inferred from prose/order.
  5. Bound all waits, clean daemon/temp resources, use no network/provider, and fail for identity divergence, event divergence, destructive migration, or lost parentage.
  6. Run the focused Vitest with worktree-correct Root-runtime aliases. Run only further narrow checks that are efficient; manager owns final node fan-in.
  7. No changed path outside AllowedWriteTargets.
- EXCLUSIONS: no Root runtime, Electron, manifest/lockfile, receipt, completion-log, decision/register, authority, loop-plan, other-deliverable/package, PKG-08-node, lifecycle, or Git writes; no delegation.
- Escalation: return a precise blocker without editing Root runtime if the proof reveals a Root-owned defect or requires authority/public-contract change.
- ExpectedReturn: code-first summary, exact evidence, scope containment, residual risks, and rerun triggers.
