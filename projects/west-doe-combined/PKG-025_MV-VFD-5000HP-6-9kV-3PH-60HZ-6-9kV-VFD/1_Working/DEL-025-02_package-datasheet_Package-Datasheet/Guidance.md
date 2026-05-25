# Guidance: DEL-025-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-025` into a source-supported technical handoff document for the "MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD" package. It should let the Package Vendor understand the EPC integration basis for an MV VFD operating at 6.9 kV class while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried verbatim as "MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD" because that is the workbook and Gate 7 register spelling.
- Treat all six workbook interface `X` facts (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned drive engineering with the Package Vendor and facility-level integration (feeders, grounding network, control/comms tie-ins, building installation, maintenance corridors) with the EPC Integrator.
- Use `TBD` for ratings, quantity allocation, drive topology, harmonic class, cooling, enclosure, isolation/phase-shift transformer, motor identity binding, and building assignment until a source-supported package-specific basis is available.
- Use DBM electrical basis at the level it supports: 6.9 kV service class, Starting-VFD use for KM-2150/2250 compressors, synchronous-transfer arrangement, PF-correction-capacitor prohibition on MCC-8200, MV cable specification, Zone 2 marking, UPS-based MV breaker/protection control, and electrical-building housing context.

## Considerations

The DBM electrical design basis applies 6.9 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded service to "facility process AC inverter-drive motors rated 5,500 hp and above." The PKG-025 workbook name carries a 5,000 hp label. This is below the DBM 5,500 hp MV threshold and so the assignment of 6.9 kV service to a 5,000 hp motor is not directly explained by the DBM voltage/service table. The datasheet should preserve both numbers and surface the mismatch for human ruling rather than silently choosing one.

The only Starting VFD usage that DBM names at 6.9 kV is the KM-2150 and KM-2250 Inlet/Sales Gas Compressor motors, fed from the 6.9 kV MCC with synchronous transfer to the MCC-8200 normal-service bus after reaching full speed. The DBM inlet/sales compressor section also describes each compressor as driven by a 6,700 hp 3-phase electric drive (with a legacy 7,000 hp conflict). Whether PKG-025 is the vendor package supplying those Starting VFDs - or a different MV VFD scope - is not confirmed by the accessible source set. The datasheet treats the KM-2150/2250 application as a candidate context (ASSUMPTION) and requires human confirmation before binding PKG-025 to specific motor tags.

Power-factor-correction capacitor banks are explicitly prohibited on the MCC-8200 synchronous-transfer bus. The datasheet should carry this prohibition forward as a Starting-VFD design constraint, applicable to any PKG-025 unit attached to that bus.

The DBM 6.9 kV MCC requires an Ethernet communication port to the plant PLC central control panel for data acquisition. The Communications / Network interface fact for PKG-025 should be specified consistently with that integration model.

The MV cable basis (three-conductor copper TECK, rated 8 kV, 100 percent insulation, shielded) and the maintenance-access constraint on cable tray and conduit routing are stable DBM facts and should govern feeder and routing requirements at the package interface, while vendor-internal cabling remains vendor scope.

Hazardous-area treatment requires VFD-fed motors in Zone 2 to be marked accordingly and to carry a temperature code lower than the area-classification drawing or fugitive-emissions study allows. Whether PKG-025's motor is located in Zone 2 is `TBD`; the requirement is preserved as conditional.

Grounding/bonding for PKG-025 is governed by the DBM grounding paragraphs: two-point ground-grid connection for major electrical equipment and a 100 A, 10 s neutral grounding resistor on each 6.9 kV transformer (tripping). Package-specific conductor sizes and connection points are not assigned and should remain `TBD`.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| 5,000 hp (workbook) vs 5,500 hp (DBM MV threshold) vs 6,700 hp (inlet/sales drive) | Carry all three values, mark as a Conflict Table entry, do not silently pick one. | The numbers come from different source slices and serve different purposes (package name, voltage-class threshold, compressor drive sizing); reconciling them is a human decision. |
| Assignment of PKG-025 to KM-2150/2250 Starting VFDs | Treat as candidate context (ASSUMPTION); do not bind motor tags in the datasheet until confirmed. | The DBM Starting-VFD basis is the only 6.9 kV VFD use named; the workbook does not bind PKG-025 to those tags. |
| Drive topology, harmonic mitigation, isolation/phase-shift transformer | Leave `TBD` pending vendor data. | DBM does not specify drive topology or harmonic class for this package. |
| Building assignment | Identify the 6.9 kV Inlet/Sales Compressor Electrical Building as candidate context only. | DBM lists it as a building and describes MV VFDs as possible electrical-building occupants, but does not assign PKG-025. |
| Standards (CEC, area classification, harmonic / power-quality) | List as governing bases with clause/location `TBD`. | DBM cites these bases; clause locations are not in the deliverable folder. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 27 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "VFD output current and harmonic class: TBD. No package-specific source slice available."
- Acceptable conditional entry: "Where supplied as a Starting VFD per DBM (KM-2150/2250 basis), synchronous transfer to MCC-8200 and the PF-correction-capacitor prohibition apply."
- Not acceptable without new source: "PKG-025 supplies the KM-2150-1 Inlet/Sales Compressor motor at 6,700 hp." The accessible source set does not establish that binding.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-025-02-001 | Workbook package name is "5000HP, 6.9kV", but the DBM voltage/service table applies 6.9 kV service to motors "rated 5,500 hp and above," and the DBM inlet/sales compressor paragraph cites a 6,700 hp drive (with a legacy 7,000 hp conflict). | Workbook Packages row 27; `PACKAGE_REGISTER.csv` row `PKG-025` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage/service table (~line 2935); inlet/sales compressor paragraph (~line 893) | Datasheet Attributes (nominal motor rating); Specification REQ-025-02-004, REQ-025-02-005 | Treat 5,000 hp as workbook nomenclature only; flag the 5,500 hp DBM threshold and the 6,700 hp drive value as separate facts; do not silently reconcile. | TBD |
| HRR-025-02-002 | DBM names Starting VFDs for KM-2150/2250 Inlet/Sales Gas Compressor motors fed from the 6.9 kV MCC with synchronous transfer to MCC-8200, but neither workbook row 27 nor the Gate 7 registers explicitly bind PKG-025 to those motor tags. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 6.9 kV MCC paragraph (~line 2955) | Workbook Packages row 27; `PACKAGE_REGISTER.csv`/`INTERFACE_REGISTER.csv` rows for PKG-025 | Datasheet Attributes (application context, drive topology); Specification REQ-025-02-006 | Treat KM-2150/2250 Starting-VFD application as candidate context (ASSUMPTION) and bind tags only on human confirmation; carry generic 6.9 kV MV VFD requirements unconditionally. | TBD |
| HRR-025-02-003 | Quantity of MV VFD units allocated to PKG-025 is not stated in any accessible source slice. | Workbook Packages row 27 (no quantity column applicable to PKG-025) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment lists and 6.9 kV MCC paragraph | Datasheet Attributes (quantity allocated to PKG-025); Specification REQ-025-02-013 | Record quantity as `TBD` and resolve via vendor inquiry or human ruling. | TBD |
