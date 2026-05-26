# Datasheet — DEL-041-03 Construction Work Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-041-03_construction-work-package` | `_CONTEXT.md` Identity |
| Name | Construction Work Package | `_CONTEXT.md` Identity |
| Artifact identity | ART-55CB0F50C6 — EPC Construction Work Package | GATE-07 `ARTIFACT_REGISTER.csv` row for DEL-041-03 |
| Parent Package | `PKG-041` — 13.8kV, 3.0MW STANDBY GENERATOR BUILDING (490-1) | `_CONTEXT.md`; GATE-07 `PACKAGE_REGISTER.csv` |
| Workbook ID | 41 (Workbook Packages row 43) | GATE-07 `PACKAGE_REGISTER.csv` |
| WBS | 01 | GATE-07 `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-032 | GATE-07 `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `_CONTEXT.md`; GATE-07 `PACKAGE_REGISTER.csv` |
| Deliverable Type | EPC Construction Work Package | `_CONTEXT.md` Identity |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; GATE-07 `DELIVERABLE_REGISTER.csv` |
| Covers Scope Item | `SOW-0042` | `_CONTEXT.md`; GATE-07 `DELIVERABLE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | 13.8 kV, 3.0 MW standby generator building (490-1) supporting facility electrical reliability | GATE-07 `PACKAGE_REGISTER.csv` package name; package function inference (ASSUMPTION) |
| Ownership split — Package Vendor | Package engineering, package design, vendor documentation, physical equipment package | GATE-07 `PACKAGE_REGISTER.csv` responsibility narrative |
| Ownership split — EPC Integrator | Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | GATE-07 `PACKAGE_REGISTER.csv` responsibility narrative |
| Construction anchor artifact | ART-55CB0F50C6 — Construction work package (integrator-authored construction work package for physical installation, construction, and tie-in to larger systems) | GATE-07 `ARTIFACT_REGISTER.csv` |
| Anticipated artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | `_CONTEXT.md` Anticipated Artifacts |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Voltage class | 13.8 kV | Package name (GATE-07 `PACKAGE_REGISTER.csv`) |
| Generator rating | 3.0 MW | Package name (GATE-07 `PACKAGE_REGISTER.csv`) |
| Service classification | Standby generator building | Package name (GATE-07 `PACKAGE_REGISTER.csv`) |
| Site building reference | 490-1 | Package name (GATE-07 `PACKAGE_REGISTER.csv`) |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials | GATE-07 `PACKAGE_REGISTER.csv` exclusions column |
| Environmental / site conditions | TBD — not stated in accessible registers; resolve from Design Basis Memorandum (`_Sources/DBM-Deepcut`) source slices before construction | location TBD |

## Construction

### Declared Package Interfaces (must be planned, tied-in, inspected, and turned over)

Twelve workbook-declared interface types apply to PKG-041 (per GATE-07 `INTERFACE_REGISTER.csv`):

| Interface ID | Interface Type |
|---|---|
| IFC-508C53EB72 | Utility Piping |
| IFC-1528C860A4 | Drain / Containment |
| IFC-004BB1B385 | Electrical Power |
| IFC-134CB10F1D | Grounding / Bonding |
| IFC-8E23F09E7C | Area / Exterior Lighting |
| IFC-1E6785E532 | I&C / Control Cabling |
| IFC-FEEE41EDAA | Communications / Network |
| IFC-7D36256CF5 | Building HVAC / Services |
| IFC-5F7FE5FA2A | Fire & Gas / Safety Systems |
| IFC-57828C08C8 | Maintenance Access |
| IFC-B9452850B5 | Grading / Site Drainage / Spill Containment |
| IFC-D0146B1F8C | Structural / Foundations / Supports |

Each interface row is the construction-side tie-in obligation owned by the EPC Integrator. Interface fact evidence is carried on DEL-041-02 (Package Datasheet); the construction work package consumes those facts and produces tie-in workface plans and turnover checklists.

### Construction phases (high level)

| Phase | Source / Status |
|---|---|
| Site preparation, foundations, grading | Implied by interface types Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports; detailed scope TBD |
| Building erection / setting of vendor-furnished generator building | ASSUMPTION based on package type "standby generator building"; vendor split per `PACKAGE_REGISTER.csv` responsibility narrative |
| Mechanical / utility tie-ins | Interface types Utility Piping; Drain / Containment; Building HVAC / Services |
| Electrical tie-ins | Interface types Electrical Power; Grounding / Bonding; Area / Exterior Lighting |
| Controls / communications tie-ins | Interface types I&C / Control Cabling; Communications / Network |
| Safety system integration | Interface type Fire & Gas / Safety Systems |
| Maintenance access provisions | Interface type Maintenance Access |
| Inspection, test, and turnover | Anticipated artifact: construction interface and turnover checklist |

## References

- `_CONTEXT.md` (deliverable-local)
- `_REFERENCES.md` (deliverable-local)
- `_DEPENDENCIES.md` (deliverable-local)
- GATE-07 `DELIVERABLE_REGISTER.csv` — row for DEL-041-03
- GATE-07 `PACKAGE_REGISTER.csv` — row for PKG-041
- GATE-07 `ARTIFACT_REGISTER.csv` — rows for DEL-041-03 and sibling DEL-041-02
- GATE-07 `INTERFACE_REGISTER.csv` — rows IFC-* for PKG-041
- GATE-07 `OBJECTIVE_DELIVERABLE_MAP.csv` — rows mapping OBJ-001/004/005/006/007/008/009/010 to DEL-041-03
- Workbook Packages row 43 (source reference cited in registers; full workbook slice not opened in this run; location TBD for specific tie-in design values)
- `_Sources/DBM-Deepcut` Design Basis Memorandum (not read in this run; location TBD)
