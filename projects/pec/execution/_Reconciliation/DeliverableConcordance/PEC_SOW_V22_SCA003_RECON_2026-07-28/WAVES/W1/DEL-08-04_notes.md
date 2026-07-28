---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
wave_id: W1
phase: R2_DISCOVERY
deliverable_id: DEL-08-04
operation: VERIFY
production_format: SOW_V1
lifecycle_state: INITIALIZED
status_policy: NO_STATUS_TOUCH
source_commit: 404e47c16a88e7ffdc6d1fc5fac61ebb6864211e
result: REPAIR_CANDIDATES_FOUND
---

# DEL-08-04 claim discovery notes

## Scope and write boundary

Read-only semantic discovery was performed against:

`projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/ScopeOfWork.md`

No contract, `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, dependency,
decomposition, PRD, implementation, lifecycle, release, estimate, schedule,
or other run artifact was edited. The six `DEL-08-04_*` W1 files are the only
worker outputs.

## Frozen-source reproduction

| Surface | SHA-256 | Result |
|---|---|---|
| `ScopeOfWork.md` | `ef40833af6112f179d9021f036e37d78af486b9d39a19cb5d994bf693e5c3f23` | reproduced |
| `_STATUS.md` | `f33ac4a98d0650deb5e6815eb7d201a55f79750ab76bde6f7b3edf9573f1d4a4` | reproduced; `INITIALIZED`; untouched |
| `projects/pec/docs/PRD.md` v2.2 | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` | matches `RUN_BASIS.md` |
| `SOFTWARE_DECOMP.md` revision 1.3 | `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787` | matches `RUN_BASIS.md` |
| `D-PEC-69` | `e6453ef467e71d7bb8548bf6fa36bb01affb73462cc9cdb54192585a520e4e0b` | matches `RUN_BASIS.md` |

The active reliance hold remains unchanged. This worker performed only
historical read-only inspection, exact-correction preparation, and candidate
validation; it performed no reliance, production dispatch, promotion,
consumption, or hold release.

## Deterministic checks

- `validate_scope_of_work.py`: `valid=true`, format `SOW_V1`, zero issues.
- `derive_review_checklist.py`: 16 items, covering `AC-001` through `AC-016`
  once each and binding contract SHA
  `ef40833af6112f179d9021f036e37d78af486b9d39a19cb5d994bf693e5c3f23`.
- `scan_deliverable_consistency.py`: zero identity mismatches, zero missing
  core files, zero candidate unsourced numerics, and 26 marker hits. The
  marker hits are expected explicit `TBD-*` / `CON-*` definitions or their
  references; none is a newly inferred defect.
- `check_boundary_owner_resolution.py`: status `OK`; one whole-requirement
  exclusion checked; one per-act exclusion routed to semantic QA; no
  unresolved deterministic owner and no undefined claim.

### Manual boundary-owner QA

`REQ-012` excludes adding a third-party runtime dependency and external
network egress. Both excluded acts resolve to `DEL-01-05` through
`PEC-SVC-001`, `PEC-SVC-002`, and `CLM-011`; the requirement names
`DEL-01-05` directly and states that its standing enforcement is not
discharged here. The tool's `NOT_CHECKABLE` result is therefore a syntactic
detector limit, not an unresolved semantic owner.

## Claim census

The ledger contains exactly 82 bold local definitions:

| Class | Count |
|---|---:|
| `OUT` | 2 |
| `CLM` | 15 |
| `TBD` | 4 |
| `REQ` | 13 |
| `AC` | 16 |
| `CON` | 6 |
| `VER` | 14 |
| `AX` | 12 |

Disposition census:

- `DOCUMENTED_DIFFERENTLY`: 6
- `ALIGNED`: 76
- `AUTHORITY_CONFLICT`: 0
- `UNKNOWN`: 0
- `ACCEPTED_DIVERGENCE`: 0
- `STALE_INPUT`: 0

## Exact changed-claim candidate set

| Local ID | Defect | Minimal exact correction |
|---|---|---|
| `CLM-002` | Quotes the pre-SCA-003 `SOW-041`, `PEC-API-002`, and SSOW wording as “Session-start critical path” and treats that parenthetical as the current source basis. | Preserve the ≤100 ms p95 bound, stable IDs, and traceability. Replace the three stale quotations and interpretation with revision-1.3 wording: latency-sensitive pull path; any session-start use requires separately adopted consumer authority. |
| `CLM-008` | Embeds the upstream `DEL-08-03/CON-001` quotation containing the obsolete `PEC-API-002` session-start parenthetical and stale at-authoring representation. | Preserve serializer adjacency, the absence of an accepted compactness metric, and the no-budget-allocation conclusion. Update the embedded quotation to the repaired DEL-08-03/current PEC-API-002 basis. |
| `CLM-010` | Calls the current PRD §11 uptake metric “harness poll adoption.” | Preserve the five-locus bound census and the finding that latency is not a P1 exit or §11 metric. Replace the obsolete phrase with PRD v2.2 consumer uptake and its no-receiving-loop-conformance boundary. |
| `CLM-014` | Says `_STATUS.md` records `OPEN`; the authoritative state is `INITIALIZED`. | Correct the embedded state to `INITIALIZED`; preserve the no-implementation/no-measurement statements and do not edit `_STATUS.md`. |
| `CON-005` | Uses the superseded OI-011 interpretation to identify scoped session start and conversation→workbench as polling/sample moments. | Preserve the genuine unknowns about environment, sample population, window, repetition, concurrency, and warm/cold conditions. State that PEC declares no polling moment; this is a latency-sensitive pull path, and any session-start measurement/use requires separately adopted consumer authority. |
| `AX-012` | Correctly preserves unknowns but says the deliverable is `OPEN`. | Correct the embedded state to `INITIALIZED`; preserve all `TBD-*` / `CON-*` records, lifecycle neutrality, and no-status-touch. |

The numerical requirement, test design, measurement conditioning, output
structure, verification mapping, and non-authoritative disposition posture
remain aligned. In particular:

- the bound remains exactly ≤100 ms at p95 against the identified current
  corpus;
- the contract measures a pull path and creates no session-start, polling,
  cadence, injection, subscription, or receiving-loop conformance duty;
- the unresolved measurement-environment and sample-design questions remain
  unknowns rather than being inferred from a consumer contact point;
- `CON-006` / `AC-015` concern the suite's own one-shot-versus-standing
  measurement posture, not a receiving consumer's contact cadence; and
- the canonical downstream label “Poll-adoption measurement” remains stable
  identity and is not treated as current consumer-interface semantics.

## Non-definition production-contract corrections

A later whole-contract repair must also:

1. update frontmatter `decomposition_basis` from
   `SOFTWARE_DECOMP.md@3623b958b` to the accepted revision-1.3/SCA-003 basis;
2. replace the opening revision-1.2 `current_basis` paragraph with revision
   1.3 / SCA-003 while preserving the historical SCA-002 objective-mapping
   warrant;
3. accurately report `_CONTEXT.md` and `_REFERENCES.md` as stale derivative
   metadata without editing either file; and
4. update the quotation record after the `PEC-API-002`, `SOW-041`, OI-011,
   and embedded DEL-08-03 quotations are corrected, so it does not claim that
   superseded text is verbatim current authority.

The repair must preserve all 82 local IDs, heading order, objective mapping,
two outputs, matrix structure, dependency semantics, numerical bound, and all
unaffected meaning.

## Rulings and residuals

- `AUTHORITY_CONFLICT`: none.
- `UNKNOWN`: none beyond the contract's already explicit, aligned
  `TBD-*` / `CON-*` definitions.
- No dependency cycle, topology change, stable-ID change, scope addition, or
  lifecycle act is proposed.
- Correcting embedded lifecycle prose to the existing `INITIALIZED` authority
  is not a status transition.
