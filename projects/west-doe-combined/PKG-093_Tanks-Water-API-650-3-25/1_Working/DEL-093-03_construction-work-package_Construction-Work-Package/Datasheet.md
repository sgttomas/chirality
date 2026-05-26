# Datasheet — DEL-093-03 Construction Work Package (PKG-093 Tanks, Water (API 650) 3-25)

> Descriptive datasheet for the EPC Construction Work Package covering the two sweet produced-water storage tanks (TK-9060-2, TK-9070-2) in PKG-093 at the 03-25 West Doe Compressor Station and Liquids Hub.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-093-03_construction-work-package` |
| Name | Construction Work Package |
| ParentPackageID | `PKG-093` |
| PackageName | Tanks, Water (API 650) 3-25 |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| Facility | 03-25 West Doe Compressor Station and Liquids Hub, LSD 03-25-80-15 W6M, north of Dawson Creek, BC (`SourcePath: _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, `SectionRef: Site Basis`) |
| Covers ScopeItems | SOW-0229; SOW-0230; SOW-0231; SOW-0232 |
| Supports Objectives | OBJ-002; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION: package-grouping heuristic) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package equipment | Two (2) 3800 bbl Sweet Produced Water Storage Tanks: TK-9060-2, TK-9070-2 | PACKAGE_REGISTER.csv row PKG-093 |
| Tank standard | API 650 (per package name; clause-level requirements TBD — location TBD in 26020-Package_Requirements.docx heading 45) | PACKAGE_REGISTER.csv row PKG-093; ASSUMPTION on clause set |
| Process service | Sweet Produced Water & Process Water | PACKAGE_REGISTER.csv row PKG-093 |
| Construction artifact set | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | DELIVERABLE_REGISTER.csv row DEL-093-03 |
| Site ambient design temperature (governing) | -40 deg C minimum (governs exposed equipment, packages, instrumentation) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Site Basis |
| Site elevation | 673 m AMSL | DBM Site Basis |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Produced-water service basis | Storage, treatment, and transfer for 03-25 and 04-25 sources | DBM Site Basis |
| Facility produced-water design flow | 3,600 m3/d (22,644 bbl/d) | DBM Raw Gas and Water Design Conditions |
| Produced-water density (design) | 1.18 SG; tank design SG 1.25 TBC | DBM Raw Gas and Water Design Conditions |
| Cold-climate constructability driver | Winterization, electrical heat tracing, tank heating, road access, drainage, foundations, structural steel design considerations apply | DBM Site Basis |
| Applicable package interface types | Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | PACKAGE_REGISTER.csv row PKG-093 |

## Construction

| Item | Value | Source |
|---|---|---|
| EPC Integrator scope (governing this deliverable) | Integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | PACKAGE_REGISTER.csv row PKG-093 |
| Package Vendor scope (boundary) | Package engineering, package design, vendor documentation, and physical equipment package | PACKAGE_REGISTER.csv row PKG-093 |
| Anchor artifacts produced | Construction Work Package narrative; Installation and Tie-in Workface Plan; Construction Interface and Turnover Checklist | DELIVERABLE_REGISTER.csv row DEL-093-03 |
| Foundation and structural basis | Tank foundations sized for SG 1.25 design basis (TBC) and -40 deg C minimum ambient | ASSUMPTION derived from DBM; final values TBD |
| Inspection / turnover scope | API 650 hydrostatic test, tank shell weld inspection, settlement survey, coating/lining acceptance | ASSUMPTION (API 650 conventional set); clause-level location TBD |
| Tie-in interfaces (per package interface types) | Process piping to/from produced-water transfer pumps and H2O2 treatment; vent/relief; spill containment; grounding/bonding; CP; cabling; site drainage | PACKAGE_REGISTER.csv row PKG-093; DBM Produced Water section |

## References

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Site Basis; Raw Gas and Water Design Conditions; Condensate and Produced-Water Receipts; Produced Water)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (row PKG-093)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row DEL-093-03)
- 26020-Package_Requirements.docx package heading 45 (binary; clause-level slice not text-accessible this run — location TBD)
- API 650 (Welded Tanks for Oil Storage) — referenced by package name; clause set TBD
