# Brief — AUDIT_DECOMP pre-change baseline (SCA-004 Gate 2)

| Parameter | Value |
|---|---|
| `EXECUTION_ROOT` | `projects/pec/execution` |
| `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` |
| `SCOPE` | `ALL` |
| `DECOMP_VARIANT` | `SOFTWARE` |
| `RUN_LABEL` | `SCA004_PRECHANGE_2026-08-02` |
| `REQUESTED_BY` | `SCOPE_CHANGE` |
| `EXPECTED_SOURCE_SNAPSHOT` | `projects/pec/execution/_Decomposition/_LATEST.md` revision 1.3 `current_basis`, plus D-PEC-78 O-A and the confirmed SCA-004 Gate 1 intake |
| `EXPECTED_HANDOFF_PHASE` | `SCA-004 Gate 2 pre-change baseline` |

## Sealed execution boundary

Write exactly one new immutable audit snapshot under
`projects/pec/execution/_Evaluation/DecompCoverage/`. Do not update
`_Evaluation/DecompCoverage/_LATEST.md` or any decomposition, `_ScopeChange`,
deliverable, decision, receipt, source, register, lifecycle, or foreign
surface. The narrower no-pointer brief overrides the normal protocol's
pointer-update step.

This snapshot is derivative evidence. It does not replace the accepted
decomposition package, accept Gate 2, or authorize an amendment.
