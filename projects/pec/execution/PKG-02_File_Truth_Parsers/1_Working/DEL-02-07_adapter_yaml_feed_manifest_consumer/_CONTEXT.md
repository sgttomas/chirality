# _CONTEXT — DEL-02-07

| Field | Value |
|---|---|
| DeliverableID | DEL-02-07 |
| Canonical name | `adapter.yaml` feed-manifest consumer |
| PackageID | PKG-02 (File-Truth Parsers) |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | S |
| PhaseHint | P1 |
| CoversScopeItems | SOW-017 |
| SupportsObjectives | OBJ-001;OBJ-002 |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

Per-project `_harness/adapter.yaml` consumed as the feed manifest driving which feeds are read per loop.

## Anticipated artifacts

Manifest reader + fixture tests

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
