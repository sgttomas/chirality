---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
wave_id: W1
phase: R2_DISCOVERY
deliverable_id: DEL-10-11
status: complete_read_only
source_commit: 404e47c16a88e7ffdc6d1fc5fac61ebb6864211e
---

# DEL-10-11 read-only claim discovery

## Source state

- Production format: `SOW_V1`
- Lifecycle: `INITIALIZED`
- Status policy: `NO_STATUS_TOUCH`
- Contract SHA-256: `bd44b1e27efe57180185c350d3c4da03a7323a63ed71ddba15cad463bef1d8e6`
- `_STATUS.md` SHA-256: `83e644c4f797d8b4c2a25952a0be3161d064dcee52e8b365faa845b9654f5bb6`
- PRD v2.2 SHA-256: `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`
- SOFTWARE_DECOMP revision 1.3 SHA-256: `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787`
- Hold preflight: `historical-read-only-inspection` returned `ALLOW`.

## Claim census

Every bold local definition was extracted exactly once:

| Class | Count |
|---|---:|
| `CLM` | 17 |
| `OUT` | 1 |
| `TBD` | 5 |
| `CON` | 6 |
| `REQ` | 13 |
| `AC` | 15 |
| `VER` | 13 |
| `AX` | 9 |
| **Total** | **79** |

Disposition census:

- `ALIGNED`: 73
- `DOCUMENTED_DIFFERENTLY`: 6
- `ACCEPTED_DIVERGENCE`: 0
- `AUTHORITY_CONFLICT`: 0
- `UNKNOWN`: 0
- `STALE_INPUT`: 0

Exact repair-candidate set:

`CLM-003`, `CLM-015`, `CLM-017`, `CON-003`, `AC-015`, `AX-009`.

## Minimal semantic repairs

- `CLM-003`: replace the superseded PRD §11 clause and limb descriptions with
  PRD v2.2's two-part evidence: negligible explicit consumer enablement or
  negligible orientation use by enabled consumers, plus owner non-use.
  Preserve the conclusion that parity metric 5 does not arm either limb.
- `CLM-015`: retain the canonical `DEL-10-12` ID, “Poll-adoption metric” label,
  and path, but describe its revised `SOW-060` duty as consumer-uptake
  measurement. Do not infer polling, an externally imposed cadence, required
  contact, or required injection.
- `CON-003`: retain the open threshold/target/direction/interpretation record,
  but update its falsification-evidence rationale to the v2.2 consumer-enable,
  enabled-consumer-use, and owner-use/non-use formulation.
- `AC-015`: retain the accountable-owner decision about the parity metric's
  purpose, gate role, publication surface, and recipient; update only its stale
  falsification premise.
- `CLM-017` and `AX-009`: replace `OPEN` with `INITIALIZED` while preserving
  lifecycle neutrality and the no-implementation/no-artifact assertion.
- `AX-009`: also advance the accepted decomposition basis from revision
  1.2/SCA-002/`3623b958b` to revision 1.3/SCA-003/
  `404e47c16a88e7ffdc6d1fc5fac61ebb6864211e`. Older pins may remain only as
  explicitly superseded provenance.

PRD v2.2 makes adoption evidence consumer-relative. Receiving-loop
conformance, successful parsing, transport compatibility, or another system's
ability to consume an artifact does not establish enablement or actual use.
Nothing else in this contract imposes such a conformance criterion.

Non-local-definition repair candidates:

- frontmatter `decomposition_basis`, the opening basis paragraphs, and related
  current-basis prose still present revision 1.2 / `3623b958b` as current;
- the Production and Verification Method introduction still says the
  deliverable is at `OPEN`;
- the `AC-015` acceptance-matrix row repeats the superseded falsification
  premise and must follow the corrected criterion without changing matrix
  structure.

## Deterministic checks

- `validate_scope_of_work.py`: PASS; `SOW_V1`; zero issues.
- `derive_review_checklist.py`: PASS; 15 items, `AC-001..AC-015` exactly once
  in source order.
- `check_boundary_owner_resolution.py`: `OK`; one per-act exclusion routed as
  `NOT_CHECKABLE`; zero unresolved owners and zero requirements lacking a cited
  claim.
- Manual resolution of the `NOT_CHECKABLE` case:
  - `REQ-011` binds the input to `DEL-03-04`'s accepted contract, cites
    `[E-A18]` and `CLM-010`, and points through `AX-006`; `CLM-013` quotes the
    upstream contract's exclusion of acts owned by other deliverables. The
    owner and exclusion are semantically explicit even though the checker
    cannot bind them syntactically.
- `scan_deliverable_consistency.py`: completed; zero identity mismatches, zero
  missing artifacts, 20 marker findings, and one candidate unsourced numeric.
  The marker findings are intentional register `TBD` values, quoted upstream
  `TBD` records, the five local `TBD-*` records, and references to them. The
  sole numeric candidate is the accepted SCA-002 Gate 5 verification-table row
  identifier `4v`, not an unsourced production parameter. The scanner's null
  package/production-unit summary fields are an execution-substrate reporting
  limitation; frontmatter and the contract validator resolve `PKG-10` /
  `DEL-10-11`.

## Blockers and preserved state

- `AUTHORITY_CONFLICT`: none.
- `UNKNOWN`: none.
- The five `TBD-*` and six `CON-*` records remain open; the corrections do not
  decide them.
- The parity metric's threshold, purpose, release-gating role, consumer,
  publication surface, inclusion discriminator, and denominator remain
  unresolved exactly where the contract records them.
- No new dependency or cycle was found.
- Stable IDs, heading order, output identity, acceptance-matrix structure,
  objectives, dependencies, and unaffected meaning remain preserved.
- No contract, `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, dependency,
  decomposition, hold, lifecycle, implementation, or other control/source
  surface was edited.
