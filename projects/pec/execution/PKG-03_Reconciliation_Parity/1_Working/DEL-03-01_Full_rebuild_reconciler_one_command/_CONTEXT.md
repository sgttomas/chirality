# _CONTEXT — DEL-03-01

| Field | Value |
|---|---|
| DeliverableID | DEL-03-01 |
| Canonical name | Full-rebuild reconciler (one command) |
| PackageID | PKG-03 (Reconciliation & Parity) |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |
| PhaseHint | P1 |
| CoversScopeItems | SOW-010;SOW-021 |
| SupportsObjectives | OBJ-005 |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

One-command full rebuild of the record tier from sources; writes restricted to the store and generated views; store safe to delete.

## Anticipated artifacts

Reconciler entry point + rebuild tests

## Envelope notes

(none)

## Provenance

Scaffolded under `D-PEC-62` (2026-07-25) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (SCA-001
successor), superseded by revision 1.2 (`current_basis`, SCA-002
successor). Fields templated deterministically from
`Deliverables.csv`; this file restates register truth and is not an
independent authority.
