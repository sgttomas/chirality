# Guidance: DEL-031-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-031` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the Transformer TXP-8500-1 (3 MVA, 13.8 kV / 600 V / 347 V step-down distribution transformer) while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "Transformer TXP-8500-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 3MVA 13.8kV/600/347V" because that is the workbook and Gate 7 register spelling. The tag TXP-8500-1 and ratings (3 MVA; 13.8 kV primary; 600 V / 347 V secondary) are carried as identity facts.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned design work with the Package Vendor and facility-level integration with the EPC Integrator.
- Use `TBD` for construction class, impedance, vector group, tap range, BIL, cooling class, losses, noise rating, containment outcome, installation location, and protective relaying until a source-supported package-specific basis is available.
- Use DBM electrical basis only at the level it supports: 13.8 kV upstream distribution, 600 V downstream service, transformer foundation and spacing convention, grounding/bonding, cable specification, and maintenance-access constraints.

## Considerations

The DBM electrical design basis supports a system context in which the 13.8 kV switchgear distributes radially through step-down transformers to 600 V (and other) electrical buildings; the 600 V level is high-resistance grounded with a 5 A continuous resistor. TXP-8500-1's primary/secondary voltages match this facility basis. The 347 V value is the standard line-to-neutral of a 600 V three-phase system, and the package name preserves it.

The DBM addresses transformers at the facility level: large oil-filled transformers shall be spaced per CEC and generally installed on structural steel transformer bases over precast concrete bearing foundations; secondary containment shall be reviewed and selection should limit containment where practical. The accessible source set does not state whether TXP-8500-1 is to be oil-filled or dry-type, so construction class is `TBD`.

The DBM equipment list identifies "Oil-Filled Transformers" quantity 2 at the facility level (ELC-QAS-000011-001), but the accessible source set does not allocate one of those units to PKG-031 vs. other transformer tags; package-quantity allocation is `TBD`.

Cable specifications are well-defined at the facility level: 13.8 kV primary feeders use three-conductor copper TECK, 15 kV with 133 percent insulation, shielded; 600 V transformer secondary to MCC uses ACWU and avoids single-conductor cables. These are carried as datasheet requirements.

Grounding is an applicable interface and is well-defined at the facility level: two-point ground-grid connection for major electrical equipment, separate copper ground conductors for distribution transformers per CEC, and ground wells at power transformers for maintenance. The datasheet should require coordination with this basis while leaving package-specific conductor sizes to detailed design.

Maintenance Access is both an explicit workbook interface fact and a DBM routing constraint for cable tray and conduit. Area / Exterior Lighting, I&C / Control Cabling, and Communications / Network are interface facts from the workbook row; the accessible source set supports them as applicable interfaces but does not provide TXP-8500-1-specific cabling counts, control schemes, or network endpoints — those remain vendor-detailed-design items.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Construction class (oil-filled vs. dry-type) | Mark `TBD` pending vendor/detailed-design selection. | DBM addresses oil-filled at the facility level and recommends limiting containment requirements, but does not specify the class for TXP-8500-1. |
| Quantity allocation | One transformer = TXP-8500-1; do not allocate further facility quantities to this package without confirmation. | DBM lists facility-wide transformer quantity but does not bind specific tags to PKG-031. |
| Installation location | Identify 600 V buildings 840-1 / 850-1 / 860-1 as candidate served buildings, not as confirmed installation locations. | DBM lists 600 V electrical buildings but does not assign TXP-8500-1 to a building or outdoor pad. |
| Impedance, vector group, tap range, BIL, cooling, losses, noise | Mark `TBD` and defer to vendor data and detailed transformer specification. | Accessible source set does not contain TXP-8500-1-specific values. |
| Standards | List CEC, project electrical specifications, area classification standards, and (ASSUMPTION) CSA/IEEE transformer standards with locations TBD. | DBM references the facility-level bases; transformer-specific industry standards are conventional but not explicitly cited in the accessible source set. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 33 and `INTERFACE_REGISTER.csv`."
- Acceptable datasheet entry: "Primary feeder: three-conductor copper TECK, 15 kV, 133% insulation, shielded. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable, Wire, and Raceways table."
- Acceptable source-gap entry: "Transformer impedance: TBD. No package-specific source slice available; vendor data required."
- Not acceptable without new source: "TXP-8500-1 is a 3 MVA ONAN-cooled oil-filled transformer with 5.75% impedance and Dyn11 vector group." Construction, impedance, and vector group are not established by the accessible source set.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-031-02-001 | Transformer construction class (oil-filled vs. dry-type) for TXP-8500-1 is not stated in the accessible source set. DBM addresses oil-filled transformers at the facility level but also recommends limiting containment where practical, which could favor dry-type for some applications. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph (oil-filled basis) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph (containment-limitation guidance) | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Mark construction class `TBD` and defer to vendor selection and detailed engineering containment review for TXP-8500-1; do not assume oil-filled or dry-type. | TBD |
| HRR-031-02-002 | DBM equipment list identifies "Oil-Filled Transformers" quantity 2 facility-wide, but allocation of either unit to PKG-031 / TXP-8500-1 is not confirmed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment list ELC-QAS-000011-001 | Workbook Packages row 33; Gate 7 `PACKAGE_REGISTER.csv` row `PKG-031` | Datasheet Attributes (quantity); Specification Requirements | Treat PKG-031 as one transformer (TXP-8500-1); do not assign facility-wide transformer counts to this package without source confirmation. | TBD |
| HRR-031-02-003 | Installation location of TXP-8500-1 is not stated in the accessible source set. 600 V electrical buildings 840-1, 850-1, and 860-1 are candidate served buildings, but assignment of TXP-8500-1 to a building, outdoor pad, or skid is not confirmed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list | Workbook Packages row 33 (no location field) | Datasheet Construction (installation location); Procedure prerequisites | Carry installation location as `TBD` and defer to layout / single-line diagram development in detailed engineering. | TBD |
