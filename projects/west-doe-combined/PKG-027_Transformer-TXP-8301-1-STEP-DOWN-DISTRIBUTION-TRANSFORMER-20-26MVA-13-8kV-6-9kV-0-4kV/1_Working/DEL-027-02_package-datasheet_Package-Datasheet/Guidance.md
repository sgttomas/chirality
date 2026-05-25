# Guidance: DEL-027-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-027` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the Transformer TXP-8301-1 (20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV step-down distribution transformer) while keeping EPC-owned facility interfaces distinct from vendor-owned transformer design and supply.

## Principles

- Preserve source spelling and identity. The package name is carried verbatim as it appears in the workbook and Gate 7 registers, including the tag "TXP-8301-1" and the voltage list "13.8kV/6.9kV/0.4kV."
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned transformer design (impedance, BIL, vector group, taps, accessories, type/routine tests) with the Package Vendor; keep facility-level integration (yard placement, foundation interface, ground grid tie-ins, MV cable routing, secondary containment decisions) with the EPC Integrator.
- Use `TBD` for transformer parameters that the accessible source set does not establish, even when industry convention would suggest typical values.
- Use DBM electrical basis only at the level it supports: voltage and service basis, 6.9 kV-side grounding resistor, ground grid and bonding, MV cable specifications, cable tray and conduit routing, transformer installation/foundations/containment, and the existence of the 6.9 kV Inlet/Sales Compressor Electrical Building as the downstream load center.

## Considerations

The DBM electrical service basis defines 13.8 kV and 6.9 kV facility services as 3-phase, 3-wire, 60 Hz, low-resistance grounded. The 6.9 kV service is specifically for facility process AC inverter-drive motors rated 5,500 hp and above, and DBM identifies the 6.9 kV MCC (MCC-8200 synchronous-transfer bus) serving the KM-2150/2250 Inlet/Sales Gas Compressor motors. TXP-8301-1's 13.8 kV/6.9 kV step-down is therefore consistent with feeding this 6.9 kV load center via the 6.9 kV Inlet/Sales Compressor Electrical Building. This direction is strongly supported but the specific feeder assignment from TXP-8301-1 to a named bus or building is not enumerated in the source slices.

The 0.4 kV value in the package name is unusual relative to the DBM electrical service table, which lists facility services at 13.8 kV, 6.9 kV, 600 V (3-phase) and 208/120 V. No DBM service line establishes a 0.4 kV distribution service for the plant. Possible interpretations include an auxiliary/tertiary winding for cooling/auxiliaries, a transformer auxiliary supply, or a metric-labeled 400 V service tied to vendor-package equipment. Because none of these is source-supported, the 0.4 kV value is carried as identity-level metadata, with service basis and connected load `TBD`.

The DBM equipment list identifies "Oil-Filled Transformers" with quantity 2 at the facility level. PKG-026 (TXP-8300-2) and PKG-027 (TXP-8301-1) are both 20/26 MVA 13.8kV/6.9kV/0.4kV transformers per the package register; allocating both DBM oil-filled transformers to these two package rows is plausible but not confirmed in the source slices accessible to this deliverable. The datasheet treats insulating medium as `TBD` to avoid asserting an unsupported vendor-design choice.

Grounding and bonding are applicable interface topics. The DBM source explicitly requires that each 6.9 kV transformer neutral be grounded through a 100 A, 10 s neutral grounding resistor operating as a tripping system. This is source-supported and is carried into the datasheet as a binding requirement on the 6.9 kV secondary. The facility ground-grid two-point connection, the ground well at the power transformer, and the separate copper ground conductor for distribution transformers are also source-supported and carried as installation conditions.

Maintenance access is both an explicit workbook interface fact and a DBM routing constraint for cable tray and conduit. The datasheet requires electrical routing and physical placement to preserve maintenance access, but detailed clearances remain `TBD` unless issued by detailed design or vendor data.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| 20/26 MVA dual rating | Carry both values; mark cooling-stage interpretation (ONAN/ONAF or equivalent) as ASSUMPTION until vendor confirms. | The dual-rating designation is universal in the workbook spelling; the standard cooling-stage interpretation is industry convention, not source-supported. |
| Insulating medium | Mark `TBD` (do not assert "oil-filled" for TXP-8301-1). | DBM equipment list identifies oil-filled transformers facility-wide but does not name TXP-8301-1; allocation against the count-of-2 is unconfirmed. |
| 0.4 kV interpretation | Treat 0.4 kV as identity-level only; service basis and connected load `TBD`. | DBM electrical service table does not enumerate a 0.4 kV service for the plant; choosing an interpretation without vendor or source confirmation would invent design. |
| Downstream feeder | Direction is strongly supported (feeds 6.9 kV Inlet/Sales Compressor Electrical Building) but specific feeder assignment is `TBD`. | DBM names the 6.9 kV building and 6.9 kV MCC service, but does not explicitly tag TXP-8301-1 to a named downstream bus. |
| Standards | List CEC, area classification, project electrical specifications as governing bases; list IEEE C57 / IEC 60076 as ASSUMPTION until vendor or specification confirms. | DBM references CEC and project specifications; transformer-specific standards are industry convention rather than source-cited. |

## Examples

- Acceptable datasheet entry: "Secondary voltage 6.9 kV, 3 phase, 3 wire, 60 Hz, LRG. Source: DBM electrical service table."
- Acceptable datasheet entry: "Secondary neutral grounding: 100 A, 10 s NGR, tripping. Source: DBM grounding-resistor paragraph."
- Acceptable source-gap entry: "Insulating medium: TBD pending vendor selection."
- Not acceptable without new source: "Transformer impedance 8.0 percent at 20 MVA base, vector group YNd1, BIL 110 kV LV / 95 kV neutral." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-027-02-001 | The package name lists 0.4 kV alongside 13.8 kV and 6.9 kV, but the DBM electrical service table does not enumerate a 0.4 kV distribution service for the plant; the technical meaning (tertiary winding vs auxiliary tap vs vendor-internal supply) is undefined in accessible sources. | Workbook Packages row 29; `PACKAGE_REGISTER.csv` row `PKG-027` (package name) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table | Datasheet Attributes; Specification Requirement REQ-027-02-011 | Carry 0.4 kV as identity-level metadata; mark service basis and connected load `TBD`; do not assert a tertiary-winding or auxiliary interpretation until confirmed by vendor data or project electrical specification. | TBD |
| HRR-027-02-002 | The DBM equipment list identifies "Oil-Filled Transformers" quantity 2, but does not allocate them to PKG-026 (TXP-8300-2) and PKG-027 (TXP-8301-1); insulating medium for TXP-8301-1 is therefore not source-confirmed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, equipment list | Workbook Packages row 29; `PACKAGE_REGISTER.csv` row `PKG-027` | Datasheet Attributes (Insulating medium); Specification gap list (REQ-027-02-010) | Mark insulating medium `TBD` for PKG-027 until allocation is confirmed; do not assert "oil-filled" without explicit allocation. | TBD |
| HRR-027-02-003 | The 20/26 MVA dual rating's cooling-stage interpretation (typically ONAN/ONAF) is industry convention but not stated in accessible source slices. | Workbook Packages row 29 (package name "20/26MVA") | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformer installation paragraph (no cooling-stage statement) | Datasheet Attributes (Rated capacity); Specification Requirements | Carry both 20 and 26 MVA values; mark cooling-stage interpretation as ASSUMPTION pending vendor data. | TBD |
| HRR-027-02-004 | No deliverable-specific source slices from `26020-Package_Requirements.docx` were copied during PREPARATION; transformer-specific impedance, BIL, vector group, taps, sound level, temperature rise, and accessories cannot be derived. | `_REFERENCES.md`, Missing / Deferred References | Workbook Packages row 29 | Datasheet Attributes; Specification Requirements | Resolve `26020-Package_Requirements.docx` slices into the deliverable folder before the datasheet is treated as vendor-ready; in the interim carry these parameters as `TBD`. | TBD |
