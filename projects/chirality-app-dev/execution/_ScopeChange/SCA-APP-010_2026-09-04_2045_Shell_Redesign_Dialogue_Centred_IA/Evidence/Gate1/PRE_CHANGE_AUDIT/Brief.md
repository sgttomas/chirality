# Brief — SCA-APP-010 Gate-1 pre-change baseline audit

Act as a fresh, bounded, read-only `AUDIT_DECOMP` Agent 2 dispatched by
HELP_HUMAN for SCOPE_CHANGE Gate 1 step 5 (pre-change baseline) of
SCA-APP-010 (Chirality App shell redesign, dialogue-centred information
architecture). Work only inside the git worktree at basis
`95b5687a7c9a4c6fe6e655f628495dec08ce04d8` (`origin/main` after PR #706 and
PR #707). Read `agents/AGENT_AUDIT_DECOMP.md`, `agents/AGENT_SCOPE_CHANGE.md`
Gate 1 step 5, and the SCA-APP-009 Gate-5 `AUDIT_DECOMP` and
`PRE_CHANGE_AUDIT` outputs as method precedent and parity basis.

Recompute full-scope SOFTWARE decomposition coverage at this basis: topology
(expected 10 packages / 52 deliverables / 80 scope rows after SCA-APP-009),
ledger distribution, forward and reverse coverage against
`execution/PKG-*/1_Working/DEL-*/`, `_CONTEXT.md` / `_STATUS.md` /
`MEMORY.md` presence and fidelity, package discipline, objective mappings,
stable IDs, companion-register row and family counts, active SCA snapshot
completeness (SCA-APP-009 top-level layout versus the SCOPE_CHANGE snapshot
contract, and the carried SCA-APP-008 package-shape blocker), pointer parity,
and authority-corpus status. Compare with the SCA-APP-009 Gate-5 post-change
audit and state exactly what changed, noting whether the SCA-APP-009 pointer
landing changed any finding. Also report the affected-package view for
PKG-02, PKG-04, PKG-05, PKG-06, PKG-07, and PKG-08.

Write only the nine named files into
`_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Evidence/Gate1/PRE_CHANGE_AUDIT/`
(`Brief.md`, `AUDIT_DECOMP_RETURN.md`, `Decision_Log.md`,
`Decomp_Coverage_IssueLog.csv`, `Decomp_Coverage_Matrix.csv`,
`Decomp_Coverage_Report.md`, `QA_Report.md`, `RUN_SUMMARY.md`,
`coverage_summary.json`), matching the SCA-APP-009 audit shapes and column
sets. Do not write under `_Evaluation/DecompCoverage/`; record that override
in `Decision_Log.md`. Do not modify any other file, use the network, delegate,
or run state-changing git commands. Every finding cites a decomposition line
and a filesystem path; unknowns are `UNKNOWN`. Status vocabulary: OVERALL
`PASS` / `WARNINGS` / `BLOCKERS`; closure readiness `PASS` / `FAIL`.

## Normalized parameters

| Parameter | Value |
|---|---|
| `EXECUTION_ROOT` | `projects/chirality-app-dev/execution` |
| `DECOMPOSITION_PATH` | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (expected SHA-256 `e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97`) |
| Companion register | `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` (expected SHA-256 `e47fced6f0bea32b1d18f987a7e33af0432271c4ff49bb196cdad6fb91742b70`) |
| `DECOMP_VARIANT` | `SOFTWARE` |
| `SCOPE` | `ALL` (plus affected-package view for PKG-02, PKG-04, PKG-05, PKG-06, PKG-07, PKG-08) |
| Basis | git HEAD `95b5687a7c9a4c6fe6e655f628495dec08ce04d8`; working tree clean apart from the new SCA-APP-010 folder |
| `RUN_LABEL` | `SCA_APP_010_GATE1_PRECHANGE` |
| `EXPECTED_HANDOFF_PHASE` | Gate 1 pre-change baseline |
| `REQUESTED_BY` | SCOPE_CHANGE via HELP_HUMAN |
| `PRIOR_RUN_LABEL` | `SCA_APP_009_GATE5_POSTCHANGE_R3` (at `SCA-APP-009_.../Evidence/Gate5/AUDIT_DECOMP/`) |
| Active SCA pointer | `projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md` (expected SHA-256 `f235ced4526aac51c4e7f5307ac619f3500e824c3549960b106bb80b67a6e17c`), pointing to SCA-APP-009 with status `OPEN_PENDING_DERIVATIVE_CLOSURE` |
| Output location | `_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Evidence/Gate1/PRE_CHANGE_AUDIT/` (brief override of the `_Evaluation/DecompCoverage/` tool root) |
| Attribution | Claude Fable 5.1 (Anthropic) as a Claude Code subagent acting as AUDIT_DECOMP, dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched |
