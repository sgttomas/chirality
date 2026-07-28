---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
wave_id: W1
phase: R2_DISCOVERY
deliverable_id: DEL-08-03
status: complete_read_only
source_commit: 404e47c16a88e7ffdc6d1fc5fac61ebb6864211e
---

# DEL-08-03 read-only claim discovery

## Source state

- Production format: `SOW_V1`
- Lifecycle: `INITIALIZED`
- Status policy: `NO_STATUS_TOUCH`
- Contract SHA-256: `a9ed7f560a7655aa4b873ab9f35e8e662d1427044e64febbecf450017f5b884a`
- `_STATUS.md` SHA-256: `4b119028c9af1d82aa529cdd1bf851493f63b3471998ca0dbb3667e2caa0d5ee`
- PRD v2.2 SHA-256: `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`
- SOFTWARE_DECOMP revision 1.3 SHA-256: `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787`
- Hold preflight: `historical-read-only-inspection` returned `ALLOW`.

## Claim census

Every bold local definition was extracted exactly once:

| Class | Count |
|---|---:|
| `CLM` | 11 |
| `OUT` | 3 |
| `TBD` | 3 |
| `REQ` | 13 |
| `AC` | 14 |
| `CON` | 4 |
| `VER` | 13 |
| `AX` | 10 |
| **Total** | **71** |

Disposition census:

- `ALIGNED`: 65
- `DOCUMENTED_DIFFERENTLY`: 6
- `ACCEPTED_DIVERGENCE`: 0
- `AUTHORITY_CONFLICT`: 0
- `UNKNOWN`: 0
- `STALE_INPUT`: 0

Exact repair-candidate set:

`CLM-011`, `REQ-005`, `CON-001`, `CON-003`, `AX-006`, `AX-010`.

## Minimal semantic repairs

- `REQ-005`: retain the machine-first artifact requirement, but replace the
  superseded statement that harnesses poll and inject. State that an explicitly
  PEC-enabled harness may request orientation and may optionally inject labeled
  non-authoritative data under its own authority; no polling, cadence, contact,
  or injection duty is created.
- `CON-003`: retain the unresolved meaning of “machine-first,” but replace
  polling/injection and mode-proportional consumption with consumer-owned use,
  mode mapping, cadence, and optional injection; pipeline and unscoped
  conversation may remain zero-contact.
- `CON-001`: retain the unresolved compactness conclusion and non-allocation of
  the latency budget; replace “session-start critical path” with the v2.2
  latency-sensitive pull-path wording and its separate-consumer-authority
  condition. DEL-08-04 now has an `INITIALIZED` production contract.
- `AX-006`: preserve the non-transfer of the latency budget while updating or
  explicitly historicizing the claim that DEL-08-04 had no accepted contract.
- `CLM-011` and `AX-010`: replace `OPEN` with `INITIALIZED`; preserve
  lifecycle neutrality and the absence of implementation/artifacts/results.

Non-local-definition repair candidates:

- frontmatter `decomposition_basis` and the opening basis paragraph still
  present revision 1.2 / `3623b958b` as current; advance contract basis to
  revision 1.3/SCA-003 while retaining the older `_REFERENCES.md` and
  `_CONTEXT.md` pins as superseded provenance;
- the prose following `CLM-005` says DEL-08-04 had no accepted ScopeOfWork at
  authoring time. It may remain only as explicitly historical context or be
  updated to current evidence.

No self-polling implementation, forced contact, external cadence, required
injection, or receiving-loop conformance criterion is otherwise introduced.
Occurrences of “conformance” outside the stale source rationale describe the
format and its own tests, not a consumer duty.

## Deterministic checks

- `validate_scope_of_work.py`: PASS; `SOW_V1`; 0 issues.
- `derive_review_checklist.py`: PASS; 14 items, `AC-001..AC-014` exactly once
  in source order.
- `check_boundary_owner_resolution.py`: `OK`; one whole-requirement exclusion
  checked; four `NOT_CHECKABLE`; zero unresolved owners and zero
  `NO_CITED_CLAIM`.
- Manual resolution of the four `NOT_CHECKABLE` cases:
  - `REQ-004` → schema/version ownership `DEL-08-02`, cited through `CLM-006`;
  - `REQ-008` → citation/stamp production `DEL-04-03` and presence guard
    `DEL-06-05`, cited through `CLM-009`;
  - `REQ-009` → limitation rendering `DEL-04-05`, cited through `CLM-009`;
  - `REQ-011` → dependency/no-egress enforcement `DEL-01-05`, cited in the
    requirement and `CLM-009`.
- `scan_deliverable_consistency.py`: completed; zero identity mismatches, zero
  unsourced-numeric candidates, zero missing artifacts, and 14 marker findings.
  Marker findings are intentional register `TBD` values, the three local
  `TBD-*` records, the known dependency `location TBD`, and references to
  those records. The scanner's null package/production-unit summary fields
  are an execution-substrate reporting limitation; frontmatter and the
  contract validator resolve `PKG-08` / `DEL-08-03`.

## Blockers and preserved state

- `AUTHORITY_CONFLICT`: none.
- `UNKNOWN`: none.
- The three `TBD-*` and four `CON-*` records remain open; the corrections do
  not decide them.
- No new dependency or cycle was found.
- Stable IDs, heading order, outputs, acceptance matrix, objectives,
  dependencies, and unaffected meaning remain preserved.
- No contract, `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, dependency,
  decomposition, hold, lifecycle, implementation, or other control/source
  surface was edited.
