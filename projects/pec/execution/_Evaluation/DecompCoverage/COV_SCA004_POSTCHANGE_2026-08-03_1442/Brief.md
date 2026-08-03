# Brief — AUDIT_DECOMP post-change validation (SCA-004 Gate 5)

| Parameter | Value |
|---|---|
| `EXECUTION_ROOT` | `projects/pec/execution` |
| `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` |
| `SCOPE` | `ALL` |
| `DECOMP_VARIANT` | `SOFTWARE` |
| `RUN_LABEL` | `SCA004_POSTCHANGE` |
| `REQUESTED_BY` | `SCOPE_CHANGE` |
| `PRIOR_RUN_LABEL` | `COV_SCA004_PRECHANGE_2026-08-02_2327` |
| `EXPECTED_SOURCE_SNAPSHOT` | SCA-004 Gate 5 revision 1.4 candidate under D-PEC-78 O-A and the owner's 2026-08-03 execution direction |
| `EXPECTED_HANDOFF_PHASE` | SCA-004 Gate 5 post-change validation before pointer movement |

This run is read-only on decomposition and deliverable content. It writes only
this immutable audit snapshot. Pointer movement is serialized after the SCA
snapshot is complete and is verified separately by the Gate 5 integration
owner.
