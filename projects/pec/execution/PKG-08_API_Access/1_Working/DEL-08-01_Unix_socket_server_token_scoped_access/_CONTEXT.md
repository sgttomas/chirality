# _CONTEXT — DEL-08-01

| Field | Value |
|---|---|
| DeliverableID | DEL-08-01 |
| Canonical name | Unix-socket server + token-scoped access |
| PackageID | PKG-08 (API & Access) |
| Type | SECURITY_CONTROL |
| ContextEnvelope | M |
| PhaseHint | P1 |
| CoversScopeItems | SOW-003;SOW-040 |
| SupportsObjectives | OBJ-001 |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

Local-only Unix-socket binding with token-scoped access classes (owner, harness, admin); auth-reuse choice tracked by OI-006.

## Anticipated artifacts

Socket server + auth + tests

## Envelope notes

OI-006 determines the token mechanism (PEC-local vs daemon registry); the socket+access-class core is stable either way, but the auth half may be reworked on ruling

## Provenance

Scaffolded under `D-PEC-62` (2026-07-25) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (SCA-001
successor), superseded by revision 1.2 (`current_basis`, SCA-002
successor). Fields templated deterministically from
`Deliverables.csv`; this file restates register truth and is not an
independent authority.
