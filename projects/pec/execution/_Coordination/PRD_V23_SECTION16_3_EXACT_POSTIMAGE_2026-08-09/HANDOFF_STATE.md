# Handoff state — D-PEC-79 exact bytes adopted, application withheld

## Closure and authority state

| Field | Value |
|---|---|
| Decision | `D-PEC-79` |
| Package | `projects/pec/execution/_Coordination/PRD_V23_SECTION16_3_EXACT_POSTIMAGE_2026-08-09/` |
| Owner ruling | `OWNER_RULING_2026-08-09.md`, SHA-256 `d1995cef187116913e675f2cf55e3bb75a0e469ec21ea03c8762927faf037c97` |
| ExactByteAdoptionState | `COMPLETE` |
| ApplicationAuthorizationState | `NOT_AUTHORIZED_IN_THIS_TRANCHE` |
| LiveApplicationState | `NOT_APPLIED` |
| LivePRDState | `UNCHANGED_V2_2` |
| LiveDecisionCarrierState | `NOT_MATERIALIZED` |
| LiveDecisionRegisterState | `UNCHANGED` |
| DecompositionTruthState | `UNCHANGED_REVISION_1_4` |
| GitCloseoutState | `NOT_AUTHORIZED` |
| ClosureVerdict | `CLOSED_FOR_EXACT_BYTE_PREPARATION_ONLY` |
| ReadyForNextOwner | `LATER_APPLICATION_TRANCHE_ONLY` |

## Adopted exact artifacts

| Artifact | Package role | SHA-256 | State |
|---|---|---|---|
| `PRD_V2_3_CANDIDATE_POSTIMAGE.md` | Adopted candidate postimage; not live product authority until application | `92627ee1d384dd8ef0f2db5d63362ec54eee9da30794b9c2d776bd46fb20f5b0` | `EXACT_BYTES_ADOPTED / NOT_APPLIED` |
| `D-PEC-79_prd_v2_3_section16_3_concordance.md` | Adopted product-amendment carrier; not materialized in live `_DECISIONS` | `bc3a4bd59d4542e3d686c4663cc5b5b4fc59f4f3abc6bc4a40ea65063716b5d2` | `EXACT_BYTES_ADOPTED / NOT_APPLIED` |
| `OWNER_RULING_2026-08-09.md` | Coordination ruling evidence | `d1995cef187116913e675f2cf55e3bb75a0e469ec21ea03c8762927faf037c97` | `CURRENT` |

The exact adopted postimage and carrier are immutable inputs to a later
application tranche. They must not be regenerated, normalized, or amended in
place. Any different byte requires a successor candidate and another exact
owner gate.

## Live state observed at handoff

| Live surface | SHA-256 | State |
|---|---|---|
| `projects/pec/docs/PRD.md` | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` | v2.2; unchanged; §16.3 still textually open |
| `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` | `8eb80613b711508b77590d0fbfd2ad4139205603a6a6f86c2f8dc9525b672afc` | unchanged by this tranche; no D-PEC-79 row added |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-79_prd_v2_3_section16_3_concordance.md` | n/a | absent; live carrier not materialized |

D-PEC-78, SCA-004, accepted SOFTWARE_DECOMP revision 1.4, and their pointers
remain the current accepted authority chain for the settled loop-registry
meaning. The live PRD mismatch remains visible until a later application
tranche is separately authorized and completes.

## Later exact application fence

The next owner may authorize only the exact fence adopted in the carrier:

1. `projects/pec/docs/PRD.md`
   - replace live preimage SHA-256
     `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`
     with adopted postimage SHA-256
     `92627ee1d384dd8ef0f2db5d63362ec54eee9da30794b9c2d776bd46fb20f5b0`;
2. `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-79_prd_v2_3_section16_3_concordance.md`
   - materialize the adopted carrier byte-for-byte at SHA-256
     `bc3a4bd59d4542e3d686c4663cc5b5b4fc59f4f3abc6bc4a40ea65063716b5d2`;
3. `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
   - add only the D-PEC-79 row recording the ruling, the two adopted hashes,
     and ruled status.

No current instruction in this package authorizes that application. The
later application owner must provide or hold separate application authority,
re-run the PEC reliance-hold preflight, and fail closed if the live PRD
preimage or either adopted artifact hash differs.

## Later application verification

Before any live write, the later tranche must:

1. reproduce all three hashes in the adopted-artifact table;
2. reproduce the live PRD preimage hash;
3. confirm the live D-PEC-79 decision path remains absent and the register has
   no D-PEC-79 row, or stop for reconciliation;
4. verify the exact changed-path set is limited to the three-path fence;
5. apply the adopted postimage and carrier byte-for-byte without semantic
   rewriting;
6. verify D-PEC-78, SCA-004, decomposition revision 1.4, and all excluded
   surfaces remain unchanged;
7. run targeted §16 parity checks, `git diff --check`, and applicable PEC
   governance/path checks; and
8. return Git closeout separately to CHANGE.

## Rollback boundary

- This preparation tranche made no live application and therefore requires
  no live rollback.
- A later pre-publication application rollback restores the live PRD and
  register to their exact pre-application blobs and removes only the newly
  materialized live D-PEC-79 carrier.
- A post-publication rollback requires a separately approved revert or
  successor product decision. D-PEC-78, the ruling record, adopted candidate
  identities, and SCA-004 are never silently rewritten.

## Non-effects and remaining blocker

This handoff does not alter or authorize alteration of the live PRD, live
decision carrier/register, standing plan, receipt, status, SCA, decomposition,
source, configuration, lifecycle, dependencies, estimates, schedules,
artifacts, reviews, Task Management, releases, reliance state, or foreign-loop
surfaces. It authorizes no implementation, professional reliance, staging,
commit, push, merge, pull request, or publication.

The only remaining blocker is separate authority for the later exact
application tranche. Until that authority is supplied and the exact fence is
successfully validated/applied, the adopted bytes remain coordination-only
and the live PRD remains v2.2.
