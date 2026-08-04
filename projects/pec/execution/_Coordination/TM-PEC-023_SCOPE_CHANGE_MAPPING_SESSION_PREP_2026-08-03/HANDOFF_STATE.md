# Handoff state — TM-PEC-023 mapping-session preparation

## State

| Field | Value |
|---|---|
| Status | `PREPARED / AWAITING_DEDICATED_OWNER_SESSION` |
| PackageRole | non-authoritative coordination / pre-amendment decision support |
| AcceptedUpstreamSnapshot | `projects/pec/execution/_ScopeChange/SCA-004_2026-08-02_2325/` |
| DecompositionBasis | accepted PEC SOFTWARE_DECOMP revision 1.4 |
| DecompositionTruthChanged | `NO` |
| SCAOpened | `NO` |
| SCAAccepted | `NO` |
| NineSupportsObjectivesBytesPreserved | `YES` |
| TMPEC023State | `OPEN / ROUTED TO DEDICATED OWNER SESSION` |
| CoverageFindingsState | `COV-062..COV-070 OPEN` |
| DownstreamGate | `NONE` — nothing downstream is gated on this session |
| Urgency | `NONE` — session occurs at owner convenience |
| ReadyForAmendment | `NO` — nine owner selections and mechanics ruling required |
| NextOwner | human owner in a dedicated SCOPE_CHANGE mapping session |

## Prepared decision surface

`DECISION_SURFACE.md` provides exactly nine owner-only blocks. Each preserves
the current empty objective fields and offers one or more exact mapping token
sets plus an exact typed non-mapping alternative. Every mapping option is
classified as `DIRECT_ACCEPTED_LINK`, `INDIRECT_SUPERSESSION_CANDIDATE`, or
`NEW_OWNER_ATTRIBUTION`. Only DEL-05-01 / `OBJ-004` is presented as a direct
accepted link; all other mappings state that the future owner ruling would be
their authority. Stated ambiguity is retained rather than hidden.
`SCHEMA_MECHANICS_PROPOSAL.md` proposes lawful recording mechanics without a
new CSV column or non-objective sentinel in objective fields.

## Future outcome contract — owner authorized, not yet executed

After the dedicated session rules all nine rows and the recording mechanic:

1. SCOPE_CHANGE runs a five-gate `MODIFY` amendment against then-current
   accepted SOFTWARE decomposition truth.
2. Gate 3 shows the exact objective-field changes and/or typed disposition
   rows; Gate 4 names every propagation and validation act, including any
   audit/validator consumer changes needed to recognize typed dispositions.
3. Gate 5 applies only the ruled postimage, validates register/objective
   parity and typed-nonmapping uniqueness, writes a new immutable SCA
   snapshot, and updates pointers only where the protocol and owner act allow.
4. COV-062..COV-070 retire only against that accepted amendment/snapshot.
5. PROJECT_SETUP regenerates the nine deliverable-local mirrors only from the
   accepted successor handoff; no mirror is regenerated from this package.
6. TM-PEC-023 closes `RESOLVED_BY_DECISION` citing the accepted amendment.

## Current holds and exclusions

- The nine `SupportsObjectives` values and their corresponding ten
  `ScopeLedger.ObjectiveIDs` values remain byte-identical.
- TM-PEC-023 remains OPEN. The routed dedicated session is its carrier.
- COV-062..COV-070 remain open findings. This package does not characterize
  them as accepted residue. The owner's correction controls prospectively;
  the historical issue-log wording remains unchanged and is cited only as
  superseded rationale/evidence of the finding state.
- No schema change is authorized.
- DEL-01-06 RF-002 revision/REVIEW, push/PR, merge, and receipt recording are
  outside this bounded node. Their rulings are preserved verbatim in
  `OWNER_RULINGS_2026-08-03.md` only.
- No downstream act is blocked and no urgency is inferred.

## Rerun triggers

Rebuild or revalidate this preparation package before the owner session if
any of the following occurs:

- accepted decomposition revision, `ScopeLedger.csv`, `Deliverables.csv`, or
  §3 objective text changes;
- the TM-PEC-023 routed carrier or Task Management row changes;
- COV-062..COV-070 are changed, retired, renumbered, or superseded;
- the objective-field grammar or decomposition-register validator changes;
- the owner amends the mapping mandate or preselects a disposition; or
- another accepted SCA opens or lands before this mapping session.

At session start, scan the live `_ScopeChange/` state for the next amendment
ID; do not infer an ID from this package.

## Remaining decisions / blockers

The only blockers to an amendment are deliberate owner gates:

1. nine exact per-row mapping-or-typed-non-mapping selections;
2. one existing-schema recording mechanic for typed non-mapping rows;
3. the five SCOPE_CHANGE gate confirmations, including exact postimage and
   propagation plan; and
4. final Gate 5 acceptance after validation.

These are not blockers to unrelated downstream work.
