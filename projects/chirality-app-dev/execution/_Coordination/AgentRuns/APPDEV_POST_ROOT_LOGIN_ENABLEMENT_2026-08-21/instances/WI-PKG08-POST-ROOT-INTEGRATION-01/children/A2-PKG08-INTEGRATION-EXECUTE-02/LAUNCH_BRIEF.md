# Sealed Agent 2 brief — post-Root integration executor, fresh attempt 2

- RequestedBy: `WI-PKG08-POST-ROOT-INTEGRATION-01`
- RunID: `APPDEV_POST_ROOT_LOGIN_ENABLEMENT_2026-08-21`
- ParentInstanceID: `WI-PKG08-POST-ROOT-INTEGRATION-01`
- ChildInstanceID: `A2-PKG08-INTEGRATION-EXECUTE-02`
- AgentForm: ephemeral bounded generalist, Agent 2; delegation prohibited.
- PackageID: `PKG-08`
- DeliverableID: `DEL-08-04`
- PredecessorDisposition: attempt 1 was interrupted and rejected before return
  because APP-HOLD preflight had not preceded dispatch; none of its work may be
  used.
- DispatchPreflight: `ALLOW` at accepted basis, recorded in
  `../../APP_HOLD_PREFLIGHT.json`; DEL-08-04 is `CLEAR` / `NOT_HELD`, scan
  fingerprint
  `7f9cc294f286f7b91ee972d615ee9ec59430575c65c200ece57dfe6042476daa`.
- Objective: independently execute and evidence the owner-enumerated post-Root
  cross-surface admission and fail-closed matrix on the current accepted basis,
  without implementing or modifying product/root truth.
- AcceptedBasis: repository commit
  `1b375af4f1219ecfc00fc2755854aa7fd4220901`; App harness implementation
  commit `ac2cd801a06a0679bc86830c627218ccca78b658`; App Receipt 172; Root
  TM125 notice; frozen parent activation/work graph.
- DeclaredReads: root `AGENTS.md`; `agents/AGENT_HELP_HUMAN.md`;
  `tools/validation/{validate_agent_instructions.py,test_validate_agent_instructions.py}`;
  App `software-workflow.json`; DEL-08-04 SOW/status/memory/run records;
  App Receipt 172 and 184; TM125 notice; prior Agent 0 direct-A2 run evidence;
  `frontend/src/lib/harness/{managed-delegation.ts,subagent-governance.ts}` and
  their exact tests; current Git state and history for commit containment.
- AllowedTools: read-only repository/Git inspection; SHA utilities; Python
  Root validator and its dedicated tests; npm/Vitest for exactly
  `managed-delegation.test.ts` and `harness-subagent-governance.test.ts`.
- AllowedWriteTargets: only this child instance directory, specifically
  `RETURN.md` and `STATUS.json`.
- RequiredMatrix:
  1. prove live HELP_HUMAN metadata allowlists canonical TASK and opts into
     ephemeral generalist Agent 2;
  2. prove Root validation admits Agent 0 to canonical TASK and generalist
     opt-in while rejecting unsupported named Agent 2, unresolved role,
     missing opt-in behavior, and Agent-2-parent routes;
  3. prove App managed launch and governance enumeration admit canonical TASK
     and explicit generalist while fail-closing the same unsupported classes;
  4. run the Root validator, its tests, and both App focused files together on
     this basis; report exact commands, exit status, and test counts.
- AcceptanceCriteria: all required positive and negative routes have cited test
  names/lines or command evidence; all four check groups exit zero; basis hashes
  match; no source/package truth changes; no claims beyond validation.
- ExpectedReturn: `RETURN.md` with verdict `PASS|BLOCK`, exact command/result
  table, route matrix, basis evidence, changed-path containment, blockers and
  reruns, and derivative-evidence disposition; `STATUS.json` with terminal
  state.
- EXCLUSIONS: edits outside this child instance; root writes; App product/test
  edits; DEL-08-04 state edits; install/package/network/provider operations;
  lifecycle/release/reliance/issuance; Git stage/commit/push/PR/merge.
- Escalation: return `BLOCK` on any failing check, missing route evidence,
  basis drift, required write, scope conflict, or authority ambiguity.
