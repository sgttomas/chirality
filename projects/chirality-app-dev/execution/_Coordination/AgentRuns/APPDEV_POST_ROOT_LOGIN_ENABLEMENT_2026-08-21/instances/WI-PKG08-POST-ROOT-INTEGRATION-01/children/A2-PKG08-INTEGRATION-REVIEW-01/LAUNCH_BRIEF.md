# Sealed Agent 2 brief — fresh post-Root integration review

- RequestedBy: `WI-PKG08-POST-ROOT-INTEGRATION-01`
- RunID: `APPDEV_POST_ROOT_LOGIN_ENABLEMENT_2026-08-21`
- ParentInstanceID: `WI-PKG08-POST-ROOT-INTEGRATION-01`
- ChildInstanceID: `A2-PKG08-INTEGRATION-REVIEW-01`
- AgentForm: fresh ephemeral bounded generalist, Agent 2; delegation prohibited.
- PackageID / DeliverableID: `PKG-08` / `DEL-08-04`
- Objective: perform a fresh, read-only, 100% review of the post-preflight
  executor evidence and the three DEL-08-04 candidate truth edits against the
  owner-enumerated Node 1 contract.
- AcceptedBasis: `1b375af4f1219ecfc00fc2755854aa7fd4220901`;
  App implementation `ac2cd801a06a0679bc86830c627218ccca78b658`;
  Root TM125 notice; App Receipts 172/184; frozen parent activation/work graph.
- AcceptedExecutor: `A2-PKG08-INTEGRATION-EXECUTE-02/RETURN.md`, SHA-256
  `3f51c39e3ddd386da9f34804f6f2379da69f42972821945a781c3248927b070f`.
  Attempt 1 is rejected and must not support acceptance.
- FrozenCandidate:
  - `_STATUS.md` SHA-256
    `0a60e895113bcfdf530e9c27b260ece9e7364b91a955523d1d2a4eeb6f2ac9bb`;
  - `MEMORY.md` SHA-256
    `815414626a592c8c1738bef7928004dacc81aae35d37d718cd0963af10eb6407`;
  - `_run_records/POST_ROOT_AGENT0_A2_INTEGRATION_2026-08-21.md` SHA-256
    `e5967b3eeac426807a4d6ecf8ad47a87b23055a9e1ad0707411bf32bd005f0f3`.
- DeclaredReads: root/App instructions and committed plan; human transcription;
  frozen orchestration plan/work graph; Root TM125 notice; DEL-08-04
  SOW/status/memory/dependencies/prior run record; Receipts 172/184; current
  Root validator/tests; affected App sources/tests; complete manager instance,
  including APP-HOLD preflight, both attempt records, telemetry, and candidate
  truth edits; Git status/diff/read-only history.
- AllowedTools: read-only file/Git inspection, SHA/JSON checks, and optional
  rerun of the exact Root validator/tests and two focused App Vitest files.
- AllowedWriteTargets: only this reviewer instance directory, specifically
  `RETURN.md` and `STATUS.json`.
- ReviewCriteria:
  1. positive canonical TASK and explicit-generalist admission are proved on
     the live HELP_HUMAN basis, without conflating enumeration and launch;
  2. unsupported named Agent 2, unresolved, missing-opt-in, Agent-2-parent,
     and noncanonical TASK-class routes are fail-closed with direct evidence;
  3. Root validator/tests plus both App check files pass and the App four-file
     implementation is unchanged since `ac2cd801...`;
  4. attempt 1 is rejected and contributes no acceptance evidence; attempt 2
     followed APP-HOLD `ALLOW` and its return is complete;
  5. only the satisfied post-Root Remaining item is removed, D-APP-103 stays,
     state remains `IN_PROGRESS`, and Checking Approval SHA is unchanged;
  6. TM125 is acknowledged as `INCORPORATED` through App-owned deliverable
     instruments, with no Root or duplicate implementation write;
  7. all claims are calibrated to validation only; derivative disposition,
     blockers, and reruns are explicit;
  8. write containment, diff hygiene, JSON parse, and frozen hashes pass.
- ExpectedReturn: verdict `PASS` with zero actionable findings, or `BLOCK`
  with numbered finding(s), exact evidence, impact, and bounded remediation.
- EXCLUSIONS: any edit outside reviewer RETURN/STATUS; repair; Root/App product,
  deliverable, shared receipt, completion, lifecycle, Git, release, provider,
  or reliance acts.
- Escalation: any hash drift, missing criterion evidence, scope conflict,
  unsupported claim, or failing check is a `BLOCK` finding.

