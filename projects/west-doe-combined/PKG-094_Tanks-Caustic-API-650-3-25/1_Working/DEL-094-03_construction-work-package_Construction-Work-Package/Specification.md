# Specification: DEL-094-03_construction-work-package — Construction Work Package

## Scope

This specification defines the minimum content requirements for the PKG-094 Construction Work Package for the Tanks, Caustic (API 650) 3-25 package. The package covers how the fresh caustic and spent caustic tank installation will be physically installed, built, inspected, turned over, and tied into the larger 03-25 West Doe Liquids Hub.

The work package shall include:

- construction work package content for PKG-094;
- installation and tie-in workface plan content for one (1) fresh caustic tank and one (1) spent caustic tank;
- construction interface and turnover checklist content for the nine applicable PKG-094 interfaces.

Exclusions: PACKAGE_REGISTER.csv row PKG-094 records exclusions as `TBD; no package-specific exclusions stated in source materials`.

## Requirements

| Req ID | Requirement | Verification |
|---|---|---|
| CWP-001 | The Construction Work Package shall identify the package as PKG-094, Tanks, Caustic (API 650) 3-25, WBS 03, CoA tracking number 26020-03-19-002, Mechanical discipline. | Check against workbook Packages row 86, PACKAGE_REGISTER.csv row PKG-094, and DELIVERABLE_REGISTER.csv row DEL-094-03. |
| CWP-002 | The Construction Work Package shall include a construction-facing plan for physical installation, construction, inspection, turnover, and tie-in to larger facility systems for one (1) fresh caustic tank and one (1) spent caustic tank. | Confirm document sections or attached workface plan cover each named function for each tank. |
| CWP-003 | The Construction Work Package shall address each PKG-094 interface in the construction interface and turnover checklist: Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | Cross-check interface matrix/checklist against INTERFACE_REGISTER.csv rows for PKG-094 and workbook Packages row 86. |
| CWP-004 | The Construction Work Package shall carry tank service basis: atmospheric 32 oz construction with LP fuel-gas blanket, heating, and insulation; caustic solution 50 wt% NaOH/H2O at SG 1.75 (TBC). | Check construction package values against DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, Caustic Mercaptan Treating Basis. |
| CWP-005 | The Construction Work Package shall prohibit use of aluminum within the caustic building and shall flag caustic tank material/coating details as TBC until detailed engineering closes them. | Check materials and exclusions list in the work package against DBM Caustic Mercaptan Treating Basis. |
| CWP-006 | The Construction Work Package shall carry the spent-caustic venting basis: flame arrestor to incinerator header; support for truck-out at the spent caustic tank. | Check venting and truck-out provisions in the workface plan and interface checklist. |
| CWP-007 | The Construction Work Package shall carry caustic drain construction provisions: minimum drain-header rating 300# ANSI; termination at 300# flange at the spent-caustic tank; maximum caustic drain temperature 121 deg C / 250 deg F (TBC); minimum drain-tank temperature 80 deg F; heat tracing at 37.8 deg C / 100 deg F with redundant circuits (under consideration). | Confirm drain-system tie-in provisions in the workface plan match DBM Drain Systems and detailed engineering. |
| CWP-008 | The Construction Work Package shall carry the site basis governing winterization, electrical heat tracing, building heating, tank heating, foundations, structural steel design, equipment metallurgy (where affected by low temperature), and module layout. | Confirm against DBM Site Basis. |
| CWP-009 | The Construction Work Package shall include API 650 as a named governing standard for tank construction. Clause-level construction provisions remain TBD pending access to API 650 source slices. | Check standards section and `TBD` markers; confirm any cited clauses are evidenced. |
| CWP-010 | The Construction Work Package shall identify all unresolved construction inputs, including: tank material/coating selection (TBC), caustic drain maximum temperature (TBC), heat-tracing decision, foundation drawings, plot plan/equipment coordinates, geotechnical/topographical inputs, approved inspection/turnover forms, and the construction-responsibility assignment for PKG-094. | Review open item log and turnover checklist. |
| CWP-011 | ASSUMPTION: The construction work package shall distinguish EPC Integrator deliverable ownership from field construction execution responsibility; PKG-094-specific field construction assignment is not located in accessible source slices and remains TBD. | Human review of responsibility matrix. |
| CWP-012 | The Construction Work Package shall be consistent with PACKAGE_REGISTER.csv row PKG-094 split: package vendor owns package engineering, design, vendor documentation, and the physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, and procurement/construction coordination. | Cross-check responsibility narrative in the work package against PACKAGE_REGISTER.csv row PKG-094. |

## Standards

| Standard or basis | Applicability | Source |
|---|---|---|
| API 650 | Welded tanks for oil storage; named in the package title for the caustic tank construction basis. Clause-level provisions are `location TBD` pending access to the API 650 source. | PACKAGE_REGISTER.csv row PKG-094 (package title); ASSUMPTION: API 650 governs tank construction. |
| 26020 Package Requirements (Word source) | Package-level construction and turnover requirements as stated under heading 46 of `26020-Package_Requirements.docx`. Source slice not extracted to local markdown; `location TBD`. | _REFERENCES.md; PACKAGE_REGISTER.csv row PKG-094 |
| DBM-Comp_and_Liquids 3-25 | Facility design basis governing site, winterization, caustic service, and caustic drain provisions affecting construction. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md |

## Verification

The Construction Work Package is ready for controlled review when:

- identity fields match Gate 7 PACKAGE/DELIVERABLE registers and workbook row 86;
- all nine PKG-094 interface facts are carried into the construction interface checklist;
- DBM caustic-service and caustic-drain values used in the work package cite the DBM section or approved downstream engineering;
- API 650 is named and clause-level construction provisions are listed as `TBD` or evidenced;
- all missing construction quantities, drawings, coordinates, form IDs, and material/coating selections are listed as `TBD` or open items;
- EPC Integrator deliverable ownership is distinguished from field construction execution responsibility, with the field execution assignment marked `TBD` until human ruling.

## Documentation

The following documentation shall be produced or attached to the Construction Work Package:

- construction work package;
- installation and tie-in workface plan (fresh caustic tank; spent caustic tank);
- construction interface and turnover checklist covering the nine PKG-094 interfaces;
- responsibility matrix distinguishing EPC Integrator deliverable ownership from field construction execution responsibility;
- open input and TBD register (including tank material/coating, caustic drain temperature, heat tracing decision, plot plan and foundation coordinates);
- inspection and turnover record index, with final forms TBD.
