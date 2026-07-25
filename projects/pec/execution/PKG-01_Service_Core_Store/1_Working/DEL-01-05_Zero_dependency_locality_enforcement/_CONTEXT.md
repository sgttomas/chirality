# _CONTEXT — DEL-01-05

| Field | Value |
|---|---|
| DeliverableID | DEL-01-05 |
| Canonical name | Zero-dependency & locality enforcement |
| PackageID | PKG-01 (Service Core & Store) |
| Type | CI_CD_CHANGE |
| ContextEnvelope | S |
| PhaseHint | P1 |
| CoversScopeItems | SOW-052;SOW-053 |
| SupportsObjectives | (none mapped — see §3 mapping notes) |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

Automated assertion that the service core carries no third-party runtime dependencies (workspace-internal contracts permitted) and no external egress.

## Anticipated artifacts

CI/lint check + posture note

## Envelope notes

(none)

## Provenance

Scaffolded under `D-PEC-62` (2026-07-25) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (`current_basis`,
SCA-001 successor). Fields templated deterministically from
`Deliverables.csv`; this file restates register truth and is not an
independent authority.
