# Datasheet: DEL-018-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-018-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Type | EPC Vendor Package Acceptance | `DELIVERABLE_REGISTER.csv` |
| ParentPackageID | `PKG-018` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package Name | MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD | Workbook Packages row 20; `PACKAGE_REGISTER.csv` |
| Workbook Row | 20 | `PACKAGE_REGISTER.csv` |
| WBS | 02 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-02-30-009 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Responsible Party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers Scope Items | `SOW-0019` | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable role | EPC-integrator-side review, integration acceptance, and handoff-readiness evidence for the vendor-supplied `PKG-018` MV VFD package. | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |
| Acceptance basis | EPC Scope of Work (`DEL-018-01`), Package Datasheet (`DEL-018-02`), and Construction Work Package (`DEL-018-03`). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Anticipated artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Coordination mode | DECLARED | `_DEPENDENCIES.md` |
| Declared upstream | None declared during PREPARATION. | `_DEPENDENCIES.md` |
| Declared downstream | None declared during PREPARATION. | `_DEPENDENCIES.md` |
| Applicable interfaces (package) | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` rows for `PKG-018` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Responsibility split | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility-level integration, tie-ins, constructability, procurement/construction coordination, and facility integration. | `PACKAGE_REGISTER.csv` row `PKG-018` |
| Source set for acceptance criteria | EPC Scope of Work for `PKG-018` — companion `DEL-018-01` (in-project, draft), original SoW clause set `location TBD`; Package Datasheet `DEL-018-02` (in-project, draft); Construction Work Package `DEL-018-03` (in-project, draft); applicable Gate 7 registers; DBM electrical context. | `_REFERENCES.md`; `_CONTEXT.md` |
| Vendor deliverables to be reviewed | Vendor design documentation, certified drawings, harmonic and reactive-power study results, FAT records, installation/operation manuals, spare parts and warranty data (item set `TBD` pending vendor data list). | ASSUMPTION grounded in deliverable type `EPC Vendor Package Acceptance` and anticipated artifacts. |
| VFD service basis (package-level) | The package serves a starting / inverter-duty role for large 4,000 V three-phase 60 Hz inlet-compressor motors (KM-2150, KM-2250) per the DBM compression basis; SCA-001 VE #34 establishes starting VFDs as the basis, and SCA-001 VE #37 removes capacitor banks from the synchronous bus on MCC-8200 where VFDs are present. Harmonic and reactive-power mitigation is a detailed-design study item. Specific VFD rating, topology, cooling, and enclosure are vendor-defined and `TBD` at the decomposition level until vendor data is received. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (lines 324, 326, 533, 752-760); `PACKAGE_REGISTER.csv` |
| Package name attribute reconciliation | "5000HP, 4160V, 3PH, 60HZ" is the project identifier for the VFD package; the DBM motor basis cites 3,878 kW / 5,200 hp at 4,000 V three-phase 60 Hz inverter-duty. Use the package name as identity; treat the DBM values as the related motor-side design basis. Final VFD-side ratings are vendor-defined and `TBD` until vendor data is accepted. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (lines 324, 533); `PACKAGE_REGISTER.csv` |

## Construction

| Element | Value | Source |
|---|---|---|
| Production unit | Single deliverable folder under `PKG-018/1_Working`. | `_CONTEXT.md` |
| Document set | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, plus deliverable-local metadata. | Skill contract `four-documents`; this run. |
| Acceptance evidence container | Vendor document review log + acceptance checklist + test/inspection evidence + turnover evidence (file shapes `TBD` until EPC procedure is confirmed). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Status gate (this run) | `OPEN` → `INITIALIZED` on successful Pass 1+2. | `_STATUS.md`; `four-documents/SKILL.md` Step 7 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- Gate 7 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `PACKAGE_REGISTER.csv` row `PKG-018`
  - `DELIVERABLE_REGISTER.csv` row `DEL-018-06_epc-vendor-package-review-and-acceptance`
  - `INTERFACE_REGISTER.csv` rows for `PKG-018`
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
- Workbook Packages row 20: `_Sources/26020-Packages_Interfaces_4_export.xlsx`
- Companion deliverables: `DEL-018-01_scope-of-work`, `DEL-018-02_package-datasheet`, `DEL-018-03_construction-work-package`, `DEL-018-04_vendor-engineered-equipment-package`, `DEL-018-05_vendor-document-turnover-package`.
- DBM compression/electrical context: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (motor and 4160V MCC basis).
- EPC Scope of Work and Construction Work Package clause sets external to the project workspace: `location TBD`.
