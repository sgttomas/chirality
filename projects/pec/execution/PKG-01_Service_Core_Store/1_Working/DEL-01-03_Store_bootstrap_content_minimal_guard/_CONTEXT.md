# _CONTEXT — DEL-01-03

| Field | Value |
|---|---|
| DeliverableID | DEL-01-03 |
| Canonical name | Store bootstrap & content-minimal guard |
| PackageID | PKG-01 (Service Core & Store) |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |
| PhaseHint | P1 |
| CoversScopeItems | SOW-056 |
| SupportsObjectives | OBJ-005 |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

Gitignored store path management, safe-delete semantics, and the ingest-boundary content-minimal enforcement layer (paths/counts/SHAs/states/hashes only).

## Anticipated artifacts

Store lifecycle module + guard + tests

## Envelope notes

(none)

## Provenance

Scaffolded under `D-PEC-62` (2026-07-25) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (SCA-001
successor), superseded by revision 1.2 (`current_basis`, SCA-002
successor). Fields templated deterministically from
`Deliverables.csv`; this file restates register truth and is not an
independent authority.
