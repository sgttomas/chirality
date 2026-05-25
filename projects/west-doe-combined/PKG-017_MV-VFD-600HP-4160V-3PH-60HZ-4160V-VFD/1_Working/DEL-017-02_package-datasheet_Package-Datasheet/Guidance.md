# Guidance: DEL-017-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-017` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the "MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD" package while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned design work with the Package Vendor and facility-level integration with the EPC Integrator.
- Use `TBD` for driven-motor identity, output rating, continuous/intermittent duty basis, control profile, harmonic mitigation selections, filters/reactors, cooling, enclosure rating, building/room assignment, and support details until a source-supported package-specific basis is available.
- Use DBM electrical basis only at the level it supports: the 4,160 V MV service bus, MV VFD presence within electrical buildings, harmonic/reactive-power treatment as a study item, grounding/bonding, cable/conduit separation, maintenance-access constraints, and ambient design.

## Considerations

The DBM electrical design basis supports a facility medium-voltage service of 4,160 V, 3-phase, 3-wire, 60 Hz LRG, identified as the bus for "process AC inverter-drive motors from 250 hp to 5,500 hp." This frames the input-voltage context for an MV VFD package within the facility but does not by itself confirm the 600 HP MV VFD application for `PKG-017`.

DBM source material documents two specific VFD instances:
- Starting VFDs for inlet compressors KM-2150 and KM-2250, which are 5,200 HP, 4,000 V class machines under SCA-001 VE #34 (not a 600 HP MV VFD).
- 600 V VFDs built into the 600 V MCC for low-voltage loads (not an MV 4,160 V VFD).

Neither documented instance matches the `PKG-017` title of a 600 HP, 4,160 V MV VFD. The accessible source set does not name a 600 HP MV VFD load. The workbook row and Gate 7 registers establish the package identity, interface profile, and responsibility split, but do not provide source-supported detailed VFD performance values for `PKG-017`. Vendor-facing datasheet content should therefore remain conservative until the missing detailed requirements are resolved.

Harmonic and reactive-power mitigation should be flagged as detailed-study items. SCA-001 VE #37 documents that capacitor banks are removed from the synchronous bus on MCC-8200 where VFDs are present; this is a facility-level reactive-power coordination signal relevant to any MV VFD integration.

Grounding and bonding are applicable interface topics. The DBM source contains facility grounding basis (two-point grounding for major electrical equipment, separate copper ground conductors per CEC sizing for distribution transformers, panelboards, and three-phase motors larger than 100 hp). The datasheet should require coordination with this basis while avoiding unsupported package-specific conductor sizing or connection details.

Cable/conduit routing for power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing. Maintenance access is both an explicit workbook interface fact and a DBM routing constraint, so electrical routing and physical placement must preserve maintenance clearances; detailed clearances remain `TBD` unless issued by detailed design or vendor data.

Communications/network integration with the plant PLC central control panel is the documented MV electrical pattern (EtherNet at the 4160V MCC). The MV VFD package should be expected to expose status, control, and protection signaling for plant-PLC integration, with specifics deferred to detailed design.

Indoor placement in prefabricated, modular electrical buildings is the documented MV-VFD housing context. The `-40 deg C` site minimum ambient governs any exposed elements.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| 600 HP MV VFD application | Treat "600HP" as package title only until source confirms the driven motor and the VFD output rating. | No accessible source slice names a 600 HP MV VFD load; documented MV VFD use is for 5,200 HP inlet compressor starting. |
| Driven-motor identity | Mark `TBD` pending package-specific source confirmation. | Workbook row identifies the package, not the motor it serves. |
| VFD duty (continuous vs. starting) | Mark `TBD`; do not adopt the SCA-001 starting-VFD pattern by default. | The starting-VFD pattern in the DBM is specific to KM-2150/KM-2250 and is not directly transferable to `PKG-017`. |
| Harmonic / reactive-power mitigation | Carry as a detailed electrical study requirement; do not specify filter/reactor configuration. | DBM defers harmonic/reactive-power mitigation to detailed electrical studies. |
| Electrical-building location | Identify indoor electrical-building placement as likely context; do not confirm specific building/room for `PKG-017`. | DBM allows MV VFDs in prefabricated modular electrical buildings but does not locate `PKG-017`. |
| Standards | List CEC, NEMA MG1 (motor basis), area classification, and project electrical specifications as governing bases with locations/clauses TBD. | DBM references these bases but detailed clauses/specification documents are not available in the deliverable folder. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 19 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Driven motor: TBD. No accessible source slice identifies the 600 HP MV motor served by this package."
- Acceptable harmonic entry: "Harmonic and reactive-power mitigation: to be determined by detailed electrical studies (DBM)."
- Not acceptable without new source: "This VFD provides starting and continuous variable-speed control for inlet compressor KM-2150." The accessible source set assigns the starting VFDs for KM-2150 to the 5,200 HP, 4,000 V class, not a 600 HP MV VFD.
- Not acceptable without new source: "Output is 600 HP at 4,160 V with [specific] filter and reactor configuration." Detailed package values are not supported by accessible sources.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-017-02-001 | The package title declares a 600 HP MV (4,160 V) VFD, but accessible DBM source slices do not name any 600 HP MV VFD load or driven motor. The only MV VFDs documented in source are starting VFDs for 5,200 HP inlet compressors at 4,000 V; the only 600 V VFDs documented are built into the 600 V MCC. | Workbook Packages row 19; `PACKAGE_REGISTER.csv` row `PKG-017` | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electric driver basis / 4160V MCC / 600V MCC paragraphs; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Treat "600HP, 4160V" as package title/identity only and keep the driven-motor identification, VFD output rating, duty basis, and detailed configuration `TBD` until vendor data or an additional source slice is accepted. | TBD |
| HRR-017-02-002 | The package title carries "4160V VFD" both at the input and output side, but no accessible source slice confirms an output voltage class for this package or its motor pairing. | Workbook Packages row 19 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical voltage/service table | Datasheet Attributes; Specification Requirements (REQ-017-02-004, REQ-017-02-005) | Carry rated input voltage as 4,160 V consistent with the documented MV bus; mark rated output voltage and motor pairing `TBD` pending motor data. | TBD |
| HRR-017-02-003 | Workbook row 19 carries six interface facts for PKG-017 (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports). DBM source slices support the MV electrical, grounding, cable routing, and maintenance-access bases, but specific package-level I&C and Communications/Network integration values (signal lists, network protocol, control architecture) are not present in the accessible source set. | `INTERFACE_REGISTER.csv` rows for `PKG-017`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` 4160V MCC EtherNet paragraph | Source gap; no PKG-017-specific I&C/communications slice | Specification verification; Procedure interface steps | Carry I&C/Communications coordination as a detailed-design requirement aligned with the plant-PLC EtherNet pattern; do not invent signal lists or protocol selections. | TBD |
