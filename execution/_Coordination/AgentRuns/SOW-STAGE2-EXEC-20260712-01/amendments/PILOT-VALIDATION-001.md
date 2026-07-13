# Pilot Validation Amendment 001

Status: `ACTIVE — CROSS-LANE BRIEF CORRECTION`

## Trigger

WORKING-P-P proved before child dispatch that every exact Stage-1 pilot blob
contains the historical provenance marker
`<!-- pilot-variance: D-GOV-15@58aa81d62f4a32e3c2d687e4356a1e4be8141674 -->`
and no D-GOV-16 migration-authority marker. Current consumer activation
correctly requires an exact embedded
`D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176` marker before an
isolated `MIGRATION_DUAL` directory may resolve. Supplying the ruled authority
while preserving the exact Stage-1 blob therefore returns AMBIGUOUS; inserting
the marker would change the candidate hash and violate the accepted pilot
extraction rule. WORKING-P-A confirmed the same marker posture for all six App
candidates. No child was dispatched before disposition.

## Disposition

The parent briefs over-specified transient dual validation. The accepted
Stage-2 plan requires exact Stage-1 candidate extraction, validation on the
current basis, and atomic integration that leaves `SOW_V1`; it prohibits
regeneration, candidate mutation, merging a dual-format branch, or accepting a
dual-format commit. C2F already proved the exact D-GOV-16 isolated-dual
consumer contract independently.

For all ten pilot verifier children, replace the contradictory dual-state
criterion with these exact state checks:

1. validate the current P3-bound legacy kit, with no SOW present, as valid
   `LEGACY_FOUR_DOC`;
2. validate the byte-exact extracted candidate, in a SOW-only temporary target
   with no legacy production files, as valid `SOW_V1`;
3. run mapping, parity, checklist, repeated rendering, source/status hashing,
   provenance, grounding, and containment checks against the unchanged legacy
   sources and exact candidate;
4. prove the future atomic five-path replacement manifest changes only `A
   ScopeOfWork.md` and deletes the four legacy production files, leaving every
   control/status/lifecycle byte unchanged; and
5. fail if either state is invalid, the candidate differs from the Stage-1
   blob, any semantic/mapping/parity/checklist result fails, or any child
   manufactures a modified candidate.

Children must not add a D-GOV-16 marker to the Stage-1 blob, invoke conversion,
or treat the D-GOV-15 provenance marker as Stage-2 migration authority. No
synthetic dual overlay is required for pilot acceptance.

This versioned correction restores the accepted exact-candidate and atomic
single-format criteria; it does not change D-GOV-16, objective, scope, risk,
ownership, lifecycle meaning, integration authority, H1/H2 posture, or the
human-approved acceptance gate. Managers must version their package graph and
all child briefs before dispatch and cite this amendment in terminal evidence.
