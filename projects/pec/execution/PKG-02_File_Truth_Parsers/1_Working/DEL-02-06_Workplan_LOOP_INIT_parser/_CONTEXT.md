# _CONTEXT — DEL-02-06

| Field | Value |
|---|---|
| DeliverableID | DEL-02-06 |
| Canonical name | Workplan/LOOP_INIT parser |
| PackageID | PKG-02 (File-Truth Parsers) |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |
| PhaseHint | P1 |
| CoversScopeItems | SOW-016 |
| SupportsObjectives | OBJ-001;OBJ-002 |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

`LOOP_INIT.md` loop identity, entrypoint and procedure SHA only; workplans as a declared historical grammar; no step/gate state is read from `LOOP_INIT.md` (gate state is re-sourced per SOW-001). Name "Workplan/LOOP_INIT parser" and path retained under SCA-005 (CP1-N); the label now overstates the live scope.

## Anticipated artifacts

Parser + fixture tests

## Envelope notes

M held under SCA-005: scope narrowed to `LOOP_INIT.md` identity plus the historical workplan grammar; may fall to S on re-assessment

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
