# _CONTEXT — DEL-08-06

| Field | Value |
|---|---|
| DeliverableID | DEL-08-06 |
| Canonical name | Agent tool-call query surface |
| PackageID | PKG-08 (API & Access) |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |
| PhaseHint | P3 |
| CoversScopeItems | SOW-099 |
| SupportsObjectives | OBJ-001 |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

Read-only query interface packaged for agent tool calls over the versioned API and responses, bound to the read-only agent access class; enabling it is consumer-owned; writes nothing.

## Anticipated artifacts

Tool definitions over the read API + access-class binding + tests

## Envelope notes

Token mechanism follows OI-006; the tier-0 profile is amended before any tool is declared or invoked

## Provenance

Scaffolded under `D-PEC-101` (2026-09-26) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.6 (`current_basis`,
SCA-006 successor; deliverable added by A-28). Fields templated
deterministically from `Deliverables.csv`; this file restates register truth
and is not an independent authority.
