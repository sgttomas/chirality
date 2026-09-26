# Latest Scope Change

| Field | Value |
|---|---|
| AmendmentID | `SCA-006` |
| Snapshot | `execution/_ScopeChange/SCA-006_2026-09-25_1912/` |
| Variant | `SOFTWARE` |
| Status | **`CLOSED_FOR_SCOPE_CHANGE_ONLY`** |
| CurrentGate | Checkpoint group 3 — audited poststate accepted |
| AcceptedBasis | `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.6 (`current_basis`) |
| AcceptedPredecessor | `SCA-005` (`execution/_ScopeChange/SCA-005_2026-09-23_2139/`) |
| Authority | D-PEC-90 R-A with D-PEC-94; owner checkpoint-1 acceptance 2026-09-25; checkpoint-2 acceptance 2026-09-25 (`D-PEC-97`) with amendment 1 (2026-09-26); checkpoint-3 acceptance 2026-09-26 |
| DecisionSnapshots | `checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/`, `SCA-006_GROUP-2_2026-09-25/` (+ `SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/`), `SCA-006_GROUP-3_2026-09-26/` |
| DecompositionTruthState | `COMPLETE` |
| DerivativePackageState | `INCOMPLETE` — Lane B1–B8 and the COV-083 correction open, each under its own packet |
| ContentRemediationState | `NOT_REQUIRED` |
| DownstreamRerunState | `FROZEN` — no Lane B item authorized by checkpoint 3 |
| MetadataAlignmentState | `IN_PROGRESS` — three direct `_CONTEXT.md` mirrors written; the B7 re-pin to revision 1.6 / PRD v2.4 is open |
| AuditState | `WARNINGS` — `COV_SCA006_POSTCHANGE_2026-09-26_0051`, 0 blockers / 3 pre-existing warnings / 71 info / 12 expected consequences |
| ReadyForNextPhase | `NO` |
| ClosureVerdict | **`CLOSED_FOR_SCOPE_CHANGE_ONLY`** (owner acceptance of 2026-09-26) |

## Result

Revision 1.6 applies the exact accepted SCA-006 amendment: operational
reliance on PEC data within the declared pin, coverage and tier, with file
fallback and only from a release that has passed the §12
reliance-advertisement gate; the read-only `agent` access class and a
tool-call query surface; the reliance envelope and response-size budgets;
new SOW-097..100 and register rows DEL-08-06 and DEL-10-13. PRD v2.4 is the
product definition of record. Authority is unchanged: PEC output stays
never citable as authority (R-C excluded). Stable IDs are preserved; no ID
is reused.

## Downstream boundary

Checkpoint 3 authorized no downstream repair; each downstream item is
separately gated (`SCA-006_2026-09-25_1912/RUN_SUMMARY.md` §6). The
`remaining-loop` design text (COV-083) is carried knowingly and routed to a
later PEC scope change. Undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`
plans the open items in
`_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`.
