# Guidance: DEL-023-04_vendor-engineered-equipment-package

## Purpose

This Guidance explains how to interpret and use the Vendor Engineered Equipment Package deliverable for `PKG-023` — `MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD`. The deliverable frames the Package Vendor's production unit: engineering, design, fabrication/supply, and the physical equipment package, together with the vendor's own design basis and datasheet set, all developed from the EPC Scope of Work (`DEL-023-01`) and EPC Package Datasheet (`DEL-023-02`).

The decomposition narrative makes this a "Vendor Package Production Unit" rather than a single document deliverable: the artifact set spans engineered hardware and the design evidence supporting it.

## Principles

- **Anchor on EPC handoff, not on title alone.** The workbook package title ("MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD") fixes voltage class, drive class, and nominal motor HP. Detailed motor service, duty, starting profile, and bus assignment must come from the accepted EPC Package Datasheet, not from this title or from generic VFD prose in the DBM.
- **Package Vendor scope is bounded.** Engineering, design, fabrication/supply, and the physical package are vendor-owned; facility integration, tie-ins, constructability, and procurement/construction coordination are EPC-owned. The vendor design basis and vendor datasheet set must respect this boundary.
- **Interfaces are the contract surface.** The six declared `PKG-023` interfaces (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) are how this vendor package connects to the facility; vendor scope is fully specified only when each interface has a documented package-side termination.
- **Source over convention.** Where the DBM speaks directly about MV-VFDs (Zone 2 marking, electrical buildings, grounding, cable type), use those statements. Where it does not (drive topology, harmonic mitigation, cooling), do not invent values; carry as `TBD` until the EPC Package Datasheet or a vendor source closes them.

## Considerations

- **DBM's MV-VFD prose is general, not PKG-023-specific.** The DBM names specific starting VFDs for the KM-2150/2250 Inlet/Sales Gas Compressors and air-cooler fan VFDs and records that VFD/soft-starter requirements for 4.16 kV motors are `TBD`. Do not allocate those statements to PKG-023 without source-supported confirmation of the driven service.
- **Cable type asymmetry.** The DBM fixes copper TECK for low-voltage VFD-fed cables but does not, in the available slice, fix the medium-voltage VFD-fed motor cable type. Vendor design basis should flag this as an open item to coordinate at detailed design.
- **Building accommodation is optional.** The DBM allows medium-voltage VFDs to be housed in prefabricated modular electrical buildings, but does not require it. Vendor and EPC Integrator must decide jointly whether PKG-023 is building-housed, skid-mounted, or otherwise sited.
- **Communications interface analog.** The DBM requires the 6.9 kV MCC to expose an Ethernet port to the plant PLC central control panel for data acquisition. By analogy, a 4.16 kV class MV-VFD package will typically need an equivalent communications interface; treat this as ASSUMPTION until the EPC Package Datasheet or vendor design fixes the requirement.

## Trade-offs

- **Drive topology vs. harmonic mitigation.** Multi-pulse (12/18/24-pulse) front ends, active front ends, and line-side filters trade harmonic performance against cost, footprint, and efficiency. The PKG-023 vendor design basis should document the chosen approach against project harmonic limits (TBD).
- **Cooling method.** Air-cooled MV-VFDs simplify mechanical interfaces; liquid-cooled MV-VFDs reduce footprint and acoustic emissions but add a mechanical interface. The choice should follow the installed environment and EPC integration plan.
- **Standalone enclosure vs. building-housed.** A standalone enclosure simplifies vendor scope and clarifies maintenance access; building-housed equipment improves environmental control but couples the vendor package to the EPC building deliverable.

## Examples

No PKG-023-specific worked examples are available from accessible source materials. Cross-package patterns (e.g., MV starting VFDs for the KM-2150/2250 inlet/sales gas compressors described in the DBM) are illustrative only; they are not authority for PKG-023.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-023-04-001 | DBM records `VFD and soft-starter requirements for 4.16 kV motors are TBD` while the PKG-023 workbook title fixes a 4160 V VFD application. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 3088 | Workbook Packages row 25 | Datasheet Attributes; Spec REQ-023-04-02, REQ-023-04-09 | Treat the workbook title as identity (4160 V class MV-VFD for nominal 1500 HP) and carry detailed 4.16 kV starting/control requirements as `TBD` until the EPC Package Datasheet is accepted. | TBD |
| HRR-023-04-002 | DBM identifies specific MV-VFD applications (KM-2150/2250 starting VFDs; air-cooler fan VFDs) but does not bind PKG-023 to any specific driven service. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 893, 2955, 2963 | `_CONTEXT.md` Scope | Datasheet Attributes (`Driven service identity`) | Do not assign a driven service to PKG-023 from DBM context; leave `TBD` until the EPC Scope of Work / Package Datasheet fixes it. | TBD |
| HRR-023-04-003 | DBM fixes copper TECK cable for low-voltage VFD-fed cable; medium-voltage VFD-fed cable type is not fixed in the accessible slice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 3013 | none in accessible slice | Datasheet Attributes; Spec REQ-023-04-07 | Carry MV VFD-fed motor cable type as `TBD`; coordinate with EPC Integrator at detailed design. | TBD |
| HRR-023-04-004 | `26020-Package_Requirements.docx` may contain PKG-023-specific vendor package requirements but was not parsed in this run. | `_REFERENCES.md` | this Datasheet/Spec | All sections | Treat as deferred; re-run with a parsed source slice when available. | TBD |
