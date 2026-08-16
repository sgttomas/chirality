# Sealed Agent 2 brief — fresh top-bar runtime reconnect review

- RequestedBy: `HELP_HUMAN -> WORKING_ITEMS`
- RunID: `APPDEV_TOPBAR_RUNTIME_RECONNECT_2026-08-15`
- ParentInstanceID: `A1-PKG02-RECONNECT-01`
- ChildInstanceID: `A2-PKG02-RECONNECT-REVIEW-01`
- AgentRole: `TASK` (fresh Agent 2; no delegation)
- TaskSkill: `software-code-review`
- PackageID: `PKG-02`
- DeliverableID: `DEL-02-01`
- ScopePath: `projects/chirality-app-dev/frontend`
- ImplementationBrief: `../A2-PKG02-RECONNECT-IMPLEMENT-01/LAUNCH_BRIEF.md`
- AcceptedBasis: branch `codex/app-dev-topbar-runtime-reconnect` baseline `4dfa1b4c1a894b309185702c013f8728fa444079`; implementation return frozen at sibling `RETURN.md`; D-APP-60 refined by D-APP-64; D-APP-36 UI component/render bar; project software profile.
- DiffBasis: 100% of the four-file product diff under `frontend/src/**` relative to `4dfa1b4c1a894b309185702c013f8728fa444079`. Coordination/deliverable closeout is not yet part of this review.
- VerificationEvidence: implementation return plus the changed tests; registered full test had 1,119 pass/4 skip and one unrelated model-drain timeout; initial typecheck environment-resolution failure must be treated as a manager rerun requirement, not concealed.
- PROFILE_PATH: `projects/chirality-app-dev/software-workflow.json`
- ApplyEdits: false
- AllowedWriteTargets: none. Use the runtime-owned managed return only; do not write any file.
- DeclaredReads: `AGENTS.md`; `agents/AGENT_TASK.md`; `skills/software-code-review/{SKILL.md,BRIEF_SCHEMA.md,TOOL_POLICY.md,QA_CHECKS.md}`; the implementation brief/return; profile; DEL-02-01 `_STATUS.md`; D-APP-64 §5; relevant four-file diff and traced existing preload/control/supervisor source/tests.
- Objective: independently try to refute correctness and readiness of the reconnect implementation. Validate exact containment first; trace activation through the existing desktop bridge/status IPC to `onDaemonAvailable -> refreshNow`; inspect accessible semantics, truthful state/error reporting, reentrancy, unmount behavior, test adequacy, regression risk, and D-APP-64 attribution/fence compliance.
- AcceptanceCriteria:
  1. Review 100% of the four-file product diff and its direct callers/interfaces.
  2. Confirm the action exists only when the desktop connectivity chip exists and calls only the existing daemon `status` path.
  3. Check accessible name/description/live feedback, keyboard-native behavior, pending/disabled/reentrancy, status-truth preservation, failure handling, and response-after-unmount risk.
  4. Confirm the control-handler test truly proves reachable status calls `onDaemonAvailable`, and the production main-process binding still maps that callback to supervisor `refreshNow()`.
  5. Identify concrete actionable findings with exact paths/lines and impact. Any correctness, accessibility, security, contract, scope, or missing-test blocker yields `BLOCK`.
  6. Return exactly `COMMIT-SAFE` or `BLOCK`; no edits or lifecycle acceptance.
- EXCLUSIONS: no repairs, writes, test execution requiring generated evidence, install/network/GUI/Git action, acceptance/lifecycle claim, or delegation.
- ExpectedReturn: verdict; findings ordered by severity; scope/evidence assessment; residual risk; explicit rerun requirements; model/provider attribution when exposed.
