# TASK-PKG04-API-KEY-PRECEDENCE-REVIEW-01 — sealed review brief

- RequestedBy: `WI-PKG04-API-KEY-PRECEDENCE-01`
- RunID: `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
- ParentInstanceID: `WI-PKG04-API-KEY-PRECEDENCE-01`
- ChildInstanceID: `TASK-PKG04-API-KEY-PRECEDENCE-REVIEW-01`
- Role: fresh `TASK` Agent 2, read-only
- TaskSkill: `software-code-review`
- PackageID: `PKG-04`
- DeliverableIDs: `DEL-04-05`
- ScopePath: `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge`
- ImplementationBrief: sibling implementer `LAUNCH_BRIEF.md` plus its
  terminal `RETURN.md`.
- AcceptedBasis: `6710ee6354debc201f6a454e2802897026cd4b38`;
  `docs/SPEC.md` Section 12.3; `docs/PRD.md` FR-030;
  `DEL-04-05-RQ-001`, `AC-001`, `VER-001`; Receipt-180; owner authorization
  and frozen run graph.
- DiffBasis: `FROZEN_DIFF_MANIFEST.md` in the parent instance; reject any
  mismatch. Review 100% of both product/test files and the exact Git diff from
  the accepted basis.
- VerificationEvidence: focused Vitest plus normalized registered full
  frontend test, typecheck, and build evidence in the frozen manifest.
- PROFILE_PATH: `projects/chirality-app-dev/software-workflow.json`
- ApplyEdits: `false`
- AllowedWriteTargets: no project-content writes; only this managed instance's
  runtime-owned `STATUS.json` and `RETURN.md` may be persisted.
- AllowedTools: repository reads; `validate_change_scope.py` and
  `select_affected_checks.py` per the skill. No edits, installs, release,
  network, destructive commands, Git publication, or delegation.
- ReviewCriteria: correctness of exact precedence; all stored/env/whitespace
  cases; preservation of oMLX isolation and storage/error semantics; test
  self-expiry removal; contract/scope compliance; evidence sufficiency;
  security, regression, and maintainability risks; exclusions and diff
  hygiene.
- EXCLUSIONS: remediation, lifecycle/status/memory/evidence edits, other
  packages, shared fan-in/receipt/completion logs, commit/push/PR.
- ExpectedReturn: `PASS` with zero actionable findings or `FAIL` with exact
  file/line, impact, evidence, and bounded remediation direction; identity and
  coverage; blocking/non-blocking risk; rerun requirements; fan-in validity.
- ModelAttribution: OpenAI Codex; exact model build not exposed.
