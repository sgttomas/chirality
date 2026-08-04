---
amendment_id: SCA-003
doc_kind: scope_change.basis_reconciliation_impact
created: 2026-08-02
status: AWAITING_OWNER_ACCEPTANCE
---

# SCA-003 antecedent basis reconciliation — impact assessment

## Gate posture

The 2026-08-02 continuation ruling confirms the requested repair envelope and
authorizes preparation/routing only. It does not accept this assessment,
approve the exact bytes, authorize application, or waive either owning
instrument's gates.

This antecedent repair is not the zero-action TM-ROOT-107 decomposition
disposition. It exists so that SCA-003 Gate 1 can later be rerun against one
internally consistent current basis. `Parsed_Actions.csv` therefore remains
the header-only parse of the original two-input intake; the two administrative
repair rows are separately recorded in `Basis_Reconciliation_Actions.csv`.

## Owning instruments and applicable human gates

| Surface | Owning instrument | Current gate | Application gate |
|---|---|---|---|
| `docs/PRD_ROOT.md` | Root product-basis M2 instruction-surface correction, using PR review under D-1 and the standing Revision-8 authority | Exact metadata candidate and impact/propagation acceptance | Explicit owner application authorization; M2 manifest, routed notices, export-manifest/public-export disposition, validation, and CHANGE closeout remain required |
| `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | SCOPE_CHANGE metadata amendment discipline | Exact metadata candidate and impact/propagation acceptance | Apply only after the PRD candidate is applied; validate REF-001 against the exact applied PRD bytes; no companion-register or `_LATEST.md` change |

The product-basis correction must apply first because the decomposition
candidate's REF-001 pins the exact PRD candidate SHA-256.

## Four-lens impact assessment

| Lens | Finding | Consequence |
|---|---|---|
| Decomposition structure | No scope item, package, deliverable, objective, stable ID, mapping, status row, count, or topology changes | No parent/child closure set; no new decomposition action; no companion-register edit |
| Variant-local metadata | Only the decomposition working surface's current title/header/status, sole-source pin, additive DEC-024/Change Log disposition, and downstream acceptance note change | Exact candidate SHA-256 `69bdb9ca…1278c`; source and deliverable registers remain byte-identical |
| Product basis | PRD stable-commitment rows and the accepted §5.3.1 annex are byte-identical; current-status/document-control metadata is layered over preserved Revision-7 proposal history | Exact candidate SHA-256 `d4f97d75…5cc4`; no product requirement or authority effect is created by the candidate itself |
| Downstream consumers | Any accepted `docs/PRD_ROOT.md` byte change is an M2 instruction-surface tranche under PRD §9.4 | Application must separately satisfy tranche-manifest, routed-notice, export disposition, and CHANGE gates; no project-loop write is made by this preparation run |
| Invariant / telemetry risk | The proposed pair removes an authority-state contradiction; identifier set remains 89 and all 43 PRD stable-commitment rows are unchanged | No coverage, estimate, dependency, schedule, lifecycle, runtime, release, or reliance rerun is caused by the metadata semantics themselves |

## Derivative-surface classification

| Surface | Classification | State after candidate acceptance but before application | Required owner/workflow action |
|---|---|---|---|
| PRD Revision-7 candidate controls | `NO_CHANGE_HISTORICAL` | Preserved and explicitly time-scoped | None |
| PRD stable commitments and §5.3.1 | `NO_CHANGE` | Byte-identical to live Revision 8 | None |
| Decomposition companion CSVs | `NO_CHANGE` | Scope ledger SHA `3deed192…59c2`; deliverable register SHA `a29759be…1395` | None |
| `_ScopeChange/_LATEST.md` | `NO_CHANGE` | Continues to point to accepted SCA-002 because SCA-003 remains open | None during antecedent repair |
| M2 tranche manifest | `DOWNSTREAM_REQUIRED_AT_APPLICATION` | Not created | Root product-basis/M2 applying workflow |
| Registered-loop notices | `DOWNSTREAM_REQUIRED_AT_APPLICATION` | Not drafted or routed; foreign writes prohibited in this run | Root M2 applying workflow under the owner application ruling |
| Public export / export manifest | `DOWNSTREAM_DISPOSITION_REQUIRED` | Already stale by standing record; no write in this run | Export owner at the M2 application/next release, with explicit currentness record |
| AUDIT_DECOMP | `RERUN_AFTER_APPLICATION` | Existing return remains BLOCKED on the contradiction this candidate addresses | Read-only post-application rerun before SCA-003 Gate 1 is reopened |

## Orphan and rollback assessment

- Orphan risk is zero: no entity or mapping changes.
- Stable-ID risk is zero: no ID is removed, renamed, or reused; DEC-024 is an
  additive decision-log identifier in candidate bytes only.
- Before application, rollback is unnecessary because live surfaces are
  untouched. After exact application, reversal is a new owner-gated correction.
- If the owner declines either file, decline the pair: applying only the PRD
  would leave the decomposition pin stale; applying only the decomposition
  would pin bytes absent from the live product basis.

## Owner Gate-2 question

Do you accept this impact assessment and its coupled two-instrument,
PRD-first application boundary?
