# Procedure: DEL-008-01_scope-of-work — Scope of Work

## Purpose

Define the working procedure for producing and checking the DEL-008-01 Scope of Work for the PKG-008 Controls system design and integration package.

## Prerequisites

- Accepted upstream decomposition truth: Gate 7 final published PROJECT_DECOMP snapshot dated 2026-05-24.
- Deliverable-local context files: _CONTEXT.md, _REFERENCES.md, _DEPENDENCIES.md, and _STATUS.md.
- Declared dependency status: no upstream or downstream dependencies declared during PREPARATION.
- Current workflow status allowing write: OPEN or INITIALIZED.
- Source limitation acknowledged: no deliverable-specific source slices were copied during PREPARATION; use the Gate 7 snapshot and local context as accepted upstream truth for this run.

## Steps

1. Confirm deliverable identity from _CONTEXT.md:
   - DEL-008-01_scope-of-work.
   - PKG-008 Controls system design and integration.
   - Discipline Controls.
   - Type EPC Scope of Work.
   - Responsible party EPC Integrator.

2. Confirm Gate 7 register basis:
   - Read PACKAGE_REGISTER.csv row PKG-008.
   - Read DELIVERABLE_REGISTER.csv row DEL-008-01_scope-of-work.
   - Read ARTIFACT_REGISTER.csv rows for DEL-008-01_scope-of-work.
   - Read INTERFACE_REGISTER.csv rows for PKG-008.
   - Read objective mapping rows for DEL-008-01_scope-of-work as context.

3. Populate the Scope of Work content:
   - Identify WBS 01 and CoA tracking number 26020-01-32-001.
   - State package scope as a workbook-defined Controls package for controls system design and integration.
   - Include the anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record.
   - Include accepted interface types: Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems.
   - Preserve the source-dependent responsibility model.

4. Apply source-fidelity controls:
   - Mark package-specific exclusions as TBD.
   - Mark detailed design values, detailed tagged equipment, clause-level controls requirements, and detailed standards as TBD unless supported by accepted snapshot data.
   - Do not reinterpret raw source corpus during this Phase 2.2 run.

5. Resolve interface treatment:
   - Record that controls power-panel interfaces remain interface facts/artifacts under the package datasheet.
   - Do not create a separate controls power-panel package or deliverable.

6. Check cross-document consistency:
   - Datasheet identity fields match Specification requirements.
   - Specification requirements have Procedure verification hooks.
   - Guidance rationale does not overstate accepted snapshot data.
   - TBDs are used consistently for missing technical detail.
   - Human ruling items are carried in the Guidance conflict table.

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity check | Deliverable ID, package ID, package name, WBS, CoA tracking number, discipline, type, and responsible party match _CONTEXT.md and Gate 7 registers. |
| Artifact check | All four anticipated artifacts for DEL-008-01 are represented. |
| Interface check | All eight PKG-008 interface types are listed consistently. |
| Source-fidelity check | Unsupported detail is marked TBD or ASSUMPTION and not converted into requirements. |
| Human-ruling check | Responsibility ambiguity and controls power-panel tracking disposition are visible in the Conflict Table. |
| Dependency check | No blockers are asserted because no declared upstream dependencies exist. |

## Records

Retain the following records with the deliverable:

- Datasheet.md.
- Specification.md.
- Guidance.md, including Conflict Table entries.
- Procedure.md.
- _STATUS.md state history.
- TASK run record in _run_records/.
- Future human rulings or source-verification outputs, if produced by later workflows.
