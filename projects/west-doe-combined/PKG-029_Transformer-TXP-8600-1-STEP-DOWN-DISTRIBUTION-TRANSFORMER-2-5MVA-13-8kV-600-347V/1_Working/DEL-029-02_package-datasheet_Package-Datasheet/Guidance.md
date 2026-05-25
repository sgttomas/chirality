# Guidance: DEL-029-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-029` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the TXP-8600-1 step-down distribution transformer (2.5 MVA, 13.8 kV primary, 600/347 V secondary per package title) while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package and equipment tags are carried as "Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V" and "TXP-8600-1" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned design work (winding design, impedance, taps, losses, accessories, protection, testing) with the Package Vendor and facility-level integration with the EPC Integrator.
- Use `TBD` for insulation/cooling type, secondary winding configuration and grounding, foundation/containment specifics, location, source feeder, and load list until a source-supported package-specific basis is available.
- Use the DBM electrical basis only at the level it supports: 13.8 kV backbone, generic 600 V service basis, transformer spacing/base/containment principles, grounding basis, cable tray, conduit, and maintenance-access constraints.

## Considerations

The DBM electrical design basis supports the medium-voltage primary as 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded, fed radially from the 13.8 kV switchgear to facility electrical buildings. TXP-8600-1's WBS 01 / CoA 26020-01-30-020 placement and the DBM source pointer for PKG-029 in `PACKAGE_REGISTER.csv` (DBM-Deepcut) indicate the Deepcut 04-25 facility scope.

The DBM Transformers paragraph identifies oil-filled transformer spacing per CEC, structural steel transformer bases, and secondary-containment review. The foundations table also lists "Generally supported on precast concrete bearing foundations" for transformers. Whether TXP-8600-1 is oil-filled or dry-type, indoor or outdoor, is not stated by accessible source.

The package title carries the secondary voltage as "600/347V," which mathematically corresponds to a 600Y/347V wye secondary (600/√3 ≈ 346.4). DBM Section "System Voltages" lists low-voltage services as "600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with 5 A continuous resistor," which is a 3-wire HRG configuration that does not include a 347 V phase-to-neutral service. This discrepancy must be reconciled by detailed engineering and is captured below as `HRR-029-02-001`.

Grounding and bonding are an applicable interface topic and are supported by the DBM grounding paragraphs, including two-point ground-grid connection for major electrical equipment, ground wells at power transformers for maintenance/testing, and a separate copper ground conductor for distribution transformers sized per CEC. The datasheet should require coordination with this basis while avoiding unsupported package-specific conductor sizing or connection details.

Maintenance access is both an explicit workbook interface fact and a DBM routing constraint for cable tray and conduit. The datasheet should require electrical routing and physical placement to preserve maintenance access, but detailed clearances remain `TBD` unless issued by detailed design or vendor data.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Nameplate rating (2.5 MVA) | Carry from package title as `ASSUMPTION`; do not derive vendor design values (impedance, taps, losses, sound) from this rating alone. | The 2.5 MVA value is asserted by the workbook/registers but not corroborated by DBM source text in this run. |
| Secondary winding (wye vs delta) | Mark `TBD` until reconciled; flag the 600/347V vs DBM 600 V 3-wire HRG discrepancy. | The package title implies a wye secondary; the DBM low-voltage basis is 3-wire HRG. The two are not directly compatible without further design definition. |
| Insulation/cooling (oil vs dry) | Mark `TBD`. | DBM speaks to oil-filled spacing principles generally; TXP-8600-1 is not specifically classed as oil-filled or dry-type by source. |
| Containment / foundation | Mark `TBD` pending oil-filled determination; cite DBM principles only. | Containment review is conditional on oil-filled selection. |
| Installation location | Identify as possible electrical-building or outdoor pad context, not a confirmed location. | DBM identifies the electrical-building set but does not locate PKG-029. |
| Source feeder / connected loads | Mark `TBD`. | DBM identifies radial distribution from 13.8 kV switchgear but does not name the upstream feeder or downstream loads for TXP-8600-1. |
| Standards | List CEC, project electrical specifications, and area classification as governing bases with locations TBD; treat IEEE C57 / CSA C88 as ASSUMPTION pending source confirmation. | DBM references CEC and project specs broadly; transformer-specific construction/testing standards are not named in the accessible source slices. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 31 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Insulation / cooling: TBD. DBM addresses transformers generally; TXP-8600-1 oil-filled vs dry-type classification is not stated by accessible source."
- Not acceptable without new source: "TXP-8600-1 is an oil-filled ONAN transformer with 5.75 percent impedance and ±2×2.5 percent off-load taps." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-029-02-001 | Package title carries the secondary voltage as "600/347V" (implying 600Y/347V wye secondary), but the DBM low-voltage service basis is "600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with 5 A continuous resistor" (3-wire HRG, no 347 V phase-to-neutral). | `PACKAGE_REGISTER.csv` row `PKG-029` package name (Workbook Packages row 31) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table; grounding paragraph | Datasheet Attributes (secondary voltage, secondary grounding); Specification REQ-029-02-005; Procedure verification | Carry "600/347V" from the package title as identity; mark secondary winding configuration and secondary grounding as `TBD` pending detailed-engineering reconciliation; do not assert either 4-wire wye or 3-wire HRG as the package basis from this run. | TBD |
| HRR-029-02-002 | Package title asserts a 2.5 MVA nameplate rating for TXP-8600-1, but no corroborating DBM source slice for this rating was located in accessible material; package-specific requirements (`26020-Package_Requirements.docx` row for PKG-029) were not located either. | `PACKAGE_REGISTER.csv` row `PKG-029` package name; Workbook Packages row 31 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (no TXP-8600-1 rating clause located); `_Sources/26020-Package_Requirements.docx` (no PKG-029 match located) | Datasheet Attributes (nameplate rating); Specification REQ-029-02-009 | Carry 2.5 MVA from the package title as `ASSUMPTION`; do not derive design-basis values from it; resolve via vendor data or package-specific requirements source. | TBD |
| HRR-029-02-003 | DBM Transformers paragraph addresses oil-filled transformer spacing/base/containment principles, but TXP-8600-1 is not explicitly classified as oil-filled or dry-type by accessible source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph and foundations table | Workbook Packages row 31; `PACKAGE_REGISTER.csv` row `PKG-029` | Datasheet Attributes (insulation/cooling); Datasheet Construction (foundation, containment); Specification REQ-029-02-006 | Treat insulation/cooling type, foundation type, and secondary containment requirement as `TBD` until vendor data or detailed engineering classifies the unit. | TBD |
