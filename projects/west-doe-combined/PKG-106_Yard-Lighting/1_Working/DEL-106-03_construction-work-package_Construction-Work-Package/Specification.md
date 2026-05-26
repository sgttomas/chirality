# Specification — DEL-106-03 Construction Work Package (Yard Lighting)

> Normative requirements for what this Construction Work Package must contain to satisfy the Gate 5 EPC anchor deliverable definition. Requirements derived from the GATE-07 accepted decomposition snapshot. Technical limit-values, codes/standards clauses, and design parameters that are not in deliverable-local source slices are marked `TBD` or labeled `ASSUMPTION`.

## Scope

**In-scope.** Authoring the EPC Integrator construction-work-package set for `PKG-106 Yard Lighting`, covering:

- Physical installation method for the vendor-engineered yard-lighting package (`DEL-106-04`).
- Construction tie-ins to facility electrical power, grounding/bonding, and area/exterior-lighting interfaces (`INTERFACE_REGISTER.csv` PKG-106).
- Inspection, turnover, and construction-interface evidence supporting acceptance under `DEL-106-06`.

**Out of scope.**

- Vendor package engineering, design, fabrication, and physical equipment supply (covered by `DEL-106-04`).
- Vendor document register, submittals, and document turnover (covered by `DEL-106-05`).
- EPC review and acceptance of the integrated package (covered by `DEL-106-06`).
- Package scope-of-work narrative and tagged-equipment list (covered by `DEL-106-01`).
- Technical datasheet and interface requirements matrix for vendor handoff (covered by `DEL-106-02`).

Source: `DELIVERABLE_REGISTER.csv` (rows for `DEL-106-01..06`); `_CONTEXT.md`.

## Requirements

| ReqID | Requirement | Source | Label |
|---|---|---|---|
| R-1 | The construction work package SHALL describe how the Yard Lighting package will be physically installed, built, inspected, turned over, and tied into the larger facility systems. | `DELIVERABLE_REGISTER.csv` Description for `DEL-106-03` | FACT |
| R-2 | The deliverable SHALL produce three artifacts: (a) Construction work package (`ART-88F0D51520`), (b) Installation and tie-in workface plan (`ART-F0EC8767B3`), (c) Construction interface and turnover checklist (`ART-FC16B15401`). | `ARTIFACT_REGISTER.csv` (rows for `DEL-106-03`); `_CONTEXT.md` Anticipated Artifacts | FACT |
| R-3 | The construction work package SHALL preserve the EPC Integrator / Package Vendor responsibility split: vendor owns package engineering, design, documentation, and physical equipment; EPC Integrator owns facility integration, tie-ins, constructability, and procurement/construction coordination. | `PACKAGE_REGISTER.csv` (ResponsibilityModel); `OBJECTIVE_REGISTER.csv` (OBJ-004) | FACT |
| R-4 | The installation and tie-in workface plan SHALL address each applicable package interface: Electrical Power, Grounding/Bonding, Area/Exterior Lighting. | `INTERFACE_REGISTER.csv` PKG-106 (IFC-6FCF1B30D6, IFC-DA0D60681B, IFC-ED86F51087) | FACT |
| R-5 | The construction interface and turnover checklist SHALL provide construction-facing interface, tie-in, inspection, and turnover evidence for the approved package, suitable to feed `DEL-106-06` acceptance. | `ARTIFACT_REGISTER.csv` (`ART-FC16B15401` Notes); `DELIVERABLE_REGISTER.csv` (`DEL-106-06`) | FACT |
| R-6 | Construction scope SHALL incorporate civil/structural/site/construction-support requirements (foundations, grading, access, containment) as applicable to yard-lighting installation. | `OBJECTIVE_REGISTER.csv` (OBJ-008) | ASSUMPTION (package-heuristic mapping; specific civil items at `location TBD`) |
| R-7 | The work package SHALL carry sour-service, fire/gas, shutdown, environmental, and applicable code/standard constraints into installation and tie-in steps where applicable to exterior lighting in the operating area. | `OBJECTIVE_REGISTER.csv` (OBJ-009) | ASSUMPTION (package-heuristic; specific clauses `TBD`) |
| R-8 | The work package SHALL preserve operability, maintainability, sparing, isolation, winterization, commissioning, turnover, and open-item closure considerations from package procurement through facility handoff. | `OBJECTIVE_REGISTER.csv` (OBJ-010) | ASSUMPTION (package-heuristic) |
| R-9 | All non-trivial technical values (lighting levels, fixture counts, pole types, conductor sizes, panel ratings, area-classification compliance) SHALL be sourced; values absent from accessible source slices SHALL be carried as `TBD` rather than invented. | Skill `four-documents` constraint; `_REFERENCES.md` (no deliverable-local source slices copied) | FACT |
| R-10 | The work package SHALL cite Workbook Packages row 12 as source basis for package identity, scope, and interface applicability. | `_REFERENCES.md`; `DELIVERABLE_REGISTER.csv` SourceRef | FACT |

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| Workbook Packages row 12 (`_Sources/26020-Packages_Interfaces_4_export.xlsx`) | Authoritative package identity, discipline, responsibility model, interfaces | `_Sources/26020-Packages_Interfaces_4_export.xlsx` (deliverable-local slice TBD) |
| `26020-Package_Requirements.docx` | Vendor-document and package-requirements basis (per OBJ-004/OBJ-010) | `_Sources/26020-Package_Requirements.docx` (deliverable-local slice TBD) |
| DBM-Deepcut SEC-12 Electrical Basis | Facility electrical basis (power, grounding, lighting, EHT, cathodic) | location TBD (referenced by OBJ-005; not deliverable-local slice) |
| DBM-Deepcut SEC-11 Civil, Buildings, and Miscellaneous Facilities Basis | Civil/structural/site basis for installation | location TBD (referenced by OBJ-008) |
| DBM-Deepcut SEC-14 Instrumented Protection / SEC-15 Regulatory, Codes, and Standards | Safety, regulatory, codes & standards constraints | location TBD (referenced by OBJ-009) |
| Project / jurisdiction electrical codes (NEC/CEC or equivalent), area-classification standards, exterior-lighting standards | Applicable to installation methods, grounding, hazardous-area compliance | ASSUMPTION: likely applicable; specific standards `TBD` |

## Verification

| ReqID | Verification approach |
|---|---|
| R-1 | Inspection of the Construction work package artifact (`ART-88F0D51520`) against this Spec. |
| R-2 | Artifact presence check (three artifacts exist and are linked from the deliverable). |
| R-3 | Inspection of responsibility narrative for vendor/EPC split language consistent with `PACKAGE_REGISTER.csv`. |
| R-4 | Workface plan review: each of the three applicable interfaces has a defined construction tie-in method. |
| R-5 | Turnover checklist completeness review; cross-walk to `DEL-106-06` acceptance basis. |
| R-6 | Cross-walk between civil/structural items in workface plan and OBJ-008-relevant interfaces. |
| R-7 | Code/standard applicability check; safety/shutdown/area-class items reflected in steps. |
| R-8 | Operability/maintenance/commissioning/turnover items present in checklist. |
| R-9 | TBD audit: any non-trivial unsourced value is carried as `TBD`, not invented. |
| R-10 | Source-citation audit. |

## Documentation

Required artifacts to be produced (under this deliverable):

- Construction work package narrative (`ART-88F0D51520`).
- Installation and tie-in workface plan (`ART-F0EC8767B3`).
- Construction interface and turnover checklist (`ART-FC16B15401`).

Supporting deliverable-local files maintained by skill outputs: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, `_STATUS.md`, `_run_records/`.
