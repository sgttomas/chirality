# AUDIT_DECOMP Brief

## Verbatim brief

Act as named Agent 2 AUDIT_DECOMP under SCOPE_CHANGE. Load and follow `/Users/ryan/.codex/worktrees/5bef/chirality/AGENTS.md` and `agents/AGENT_AUDIT_DECOMP.md`.

- `EXECUTION_ROOT=/Users/ryan/.codex/worktrees/5bef/chirality/projects/chirality-app-dev/execution`
- `DECOMPOSITION_PATH=/Users/ryan/.codex/worktrees/5bef/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- `SCOPE=PKG-03,PKG-09`
- `DECOMP_VARIANT=SOFTWARE`
- `RUN_LABEL=SCA_APP_007_PRECHANGE_DEL03_RECON_2026-08-01`
- `REQUESTED_BY=SCOPE_CHANGE`
- `EXPECTED_SOURCE_SNAPSHOT=current accepted decomposition plus execution/_ScopeChange/_LATEST.md`
- `EXPECTED_HANDOFF_PHASE=SCA-APP-007 Gate 1 pre-change`

Objective: produce the required immutable AUDIT_DECOMP snapshot under `execution/_Evaluation/DecompCoverage`, and report the `coverage_summary.json` path. Pay special attention to duplicate PKG-03 physical folders, declared DEL-03-01..04, absence/history residue DEL-03-05, undeclared DEL-03-06, and accepted DEL-09-06. Read-only on all deliverables/decomposition; only write audit snapshot and pointer per the AUDIT_DECOMP contract. No delegation.

## Normalized parameters

| Parameter | Value |
|---|---|
| Execution root | `projects/chirality-app-dev/execution` |
| Decomposition | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| Variant | `SOFTWARE` |
| Scope | `PKG-03,PKG-09` |
| Requested by | `SCOPE_CHANGE` |
| Source basis | current accepted decomposition plus `execution/_ScopeChange/_LATEST.md` |
| Handoff phase | `SCA-APP-007 Gate 1 pre-change` |
| Write zone | `execution/_Evaluation/DecompCoverage/` only |
