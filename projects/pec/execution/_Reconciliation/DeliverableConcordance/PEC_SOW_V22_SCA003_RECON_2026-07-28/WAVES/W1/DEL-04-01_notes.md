---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
wave_id: W1
phase: R2_DISCOVERY
deliverable_id: DEL-04-01
operation: VERIFY
production_format: SOW_V1
lifecycle_state: INITIALIZED
status_policy: NO_STATUS_TOUCH
source_commit: 404e47c16a88e7ffdc6d1fc5fac61ebb6864211e
result: REPAIR_CANDIDATES_FOUND
---

# DEL-04-01 claim discovery notes

## Scope and write boundary

Read-only semantic discovery was performed against:

`projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md`

No production contract, `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`,
dependency, decomposition, PRD, implementation, lifecycle, release, estimate,
or schedule surface was edited. The six `DEL-04-01_*` W1 artifacts are the
only worker outputs.

## Frozen-source reproduction

| Surface | SHA-256 | Result |
|---|---|---|
| `ScopeOfWork.md` | `dc667f992c25ed037b195400167319d120a1e5e0118ce777a29f5a64186d0feb` | reproduced |
| `_STATUS.md` | `7c9902184deeb30b80728979fd76c710a23396ba549c144bc713134e51a94dd1` | reproduced; `INITIALIZED`; untouched |
| `projects/pec/docs/PRD.md` v2.2 | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` | matches `RUN_BASIS.md` |
| `SOFTWARE_DECOMP.md` revision 1.3 | `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787` | matches `RUN_BASIS.md` |
| `D-PEC-67` | `c04f8ddd90cfe4ca3ecdabad8f48b4820c9952c9c4515655dc8ed21304d9d9a8` | read |
| `D-PEC-68` | `b6511118fa51275a3a2441e3d9baff037fa13ccd0abd34f8ae8ab11a836a7fdb` | read |
| `D-PEC-69` | `e6453ef467e71d7bb8548bf6fa36bb01affb73462cc9cdb54192585a520e4e0b` | matches `RUN_BASIS.md` |
| SCA-003 `RUN_SUMMARY.md` | `ce5682d6bed177c489452e884046b249431f975dcd4b35623a8d4515c9d6a2b8` | read |
| `ACTIVE_RELIANCE_HOLDS.csv` | `d92d134bdfe4466dc06292fa53fa44cf368d6be1dfeb04fefa6ce188bba8002a` | matches `RUN_BASIS.md`; hold unchanged |

The run-level hold preflight records `ALLOW` for historical read-only
inspection, exact-correction preparation, and candidate validation. No
production reliance, dispatch, promotion, consumption, or hold release was
performed.

## Deterministic checks

- `validate_scope_of_work.py`: `valid=true`, format `SOW_V1`, zero issues.
- `derive_review_checklist.py`: 16 items, covering `AC-001` through `AC-016`
  once each and binding contract SHA
  `dc667f992c25ed037b195400167319d120a1e5e0118ce777a29f5a64186d0feb`.
- `scan_deliverable_consistency.py`: zero identity mismatches, zero missing
  core files, zero unsourced numeric candidates, and 12 marker hits. The
  marker hits are expected references to explicit `TBD-*` definitions or
  marker words; none is a newly inferred defect.
- `check_boundary_owner_resolution.py`: status `OK`; one whole-requirement
  exclusion checked; three per-act exclusions routed to semantic QA; no
  unresolved deterministic owner and no undefined claim.

### Manual boundary-owner QA

- `REQ-005`: citation attachment, response stamping, generation-time
  stamping, per-feed-freshness stamping, and freshness computation resolve to
  `DEL-04-03` through `CLM-011`, `CLM-015`, and `CON-003`.
- `REQ-006`: limitation rendering resolves to `DEL-04-05` through `CLM-012`
  and `CLM-015`.
- `REQ-003`: record-tier entity/schema definition resolves to `DEL-01-01`
  through `CLM-011`; the reconcile path resolves to `DEL-03-01` through
  `CLM-012`. The excluded feed-grammar-definition act has no owner named by a
  claim that `REQ-003` cites. The claim ledger therefore records `REQ-003` as
  `UNKNOWN`, with no repair inferred inside this reconciliation window.

## Claim census

The ledger contains exactly 87 bold local definitions:

| Class | Count |
|---|---:|
| `OUT` | 2 |
| `CLM` | 18 |
| `TBD` | 4 |
| `REQ` | 15 |
| `AC` | 16 |
| `CON` | 4 |
| `VER` | 15 |
| `AX` | 13 |

Disposition census:

- `DOCUMENTED_DIFFERENTLY`: 6
- `UNKNOWN`: 1
- `ALIGNED`: 80
- `AUTHORITY_CONFLICT`: 0
- `ACCEPTED_DIVERGENCE`: 0
- `STALE_INPUT`: 0

## Exact changed-claim candidate set

| Local ID | Defect | Minimal exact correction |
|---|---|---|
| `CLM-016` | Quotes superseded PEC-K-03/-11 text that assigns polling moments and injection to harnesses and assigns cadence through the old modes ladder. | Preserve “composes on request and initiates nothing”; replace the obsolete quotations and allocation with consumer-owned use, mode mapping, cadence, and optional injection. State that PEC declares no polling moment or receiving-loop duty. |
| `REQ-010` | Its no-initiation requirement is correct, but its final clause assigns polling moments and mode-proportional contact to “the harness.” | Preserve call-only/no-timer/no-push/no-session-initiation behavior; replace only the ownership rationale with neutral on-request behavior and separately authorized, consumer-owned use/cadence/injection. |
| `AX-007` | Categorically states that harnesses poll at moments of consequence and inject the result. | Replace with PEC-K-03/-11 as adopted: PEC serves labeled non-authoritative orientation on request; an explicitly enabled consumer decides whether and when to consume and whether to inject; zero contact remains valid. |
| `AX-012` | Treats OI-011 as resolved to a conditional session-start polling moment. Revision 1.3 records that interpretation as superseded. | State that PEC declares no polling moment; session start or mode transition is a contact point only if a consumer owner separately adopts it. |
| `CLM-018` | Says the deliverable is `OPEN`; `_STATUS.md` is `INITIALIZED`. | Correct the embedded description to `INITIALIZED`; do not edit `_STATUS.md`. |
| `AX-013` | Says the deliverable is `OPEN`; `_STATUS.md` is `INITIALIZED`. | Correct the embedded description to `INITIALIZED`; do not edit `_STATUS.md`. |

`AC-010` and `VER-010` are already neutral and aligned: they verify only that
composition is call-triggered and that this deliverable originates no timer,
scheduler, subscription, push, session-lifecycle act, polling logic, or
cadence logic. They do not assign a polling duty, contact point, or injection
act to any consumer and should remain semantically unchanged.

## Non-definition production-contract corrections

These are not additional claim-ledger rows, but a whole-contract repair must
also update the stale accepted-basis prose:

1. Frontmatter `decomposition_basis` remains pinned to
   `SOFTWARE_DECOMP.md@3623b958b`.
2. The opening basis paragraph still calls revision 1.2 `current_basis`.
3. Any retained revision-1.2 objective-mapping history must be explicitly
   historical while the contract cites revision 1.3 / SCA-003 as its current
   basis.
4. The paragraph may continue to report that `_REFERENCES.md` and this
   deliverable's `_CONTEXT.md` are stale derivative metadata; this run does not
   authorize either file to change.

The repair must preserve all 87 local IDs, heading order, objective mappings,
matrix structure, output count, dependency semantics, and unaffected meaning.

## Rulings and residuals

- `AUTHORITY_CONFLICT`: none.
- `UNKNOWN`: `REQ-003` lacks a cited owner for the excluded
  feed-grammar-definition act. Do not infer one or widen the v2.2/SCA-003
  repair.
- No dependency cycle or ordering issue was introduced or resolved.
- No lifecycle act is requested: correcting embedded prose to the already
  authoritative `INITIALIZED` state is not a status transition.
