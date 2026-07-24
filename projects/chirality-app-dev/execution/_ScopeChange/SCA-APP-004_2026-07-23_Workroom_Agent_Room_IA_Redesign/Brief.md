# SCA-APP-004 Brief — Workroom and Agent Room Information Architecture

**Status:** `GATE_5_GOVERNANCE_PROPAGATION_IN_PROGRESS`
**Date:** `2026-07-23`
**Requested by:** owner
**Decomposition variant:** `SOFTWARE`
**Decomposition:** `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
**Allow renumbering:** `false`
**Pre-change audit:** `execution/_Evaluation/DecompCoverage/COV_SCA_APP_004_PRECHANGE_2026-07-23_1330/`

## Human-originated change request

Replace the current system-shaped and chat-dominant application experience
with a calm, artifact-centred professional Workroom and a spatial Agent Room.
The first product horizon centres files, Markdown, diffs, deliverables,
evidence, validation results, and agent returns. Agent controls and chat
support those artifacts. A later PEC-derived inbox and project control plane
remain deferred.

The redesign must preserve Chirality's authority boundaries, current
shared-runtime ownership, canonical evidence, filesystem/Git project truth,
human gates, and current route/API/SSE compatibility until separately
approved for retirement.

## Parsed action envelope

| Action | Type | Entity | Requested change | Gate-1 disposition |
|---|---|---|---|---|
| A001 | MODIFY | `OBJ-001` | Restate the UI objective around governed artifact work, semantic operator state, and bounded agent supervision without fixing PORTAL/WORKBENCH/PIPELINE as the permanent primary taxonomy. | VALID |
| A002 | MODIFY | `SOW-001` | Replace fixed three-surface navigation and the already-false “current baseline preserved” note with an artifact-centred shell and compatibility requirement. | VALID |
| A003 | MODIFY | `SOW-004`, `SOW-006`, `SOW-007`, `SOW-008` | Preserve professional layout, local state, Workbench/Pipeline functions, and toolkit controls while decoupling them from fixed route/pane presentation. | VALID |
| A004 | MODIFY | `SOW-005` | Reassess canonical matrix presentation and routing; exact modification or non-destructive retirement is deferred to owner concept selection. | VALID_WITH_DEFERRED_FINAL_TYPE |
| A005 | MODIFY | `PKG-02` | Retain the package and redefine its scope around the Workroom shell, artifact navigation/canvas, operator state, compatibility, and local UI state. | VALID |
| A006 | MODIFY | `DEL-02-01`, `DEL-02-02`, `DEL-02-04` | Reframe existing UI deliverables for the selected shell, re-hosted Workbench/Pipeline functions, and versioned layout state without adding topology. | VALID |
| A007 | MODIFY | `DEL-05-04` | Extend the existing replay/transcript view responsibility only enough to support a rebuildable, evidence-linked Agent Room projection. | VALID |
| A008 | MODIFY | `DEL-08-02` | Reassess persona/matrix routing presentation; exact modification or non-destructive retirement is deferred to owner concept selection. | VALID_WITH_DEFERRED_FINAL_TYPE |
| A009 | MODIFY | `DEL-08-03` | Preserve DECOMP/PREP/TASK/AUDIT dispatch semantics while decoupling them from the current selector presentation. | VALID |

No `ADD`, `RECLASSIFY`, `MERGE`, `SPLIT`, package move, or deliverable
renumbering is requested at Gate 1. If concept selection later requires a new
stable deliverable or changes the 10-package/51-deliverable topology, the
amendment returns to Gates 1–2 for explicit owner approval.

## Validation

- Every named objective, SOW row, package, and deliverable exists.
- All 15 deliverables in the three affected packages, including the eight
  action-envelope deliverables, have matching folders and valid contexts.
- No stable ID collision or parent-closure issue exists.
- The requested change is contract-level because it changes accepted product
  information architecture and acceptance semantics, but it does not change
  the decomposition ontology.
- The current code/decomposition divergence is disclosed, not ratified.
- The current shared runtime, provider boundary, and project authority remain
  unchanged.

## Warnings carried to Gate 2

1. Live routes use loop-first shells while accepted decomposition retains the
   three-surface/matrix vocabulary.
2. `DEL-02-02` and `DEL-08-03` overlap on `SOW-007`.
3. `DEL-02-05` traceability omits `SOW-023`.
4. The coverage audit records 15 folder-local artifact-index warnings rather
   than inferring source-code ownership outside deliverable folders.
5. `DEL-02-03` retains render/edge-evidence gaps.
6. `DEL-02-05` and `DEL-05-04` Remaining records lag merged shared-runtime
   evidence.
7. `SOW-005` and `DEL-08-02` cannot be finally dispositioned before concept
   selection.

## Explicit exclusions

- Runtime API or capability expansion.
- Arbitrary multi-agent graph creation or multi-child execution.
- Automatic scheduling, model routing, or residency changes.
- PEC decision inbox or project-control-plane implementation.
- Deletion or retirement of the current UI.
- Route, query, API, or SSE breaking changes.
- Release, publication, professional reliance, or lifecycle advancement.

## Gate-1 question

Does this parsed action envelope accurately express the intended frontend
information-architecture change?

**Owner response:** Confirmed on 2026-07-23.
