# Latest Scope Change

| Field | Value |
|---|---|
| AmendmentID | `SCA-004` |
| Snapshot | `execution/_ScopeChange/SCA-004_2026-08-02_2325/` |
| Variant | `SOFTWARE` |
| Status | **`CLOSED_FOR_SCOPE_CHANGE_ONLY`** |
| CurrentGate | Gate 5 — Confirmed / Executed / Validated |
| AcceptedBasis | `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.4 (`current_basis`) |
| Authority | D-PEC-78 O-A and owner SCA-004 Gate 5 direction, 2026-08-03 |
| DecompositionTruthState | `COMPLETE` |
| DerivativePackageState | `INCOMPLETE` — downstream surfaces remain stale |
| ContentRemediationState | `NOT_REQUIRED` |
| DownstreamRerunState | `FROZEN` — no downstream repair authorized by Gate 5 |
| MetadataAlignmentState | `NOT_STARTED` — 63 contexts / 64 references |
| AuditState | **`WARNINGS`** — `COV_SCA004_POSTCHANGE_2026-08-03_1442`, 0 blockers / 1 unchanged unrelated warning |
| ReadyForNextPhase | `NO` |
| ClosureVerdict | **`CLOSED_FOR_SCOPE_CHANGE_ONLY`** |

## Result

Revision 1.4 applies the exact approved SCA-004 postimage and direct
DEL-01-06 context mirror. SOW-077 is now `IN` and maps to PKG-01 /
DEL-01-06 / OBJ-004; OI-003 is resolved by D-PEC-78 O-A. Stable IDs,
topology, source, dependencies, lifecycle, envelope, phase, name, and path are
unchanged.

## Downstream boundary

Gate 5 performed no downstream repair. `SCA-004_2026-08-02_2325/Handoff_State.md`
is the controlling derivative-state handoff and names every stale population,
owner, and rerun obligation: 63 contexts, 64 references, the DEL-01-06
requirement anchor, four SOW contracts, the DEL-00-03 SPEC, and four PEC
orientation/map surfaces. Each is separately gated.
