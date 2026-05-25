# Procedure: DEL-005-01_scope-of-work - Scope of Work

## Purpose

This procedure describes how to produce and verify the `DEL-005-01_scope-of-work` document for `PKG-005 Site Grading` using the accepted Gate 7 decomposition snapshot and locally accessible source basis.

## Prerequisites

- Current deliverable state permits writing. For this run, `_STATUS.md` was `OPEN`.
- Accepted decomposition truth is available at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Deliverable-local context files are available: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`.
- DBM 03-25 source is available at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- Declared upstream dependencies: none.
- Declared downstream dependencies: none.

## Steps

1. Confirm identity from `_CONTEXT.md` and Gate 7 registers.
   - Verify deliverable ID `DEL-005-01_scope-of-work`.
   - Verify parent package `PKG-005`, package name `Site Grading`, discipline `Civil`, WBS `03`, and responsible party `EPC Integrator`.

2. Confirm governed scope and objective context.
   - Read Gate 7 `SCOPE_LEDGER.csv` row `SOW-0005`.
   - Read Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-005-01_scope-of-work`.
   - Read Gate 7 `PROJECT_DECOMP.md` objective text for OBJ-002, OBJ-007, OBJ-008, and OBJ-009.
   - Treat objective association as context unless the deliverable row explicitly supports a requirement.

3. Build the package identity and artifact list.
   - Read Gate 7 `DELIVERABLE_REGISTER.csv` row for `DEL-005-01_scope-of-work`.
   - Read Gate 7 `ARTIFACT_REGISTER.csv` rows for `DEL-005-01_scope-of-work`.
   - Include package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record.
   - Mark tagged equipment details as `TBD` unless a source-supported tagged equipment list is available.

4. Build the interface narrative.
   - Read Gate 7 `INTERFACE_REGISTER.csv` rows for `PKG-005`.
   - Include `Drain / Containment` and `Grading / Site Drainage / Spill Containment`.
   - Do not add undeclared interface types as authoritative scope.

5. Add civil and drainage source context.
   - Read DBM 03-25 `SEC-11 - Layout Basis`, `Site and Civil Conditions`, and `Surface Water and Drainage`.
   - Include surface-water collection, segregation, retention, process-area protection, construction and operations access, and contaminated-drainage routing to appropriate drain or containment systems.
   - Keep detailed design values outside the Scope of Work unless needed for boundary clarity.

6. Add maturity and open-item controls.
   - Read DBM 03-25 `SEC-02` rainfall/geotechnical source slices and `SEC-15` regulatory source slices.
   - Preserve final hydrology inputs, final geotechnical report, civil drawings/equipment layout, and detailed regulatory review as `TBD` where source material is not available.

7. Cross-check against sibling deliverable boundaries.
   - Confirm the Scope of Work does not replace the package datasheet (`DEL-005-02`), construction work package (`DEL-005-03`), or EPC/Civil discipline production package (`DEL-005-04`).
   - Keep downstream handoff requirements clear enough for those documents to consume.

8. Perform cross-document consistency checks.
   - Confirm terminology is consistent across `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`.
   - Confirm all non-trivial values and requirements cite Gate 7 registers or DBM source sections.
   - Confirm unsupported items are labeled `TBD`, **ASSUMPTION**, or captured in the Conflict Table.

## Verification

| Check | Expected result |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` exist in the deliverable folder. |
| Default sections exist | Datasheet includes Identification, Attributes, Conditions, Construction, References; Specification includes Scope, Requirements, Standards, Verification, Documentation; Guidance includes Purpose, Principles, Considerations, Trade-offs, Examples; Procedure includes Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Package identity and interfaces trace to Gate 7 registers; civil/drainage/geotechnical/regulatory context traces to DBM 03-25 sections. |
| Dependency handling | No blockers are asserted because no declared upstream dependencies exist. |
| Open items | Unsupported exclusions, final hydrology, final geotechnical report, civil drawing/equipment layout, and detailed regulatory deliverables remain `TBD` or Human Ruling Required. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_2026-05-24_1640.md`
