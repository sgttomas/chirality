---
amendment_id: SCA-001
doc_kind: scope_change.handoff_state
decomp_variant: SOFTWARE
created: 2026-07-24
status: closed_for_scope_change_only
authority: D-PEC-61
---

# SCA-001 Handoff State

## Fixed state fields

| Field | Current state |
|---|---|
| `DecompositionTruthState` | `COMPLETE` — approved revision 1.1 amendment applied and validated |
| `DerivativePackageState` | `COMPLETE` — affected decomposition package and SCA evidence are in parity |
| `ContentRemediationState` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` — not executed by SCOPE_CHANGE; released to Project Setup |
| `MetadataAlignmentState` | `NOT_REQUIRED` |
| `AuditState` | `WARNINGS` — only the expected pre-scaffold `AUDIT_DECOMP FAILED_INPUTS` limitation |
| `ReadyForNextPhase` | `REGEN_ONLY` |
| `ClosureVerdict` | `CLOSED_FOR_SCOPE_CHANGE_ONLY` |

## Validated successor

- **Upstream authority:** PRD v2.1 (`D-PEC-58`, amended by `D-PEC-61`).
- **Pre-change accepted basis:** SOFTWARE_DECOMP revision 1.0 (`D-PEC-60`).
- **Validated successor:** SOFTWARE_DECOMP revision 1.1, SCA-001.
- **Active state:** decomposition `_LATEST.md` names revision 1.1
  `current_basis`.
- **Authoritative truth changed:** `SOFTWARE_DECOMP.md`, the `SOW-064` row in
  `ScopeLedger.csv`, the `DEL-10-10` rows in `Deliverables.csv` and
  `ContextBudgetQA.csv`, and the decomposition handoff pointer.
- **Topology:** unchanged at 94 scope items, 64 deliverables, 11 packages,
  and 6 objectives.

## Derivative-package state

| Package | Owner | Status | Evidence | Next required action |
|---|---|---|---|---|
| Pre-change audit | `AUDIT_DECOMP` | Historical derivative evidence; expected `FAILED_INPUTS` | `execution/_Evaluation/DecompCoverage/COV_SCA001_PRECHANGE_2026-07-24_2209/` | Preserve |
| Post-change audit | `AUDIT_DECOMP` | Current derivative evidence; expected `FAILED_INPUTS` | `execution/_Evaluation/DecompCoverage/COV_SCA001_POSTCHANGE_2026-07-24_2230/` | Rerun after Project Setup scaffolding if filesystem coverage is required |
| Register-integrity evidence | `SCOPE_CHANGE` | Complete | `Pre_Change_Coverage.json`; `Post_Change_Coverage.json` | Preserve |
| Full DAG / dependency register | `PROJECT_SETUP` | Not created; frozen pending confirmation | D-PEC-61; this handoff | Materialize from revision 1.1 after confirmation |
| Package/deliverable scaffold | `PROJECT_SETUP` → `PREPARATION` | Not created | Expected audit limitation | Create only under Project Setup's gates |
| Estimates and schedules | `PROJECT_SETUP` | Not created | No current artifacts | Generate only if selected downstream |
| Implementation | `WORKING_ITEMS` | Not started | No scaffold/activation | Consume accepted downstream state |

## Active surface state

| Surface | Classification | Status | Evidence |
|---|---|---|---|
| `SOFTWARE_DECOMP.md` | `DIRECT_EDIT` | Revision 1.1 validated | `Post_Change_Coverage.json` |
| `ScopeLedger.csv` | `DIRECT_EDIT` | SOW-064 validated | Bidirectional mapping and target-lineage checks |
| `Deliverables.csv` | `DIRECT_EDIT` | DEL-10-10 validated | Deliverable/objective/envelope checks |
| `ContextBudgetQA.csv` | `DIRECT_EDIT` | DEL-10-10 QA parity validated | QA one-to-one and envelope parity checks |
| `_Decomposition/_LATEST.md` | `DIRECT_EDIT` | Honest pending-confirmation pointer | Source-anchor and pointer-state checks |
| `Companion_Inventory.csv` | `NO_CHANGE` | Byte-identical | SHA-256 `18793e150c537371f80d659af2784674d42bac0de37bf7128e484774a557ec23` |
| `Supersession_Map.csv` | `RECOMPUTE` | Header-only, 0 rows, 0 findings | Registered accumulator with `--allow-empty` |
| `Supersession_Delta.csv` | `NO_CHANGE` / not required | Absent | No admitted authority fact overridden |

## Validation summary

- All six pre-change hashes matched before application.
- All CSVs parse and retain unique IDs.
- Every IN scope item retains exactly one package and one deliverable.
- All forward/reverse references and package lineage resolve.
- `SOW-064 → PKG-10 → DEL-10-10 → OBJ-006`.
- OBJ-006 support is 9 scope items and 9 deliverables.
- Context Envelopes are S 28 / M 34 / L 2 / XL 0.
- C16, DL-16, and revision-history 1.1 occur exactly once.
- Source anchors cite PRD v2.1 and D-PEC-61.
- Plural product intent, human authority, acyclic bootstrap, and file-native
  fallback remain explicit.
- `git diff --check` and the exact path-fence check pass.

The audit warning is not a semantic or register-integrity failure. It records
that zero package/deliverable folders exist before Project Setup, so
`AUDIT_DECOMP` cannot yet measure filesystem coverage. OI-013 remains open.

## Closure and next owners

No SCA closure blocker remains.

1. `PROJECT_SETUP` is released with revision 1.1 as its accepted basis,
   `FULL_GRAPH` already selected, and dependency materialization pending.
2. `CHANGE` is authorized to receive the validated file list for scoped Git
   closeout.
3. Neither workflow was invoked by SCOPE_CHANGE.

Project Setup's Phase 1.3 dependency-maturity threshold and register-storage
choices remain at their normal owner gate.
