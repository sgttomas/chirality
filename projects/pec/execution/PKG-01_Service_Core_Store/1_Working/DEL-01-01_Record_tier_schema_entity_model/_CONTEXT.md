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
| SupportsObjectives | OBJ-001;OBJ-002 |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

Store schema and typed entity model for the record tier: 16 entity types (Workplan/Step/Gate, Package/Deliverable and WorkGraph/WorkNode are compound rows) — Loop, Workplan, Step, Gate, Receipt, DecisionRow, Fence, Package, Deliverable, DependencyEdge, RunRecord, CandidateBrief, OrientationSnapshot, DriftFinding, WorkGraph, WorkNode. Workplan/Step/Gate is a declared historical-grammar entity whose gate state is re-sourced from decision registers, scope-change pointers and graph BLOCKED nodes; Receipt covers ledger entries and central `RECEIPT.md`; RunRecord is sourced from central receipts, work graphs and the MEMORY run index, with JSON run evidence historical; "remaining items" is a per-loop optional field.

## Anticipated artifacts

Schema/DDL + entity types + model tests

## Envelope notes

L: 16 entity types (DL-14's 14 plus WorkGraph and WorkNode) and the schema every derivation package depends on; kept one cohesive DDL slice — split (core record entities vs lifecycle/dependency/run/graph entities) only if implementation shows a natural seam

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
