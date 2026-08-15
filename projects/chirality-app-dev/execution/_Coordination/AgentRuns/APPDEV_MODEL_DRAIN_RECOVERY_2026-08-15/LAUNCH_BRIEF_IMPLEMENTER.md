# Sealed Agent 2 brief — PKG-03 model-drain recovery implementation

- RequestedBy: `HELP_HUMAN -> WORKING_ITEMS`
- RunID: `APPDEV_MODEL_DRAIN_RECOVERY_2026-08-15`
- ParentInstanceID: `WI-PKG03-MODEL-DRAIN`
- ChildInstanceID: `A2-PKG03-MODEL-DRAIN-IMPLEMENT-01`
- AgentRole: `TASK`
- TaskSkill: `software-bounded-implementation`
- PackageID: `PKG-03`
- DeliverableID: `DEL-03-04`
- ScopePath: `projects/chirality-app-dev/frontend`
- WorkingRoot: `projects/chirality-app-dev`
- Objective: add the smallest realistic automated integration case under `frontend/**` that arms an in-flight model drain, restarts the daemon through public seams, and proves exactly one durable terminal outcome. If and only if the case exposes an App-owned defect, fix it within App frontend source.
- AcceptedBasis: clean branch `codex/app-dev-model-drain-recovery` at `910c02129811a005da9b180c31e3c18dd365df6f`; `DEL-03-04` Remaining is the authorized objective; Root runtime is established product behavior and read-only evidence; APP-HOLD-1 dispatch preflight passed.
- Dependencies: Root runtime daemon/client/session public seams available in the checkout and existing frontend integration harness patterns.
- DeclaredReads: `AGENTS.md`; `agents/AGENT_TASK.md`; `docs/SOFTWARE_WORKFLOW_PROFILE.md`; `skills/software-bounded-implementation/{SKILL.md,BRIEF_SCHEMA.md,TOOL_POLICY.md,QA_CHECKS.md}`; `projects/chirality-app-dev/{AGENTS.md,software-workflow.json}`; DEL-03-04 `ScopeOfWork.md` and `_STATUS.md`; relevant `projects/chirality-app-dev/frontend/**`; relevant Root `runtime/**` read-only.
- ApplyEdits: true.
- AllowedWriteTargets: `projects/chirality-app-dev/frontend/**` only. The runtime-owned managed child return is sufficient as the Agent 2 run record; do not create an additional local `_run_records` file.
- AllowedTools: repository reads/search, `apply_patch`, and local frontend test commands; use the registered workflow profile for broad checks. No installs, network, GUI, provider calls, or Git operations.
- ExpectedOutputs: App integration test and only any strictly necessary App-owned source fix; exact changed paths; focused test result; scope proof; behavioral explanation; residual risks; actual engine/provider/model attribution when the runtime exposes it.
- AcceptanceCriteria:
  1. Test drives a real `RuntimeDaemon` plus authenticated `RuntimeClient`/session public seams from an App-owned frontend integration test, without editing Root runtime.
  2. Test accepts a turn, holds model work in flight, triggers model drain, stops and restarts the daemon, replays durable session events, and proves exactly one terminal event among `turn.completed`, `turn.failed`, `turn.cancelled`, and `turn.interrupted` for that accepted turn.
  3. Test is deterministic, bounded, cleans daemon/temp resources, uses no network/provider, and would fail for missing or duplicate terminal persistence.
  4. Focused frontend Vitest passes. Run further registered checks only if efficient; manager owns final full-suite fan-in.
  5. No changed path outside `projects/chirality-app-dev/frontend/**`.
- EXCLUSIONS: no writes to `runtime/**`, package state, PKG-09, `_DomainEngines`, decisions, receipts, release/lifecycle state, dependencies, or lockfiles; no provider/network expansion; no delegation.
- Escalation: return a precise blocker without writing Root runtime if the proof cannot be built through existing public seams, or if satisfying it requires a public-contract/change-authority decision.
- ExpectedReturn: code-first summary, exact checks and outcomes, scope proof, risks, and cross-package observation for PKG-09 verification ownership.
