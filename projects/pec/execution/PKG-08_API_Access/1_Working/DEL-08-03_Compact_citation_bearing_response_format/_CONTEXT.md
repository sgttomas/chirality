# _CONTEXT — DEL-08-03

| Field | Value |
|---|---|
| DeliverableID | DEL-08-03 |
| Canonical name | Compact citation-bearing response format |
| PackageID | PKG-08 (API & Access) |
| Type | API_CONTRACT |
| ContextEnvelope | M |
| PhaseHint | P1 |
| CoversScopeItems | SOW-043;SOW-098 |
| SupportsObjectives | OBJ-001 |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

Machine-first response envelope carrying citations. Responses are bounded by declared size budgets met by pagination or continuation, with any truncation stated.

## Anticipated artifacts

Format spec + serializer + tests

## Envelope notes

M under SCA-006: declared response-size budgets met by pagination or continuation, with stated truncation, join the compact citation-bearing format (SOW-043, SOW-098); kept one cohesive format slice

## Provenance

Scaffolded under `D-PEC-62` (2026-07-25) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (SCA-001
successor), superseded by revision 1.2 (`current_basis`, SCA-002
successor), in turn superseded by revision 1.3 (`current_basis`, SCA-003
successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
then by revision 1.5 (`current_basis`, SCA-005 successor),
then by revision 1.6 (`current_basis`, SCA-006 successor).
Fields templated deterministically from
`Deliverables.csv`; this file restates register truth and is not an
independent authority.
