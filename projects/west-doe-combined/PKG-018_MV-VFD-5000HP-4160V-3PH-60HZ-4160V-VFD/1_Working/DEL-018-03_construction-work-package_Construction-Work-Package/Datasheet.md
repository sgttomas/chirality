# Datasheet: DEL-018-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-018-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 92 |
| Parent package | `PKG-018` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 20 |
| Package name | MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD | Workbook Packages row 20; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 18 / row 20 | Workbook Packages row 20; `PACKAGE_REGISTER.csv` |
| WBS | 02 | `PACKAGE_REGISTER.csv` row `PKG-018` |
| CoA tracking number | 26020-02-30-009 | `PACKAGE_REGISTER.csv` row `PKG-018` |
| Discipline | Electrical | Workbook Packages row 20; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-018` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package with EPC Integrator construction and integration responsibility | `PACKAGE_REGISTER.csv` row `PKG-018` |
| Package function | Medium-voltage variable-frequency drive(s) for the 4160 V, 3-phase, 60 Hz, 5000 HP class motor service. Title rating is workbook-defined. | Workbook Packages row 20; `_CONTEXT.md` |
| Likely served motor basis (ASSUMPTION) | The accessible DBM source slice identifies the 03-25 facility's 4000 V, three-phase, 60 Hz inverter-duty inlet compressor motors (KM-2150, KM-2250, approximately 5,200 hp / 3,878 kW) as the loads requiring starting VFDs per SCA-001 VE #34. ASSUMPTION: PKG-018 corresponds to those starting VFDs. Detailed allocation TBD. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, motor and 4160V MCC sections |
| Drive type / topology | TBD. No accessible source slice defines VFD topology, harmonic mitigation, cooling, enclosure class, or VFD bypass configuration. SCA-001 VE #37 notes capacitor banks are removed from the synchronous bus on MCC-8200 where VFDs are present; harmonic and reactive-power mitigation is left to detailed electrical studies. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC section |
| Installation location | TBD. DBM identifies electrical buildings as the typical housing for medium-voltage switchgear and related equipment; package-specific room/building/skid placement is not assigned. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (location TBD) |
| Field assembly basis | TBD. Modularization, shipping splits, lift plan, and rigging requirements are not stated in accessible source material for PKG-018. | Source gap |
| Construction scope alignment | The facility construction scope includes mechanical hookups, home-run cabling, terminations, pipe supports, and tie-ins; the PKG-018 construction work package aligns with this construction basis for the VFD scope. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, construction scope paragraph |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Applicable interface fact for PKG-018; must be represented in the construction interface and turnover checklist. | Workbook Packages row 20; `INTERFACE_REGISTER.csv` `IFC-81D9418AA1` |
| Grounding / Bonding | Applicable interface fact for PKG-018; construction tie-in shall coordinate with facility grounding basis. | Workbook Packages row 20; `INTERFACE_REGISTER.csv` `IFC-20754345F3` |
| I&C / Control Cabling | Applicable interface fact for PKG-018; construction shall execute home-run control cabling and terminations to the 4160V MCC / BPCS as required. | Workbook Packages row 20; `INTERFACE_REGISTER.csv` `IFC-EF82F842B4` |
| Communications / Network | Applicable interface fact for PKG-018; EtherNet/PRP connectivity to plant PLC/BPCS shall be installed per detailed design. | Workbook Packages row 20; `INTERFACE_REGISTER.csv` `IFC-DC83D04DC5`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, BPCS/RIO paragraph |
| Maintenance Access | Applicable interface fact for PKG-018; installed arrangement and cable/conduit routing shall preserve maintenance access. | Workbook Packages row 20; `INTERFACE_REGISTER.csv` `IFC-35F60961CA`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, cable tray and conduit paragraph |
| Structural / Foundations / Supports | Applicable interface fact for PKG-018; foundations, pads, anchorage, and supports shall be provided per detailed design. | Workbook Packages row 20; `INTERFACE_REGISTER.csv` `IFC-87DE46369F` |
| 4160V MCC tie-in | Construction shall coordinate VFD tie-in to the 4160V MCC, which provides field-fused contactors, motor protection relays, and EtherNet communication to the plant PLC central control panel. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC section |
| Grounding design basis | Major electrical equipment shall be directly connected to the ground grid at two points; distribution transformers, panelboards, and three-phase motors larger than 100 hp require separate copper ground conductors per CEC sizing. Package-specific application TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-018` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-018` |
| Foundations / supports installation | Structural / foundations / supports interface applies; package-specific pad and anchorage details TBD. | `INTERFACE_REGISTER.csv` `IFC-87DE46369F` |
| Cable, conduit, and tray routing | Home-run cabling, terminations, and tray/conduit installation are within facility construction scope; routing shall preserve maintenance access. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, construction scope and cable tray paragraphs |
| Module offloading and setting | DBM construction scope includes offloading and setting of modules; PKG-018 modular split and lift plan TBD. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, construction scope paragraph |
| Inspection and turnover | EPC Integrator shall produce a construction interface and turnover checklist as an artifact of this deliverable; detailed inspection scope TBD until vendor documentation and detailed design are available. | `_CONTEXT.md` anticipated artifacts; `DELIVERABLE_REGISTER.csv` row 92 |
| Pre-energization and commissioning handoff | TBD. No accessible source slice defines pre-energization checks, factory test acceptance, or commissioning hold points for PKG-018. | Source gap |
| Construction work package register alignment | The construction work package shall be aligned to the plot plan, equipment list, and construction work package register before issue for construction. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, miscellaneous facilities alignment paragraph |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-018-03_construction-work-package` (line 92).
- `PACKAGE_REGISTER.csv`, row `PKG-018` (line 20).
- `INTERFACE_REGISTER.csv`, rows for `PKG-018` (six applicable interface facts).
- `ARTIFACT_REGISTER.csv`, rows for `DEL-018-03_construction-work-package`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-018-03_construction-work-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 20.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, construction scope, inlet compressor motor, 4160V MCC, BPCS/RIO, and cable tray / conduit source slices.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical grounding and bonding source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific PKG-018 VFD construction content; no accessible package-specific match was identified during this run.
