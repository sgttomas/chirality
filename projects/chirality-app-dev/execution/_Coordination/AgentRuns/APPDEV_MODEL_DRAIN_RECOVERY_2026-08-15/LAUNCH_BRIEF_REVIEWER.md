# Sealed Agent 2 brief — PKG-03 model-drain recovery review

- RequestedBy: `HELP_HUMAN -> WORKING_ITEMS`
- RunID: `APPDEV_MODEL_DRAIN_RECOVERY_2026-08-15`
- ParentInstanceID: `WI-PKG03-MODEL-DRAIN`
- ChildInstanceID: `A2-PKG03-MODEL-DRAIN-REVIEW-01`
- AgentRole: `TASK`
- TaskSkill: `software-code-review`
- PackageID: `PKG-03`
- DeliverableID: `DEL-03-04`
- ScopePath: `projects/chirality-app-dev/frontend`
- WorkingRoot: `projects/chirality-app-dev`
- Objective: independently review 100% of the frozen App integration diff proving exactly one durable terminal outcome when daemon restart interrupts an in-flight model drain.
- AcceptedBasis: implementer changed only `projects/chirality-app-dev/frontend/src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts`; focused Vitest passed with worktree-correct aliases (1 passed, 2 skipped, 2.11 s); Root runtime is read-only.
- DeclaredReads: `AGENTS.md`; `agents/AGENT_TASK.md`; `docs/SOFTWARE_WORKFLOW_PROFILE.md`; `skills/software-code-review/{SKILL.md,BRIEF_SCHEMA.md,TOOL_POLICY.md,QA_CHECKS.md}`; `projects/chirality-app-dev/{AGENTS.md,software-workflow.json}`; DEL-03-04 `ScopeOfWork.md` and `_STATUS.md`; the complete Git diff and relevant frontend/root-runtime implementation and tests.
- ApplyEdits: false.
- AllowedWriteTargets: none. Managed runtime launch/status/return are the durable record.
- AllowedTools: repository reads/search and read-only Git diff/status. Do not run network/provider/GUI commands and do not modify files.
- ExpectedOutputs: actionable findings with exact locations and impact; acceptance/rejection for manager fan-in; assessment of realism, determinism, public-seam use, durable exactly-once proof, cleanup, worktree-resolution caveat, scope containment, and residual risk; actual engine/provider/model attribution when exposed.
- AcceptanceCriteria:
  1. Review every changed line and trace the test through daemon stop/restart, residency drain, turn interruption, event persistence, and replay.
  2. Reject false realism, internal-only seam use where public client seams exist, a missing accepted-turn correlation, duplicate/missing terminal gaps, unbounded waits, cleanup leaks, or Root-runtime writes.
  3. Confirm whether the focused evidence is credible given explicit worktree aliases and identify required broad-check handling.
  4. Return `PASS` only with no actionable finding; do not perform lifecycle acceptance.
- EXCLUSIONS: no edits, no remediation, no package/PKG-09/governance/receipt/lifecycle/Git-closeout actions, no delegation.
- Escalation: report findings to the manager; never repair them directly.
