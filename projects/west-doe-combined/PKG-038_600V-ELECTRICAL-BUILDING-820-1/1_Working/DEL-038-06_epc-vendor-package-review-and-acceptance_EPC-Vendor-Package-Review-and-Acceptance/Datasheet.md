# Datasheet: DEL-038-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-038-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Type | EPC Vendor Package Acceptance | `DELIVERABLE_REGISTER.csv` |
| ParentPackageID | `PKG-038` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package Name | 600V ELECTRICAL BUILDING (820-1) | Workbook Packages row 40; `PACKAGE_REGISTER.csv` |
| Workbook Row | 40 | `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-01-30-029 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Responsible Party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers Scope Items | `SOW-0039` | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Supports Objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable role | EPC-integrator-side review, integration acceptance, and handoff-readiness evidence for the vendor-supplied `PKG-038` 600V Electrical Building (820-1) package. | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |
| Acceptance basis | EPC Scope of Work (`DEL-038-01`), Package Datasheet (`DEL-038-02`), and Construction Work Package (`DEL-038-03`). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Anticipated artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Coordination mode | DECLARED | `_DEPENDENCIES.md` |
| Declared upstream | None declared during PREPARATION. | `_DEPENDENCIES.md` |
| Declared downstream | None declared during PREPARATION. | `_DEPENDENCIES.md` |
| Applicable interfaces (package) | Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` rows for `PKG-038` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Responsibility split | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility-level integration, tie-ins, constructability, procurement/construction coordination, and facility integration. | `PACKAGE_REGISTER.csv` row `PKG-038` |
| Source set for acceptance criteria | EPC Scope of Work for `PKG-038` (in-project draft `DEL-038-01`, status per its own `_STATUS.md`); Package Datasheet `DEL-038-02` (in-project, status per its own `_STATUS.md`); Construction Work Package `DEL-038-03` (in-project, status per its own `_STATUS.md`); applicable Gate 7 registers. External EPC SoW reference not present in accessible source set at acceptance-criteria fidelity. | `_REFERENCES.md`; `_CONTEXT.md` |
| Vendor deliverables to be reviewed | Vendor package design documentation, building general-arrangement and equipment-layout drawings, 600V switchgear/MCC/panelboard data, building electrical single-line, grounding and bonding details, lighting and receptacle layouts, fire & gas / safety system integration data, HVAC and ventilation interface data, factory test records, installation/operation manuals, spare parts and warranty data (item set TBD pending vendor data list). | ASSUMPTION grounded in deliverable type `EPC Vendor Package Acceptance` and 600V electrical-building package context (`PACKAGE_REGISTER.csv` row `PKG-038`); specific item list pending vendor data. |
| 600V electrical-building service basis (package-level) | TBD — accessible sources do not define the 600V electrical building's nominal/maximum design voltage, lineup configuration, distribution bus rating, short-circuit interrupting rating, MCC/panelboard count, control voltage, building dimensions, structural/foundation loads, HVAC capacity, or fire & gas configuration at the level needed for acceptance criteria; carry as `TBD` until vendor data and accepted EPC SoW/Datasheet are available. | DBM electrical context (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`); `PACKAGE_REGISTER.csv` |

## Construction

| Element | Value | Source |
|---|---|---|
| Production unit | Single deliverable folder under `PKG-038/1_Working`. | `_CONTEXT.md` |
| Document set | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, plus deliverable-local metadata. | Skill contract `four-documents`; this run. |
| Acceptance evidence container | Vendor document review log + acceptance checklist + test/inspection evidence + turnover evidence (file shapes TBD until EPC procedure is confirmed). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Status gate (this run) | `OPEN` → `INITIALIZED` on successful Pass 1+2. | `_STATUS.md`; `four-documents/SKILL.md` Step 7 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- Gate 7 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `PACKAGE_REGISTER.csv` row `PKG-038`
  - `DELIVERABLE_REGISTER.csv` row `DEL-038-06_epc-vendor-package-review-and-acceptance`
  - `INTERFACE_REGISTER.csv` rows for `PKG-038`
  - `SCOPE_LEDGER.csv` row `SOW-0039`
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
- Workbook Packages row 40: `_Sources/26020-Packages_Interfaces_4_export.xlsx`
- Companion deliverables: `DEL-038-01_scope-of-work`, `DEL-038-02_package-datasheet`, `DEL-038-03_construction-work-package`, `DEL-038-04_vendor-engineered-equipment-package`, `DEL-038-05_vendor-document-turnover-package`.
- DBM electrical context: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- EPC Scope of Work external reference, Construction Work Package detail, and vendor data package: not present in accessible source set at production-document fidelity — `location TBD`.
