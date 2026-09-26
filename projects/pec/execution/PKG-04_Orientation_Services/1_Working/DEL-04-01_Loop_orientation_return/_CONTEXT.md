# _CONTEXT — DEL-04-01

| Field | Value |
|---|---|
| DeliverableID | DEL-04-01 |
| Canonical name | Loop orientation return |
| PackageID | PKG-04 (Orientation Services) |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | M |
| PhaseHint | P1 |
| CoversScopeItems | SOW-004 |
| SupportsObjectives | OBJ-001 |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

Per-loop orientation: newest applicable receipt over central receipts and ledgers, examined-through SHA, gate states from decisions, scope-change state and graph BLOCKED nodes, owner directions of record, open tranches/candidate briefs and parked lanes over graph READY/ACTIVE/BLOCKED nodes, each parked lane with its unparking act; terminal completion derived from local Git merge reachability of cited PRs, Explain-cited and advisory.

## Anticipated artifacts

Orientation builder + tests

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
