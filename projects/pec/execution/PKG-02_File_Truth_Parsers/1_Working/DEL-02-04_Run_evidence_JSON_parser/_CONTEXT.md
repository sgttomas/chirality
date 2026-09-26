# _CONTEXT — DEL-02-04

| Field | Value |
|---|---|
| DeliverableID | DEL-02-04 |
| Canonical name | Run-evidence JSON parser |
| PackageID | PKG-02 (File-Truth Parsers) |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | S |
| PhaseHint | P1 |
| CoversScopeItems | SOW-014 |
| SupportsObjectives | OBJ-001;OBJ-002 |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

`STATUS.json` / `RUNTIME_SUMMARY.json` under `execution/**` into RunRecord summaries, as a declared historical grammar for App/Piping and current-by-own-practice for PEC/Root; application-owned Runtime service user-data is operational, never an input. Name and path retained under SCA-005 (CP1-N); run-evidence JSON is no longer the primary RunRecord source.

## Anticipated artifacts

Parser + fixture tests

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
