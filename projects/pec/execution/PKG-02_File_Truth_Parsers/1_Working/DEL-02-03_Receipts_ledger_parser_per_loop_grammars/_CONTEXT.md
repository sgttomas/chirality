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

Receipt parsing over two grammar generations of one Receipt feed kind: `LOOP_RECEIPTS.md` ledgers under per-loop grammar (live for PEC/Root/Runtime/Bridge; declared historical for App/Piping), including the receipt-contract-v2 marker where a ledger carries it, and central `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md`; prose-structured ledgers parsed best-effort with stated limits. Name and path retained under SCA-005 (CP1-N); the label "ledger parser (per-loop grammars)" no longer names the central-receipt grammar.

## Anticipated artifacts

Parser + per-loop grammar table + fixture tests

## Envelope notes

L because grammar varies: the receipt-contract-v2 family (App, Piping, PEC), the Root/Runtime/Bridge prose ledgers and the central `RECEIPT.md` grammar, with SOW-082 (OI-008) still open for the Root, Runtime and Bridge ledgers; single domain, but multiple grammars within one parser. Split line: the central-receipt grammar becomes its own deliverable if implementation demands a split

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
