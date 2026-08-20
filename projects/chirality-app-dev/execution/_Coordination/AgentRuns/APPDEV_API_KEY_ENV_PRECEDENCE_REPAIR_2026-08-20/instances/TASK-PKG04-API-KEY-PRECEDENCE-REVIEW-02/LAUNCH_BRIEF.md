# TASK-PKG04-API-KEY-PRECEDENCE-REVIEW-02 — sealed review brief

- RequestedBy: `WI-PKG04-API-KEY-PRECEDENCE-01`
- RunID: `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
- ParentInstanceID: `WI-PKG04-API-KEY-PRECEDENCE-01`
- ChildInstanceID: `TASK-PKG04-API-KEY-PRECEDENCE-REVIEW-02`
- Role: fresh `TASK` Agent 2, read-only
- TaskSkill: `software-code-review`
- PackageID: `PKG-04`
- DeliverableIDs: `DEL-04-05`
- ScopePath: `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge`
- ImplementationBrief: implementer launch/return plus Review-01 return and
  `REVIEW_01_DISPOSITION.md`.
- AcceptedBasis: `6710ee6354debc201f6a454e2802897026cd4b38`;
  `docs/SPEC.md` Section 12.3; `docs/PRD.md` FR-030;
  `DEL-04-05-RQ-001`, `AC-001`, `VER-001`; Receipt-180; frozen graph.
- DiffBasis: parent `FROZEN_DIFF_MANIFEST_V2.md`; reject any mismatch. Review
  100% of both product/test files and exact Git basis diff.
- VerificationEvidence: the eight frozen v2 subjects, including normalized
  frontend and manager registered-check evidence.
- PROFILE_PATH: `projects/chirality-app-dev/software-workflow.json`
- ApplyEdits: `false`
- AllowedWriteTargets: no project-content writes; only this managed instance's
  `STATUS.json` and `RETURN.md` may be persisted.
- AllowedTools: repository reads; `validate_change_scope.py` and
  `select_affected_checks.py` per skill. No edits, installs, release, network,
  destructive commands, Git publication, or delegation.
- ReviewCriteria: Review-01 finding closure; exact precedence correctness;
  stored/env/whitespace cases; preservation of oMLX/storage/error semantics;
  profile-selected check completeness; contract/scope/security/regression
  compliance; exclusions and diff hygiene.
- EXCLUSIONS: remediation, package-state/lifecycle/memory/evidence edits,
  other packages, shared fan-in/receipt/completion logs, commit/push/PR.
- ExpectedReturn: PASS with zero actionable findings or FAIL with exact
  findings; identity/coverage; Review-01 backcheck; risks; reruns; fan-in
  validity.
- ModelAttribution: OpenAI Codex; exact model build not exposed.
