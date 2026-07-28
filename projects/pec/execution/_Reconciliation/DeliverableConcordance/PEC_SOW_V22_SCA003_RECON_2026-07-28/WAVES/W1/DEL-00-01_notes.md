---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
wave_id: W1
phase: R2_DISCOVERY
deliverable_id: DEL-00-01
status: complete_read_only
source_commit: 404e47c16a88e7ffdc6d1fc5fac61ebb6864211e
---

# DEL-00-01 read-only claim discovery

## Scope and source state

- Contract: `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/ScopeOfWork.md`
- Production format: `SOW_V1`
- Lifecycle source state: `INITIALIZED`
- Status policy: `NO_STATUS_TOUCH`
- Contract SHA-256: `e7c7ae02b254726a0a25422859b8a798b4b1989cd6cf013b0e1d41886ce3c80f`
- `_STATUS.md` SHA-256: `dc13864dac56de38e5c0dc1a82cde5cad8dad7850c1ca1e80dbfec7d5b63f9ee`
- PRD v2.2 SHA-256: `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`
- SOFTWARE_DECOMP revision 1.3 SHA-256: `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787`
- Hold preflight: `historical-read-only-inspection` returned `ALLOW` for `CLM-005` / `REQ-004`.

## Extraction census

Every bold local definition was extracted exactly once. `ClaimText` preserves
the source line verbatim except that the Markdown emphasis around the local ID
is removed.

| Claim class | Count |
|---|---:|
| `OUT` | 2 |
| `CLM` | 8 |
| `TBD` | 2 |
| `CON` | 1 |
| `REQ` | 10 |
| `AC` | 7 |
| `VER` | 4 |
| `AX` | 7 |
| **Total** | **41** |

Disposition census:

- `ALIGNED`: 33
- `DOCUMENTED_DIFFERENTLY`: 8
- `ACCEPTED_DIVERGENCE`: 0
- `AUTHORITY_CONFLICT`: 0
- `UNKNOWN`: 0
- `STALE_INPUT`: 0

Repair-candidate local IDs:

`OUT-002`, `CLM-002`, `REQ-005`, `AC-003`, `VER-002`, `AX-002`,
`AX-004`, `AX-006`.

## ADR-014 proof and residuals

The two hold-scoped clauses already contain the required correction:

- `CLM-005` says ADR-014 is historical evidence, says the old PEC
  project-adapter allocation is **not** a live v2 posture, identifies the
  D-PEC-56 adapter-retention behavior as retired, and limits carry-forward to
  the accepted Root-runtime / optional-client / no-second-loop /
  human-only-act boundary.
- `REQ-004` requires the ADR set to cite ADR-014 as historical lineage, forbids
  re-adoption of the retired adapter allocation, and explicitly requires the
  ADR to say that the old allocation of deterministic acts, RBAC, reporting,
  visibility, and data boundaries is not a PEC v2 requirement.

All nine literal `ADR-014` occurrences were reviewed:

- current-meaning defects: purpose quotation at line 19, `OUT-002` at line 59,
  `CLM-002` at line 66, and `AC-003` at line 102;
- aligned proof/boundary text: `CLM-005` at line 74 and `REQ-004` at line 92;
- historical or absence-oriented context: the SCA-002 attribution quotation
  at line 38, the absence rationale at line 45, and the instruction to read
  archived ADR text at line 112. The line-38 quotation should be explicitly
  retained as historical attribution or simplified during repair so that it
  cannot be mistaken for current product meaning.

Three local claims without a literal `ADR-014` token still carry stale
two-live-posture semantics and are repair candidates: `REQ-005`, `VER-002`,
and `AX-004`.

No claim was found that reasserts the retired allocation's acts as current v2
PEC responsibilities. The defects instead misclassify ADR-014 itself as a
live carried posture. The exact repair is therefore a status/meaning
correction, not a new ownership allocation.

## Other whole-contract repair candidates

These are non-local-definition prose or metadata and therefore do not create
additional rows in the claim ledger:

- frontmatter `decomposition_basis` still pins revision 1.2 commit
  `3623b958b`; current accepted basis is revision 1.3 through SCA-003;
- the purpose quotation still reproduces the superseded SOW-088 wording;
- the objective-warrant and basis-provenance paragraphs still present
  revision 1.2 as the current successor rather than as historical attribution;
- the production-sequence phrase “carried-posture re-citations” and the
  OUT-002 matrix evidence should express the ADR-002-live / ADR-014-historical
  asymmetry;
- the completion preamble says `_STATUS.md` records `OPEN`, while the actual
  lifecycle source records `INITIALIZED`; local claim `AX-006` carries the
  same stale state and is included in the repair set.

No stable ID, objective mapping, dependency, output-matrix structure, or
unaffected contract meaning needs to change.

## Deterministic tool verdicts

### ScopeOfWork validation

- Verdict: `PASS`
- Resolved format: `SOW_V1`
- `valid: true`
- Issues: 0

### REVIEW checklist derivation

- Verdict: `PASS`
- Item count: 7
- Every `AC-001..AC-007` appears exactly once in source order.
- The derived checklist correctly reflects the current contract bytes. Its
  `AC-003` entry is therefore stale semantically and must be regenerated after
  the approved contract repair.

### Boundary-owner resolution

- Verdict: `OK`
- Contracts failing: 0
- Deterministically checkable boundary requirements: 0
- Per-act `NOT_CHECKABLE`: 0
- `NO_CITED_CLAIM`: 0
- Manual semantic review: `REQ-004` is a historical-allocation
  non-re-adoption rule, not a cross-deliverable “perform no act owned by”
  requirement. It enumerates the retired acts and binds their rejection to
  `CLM-005`; it creates no active owner transfer and no unresolved v2 owner.

### Deliverable consistency

- Verdict: completed; no identity mismatch and no missing core artifact.
- Candidate unsourced numerics: 1, a false positive on the cited section token
  `§2.1` at line 21 rather than an unsourced design parameter.
- Marker findings: 6. They are the intentional `ResponsibleParty: TBD`,
  `TBD-001`, `TBD-002`, and references to those local records; none is an
  unlabelled unknown.
- The scanner returned `package_id: null` and `production_unit_id: null` while
  also returning zero identity mismatches. This is an execution-substrate
  reporting limitation, not a project-content finding; the validator and
  frontmatter independently resolve `PKG-00` / `DEL-00-01`.

## Conflict and dependency disposition

- `AUTHORITY_CONFLICT`: none.
- `UNKNOWN`: none.
- `CON-001` and both `TBD-*` definitions remain intentionally open and aligned;
  they are not inferred closed.
- No mutual dependency or new cycle was discovered. Existing proposed
  downstream relations remain non-gating and untouched.
- No contract, status, context, reference, dependency, decomposition, hold,
  lifecycle, implementation, or control surface was edited in this wave.
