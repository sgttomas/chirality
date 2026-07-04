# Human Decisions - PEC tier-0 registration prep

All rows below are owner decisions. Agents may recommend and prepare artifacts;
only the owner rules. No `Ruling SHA` field is present until a ruling is
published.

| ID | Decision | Recommendation | Unblocks |
|---|---|---|---|
| D-T0-11 | Registration shape: loop dir/profile id/proposals dir/profile staging, `_LATEST.md` convention, one-time STATUS pointer, and `D-PEC-XX` local ID scheme. | Approve as authored: id `pec`, loop dir `_DomainEngines/pec/`, profile staged under `_DomainEngines/pec/profile/`, proposals dir `_DomainEngines/proposals/pec/`, `_LATEST.md` remains bridge-pointed. | D-T0-12..16 and any standing PEC loop work. |
| D-T0-12 | PEC profile lifecycle and owner Gate 2. | Use the existing validator for DRAFT-to-VALIDATED evidence; owner Gate 2 decides adoption. | Profile can later move from DRAFT to ADOPTED if owner rules. |
| D-T0-13 | Integration level target and staging. | L0 now; L2 destination staged through read-only L1 evidence then per-operation L2. L3 future-only until PEC exposes a proposal-shaped API. | Staged integration plan. |
| D-T0-14 | Data residency for PEC instance content. | Frame only; if deferred, default CLOSED/TBD and repo-file-only reads. | Whether any L1/L2 evidence may touch instance content. |
| D-T0-15 | Standing PEC loop goal and fences F-PEC-1..4. | Adopt fences and the proposed standing goal; recognize the launcher already landed ACTIVE by Receipt 0 owner direction. | The standing PEC loop can continue after the registration slate. |
| D-T0-16 | Harness-tranche authorization. | Authorize after the registration package lands and owner accepts the needed staging. | Multi-profile adapter fix, PEC alias/register/status/self-check citizenship, and profile move to `_DomainEngines/profiles/pec.yaml`. |

## Gate

Stop here for owner ruling. Filling any `HumanRuling`, changing profile status
to ADOPTED, executing the harness tranche, moving the profile into
`_DomainEngines/profiles/`, or changing PEC runtime state is outside this prep.

