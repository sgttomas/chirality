# Guidance: DEL-017-04_vendor-engineered-equipment-package

## Purpose

This guidance supports the Package Vendor production unit (engineering, design, fabrication/supply, and physical equipment) for the MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD package, `PKG-017`. The deliverable converts the accepted EPC Scope of Work (`DEL-017-01`) and EPC Package Datasheet (`DEL-017-02`) into a vendor-engineered package with a defendable design basis and supplied equipment. EPC integration review is performed downstream (`DEL-017-06`).

## Principles

- **Vendor inputs are EPC outputs.** The vendor design starts from `DEL-017-01` (Scope of Work) and `DEL-017-02` (Package Datasheet). The vendor shall not invent package scope outside those inputs.
- **Responsibility split is preserved.** Package engineering, design, vendor documentation, and physical equipment belong to the Package Vendor. Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration belong to the EPC Integrator.
- **Source-anchored values only.** Where accessible source slices (DBM-Comp_and_Liquids electrical sections, Gate 7 registers, workbook row 19) define a value or constraint, the vendor design shall reflect it. Where source is silent, values remain `TBD` for vendor data and `DEL-017-02` to close — not for invention by drafting.
- **Interfaces drive design, not the reverse.** The six package interfaces (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) are inputs to vendor engineering, not items the vendor may redefine.
- **Power-quality studies remain with the EPC.** Harmonic and reactive-power mitigation are determined by detailed electrical studies (DBM 4160 V MCC paragraph). Vendor design accommodates EPC-defined study outcomes; it does not pre-empt them.

## Considerations

- **System voltage context.** The 4160 V system is fed by a 13.8 kV / 4.16 kV, 12 MVA transformer and served by a 4160 V MCC that hosts field-fused contactors, motor protection relays, and an EtherNet path to the plant PLC central control panel for data acquisition. PKG-017 sits in this 4160 V class system. The vendor design shall be electrically and communications-compatible with this MCC environment.
- **Driven motor.** The package name identifies 600 HP and 4160 V VFD output, but the DBM VFD content addresses the 4000 V / 5200 HP inlet compressor motors (KM-2150, KM-2250) under SCA-001 VE #34, not a 600 HP / 4160 V drive. The actual driven motor tag, inverter-duty rating, and motor data are vendor inputs from `DEL-017-02`, not from the DBM.
- **Capacitor-bank removal.** SCA-001 VE #37 removes capacitor banks from the synchronous bus on MCC-8200 where VFDs are present. Vendor reactive-power assumptions shall not rely on capacitor-bank compensation that the EPC has removed.
- **Standards alignment.** The DBM motor basis cites NEMA MG1 for inlet compressor motors. Applicability of NEMA MG1 motor compatibility (e.g., inverter-duty bearing/insulation) to a 600 HP / 4160 V driven motor is a vendor confirmation point tied to `DEL-017-02`.
- **Hazardous-area classification.** Installation location is `TBD`; area classification effects on enclosure ratings, conduit seals, and equipment selection cannot be finalized until EPC confirms the location.

## Trade-offs

- **VFD topology.** MV drive topologies (cascaded H-bridge, NPC, AFE, etc.) trade off harmonic performance, footprint, redundancy, and cost. With harmonic study results not yet defined for this package, the vendor should propose a topology and present its harmonic / power-quality envelope for EPC review against the electrical studies.
- **Cooling method.** Air-cooled vs. liquid-cooled MV drives trade off enclosure size, ambient sensitivity, and maintenance. Installation location and area classification are needed to lock this in.
- **Integrated drive isolation / bypass.** Integrated input isolation switches, output contactors, and bypass arrangements affect maintenance access (interface `IFC-A807F5E0B3`) and the I&C / Control Cabling termination set. Vendor proposal shall identify what is integrated and what is left for EPC integration.
- **Continuous-duty vs. start-only operation.** DBM treats MV VFDs in the 4160 V MCC context as starting devices for the large inlet compressor motors. Continuous-duty operation for a 600 HP / 4160 V driven load is a different design point and depends on `DEL-017-02` direction.

## Examples

- A vendor 4160 V MV VFD production unit, rated for a 600 HP / 4160 V driven motor, supplied with control, protection, and EtherNet communications consistent with the 4160 V MCC environment. (ASSUMPTION: representative configuration; actual configuration set by `DEL-017-02` and vendor data.)
- A vendor design basis document that, for each of the six interfaces (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports), states the vendor-side response at the package boundary and the EPC-side expectation.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-017-04-001 | Package name states "600 HP, 4160 V" 4160 V VFD, but accessible DBM VFD content addresses only 4000 V / 5200 HP inlet compressor motors (KM-2150, KM-2250); no 600 HP / 4160 V driven motor is identified in source. | Workbook Packages row 19 (package name) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, motor basis paragraph and 4160 V MCC paragraph | Datasheet attributes (driven load identification, service basis); Specification REQ-017-04-004, REQ-017-04-011; Guidance Principles, Considerations | Treat package name as identity; defer driven-motor identification and service basis to the EPC Package Datasheet (`DEL-017-02`); mark vendor-side values `TBD` until `DEL-017-02` resolves them. | TBD |
| CFL-017-04-002 | DBM treats MV VFDs in the 4160 V MCC context as starting VFDs (SCA-001 VE #34), not continuous-duty drives, while the package title implies a dedicated 4160 V VFD output. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160 V MCC paragraph (SCA-001 VE #34) | Workbook Packages row 19 (package name and intent) | Datasheet attributes (service basis); Specification REQ-017-04-004; Guidance Trade-offs | Take operating-duty basis from `DEL-017-02`; do not commit vendor design to either starting or continuous duty until `DEL-017-02` is accepted. | TBD |
| CFL-017-04-003 | Installation location for the vendor package is unassigned; DBM identifies the 4160 V MCC environment but no PKG-017-specific assignment exists, leaving area classification and structural support basis undefined. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160 V MCC paragraph | Gate 7 registers (silent on PKG-017 location) | Datasheet construction; Specification standards (area classification); Guidance Trade-offs | Defer installation location decision to EPC integration; vendor design proposes options against indoor and outdoor / classified-area possibilities until resolved. | TBD |
| CFL-017-04-004 | Source mandates that harmonic and reactive-power mitigation be set by detailed electrical studies, and that capacitor banks are removed from MCC-8200 where VFDs are present, but no PKG-017-specific harmonic envelope is given in source. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160 V MCC paragraph (SCA-001 VE #37) | Gate 7 registers (silent on power-quality acceptance criteria) | Datasheet Conditions (harmonic / reactive); Specification REQ-017-04-006; Guidance Trade-offs (VFD topology) | Vendor proposes a topology and a harmonic / power-quality envelope; EPC reviews against the detailed electrical study at `DEL-017-06`; no capacitor-bank reactive support shall be assumed. | TBD |
