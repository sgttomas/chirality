# _CONTEXT — DEL-02-09

| Field | Value |
|---|---|
| DeliverableID | DEL-02-09 |
| Canonical name | MEMORY run-index parser |
| PackageID | PKG-02 (File-Truth Parsers) |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | S |
| PhaseHint | P1 |
| CoversScopeItems | SOW-096 |
| SupportsObjectives | OBJ-001;OBJ-002 |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

Parser for deliverable `MEMORY.md` run-index entries (run-ID tokens, dates, link targets) in the template `## Runs` table, the observed bullet form and the dated-heading form, as RunRecord join evidence; absence is a stated coverage limit; run descriptions are never extracted.

## Anticipated artifacts

Parser + fixture tests (table, bullet and dated-heading forms)

## Envelope notes

(none)

## Provenance

Scaffolded under `D-PEC-93` (2026-09-25) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.5 (`current_basis`,
SCA-005 successor; deliverable added by A-20). Fields templated
deterministically from `Deliverables.csv`; this file restates register truth
and is not an independent authority.
