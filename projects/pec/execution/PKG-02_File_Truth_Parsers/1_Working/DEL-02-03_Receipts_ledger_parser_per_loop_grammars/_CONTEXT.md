# _CONTEXT — DEL-02-03

| Field | Value |
|---|---|
| DeliverableID | DEL-02-03 |
| Canonical name | Receipts ledger parser (per-loop grammars) |
| PackageID | PKG-02 (File-Truth Parsers) |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | L |
| PhaseHint | P1 |
| CoversScopeItems | SOW-013 |
| SupportsObjectives | OBJ-001;OBJ-002 |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

`LOOP_RECEIPTS.md` parsing under per-loop grammar, including the D-APP-57 contract where adopted; prose-structured ledgers parsed best-effort with stated limits.

## Anticipated artifacts

Parser + per-loop grammar table + fixture tests

## Envelope notes

L because grammar varies per loop and SOW-082 (OI-008) keeps the contract-adoption surface open; single domain, but multiple grammars within one parser. Split further only if a loop's grammar proves adversarial

## Provenance

Scaffolded under `D-PEC-62` (2026-07-25) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (SCA-001
successor), superseded by revision 1.2 (`current_basis`, SCA-002
successor), in turn superseded by revision 1.3 (`current_basis`, SCA-003
successor), then by revision 1.4 (`current_basis`, SCA-004 successor).
Fields templated deterministically from
`Deliverables.csv`; this file restates register truth and is not an
independent authority.
