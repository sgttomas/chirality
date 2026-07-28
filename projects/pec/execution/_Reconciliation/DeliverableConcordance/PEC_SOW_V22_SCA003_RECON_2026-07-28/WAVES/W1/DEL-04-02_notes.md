---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
wave_id: W1
deliverable_id: DEL-04-02
phase: R2_DISCOVERY
status: complete_read_only
source_commit: 404e47c16a88e7ffdc6d1fc5fac61ebb6864211e
---

# DEL-04-02 discovery notes

## Source identity and census

- Contract:
  `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/ScopeOfWork.md`.
- Contract SHA-256 before and after discovery:
  `a7dcc4d45c01194138191ad2eb996aefdf0f0b5a6782192a5f0110f09dd06d86`.
- `_STATUS.md` SHA-256 before and after discovery:
  `e11421d3eabcf50e240ef11e0af1f998a0de213ea3da5128e09f20feff5754d7`.
- Production format: `SOW_V1`.
- Local-definition census: 87 definitions and 87 ledger rows:
  2 `OUT`, 17 `CLM`, 4 `TBD`, 15 `REQ`, 16 `AC`, 5 `CON`, 15 `VER`,
  and 13 `AX`. Local IDs and claim-row IDs are each unique.
- Lifecycle authority: `_STATUS.md` says `INITIALIZED` (last updated
  2026-07-25). No implementation exists.

## Concordance result

The contract is a whole-contract repair candidate. Four local definitions are
incompatible with the accepted PRD v2.2 / SOFTWARE_DECOMP revision 1.3
consumer-interface or lifecycle basis:

| Local ID | Finding | Minimal repair |
|---|---|---|
| `CLM-016` | Quotes the superseded PEC-K-03 harness-polling/injection rule, uses the pre-v2.2 modes-table headings/postures, infers a harness-polling caller population, and assigns mode-proportional polling to the harness. | Replace that passage with the exact pull-oriented, consumer-owned posture: PEC serves labeled non-authoritative data only on request; an explicitly enabled consumer chooses whether/when to consume, its mode mapping and cadence, and any optional injection; no session-start or transition duty; zero-contact modes remain available. |
| `CLM-017` | Says lifecycle `OPEN`; `_STATUS.md` says `INITIALIZED`. | Replace only the lifecycle label, retaining the no-implementation and future-contract meaning. |
| `REQ-013` | Its request-only and no-initiation prohibitions align, but its final sentence assigns superseded polling moments and mode-proportional contact to the harness. | Retain the prohibitions; state that an explicitly enabled consumer owns whether/when to request, mode mapping/contact cadence and optional injection, while PEC imposes no polling event. |
| `AX-013` | Says lifecycle `OPEN`; `_STATUS.md` says `INITIALIZED`. | Replace only the lifecycle label; do not change lifecycle state. |

The contract-level basis also requires a non-ID mechanical re-pin:

- frontmatter `decomposition_basis` from revision-1.2 commit `3623b958b` to
  the accepted revision-1.3/SCA-003 durable merge
  `11a494e9ae0cca795aa460deec19b9eac4d922a8`;
- the opening accepted-basis paragraph from revision 1.2 / SCA-002 successor
  to revision 1.3 / SCA-003 successor;
- current-state descriptions of the two objective rows should say revision
  1.3, while preserving the accurate fact that the mappings pre-date and were
  unchanged by SCA-002 and SCA-003;
- quotation-record inventory must track the corrected current §5 row text.

Those basis edits create no new scope and must not alter local IDs, objective
mappings, output/evaluation matrix structure, dependencies, lifecycle,
implementation, estimates, schedules, release semantics, or reliance state.

The remaining 74 local definitions are `ALIGNED`. Nine intentionally open
definitions (`TBD-001..004`, `CON-001..005`) are `UNKNOWN`, not silently
resolved. No `AUTHORITY_CONFLICT` was found.

## Deterministic checks and semantic QA

- `validate_scope_of_work.py`: valid `SOW_V1`; zero issues.
- `derive_review_checklist.py`: 16 items, one for each `AC-001..016`, in
  source order and bound to the contract SHA.
- `check_boundary_owner_resolution.py`: `OK`; one whole-requirement boundary
  checked; zero unresolved or undefined owners. Four per-act clauses are
  `NOT_CHECKABLE` and were resolved semantically:
  - `REQ-006` limitation rendering → `DEL-04-05` in `CLM-015`;
  - `REQ-007` response stamping/citation attachment → `DEL-04-03` in
    `CLM-007` and `CLM-015`;
  - `REQ-008` record-tier type ownership → `DEL-01-01` in `CLM-011` and
    `CLM-015`;
  - `REQ-010` SSE subscription → `DEL-08-05` in `CLM-012` and `CLM-015`;
    transport/rendering remain package-owned by `PKG-08`/`PKG-09` under
    `CLM-006`.
- `scan_deliverable_consistency.py`: no missing files, identity mismatch,
  format issue, or candidate unsourced numeric. Its 16 marker hits are
  deliberate claim IDs, cited `TBD` values, quotations, or ordinary-language
  detector matches; they do not create an additional repair.

## Stable-contract constraints

Preserve the `SOW_V1` heading order, all 87 local IDs and their ordering, the
two outputs, 16-row output/evaluation matrix, `SOW-005` mapping,
`OBJ-001;OBJ-002` mapping, all five explicit conflicts, all four TBDs, and all
unaffected meaning. The canonical file may be replaced only as one whole
contract under the approved R5 repair, with the semantic delta limited to the
four local definitions and the current-basis/quotation bookkeeping above.

`PEC-HOLD-001` remains active. This discovery prepared an exact correction
candidate only; it performed no reliance, production dispatch, promotion,
consumption, hold release, lifecycle act, or target-corpus edit.
