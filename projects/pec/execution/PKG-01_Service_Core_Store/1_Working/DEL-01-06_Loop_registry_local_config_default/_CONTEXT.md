# _CONTEXT — DEL-01-06

| Field | Value |
|---|---|
| DeliverableID | DEL-01-06 |
| Canonical name | Loop registry (local config default) |
| PackageID | PKG-01 (Service Core & Store) |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | S |
| PhaseHint | P1 |
| CoversScopeItems | SOW-077;SOW-094 |
| SupportsObjectives | OBJ-004 |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

PEC-owned local configuration naming the loop locators PEC serves: one loop at P1 (PEC's own build, OI-010), extendable by owner-gated PEC configuration changes. The strict, versioned JSON/schema paths and core-owned typed port are the long-term home and shape under D-PEC-78; each listed loop remains authoritative for its own entrypoint and truth, and no governed act depends on PEC or the registry. Each row declares a closed, PEC-versioned feed profile (profile ID, version, live/historical, basis citation to the loop's own record), PEC's reading hypothesis and never the loop's truth; PEC's own row declares `remaining-loop` now. Feed-profile declarations need a strict schema v2 (`loops.schema.json` v2, `loops.json`, a `RegisteredLoop` field) through a later D-PEC source packet within D-PEC-78 O-A, with VER-001/VER-003 re-run: a new Scope of Work currency obligation (RF-002 stays resolved).

## Anticipated artifacts

Config format + loader + tests

## Envelope notes

(none)

## Provenance

Scaffolded under `D-PEC-62` (2026-07-25) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (SCA-001
successor), superseded by revision 1.2 (`current_basis`, SCA-002
successor), in turn superseded by revision 1.3 (`current_basis`, SCA-003
successor), then by revision 1.4 (`current_basis`, SCA-004 successor),
then by revision 1.5 (`current_basis`, SCA-005 successor).
Fields templated deterministically from
`Deliverables.csv`; this file restates register truth and is not an
independent authority.
