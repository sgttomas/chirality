# _CONTEXT — DEL-06-05

| Field | Value |
|---|---|
| DeliverableID | DEL-06-05 |
| Canonical name | TTL/heartbeat discipline & citation exclusion |
| PackageID | PKG-06 (Presence & Git Observation) |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |
| PhaseHint | P3 |
| CoversScopeItems | SOW-030;SOW-032 |
| SupportsObjectives | OBJ-003 |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

TTLs and last-heartbeat age on presence records; liveness never asserted beyond heartbeat; enforced exclusion of presence data from record-tier citations. The exclusion is two-sided: the presence-store guard lands here; the citation-production side is asserted in DEL-04-03's tests (declared dependency edge, DL-14).

## Anticipated artifacts

TTL machinery + exclusion guard + tests

## Envelope notes

(none)

## Provenance

Scaffolded under `D-PEC-62` (2026-07-25) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (SCA-001
successor), superseded by revision 1.2 (`current_basis`, SCA-002
successor), in turn superseded by revision 1.3 (`current_basis`, SCA-003
successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
Fields templated deterministically from
`Deliverables.csv`; this file restates register truth and is not an
independent authority.
