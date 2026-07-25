# _CONTEXT — DEL-05-01

| Field | Value |
|---|---|
| DeliverableID | DEL-05-01 |
| Canonical name | Gate precondition evaluators (Explain-shaped) |
| PackageID | PKG-05 (Gate Evaluation & Decision Slate) |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |
| PhaseHint | P2 |
| CoversScopeItems | SOW-022;SOW-023 |
| SupportsObjectives | (none mapped — see §3 mapping notes) |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

Deterministic evaluation of file/Git-reducible gate preconditions (ruling presence, SHA reachability, receipt ancestry, snapshot presence, register-row status) with Explain-shaped advisory verdicts.

## Anticipated artifacts

Evaluators + Explain types + tests

## Envelope notes

(none)

## Provenance

Scaffolded under `D-PEC-62` (2026-07-25) from accepted decomposition
`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.1 (SCA-001
successor), superseded by revision 1.2 (`current_basis`, SCA-002
successor). Fields templated deterministically from
`Deliverables.csv`; this file restates register truth and is not an
independent authority.
