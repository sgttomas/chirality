---
amendment_id: SCA-003
doc_kind: scope_change.handoff_state
decomp_variant: SOFTWARE
gate: 5
created: 2026-07-28
status: closed_for_scope_change_only
---

# SCA-003 — Handoff State

## State

| Field | Value |
|---|---|
| `DecompositionTruthState` | `COMPLETE` |
| `DerivativePackageState` | `COMPLETE` — decomposition-local derivatives only |
| `ContentRemediationState` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` |
| `MetadataAlignmentState` | `NOT_REQUIRED` |
| `AuditState` | `NON_BLOCKING_PASS` |
| `ReadyForNextPhase` | `REGEN_ONLY` |
| `ClosureVerdict` | `CLOSED_FOR_SCOPE_CHANGE_ONLY` |

## Accepted upstream snapshots

- D-PEC-68 durable merge:
  `ec3bec922e2e62e32fb283c5873b28b2bb9c510e`.
- PRD v2.2:
  `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`.
- Pre-change audit:
  `COV_SCA003_PRECHANGE_2026-07-28_0817`.
- Final post-change audit:
  `COV_SCA003_POSTCHANGE_FINAL_2026-07-28_0831`, `OK`, 0 blockers /
  0 warnings; its summary is copied to `Post_Change_Coverage.json`.

## Accepted decomposition successor

`execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.3, with:

- `SOFTWARE_DECOMP.md` SHA-256
  `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787`;
- `ScopeLedger.csv` SHA-256
  `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5`;
- `Deliverables.csv` SHA-256
  `b27ff4631f4966931990bbf9c033d2593d3dd8ac51b09e0d5112002b98afbc40`.

## Closure and rerun requirements

SCA-003 is closed only for scope change. The owning downstream workflows must
regenerate or explicitly re-pin affected `ScopeOfWork.md` contracts and all
stale `_REFERENCES.md` surfaces before relying on the successor content. They
must preserve the consumer-owned posture and may not create a receiving-loop
duty without that loop's own authority.

The active L-A1 reliance hold remains in force. No implementation, lifecycle,
dependency, estimate, schedule, release or hold-release authority is carried
by this handoff.

## Derivative-package state

| Package | Owner | Status | Evidence | Next required action |
|---|---|---|---|---|
| Decomposition-local contexts | SCOPE_CHANGE | `COMPLETE` | Three exact context diffs | None |
| Active ScopeOfWork contracts | WORKING_ITEMS / contract owner | `STALE_FROZEN` | Changed SOW/DEL semantics; zero contract writes | Regenerate or reconcile under separate authority |
| Reference packets | PROJECT_SETUP / packet owner | `STALE_FROZEN` | 64 `_REFERENCES.md` unchanged | Re-pin revision basis |
| Dependencies | PROJECT_SETUP | `CURRENT_UNCHANGED` | Aggregate hash unchanged | None |
| Coverage evidence | AUDIT_DECOMP | `COMPLETE` | Pre/interim/final snapshots | Preserve |

## Active derivative-surface state

| Surface | Classification | Status | Evidence |
|---|---|---|---|
| Three `_CONTEXT.md` | `DIRECT_EDIT` | `CURRENT` | Descriptions match `Deliverables.csv`; revision 1.3 provenance |
| `_Decomposition/_LATEST.md` | `RECOMPUTE` | `CURRENT` | Revision 1.3 and direct hashes |
| `_ScopeChange/_LATEST.md` | `RECOMPUTE` | `CURRENT` | Points to this complete snapshot |
| SCA-003 snapshot | `RECOMPUTE` | `CURRENT` | Required artifact set present |
| DecompCoverage | `RECOMPUTE` | `CURRENT` | Final pointer-aware audit |
| Contracts and references | `NO_CHANGE` | `STALE_FROZEN` | Explicit downstream obligation |
| Dependencies, lifecycle, hold | `NO_CHANGE` | `CURRENT_UNCHANGED` | Exact diff/hash checks |

Active snapshot parity: `_ScopeChange/_LATEST.md` names this snapshot and all
required SOFTWARE artifacts are present. KTY remediation and metadata
alignment are not applicable to this SOFTWARE amendment.

## Remaining blockers

No blocker prevents scope-change closure. Production reliance remains blocked
by the active hold and by downstream regeneration/re-pin obligations.

Next owning workflows: CHANGE for Git publication; then PROJECT_SETUP and
WORKING_ITEMS for separately authorized regeneration/re-pin work.
