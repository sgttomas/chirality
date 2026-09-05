# Brief — SCA-APP-010 Gate-5 post-change candidate audit

Act as a fresh, bounded, read-only `AUDIT_DECOMP` Agent 2 dispatched by
HELP_HUMAN for SCOPE_CHANGE Gate 5 (post-change candidate audit) of
SCA-APP-010 (Chirality App shell redesign, dialogue-centred information
architecture). Work only inside the git worktree at basis
`11b47882f7e8726a42829cd26db5ecd8383f43b5`. No network, no delegation, no
state-changing git commands. Read `agents/AGENT_AUDIT_DECOMP.md`, the Gate-1
pre-change baseline audit (method precedent), and the SCA-APP-009 Gate-5
post-change audit (candidate-audit form) before auditing.

Audit the candidate decomposition and companion register against the live
filesystem. The live authoritative files are NOT yet changed and must not be
touched; no deliverable folder is added or removed by this amendment.
Expected: 10 packages / 52 deliverables / 84 scope rows (79 IN / 4 OUT /
1 TBD), envelopes S9 M41 L2 XL0, forward 52/52, reverse 52/54 (PKG-00 and
DEL-00-01/02 carried), companion 83 rows / 50 families, Scope Ledger to
Deliverables reverse-view parity, valid objective mappings, no duplicate or
dangling IDs, OI-008 present with an AffectedScope count of 4 equal to the
telemetry. Expected context findings: the thirteen amended carriers'
`_CONTEXT.md` (DEL-02-01, 02-02, 02-04, 02-05, 03-02, 04-04, 05-02, 06-03,
07-01, 07-03, 08-01, 08-03, 08-04) now lag the candidate rows (WARNING,
expected and routed to WORKING_ITEMS per the propagation plan); DEL-02-02's
name differs from its folder name and `_CONTEXT.md` DeliverableName. Compare
with the Gate-1 pre-change audit, report every new finding, and state
explicitly whether any new BLOCKER or MAJOR condition exists relative to
pre-change. The active pointer remains SCA-APP-009; report SCA-APP-010 as the
candidate under audit, not active.

Write only the nine named files into
`_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Evidence/Gate5/AUDIT_DECOMP/`
(`Brief.md`, `AUDIT_DECOMP_RETURN.md`, `Decision_Log.md`,
`Decomp_Coverage_IssueLog.csv`, `Decomp_Coverage_Matrix.csv`,
`Decomp_Coverage_Report.md`, `QA_Report.md`, `RUN_SUMMARY.md`,
`coverage_summary.json`) plus the tenth file, the SCA-APP-010 root
`Post_Change_Coverage.json`, byte-identical to `coverage_summary.json`. Same
shapes and columns as the Gate-1 files. LF, no trailing whitespace. Do not
write under `_Evaluation/DecompCoverage/`; record that override in
`Decision_Log.md`. Do not modify any other file, especially not the live
decomposition or companion register.

## Normalized parameters

| Parameter | Value |
|---|---|
| `EXECUTION_ROOT` | `projects/chirality-app-dev/execution` (live deliverable folders are the filesystem side) |
| `DECOMPOSITION_PATH` (candidate) | `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Gate3/DECOMP_POSTIMAGE_CANDIDATE.md` (expected SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`) |
| Companion register (candidate) | `.../Gate3/COMPANION_POSTIMAGE_CANDIDATE.csv` (expected SHA-256 `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`) |
| Live pre-images (read-only, unchanged) | decomposition `e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97`; companion `e47fced6f0bea32b1d18f987a7e33af0432271c4ff49bb196cdad6fb91742b70` |
| `DECOMP_VARIANT` | `SOFTWARE` |
| `SCOPE` | `ALL` |
| Basis | git HEAD `11b47882f7e8726a42829cd26db5ecd8383f43b5` |
| `RUN_LABEL` | `SCA_APP_010_GATE5_POSTCHANGE` |
| `EXPECTED_HANDOFF_PHASE` | Gate 5 post-change before independent review and application |
| `REQUESTED_BY` | SCOPE_CHANGE via HELP_HUMAN |
| `PRIOR_RUN_LABEL` | `SCA_APP_010_GATE1_PRECHANGE` (at `SCA-APP-010_.../Evidence/Gate1/PRE_CHANGE_AUDIT/`) |
| Approved amendment context | `Gate3/GATE3_AMENDMENT_PACKAGE.md`; `Amendment_Actions.csv` (30 actions, 25 MODIFY / 5 ADD; SOW-081..084 added; DEL-02-02 renamed; no deliverable added or removed); `Propagation_Plan.md` sections 1 and 7 |
| Active SCA pointer | `projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md` (expected SHA-256 `f235ced4526aac51c4e7f5307ac619f3500e824c3549960b106bb80b67a6e17c`), pointing to SCA-APP-009; not moved |
| Output location | `_ScopeChange/SCA-APP-010_.../Evidence/Gate5/AUDIT_DECOMP/` and `_ScopeChange/SCA-APP-010_.../Post_Change_Coverage.json` (brief override of the `_Evaluation/DecompCoverage/` tool root) |
| Attribution | Claude Fable 5.1 (Anthropic) as a Claude Code subagent acting as AUDIT_DECOMP, dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched |
