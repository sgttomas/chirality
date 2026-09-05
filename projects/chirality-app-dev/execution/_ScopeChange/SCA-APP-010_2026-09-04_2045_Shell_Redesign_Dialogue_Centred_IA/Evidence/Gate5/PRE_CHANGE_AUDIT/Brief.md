# Brief — SCA-APP-010 Gate-5 pre-change baseline audit (actual execution basis)

Act as a fresh, bounded, read-only `AUDIT_DECOMP` Agent 2 dispatched by
HELP_HUMAN for SCOPE_CHANGE Gate 5 (pre-change baseline at the actual
execution basis) of SCA-APP-010 (Chirality App shell redesign,
dialogue-centred information architecture). Work only inside the git worktree
at basis `11b47882f7e8726a42829cd26db5ecd8383f43b5`, a fast-forward descendant
of the Gate-1 basis `95b5687a7c9a4c6fe6e655f628495dec08ce04d8`. Read
`agents/AGENT_AUDIT_DECOMP.md` and, as the exact method precedent and the
baseline to compare against, the nine files under
`SCA-APP-010_.../Evidence/Gate1/PRE_CHANGE_AUDIT/`. Reproduce that method
exactly.

Recompute the full-scope SOFTWARE decomposition coverage at this basis:
topology (expected 10 packages / 52 deliverables / 80 scope rows), ledger
distribution (expected 75 IN / 4 OUT / 1 TBD), forward and reverse coverage
against `execution/PKG-*/1_Working/DEL-*/`, `_CONTEXT.md` / `_STATUS.md` /
`MEMORY.md` presence and fidelity, package discipline, objective mappings,
stable IDs, companion-register row and family counts (expected 83 / 50),
active SCA snapshot completeness for SCA-APP-009, pointer parity, and
authority-corpus status via
`python3 projects/chirality-app-dev/execution/_Reconciliation/References/reconcile_authority_corpus.py status`.
Verify with git that the only changes between the Gate-1 basis and HEAD are
files under the SCA-APP-010 snapshot folder and
`projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`, and that the SCA-APP-009
folder tree is unchanged (git tree `1c5b9e68049460c3a9a6c1abadc1b8a64e2bc085`).
The working tree carries an uncommitted edit to the SCA-APP-010 snapshot's
`Decision_Log.md` (G4-CONFIRM row); read it as data. State explicitly what
changed versus the Gate-1 audit. The SCA-APP-010 snapshot has grown but is
not the active snapshot; report it as a non-active in-progress SCA folder,
not as an error.

Write only the nine named files into
`_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Evidence/Gate5/PRE_CHANGE_AUDIT/`
(`Brief.md`, `AUDIT_DECOMP_RETURN.md`, `Decision_Log.md`,
`Decomp_Coverage_IssueLog.csv`, `Decomp_Coverage_Matrix.csv`,
`Decomp_Coverage_Report.md`, `QA_Report.md`, `RUN_SUMMARY.md`,
`coverage_summary.json`), with the same shapes and column sets as the Gate-1
files; LF line endings, no trailing whitespace. Do not write under
`_Evaluation/DecompCoverage/`; record that override in `Decision_Log.md`. Do
not modify any other file, use the network, delegate, or run state-changing
git commands. Every finding cites a decomposition line and a filesystem path;
unknowns are `UNKNOWN`. Status vocabulary: OVERALL `PASS` / `WARNINGS` /
`BLOCKERS`; closure readiness `PASS` / `FAIL`.

## Normalized parameters

| Parameter | Value |
|---|---|
| `EXECUTION_ROOT` | `projects/chirality-app-dev/execution` |
| `DECOMPOSITION_PATH` | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (expected SHA-256 `e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97`; the live file, unchanged) |
| Companion register | `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` (expected SHA-256 `e47fced6f0bea32b1d18f987a7e33af0432271c4ff49bb196cdad6fb91742b70`) |
| `DECOMP_VARIANT` | `SOFTWARE` |
| `SCOPE` | `ALL` |
| Basis | git HEAD `11b47882f7e8726a42829cd26db5ecd8383f43b5` (fast-forward descendant of Gate-1 basis `95b5687a7c9a4c6fe6e655f628495dec08ce04d8`); working tree clean apart from the uncommitted SCA-APP-010 `Decision_Log.md` edit |
| `RUN_LABEL` | `SCA_APP_010_GATE5_PRECHANGE` |
| `EXPECTED_HANDOFF_PHASE` | Gate 5 pre-change |
| `REQUESTED_BY` | SCOPE_CHANGE via HELP_HUMAN |
| `PRIOR_RUN_LABEL` | `SCA_APP_010_GATE1_PRECHANGE` (at `SCA-APP-010_.../Evidence/Gate1/PRE_CHANGE_AUDIT/`) |
| Active SCA pointer | `projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md` (expected SHA-256 `f235ced4526aac51c4e7f5307ac619f3500e824c3549960b106bb80b67a6e17c`), pointing to SCA-APP-009 with status `OPEN_PENDING_DERIVATIVE_CLOSURE`; SCA-APP-009 git tree expected `1c5b9e68049460c3a9a6c1abadc1b8a64e2bc085` |
| Output location | `_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Evidence/Gate5/PRE_CHANGE_AUDIT/` (brief override of the `_Evaluation/DecompCoverage/` tool root) |
| Attribution | Claude Fable 5.1 (Anthropic) as a Claude Code subagent acting as AUDIT_DECOMP, dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched |
