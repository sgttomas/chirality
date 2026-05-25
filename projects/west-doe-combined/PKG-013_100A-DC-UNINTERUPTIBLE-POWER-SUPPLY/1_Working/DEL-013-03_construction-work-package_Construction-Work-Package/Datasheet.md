# Datasheet: DEL-013-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-013-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-013` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 100A DC UNINTERUPTIBLE POWER SUPPLY | Workbook Packages row 15; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 13 / row 15 | Workbook Packages row 15; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 15; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-004 | Workbook Packages row 15; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 15; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-013` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Construction scope role | EPC Integrator construction-facing deliverable for physically installing, building, inspecting, turning over, and tying the `PKG-013` UPS package into the larger facility systems. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-013-03_construction-work-package` |
| Artifact set | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist. | `_CONTEXT.md`; `ARTIFACT_REGISTER.csv` rows `ART-66584B5974`, `ART-614F88809C`, `ART-D370CE5716` |
| Package class | Vendor-owned Electrical package installed by EPC construction scope. | `PACKAGE_REGISTER.csv` row `PKG-013` |
| Package function | 100A DC uninterruptible power supply package. | Workbook Packages row 15 |
| UPS service basis (for installation context) | 120 VAC / 125 VDC UPS services supporting the control system, selected emergency/critical lighting, MV breaker control, and MV protective relay loads. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical voltage/service table |
| Installation location | TBD. Source material confirms that electrical buildings may house UPS systems but does not assign `PKG-013` to a specific building, room, skid, or outdoor location. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical buildings paragraph |
| Modularization basis | TBD. No package-specific modularization, shipping-split, or self-framing-enclosure decision for `PKG-013` is recorded in accessible source material. | Source gap |
| Construction scope alignment | Civil and infrastructure includes electrical buildings; construction scope includes electrical buildings, home-run cabling, terminations, and field interconnections. Applicability to `PKG-013` installation shall be confirmed by detailed design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, civil/infrastructure and construction scope summary |

## Conditions

| Interface / condition | Construction-facing basis | Source |
|---|---|---|
| Electrical Power | Applicable interface for `PKG-013`; installation must respect facility electrical feeder, distribution, and ground-grid interfaces. | Workbook Packages row 15; `INTERFACE_REGISTER.csv` `IFC-3B1ED82A25` |
| Grounding / Bonding | Applicable interface for `PKG-013`; major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. Package-specific conductor sizes are TBD. | Workbook Packages row 15; `INTERFACE_REGISTER.csv` `IFC-8093ECDA51`; DBM grounding and bonding paragraphs |
| Maintenance Access | Applicable interface for `PKG-013`; cable tray and conduit routing shall not interfere with maintenance access; physical placement shall preserve operator/maintainer access. | Workbook Packages row 15; `INTERFACE_REGISTER.csv` `IFC-DA9E0BAB70`; DBM cable tray and conduit paragraphs |
| Structural / Foundations / Supports | Applicable interface for `PKG-013`; foundation, pile, settlement, frost protection, site preparation, and structural-support requirements shall be confirmed against the final geotechnical report. | Workbook Packages row 15; `INTERFACE_REGISTER.csv` `IFC-CAE19AED68`; DBM geotechnical paragraph |
| Construction sequencing | Construction work package shall align to the plot plan, equipment list, and construction work package register before issue for construction. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, miscellaneous facilities/issue-for-construction paragraph |
| Area classification / hazardous-area constraints | Outdoor pipe racks and general areas are non-hazardous unless detailed area classification drawings identify otherwise; installation methods, conduit sealing, and material selection shall respect the area classification assigned at detailed design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, area classification paragraphs |
| Climate / environmental basis | Roads and site-handling provisions shall accommodate the -40 deg C winter operation basis; installation method and material selection shall respect this basis. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, roads/environment paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package fabrication and supply | Package Vendor responsibility (vendor-owned Electrical package). | `PACKAGE_REGISTER.csv` row `PKG-013` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-013` |
| Construction work package artifact | Integrator-authored construction work package for physical installation, construction, and tie-in to larger systems. | `ARTIFACT_REGISTER.csv` row `ART-66584B5974` |
| Installation and tie-in workface plan | Workface-planning evidence for installing/building the package and connecting it to adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable. | `ARTIFACT_REGISTER.csv` row `ART-614F88809C` |
| Construction interface and turnover checklist | Construction-facing interface, tie-in, inspection, and turnover evidence for the approved package. | `ARTIFACT_REGISTER.csv` row `ART-D370CE5716` |
| Civil / foundations / supports | Site grading, foundations, electrical buildings, pipe racks, and field interconnections are inside construction scope; package-specific foundation and support detail is TBD pending detailed design and geotechnical confirmation. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, civil/infrastructure and geotechnical paragraphs |
| Electrical installation work | Home-run cabling, terminations, and field interconnections fall inside the construction scope. Package-specific feeder routing, cable sizing, ground-conductor sizing, conduit, and termination details are TBD. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, construction scope summary; DBM grounding/cable tray/conduit paragraphs |
| Module set / hookup | Offloading and setting of modules and mechanical hookups are in construction scope. Package-specific shipping splits, lifting plans, and hookup steps for the UPS package are TBD. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, construction scope summary |
| Inspection and test | Inspection scope shall confirm installation against the construction work package, the package interface requirements matrix, and vendor turnover documentation. Specific QA/QC checklists, ITPs, and hold points are TBD pending vendor and EPC inspection plans. | Source gap; `_REFERENCES.md` |
| Turnover and acceptance | Construction interface and turnover checklist supports the downstream EPC Vendor Package Review and Acceptance (`DEL-013-06`). Turnover content depends on vendor document turnover (`DEL-013-05`) and package datasheet (`DEL-013-02`). | `DELIVERABLE_REGISTER.csv` rows `DEL-013-05`, `DEL-013-06`; `ARTIFACT_REGISTER.csv` row `ART-D370CE5716` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-013-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-013`.
- `ARTIFACT_REGISTER.csv`, rows `ART-66584B5974`, `ART-614F88809C`, `ART-D370CE5716` for `DEL-013-03_construction-work-package`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-013` (`IFC-3B1ED82A25`, `IFC-8093ECDA51`, `IFC-DA9E0BAB70`, `IFC-CAE19AED68`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-013-03_construction-work-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 15.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, construction scope, civil/infrastructure, electrical voltage/service table, electrical buildings, grounding, cable tray, conduit, geotechnical, area classification, and issue-for-construction source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific UPS construction content; no `PKG-013` match found.
