# Brief — COV_SCA003_POSTCHANGE_FINAL

## Verbatim sealed brief

> Run the required final post-snapshot AUDIT_DECOMP now. Re-read any needed
> instructions. Same isolated worktree and scopes as prior run.
> RUN_LABEL=SCA003_POSTCHANGE_FINAL; REQUESTED_BY=SCOPE_CHANGE;
> EXPECTED_PHASE=Gate 5 final;
> EXPECTED_SOURCE_SNAPSHOT=/private/tmp/chirality-pec-sca003-exec/projects/pec/execution/_ScopeChange/SCA-003_2026-07-28_0824.
> The SCA-003 snapshot and both `_Decomposition/_LATEST.md` and
> `_ScopeChange/_LATEST.md` now exist; Post_Change_Coverage.json currently
> contains the clean interim summary. Audit-owned writes only under
> `_Evaluation/DecompCoverage` plus its `_LATEST.md`. Return verdict, issues,
> artifact paths, and hashes.

## Normalized parameters

| Parameter | Value |
|---|---|
| `EXECUTION_ROOT` | `/private/tmp/chirality-pec-sca003-exec/projects/pec/execution` |
| `DECOMPOSITION_PATH` | `/private/tmp/chirality-pec-sca003-exec/projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` |
| `SCOPE` | `ALL` |
| `DECOMP_VARIANT` | `SOFTWARE` |
| `RUN_LABEL` | `SCA003_POSTCHANGE_FINAL` |
| `REQUESTED_BY` | `SCOPE_CHANGE` |
| `EXPECTED_SOURCE_SNAPSHOT` | `/private/tmp/chirality-pec-sca003-exec/projects/pec/execution/_ScopeChange/SCA-003_2026-07-28_0824` |
| `EXPECTED_HANDOFF_PHASE` | `Gate 5 final` |
| `PRIOR_RUN_LABEL` | not provided |

## Brief amendment received during execution

The invoking manager reported that `SOFTWARE_DECOMP.md` §7 telemetry had been
corrected after dispatch. This run discarded the earlier in-turn read and
audited the current postimage at SHA-256
`3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787`.
