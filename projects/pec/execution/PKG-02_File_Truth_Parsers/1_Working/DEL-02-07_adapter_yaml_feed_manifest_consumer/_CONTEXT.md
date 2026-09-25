# _CONTEXT — DEL-02-07

| Field | Value |
|---|---|
| DeliverableID | DEL-02-07 |
| Canonical name | `adapter.yaml` feed-manifest consumer |
| PackageID | PKG-02 (File-Truth Parsers) |
| Type | BACKEND_FEATURE_SLICE |
| ContextEnvelope | S |
| PhaseHint | P1 |
| CoversScopeItems | SOW-017 |
| SupportsObjectives | OBJ-001;OBJ-002 |
| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |

## Description

Per-project `_harness/adapter.yaml` read as a parity-peer input only: PEC's declared census population is compared with the harness `status_glob`, and divergence is reported as a DriftFinding; no longer the feed manifest (per-loop feed profiles in the PEC-owned registry, DEL-01-06, declare the feeds). Name "`adapter.yaml` feed-manifest consumer" and path retained under SCA-005 (CP1-N); the label no longer describes the role.

## Anticipated artifacts

Manifest reader + fixture tests

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
