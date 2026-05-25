# Package Datasheet

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-001-02_package-datasheet |
| Deliverable name | Package Datasheet |
| Parent package | PKG-001 - Earthworks for foundations |
| Workbook ID / row | 1 / row 2 |
| WBS | 01 |
| CoA tracking number | 26020-01-42-001 |
| Discipline | Civil |
| Responsible party | EPC Integrator |
| Deliverable type | EPC Package Datasheet |
| Source basis | Workbook Packages row 2; Gate 7 PROJECT_DECOMP snapshot; DBM-Deepcut civil section |

## Attributes

| Attribute | Source-grounded value | Source |
|---|---|---|
| Package scope description | Workbook-defined Civil package for "Earthworks for foundations" under WBS 01 with recorded physical interfaces. | Gate 7 PACKAGE_REGISTER.csv, PKG-001 |
| Responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources. | Gate 7 PACKAGE_REGISTER.csv, PKG-001 |
| Inclusion criteria | Workbook row 2; discipline Civil; WBS 01; applicable interface types are Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports. | Gate 7 PACKAGE_REGISTER.csv, PKG-001; INTERFACE_REGISTER.csv, PKG-001 |
| Exclusions | TBD; no package-specific exclusions stated in source materials. | Gate 7 PACKAGE_REGISTER.csv, PKG-001 |
| Package role | Authoritative companion register row. | Gate 7 PACKAGE_REGISTER.csv, PKG-001 |
| Detailed equipment list | TBD; current source set identifies civil earthworks/foundation scope and interfaces, not a package-specific tagged equipment list for this deliverable. | Gate 7 ARTIFACT_REGISTER.csv, DEL-001-02; DBM-Deepcut civil section |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Civil/structural scope context | Applies to civil and structural engineering for the facility pad, drainage system, retention pond, roads, foundations, process and utility modules, permanent buildings, and ancillary buildings. | DBM-Deepcut, Civil Scope |
| Geotechnical inputs | Bearing capacity, LPILE curves, dynamic design criteria, road granular pavement design parameters, pavement layer thicknesses, and geotextile need are TBD pending the geotechnical assessment. | DBM-Deepcut, Geotechnical and Topographical Assumptions |
| Topographical inputs | Existing grade surface file is assumed suitable for grading and drainage design; final format, data model, and contents are TBD pending survey completion. | DBM-Deepcut, Geotechnical and Topographical Assumptions |
| Surface water management | Design must prevent off-site surface overflow from entering the expansion facility and direct/contain on-site overflow into a retention pond. | DBM-Deepcut, Site Grading and Surface Water Management |
| Retention pond | On-site retention pond with berm is required; location and capacity are TBD pending plot-plan coordination and detailed engineering. | DBM-Deepcut, Site Grading and Surface Water Management |
| Drainage design basis | Ditch and culvert storm basis is 1:10 year, 15 minute rainfall event; IDF duration is to be confirmed during detailed engineering. | DBM-Deepcut, Site Grading and Surface Water Management |

## Construction

| Construction/design datum | Value |
|---|---|
| Main pipe rack grading | High equal-elevation ridges along main pipe racks. |
| Facility pad grading | Pad slopes down from pipe racks at 1.5% to each side; may be reduced to 1.0% where required to maintain reasonable top-of-pile-cap elevations. |
| Maximum grade slope | 3H:1V maximum, including road-fill side slopes, ditches, stockpiles, pond slopes, and similar grade surfaces, unless specifically engineered or mandated otherwise by the geotechnical report. |
| Ditch slope | 0.2% minimum. |
| Culvert slope | 0.5% minimum; 1.0% preferred. |
| Road widths | Primary roads 10.0 m; secondary roads 8.0 m. |
| Road crown | 3.0% slope to each side of crown. |
| Default foundation basis | Driven steel piles for buildings, equipment, towers, tanks, modules, pipe racks, and similar structures unless a more specific foundation basis is listed or detailed engineering confirms a different requirement. |
| Compressor foundation basis | Precast concrete block supported on driven steel piles, subject to dynamic analysis; dynamic analysis results are TBD. |

## Interface Requirements Matrix

| Interface ID | Interface type | Applicability | Source |
|---|---|---|---|
| IFC-293AF03D4E | Grading / Site Drainage / Spill Containment | YES | Gate 7 INTERFACE_REGISTER.csv, Workbook Packages row 2 |
| IFC-1E47AB3801 | Structural / Foundations / Supports | YES | Gate 7 INTERFACE_REGISTER.csv, Workbook Packages row 2 |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`, row 2.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Civil Scope through Assumptions, TBDs, and Design Development Requirements.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`, PKG-001.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`, DEL-001-02_package-datasheet.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv`, DEL-001-02_package-datasheet.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv`, PKG-001.
