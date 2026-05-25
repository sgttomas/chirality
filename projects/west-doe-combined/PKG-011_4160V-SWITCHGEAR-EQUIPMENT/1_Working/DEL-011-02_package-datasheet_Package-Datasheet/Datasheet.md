# Datasheet: DEL-011-02_package-datasheet - Package Datasheet

## Identification

| Field | Value |
|---|---|
| Deliverable ID | `DEL-011-02_package-datasheet` |
| Deliverable name | Package Datasheet |
| Parent package | `PKG-011` - 4160V SWITCHGEAR EQUIPMENT |
| Workbook ID / row | 11 / row 13 |
| CoA tracking number | `26020-02-30-002` |
| Discipline | Electrical |
| Deliverable type | EPC Package Datasheet |
| Responsible party | EPC Integrator |
| Source scope item | `SOW-0012` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package role | Vendor-owned electrical equipment package with EPC Integrator facility-level integration responsibility. | `PACKAGE_REGISTER.csv`, `PKG-011` |
| Package scope | 4160V switchgear equipment for the 03-25 electrical system. | `PACKAGE_REGISTER.csv`, `PKG-011`; `3-25_Comp_and_Liquids_DBM.md`, SEC-12 |
| Electrical system relationship | The 03-25 electrical system is a shared cross-facility utility supplied from 04-25. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Design Basis |
| Incoming supply basis | 03-25 main power is sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 Incoming Power and Transformers |
| Switchgear/MCC service basis | 13.8 kV to 4.16 kV, 12 MVA transformer serving the 4160V MCC for 4000V motors. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 Incoming Power and Transformers |
| Medium-voltage service | 4,160 V, 3 phase, 3 wire, 60 Hz, low-resistance grounded; process AC inverter-drive motors from 250 hp to 5,500 hp. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 System Voltages |
| Served loads stated in source | Large 4000V motors including inlet compressors `KM-2150` and `KM-2250`. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |
| Control/data interface | Field-fused contactors, motor protection relays, and EtherNet communication port to the plant PLC central control panel for data acquisition. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |
| Starting basis for KM-2150/KM-2250 | Starting VFDs required; soft starts are not used under the current basis. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |
| Capacitor bank basis | Capacitor banks removed from synchronous bus on `MCC-8200` where VFDs are present. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |
| Harmonic/reactive-power mitigation | TBD by detailed electrical studies. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC |
| Package-specific lineup, breaker, bus, enclosure, interrupting, and metering ratings | TBD; not stated in accessible source slices. | Current source gap |

## Conditions

| Condition | Datasheet basis | Source |
|---|---|---|
| Area classification | General basis: Class I Zone 2, Gas Groups IIA and IIB; outdoor pipe racks general purpose unless detailed drawings identify otherwise. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 Area Classification |
| Electrical building context | Electrical buildings house MCCs, switchgear, distribution equipment, and HVAC/ventilation systems; area classification and HVAC coordinated with hazardous area classification and controls architecture. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Buildings, Raceways, Lighting, and Heat Tracing |
| Winterization/environment | -40 deg C minimum ambient governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe condition applies. | `3-25_Comp_and_Liquids_DBM.md`, SEC-09 Source and Governance Note |
| Circuit segregation | 13.8 kV, 4,160 V, and 600 V power circuits separated from control and instrument circuits by distance, shielding, or routing as required to minimize interference. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Buildings, Raceways, Lighting, and Heat Tracing |
| Grounding and bonding | Cable tray, conduit, grounding, and bonding shall comply with project electrical specifications and detailed design. | `3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Buildings, Raceways, Lighting, and Heat Tracing |
| Required studies before final equipment ratings | Load analysis, short-circuit study, relay coordination/arc-flash energy study, and load-flow study. | `4-25_Deepcut_DBM.md`, SEC-12 Governing Codes, Standards, Specifications, and Studies |

## Construction

| Construction / handoff element | Required datasheet content |
|---|---|
| Interface matrix | Include Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: `INTERFACE_REGISTER.csv`, `PKG-011`. |
| Vendor handoff | Provide technical basis, battery limits, design expectations, and source-supported requirements to the package delivery entity. Source: `ARTIFACT_REGISTER.csv`, `ART-BAB8DCD798`. |
| EPC integration | EPC Integrator owns facility-level interfaces, tie-ins, constructability, procurement/construction coordination, and integration. Source: `PACKAGE_REGISTER.csv`, `PKG-011`. |
| Vendor production scope | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. Source: `PACKAGE_REGISTER.csv`, `PKG-011`. |
| Vendor document requirements | Detailed vendor-document requirements are TBD for this package in the current artifact register. Source: `ARTIFACT_REGISTER.csv`, `ART-A2FEBFE6DC`. |

## References

- `_CONTEXT.md`, DEL-011-02 identity and scope.
- `DELIVERABLE_REGISTER.csv`, row `DEL-011-02_package-datasheet`.
- `PACKAGE_REGISTER.csv`, row `PKG-011`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-011-02_package-datasheet`.
- `INTERFACE_REGISTER.csv`, rows `IFC-59155DCD8A`, `IFC-11D041BE86`, `IFC-1E76A05C34`, `IFC-73DFF7BAE7`, `IFC-C035563A79`, `IFC-680C970D3C`.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-09 and SEC-12.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12.
