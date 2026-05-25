# Datasheet: DEL-017-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-017-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-017` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 17 / row 19 | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-008 | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 19; `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-017` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Production unit class | Vendor-owned Electrical package — engineering, design, fabrication/supply, and physical equipment package. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-017-04_vendor-engineered-equipment-package` |
| Package function | Medium-voltage variable frequency drive package, nameplate basis 600 HP, 4160 V, 3-phase, 60 Hz, with 4160 V VFD output. | Workbook Packages row 19 (package name) |
| Nominal motor power | 600 HP (package nameplate, per package title). | Workbook Packages row 19 |
| Nominal voltage | 4160 V supply and 4160 V VFD output, 3-phase, 60 Hz. | Workbook Packages row 19 |
| Driven load identification | TBD. No accessible source slice ties this 600 HP / 4160 V MV VFD package to a specific driven motor or tag in `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; the DBM VFD content addresses the 4000 V / 5200 HP inlet compressor motors (KM-2150, KM-2250), not a 600 HP / 4160 V drive. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, sections on motor basis (~line 324), starting basis SCA-001 VE #34 (~line 326), and 4160 V MCC (~line 752) |
| VFD topology / cooling / harmonic mitigation | TBD. Source identifies that VFD sizing, harmonic mitigation, and reactive-power treatment are detailed-design items; no PKG-017-specific topology, cooling method, or filter selection is stated. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160 V MCC paragraph (SCA-001 VE #34, VE #37) |
| Service basis (starting / continuous duty) | The DBM electrical basis treats MV VFDs in the 4160 V MCC context as starting devices for the large inlet compressor motors; continuous-duty vs. start-only operating basis for this 600 HP package is not stated in source and remains TBD pending EPC inputs (`DEL-017-01`, `DEL-017-02`). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, motor basis paragraph and 4160 V MCC paragraph |
| Vendor engineering inputs | EPC Scope of Work (`DEL-017-01`) and Package Datasheet (`DEL-017-02`) form the vendor engineering basis. | `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-017-01_scope-of-work`, `DEL-017-02_package-datasheet` |
| Vendor engineering outputs | Vendor engineered physical equipment package; vendor package design basis and datasheet set. | `_CONTEXT.md`, Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-017-04` |
| 4160 V system context | The 4160 V MCC provides field-fused contactors, motor protection relays, and an EtherNet communication port to the plant PLC central control panel for data acquisition, and serves large 4000 V motors. PKG-017 sits in this 4160 V class system. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160 V MCC paragraph |

## Conditions

| Interface / condition | Vendor package basis | Source |
|---|---|---|
| Electrical Power | Vendor package shall be engineered to the EPC-defined Electrical Power interface (4160 V supply class). | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-5E50E5F700` |
| Grounding / Bonding | Vendor package shall be engineered to the EPC-defined Grounding / Bonding interface. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-1340C6D795` |
| I&C / Control Cabling | Vendor package shall provide the I&C / Control Cabling termination set required for control, status, and protective interface. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-6ECD9C92A1` |
| Communications / Network | Vendor package shall provide the Communications / Network interface (consistent with the DBM-stated EtherNet path from the 4160 V MCC to the plant PLC central control panel for data acquisition). | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-FB4034716A`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160 V MCC paragraph |
| Maintenance Access | Vendor package layout and supply shall preserve the EPC-defined Maintenance Access interface. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-A807F5E0B3` |
| Structural / Foundations / Supports | Vendor package skid/frame/foundation provisions shall be coordinated with the EPC-defined Structural / Foundations / Supports interface. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-34EB597147` |
| Harmonic / reactive power mitigation | The DBM states that harmonic and reactive-power mitigation shall be determined by detailed electrical studies, and that capacitor banks are removed from synchronous bus MCC-8200 where VFDs are present (SCA-001 VE #37). Vendor package harmonic compliance approach shall align with these EPC-defined study outcomes. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160 V MCC paragraph |
| Inverter-duty / motor compatibility | Source motor basis for the 4000 V inlet compressors specifies continuous inverter-duty service with a starting VFD; for a 600 HP / 4160 V driven motor, motor inverter-duty compatibility shall be confirmed by the EPC Package Datasheet (`DEL-017-02`) before vendor engineering finalizes the drive design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, motor basis paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility — engineering, design, fabrication/supply, vendor documentation, and the physical equipment package. | `PACKAGE_REGISTER.csv` row `PKG-017`; `DELIVERABLE_REGISTER.csv` row `DEL-017-04` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility (subject to integration review of the vendor package). | `PACKAGE_REGISTER.csv` row `PKG-017` |
| Installation location | TBD. Source material confirms the 4160 V MCC system context but does not assign PKG-017 to a specific electrical building, room, skid, or outdoor location. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160 V MCC paragraph |
| Foundations / supports | Structural / Foundations / Supports interface applies; package-specific support basis is TBD. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` |
| Vendor documentation set | Captured separately by `DEL-017-05_vendor-document-turnover-package`; this deliverable supplies the engineering, design basis, datasheet set, and physical equipment. | `DELIVERABLE_REGISTER.csv` rows `DEL-017-04`, `DEL-017-05` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-017-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-017`.
- `ARTIFACT_REGISTER.csv`, rows for `PKG-017`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-017` (`IFC-5E50E5F700`, `IFC-1340C6D795`, `IFC-6ECD9C92A1`, `IFC-FB4034716A`, `IFC-A807F5E0B3`, `IFC-34EB597147`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-017-04_vendor-engineered-equipment-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 19.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical design basis slices — motor basis (~line 324), starting basis SCA-001 VE #34 (~line 326), 13.8 kV/4.16 kV transformer / 4160 V MCC (~lines 744–760).
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific MV VFD 600 HP content; no PKG-017 match found.
- Sibling EPC deliverables: `DEL-017-01_scope-of-work`, `DEL-017-02_package-datasheet` (vendor engineering inputs); `DEL-017-05_vendor-document-turnover-package`, `DEL-017-06_epc-vendor-package-review-and-acceptance` (downstream integration).
