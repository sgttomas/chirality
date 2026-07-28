---
amendment_id: SCA-003
doc_kind: scope_change.impact_assessment
decomp_variant: SOFTWARE
gate: 2
created: 2026-07-28
status: owner_ruled
---

# SCA-003 — Impact Assessment

## Gate 2 recommendation and owner-approved selection

**Recommendation:** accept the bounded impact assessment and proceed only
with the ten `MODIFY` actions in `Amendment_Actions.csv`. Treat the
decomposition as authoritative truth and all contexts, audit outputs and SCA
records as derivative. Freeze every excluded downstream surface.

**Owner-approved selection under the standing direction:** approve the
recommendation exactly.

Gate 2 result: **PASS / RULED**.

## Impact by lens

| Lens | Impact |
|---|---|
| Decomposition structure | No entity, partition, mapping, envelope, objective or stable-ID change |
| Dependency topology | No `Dependencies.csv` write; aggregate manifest SHA-256 remains `47f98a0157d0781973e1b42673f6a66c0223f9112ea35a2f322db8aea9f0647b` |
| Product meaning | C3/C15 and their directly mapped statement/description surfaces adopt consumer-owned use, never-forced contact, P2-B observation and ADR-014 historical lineage |
| Deliverables | Descriptions only for DEL-00-01, DEL-10-05 and DEL-10-12 |
| Context metadata | Description and decomposition-basis provenance only for the same three deliverables |
| Contracts | Ten active `ScopeOfWork.md` packets are potentially stale; no contract is amended here |
| References | All 64 `_REFERENCES.md` remain untouched and require regeneration/re-pin by the owning workflow |
| Hold | `PEC-HOLD-001` remains active; `ACTIVE_RELIANCE_HOLDS.csv` is unchanged |
| Lifecycle | `_STATUS.md` remains unchanged |
| Implementation | No source, runtime, adapter, test, estimate, schedule or release write |

## Preservation invariants

- Scope ledger remains 94 rows: 71 IN / 14 OUT / 9 TBD.
- Package count remains 11.
- Deliverable count remains 64.
- Objective count remains 6.
- DEL-10-12 retains its canonical ID, label and path.
- Every dependency edge and dependency-file byte remains unchanged.
- `ContextBudgetQA.csv` and `Companion_Inventory.csv` remain unchanged.

## Derivative-package status

| Package | Owner | Status after amendment | Required rerun / closure action |
|---|---|---|---|
| Three deliverable contexts | SCOPE_CHANGE for exact metadata propagation | `CURRENT` | None |
| Ten affected active ScopeOfWork contracts | WORKING_ITEMS / contract owner | `STALE` | Regenerate or explicitly reconcile before reliance |
| 64 deliverable reference packets | PROJECT_SETUP / packet owner | `STALE` | Re-pin to revision 1.3 under owning authority |
| Dependency package | PROJECT_SETUP | `CURRENT_UNCHANGED` | No rerun required for topology; preserve byte identity |
| SCA-003 evidence package | SCOPE_CHANGE | `CURRENT` | Final audit and pointer closure |
| Decomposition coverage package | AUDIT_DECOMP | `CURRENT` after final pass | Preserve immutable pre/interim/final snapshots |

## Derivative-surface classification

| Surface | Package role | Classification | Authority basis |
|---|---|---|---|
| `SOFTWARE_DECOMP.md` | working surface / decomposition truth | `DIRECT_EDIT` | Gate 3 approved postimage |
| `ScopeLedger.csv`, `Deliverables.csv` | authoritative companion registers | `DIRECT_EDIT` | Gate 3 approved row/cell window |
| Three `_CONTEXT.md` files | derived working metadata | `DIRECT_EDIT` | Exact propagation of approved descriptions and basis |
| `_Decomposition/_LATEST.md`, `_ScopeChange/_LATEST.md` | handoff pointers | `RECOMPUTE` | Gate 4 propagation |
| SCA-003 snapshot | immutable snapshot / handoff artifact | `RECOMPUTE` | Gates 1–5 evidence |
| DecompCoverage snapshots | audit snapshots | `RECOMPUTE` | AUDIT_DECOMP |
| `ScopeOfWork.md`, `_REFERENCES.md` | derived publication / contract artifacts | `NO_CHANGE` | Explicit fence; stale state surfaced |
| `Dependencies.csv`, `_STATUS.md`, hold register | authoritative downstream/control surfaces | `NO_CHANGE` | Explicit fence and preservation checks |
| PEC implementation | product implementation | `NO_CHANGE` | No implementation authority |

Orphan risk is zero: no parent, child, mapping, entity, objective or dependency
topology changes.

## Downstream notice

The next workflow may regenerate affected contracts and references only under
its own authority. It must not infer a receiving-loop duty from the amended
PEC decomposition.
