# Specification: DEL-003-02_package-datasheet — Package Datasheet

## Scope

This specification governs the EPC Integrator Package Datasheet for `PKG-003` Site Grading. The datasheet shall carry the source-supported technical handoff basis needed for civil package engineering and design, including the package identity, civil grading and drainage basis, interface facts, source dependencies, and unresolved items.

This deliverable covers `SOW-0003`: the workbook-defined Civil package "Site Grading" as a distinct flat project package for WBS 01.

### Exclusions

- Detailed drainage calculations are excluded until detailed engineering confirms the final hydrology, IDF duration, ditch and culvert sizing, retention pond capacity, and final pond location.
- Final geotechnical parameters are excluded until the geotechnical assessment report is complete and reviewed.
- Final existing-ground model details are excluded until the topographical survey and grade surface file are delivered.
- Vendor or discipline design not supported by the accessible source set remains `TBD`.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-001 | The datasheet shall identify the package as `PKG-003` Site Grading, Civil discipline, WBS `01`, CoA tracking number `26020-01-42-003`. | Workbook Packages row 4; Gate 7 `PACKAGE_REGISTER.csv` | Datasheet identity check |
| REQ-002 | The datasheet shall carry the package interface facts Drain / Containment and Grading / Site Drainage / Spill Containment. | Workbook Packages row 4; Gate 7 `ARTIFACT_REGISTER.csv` | Interface matrix check |
| REQ-003 | The datasheet shall identify the civil scope basis for site grading, ditching, culvert, retention pond, and surface-control requirements. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Civil Scope | Source trace check |
| REQ-004 | Site grading and drainage basis shall prevent off-site surface overflow from entering the expansion facility while directing and containing on-site overflow into a retention pond. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Site Grading and Surface Water Management | Requirement-to-datasheet check |
| REQ-005 | Surface-control features shall be considered within the facility and around selected equipment to prevent on-site releases from discharging outside the facility boundaries. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Site Grading and Surface Water Management | Requirement-to-datasheet check |
| REQ-006 | The datasheet shall preserve the source grading values for pipe rack ridges, pad slope, reduced pad slope allowance, maximum grade slope, ditch slope, culvert slope, storm basis, facility pad surface, and access-road drainage definition. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Site Grading and Surface Water Management | Values and units check |
| REQ-007 | The datasheet shall list geotechnical assessment, topographical survey/grade surface file, plot plan, and detailed drainage engineering as external dependencies for closure. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, External Dependencies | Open-item check |
| REQ-008 | The datasheet shall mark geotechnical parameters, final grade surface file contents, final IDF duration, retention pond location, and retention pond capacity as `TBD` until the required external inputs are accepted. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Geotechnical and Topographical Assumptions; External Dependencies; Assumptions | TBD register check |
| REQ-009 | ASSUMPTION: Objectives `OBJ-001`, `OBJ-007`, `OBJ-008`, and `OBJ-009` are directionally relevant context for this datasheet because they are mapped to `PKG-003`/`DEL-003-02` in the accepted Gate 7 registers. They shall not be treated as additional hard design requirements without source support. | `_CONTEXT.md`; Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`; Gate 7 `OBJECTIVE_PACKAGE_MAP.csv` | Assumption label check |

## Standards

| Standard / basis | Applicability | Source |
|---|---|---|
| National Building Code of Canada | Governing building code and project-site loading basis where civil/building support applies | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Civil and Structural Basis |
| CAN/CSA-S16 Design of Steel Structures | Steel design basis for related structures | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Civil and Structural Basis |
| CAN/CSA A23.3 Design of Concrete Structures | Concrete design basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Civil and Structural Basis |
| Canadian Foundation Engineering Manual | Foundation engineering basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Civil and Structural Basis |
| CSA G40.20/G40.21 | Structural steel material basis where structural support interfaces are implicated | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Civil and Structural Basis |
| CSA A23.1/A23.2 | Concrete materials, construction, and testing basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Civil and Structural Basis |
| Rational Method, Q = CIA | Runoff calculation basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Civil and Structural Basis |
| Manning's equation | Ditch and culvert sizing basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Governing Civil and Structural Basis |

## Verification

| Check | Acceptance basis |
|---|---|
| Identity completeness | Datasheet includes deliverable ID, package ID, WBS, CoA tracking number, package name, discipline, responsible party, source scope item, and workbook source. |
| Source traceability | Each non-TBD technical value is traceable to the workbook, Gate 7 registers, or DBM source slice. |
| Interface completeness | Drain / Containment and Grading / Site Drainage / Spill Containment are both included as interface facts. |
| TBD discipline | External inputs and design values not closed by the accessible source set are marked `TBD` or `ASSUMPTION`. |
| Cross-document consistency | Values and terms match `Datasheet.md`, `Guidance.md`, and `Procedure.md`. |

## Documentation

The completed package datasheet set shall include or reference:

- Package technical datasheet.
- Vendor or discipline engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Open external input list for geotechnical, topographical, plot plan, and detailed drainage engineering dependencies.
