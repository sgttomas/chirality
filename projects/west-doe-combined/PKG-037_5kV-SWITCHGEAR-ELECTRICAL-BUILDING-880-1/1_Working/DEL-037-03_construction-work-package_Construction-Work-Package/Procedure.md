# Procedure: DEL-037-03_construction-work-package

## Purpose

Operational steps to produce and execute the Construction Work Package for `PKG-037` (5kV SWITCHGEAR ELECTRICAL BUILDING, 880-1), covering authorship of the construction package documents and the field execution they govern. The procedure spans both producing the deliverable artifacts and executing the install/tie-in/turnover work.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot present at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md` populated by PREPARATION.
- Access to DBM-Deepcut source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (electrical buildings, electrical design basis, grounding sections).
- Companion package deliverables under development or accepted:
  - `DEL-037-01_scope-of-work` (Scope of Work).
  - `DEL-037-02_package-datasheet` (Package Datasheet).
  - `DEL-037-04_vendor-engineered-equipment-package` (Vendor Engineered Equipment Package).
- Declared upstream dependencies: none (per `_DEPENDENCIES.md`); confirm declared coordination mode is DECLARED before execution.

## Steps

### Authoring the Construction Work Package

1. Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the Gate 7 registers (`DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`) for `PKG-037` / `DEL-037-03`.
2. Read the DBM electrical buildings, electrical design basis, and grounding/bonding sections from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
3. Draft the Construction Work Package narrative covering: building set, foundations, bottom-entry cable provisions, grounding, HVAC commissioning, and door/access provisions, grounded in the DBM source slices.
4. Draft the installation and tie-in workface plan covering all twelve interface facts in `INTERFACE_REGISTER.csv` rows for `PKG-037`. Assign each interface to a responsible discipline-tie-in coordinator.
5. Draft the construction interface and turnover checklist with line items for: foundation/pile inspection, building set, bottom-entry cable provisions, ground-grid two-point connections, ground-well installation, HVAC functional check (n+1), door/transom access verification, GFI receptacle installation, and TECK/ACIC/EMT installation inspection.
6. Mark unresolved scope (lift plans, manpower loading, plot coordinates, detailed schedule, 5 kV bus rating/lineup) as `TBD` and add open items to the Conflict Table in `Guidance.md` for human ruling where they affect cross-document consistency.

### Field execution

7. Verify civil/structural readiness: piles installed and accepted; under-building tray space established; site drainage and grading complete around the building footprint.
8. Verify ground grid present at the building footprint with planned ground-well locations.
9. Receive and inspect the delivered prefabricated electrical building from the Package Vendor; record any transport damage.
10. Set the building on the prepared pile foundation; verify level, anchorage, and bottom-entry openings.
11. Execute tie-ins in coordinated sequence against the interface checklist (Utility Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports).
12. Connect major housed equipment to the facility ground grid at two points; install ground wells with bolted test points; install above-grade green insulated ground conductors in PVC conduit where mechanical protection is required, with compression connections.
13. Commission HVAC and verify n+1 redundancy by simulated unit shutdown.
14. Install/verify TECK/ACIC cabling, EMT between adjacent panels, and an exterior GFI receptacle.
15. Verify doors/transom sections accommodate removal of the largest housed equipment.
16. Complete the turnover checklist, attach grounding test records and HVAC functional check records, and route the package for EPC vendor package review and acceptance under `DEL-037-06`.

## Verification

- Identity check: deliverable identity fields match `DELIVERABLE_REGISTER.csv` row `DEL-037-03_construction-work-package` and `PACKAGE_REGISTER.csv` row `PKG-037`.
- Interface coverage check: each of the twelve `INTERFACE_REGISTER.csv` rows for `PKG-037` has an assigned tie-in line item.
- Source fidelity check: each substantive installation requirement cites a DBM source slice or is marked `TBD`.
- Field inspection check: foundation, building set, bottom-entry, grounding (two-point + ground wells), HVAC (n+1), and access verifications are signed by the EPC Integrator construction lead.
- Cross-document consistency check: package name, IDs, interface list, and `TBD` items match across `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`.

## Records

- Construction work package narrative document.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist (signed).
- Grounding installation test records.
- HVAC functional check records (including n+1 verification).
- Open-items / `TBD` register and Conflict Table entries surfaced for human ruling.
- Run record at `{ScopePath}/_run_records/TASK_RUN_2026-05-24_1910.md`.
