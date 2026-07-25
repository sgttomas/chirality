# _CONTEXT — DEL-00-02

| Field | Value |
|---|---|
| DeliverableID | DEL-00-02 |
| Canonical name | Event-contract schema v1 |
| PackageID | PKG-00 (Architecture Runway & Contracts) |
| Type | API_CONTRACT |
| ContextEnvelope | M |
| PhaseHint | P2 |
| CoversScopeItems | SOW-034 |
| SupportsObjectives | (none mapped — see §3 mapping notes) |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

Versioned event contract types consumable by daemon, hooks CLI, and adapters; PEC-local schema with pinned-mirror posture pending OI-009; additive evolution. Published one phase ahead of its P3 consumers (DEL-07-01/-03) per the PKG-00 publish/consume mechanic.

## Anticipated artifacts

Schema definitions + contract tests + versioning note

## Envelope notes

OI-009 keeps the contract home open; local schema + pinned mirror until ruled — a shared-runtime ruling moves the home under its own instrument (SOW-074)

## Provenance

Scaffolded under `D-PEC-62` (2026-07-25) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (`current_basis`,
SCA-001 successor). Fields templated deterministically from
`Deliverables.csv`; this file restates register truth and is not an
independent authority.
