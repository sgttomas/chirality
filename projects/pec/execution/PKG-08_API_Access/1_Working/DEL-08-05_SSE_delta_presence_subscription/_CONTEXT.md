# _CONTEXT — DEL-08-05

| Field | Value |
|---|---|
| DeliverableID | DEL-08-05 |
| Canonical name | SSE delta/presence subscription |
| PackageID | PKG-08 (API & Access) |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |
| PhaseHint | P4 |
| CoversScopeItems | SOW-044 |
| SupportsObjectives | (none mapped — see §3 mapping notes) |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

SSE subscription for deltas and presence changes (dashboards; long-running managers). P2/P3 dashboards poll; live subscription arrives with the P4 streams tranche — pull earlier by owner call if polling proves insufficient.

## Anticipated artifacts

SSE endpoint + tests

## Envelope notes

(none)

## Provenance

Scaffolded under `D-PEC-62` (2026-07-25) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (SCA-001
successor), superseded by revision 1.2 (`current_basis`, SCA-002
successor), in turn superseded by revision 1.3 (`current_basis`, SCA-003
successor). Fields templated deterministically from
`Deliverables.csv`; this file restates register truth and is not an
independent authority.
