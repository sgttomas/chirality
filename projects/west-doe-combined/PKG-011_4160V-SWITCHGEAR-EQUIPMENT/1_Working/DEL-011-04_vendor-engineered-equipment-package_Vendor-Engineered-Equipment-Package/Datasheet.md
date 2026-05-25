# Datasheet: DEL-011-04_vendor-engineered-equipment-package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-011-04_vendor-engineered-equipment-package |
| Deliverable name | Vendor Engineered Equipment Package |
| Parent package | PKG-011 - 4160V SWITCHGEAR EQUIPMENT |
| Workbook ID / row | 11 / 13 |
| WBS | 02 |
| CoA tracking number | 26020-02-30-002 |
| Discipline | Electrical |
| Deliverable type | Vendor Package Production Unit |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review |
| Scope item | SOW-0012 |

Sources: `_CONTEXT.md`; Gate 7 `PACKAGE_REGISTER.csv`; Gate 7 `DELIVERABLE_REGISTER.csv`.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Vendor-owned electrical package for 4160V switchgear equipment, with package engineering, design, vendor documentation, and physical equipment package owned by the Package Vendor. | Gate 7 `PACKAGE_REGISTER.csv`, PKG-011 |
| EPC integration responsibility | EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Gate 7 `PACKAGE_REGISTER.csv`, PKG-011 |
| Anticipated artifacts | Vendor engineered physical equipment package; vendor package design basis and datasheet set. | Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-011-04; Gate 7 `ARTIFACT_REGISTER.csv`, ART-35E12ECF7A and ART-095CD46A13 |
| Medium-voltage service | 4,160 V, 3 phase, 3 wire, 60 Hz LRG for process AC inverter-drive motors from 250 hp to 5,500 hp. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 System Voltages |
| Upstream transformer/service basis | 13.8 kV to 4.16 kV, 12 MVA transformer serving the 4160V MCC for 4000V motors. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Incoming Power and Transformers |
| MCC functional basis | 4160V MCC provides field-fused contactors, motor protection relays, and an EtherNet communication port to the plant PLC central control panel for data acquisition. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |
| Served loads identified in source | Large 4000V motors, including inlet compressors KM-2150 and KM-2250. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |
| Starter basis for KM-2150 / KM-2250 | Starting VFDs required; soft starts are not used under current basis. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |
| Harmonic/reactive-power mitigation | TBD by detailed electrical studies. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |

## Conditions

| Condition | Value | Source |
|---|---|---|
| General area classification basis | Class I Zone 2, Gas Groups IIA and IIB. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Area Classification |
| Process modules/buildings | Treated as Zone 2 hazardous areas based on fugitive-emission studies following API RP 505. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Area Classification |
| Electrical building coordination | Electrical buildings shall house MCCs, switchgear, distribution equipment, and associated HVAC/ventilation systems; area classification, HVAC, and remote distribution centres shall be coordinated with hazardous area classification and controls architecture. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Buildings, Raceways, Lighting, and Heat Tracing |
| Interface types applicable to PKG-011 | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | Gate 7 `INTERFACE_REGISTER.csv`, PKG-011 |

## Construction

| Construction / supply item | Required status |
|---|---|
| Vendor engineered physical equipment package | Required; detailed bill of material, lineup configuration, enclosure form, ratings beyond source values, and fabrication details are TBD pending vendor design. |
| Vendor package design basis and datasheet set | Required; detailed vendor datasheets are TBD pending vendor design and EPC review. |
| Cable routing, grounding, bonding, controls, and network interfaces | Must be coordinated with the listed interface types and project electrical requirements; detailed routing and terminations are TBD. |
| Factory/shop testing and inspection evidence | Expected at acceptance/turnover stage; detailed vendor test requirements are TBD because the current source material does not state them for this deliverable. |

## References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- Gate 7 `PACKAGE_REGISTER.csv`
- Gate 7 `DELIVERABLE_REGISTER.csv`
- Gate 7 `ARTIFACT_REGISTER.csv`
- Gate 7 `INTERFACE_REGISTER.csv`
- Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv`
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Basis
