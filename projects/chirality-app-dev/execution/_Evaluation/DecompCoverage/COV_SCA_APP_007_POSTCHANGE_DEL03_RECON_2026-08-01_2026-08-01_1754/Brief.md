# AUDIT_DECOMP Brief

## Verbatim brief

Act as named Agent 2 AUDIT_DECOMP under SCOPE_CHANGE for the required SCA-APP-007 Gate-5 post-change audit. Load and follow repo `AGENTS.md` and `agents/AGENT_AUDIT_DECOMP.md`.

- `EXECUTION_ROOT=/Users/ryan/.codex/worktrees/5bef/chirality/projects/chirality-app-dev/execution`
- `DECOMPOSITION_PATH=/Users/ryan/.codex/worktrees/5bef/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- `SCOPE=PKG-03,PKG-09`
- `DECOMP_VARIANT=SOFTWARE`
- `RUN_LABEL=SCA_APP_007_POSTCHANGE_DEL03_RECON_2026-08-01`
- `REQUESTED_BY=SCOPE_CHANGE`
- `EXPECTED_SOURCE_SNAPSHOT=current accepted decomposition plus SCA-APP-007 Gate-5 migrated filesystem`
- `EXPECTED_HANDOFF_PHASE=SCA-APP-007 Gate 5 post-change`

Objective: create a new immutable audit snapshot under `execution/_Evaluation/DecompCoverage`, prove the former DEL-03-06 reverse-only and duplicate physical PKG-03 warnings are gone, no new blocker, and report topology.

Critical sealed override: do not update `execution/_Evaluation/DecompCoverage/_LATEST.md`; the current active pointer must remain unchanged. Read-only on deliverables and decomposition; write only the new audit snapshot. No delegation.

## Normalized parameters

| Parameter | Value |
|---|---|
| Execution root | `projects/chirality-app-dev/execution` |
| Decomposition | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| Variant | `SOFTWARE` |
| Scope | `PKG-03,PKG-09` |
| Requested by | `SCOPE_CHANGE` |
| Source basis | current accepted decomposition plus SCA-APP-007 Gate-5 migrated filesystem |
| Handoff phase | `SCA-APP-007 Gate 5 post-change` |
| Write zone | this new snapshot folder only |
