# Datasheet: DEL-035-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-035-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-035` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1) | Workbook Packages row 37; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 35 / row 37 | Workbook Packages row 37; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 37; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-026 | Workbook Packages row 37; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 37; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-035` |
| Covers scope item | `SOW-0036` | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Supports objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `OBJECTIVE_SCOPE_MAP.csv` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package (prefabricated modular Electrical Building 810-1 housing the 13.8 kV main switchgear) | `PACKAGE_REGISTER.csv` row `PKG-035`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Function within the facility | Houses the 13.8 kV main switchgear that serves as the plant main power distribution center, distributing power radially through step-down transformers to other facility electrical buildings. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "The 13.8 kV switchgear shall be designed, purchased, and installed as the plant main power distribution center." |
| Incoming supply basis | Utility supply feeds a 25 kV to 13.8 kV, 50 MVA utility-supplied transformer that steps down to the 13.8 kV switchgear; bus shall be sized for the full facility scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, facility electrical system paragraph |
| Distribution voltage | 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded medium-voltage facility backbone distribution. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical service voltages table |
| Building format | Prefabricated, modular, shop-built Electrical Building (810-1), elevated on piles with space beneath for bottom-entry cabling; climate controlled with n+1 HVAC. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraphs; building list row "810-1 13.8kV Switchgear Electrical Building". |
| Construction location of building | Building 810-1 fabricated in Shop per the buildings list; field installation occurs at its designated facility location. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, buildings list row "810-1" marked Shop |
| Tie-in cables | 13.8 kV medium-voltage cables shall be three-conductor copper TECK cable rated 15 kV with 133 percent insulation, shielded; entry to the building shall be bottom-entry. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable schedule and Electrical Buildings paragraphs |

## Conditions

Each interface fact below is asserted at PKG-035 by the workbook and the Gate 7 interface register, and is in scope of this Construction Work Package as an installation, tie-in, or turnover activity.

| Interface (PKG-035) | Construction-relevant condition | Source |
|---|---|---|
| Electrical Power | EPC Integrator installs and tie-ins incoming 25 kV / 13.8 kV utility feed and outgoing radial 13.8 kV feeders to other facility electrical buildings; coordinate energization sequence with Package Vendor. | `INTERFACE_REGISTER.csv` `IFC-A5EF521315`; DBM "13.8 kV switchgear shall be designed, purchased, and installed as the plant main power distribution center" |
| Grounding / Bonding | Building and switchgear directly connected to the ground grid at two points; ground wells at electrical buildings provided for maintenance and operational testing; above-grade ground conductors green insulated in PVC conduit where mechanical protection is required; ground connections compression type. | `INTERFACE_REGISTER.csv` `IFC-C11BBF56CD`; DBM grounding and bonding paragraphs |
| Utility Piping | Construction interface listed at PKG-035; package-specific utility piping tie-in scope at Building 810-1 is TBD pending detailed source slice. | `INTERFACE_REGISTER.csv` `IFC-C8A7133D59`; Workbook Packages row 37 |
| Drain / Containment | Construction interface listed at PKG-035; package-specific drain/containment tie-in scope is TBD. | `INTERFACE_REGISTER.csv` `IFC-231DB0CBFA`; Workbook Packages row 37 |
| Area / Exterior Lighting | Construction interface listed at PKG-035; exterior lighting tie-in to 810-1 is TBD. | `INTERFACE_REGISTER.csv` `IFC-EB2FA7BDE6` |
| I&C / Control Cabling | Bottom-entry I&C and control cabling routed in cable trays per DBM cable/raceway basis; coordinate with PLC/network rack equipment housed in electrical buildings. | `INTERFACE_REGISTER.csv` `IFC-9214AEAF28`; DBM Electrical Buildings, cable tray paragraphs |
| Communications / Network | Network rack provisions inside electrical buildings; site network tie-in is TBD. | `INTERFACE_REGISTER.csv` `IFC-00317770B3`; DBM Electrical Buildings paragraph |
| Building HVAC / Services | HVAC sized n+1 so cooling can tolerate failure or maintenance shutdown of one unit without affecting heating/cooling; turnover includes HVAC commissioning. | `INTERFACE_REGISTER.csv` `IFC-73CF283A27`; DBM Electrical Buildings HVAC paragraph |
| Fire & Gas / Safety Systems | Building located in general-purpose area; F&G tie-in scope to 810-1 is TBD pending detailed source slice. | `INTERFACE_REGISTER.csv` `IFC-C00E60F032`; DBM area classification paragraph |
| Maintenance Access | Equipment doors sized for or include removable transom sections to allow removal of the largest equipment; outdoor GFI receptacle provided for exterior maintenance; cable tray/conduit routing shall not interfere with maintenance access. | `INTERFACE_REGISTER.csv` `IFC-A3B2DADC44`; DBM Electrical Buildings paragraphs |
| Grading / Site Drainage / Spill Containment | Building elevated and installed on piles; site grading and drainage at the 810-1 location coordinated with civil works. | `INTERFACE_REGISTER.csv` `IFC-589CAC7BC6`; DBM Electrical Buildings paragraph |
| Structural / Foundations / Supports | Building installed on piles; structural design coordinated with civil/structural package. Package-specific pile/foundation criteria are TBD pending civil/structural source slice. | `INTERFACE_REGISTER.csv` `IFC-A5DBFBF436`; DBM Electrical Buildings paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering, design, fabrication, vendor documentation | Package Vendor responsibility; not in EPC Integrator Construction Work Package scope. | `PACKAGE_REGISTER.csv` row `PKG-035` |
| Receiving and setting Electrical Building 810-1 | Building shop-built; EPC Integrator receives, transports to site, and sets on prepared pile foundations. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, building list "810-1 ... Shop"; Electrical Buildings paragraph |
| Power tie-ins | EPC Integrator constructs incoming utility feed from the 25 kV / 13.8 kV transformer to switchgear and outgoing radial 13.8 kV feeders to dependent electrical buildings; bottom-entry cabling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, facility electrical system and Electrical Buildings paragraphs |
| Grounding installation | Connect building and switchgear to the ground grid at two points; install ground wells, test points, and above-grade conductors per DBM. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Cable tray and conduit | Field-run cable tray limited to field-constructed portions (tank farm, interconnecting trays between main pipe racks, process skids, and electrical buildings); 13.8 kV cables three-conductor TECK rated 15 kV with 133% insulation, shielded. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and cable schedule paragraphs |
| Inspection and turnover | Construction interface and turnover checklist is an anticipated artifact for this deliverable. | `DELIVERABLE_REGISTER.csv` row `DEL-035-03_construction-work-package` |
| Vendor witness/coordination | Coordinate Package Vendor witness points (FAT/SAT, energization sequence, protection settings verification) with EPC Integrator construction schedule. | ASSUMPTION: derived from Package Vendor / EPC Integrator split in `PACKAGE_REGISTER.csv`; package-specific witness points are TBD |
| Building HVAC commissioning | n+1 HVAC commissioned prior to energization. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings HVAC paragraph |
| Final tie-in points and energization | Energization of the 13.8 kV bus is the gating tie-in for downstream electrical buildings (6.9 kV, 4.16 kV, 600 V buildings) per the radial distribution basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Power from the 13.8 kV switchgear shall be distributed radially through step-down transformers to: ..." |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-035-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-035`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-035`.
- `SCOPE_LEDGER.csv`, row `SOW-0036`.
- `OBJECTIVE_SCOPE_MAP.csv`, rows for `SOW-0036` / `PKG-035`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 37.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis (facility electrical system, Electrical Buildings, grounding, cable tray, cable schedule paragraphs; buildings list row "810-1 13.8kV Switchgear Electrical Building").
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific 13.8 kV switchgear / Building 810-1 content; no PKG-035-specific package-requirements match was identified.
