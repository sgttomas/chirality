---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
wave_id: W1
phase: R2_DISCOVERY
deliverable_id: DEL-08-01
operation: VERIFY
production_format: SOW_V1
lifecycle_state: INITIALIZED
status_policy: NO_STATUS_TOUCH
source_commit: 404e47c16a88e7ffdc6d1fc5fac61ebb6864211e
result: REPAIR_CANDIDATES_FOUND
---

# DEL-08-01 claim discovery notes

## Scope and write boundary

Read-only semantic discovery was performed against:

`projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/ScopeOfWork.md`

No contract, `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, dependency,
decomposition, PRD, implementation, lifecycle, release, estimate, schedule,
or other run artifact was edited. The six `DEL-08-01_*` W1 files are the only
worker outputs.

## Frozen-source reproduction

| Surface | SHA-256 | Result |
|---|---|---|
| `ScopeOfWork.md` | `80b4ebe03f33ae69063bd3c2f4699a2cc4df447283cd10d8951b4e2ca33f013e` | reproduced |
| `_STATUS.md` | `a7e72ebf6c52876e2f59c9eedff3039c8e4b6f7e3d5779b591df11cba1449e5a` | reproduced; `INITIALIZED`; untouched |
| `projects/pec/docs/PRD.md` v2.2 | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` | matches `RUN_BASIS.md` |
| `SOFTWARE_DECOMP.md` revision 1.3 | `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787` | matches `RUN_BASIS.md` |
| `D-PEC-69` | `e6453ef467e71d7bb8548bf6fa36bb01affb73462cc9cdb54192585a520e4e0b` | matches `RUN_BASIS.md` |

The active reliance hold is unchanged. This worker performed only historical
read-only inspection, exact-correction preparation, and candidate validation;
it performed no reliance, production dispatch, promotion, consumption, or
hold release.

## Deterministic checks

- `validate_scope_of_work.py`: `valid=true`, format `SOW_V1`, zero issues.
- `derive_review_checklist.py`: seven items, covering `AC-001` through
  `AC-007` once each and binding contract SHA
  `80b4ebe03f33ae69063bd3c2f4699a2cc4df447283cd10d8951b4e2ca33f013e`.
- `check_boundary_owner_resolution.py`: status `OK`; this contract has no
  requirement in the tool's whole-requirement boundary-exclusion grammar and
  no per-act exclusion routed to manual owner QA.
- `scan_deliverable_consistency.py`: zero identity mismatches, zero missing
  core files, 11 marker hits, and one candidate unsourced-numeric hit. The
  marker hits are expected explicit `TBD-*` definitions or references. The
  numeric hit at `AC-001` is a false positive caused by the cited local ID
  `TBD-003`, not an unsourced engineering parameter.

## Claim census

The ledger contains exactly 41 bold local definitions:

| Class | Count |
|---|---:|
| `OUT` | 3 |
| `CLM` | 6 |
| `TBD` | 4 |
| `REQ` | 7 |
| `AC` | 7 |
| `CON` | 2 |
| `VER` | 5 |
| `AX` | 7 |

Disposition census:

- `DOCUMENTED_DIFFERENTLY`: 4
- `ALIGNED`: 37
- `AUTHORITY_CONFLICT`: 0
- `UNKNOWN`: 0
- `ACCEPTED_DIVERGENCE`: 0
- `STALE_INPUT`: 0

## Exact changed-claim candidate set

| Local ID | Defect | Minimal exact correction |
|---|---|---|
| `CLM-003` | Says `_STATUS.md` records `OPEN`; the authoritative state is `INITIALIZED`. | Correct the embedded state to `INITIALIZED`; retain the no-implementation statement and do not edit `_STATUS.md`. |
| `CLM-004` | Preserves the correct owner/harness/admin access-class set but uses superseded PRD §8 prose: it characterizes harness consumption without explicit enablement and says agents receive harness-injected orientation. | Preserve the access-class set. State that harnesses are permitted machine consumers only when explicitly enabled under their own authority and that agents may receive labeled, non-authoritative orientation only if an enabled consumer chooses optional injection; injection is not required. |
| `AX-004` | Says the deliverable is `OPEN`; the authoritative state is `INITIALIZED`. | Correct the embedded state to `INITIALIZED` while preserving lifecycle neutrality and no-status-touch. |
| `AX-006` | Calls decomposition revision 1.2 / SCA-002 at `3623b958b` the accepted basis. | Advance the accepted basis to revision 1.3 / SCA-003 under the frozen D-PEC-69 source commit; retain the explicit stale-derivative disclosure for `_REFERENCES.md`. |

All `OUT-*`, `REQ-*`, `AC-*`, `VER-*`, `CON-*`, and `TBD-*` definitions are
otherwise compatible with PRD v2.2 and decomposition revision 1.3. In
particular:

- the exact access-class set remains owner, harness, and admin;
- token presentation and refusal rules apply only when a request is made;
- the contract does not require any consumer to request, poll, contact,
  inject, subscribe, or conform;
- the Unix-socket default and the still-open loopback decision remain
  unchanged;
- the canonical downstream label “Poll-adoption measurement” is historical
  identity and must be preserved, not read as a receiving-loop polling duty.

## Non-definition production-contract corrections

A later whole-contract repair must also:

1. replace frontmatter
   `decomposition_basis: .../SOFTWARE_DECOMP.md@3623b958b` with the accepted
   revision-1.3/SCA-003 basis binding;
2. replace the opening paragraph's revision-1.2 `current_basis` assertion
   with revision 1.3 / SCA-003;
3. preserve the SCA-002 objective-attribution history while making clear that
   the current contract basis is revision 1.3; and
4. leave `_CONTEXT.md` and `_REFERENCES.md` untouched while accurately
   reporting their derivative staleness.

The PRD §8 quotation at source-chain item 3 remains exact current text for the
local-only/token-scoped access paragraph and needs no semantic change.

## Rulings and residuals

- `AUTHORITY_CONFLICT`: none.
- `UNKNOWN`: none.
- No dependency cycle, topology change, stable-ID change, scope addition, or
  lifecycle act is proposed.
- Correcting embedded lifecycle prose to the existing `INITIALIZED` authority
  is not a status transition.
