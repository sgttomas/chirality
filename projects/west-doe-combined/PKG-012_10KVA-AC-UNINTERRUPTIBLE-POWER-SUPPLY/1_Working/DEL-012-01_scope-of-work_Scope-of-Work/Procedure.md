# Procedure: DEL-012-01_scope-of-work — Scope of Work

## Purpose

Define the controlled procedure for producing and checking the EPC Integrator Scope of Work for `PKG-012`, the 10KVA AC UNINTERRUPTIBLE POWER SUPPLY package.

## Prerequisites

- Accepted Gate 7 final published PROJECT_DECOMP snapshot dated 2026-05-24.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook Packages row 14 from `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- Gate 7 `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `SCOPE_LEDGER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md` during PREPARATION.

## Steps

1. Confirm deliverable identity.
   - Verify the deliverable ID is `DEL-012-01_scope-of-work`.
   - Verify the parent package is `PKG-012`.
   - Verify the package name is 10KVA AC UNINTERRUPTIBLE POWER SUPPLY.

2. Confirm source basis.
   - Read Workbook Packages row 14.
   - Confirm workbook ID 12, WBS 02, CoA tracking number 26020-02-30-003, discipline Electrical, and interface `X` marks.
   - Read the Gate 7 package, deliverable, scope, artifact, interface, and objective mapping rows for `PKG-012` and `DEL-012-01_scope-of-work`.

3. Define the responsibility boundary.
   - State that the Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package.
   - State that the EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

4. Define package scope content.
   - Include package identity and tagged equipment basis.
   - Include package function and whole-facility integration narrative.
   - Mark unavailable tag numbers, load details, runtime, battery type, enclosure data, and other unsupported technical details as `TBD`.

5. Define interface topics.
   - Include Electrical Power.
   - Include Grounding / Bonding.
   - Include Maintenance Access.
   - Include Structural / Foundations / Supports.
   - For each interface, identify the downstream information needed for package datasheet, construction work package, vendor design, vendor documentation, and EPC acceptance.

6. Define required records.
   - Package scope of work.
   - Tagged equipment and package identity list.
   - Package function and integration narrative.
   - Responsibility assignment record.
   - `TBD` / human-ruling list for unresolved technical criteria.

7. Perform consistency checks.
   - Confirm Datasheet identity fields match Specification scope and Procedure prerequisites.
   - Confirm each Specification requirement has a verification hook.
   - Confirm Guidance does not overstate unsupported source detail.
   - Confirm all unsupported technical details are shown as `TBD` or human-ruling items.

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity check | Deliverable and package identifiers match `_CONTEXT.md`, Workbook Packages row 14, and Gate 7 registers. |
| Interface check | The four workbook-marked interface categories are present and consistently named. |
| Responsibility check | Vendor and EPC Integrator responsibilities match the accepted Gate 7 responsibility model. |
| Source-fidelity check | No unsupported UPS technical values are invented. |
| Dependency check | No advisory blocker is present from declared upstream dependency edges. |
| Cross-document check | Datasheet, Specification, Guidance, and Procedure use consistent terminology and values. |

## Records

- Completed `Datasheet.md`.
- Completed `Specification.md`.
- Completed `Guidance.md`, including human-ruling conflict table.
- Completed `Procedure.md`.
- Updated `_STATUS.md` showing `INITIALIZED`.
- TASK run record under `_run_records/`.
