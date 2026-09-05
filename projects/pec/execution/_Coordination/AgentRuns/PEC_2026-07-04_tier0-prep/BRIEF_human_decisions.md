# Human Decisions - PEC tier-0 registration prep

All rows below are owner decisions. Agents may recommend and prepare artifacts;
only the owner rules. Rulings were given in-session on 2026-07-04 and are
recorded in the tier-0 register plus per-decision packets; publication remains
pending owner merge of PR #51.

| ID | Decision | Recommendation | Unblocks |
|---|---|---|---|
| D-T0-11 | Registration shape: loop dir/profile id/proposals dir/profile staging, `_LATEST.md` convention, one-time STATUS pointer, and `D-PEC-XX` local ID scheme. | Approve as authored: id `pec`, loop dir `_DomainEngines/pec/`, profile staged under `_DomainEngines/pec/profile/`, proposals dir `_DomainEngines/proposals/pec/`, `_LATEST.md` remains bridge-pointed. | D-T0-12..16 and any standing PEC loop work. |
| D-T0-12 | PEC profile lifecycle and owner Gate 2. | Use the existing validator for DRAFT-to-VALIDATED evidence; owner Gate 2 decides adoption. | Profile can later move from DRAFT to ADOPTED if owner rules. |
| D-T0-13 | Integration level target and staging. | L0 now; L2 destination staged through read-only L1 evidence then per-operation L2. L3 future-only until PEC exposes a proposal-shaped API. | Staged integration plan. |
| D-T0-14 | Data residency for PEC instance content. | Frame only; if deferred, default CLOSED/TBD and repo-file-only reads. | Whether any L1/L2 evidence may touch instance content. |
| D-T0-15 | Standing PEC loop goal and fences F-PEC-1..4. | Adopt fences and the proposed standing goal; recognize the launcher already landed ACTIVE by Receipt 0 owner direction. | The standing PEC loop can continue after the registration slate. |
| D-T0-16 | Harness-tranche authorization. | Authorize after the registration package lands and owner accepts the needed staging. | Multi-profile adapter fix, PEC alias/register/status/self-check citizenship, and profile move to `_DomainEngines/profiles/pec.yaml`. |

## Rulings recorded 2026-07-04

| ID | Ruling |
|---|---|
| D-T0-11 | O-A affirmed: authored `pec` registration shape accepted. |
| D-T0-12 | O-A affirmed: validator evidence path accepted; ADOPTED remains owner Gate 2 only. |
| D-T0-13 | O-A affirmed: L0 now, L2 destination through deterministic seams; no instance-content capture authority from this ruling. |
| D-T0-14 | Deferred: O-A CLOSED default applies for now; any O-B export/capture basis should be presented through D-PEC-01 with a concrete data case. |
| D-T0-15 | O-A affirmed: standing goal and fences adopted after package publication. |
| D-T0-16 | O-A affirmed over O-B: later TOOLMAKER harness PR authorized with sequencing and DRAFT-in-`profiles/` representation riders. |

## Gate outcome

Owner rulings have been received and recorded. This publication update still
does not change profile status to ADOPTED, execute the harness tranche, move
the profile into `_DomainEngines/profiles/`, or change PEC runtime state. Under
D-T0-16, the next lawful tranche is a separate TOOLMAKER harness PR after PR
#51 merges; that tranche must test PEC as DRAFT with Gate 2 open.
