# Datasheet: DEL-094-03_construction-work-package — Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-094-03_construction-work-package |
| Deliverable name | Construction Work Package |
| Parent package | PKG-094 — Tanks, Caustic (API 650) 3-25 |
| Parent workbook row | Workbook Packages row 86 |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| Responsible party | EPC Integrator |
| Scope items | SOW-0193; SOW-0194; SOW-0195; SOW-0196 |
| Supported objectives | OBJ-002; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 |

## Attributes

| Attribute | Current value | Source |
|---|---|---|
| Facility/WBS basis | WBS 03 / 03-25 West Doe Compressor Station and Liquids Hub | PACKAGE_REGISTER.csv row PKG-094; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, Facility Overview |
| CoA tracking number | 26020-03-19-002 | PACKAGE_REGISTER.csv row PKG-094 |
| Package discipline | Mechanical | PACKAGE_REGISTER.csv row PKG-094; 26020-Packages_Interfaces_4_export.xlsx, Packages row 86 |
| Package interfaces | Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | INTERFACE_REGISTER.csv rows for PKG-094; PACKAGE_REGISTER.csv row PKG-094 |
| Package equipment basis | One (1) fresh caustic tank and one (1) spent caustic tank; 400 bbl atmospheric 32 oz tanks with LP fuel-gas blanket, heating, and insulation. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, Liquids Hub Equipment Basis; Caustic Mercaptan Treating Basis |
| Caustic service basis | 50 wt% NaOH/H2O; SG 1.75 TBC. Spent caustic vents through a flame arrestor to the incinerator header and supports truck-out; fresh caustic is not connected to the VRU. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, Caustic Mercaptan Treating Basis |
| Material restrictions | Aluminum shall not be used in the caustic building; caustic tank material/coating details remain TBC. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, Caustic Mercaptan Treating Basis |
| Caustic drain basis | Minimum drain-header rating 300# ANSI; spent-caustic tank caustic drain terminates at a 300# flange; caustic drain maximum temperature 121 deg C / 250 deg F TBC; minimum drain-tank temperature 80 deg F; heat tracing at 37.8 deg C / 100 deg F with redundant circuits under consideration. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, Drain Systems |
| Construction responsibility basis | ASSUMPTION: EPC Integrator owns the construction work package deliverable; field construction execution assignment in the 03-25 DBM is not explicitly stated for PKG-094 in locally accessible source slices. | DELIVERABLE_REGISTER.csv row DEL-094-03; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (no explicit construction responsibility section located) |
| Deliverable artifact set | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | DELIVERABLE_REGISTER.csv row DEL-094-03; ARTIFACT_REGISTER.csv rows for DEL-094-03 |

## Conditions

| Condition | Current basis | Source |
|---|---|---|
| Site basis | LSD 03-25-80-15 W6M, north of Dawson Creek, BC; site elevation 673 m AMSL; -40 deg C minimum ambient governs exposed equipment and packages. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, Site Basis |
| Winterization basis | Site basis drives winterization, electrical heat tracing, building heating, tank heating, road access, drainage, foundations, structural steel design, equipment metallurgy where affected by low temperature, and module layout. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, Site Basis |
| Tank applicable standard | API 650 (package name explicitly references API 650). Clause-level requirements TBD; source slice for API 650 not locally accessible. | PACKAGE_REGISTER.csv row PKG-094; ASSUMPTION: standard implied by package name |
| Process function — fresh caustic | Store and supply fresh caustic solution to the caustic treatment unit. | PACKAGE_REGISTER.csv row PKG-094 |
| Process function — spent caustic | Receive and safely store spent caustic from the pressurized caustic drain drum. | PACKAGE_REGISTER.csv row PKG-094 |
| Exclusions | TBD; no package-specific exclusions stated in source materials per PACKAGE_REGISTER.csv row PKG-094. | PACKAGE_REGISTER.csv row PKG-094 |

## Construction

| Construction topic | Current basis |
|---|---|
| Work package boundary | Covers the PKG-094 caustic tanks construction package for physical installation, construction, inspection, turnover, and tie-in to larger facility systems (Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports). |
| Included field activities | TBD. Field construction activities (foundations, off-loading, setting, tie-ins, terminations) are anticipated but not enumerated in locally accessible PKG-094 source slices; activities to be confirmed by detailed engineering and project execution plan. |
| Interface controls | Must address the nine PKG-094 interfaces listed under Attributes; each interface to be carried into the construction interface and turnover checklist. |
| Caustic-service safety controls | Construction must respect caustic-service constraints: no aluminum in the caustic building; spent-caustic flame arrestor to incinerator header; fuel-gas blanketing and heating/insulation on both tanks. |
| Quantities and coordinates | TBD; not provided in locally accessible source slices for this deliverable. |
| Inspection and turnover forms | TBD; source set identifies a checklist artifact but does not provide approved form content. |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` row 86.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx`, package heading 46. (location TBD — `.docx` source slice not extracted to local markdown.)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Facility Overview; Site Basis; Liquids Hub Equipment Basis; Caustic Mercaptan Treating Basis; Drain Systems.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`, row `DEL-094-03_construction-work-package`.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`, row `PKG-094`.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv`, rows for `PKG-094`.
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv`, rows for `DEL-094-03_construction-work-package`.
