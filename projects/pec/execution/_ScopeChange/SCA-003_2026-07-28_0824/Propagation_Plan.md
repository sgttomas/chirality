---
amendment_id: SCA-003
doc_kind: scope_change.propagation_plan
decomp_variant: SOFTWARE
gate: 4
created: 2026-07-28
status: owner_ruled
---

# SCA-003 — Propagation Plan

## Gate 4 recommendation and owner-approved selection

**Recommendation:** apply only the direct decomposition postimage and three
exact `_CONTEXT.md` mirrors; regenerate SCA/audit derivative evidence and
pointers; freeze contracts, references, dependencies, hold, lifecycle and
implementation for later owning workflows.

**Owner-approved selection under the standing direction:** approve the
recommendation exactly.

Gate 4 result: **PASS / RULED**.

## Authorized propagation

| Surface | Operation |
|---|---|
| `SOFTWARE_DECOMP.md` | Apply approved semantic edits and revision 1.3 history |
| `ScopeLedger.csv` | Modify only SOW-041/060/064/085/088 statement, source or notes cells |
| `Deliverables.csv` | Modify only Description for DEL-00-01/10-05/10-12 |
| Three `_CONTEXT.md` files | Mirror those descriptions and append revision-1.3 provenance |
| `_Decomposition/_LATEST.md` | Point to revision 1.3 and this handoff |
| `_ScopeChange/SCA-003_2026-07-28_0824/` | Complete immutable SCA evidence |
| `_ScopeChange/_LATEST.md` | Point to SCA-003 |
| `_Evaluation/DecompCoverage/` | Preserve pre/post audit snapshots and final pointer |

## Frozen propagation

- `ScopeOfWork.md`: no write.
- `_REFERENCES.md`: no write.
- `Dependencies.csv`: no write.
- `ACTIVE_RELIANCE_HOLDS.csv`: no write; hold remains active.
- `_STATUS.md`: no write.
- PEC implementation/source: no write.

These surfaces are reported as rerun obligations, not silently reconciled.

## Verification contract

- Full strict register validator: zero errors and zero warnings.
- AUDIT_DECOMP pre and final post passes: no blockers.
- Topology: 94 scope items / 11 packages / 64 deliverables / 6 objectives.
- Dependency aggregate SHA-256 unchanged:
  `47f98a0157d0781973e1b42673f6a66c0223f9112ea35a2f322db8aea9f0647b`.
- PRD SHA-256 unchanged:
  `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`.
- DEL-10-12 label/path unchanged.
- `git diff --check` clean and changed-path fence exact.

## Package-role classification

| Role | Surfaces | Gate-5 state |
|---|---|---|
| Working decomposition truth | `SOFTWARE_DECOMP.md` | Directly amended and accepted |
| Authoritative companion registers | `ScopeLedger.csv`, `Deliverables.csv` | Directly amended in exact cell windows |
| Derived working metadata | Three exact `_CONTEXT.md` files | Directly propagated |
| Snapshot / handoff artifacts | SCA-003 and DecompCoverage snapshots, pointers | Recomputed |
| Derived publication / contracts | `ScopeOfWork.md`, `_REFERENCES.md` | Frozen and marked stale |
| Downstream authority/control | dependencies, lifecycle, hold | No change |

The cumulative `Supersession_Map.csv` is generated with
`tools/coordination/accumulate_supersession_map.py` from the accepted SCA-002
map and no current delta.
