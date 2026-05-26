# Specification — DEL-088-01 Scope of Work (PKG-088 Caustic Treating, Condensate Mercaptan Removal)

## Scope

### In Scope

This Scope of Work covers the EPC Integrator's whole-facility integration of the Caustic Treating (Condensate Mercaptan Removal) package, PKG-088 (tag 26020-02-PT-27-001), into the 03-25 Compressor Station and Liquids Hub. It comprises:

- Package identity and tagged-equipment definition (see `Datasheet.md`).
- Package function and process-integration narrative (mercaptan removal from C5+ condensate, non-regenerative caustic technology, Merichem or equivalent). [Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating]
- Package boundaries and applicable interfaces with the larger facility: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. [Source: PACKAGE_REGISTER.csv]
- Responsibility allocation: Package Vendor (engineering, design, vendor documentation, physical equipment package) vs. EPC Integrator (facility integration, interfaces, tie-ins, constructability, procurement/construction coordination). [Source: PACKAGE_REGISTER.csv]
- Coverage of scope items SOW-0055, SOW-0056, SOW-0057, SOW-0058. [Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv]

### Out of Scope

- Detailed package engineering, package design, vendor documentation, and the physical equipment package itself — owned by Package Vendor (see DEL-088-04 Vendor Engineered Equipment Package). [Source: PACKAGE_REGISTER.csv]
- Vendor document register and turnover records — covered by DEL-088-05. [Source: DELIVERABLE_REGISTER.csv]
- Construction installation/tie-in workface planning — covered by DEL-088-03 Construction Work Package. [Source: DELIVERABLE_REGISTER.csv]
- Vendor package review and acceptance evidence — covered by DEL-088-06. [Source: DELIVERABLE_REGISTER.csv]
- Caustic regeneration: explicitly not in the 03-25 basis. [Source: DBM-Comp_and_Liquids §Condensate Mercaptan Treating]
- Sales condensate LACT scope (third-party NRM); 03-25 scope ends at facility-side tie-in flange. [Source: DBM-Comp_and_Liquids §Process Overview]
- Package-specific exclusions beyond those above: TBD; no package-specific exclusions stated in source materials. [Source: PACKAGE_REGISTER.csv Exclusions]

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| SOW-R-01 | The Scope of Work shall identify the package by PackageID (PKG-088) and PackageTag (26020-02-PT-27-001) and list all package-level tagged equipment as defined in `Datasheet.md`. | `_CONTEXT.md` Anticipated Artifacts |
| SOW-R-02 | The Scope of Work shall describe the package function: non-regenerative caustic treating of 20,000 bbl/d C5+ condensate for mercaptan removal, with continuous fresh caustic and make-up water consumption and spent caustic / DSO production. | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| SOW-R-03 | The Scope of Work shall declare that caustic regeneration is excluded from the 03-25 basis. | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| SOW-R-04 | The Scope of Work shall enumerate the applicable interface types listed in PACKAGE_REGISTER.csv and identify each as a Package Vendor / EPC Integrator boundary. | PACKAGE_REGISTER.csv (InterfaceTypes) |
| SOW-R-05 | The Scope of Work shall include a responsibility assignment record allocating engineering, design, vendor documentation, and physical equipment to the Package Vendor, and facility integration, interfaces, tie-ins, constructability, and procurement/construction coordination to the EPC Integrator. | PACKAGE_REGISTER.csv (IntegrationModel); `_CONTEXT.md` ResponsibleParty |
| SOW-R-06 | The Scope of Work shall record the source basis and traceability: Workbook Packages row 50; `26020-Package_Requirements.docx` package heading 41; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md. | `_REFERENCES.md`; PACKAGE_REGISTER.csv |
| SOW-R-07 | The Scope of Work shall reflect whole-facility integration: vapour to incinerator header via flame arrestor; LP fuel-gas blanket on caustic tanks; spent caustic truck-out; fresh caustic NOT connected to VRU; aluminum prohibited in the caustic building. | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| SOW-R-08 | The Scope of Work shall reference the four Gate-5 EPC anchor deliverables for PKG-088 (DEL-088-01 through DEL-088-06) and explicitly call out that detailed datasheet, construction work package, vendor engineered equipment, vendor document turnover, and vendor package review/acceptance are carried by their respective deliverables. | DELIVERABLE_REGISTER.csv |
| SOW-R-09 | The Scope of Work shall cover SOW-0055, SOW-0056, SOW-0057, and SOW-0058. Mapping of each SOW item to package scope sections: TBD pending Scope-Item register slice. | `_CONTEXT.md` Covers Scope Items (location TBD for item-level text) |
| SOW-R-10 | The Scope of Work shall state objective association as informational context (OBJ-002 through OBJ-010) and label it ASSUMPTION (package-grouping heuristic) until a per-deliverable objective map is confirmed. | OBJECTIVE_DELIVERABLE_MAP.csv; `_CONTEXT.md` |

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| 26020-Package_Requirements.docx heading 41 | Authoritative package requirements text for PKG-088 | location TBD (binary not parsed) |
| 26020-Packages_Interfaces_4_export.xlsx | Authoritative interface register companion | location TBD (binary not parsed) |
| DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md | Design Basis Memorandum: process function, treating basis, conditions, drains, fuel gas, mercaptan toxicity | Accessible; cited above |
| API 650 | Atmospheric tank construction standard (caustic and DSO tanks are atmospheric per DBM) | ASSUMPTION: applicable; clause-level reference TBD |
| ANSI 300# | Minimum caustic drain header flange rating | DBM-Comp_and_Liquids §Drains |

## Verification

| Req ID | Verification approach |
|---|---|
| SOW-R-01 | Document review: confirm package and equipment identity match `Datasheet.md` and PACKAGE_REGISTER.csv. |
| SOW-R-02, SOW-R-03 | Document review against DBM-Comp_and_Liquids §Condensate Mercaptan Treating. |
| SOW-R-04 | Cross-check applicable interface types against PACKAGE_REGISTER.csv (InterfaceTypes column) and INTERFACE_REGISTER.csv rows scoped to PKG-088. |
| SOW-R-05 | Inspection of responsibility assignment record (RACI/equivalent) for completeness across vendor and integrator roles. |
| SOW-R-06 | Traceability check: each substantive section cites a source path and section reference. |
| SOW-R-07 | Cross-check facility integration statements against the DBM and against `26020-Package_Requirements.docx` heading 41 once that slice is accessible (location TBD). |
| SOW-R-08 | Cross-reference deliverable links to DEL-088-02 through DEL-088-06 in DELIVERABLE_REGISTER.csv. |
| SOW-R-09 | Map each SOW item (SOW-0055..SOW-0058) to a Scope of Work section once the Scope-Item register slice is available. |
| SOW-R-10 | Confirm objective association is labelled ASSUMPTION until human ruling. |

## Documentation

Anticipated artifacts comprising this deliverable (`_CONTEXT.md`):

- Package scope of work document (this Specification's narrative content, formatted for EPC issue).
- Tagged equipment and package identity list (see `Datasheet.md`).
- Package function and integration narrative (see `Guidance.md`).
- Responsibility assignment record (see `Procedure.md` Step "Build responsibility assignment record" and supporting tables).
