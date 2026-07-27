# Handoff State

**Amendment:** `SCA-APP-005`
**Current state:** `CLOSED_FOR_SCOPE_CHANGE_ONLY`
**Accepted upstream basis:** `main@fb16e32ed60bb4f384cf1e07a83c4a14ff63bbae`
**Derivative-package status:** Complete SCA snapshot plus immutable post-change audit
**Accepted decomposition changed:** yes — bounded Revision 2 wording only
**Active `_LATEST.md` changed:** yes — points to this complete SCA snapshot
**ClosureVerdict:** `CLOSED_FOR_SCOPE_CHANGE_ONLY`
**AuditState:** `WARNINGS`
**Blockers:** `0`
**DecompositionTruthState:** `COMPLETE`
**DerivativePackageState:** `COMPLETE`
**ContentRemediationState:** `NOT_REQUIRED`
**DownstreamRerunState:** `FROZEN`
**MetadataAlignmentState:** `COMPLETE`
**ReadyForNextPhase:** `NO`
**NextOwner:** `CHANGE`
**NextAction:** bounded Git closeout only
**ActiveSnapshotParity:** `PASS`

## Closure posture

Gate 1 is owner-confirmed. The owner approved the corrected Revision 2
envelope after two backchecks were reconciled. Exact Gate-3 concordance,
25-context parity, and topology invariants pass. The bounded
decomposition/context/notice propagation is applied. Post-change AUDIT_DECOMP
reports 0 blockers, 55 carried or pre-existing warnings, and 2 info findings.

## Next gate

CHANGE may stage only the exact SCA-APP-005 tranche after its own state and
path validation. No implementation or deferred repair rides the closeout.

## Carried exclusions

OD-6 contract/basis/invariant/hold/D-APP-48/49 work, implementation, method
reform, and UI/API semantic parity remain outside this amendment. The three
factual notices included here are coordination outputs only.

## Accepted upstream and derivative state

- Accepted pre-change basis:
  `main@fb16e32ed60bb4f384cf1e07a83c4a14ff63bbae`.
- Authoritative post-change surface:
  `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Active SCA snapshot:
  `execution/_ScopeChange/SCA-APP-005_2026-07-26_2334_Root_Runtime_Client_Boundary/`.
- Post-change derivative audit:
  `execution/_Evaluation/DecompCoverage/COV_SCA_APP_005_POSTCHANGE_2026-07-27_2026-07-27_0954/`.
- Audit state: `WARNINGS`, 0 blockers.
- Downstream rerun state: `FROZEN_SEPARATELY_GOVERNED`.
- Ready for next phase: `NO`; CHANGE closeout is the next governance action,
  not a downstream product phase.

## Derivative-state table

| Surface | State | Rerun requirement |
|---|---|---|
| App decomposition | `CURRENT_FOR_SCA_APP_005` | None before CHANGE. |
| 25 affected contexts | `CURRENT_FOR_DECOMPOSITION_METADATA` | Downstream ScopeOfWork work remains separate. |
| SCA snapshot | `COMPLETE_ACTIVE` | Rerun closure validation only if bytes change. |
| DecompCoverage audit | `WARNINGS_NO_BLOCKER` | Rerun only if authoritative decomposition/context/pointer bytes change. |
| ScopeOfWork contracts and pins | `FROZEN_STALE_REPAIR_REQUIRED` | OD-6 / owning App workflow; no repin here. |
| D-APP-48/49 evidence | `FROZEN_SEPARATELY_GOVERNED` | Evidence tranche after its own gate. |
| Runtime/App implementation | `NOT_AUTHORIZED` | Root and App WORKING_ITEMS under separate instruments. |
| Semantic parity | `NOT_AUTHORIZED` | New App instrument after corrected boundary. |

## Remaining blockers and next owner

No SCA-APP-005 blocker remains. The next owner is CHANGE for bounded Git
closeout. All substantive repair and implementation remain held behind their
own instruments and owner gates.
