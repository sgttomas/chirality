---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
wave_id: W1
deliverable_id: DEL-04-03
phase: R2_DISCOVERY
status: complete_read_only
source_commit: 404e47c16a88e7ffdc6d1fc5fac61ebb6864211e
population_basis: D-PEC-69 execution-time semantic scan
---

# DEL-04-03 discovery notes

## Source identity and census

- Contract:
  `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/ScopeOfWork.md`.
- Contract SHA-256 before and after discovery:
  `9d0d95bcd027aaa5d6cefbdc31dcc52e5f3dad8e6edc81bdf047921392e4d96f`.
- `_STATUS.md` SHA-256 before and after discovery:
  `08c9a093a7a412af8e7c8d4c9dc4e610533267ae2c55b4585ee7d1f8822b73ed`.
- Production format: `SOW_V1`.
- Local-definition census: 82 definitions and 82 ledger rows:
  2 `OUT`, 17 `CLM`, 4 `TBD`, 15 `REQ`, 15 `AC`, 4 `CON`, 14 `VER`,
  and 11 `AX`. Local IDs and claim-row IDs are each unique.
- Lifecycle authority: `_STATUS.md` says `INITIALIZED` (last updated
  2026-07-25). No implementation exists.

## Execution-scan adjudication

DEL-04-03 is an execution-time-confirmed whole-contract repair candidate,
expanding the expected ten-member population exactly as D-PEC-69 permits.

`CLM-016` is a true semantic defect, not an accepted canonical-label
divergence. SCA-003 deliberately retains DEL-10-12’s canonical label and path
as “Poll-adoption measurement”, but replaces its meaning with
candidate-consumer enablement and enabled-consumer orientation use against
contact opportunities defined by each consumer’s own adopted mode/cadence
rules, with no receiving-loop conformance criterion. The contract does not
quote the canonical label; it asserts “harness poll-adoption measurement”.
That phrase assigns the superseded behavior and must be corrected.

The generic prohibitions against performing “adoption measurement” in
`REQ-010`, `AC-010`, and `VER-010` remain aligned: they identify an adjacent
act without restating the retired behavior and correctly keep all adoption
measurement outside DEL-04-03.

## Exact repair set

| Local ID | Finding | Minimal repair |
|---|---|---|
| `CLM-016` | Names DEL-10-12’s act as “harness poll-adoption measurement”. | Retain DEL-10-12 as owner and retain its canonical “Poll-adoption measurement” label, but describe SOW-060’s current behavior: candidate enablement plus enabled-consumer orientation use against consumer-owned opportunity definitions; no receiving-loop conformance criterion. |
| `CLM-017` | Says lifecycle `OPEN`; `_STATUS.md` says `INITIALIZED`. | Replace only the lifecycle label, retaining the no-implementation and future-contract meaning. |
| `AX-011` | Says lifecycle `OPEN`; `_STATUS.md` says `INITIALIZED`. | Replace only the lifecycle label, retaining lifecycle neutrality and no-implementation meaning. |

The contract-level non-ID basis also requires a mechanical re-pin:

- frontmatter `decomposition_basis` from revision-1.2 commit `3623b958b` to
  the accepted revision-1.3/SCA-003 durable merge
  `11a494e9ae0cca795aa460deec19b9eac4d922a8`;
- the opening accepted-basis paragraph from revision 1.2 / SCA-002 successor
  to revision 1.3 / SCA-003 successor, while preserving the accurate
  historical SCA-002 mapping evidence and the superseded revision-1.1
  `_REFERENCES.md` pointer statement.

Those edits create no new scope and must not alter local IDs, item-level
objective mappings, output/evaluation matrix structure, dependencies,
lifecycle, implementation, estimates, schedules, release semantics, or
reliance state.

The remaining 71 local definitions are `ALIGNED`. Eight intentionally open
definitions (`TBD-001..004`, `CON-001..004`) are `UNKNOWN`, not silently
resolved. No `AUTHORITY_CONFLICT` was found.

## Deterministic checks and semantic QA

- `validate_scope_of_work.py`: valid `SOW_V1`; zero issues.
- `derive_review_checklist.py`: 15 items, one for each `AC-001..015`, in
  source order and bound to the contract SHA.
- `check_boundary_owner_resolution.py`: `OK`; one whole-requirement boundary
  checked; zero unresolved or undefined owners. Two per-act clauses are
  `NOT_CHECKABLE` and were resolved semantically:
  - `REQ-006` presence-store guard limb → `DEL-06-05` in `CLM-014` and
    `CLM-016`;
  - `REQ-008` measurement-limitation rendering → `DEL-04-05` in `CLM-016`.
- `scan_deliverable_consistency.py`: no missing files, identity mismatch,
  format issue, or candidate unsourced numeric. Its 12 marker hits are
  deliberate claim IDs, cited `TBD` values, or ordinary-language detector
  matches; they do not create an additional repair.

## Stable-contract constraints

Preserve the `SOW_V1` heading order, all 82 local IDs and their ordering, the
two outputs, 15-row output/evaluation matrix, `SOW-006;SOW-007` coverage,
item-level objective distinction (`SOW-006` → `OBJ-001;OBJ-002`,
`SOW-007` → `OBJ-001`), all four conflicts, all four TBDs, and all unaffected
meaning. Preserve DEL-10-12’s canonical label and path while correcting only
the behavior description. The canonical file may be replaced only as one
whole contract under the approved R5 repair, with the semantic delta limited
to the three local definitions and basis bookkeeping above.

`PEC-HOLD-001` remains active. This discovery prepared an exact correction
candidate only; it performed no reliance, production dispatch, promotion,
consumption, hold release, lifecycle act, or target-corpus edit.
