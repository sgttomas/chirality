# Datasheet: DEL-074-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-074-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Type | EPC Vendor Package Acceptance | `DELIVERABLE_REGISTER.csv` |
| ParentPackageID | `PKG-074` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package Name | Caustic Treating (NGL Mercaptan Removal) | Workbook Packages row 51; `PACKAGE_REGISTER.csv` |
| Workbook Row | 51 | `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-01-27-002 | `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Responsible Party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers Scope Items | `SOW-0059`, `SOW-0060`, `SOW-0061`, `SOW-0062` | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |
| Supports Objectives | `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable role | EPC-integrator-side review, integration acceptance, and handoff-readiness evidence for the vendor-supplied `PKG-074` Caustic Treating (NGL Mercaptan Removal) package. | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |
| Acceptance basis | EPC Scope of Work, Package Datasheet (`DEL-074-02`), and Construction Work Package (`DEL-074-03`). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Anticipated artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Coordination mode | DECLARED | `_DEPENDENCIES.md` |
| Declared upstream | None declared during PREPARATION. | `_DEPENDENCIES.md` |
| Declared downstream | None declared during PREPARATION. | `_DEPENDENCIES.md` |
| Applicable interfaces (package) | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` rows for `PKG-074` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Responsibility split | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-074` |
| Process service basis | Caustic treating system for NGL/C3+ mercaptan removal located immediately downstream of the deethanizer. | `PACKAGE_REGISTER.csv` row `PKG-074` ScopeDescription |
| Source set for acceptance criteria | EPC Scope of Work for `PKG-074` (TBD — not in accessible source set at acceptance-criteria fidelity); Package Datasheet `DEL-074-02` (in-project, status per its own `_STATUS.md`); Construction Work Package `DEL-074-03` (in-project; status per its own `_STATUS.md`); applicable Gate 7 registers. | `_REFERENCES.md`; `_CONTEXT.md` |
| Vendor deliverables to be reviewed | Vendor process and mechanical design documentation, P&IDs, equipment lists, equipment datasheets (caustic contactors/extractors, regenerators, oxidizers/coalescers/separators as applicable to the vendor design), package general arrangement, materials selection records (caustic-service compatibility), instrumentation and control narrative, PSV/relief sizing basis, hazardous-area classification, FAT/SAT records, installation/operation manuals, spare parts and warranty data (item set TBD pending vendor data list). | ASSUMPTION grounded in deliverable type `EPC Vendor Package Acceptance` and the caustic-treating/mercaptan-removal scope; specific item list pending vendor data. |
| Caustic treating package configuration (package-level) | TBD — accessible sources do not define the caustic-treating process route (e.g., extraction vs. fixed-bed vs. regenerative variants such as Merox-type), reagent concentration, regeneration scheme, oxidation step, disulfide handling, process flow rates, operating pressures/temperatures, materials of construction, hazardous-area classification, or relief philosophy at the level needed for acceptance criteria; carry as `TBD` until vendor data and EPC SoW are accepted. | `PACKAGE_REGISTER.csv` row `PKG-074`; vendor data not in accessible set. |

## Construction

| Element | Value | Source |
|---|---|---|
| Production unit | Single deliverable folder under `PKG-074/1_Working`. | `_CONTEXT.md` |
| Document set | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, plus deliverable-local metadata. | Skill contract `four-documents`; this run. |
| Acceptance evidence container | Vendor document review log + acceptance checklist + test/inspection evidence + turnover evidence (file shapes TBD until EPC procedure is confirmed). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Status gate (this run) | `OPEN` → `INITIALIZED` on successful Pass 1+2. | `_STATUS.md`; `four-documents/SKILL.md` Step 7 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- Gate 7 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `PACKAGE_REGISTER.csv` row `PKG-074`
  - `DELIVERABLE_REGISTER.csv` row `DEL-074-06_epc-vendor-package-review-and-acceptance`
  - `INTERFACE_REGISTER.csv` rows for `PKG-074`
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
- Workbook Packages row 51: `_Sources/26020-Packages_Interfaces_4_export.xlsx` (binary; location TBD for source slice).
- Word package heading 28: `_Sources/26020-Package_Requirements.docx` (binary; location TBD for source slice).
- Companion deliverables: `DEL-074-01_scope-of-work`, `DEL-074-02_package-datasheet`, `DEL-074-03_construction-work-package`, `DEL-074-04_vendor-engineered-equipment-package`, `DEL-074-05_vendor-document-turnover-package`.
- EPC Scope of Work, Construction Work Package detail, and vendor data package: not present in accessible source set at production-document fidelity — `location TBD`.
