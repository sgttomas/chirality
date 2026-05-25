# Specification: DEL-003-04_epc-civil-discipline-production-package

## Scope

This specification covers the EPC / Civil Discipline Production Package for `PKG-003` Site Grading. The package is a source-limited Civil production unit for the non-vendor package scope and is to support civil grading, drainage, containment, retention pond, and related discipline production deliverables.

The package excludes final civil design closure where the required geotechnical report, topographical survey, grade surface file, plot plan, or detailed drainage design is not yet available. Those items remain `TBD` until received and accepted.

## Requirements

| ID | Requirement | Source / Status |
|---|---|---|
| REQ-001 | The production package shall identify the Site Grading package basis, including `PKG-003`, workbook ID 3, WBS `02`, CoA Tracking Number `26020-01-42-003`, and Civil discipline ownership. | `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`; `_Sources/26020-Packages_Interfaces_4_export.xlsx`, workbook row 4 |
| REQ-002 | The package shall carry the active workbook interfaces for Drain / Containment and Grading / Site Drainage / Spill Containment. | `_Sources/26020-Packages_Interfaces_4_export.xlsx`, workbook row 4 |
| REQ-003 | The package shall include or explicitly track the civil deliverable candidates Grading Plan (`CIV-003`), Drainage / Stormwater Management Report (`CIV-004`), Retention Pond / Containment Basin Design (`CIV-015`), and Civil MTO / Quantity Take-Off (`CIV-019`) unless superseded by a human-approved deliverable register. | `_Sources/26020-Package_Requirements.docx`, civil grading / spill containment interface entries; **ASSUMPTION:** applied to this Civil production package because Gate 7 names a TBD discipline deliverable register |
| REQ-004 | Civil grading and drainage shall be designed to prevent off-site surface overflow from entering the expansion facility while directing and containing on-site overflow into a retention pond. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| REQ-005 | Surface-control features shall be considered within the facility and around selected equipment to prevent on-site releases from discharging outside the facility boundaries. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| REQ-006 | Main pipe rack grading shall use high equal-elevation ridges along main pipe racks. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| REQ-007 | Facility pad grading shall slope down from pipe racks at 1.5% to each side, with reduction to 1.0% allowed where required to maintain reasonable top-of-pile-cap elevations. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| REQ-008 | Maximum grade slopes shall be 3H:1V unless specifically engineered or mandated otherwise by the geotechnical report. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| REQ-009 | Ditches shall use a 0.2% minimum slope. Culverts shall use a 0.5% minimum slope, with 1.0% preferred. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| REQ-010 | Ditch and culvert sizing shall use the IDF curve for the 1:10 year, 15 minute rainfall event as the current basis; final duration is to be confirmed during detailed engineering. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Site Grading and Surface Water Management |
| REQ-011 | Drainage, retention pond sizing, and surface-water management shall carry the uncertainty that NBCC 2020 Dawson Creek IDF data is a proxy pending site-specific update. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-02 rainfall basis |
| REQ-012 | The package shall identify unresolved external inputs required for design closure: geotechnical assessment report, topographical survey and grade surface file, plot plan/retention-pond reference, and detailed engineering drainage design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 External Dependencies |
| REQ-013 | The package shall not treat preliminary geotechnical, topographical, drainage, or retention pond assumptions as final values. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Governing Civil and Structural Basis and External Dependencies |

## Standards

| Standard / Basis | Applicability | Source |
|---|---|---|
| National Building Code of Canada | Building code basis for civil/structural work | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 Governing Civil and Structural Basis |
| CAN/CSA-S16 Design of Steel Structures | Steel design | Same as above |
| CAN/CSA A23.3 Design of Concrete Structures | Concrete design | Same as above |
| Canadian Foundation Engineering Manual | Foundation engineering | Same as above |
| CSA G40.20/G40.21 | Structural steel materials | Same as above |
| CSA A23.1/A23.2 | Concrete materials, construction, and testing | Same as above |
| Rational Method, Q = CIA | Runoff calculations | Same as above |
| Manning's equation | Ditch and culvert sizing | Same as above |
| NBCC 2020 Dawson Creek IDF data | Current proxy rainfall basis pending site-specific update | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-02 rainfall basis |

## Verification

| Requirement(s) | Verification Approach |
|---|---|
| REQ-001 to REQ-003 | Check the discipline deliverable register and production package index against Gate 7, workbook row 4, and the package requirements source. |
| REQ-004 to REQ-010 | Check civil grading/drainage drawings, calculations, and reports against the DBM SEC-11 design principles. |
| REQ-011 | Confirm calculations and reports identify the rainfall basis as provisional until hydrology is updated. |
| REQ-012 to REQ-013 | Confirm the requirements closure record lists open geotechnical, survey, plot-plan, and detailed drainage inputs as blockers or assumptions. |

## Documentation

The production package should contain, or explicitly identify as `TBD`, the following records:

- Discipline production package basis.
- Discipline deliverable register.
- Grading Plan (`CIV-003`).
- Drainage / Stormwater Management Report (`CIV-004`).
- Retention Pond / Containment Basin Design (`CIV-015`).
- Civil MTO / Quantity Take-Off (`CIV-019`).
- Requirements closure record showing source-supported requirements, `TBD` items, assumptions, and unresolved external inputs.
- Verification evidence for cross-checking civil production outputs against the governing DBM civil basis.
