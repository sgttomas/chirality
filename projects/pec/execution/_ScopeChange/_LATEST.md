# Latest Scope Change

| Field | Value |
|---|---|
| AmendmentID | `SCA-005` |
| Snapshot | `execution/_ScopeChange/SCA-005_2026-09-23_2139/` |
| Variant | `SOFTWARE` |
| Status | **`CLOSED_FOR_SCOPE_CHANGE_ONLY`** |
| CurrentGate | Checkpoint group 3 — audited poststate accepted |
| AcceptedBasis | `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.5 (`current_basis`) |
| Authority | D-PEC-86; owner checkpoint-1 acceptance 2026-09-24 with amendments 1 and 2; checkpoint-2 acceptance 2026-09-25 (`D-PEC-92`); checkpoint-3 acceptance 2026-09-25 |
| DecisionSnapshots | `checkpoint_snapshots/SCA-005_GROUP-1_2026-09-24/` (+ amendments 1 and 2), `SCA-005_GROUP-2_2026-09-25/`, `SCA-005_GROUP-3_2026-09-25/` |
| DecompositionTruthState | `COMPLETE` |
| DerivativePackageState | `INCOMPLETE` — Lane B and the deferred A4 remain open |
| ContentRemediationState | `NOT_REQUIRED` |
| DownstreamRerunState | `FROZEN` — no Lane B rerun authorized by checkpoint 3 |
| MetadataAlignmentState | `IN_PROGRESS` — 22 direct context mirrors done; 42 contexts and 64 references await re-pinning |
| AuditState | **`BLOCKED`** by the count rule — `COV_SCA005_POSTCHANGE_2026-09-25_1344`, 2 blockers (both the A4 deferral's expected consequence) / 6 warnings / 74 info; excluding expected consequences 0 blockers / 4 warnings |
| ReadyForNextPhase | `NO` |
| ClosureVerdict | **`CLOSED_FOR_SCOPE_CHANGE_ONLY`** (owner Q-CP3-1 (a)) |

## Result

Revision 1.5 applies the exact accepted SCA-005 amendment: the O-B2 feed
model with P-β presence, new DEL-02-08/09 register rows, four retired
deliverables, cmux deferred out of scope, and every IN item and active
deliverable mapped to an objective. PRD v2.3 is the product definition of
record. Stable IDs are preserved; no ID is reused.

## Downstream boundary

Checkpoint 3 authorizes no downstream repair. `SCA-005_2026-09-23_2139/Handoff_State.md`
and `RUN_SUMMARY.md` name every open item and owner: DEL-02-08/09 folders
with the dependency rerun (PROJECT_SETUP under its own packet), context and
reference re-pinning, SOW currency, DEL-00-01/00-03 derivative review, the
registry source packet, P1 fixtures, TM-PEC-023 disposition, the D-PEC-90
reliance amendment, and the `projects/pec/AGENTS.md` instruction tranche.
Each is separately gated.
