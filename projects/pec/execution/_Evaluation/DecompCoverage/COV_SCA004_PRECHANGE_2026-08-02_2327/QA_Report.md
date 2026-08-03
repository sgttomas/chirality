# QA Report — COV_SCA004_PRECHANGE_2026-08-02

## Scan coverage

Heading-text binding resolved `Packages`, `Deliverables`, and `Scope Ledger`.
The run scanned `SOFTWARE_DECOMP.md`, four companion registers, 11 package
folders, 64 exact deliverable folders, 64 `_CONTEXT.md`, 64 `_STATUS.md`, 32
ScopeOfWork contracts, deliverable-local anticipated-artifact locations, both
current decomposition pointers, the complete active SCA-003 snapshot, and the
confirmed D-PEC-78/SCA-004 Gate 1 intake.

The PEC reliance-hold preflight returned `ALLOW` for consuming
`projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` for the SCA-004
Gate 2 pre-change audit.

## Parse and comparison results

- Audited decomposition SHA-256:
  `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787`.
- Decomposition pointer SHA-256:
  `8e63bbeeb1eca3ec14e494d17a2373f5d1b74a66ffb4534ad70d9dc8fc0b377f`.
- Companion register SHA-256: `Deliverables.csv`
  `b27ff4631f4966931990bbf9c033d2593d3dd8ac51b09e0d5112002b98afbc40`;
  `ScopeLedger.csv`
  `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5`.
- D-PEC-78 decision SHA-256:
  `3f91ea6a18360d950f3cecce755ee929cdc78c53651d0b2774a3c93aa290a565`.
- Confirmed Gate 1 intake return SHA-256:
  `071a0bfcde6a56fdf5634bf73f9b0c928c42627d6c5150251e42f20cfdf99f14`.
- 11/11 package folders and 64/64 deliverable folders found; no reverse-only
  folder.
- 64/64 contexts parsed and matched identity, package, type, responsible
  party, Context Envelope, canonical name, and current description.
- 94 ledger rows parsed: 71 `IN`, 14 `OUT`, 9 `TBD`; all `IN` package and
  deliverable references resolve.
- Objective support: OBJ-001 20, OBJ-002 12, OBJ-003 12, OBJ-004 10,
  OBJ-005 7, OBJ-006 9.
- Mapping residue: nine deliverables and 11 `IN` ledger rows, unchanged.
- Lifecycle: 28 `INITIALIZED`, 32 `OPEN`, 4 `CHECKING`.
- Contracts: 32 valid `SOW_V1`, 32 absent at `OPEN`, 0 invalid or ambiguous.
- Deliverable-local anticipated artifact sets: three present, 61 absent; the
  `DEL-08-02` absence is a warning because its lifecycle is `CHECKING`.
- Active SCA-003 snapshot: all 11 required artifacts present; both accepted
  pointers consistently name revision 1.3 / SCA-003.

## Limits

`AnticipatedArtifacts` contains prose classes rather than deterministic
filenames. Check 6 therefore uses conservative, deliverable-folder-local
matching. It found ADRs for `DEL-00-01`, the SPEC for `DEL-00-03`, and both
baseline documents for `DEL-10-01`. It did not treat source-tree artifacts as
deliverable-local matches.

This derivative audit validates structural coverage and active-snapshot
honesty. It does not judge artifact fitness, accept SCA-004 Gate 2, change any
governed state, authorize implementation, or replace the accepted
decomposition/SCA truth. Per the sealed brief, the audit `_LATEST.md` pointer
was intentionally not updated.
