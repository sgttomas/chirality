# Guidance: DEL-016-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-016` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the Transformer TXP-8200-1 step-down distribution transformer (3 MVA, 13.8 kV / 600 V / 347 V) while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 3MVA 13.8kV/600/347V" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned design work (winding configuration, BIL, impedance, taps, enclosure, cooling) with the Package Vendor and facility-level integration with the EPC Integrator.
- Use `TBD` for insulation/cooling type, BIL, impedance, tap configuration, sound level, enclosure type, and installation location until a source-supported package-specific basis is available.
- Use the DBM electrical basis only at the level it supports: 13.8 kV / 600 V voltage and grounding regimes, transformer feeder identification, 600 V MCC service, electrical-building housing possibility, raceway separation, and area classification framing.

## Considerations

The DBM Incoming Power and Transformers section explicitly lists "13.8 kV to 600V, 3 MVA transformer" serving the "600V MCC for LV loads," which aligns directly with the PKG-016 package title (3 MVA, 13.8 kV primary, 600 V/347 V secondary). The 347 V phase-to-neutral relationship to 600 V phase-to-phase three-phase is consistent with the DBM low-voltage service designation (600 V, 3 phase, 3 wire, 60 Hz HRG with 5 A continuous resistor), but the DBM LV-service description does not itself include a neutral conductor; transformer secondary winding configuration and neutral treatment must be confirmed by vendor data and detailed electrical study before being asserted as a requirement.

The DBM is explicit that 13.8 kV incoming is LRG and that 600 V LV service is HRG with a 5 A continuous resistor. These are facility-level grounding bases; package datasheet content should require coordination with these bases while avoiding unsupported package-specific neutral/grounding-conductor sizing or transformer-internal grounding details.

The DBM does not specify dry-type vs. liquid-filled, insulation class, impedance, tap range, sound level, enclosure type, or installation location for TXP-8200-1. The accessible package-specific Word requirements source did not produce a PKG-016 match during this run; therefore, vendor-facing datasheet content should remain conservative until the missing detailed requirements are resolved.

Area classification is facility-wide Class I Zone 2 (IIA/IIB) per DBM, but the transformer's specific installation location and resulting area classification at the package boundary remain `TBD`. Outdoor pipe racks are stated as general purpose non-hazardous unless detailed classification drawings identify otherwise; assignment of TXP-8200-1 to indoor electrical building, dedicated transformer pad, or outdoor location is not stated in accessible sources.

Maintenance access, structural support, control/communication cabling, and exterior lighting interfaces are applicable per workbook row 18. The datasheet should require coordination with these interface facts at the level of identifying applicability and routing constraints, but detailed clearances, lighting lux, control-cable counts, and foundation dimensions remain `TBD` unless issued by detailed design or vendor data.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Secondary winding configuration / neutral | Mark `TBD` pending vendor confirmation. | Workbook secondary "600/347V" implies a four-wire wye, but DBM 600 V LV service is described as 3 phase / 3 wire. The conflict is resolvable only by vendor data or a project electrical study. |
| Insulation / cooling type | Mark `TBD` pending package-specific source. | DBM does not specify dry-type vs. liquid-filled for TXP-8200-1; assignment is a vendor/EPC selection decision. |
| Installation location & area classification | Identify facility area-classification framing without assigning a package-specific location/classification. | DBM defines facility-wide framing but does not place TXP-8200-1 indoors, outdoors, or in a specific electrical building. |
| Standards | List CEC, area classification standards, and project electrical specifications as governing bases with locations TBD, and ASSUMPTION-flag distribution-transformer-specific standards. | DBM references several bases but detailed clauses/specification documents are not available in the deliverable folder. |
| Quantity | Datasheet covers one transformer (TXP-8200-1) as named. | Workbook row 18 and DBM list a single 3 MVA, 13.8 kV / 600 V transformer in this service. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 18 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Transformer impedance: TBD. No package-specific source slice available."
- Acceptable rating entry: "Rated capacity 3 MVA, primary 13.8 kV, secondary 600 V / 347 V. Source: Workbook Packages row 18; DBM Incoming Power and Transformers row '13.8 kV to 600V, 3 MVA transformer'."
- Not acceptable without new source: "Transformer is ONAN-cooled, 5.75% impedance, ±2 x 2.5% off-load taps." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-016-02-001 | Workbook secondary designation "600/347V" implies a 4-wire wye secondary with neutral, but DBM System Voltages defines the 600 V LV service as 3 phase / 3 wire HRG with 5 A continuous resistor. | Workbook Packages row 18; `PACKAGE_REGISTER.csv` row `PKG-016` | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages | Datasheet Attributes (secondary voltage, grounding); Specification REQ-016-02-004/005 | Carry "600 V / 347 V" as the workbook-stated nameplate target and mark transformer secondary winding configuration and neutral treatment `TBD` pending vendor data and a project electrical study; do not assert four-wire wye or three-wire delta until confirmed. | TBD |
| HRR-016-02-002 | Insulation/cooling type, BIL, impedance, tap configuration, sound level, enclosure type, and installation location for TXP-8200-1 are not stated in accessible source slices. | Workbook Packages row 18; Gate 7 `PACKAGE_REGISTER.csv` row `PKG-016` | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Incoming Power and Transformers; Electrical Buildings/Raceways | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Carry these parameters as `TBD` until vendor data or a project transformer specification is accepted; do not invent values for vendor handoff. | TBD |
