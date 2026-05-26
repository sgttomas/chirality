# Datasheet — DEL-063-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-063-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-063` |
| PackageName | Tanks, DSO (API 650) |
| Subject Equipment Tag | `26020-01-PT-19-001` — Tanks, DSO (`SourcePath: _Sources/26020-Package_Requirements.docx`, `SectionRef: Heading — 26020-01-PT-19-001 - Tanks, DSO`) |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Decomposition Snapshot | GATE-07_Final_Published_2026-05-24 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable role | Review and acceptance evidence pack for the Package Vendor production unit (`DEL-063-04`) and the Vendor Document Turnover (`DEL-063-05`) against EPC anchor deliverables (`DEL-063-01` SOW, `DEL-063-02` Package Datasheet, `DEL-063-03` Construction Work Package). | `DELIVERABLE_REGISTER.csv` row `DEL-063-06`; `_CONTEXT.md` |
| Acceptance subject | One (1) atmospheric disulphide oil (DSO) storage tank receiving separated DSO from the DSO separator (level-controlled) within the caustic regeneration system. | `26020-Package_Requirements.docx` `26020-01-PT-19-001 - Tanks, DSO`, "Basic Scope" / "Major Included Equipment" |
| Covered SOW IDs | `SOW-0209`, `SOW-0210`, `SOW-0211`, `SOW-0212` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported Objectives | `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION — package-grouping heuristic per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC` against `OBJECTIVE_DELIVERABLE_MAP.csv` for PKG-063) | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service / location | 4-25 future LPG mercaptan treating unit; vetted package scope basis. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Location / Status" |
| Design code | Design & fabrication to modified API 650. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Major Included Equipment" |
| Nominal capacity | 400 bbl. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Major Included Equipment" / "Scope Notes / Open Items" |
| Pressure rating | Atmospheric; design pressure 32 oz, 1.0 oz vacuum. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Major Included Equipment" / "Scope Notes / Open Items" |
| Heater | c/w heater at 32.2 °C (90 °F) minimum; vendor to design heater. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Major Included Equipment" |
| Internal coating | Internally coated (floor, walls, roof). | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Major Included Equipment" |
| Insulation | Insulated to maintain DSO above pour point for truck-out and handling. Minimum temperature TBD per source. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Major Included Equipment" |
| Capacity/design throughput | TBC per source. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Scope Notes / Open Items" |
| Minimum ambient temperature | TBD per source. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Scope Notes / Open Items" |
| Flow rate | TBD per source. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Scope Notes / Open Items" |
| "By others" exclusions | Foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase, etc. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Scope Notes / Open Items" |
| Acceptance trigger states (upstream maturity) | `DEL-063-04` and `DEL-063-05` reach a maturity state acceptable for integration review. (ASSUMPTION — exact gating values TBD; `_DEPENDENCIES.md` declares no upstream edges as of PREPARATION.) | `_DEPENDENCIES.md`; ASSUMPTION |

## Construction

| Acceptance Artifact (per `_CONTEXT.md` / decomposition) | Description | Source |
|---|---|---|
| Vendor document review log | Reviewer-by-document register tracking the Vendor Document Index (`PRQ-009`) and each enumerated vendor engineering deliverable for `26020-01-PT-19-001`. | `_CONTEXT.md` Anticipated Artifacts; `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Vendor Engineering Deliverables" |
| Package acceptance checklist | Pass/fail acceptance matrix mapped to SOW items `SOW-0209..0212`, the Package Datasheet (`DEL-063-02`), and the Construction Work Package (`DEL-063-03`). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Test / inspection evidence | Material Test Reports / Certificates (`QLT-013`), ITP execution records against `QLT-003`, Inspection Release Certificate (`QLT-020`), and FAT records (`MEC-022`). | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Vendor Engineering Deliverables" — Core vendor documents and Core package engineering blocks |
| Turnover evidence | Manufacturing Record Book / Vendor Data Book (`QLT-021`, `MEC-023`, `PRQ-016`), Hydrotest / Pressure Test Packages (`PIP-024`), and SPIR (`PRQ-015`). | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Vendor Engineering Deliverables" |
| Physical-interface acceptance coverage | Interfaces marked `Yes` for `26020-01-PT-19-001`: Process Piping; Relief / Flare / Vent; Drain / Containment; Area / Exterior Lighting; Grounding / Bonding; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Interfaces marked `No`: Utility Piping; Electrical Power; EHT; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Product Loading; Pipeline / Pigging. | `26020-Package_Requirements.docx` `26020-01-PT-19-001`, "Physical Interface Summary" (interface source: `26020-Packages_Interfaces.3.xlsx` col M row 90) |

## References

- `_Sources/26020-Package_Requirements.docx` — heading `26020-01-PT-19-001 - Tanks, DSO`
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — package row 90 (interface evidence, column-level location TBD)
- Source basis (referenced by Heading): `Bid Docs/_Budgetary/26020-01-PT-RFQ-19-001_Tanks_DSO_R0.docx` — not locally accessible, location TBD
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv`
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
