# _CONTEXT — DEL-01-01

| Field | Value |
|---|---|
| DeliverableID | DEL-01-01 |
| Canonical name | Record-tier schema & entity model |
| PackageID | PKG-01 (Service Core & Store) |
| Type | DATA_MODEL_CHANGE |
| ContextEnvelope | L |
| PhaseHint | P1 |
| CoversScopeItems | SOW-001 |
| SupportsObjectives | (none mapped — see §3 mapping notes) |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

Store schema and typed entity model for the record tier: 11 PRD rows, 14 entity types (Workplan/Step/Gate and Package/Deliverable are compound rows) — Loop, Workplan, Step, Gate, Receipt, DecisionRow, Fence, Package, Deliverable, DependencyEdge, RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding.

## Anticipated artifacts

Schema/DDL + entity types + model tests

## Envelope notes

L: 14 entity types and the schema every derivation package depends on; kept one cohesive DDL slice — split (core record entities vs lifecycle/dependency/run entities) only if implementation shows a natural seam

## Provenance

Scaffolded under `D-PEC-62` (2026-07-25) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (`current_basis`,
SCA-001 successor). Fields templated deterministically from
`Deliverables.csv`; this file restates register truth and is not an
independent authority.
