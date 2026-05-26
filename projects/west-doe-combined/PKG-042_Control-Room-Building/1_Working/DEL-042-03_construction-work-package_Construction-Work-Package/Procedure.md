# Procedure: DEL-042-03 — Construction Work Package (Control Room Building)

**Interpretation:** This procedure describes the steps to **produce** the Construction Work Package deliverable artifact set. Steps to **use** the CWP at construction execution time are out of scope here and belong to the field execution procedures referenced by the CWP itself.

## Prerequisites

- Accepted upstream PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`. (SourceRef: `_REFERENCES.md`.)
- Deliverable-local truth set readable: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`.
- PKG-042 package register row, deliverable register row, scope ledger row SOW-0043, and the eleven INTERFACE_REGISTER.csv rows are accessible.
- ASSUMPTION: Package Vendor inputs from DEL-042-02 (datasheet) and DEL-042-05 (vendor document turnover) will be referenced when available. Construction execution should not start before they mature.
- No declared upstream dependencies were recorded in `_DEPENDENCIES.md` at PREPARATION; declared lists may be added later via `TASK + dependency-extract`.

## Steps

1. **Confirm identity and scope.** Reload `_CONTEXT.md` and the DELIVERABLE_REGISTER.csv row for DEL-042-03; verify ParentPackageID `PKG-042`, scope text, anticipated artifacts, SOW-0043 coverage, and objective list.
2. **Inventory applicable interfaces.** Extract the eleven PKG-042 rows from INTERFACE_REGISTER.csv and assemble the Interface Coverage Matrix; one row per InterfaceID with placeholder columns for tie-in step, prerequisite, responsible craft, inspection, and turnover check. Mark TBD where information is not yet sourced.
3. **Confirm responsibility split.** Capture the PACKAGE_REGISTER.csv ResponsibilityModel verbatim in the CWP narrative to anchor what is and is not in EPC Integrator construction scope.
4. **Draft the Construction Work Package artifact (ART-6AD15AE851).** Sections: package identity; construction scope; responsibility boundary; interface scope (cross-reference Interface Coverage Matrix); standards (mark TBD where not yet confirmed); HSE/QC framework (TBD); sequence and milestones (skeleton; details TBD until vendor data is available); inspection and acceptance approach; turnover approach.
5. **Draft the Installation and Tie-in Workface Plan (ART-9882790698).** For each of the eleven interfaces, produce a workface skeleton: prework, tie-in step, in-process inspection, post-tie-in test, sign-off. Leave craft, durations, lift plans, and termination details TBD until DEL-042-02 / DEL-042-05 are mature.
6. **Draft the Construction Interface and Turnover Checklist.** Itemize per-interface acceptance items, package-level mechanical completion items, system-level energization/tie-in items, and turnover documentation items. Mark TBD where vendor or project standard inputs are needed.
7. **Produce trace evidence.**
   - Interface coverage matrix (covers R-042-03-05).
   - Responsibility traceability table (covers R-042-03-06).
   - Scope/objective trace matrix from CWP sections to SOW-0043 and OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (covers R-042-03-07).
8. **Cross-document consistency check.** Reconcile terminology, interface IDs, artifact IDs, and objective IDs across Datasheet, Specification, Guidance, Procedure, and the produced artifacts. Open Conflict Table entries for unresolved items.
9. **Record open items.** Surface every TBD and ASSUMPTION in a deliverable-local open-items list; do not resolve silently.
10. **Submit for human review.** Production of the CWP artifact set is proposal-only at the EPC Integrator level; binding acceptance is a human decision (K-AUTH-1).

## Verification

- All four documents present in `{DELIVERABLE_PATH}` and contain the default schema sections.
- Three named artifacts (construction work package, installation and tie-in workface plan, construction interface and turnover checklist) are described with placeholders or content; TBDs are explicit and not hidden.
- Interface Coverage Matrix lists all eleven PKG-042 InterfaceIDs.
- Responsibility Traceability Table reflects PACKAGE_REGISTER.csv ResponsibilityModel without modification.
- Scope/objective trace matrix lists SOW-0043 and each of the eight objectives.
- No metadata files other than `_STATUS.md` were modified.
- `_STATUS.md` transitioned from `OPEN` to `INITIALIZED` only if Pass 1/2 ran and prior state was `OPEN`.

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`
- `_STATUS.md` updated entry (OPEN → INITIALIZED)
- `_run_records/TASK_RUN_<timestamp>.md`
- Future: Interface Coverage Matrix, Responsibility Traceability Table, Scope/Objective Trace Matrix (produced when CWP narrative is populated with vendor and project-standard inputs); status of these is currently TBD.
