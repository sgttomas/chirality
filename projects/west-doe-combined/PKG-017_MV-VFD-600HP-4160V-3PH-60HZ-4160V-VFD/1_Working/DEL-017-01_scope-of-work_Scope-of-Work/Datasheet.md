# Datasheet: DEL-017-01_scope-of-work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-017-01_scope-of-work` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable name | Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-017` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 17 / row 19 | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-008 | Workbook Packages row 19; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 19; `_CONTEXT.md` |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-017` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-017` |
| Package function | Medium-voltage variable-frequency drive (VFD) package nominally identified by the workbook as "MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD". | Workbook Packages row 19 |
| Medium-voltage service basis | 4,160 V, 3 phase, 3 wire, 60 Hz LRG service is the DBM-defined medium-voltage basis for process AC inverter-drive motors from 250 hp to 5,500 hp. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages table |
| MV MCC basis | The 4160V MCC provides field-fused contactors, motor protection relays, and an EtherNet communication port to the plant PLC central control panel for data acquisition; it serves large 4000V motors including inlet compressors KM-2150 and KM-2250. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC section |
| Starting-VFD basis (DBM) | SCA-001 VE #34 requires starting VFDs for KM-2150 and KM-2250. Soft starts are not used for these inlet compressor motors under the current basis. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC section |
| Harmonics / reactive power | SCA-001 VE #37 removes capacitor banks from the synchronous bus on MCC-8200 where VFDs are present. Harmonic and reactive-power mitigation shall be determined by detailed electrical studies. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC section |
| Driven-equipment / load identity | TBD. Workbook title cites "600HP" but the DBM-confirmed MV process drives (KM-2150 / KM-2250) are 3,878 kW / 5,200 hp at 4,000 V. No accessible source slice defines a 600 hp 4160V MV VFD load for this package; the 600 hp value is more consistent with 600V LV MCC scope per DBM. See Guidance Conflict Table HRR-017-01-001. | Workbook Packages row 19; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Inlet Compressor Drive and 600V MCC sections |
| VFD topology / sizing | TBD. VFD sizing is an electrical detailed-design item per DBM. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Inlet Compressor Drive section |
| Tagged equipment list | TBD. No package-specific tag list (e.g., VFD tag, driven motor tag) is available in the accessible source slices. | Source gap; `_Sources/26020-Package_Requirements.docx` not searched in machine-readable form |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-017 and must be represented in the package interface requirements matrix. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-5E50E5F700` |
| Grounding / Bonding | Interface fact applies to PKG-017 and must be represented in the package interface requirements matrix. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-1340C6D795` |
| I&C / Control Cabling | Interface fact applies to PKG-017 and must be represented in the package interface requirements matrix. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-6ECD9C92A1` |
| Communications / Network | Interface fact applies to PKG-017; the 4160V MCC provides an EtherNet communication port to the plant PLC central control panel for data acquisition. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-FB4034716A`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC section |
| Maintenance Access | Interface fact applies to PKG-017; cable tray and conduit routing shall not interfere with maintenance access. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-A807F5E0B3`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings/Raceways section |
| Structural / Foundations / Supports | Interface fact applies to PKG-017 and must be represented in the package interface requirements matrix. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` `IFC-34EB597147` |
| Area classification | Facility general basis is Class I Zone 2, Gas Groups IIA and IIB; package-level area classification shall be confirmed by detailed classification drawings. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Area Classification section |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-017` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-017` |
| Installation location | TBD. DBM places MV MCCs in electrical buildings but does not assign PKG-017 to a specific building, room, or skid. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings section |
| Power/control circuit separation | Power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing as required. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings/Raceways section |
| Foundations / supports | Structural / Foundations / Supports interface applies; package-specific support basis is TBD. | Workbook Packages row 19; `INTERFACE_REGISTER.csv` |
| Tagged equipment, vendor design, VFD topology, transformer/converter sections, cooling | TBD pending vendor package data and detailed design. | Source gap |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-017-01_scope-of-work`.
- `PACKAGE_REGISTER.csv`, row `PKG-017`.
- `ARTIFACT_REGISTER.csv`, rows `ART-48D5FBB23A`, `ART-53AEA33639`, `ART-52F1155060`, `ART-2C11F1D37E` for `DEL-017-01_scope-of-work`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-017` (Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-017-01_scope-of-work`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 19.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical design basis source slices: System Voltages, Incoming Power and Transformers, 4160V MCC, 600V MCC and Standby Power, Electrical Buildings/Raceways, Area Classification, Inlet Compressor Drive.
- `_Sources/26020-Package_Requirements.docx`, not machine-readable in this run; package-specific PKG-017 match not confirmed.
