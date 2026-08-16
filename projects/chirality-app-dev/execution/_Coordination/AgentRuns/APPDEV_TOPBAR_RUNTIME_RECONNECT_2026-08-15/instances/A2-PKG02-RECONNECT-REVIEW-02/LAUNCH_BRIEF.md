# Sealed Agent 2 brief — fresh post-remediation refutation review

- RequestedBy: `WORKING_ITEMS`
- RunID: `APPDEV_TOPBAR_RUNTIME_RECONNECT_2026-08-15`
- ParentInstanceID: `A1-PKG02-RECONNECT-01`
- ChildInstanceID: `A2-PKG02-RECONNECT-REVIEW-02`
- AgentRole: `TASK` (fresh Agent 2; no delegation)
- TaskSkill: `software-code-review`
- PackageID: `PKG-02`
- DeliverableID: `DEL-02-01`
- ScopePath: `projects/chirality-app-dev/frontend`
- ImplementationBrief: original implementation brief plus remediation brief `../A2-PKG02-RECONNECT-REMEDIATE-01/LAUNCH_BRIEF.md`
- AcceptedBasis: baseline `4dfa1b4c1a894b309185702c013f8728fa444079`; first review `BLOCK` and frozen return; completed remediation return; D-APP-60 refined by D-APP-64; D-APP-36 UI component/render bar.
- DiffBasis: 100% of the final four-file product diff under `frontend/src/**` relative to baseline, including the repaired production response shape.
- VerificationEvidence: focused component suite 13/13 PASS; control-handler test passed within earlier run; manager-owned full registered frontend-test/typecheck reruns still pending due disclosed environment resolution/listener conditions.
- PROFILE_PATH: `projects/chirality-app-dev/software-workflow.json`
- ApplyEdits: false
- AllowedWriteTargets: none; managed return only.
- Objective: independently refute the entire repaired candidate and decide whether the product diff is `COMMIT-SAFE` or `BLOCK`, explicitly rechecking the accepted first-review blocker and searching for fresh correctness/accessibility/scope/security/test issues.
- DeclaredReads: `AGENTS.md`; `agents/AGENT_TASK.md`; software-code-review skill/companions; original/remediation/review briefs and returns; final four-file diff; existing preload/control/supervisor sources and tests; DEL-02-01 status; D-APP-64 §5.
- AcceptanceCriteria:
  1. Confirm `{ ok: true, daemon.running: false }` now yields secondary failure without changing snapshot truth and the test uses the production payload.
  2. Recheck desktop-only presence, existing status path, reachable `onDaemonAvailable -> refreshNow`, native accessibility, live feedback, reentrancy, error/success cases, unmount residual risk, and exact scope.
  3. Review 100% of all four final files, not merely the remediation hunk.
  4. Return only actionable findings with exact evidence. Any correctness/accessibility/security/contract/scope/missing-test blocker yields `BLOCK`.
  5. Return exactly `COMMIT-SAFE` or `BLOCK`. No edits or lifecycle acceptance.
- EXCLUSIONS: no writes/repairs, installs/network/GUI/Git action, lifecycle/acceptance claims, or delegation.
- ExpectedReturn: exact verdict, findings, first-block disposition, evidence/rerun assessment, residual risk, model/provider attribution if exposed.
