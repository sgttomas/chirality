# Brief — COV_SCA003_POSTCHANGE_INTERIM

## Verbatim sealed brief

> Act as Agent 2 AUDIT_DECOMP for PEC SCA-003 post-change interim audit. Read
> in full: root AGENTS.md, projects/pec/AGENTS.md,
> agents/AGENT_AUDIT_DECOMP.md. Work only in isolated worktree
> /private/tmp/chirality-pec-sca003-exec.
> EXECUTION_ROOT=/private/tmp/chirality-pec-sca003-exec/projects/pec/execution;
> DECOMP_PATH=/private/tmp/chirality-pec-sca003-exec/projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md;
> SCOPE=all; DECOMP_TYPE=SOFTWARE;
> RUN_LABEL=SCA003_POSTCHANGE_INTERIM; REQUESTED_BY=SCOPE_CHANGE;
> EXPECTED_PHASE=Gate 5 pre-snapshot; expected source is the accepted
> decomposition working state being assembled into SCA-003. This is read-only
> except the audit-owned directory under _Evaluation/DecompCoverage and its
> _LATEST pointer. Execute the governed audit fully, write the immutable audit
> snapshot and pointer, and return verdict, issues, artifact paths, and hashes.
> Do not modify decomposition, SCA, packages, contracts, dependencies, hold,
> lifecycle, or implementation.

## Normalized parameters

| Parameter | Value |
|---|---|
| `EXECUTION_ROOT` | `/private/tmp/chirality-pec-sca003-exec/projects/pec/execution` |
| `DECOMPOSITION_PATH` | `/private/tmp/chirality-pec-sca003-exec/projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` |
| `SCOPE` | `ALL` |
| `DECOMP_VARIANT` | `SOFTWARE` |
| `RUN_LABEL` | `SCA003_POSTCHANGE_INTERIM` |
| `REQUESTED_BY` | `SCOPE_CHANGE` |
| `EXPECTED_SOURCE_SNAPSHOT` | `accepted decomposition working state being assembled into SCA-003` |
| `EXPECTED_HANDOFF_PHASE` | `Gate 5 pre-snapshot` |
| `PRIOR_RUN_LABEL` | not provided |
