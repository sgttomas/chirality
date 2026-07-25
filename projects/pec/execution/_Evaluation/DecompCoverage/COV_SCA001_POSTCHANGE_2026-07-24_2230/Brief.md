# AUDIT_DECOMP Brief — SCA-001 Post-change

## Verbatim brief

> Act as dedicated AUDIT_DECOMP Agent 2 for PEC SCA-001 Gate 5 post-change
> audit. Read agents/AGENT_AUDIT_DECOMP.md completely and obey it, plus root
> and projects/pec/AGENTS.md. Inputs:
> EXECUTION_ROOT=projects/pec/execution;
> DECOMPOSITION_PATH=projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md;
> SCOPE=ALL; DECOMP_VARIANT=SOFTWARE; RUN_LABEL=SCA001_POSTCHANGE;
> REQUESTED_BY=SCOPE_CHANGE;
> EXPECTED_SOURCE_SNAPSHOT=projects/pec/execution/_Decomposition/_LATEST.md;
> EXPECTED_HANDOFF_PHASE=SCOPE_CHANGE_GATE_5. The amended package is revision
> 1.1 but Project Setup remains unscaffolded, so preserve the
> contract-required FAILED_INPUTS result if no deliverable folders are
> discoverable. Write only the required immutable audit snapshot and audit
> _LATEST pointer under
> projects/pec/execution/_Evaluation/DecompCoverage/. Do not write any
> decomposition, PRD, coordination, SCA, project pointer, or other surface.
> Return snapshot path, RUN_STATUS, exact failure evidence, and files written.

## Normalized parameters

- `EXECUTION_ROOT`: `projects/pec/execution`
- `DECOMPOSITION_PATH`:
  `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`
- `SCOPE`: `ALL`
- `DECOMP_VARIANT`: `SOFTWARE`
- `RUN_LABEL`: `SCA001_POSTCHANGE`
- `REQUESTED_BY`: `SCOPE_CHANGE`
- `EXPECTED_SOURCE_SNAPSHOT`:
  `projects/pec/execution/_Decomposition/_LATEST.md`
- `EXPECTED_HANDOFF_PHASE`: `SCOPE_CHANGE_GATE_5`
- Evaluated decomposition revision: `1.1`
- Evaluated repository HEAD:
  `6c74959adfa50245ecb5345653851ebf258c5890`
