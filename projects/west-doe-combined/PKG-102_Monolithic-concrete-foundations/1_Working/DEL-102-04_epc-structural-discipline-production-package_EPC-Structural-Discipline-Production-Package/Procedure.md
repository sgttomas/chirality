# Procedure: DEL-102-04 — EPC / Structural Discipline Production Package

## Purpose

Produce the EPC/Structural discipline production unit artifacts for PKG-102 (Monolithic concrete foundations), under WBS 01, in a manner that preserves source fidelity and explicitly records source-limited gaps for Gate 5 disposition.

## Prerequisites

- **Declared upstream dependencies:** None declared during PREPARATION (`_DEPENDENCIES.md`).
- **Required references (locally accessible):**
  - `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (this deliverable folder)
  - Gate 7 PROJECT_DECOMP snapshot under `/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`, specifically `DELIVERABLE_REGISTER.csv` row DEL-102-04, `PACKAGE_REGISTER.csv` PKG-102, `ARTIFACT_REGISTER.csv` PKG-102 rows, `INTERFACE_REGISTER.csv` PKG-102 rows
- **Required references (deferred — to be obtained before R-09 can close):**
  - Workbook Packages row 103 slice from `_Sources/26020-Package_Requirements.docx`
  - DBM-Deepcut/4-25_Deepcut_DBM.md structural slice for PKG-102
- **Responsibility assignment:** Confirmation of EPC Integrator vs. discipline subcontractor by the human authority (PMO/EPC Integrator). ASSUMPTION until confirmed.

## Steps

1. **Confirm scope and identity.** Cross-check `_CONTEXT.md` against `DELIVERABLE_REGISTER.csv` row DEL-102-04 and `PACKAGE_REGISTER.csv` PKG-102. Record any discrepancy in the Guidance Conflict Table.
2. **Obtain source slices (deferred reference resolution).** Pull workbook row 103 and DBM-Deepcut PKG-102 slices into the deliverable folder or an authorized shared location, and update `_REFERENCES.md` to mark them accessible. If unavailable: continue with TBD posture.
3. **Author the discipline production package basis (ART-5C2432867E).** Capture: (a) package identity and scope from `_CONTEXT.md`/registers; (b) structural design assumptions explicitly labeled ASSUMPTION; (c) interface matrix referencing `INTERFACE_REGISTER.csv` PKG-102 rows; (d) responsibility-assignment placeholder. Cite every non-trivial claim. Mark TBD where source is missing.
4. **Compile the TBD discipline deliverable register.** Enumerate anticipated structural sub-deliverables (e.g., foundation design package, rebar schedule, concrete mix specification, geotechnical interface record) — TBD: do not commit to a sub-deliverable list not supported by source. Record each row with `Status=TBD-Pending-Source` and the source it would require.
5. **Produce the source-limited requirements closure record (ART-712FAD4E91).** For each requirement in Specification R-01..R-09, record: current source basis, accessibility status, gap statement, and disposition route (Gate 5 ruling, source acquisition, or human authority).
6. **Cross-document consistency sweep.** Confirm Datasheet, Specification, Guidance, Procedure share consistent terminology, ReqIDs, ArtifactIDs, InterfaceIDs, and values; update the Guidance Conflict Table for residual discrepancies.
7. **Human-authority handoff.** Route responsibility-assignment confirmation (R-07), objective-mapping confirmation (R-08), and source-acquisition disposition (R-09) to the human authority. Do not self-resolve.
8. **Record run evidence.** Append a run record under `_run_records/` documenting source rereads (Pass 3, when applicable) and disposition decisions.

## Verification

| Step | Verification |
|---|---|
| 1 | Identity/scope cross-check produces no unresolved deltas, or deltas are captured in the Conflict Table. |
| 2 | `_REFERENCES.md` updated; or, if unavailable, the unavailability is reflected in the closure record (Step 5). |
| 3 | ART-5C2432867E exists and every non-trivial claim cites a source or is marked TBD/ASSUMPTION. |
| 4 | Discipline deliverable register exists; no sub-deliverables claimed without source backing. |
| 5 | ART-712FAD4E91 exists and enumerates every Specification gap with provenance and disposition route. |
| 6 | Consistency sweep produces no contradictions or all are captured in the Conflict Table. |
| 7 | Human-authority routing evidence exists (referral note, email, or PMO record). |
| 8 | Run record present under `_run_records/`. |

## Records

- `ART-5C2432867E` — Discipline production package basis (this deliverable folder).
- `ART-712FAD4E91` — Source-limited requirements closure record (this deliverable folder).
- TBD discipline deliverable register (this deliverable folder; filename TBD).
- `_run_records/TASK_RUN_*.md` — execution evidence.
- `_STATUS.md` — lifecycle state (safe update only).
- `_REFERENCES.md` — updated when deferred source slices are obtained (out of this skill's write scope; updated by upstream PREPARATION or human edit).
