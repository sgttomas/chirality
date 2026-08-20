# TASK-PKG04-API-KEY-STATUS-SOURCE-REVIEW-03 — sealed review brief

- RequestedBy: `WI-PKG04-API-KEY-PRECEDENCE-01`
- RunID: `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
- ParentInstanceID: `WI-PKG04-API-KEY-PRECEDENCE-01`
- ChildInstanceID: `TASK-PKG04-API-KEY-STATUS-SOURCE-REVIEW-03`
- Role: fresh `TASK` Agent 2, read-only
- TaskSkill: `software-code-review`
- PackageID: `PKG-04`
- DeliverableIDs: `DEL-04-05`
- ScopePath: `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge`
- ImplementationBrief: status-source implementer launch/return plus v2 graph,
  N2 amendment, and manager validation.
- AcceptedBasis: `6710ee6354debc201f6a454e2802897026cd4b38`;
  `docs/SPEC.md` Section 12.3; `docs/PRD.md` FR-030;
  `DEL-04-05-RQ-001`, `RQ-004`, `AC-001`, `VER-001`; Receipt-180;
  `ORCHESTRATION_PLAN_V2.md`; `WORK_GRAPH_V2.md`.
- DiffBasis: parent `FROZEN_DIFF_MANIFEST_V3.md`; reject any mismatch. Review
  100% of both product/test files and the exact Git basis diff.
- VerificationEvidence: all twelve frozen v3 subjects.
- PROFILE_PATH: `projects/chirality-app-dev/software-workflow.json`
- ApplyEdits: `false`
- AllowedWriteTargets: no project-content writes; only this managed instance's
  `STATUS.json` and `RETURN.md` may be persisted.
- AllowedTools: repository reads; `validate_change_scope.py` and
  `select_affected_checks.py` per skill. No edits, installs, release, network,
  destructive commands, Git publication, or delegation.
- ReviewCriteria: exact source discriminator correctness; no credential
  disclosure; stored/UI over simultaneous env; canonical-before-compatibility
  environment resolution; oMLX and unsupported-provider isolation; unchanged
  get/set/remove and error behavior; runtime daemon serialization and N2
  consumption sufficiency; check completeness; scope/security/regression and
  diff hygiene.
- EXCLUSIONS: remediation, IPC/root-runtime-contract edits,
  package-state/lifecycle/memory/evidence edits, other packages, shared
  fan-in/receipt/completion logs, commit/push/PR.
- ExpectedReturn: PASS with zero actionable findings or FAIL with exact
  findings; identity/coverage; contract/caller trace; risks; reruns; fan-in
  validity and exact N2 handoff.
- ModelAttribution: OpenAI Codex; exact model build not exposed.
