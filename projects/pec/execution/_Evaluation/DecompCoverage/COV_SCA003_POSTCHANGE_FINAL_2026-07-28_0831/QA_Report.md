# QA Report — COV_SCA003_POSTCHANGE_FINAL

## Scan coverage

Heading-text binding resolved `Packages`, `Deliverables`, and `Scope Ledger`.
The final run scanned the current `SOFTWARE_DECOMP.md`, four companion
registers, 11 package folders, 64 exact deliverable folders, 64
`_CONTEXT.md`, 64 `_STATUS.md`, 32 ScopeOfWork contracts, both current
decomposition pointers, and the complete active SCA-003 snapshot.

## Parse and comparison results

- Current audited decomposition SHA-256:
  `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787`.
- Companion register SHA-256: `Deliverables.csv`
  `b27ff4631f4966931990bbf9c033d2593d3dd8ac51b09e0d5112002b98afbc40`;
  `ScopeLedger.csv`
  `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5`.
- 11/11 package folders and 64/64 deliverable folders found; no reverse-only
  folder.
- 64/64 contexts parsed and matched identity, package, type, Context Envelope,
  canonical name, and current description exactly.
- 94 ledger rows parsed: 71 `IN`, 14 `OUT`, 9 `TBD`; all `IN` package and
  deliverable references resolve.
- Objective support: OBJ-001 20, OBJ-002 12, OBJ-003 12, OBJ-004 10,
  OBJ-005 7, OBJ-006 9.
- Mapping residue: nine deliverables and 11 `IN` ledger rows, unchanged.
- Lifecycle: 32 `INITIALIZED`, 32 `OPEN`.
- Contracts: 32 valid `SOW_V1`, 32 absent at `OPEN`, 0 invalid or ambiguous.
- Active SCA-003 snapshot: 11/11 required artifacts present; both `_LATEST.md`
  pointers name revision 1.3 / SCA-003 consistently.

## Limits

`AnticipatedArtifacts` contains prose artifact classes rather than
deterministic filenames, so all are conservatively marked absent. Their
pre-production lifecycle states keep the 64 findings informational.

This derivative audit validates structural coverage and active snapshot
honesty. It does not refresh excluded ScopeOfWork or `_REFERENCES.md`
surfaces, release `PEC-HOLD-001`, change lifecycle or dependencies, authorize
implementation, or replace the accepted decomposition and SCA snapshot.
