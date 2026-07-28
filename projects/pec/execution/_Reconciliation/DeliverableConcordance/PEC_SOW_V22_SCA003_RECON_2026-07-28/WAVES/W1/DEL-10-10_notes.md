---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
wave_id: W1
phase: R2_DISCOVERY
deliverable_id: DEL-10-10
operation: VERIFY
production_format: SOW_V1
lifecycle_state: INITIALIZED
status_policy: NO_STATUS_TOUCH
source_commit: 404e47c16a88e7ffdc6d1fc5fac61ebb6864211e
result: REPAIR_CANDIDATES_FOUND
---

# DEL-10-10 claim discovery notes

## Scope and write boundary

Read-only semantic discovery was performed against:

`projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/ScopeOfWork.md`

No contract, `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, dependency,
decomposition, PRD, implementation, lifecycle, release, estimate, schedule,
or other run artifact was edited. The six `DEL-10-10_*` W1 files are the only
worker outputs.

## Frozen-source reproduction

| Surface | SHA-256 | Result |
|---|---|---|
| `ScopeOfWork.md` | `5e63c9ff6e2846e93c8e1941d79f7f64a9888c83f16074d7ff404c8806da2be5` | reproduced |
| `_STATUS.md` | `24030ebc3d4badfce74149e729a67b6a525522ccd08f048dd4d31811d57905a3` | reproduced; `INITIALIZED`; untouched |
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
  `5e63c9ff6e2846e93c8e1941d79f7f64a9888c83f16074d7ff404c8806da2be5`.
- `scan_deliverable_consistency.py`: zero identity mismatches, zero missing
  core files, zero candidate unsourced numerics, and 17 marker hits. Ten
  marker details are emitted and seven are reported truncated by the tool;
  the emitted hits are expected explicit `TBD-*` / `CON-*` definitions or
  their references, not newly inferred defects.
- `check_boundary_owner_resolution.py`: status `OK`; one whole-requirement
  exclusion checked; no per-act exclusion was routed to semantic QA; no
  unresolved deterministic owner and no undefined claim.

### Manual boundary-owner QA

`REQ-011` excludes grammar definition, register/work-graph parsing, rebuild,
reconcile, drift classification, parity diff, kill test, no-ruling-write
testing, rebuild-bound measurement, edge materialization, blocker computation,
scaffolding, and writes to governed control surfaces. `CLM-018`, which the
requirement cites, names the owning deliverables or workflow for each act.
`CLM-017` supplies the governing “validation act, not a reconciler feature”
boundary. No owner is unresolved.

## Claim census

The ledger contains exactly 86 bold local definitions:

| Class | Count |
|---|---:|
| `OUT` | 1 |
| `CLM` | 20 |
| `TBD` | 5 |
| `REQ` | 14 |
| `AC` | 16 |
| `CON` | 5 |
| `VER` | 14 |
| `AX` | 11 |

Disposition census:

- `DOCUMENTED_DIFFERENTLY`: 6
- `ALIGNED`: 80
- `AUTHORITY_CONFLICT`: 0
- `UNKNOWN`: 0
- `ACCEPTED_DIVERGENCE`: 0
- `STALE_INPUT`: 0

## Exact changed-claim candidate set

| Local ID | Defect | Minimal exact correction |
|---|---|---|
| `CLM-001` | Quotes the pre-SCA-003 `SOW-064` ledger and SSOW rows with `SourceRef` `PRD v2.1 §12, D-PEC-61` as current. | Preserve the scope statement, mappings, decision refs, and notes. Replace only the quoted source fields with `PRD v2.2 §12, D-PEC-61, D-PEC-68`. |
| `CLM-002` | Calls PRD v2.1 §12 the current first source locus and presents the superseded P1 “one loop (piping or root)” row as the live row. | Cite PRD v2.2 §12, preserve the directed-bootstrap paragraphs, quote the current P1 “PEC's own build graph” row, and retain OI-010 only as historical provenance for the incorporated clarification. |
| `CLM-004` | Quotes current `C16` with its pre-SCA-003 source field `PRD v2.1 §12, D-PEC-61`. | Preserve C16's substantive wording and update its source field to `PRD v2.2 §12, D-PEC-61, D-PEC-68`. |
| `CLM-005` | Calls revision 1.2 current and quotes the superseded “harness poll adoption” §11 metric and falsification clause. | Preserve the register-direct `OBJ-006` mapping; cite revision 1.3 and PRD v2.2 consumer uptake, explicit enablement/enabled-consumer use, and the no-receiving-loop-conformance boundary. |
| `CLM-020` | Says the lifecycle state is `OPEN`; `_STATUS.md` is `INITIALIZED`. | Correct the embedded state to `INITIALIZED`; preserve the no-implementation and future-contract statements and do not edit `_STATUS.md`. |
| `AX-011` | Correctly preserves lifecycle neutrality but says the deliverable is `OPEN`. | Correct the embedded state to `INITIALIZED`; preserve lifecycle neutrality and no-status-touch. |

The directed-bootstrap substance, requirements, evidence posture, output
structure, and owner boundaries otherwise remain aligned. In particular:

- directed bootstrap is PEC's own accepted build graph first; later DAG nodes
  consume only predecessor-produced and accepted PEC capabilities;
- the bootstrap rule is not a general receiving-consumer use mandate and
  creates no PEC-owned poll, session trigger, cadence, injection, or
  conformance condition;
- any consumer-interface use or injection remains optional and under separately
  adopted consumer authority;
- `CLM-014`'s zero-consumer statement concerns accepted deliverable dependency
  edges, not a duty imposed on external receiving loops;
- `CON-001` continues to preserve the unresolved release-gating authority
  question, and the five `TBD-*` plus remaining `CON-*` records remain explicit
  unknowns rather than inferred resolutions; and
- the stable IDs, one-output ontology, headings, requirement/acceptance/
  verification structure, and matrix shape require no change.

## Non-definition production-contract corrections

A later whole-contract repair must also:

1. update frontmatter `decomposition_basis` and the opening accepted-basis
   paragraph from revision 1.2/SCA-002 to revision 1.3/SCA-003;
2. revise the objective-warrant reproduction: the SCA-001 mapping remains
   unchanged, but the full `SOW-064` row is no longer byte-identical because
   SCA-003 changed its source-only provenance;
3. update the opening `SOW-064` source statement and ordered source chain to
   PRD v2.2 plus `D-PEC-68`;
4. update the quotation record after the SOW-064, PRD §12, C16, and PRD §11
   quotations are corrected;
5. update the AC-016 human-review/matrix evidence wording to acknowledge the
   SCA-003 source-only propagation while preserving the SCA-001 objective
   mapping; and
6. accurately report `_CONTEXT.md` and `_REFERENCES.md` as stale derivative
   metadata without editing either file.

The repair must preserve all 86 local IDs, heading order, one-output ontology,
dependency topology, standing/release-authority conflict, explicit unknowns,
objective mapping, and output-matrix structure.

## Rulings and residuals

- `AUTHORITY_CONFLICT`: none newly introduced; `CON-001` remains an explicit
  aligned unresolved authority question.
- `UNKNOWN`: none beyond the contract's already explicit, aligned `TBD-*` /
  `CON-*` definitions.
- No dependency cycle, topology change, stable-ID change, scope addition,
  consumer duty, or lifecycle act is proposed.
- Correcting embedded lifecycle prose to the existing `INITIALIZED` authority
  is not a status transition.
