# Sealed Agent 2 brief — PKG-05 canonical replay restart review

- RequestedBy: `HELP_HUMAN -> WORKING_ITEMS`
- RunID: `APPDEV_CANONICAL_REPLAY_RESTART_2026-08-16`
- ParentInstanceID: `WI-PKG05-CANONICAL-REPLAY`
- ChildInstanceID: `A2-PKG05-CANONICAL-REPLAY-REVIEW-01`
- AgentRole: `TASK`
- TaskSkill: `software-code-review`
- PackageID: `PKG-05`
- DeliverableID: `DEL-05-04`
- ScopePath: `projects/chirality-app-dev/frontend`
- WorkingRoot: `projects/chirality-app-dev`
- Objective: independently review 100% of the frozen PKG-05 node diff proving canonical Desktop/CLI replay across daemon restart and lazy migration with exact manager/child attribution.
- AcceptedBasis: implementation changed only `projects/chirality-app-dev/frontend/src/__tests__/integration/runtime-canonical-replay-restart.integration.test.ts`; focused worktree-correct Vitest passed 1/1 in 237 ms; scope validation passed; Root runtime remained read-only.
- DeclaredReads: root/App AGENTS; `agents/AGENT_TASK.md`; software workflow profile; `software-code-review` skill and companions; App profile/validation docs; DEL-05-04 status/ScopeOfWork/dependencies; the complete one-file node diff; relevant Root runtime and App client/projection implementation/tests read-only.
- ApplyEdits: false.
- AllowedWriteTargets: none. Managed runtime return is the durable record.
- AllowedTools: repository reads/search, read-only Git status/diff, and registered read-only scope/check-selection helpers. Do not run network/provider/GUI commands and do not modify files.
- ExpectedOutputs: findings with exact location/impact; `PASS` or `BLOCK` for manager fan-in; assessment of public-seam realism, same-session/event equivalence, migration non-destructiveness, central persistence after fresh-service restart, exact recorded attribution, input-order independence, cleanup/time bounds, worktree-correct evidence, containment, residual risk, and model/provider attribution.
- AcceptanceCriteria:
  1. Review every changed line and trace replay through public App/Root seams, lazy migration, canonical store, restart, and Woven hierarchy construction.
  2. Reject internal-only substitutes, identity/event divergence gaps, source-destructive migration, restart that reuses the original service, inferred hierarchy, missing manager/child role assertions, unbounded waits, cleanup leaks, or any Root/PKG-08/foreign-node write.
  3. Confirm the focused evidence is credible and state narrow manager-owned checks still required.
  4. Return PASS only with no actionable finding; do not repair or perform lifecycle acceptance.
- EXCLUSIONS: no edits, remediation, other-package action, lifecycle/release/Git action, or delegation.
- Escalation: report any finding to the manager; never repair it directly.
