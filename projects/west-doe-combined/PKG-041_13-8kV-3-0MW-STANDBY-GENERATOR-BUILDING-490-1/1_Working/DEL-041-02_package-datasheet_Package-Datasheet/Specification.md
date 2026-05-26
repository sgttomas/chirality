# Specification: DEL-041-02 — Package Datasheet (PKG-041)

> Normative requirements for the EPC-authored Package Datasheet that hands the 13.8 kV, 3.0 MW Standby Generator Building (490-1) to a third-party package vendor for engineering and design. Requirements are derived from the Gate-07 PROJECT_DECOMP snapshot. Code- and clause-level requirements are marked `ASSUMPTION` or `TBD` because the governing standard texts are not locally accessible.

## Scope

**In scope.** This deliverable specifies the technical handoff data the EPC Integrator must publish for PKG-041 so that a third-party package vendor can perform package engineering, design, and equipment supply. Content includes: package identification; functional duty and ratings; design conditions; equipment list; interface requirements matrix (all twelve workbook interface facts carried here as evidence); and the vendor handoff basis (`ART-1851AF6B89`, `ART-8FF7B18574`, `ART-7F81FF2CB4`, plus twelve `ART-*` interface fact rows under `ParentDeliverableID = DEL-041-02_package-datasheet`).

**Out of scope.**
- Package scope of work narrative and responsibility assignment (owned by `DEL-041-01_scope-of-work`).
- Construction installation, tie-in workface plan, turnover (owned by `DEL-041-03_construction-work-package`).
- Vendor-produced engineering/design/equipment package (owned by `DEL-041-04_vendor-engineered-equipment-package`).
- Vendor document turnover (owned by `DEL-041-05_vendor-document-turnover-package`).
- EPC vendor package review/acceptance (owned by `DEL-041-06_epc-vendor-package-review-and-acceptance`).
- Standalone interface deliverables (intentionally absent per `_CONTEXT.md` Notes; interface facts are evidence here).

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| REQ-DS-01 | The datasheet SHALL identify the package by `PackageID = PKG-041`, `WorkbookID = 41`, `WorkbookRow = 43`, `CoATrackingNumber = 26020-01-30-032`, `WBS = 01`, `Discipline = Electrical`, `Name = "13.8kV, 3.0MW STANDBY GENERATOR BUILDING (490-1)"`. | PACKAGE_REGISTER `PKG-041` |
| REQ-DS-02 | The datasheet SHALL state the responsibility split: Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | PACKAGE_REGISTER `PKG-041` ResponsibilityModel |
| REQ-DS-03 | The datasheet SHALL declare the nominal medium-voltage tie-in as 13.8 kV and nominal capacity as 3.0 MW standby, as stated in the package name. | PACKAGE_REGISTER `PKG-041` Name |
| REQ-DS-04 | The datasheet SHALL enumerate all twelve applicable interface types carried as artifact evidence (`ART-0096A23E12` through `ART-E2472057A2`) under `ParentDeliverableID = DEL-041-02_package-datasheet`, preserving each `IFC-*` ID. | ARTIFACT_REGISTER; INTERFACE_REGISTER |
| REQ-DS-05 | For each interface type listed in REQ-DS-04, the datasheet SHALL provide a battery-limit description, tie-point reference, and sizing/loading parameters sufficient for vendor engineering. Where the source value is not available, the entry SHALL be marked `TBD` with reference to the source location. | derived from `_CONTEXT.md` Scope ("interface requirements matrix"); ASSUMPTION on field granularity |
| REQ-DS-06 | The datasheet SHALL document the vendor engineering handoff basis (technical basis, battery limits, design expectations, source-supported requirements) per `ART-8FF7B18574`. | ARTIFACT_REGISTER `ART-8FF7B18574` |
| REQ-DS-07 | The datasheet SHALL identify the tagged equipment within the package. Where the workbook source slice is not locally accessible, equipment entries SHALL be marked `TBD` rather than inferred. | derived from `_CONTEXT.md` Anticipated Artifacts |
| REQ-DS-08 | The datasheet SHALL not reassert content owned by `DEL-041-01` (scope of work) or `DEL-041-03` (construction work package); cross-references are permitted. | DELIVERABLE_REGISTER PKG-041 set |
| REQ-DS-09 | The datasheet SHALL be a derivative work of the Gate-07 PROJECT_DECOMP snapshot and SHALL cite that snapshot path as its decomposition basis. | `_REFERENCES.md`; chirality derivative-package rule (governance) |
| REQ-DS-10 | The datasheet SHALL support the eight declared objectives `OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010`. | DELIVERABLE_REGISTER `DEL-041-02_package-datasheet`; OBJECTIVE_DELIVERABLE_MAP |
| REQ-DS-11 | The datasheet SHALL be issued for third-party (vendor or discipline) package engineering and design; vendor-targeted clarity is mandatory (units, definitions, acronyms expanded on first use). | `_CONTEXT.md` Scope; ASSUMPTION on style convention |

## Standards

| Standard | Applicability | Location | Source |
|---|---|---|---|
| Project Workbook (`26020-Packages_Interfaces_4_export.xlsx`), Packages tab, row 43 | Governing source for package identity and interface fact set | `_Sources/26020-Packages_Interfaces_4_export.xlsx` (binary; row slice **location TBD**) | `_REFERENCES.md`; PACKAGE_REGISTER SourceRefs |
| Project Package Requirements (`26020-Package_Requirements.docx`) | Governing source for package-level requirements convention | `_Sources/26020-Package_Requirements.docx` (location TBD for PKG-041 slice) | `_REFERENCES.md` (project-level) |
| Deepcut DBM excerpt (`DBM-Deepcut/4-25_Deepcut_DBM.md`) | Design-basis reference for WBS 01 deepcut packages | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (location TBD for PKG-041 slice) | PACKAGE_REGISTER `PKG-041` SourceRefs |
| ISO 8528 (Reciprocating internal combustion engine driven AC generating sets) | ASSUMPTION: likely applicable to a 3 MW standby genset | not locally accessible | ASSUMPTION |
| NFPA 110 (Emergency and Standby Power Systems) | ASSUMPTION: likely applicable to standby duty classification | not locally accessible | ASSUMPTION |
| IEEE C37 / ANSI medium-voltage switchgear standards | ASSUMPTION: likely applicable to 13.8 kV interface | not locally accessible | ASSUMPTION |
| NEC / CEC (jurisdiction TBD) | ASSUMPTION: likely applicable to building electrical | not locally accessible | ASSUMPTION |

## Verification

| Req ID | Verification approach |
|---|---|
| REQ-DS-01 | Cross-check identification block against `PACKAGE_REGISTER.csv` row `PKG-041` (peer review). |
| REQ-DS-02 | Cross-check ResponsibilityModel text against PACKAGE_REGISTER row `PKG-041` (peer review). |
| REQ-DS-03 | Cross-check name-derived ratings against PACKAGE_REGISTER row `PKG-041` (peer review). |
| REQ-DS-04 | Enumerate the twelve `IFC-*` IDs and confirm they match `INTERFACE_REGISTER.csv` where `ParentPackageID = PKG-041`. |
| REQ-DS-05 | Per-interface completeness audit; flag every `TBD` as a vendor handoff open item. |
| REQ-DS-06 | Inspection: handoff section present and source-anchored. |
| REQ-DS-07 | Inspection: equipment list present; absent items marked `TBD` with source path. |
| REQ-DS-08 | Inspection: no scope-of-work narrative duplicated; no installation/turnover content. |
| REQ-DS-09 | Inspection: References section cites GATE-07 snapshot path. |
| REQ-DS-10 | Cross-check supported objectives list against DELIVERABLE_REGISTER row. |
| REQ-DS-11 | Editorial review: units, acronyms, terminology consistent with `Guidance.md` glossary. |

## Documentation

Produced artifacts (per ARTIFACT_REGISTER, `ParentDeliverableID = DEL-041-02_package-datasheet`):

- `ART-1851AF6B89` — Package technical datasheet (this `Datasheet.md`).
- `ART-8FF7B18574` — Vendor engineering handoff basis (sections within `Datasheet.md` and `Guidance.md`).
- `ART-7F81FF2CB4` — Package interface requirements matrix (Interface Requirements Matrix section of `Datasheet.md`).
- `ART-0096A23E12` through `ART-E2472057A2` — Twelve interface fact rows (matrix rows in `Datasheet.md`).

Companion deliverable documents in this folder: `Guidance.md`, `Procedure.md`, this `Specification.md`.
