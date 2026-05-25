# Datasheet: DEL-023-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-023-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-023` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 23 / row 25 | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-014 | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 25; `_CONTEXT.md` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-023` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package (MV VFD) | `PACKAGE_REGISTER.csv` row `PKG-023` |
| Package function | Medium-voltage variable-frequency drive package, 1500 HP, 4160 V, 3-phase, 60 Hz, with 4160 V VFD topology. | Workbook Packages row 25; `PACKAGE_REGISTER.csv` |
| Turnover scope | Vendor document register, vendor document submittals, source-required vendor documentation, and turnover records. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-023-05_vendor-document-turnover-package` |
| Vendor document register basis | TBD. Detailed vendor-document requirements are not present in the current source material for this package. | `ARTIFACT_REGISTER.csv` row `ART-950E899C01` (Vendor Documentation Gap Evidence) |
| Voltage class context | MV VFD service falls within the DBM-recognized 4.16 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded medium-voltage service for AC inverter-drive motors rated 250 hp up to 5,500 hp. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage and service table |
| MV VFD design-basis context | DBM electrical section identifies MV VFDs as equipment that may be housed in electrical buildings; specific 4.16 kV VFD/soft-starter requirements are TBD per DBM. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph; 4.16 kV MCC paragraph |
| Document submittal log basis | TBD. No package-specific submittal index, document numbering plan, or transmittal template was found in the accessible source set. | Source gap; `_REFERENCES.md` |
| Turnover record basis | TBD. No package-specific turnover record list (e.g., FAT reports, mill certs, calibration records, as-built drawings) was found in the accessible source set. | Source gap; `_REFERENCES.md` |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-023; vendor documentation shall include electrical power interface evidence. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-2F6B2D3B80` |
| Grounding / Bonding | Interface fact applies to PKG-023; vendor documentation shall include grounding/bonding evidence. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-CEF43B776E` |
| I&C / Control Cabling | Interface fact applies to PKG-023; vendor documentation shall include I&C/control-cabling interface evidence. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-488756F914` |
| Communications / Network | Interface fact applies to PKG-023; vendor documentation shall include communications/network interface evidence (e.g., Ethernet to plant PLC). | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-FF4188D90D` |
| Maintenance Access | Interface fact applies to PKG-023; vendor documentation shall include maintenance-access evidence. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-38BEE3F6CC` |
| Structural / Foundations / Supports | Interface fact applies to PKG-023; vendor documentation shall include foundation/support load and anchorage evidence. | Workbook Packages row 25; `INTERFACE_REGISTER.csv` `IFC-0AED039BBE` |
| Plant PLC communication | DBM requires MV MCC equipment to provide an Ethernet communication port to the plant PLC central control panel; vendor documentation for the MV VFD shall reflect equivalent integration evidence where applicable. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV / 4.16 kV MCC paragraphs (ASSUMPTION: applicability to MV VFD specifically is TBC) |
| Area classification marking | DBM requires VFD-fed motors located in Zone 2 areas to be marked accordingly and supplied with a temperature code lower than specified; vendor documentation shall provide equivalent VFD package area-classification and temperature-code marking evidence where applicable. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, VFD/area classification paragraph (ASSUMPTION: area classification of PKG-023 is TBD) |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor documentation authorship | Package Vendor. | `PACKAGE_REGISTER.csv` row `PKG-023`; `_CONTEXT.md` |
| EPC review of vendor documentation | EPC Integrator interface/integration review. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Vendor document register | TBD index of vendor documents required for this package (e.g., GA drawings, schematics, datasheets, FAT/SAT procedures, IOM manuals, spare parts list, recommended spares, vendor specifications, certifications, test reports, drive-tuning records). | `ARTIFACT_REGISTER.csv` row `ART-950E899C01`; source-content for the index itself is TBD |
| Submittal handling | TBD. Submittal transmittal numbering, revision control, EPC document control acceptance criteria, and submittal cycle are not source-defined for this package. | Source gap |
| Turnover records | TBD. Specific turnover record list (FAT, SAT, mill certs, calibration, factory test, drive commissioning records, as-built drawings, training records) is not source-defined for this package. | Source gap |
| Installation location | TBD. DBM identifies MV VFDs as electrical-building-eligible equipment but does not assign PKG-023 to a specific building, room, skid, or outdoor location. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers and shared source root.
- `DELIVERABLE_REGISTER.csv`, row `DEL-023-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-023`.
- `ARTIFACT_REGISTER.csv`, row `ART-950E899C01` (TBD vendor document register; Vendor Documentation Gap Evidence).
- `INTERFACE_REGISTER.csv`, rows for `PKG-023` (`IFC-2F6B2D3B80`, `IFC-CEF43B776E`, `IFC-488756F914`, `IFC-FF4188D90D`, `IFC-38BEE3F6CC`, `IFC-0AED039BBE`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-023-05_vendor-document-turnover-package` (package-grouping heuristic; ASSUMPTION).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 25.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical voltage/service table; 4.16 kV MCC paragraphs; electrical buildings paragraph; VFD/area-classification paragraph.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific MV VFD vendor-documentation content; no PKG-023 vendor-document index was located.
