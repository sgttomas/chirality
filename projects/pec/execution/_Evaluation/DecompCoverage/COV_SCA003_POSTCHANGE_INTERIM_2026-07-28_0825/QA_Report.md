# QA Report — COV_SCA003_POSTCHANGE_INTERIM

## Scan coverage

Heading-text binding resolved `Packages`, `Deliverables`, and `Scope Ledger`.
The run scanned `SOFTWARE_DECOMP.md`, four companion registers, 11 package
folders, 64 exact deliverable folders, 64 `_CONTEXT.md`, 64 `_STATUS.md`, 32
ScopeOfWork contracts, and the active ScopeChange pointer/snapshot.

## Parse and comparison results

- 11/11 package folders and 64/64 deliverable folders found; no reverse-only
  folder.
- 64/64 contexts parsed and matched identity, package, type, Context Envelope,
  canonical name, and current description exactly.
- 94 ledger rows parsed: 71 `IN`, 14 `OUT`, 9 `TBD`; all `IN` package and
  deliverable references resolve.
- Objective support counts: OBJ-001 20, OBJ-002 12, OBJ-003 12, OBJ-004 10,
  OBJ-005 7, OBJ-006 9.
- Mapping residue remains 9 deliverables and 11 `IN` ledger rows, matching the
  accepted revision-1.2 mapping state and unaffected by SCA-003.
- Lifecycle census: 32 `INITIALIZED`, 32 `OPEN`.
- Contract census: 32 valid `SOW_V1`, 32 absent at `OPEN`, 0 invalid or
  ambiguous dual-format states.
- Current input hashes: `SOFTWARE_DECOMP.md`
  `cc9ccc97aed6d94790aab08252feb891c1393159c267d12ccbbfa192198171fe`;
  `Deliverables.csv`
  `b27ff4631f4966931990bbf9c033d2593d3dd8ac51b09e0d5112002b98afbc40`;
  `ScopeLedger.csv`
  `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5`.

## Limits

`AnticipatedArtifacts` contains prose artifact classes, not deterministic
filenames. They are conservatively marked absent, and because every lifecycle
state precedes `IN_PROGRESS`, all 64 findings remain informational.

This audit validates decomposition-to-filesystem coverage. It does not
semantically approve SCA-003, refresh excluded ScopeOfWork contracts or
`_REFERENCES.md`, update `_Decomposition/_LATEST.md`, or anticipate the
not-yet-created SCA-003 snapshot. A final post-snapshot audit is required to
validate the future SCA-003 active-snapshot contract.
