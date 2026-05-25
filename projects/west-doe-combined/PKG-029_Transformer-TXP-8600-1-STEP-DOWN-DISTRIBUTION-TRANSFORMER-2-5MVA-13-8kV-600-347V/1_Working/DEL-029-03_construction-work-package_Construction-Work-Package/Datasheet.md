# Datasheet: DEL-029-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-029-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-029` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V | Workbook Packages row 31; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 29 / row 31 | Workbook Packages row 31; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 31; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-020 | Workbook Packages row 31; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 31; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-029` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Construction scope role | EPC Integrator construction-facing deliverable for physically installing, building, inspecting, turning over, and tying the `PKG-029` step-down distribution transformer package into the larger facility systems. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-029-03_construction-work-package` |
| Artifact set | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist. | `_CONTEXT.md`; `ARTIFACT_REGISTER.csv` rows `ART-C18BB35507`, `ART-A14748BEA0`, `ART-15977E3467` |
| Package class | Vendor-owned Electrical package installed by EPC construction scope. | `PACKAGE_REGISTER.csv` row `PKG-029` |
| Package function | Step-down distribution transformer, tag TXP-8600-1, nameplate 2.5 MVA, primary 13.8 kV, secondary 600/347 V per workbook identity. The 600 V secondary aligns with the Deepcut facility LV service basis; the 347 V phase-to-neutral relationship and specific winding/connection details are TBD pending vendor data or detailed electrical source. | Workbook Packages row 31; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage table and incoming-power/transformer paragraphs |
| Installation location | TBD. Source material confirms electrical buildings may house transformer-related distribution equipment and that large oil-filled transformers are spaced and installed on structural steel transformer bases per CEC, but does not assign `PKG-029` (TXP-8600-1) to a specific building, pad, or location. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers and electrical-buildings paragraphs |
| Construction support basis | Transformers will generally be installed on structural steel transformer bases; large oil-filled transformers are spaced in accordance with CEC requirements; secondary containment shall be reviewed and minimized where practical. Applicability of these provisions to TXP-8600-1 (oil-filled vs dry-type, indoor vs outdoor) is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph; geotechnical/foundation paragraph |
| Modularization basis | TBD. No package-specific modularization, shipping-split, or self-framing-enclosure decision for `PKG-029` is recorded in accessible source material. | Source gap |
| Construction scope alignment | Civil and infrastructure includes electrical buildings; construction scope includes electrical buildings, transformer foundations, home-run cabling, terminations, grounding, and field interconnections. Applicability to `PKG-029` installation shall be confirmed by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, civil/infrastructure and construction scope summaries |

## Conditions

| Interface / condition | Construction-facing basis | Source |
|---|---|---|
| Electrical Power | Applicable interface for `PKG-029`; installation must respect facility 13.8 kV primary feed (from upstream MV switchgear) and 600 V secondary distribution interfaces, including feeder routing, terminations, and protection coordination at the tie-in. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` row `IFC-717D0187BA`; DBM incoming-power/transformer paragraphs |
| Grounding / Bonding | Applicable interface for `PKG-029`; major electrical equipment shall be directly connected to the ground grid at two points; ground wells at power transformers shall be provided for maintenance and operational testing; distribution transformers, panelboards, and three-phase motors larger than 100 hp shall have a separate copper ground conductor sized per CEC; 600 V transformers shall be grounded by a 5 A continuous high-resistance grounding resistor. Package-specific conductor sizes, ground-well details, and HRG installation details are TBD. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` row `IFC-C49653E450`; DBM grounding and bonding paragraphs |
| Area / Exterior Lighting | Applicable interface for `PKG-029`; if the package is installed in an outdoor/yard location, area or exterior lighting tie-ins at the pad or enclosure shall be addressed by the construction work package. Specific lighting layout is TBD. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` row `IFC-DFC1A10C2D` |
| I&C / Control Cabling | Applicable interface for `PKG-029`; control wiring (temperature, level, pressure, alarms, protection trips) shall be terminated and tested as part of construction; routing shall separate power and control circuits per DBM. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` row `IFC-A5C9438164`; DBM cable separation paragraph |
| Communications / Network | Applicable interface for `PKG-029`; if the transformer monitoring or protective relaying ties into the plant network, terminations and network drops shall be installed and tested as part of construction. Specific protocol/medium is TBD. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` row `IFC-81CFD2A32C` |
| Maintenance Access | Applicable interface for `PKG-029`; cable tray, conduit routing, and equipment placement shall preserve operator and maintainer access; CEC transformer spacing requirements shall be respected. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` row `IFC-2C14FA1228`; DBM cable tray/conduit and transformer paragraphs |
| Structural / Foundations / Supports | Applicable interface for `PKG-029`; foundations are generally precast concrete bearing foundations or structural steel transformer bases; settlement, frost protection, site preparation, secondary containment review, and structural support requirements shall be confirmed against the final geotechnical report. | Workbook Packages row 31; `INTERFACE_REGISTER.csv` row `IFC-380F4773FB`; DBM transformer foundation/geotechnical paragraphs |
| Construction sequencing | Construction work package shall align to the plot plan, equipment list, and construction work package register before issue for construction. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, miscellaneous facilities/issue-for-construction paragraphs |
| Area classification / hazardous-area constraints | Outdoor pipe racks and general areas are non-hazardous unless detailed area classification drawings identify otherwise; installation methods, conduit sealing, and material selection shall respect the area classification assigned at detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, area classification paragraphs |
| Climate / environmental basis | Installation and material selection shall accommodate the project winter operation basis (cold-climate Deepcut facility); transformer cold-start, oil viscosity, and heater provisions are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, climate/environment paragraphs |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package fabrication and supply | Package Vendor responsibility (vendor-owned Electrical package). | `PACKAGE_REGISTER.csv` row `PKG-029` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-029` |
| Construction work package artifact | Integrator-authored construction work package for physical installation, construction, and tie-in to larger systems. | `ARTIFACT_REGISTER.csv` row `ART-C18BB35507` |
| Installation and tie-in workface plan | Workface-planning evidence for installing/building the package and connecting it to adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable. | `ARTIFACT_REGISTER.csv` row `ART-A14748BEA0` |
| Construction interface and turnover checklist | Construction-facing interface, tie-in, inspection, and turnover evidence for the approved package. | `ARTIFACT_REGISTER.csv` row `ART-15977E3467` |
| Civil / foundations / supports | Transformer foundations are generally precast concrete bearing foundations or structural steel bases; site grading, pad construction, and field interconnections are inside construction scope; package-specific foundation, pad sizing, anchor, and containment details are TBD pending detailed design and geotechnical confirmation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformer foundation, geotechnical, and civil/infrastructure paragraphs |
| Electrical installation work | Home-run MV (13.8 kV) primary cabling, LV (600 V) secondary cabling, terminations, conduit, cable tray, and grounding tie-ins fall inside the construction scope. Package-specific feeder routing, cable type, sizing, conduit, and termination details are TBD. The DBM specifies three-conductor copper TECK 15 kV 133 percent insulated shielded cable for 13.8 kV circuits and ACWU for 600 V transformer secondary circuits, which shall be respected in cable specification. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MV cable and LV secondary cable paragraphs; grounding/cable tray/conduit paragraphs |
| Grounding installation work | Two-point ground-grid connection for the transformer; ground well at the transformer; separate copper ground conductor per CEC for the distribution transformer; HRG installation for the 600 V secondary system. Conductor sizing and ground-well construction details are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs |
| Module set / hookup | Offloading and setting of the transformer, mechanical anchoring, oil filling/testing (if oil-filled), and termination work fall under construction scope. Package-specific lift plan, rigging, oil-handling, and hookup steps are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, construction scope summary; transformers paragraph |
| Inspection and test | Inspection scope shall confirm installation against the construction work package, the package interface requirements matrix, vendor turnover documentation, and applicable field tests (insulation resistance, turns ratio, oil dielectric for oil-filled units). Specific QA/QC checklists, ITPs, and hold points are TBD pending vendor and EPC inspection plans. | Source gap; `_REFERENCES.md` |
| Turnover and acceptance | Construction interface and turnover checklist supports the downstream EPC Vendor Package Review and Acceptance (`DEL-029-06`). Turnover content depends on vendor document turnover (`DEL-029-05`) and package datasheet (`DEL-029-02`). | `DELIVERABLE_REGISTER.csv` rows `DEL-029-05`, `DEL-029-06`; `ARTIFACT_REGISTER.csv` row `ART-15977E3467` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-029-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-029`.
- `ARTIFACT_REGISTER.csv`, rows `ART-C18BB35507`, `ART-A14748BEA0`, `ART-15977E3467` for `DEL-029-03_construction-work-package`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-029` (`IFC-717D0187BA`, `IFC-C49653E450`, `IFC-DFC1A10C2D`, `IFC-A5C9438164`, `IFC-81CFD2A32C`, `IFC-2C14FA1228`, `IFC-380F4773FB`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-029-03_construction-work-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 31.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers, incoming-power, electrical voltage table, electrical buildings, grounding, cable tray, conduit, geotechnical, area classification, MV/LV cable, and issue-for-construction source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific transformer construction content; no `PKG-029` / TXP-8600-1 match found.
