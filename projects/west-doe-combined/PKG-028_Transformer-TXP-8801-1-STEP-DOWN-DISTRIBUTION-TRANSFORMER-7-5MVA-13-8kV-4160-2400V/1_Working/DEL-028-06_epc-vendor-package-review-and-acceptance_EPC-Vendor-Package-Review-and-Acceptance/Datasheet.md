# Datasheet: DEL-028-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-028-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Type | EPC Vendor Package Acceptance | `DELIVERABLE_REGISTER.csv` |
| ParentPackageID | `PKG-028` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package Name | Transformer TXP-8801-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 7.5MVA 13.8kV/4160/2400V | Workbook Packages row 30; `PACKAGE_REGISTER.csv` |
| Workbook Row | 30 | `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-01-30-019 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Responsible Party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers Scope Items | `SOW-0029` | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |
| Supports Objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable role | EPC-integrator-side review, integration acceptance, and handoff-readiness evidence for the vendor-supplied `PKG-028` step-down distribution transformer (TXP-8801-1, 7.5 MVA, 13.8 kV / 4160 / 2400 V). | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |
| Acceptance basis | EPC Scope of Work, Package Datasheet (`DEL-028-02`), and Construction Work Package (`DEL-028-03`). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Anticipated artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Coordination mode | DECLARED | `_DEPENDENCIES.md` |
| Declared upstream | None declared during PREPARATION. | `_DEPENDENCIES.md` |
| Declared downstream | None declared during PREPARATION. | `_DEPENDENCIES.md` |
| Applicable interfaces (package) | Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` rows for `PKG-028` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Responsibility split | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility-level integration, tie-ins, constructability, procurement/construction coordination, and facility integration. | `PACKAGE_REGISTER.csv` row `PKG-028` |
| Source set for acceptance criteria | EPC Scope of Work for `PKG-028` (TBD — not in accessible source set); Package Datasheet `DEL-028-02` (in-project, status per its own `_STATUS.md`); Construction Work Package `DEL-028-03` (in-project; status per its own `_STATUS.md`); applicable Gate 7 registers. | `_REFERENCES.md`; `_CONTEXT.md` |
| Vendor deliverables to be reviewed | Vendor design documentation, certified drawings (general arrangement, nameplate, schematic, BIL/insulation coordination), FAT records, installation/operation/maintenance manuals, factory test reports (routine, type, and special tests as applicable), spare parts and warranty data (item set TBD pending vendor data list). | ASSUMPTION grounded in deliverable type `EPC Vendor Package Acceptance` and step-down distribution transformer context. |
| Transformer service basis (package-level) | TBD — accessible sources do not define the 7.5 MVA / 13.8 kV / 4160 V / 2400 V transformer's winding configuration, vector group, cooling class, tap-changer arrangement, BIL, impedance, accessories, or enclosure type at the level needed for acceptance criteria; carry as `TBD` until vendor data and EPC SoW are accepted. | DBM electrical context (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`); `PACKAGE_REGISTER.csv` |

## Construction

| Element | Value | Source |
|---|---|---|
| Production unit | Single deliverable folder under `PKG-028/1_Working`. | `_CONTEXT.md` |
| Document set | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, plus deliverable-local metadata. | Skill contract `four-documents`; this run. |
| Acceptance evidence container | Vendor document review log + acceptance checklist + test/inspection evidence + turnover evidence (file shapes TBD until EPC procedure is confirmed). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Status gate (this run) | `OPEN` → `INITIALIZED` on successful Pass 1+2. | `_STATUS.md`; `four-documents/SKILL.md` Step 7 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- Gate 7 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `PACKAGE_REGISTER.csv` row `PKG-028`
  - `DELIVERABLE_REGISTER.csv` row `DEL-028-06_epc-vendor-package-review-and-acceptance`
  - `INTERFACE_REGISTER.csv` rows for `PKG-028`
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
- Workbook Packages row 30: `_Sources/26020-Packages_Interfaces_4_export.xlsx`
- Companion deliverables: `DEL-028-01_scope-of-work`, `DEL-028-02_package-datasheet`, `DEL-028-03_construction-work-package`, `DEL-028-04_vendor-engineered-equipment-package`, `DEL-028-05_vendor-document-turnover-package`.
- DBM electrical context: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- EPC Scope of Work, Construction Work Package detail, and vendor data package: not present in accessible source set at production-document fidelity — `location TBD`.
