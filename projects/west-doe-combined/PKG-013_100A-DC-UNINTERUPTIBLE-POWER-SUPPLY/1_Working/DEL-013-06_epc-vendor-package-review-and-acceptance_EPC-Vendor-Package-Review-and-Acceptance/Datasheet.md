# Datasheet: DEL-013-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-013-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Type | EPC Vendor Package Acceptance | `DELIVERABLE_REGISTER.csv` |
| ParentPackageID | `PKG-013` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package Name | 100A DC UNINTERUPTIBLE POWER SUPPLY | Workbook Packages row 15; `PACKAGE_REGISTER.csv` |
| Workbook Row | 15 | `PACKAGE_REGISTER.csv` |
| WBS | 02 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-02-30-004 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Responsible Party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers Scope Items | `SOW-0014` | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable role | EPC-integrator-side review, integration acceptance, and handoff-readiness evidence for the vendor-supplied `PKG-013` package. | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |
| Acceptance basis | EPC Scope of Work, Package Datasheet (`DEL-013-02`), and Construction Work Package. | `_CONTEXT.md` |
| Anticipated artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Coordination mode | DECLARED | `_DEPENDENCIES.md` |
| Declared upstream | None declared during PREPARATION. | `_DEPENDENCIES.md` |
| Declared downstream | None declared during PREPARATION. | `_DEPENDENCIES.md` |
| Applicable interfaces (package) | Electrical Power; Grounding / Bonding; Maintenance Access; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` rows for `PKG-013` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Responsibility split | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility-level integration, tie-ins, constructability, procurement/construction coordination, and facility integration. | `PACKAGE_REGISTER.csv` row `PKG-013` |
| Source set for acceptance criteria | EPC Scope of Work for `PKG-013` (TBD — not in accessible source set); Package Datasheet `DEL-013-02` (in-project, draft); Construction Work Package for `PKG-013` (TBD — not in accessible source set); applicable Gate 7 registers. | `_REFERENCES.md`; `_CONTEXT.md` |
| Vendor deliverables to be reviewed | Vendor design documentation, certified drawings, FAT records, installation/operation manuals, spare parts and warranty data (item set TBD pending vendor data list). | ASSUMPTION grounded in deliverable type `EPC Vendor Package Acceptance` and anticipated artifacts. |
| UPS service basis (package-level) | TBD — accessible sources do not define 100A DC UPS package rating, voltage, autonomy, charger, or distribution configuration. | DBM electrical slices (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`); `PACKAGE_REGISTER.csv` |

## Construction

| Element | Value | Source |
|---|---|---|
| Production unit | Single deliverable folder under `PKG-013/1_Working`. | `_CONTEXT.md` |
| Document set | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, plus deliverable-local metadata. | Skill contract `four-documents`; this run. |
| Acceptance evidence container | Vendor document review log + acceptance checklist + test/inspection evidence + turnover evidence (file shapes TBD until EPC procedure is confirmed). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Status gate (this run) | `OPEN` → `INITIALIZED` on successful Pass 1+2. | `_STATUS.md`; `four-documents/SKILL.md` Step 7 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- Gate 7 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `PACKAGE_REGISTER.csv` row `PKG-013`
  - `DELIVERABLE_REGISTER.csv` row `DEL-013-06_epc-vendor-package-review-and-acceptance`
  - `INTERFACE_REGISTER.csv` rows for `PKG-013`
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
- Workbook Packages row 15: `_Sources/26020-Packages_Interfaces_4_export.xlsx`
- Companion deliverable: `DEL-013-02_package-datasheet` (Package Datasheet)
- DBM electrical context: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (used by `DEL-013-02` for electrical service basis)
- EPC Scope of Work, Construction Work Package, and vendor data package: not present in accessible source set — `location TBD`.
