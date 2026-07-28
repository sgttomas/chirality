---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
wave_id: W1
deliverable_id: DEL-10-01
phase: R2_DISCOVERY
status: complete_read_only
source_commit: 404e47c16a88e7ffdc6d1fc5fac61ebb6864211e
---

# DEL-10-01 discovery notes

## Source identity and census

- Contract:
  `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-01_Step_0_cost_baseline_pre_P1/ScopeOfWork.md`.
- Contract SHA-256 before and after discovery:
  `f133318531206b6be7c1bbde391914ce967ca602348cb1df819cd0a684c327ff`.
- `_STATUS.md` SHA-256 before and after discovery:
  `9c091956a537699d79dd316c7fdbb6b9c197791c330765ed1346ba900fe564d7`.
- Production format: `SOW_V1`.
- Local-definition census: 50 definitions and 50 ledger rows:
  2 `OUT`, 12 `CLM`, 3 `TBD`, 1 `CON`, 12 `REQ`, 8 `AC`, 5 `VER`, and
  7 `AX`. Local IDs and claim-row IDs are each unique.
- Lifecycle authority: `_STATUS.md` says `INITIALIZED` (last updated
  2026-07-25). No measurement method, sample, or baseline exists.

## Concordance result

The contract is a whole-contract repair candidate. Four local definitions are
incompatible with the accepted PRD v2.2 / SOFTWARE_DECOMP revision 1.3 basis:

| Local ID | Finding | Minimal repair |
|---|---|---|
| `CLM-004` | Metric 1 remains correct, but the PRD §11 preamble is quoted as “measured in system behavior, not human behavior.” | Retain metric 1 and use the current §11 framing, “Success metrics (measured in observable system and use behavior).” Do not turn observable use into a receiving-loop duty or conformance criterion. |
| `CLM-007` | Quotes the obsolete “harness poll adoption” falsification clause. | Use the exact v2.2 clause: after Phase 3, negligible explicit consumer enablement or enabled-consumer orientation use plus owner dashboard non-use falsifies the thesis; non-adoption is evidence about PEC, never external nonconformance. Retain that DEL-10-01 supplies only metric 1’s before leg and does not evaluate falsification. |
| `AX-005` | Names revision 1.2 / SCA-002 as the accepted decomposition basis. | Re-pin to revision 1.3 / SCA-003 durable merge `11a494e9ae0cca795aa460deec19b9eac4d922a8`; preserve the revision-1.1 `_REFERENCES.md` statement as superseded provenance only. |
| `AX-007` | Says lifecycle `OPEN`; `_STATUS.md` says `INITIALIZED`. | Replace only the lifecycle label, retaining lifecycle neutrality and the no-method/no-sample/no-baseline meaning. |

The contract-level non-ID basis/lifecycle prose also requires mechanical
correction:

- frontmatter `decomposition_basis` from revision-1.2 commit `3623b958b` to
  the accepted revision-1.3/SCA-003 basis;
- the Basis-revision note from revision 1.2 to revision 1.3, while keeping the
  revision-1.1 reference pointer explicitly superseded;
- the Epistemology introduction from `_STATUS.md` state `OPEN` to
  `INITIALIZED`, with no implication that a method or baseline exists.

Those edits create no new scope and must not alter local IDs, objective
mappings, output/evaluation matrix structure, dependencies, lifecycle,
implementation, estimates, schedules, release semantics, or reliance state.

The remaining 42 local definitions are `ALIGNED`. Four intentionally open
definitions (`TBD-001..003`, `CON-001`) are `UNKNOWN`, not silently resolved.
No `AUTHORITY_CONFLICT` was found.

## Deterministic checks and semantic QA

- `validate_scope_of_work.py`: valid `SOW_V1`; zero issues.
- `derive_review_checklist.py`: 8 items, one for each `AC-001..008`, in source
  order and bound to the contract SHA.
- `check_boundary_owner_resolution.py`: `OK`; no whole-requirement or per-act
  boundary-exclusion grammar was detected, and there are zero unresolved or
  undefined owners. Semantic review confirms:
  - `REQ-007` preserves the practitioner-harness boundary in `CLM-008`;
  - `REQ-008` preserves behavior ownership in home packages through `CLM-009`;
  - `REQ-010` identifies only declared sequencing consumers and creates no
    consumption cadence, polling event, injection, or receiving-loop duty.
- `scan_deliverable_consistency.py`: no missing files, identity mismatch,
  format issue, or candidate unsourced numeric. Its 13 marker hits are
  deliberate claim IDs, cited `TBD` values, or ordinary-language detector
  matches; they do not create an additional repair.

## Stable-contract constraints

Preserve the `SOW_V1` heading order, all 50 local IDs and their ordering, the
two outputs, seven-row output/evaluation matrix, `SOW-058` mapping,
`OBJ-001;OBJ-006` mapping, `CON-001`, all three TBDs, and all unaffected
meaning. Preserve the pre-P1 sequencing obligation and the explicit distinction
between the token metric and the harness’s historical latency precondition.
The canonical file may be replaced only as one whole contract under the
approved R5 repair, with the semantic delta limited to the four local
definitions and the current-basis/lifecycle bookkeeping above.

`PEC-HOLD-001` remains active. This discovery prepared an exact correction
candidate only; it performed no reliance, production dispatch, promotion,
consumption, hold release, lifecycle act, or target-corpus edit.
