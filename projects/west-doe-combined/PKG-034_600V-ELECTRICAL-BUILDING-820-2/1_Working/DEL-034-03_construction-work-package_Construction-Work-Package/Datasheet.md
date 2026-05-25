# Datasheet: DEL-034-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-034-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-034` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 600V ELECTRICAL BUILDING (820-2) | Workbook Packages row 36; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 34 / row 36 | Workbook Packages row 36; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 36; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-025 | Workbook Packages row 36; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 36; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-034` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Construction scope role | EPC Integrator construction-facing deliverable for physically installing, building, inspecting, turning over, and tying the `PKG-034` 600V Electrical Building (820-2) package into the larger facility systems. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-034-03_construction-work-package` |
| Artifact set | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist. | `_CONTEXT.md`; `ARTIFACT_REGISTER.csv` rows `ART-C0421485B2`, `ART-73E810858A`, `ART-EEB94D0E0D` |
| Package class | Vendor-owned Electrical package installed by EPC construction scope. | `PACKAGE_REGISTER.csv` row `PKG-034` |
| Package function | 600V electrical building (substation/MCC building) serving WBS 02 (820-2) scope. | Workbook Packages row 36 |
| Service basis (for installation context) | DBM identifies electrical buildings as houses for MV/LV distribution, MCC, UPS, battery banks, and control/protection equipment supporting the project electrical voltage hierarchy (including 600V class distribution). Package-specific equipment population is TBD pending vendor data. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical buildings and electrical voltage/service paragraphs |
| Installation location | TBD. Source material confirms that the project includes electrical buildings within WBS 02 (820-series) but does not assign `PKG-034` to a specific plot-plan coordinate, area, or orientation. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical buildings paragraph |
| Modularization basis | TBD. No package-specific modularization, shipping-split, transport, or set-on-foundation decision for `PKG-034` is recorded in accessible source material. Electrical buildings are commonly pre-fabricated/modular, but this is ASSUMPTION until confirmed. | Source gap |
| Construction scope alignment | Civil and infrastructure includes electrical buildings; construction scope includes electrical buildings, home-run cabling, terminations, and field interconnections. Applicability to `PKG-034` installation shall be confirmed by detailed design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, civil/infrastructure and construction scope summary |

## Conditions

| Interface / condition | Construction-facing basis | Source |
|---|---|---|
| Utility Piping | Applicable interface for `PKG-034`; installation must coordinate utility piping tie-ins (e.g., services to the building) with the facility utility scope. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-FC0F34096E` |
| Drain / Containment | Applicable interface for `PKG-034`; building drain and containment connections to facility systems shall be coordinated during installation. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-E270A479B8` |
| Electrical Power | Applicable interface for `PKG-034`; installation must respect facility electrical feeder, distribution, and ground-grid interfaces to the 600V building. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-0E87B7BCE6` |
| Grounding / Bonding | Applicable interface for `PKG-034`; major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. Package-specific conductor sizes are TBD. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-46D2497CB7`; DBM grounding and bonding paragraphs |
| Area / Exterior Lighting | Applicable interface for `PKG-034`; building exterior lighting tie-ins to facility lighting scope shall be coordinated during installation. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-63A70A25C3` |
| I&C / Control Cabling | Applicable interface for `PKG-034`; installation shall coordinate control cabling tie-ins between building distribution and facility I&C scope. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-5EA9F4B39F` |
| Communications / Network | Applicable interface for `PKG-034`; installation shall coordinate communications/network tie-ins to facility communication scope. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-1333B6962E` |
| Building HVAC / Services | Applicable interface for `PKG-034`; installation shall coordinate building HVAC and service tie-ins with facility HVAC and services scope. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-DA391B1AF1` |
| Fire & Gas / Safety Systems | Applicable interface for `PKG-034`; installation shall coordinate F&G and safety-system tie-ins with the facility fire and gas scope. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-94BF4E7C7C` |
| Maintenance Access | Applicable interface for `PKG-034`; cable tray and conduit routing shall not interfere with maintenance access; physical placement shall preserve operator/maintainer access to building equipment. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-CAE509DDFA`; DBM cable tray and conduit paragraphs |
| Grading / Site Drainage / Spill Containment | Applicable interface for `PKG-034`; site grading, drainage, and spill containment around the electrical building shall be coordinated with civil/site scope. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-7BD20E62E6` |
| Structural / Foundations / Supports | Applicable interface for `PKG-034`; foundation, pile, settlement, frost protection, site preparation, and structural-support requirements shall be confirmed against the final geotechnical report. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-EC6DF8B5D4`; DBM geotechnical paragraph |
| Construction sequencing | Construction work package shall align to the plot plan, equipment list, and construction work package register before issue for construction. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, miscellaneous facilities/issue-for-construction paragraph |
| Area classification / hazardous-area constraints | Outdoor pipe racks and general areas are non-hazardous unless detailed area classification drawings identify otherwise; installation methods, conduit sealing, building penetrations, and material selection shall respect the area classification assigned at detailed design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, area classification paragraphs |
| Climate / environmental basis | Roads and site-handling provisions shall accommodate the -40 deg C winter operation basis; installation method, building set sequence, and material selection shall respect this basis. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, roads/environment paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package fabrication and supply | Package Vendor responsibility (vendor-owned Electrical package). | `PACKAGE_REGISTER.csv` row `PKG-034` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-034` |
| Construction work package artifact | Integrator-authored construction work package for physical installation, construction, and tie-in to larger systems. | `ARTIFACT_REGISTER.csv` row `ART-C0421485B2` |
| Installation and tie-in workface plan | Workface-planning evidence for installing/building the package and connecting it to adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable. | `ARTIFACT_REGISTER.csv` row `ART-73E810858A` |
| Construction interface and turnover checklist | Construction-facing interface, tie-in, inspection, and turnover evidence for the approved package. | `ARTIFACT_REGISTER.csv` row `ART-EEB94D0E0D` |
| Civil / foundations / supports | Site grading, foundations, electrical buildings, pipe racks, and field interconnections are inside construction scope; package-specific foundation and support detail is TBD pending detailed design and geotechnical confirmation. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, civil/infrastructure and geotechnical paragraphs |
| Electrical installation work | Home-run cabling, terminations, and field interconnections fall inside the construction scope. Package-specific feeder routing, cable sizing, ground-conductor sizing, conduit, and termination details are TBD. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, construction scope summary; DBM grounding/cable tray/conduit paragraphs |
| Module set / hookup | Offloading and setting of modules and mechanical hookups are in construction scope. Package-specific shipping splits, lifting plans, building-set sequence, and hookup steps for the 600V electrical building are TBD. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, construction scope summary |
| Inspection and test | Inspection scope shall confirm installation against the construction work package, the package interface requirements matrix, and vendor turnover documentation. Specific QA/QC checklists, ITPs, and hold points are TBD pending vendor and EPC inspection plans. | Source gap; `_REFERENCES.md` |
| Turnover and acceptance | Construction interface and turnover checklist supports the downstream EPC Vendor Package Review and Acceptance (`DEL-034-06`). Turnover content depends on vendor document turnover (`DEL-034-05`) and package datasheet (`DEL-034-02`). | `DELIVERABLE_REGISTER.csv` rows `DEL-034-05`, `DEL-034-06`; `ARTIFACT_REGISTER.csv` row `ART-EEB94D0E0D` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-034-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-034`.
- `ARTIFACT_REGISTER.csv`, rows `ART-C0421485B2`, `ART-73E810858A`, `ART-EEB94D0E0D` for `DEL-034-03_construction-work-package`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-034` (`IFC-FC0F34096E`, `IFC-E270A479B8`, `IFC-0E87B7BCE6`, `IFC-46D2497CB7`, `IFC-63A70A25C3`, `IFC-5EA9F4B39F`, `IFC-1333B6962E`, `IFC-DA391B1AF1`, `IFC-94BF4E7C7C`, `IFC-CAE509DDFA`, `IFC-7BD20E62E6`, `IFC-EC6DF8B5D4`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-034-03_construction-work-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 36.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, construction scope, civil/infrastructure, electrical voltage/service table, electrical buildings, grounding, cable tray, conduit, geotechnical, area classification, and issue-for-construction source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific 600V electrical building construction content; no `PKG-034` match found.
