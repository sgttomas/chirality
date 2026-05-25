# Guidance: DEL-015-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-015` into a source-supported technical handoff document for the TXP-8300-1 step-down distribution transformer. It should let the Package Vendor understand the EPC integration basis (incoming 13.8 kV feed from 04-25, secondary feed to the 4160V MCC for 4000V motors) while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "Transformer TXP-8300-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 12/15MVA 13.8kV/4160/2400V" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned design work (cooling class, BIL, impedance, tap range, bushings, radiator/conservator, OLTC, audible noise, dimensions, type tests) with the Package Vendor.
- Use the DBM electrical basis only at the level it supports: System Voltages table (13.8 kV LRG, 4.16 kV LRG, 60 Hz), Incoming Power and Transformers table (13.8 kV to 4.16 kV, 12 MVA transformer feeds the 4160V MCC), and adjacent raceway/grounding/area/foundation guidance.
- Mark unsupported package-title values (15 MVA FA, 2400 V tertiary) as `ASSUMPTION` rather than rewording them as confirmed facts.

## Considerations

The DBM SEC-12 Electrical Basis confirms the primary service basis of 13.8 kV, 3 phase, 3 wire, 60 Hz LRG (incoming from 04-25) and the medium-voltage service basis of 4,160 V, 3 phase, 3 wire, 60 Hz LRG. The Incoming Power and Transformers table specifically identifies a "13.8 kV to 4.16 kV, 12 MVA transformer" feeding the 4160V MCC for 4000V motors. That row aligns with the workbook identity of TXP-8300-1 and is the strongest source-supported anchor for the datasheet's voltage and rating fields.

The DBM does not identify a 2400 V secondary or a 15 MVA forced-air rating in any accessible source slice. Because the package title carries both, treat them as `ASSUMPTION` derived from package identity rather than as confirmed nameplate values. Vendor data, the package-specific Word requirements source (if a confirmed PKG-015 match is later found), or accepted electrical studies are needed to convert these to firm values.

The 4160V MCC source slice provides downstream context: large 4000V motors (including inlet compressors KM-2150 and KM-2250) are served from the MCC; SCA-001 VE #34 requires starting VFDs for KM-2150 and KM-2250; SCA-001 VE #37 removes capacitor banks from the synchronous bus on MCC-8200 where VFDs are present. Harmonic and reactive-power mitigation is to be determined by detailed electrical studies and may influence transformer harmonic/K-factor or thermal duty selection. Carry harmonic-duty and K-factor as `TBD` pending those studies.

Grounding and bonding are applicable interface topics. The DBM source identifies project-wide grounding philosophy at the system level (LRG on 13.8 kV and 4.16 kV) but does not supply transformer-specific neutral grounding, NGR rating, or grounding-conductor sizing values. The datasheet should require coordination with the project grounding basis while leaving neutral grounding resistor (NGR) and grounding-conductor sizing as `TBD` until detailed design.

Maintenance access, area/exterior lighting, I&C/control cabling, communications/network, and structural/foundations/supports are explicit workbook interface facts. The datasheet should require electrical routing, lighting coverage at the transformer pad, control cabling for monitoring and protection, communications integration (Modbus monitoring only via Kepware), maintenance clearances, and foundation/support coordination with the geotechnical and structural disciplines, but detailed dimensions, lux levels, and clearances remain `TBD` unless issued by detailed design or vendor data.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Nameplate rating | Cite 12 MVA from the DBM; mark 15 MVA FA as `ASSUMPTION`. | DBM table confirms 12 MVA; the FA rating in the package title is not source-corroborated. |
| Secondary voltage(s) | Cite 4.16 kV from the DBM; mark 2400 V tertiary as `ASSUMPTION`. | DBM identifies only the 4.16 kV secondary; 2400 V appears only in the package title. |
| Cooling class / insulation / BIL | Mark `TBD` pending vendor data. | No accessible source slice specifies ONAN/ONAF, insulation level, or BIL. |
| Vector group / impedance / tap range | Mark `TBD` pending vendor data. | Not stated in accessible sources. |
| Standards (CSA C88, IEEE C57 series) | List as `ASSUMPTION: likely applicable`. | Standard names not present in accessible source slice; cannot cite clauses. |
| Installation location | Identify "4.16 kV inlet/overheads compressor electrical building" as adjacent context, not a confirmed location for TXP-8300-1. | DBM Buildings section references the 4.16 kV electrical building generally, not as TXP-8300-1's assigned location. |
| Neutral grounding (NGR) | Mark sizing and configuration `TBD`. | DBM defines LRG philosophy but not NGR rating for this transformer. |

## Examples

- Acceptable datasheet entry: "Primary: 13.8 kV, 3 phase, 3 wire, 60 Hz LRG. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 System Voltages table."
- Acceptable assumption entry: "Forced-air (FA) rating 15 MVA — ASSUMPTION derived from package title; not confirmed by DBM source slice. Source: Workbook Packages row 17 (title)."
- Acceptable source-gap entry: "BIL: TBD. No accessible source slice specifies basic impulse level."
- Not acceptable without new source: "Impedance is 7.5% at 12 MVA OA base." The accessible source set does not establish this value.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-015-02-001 | Package title carries "12/15 MVA" but the DBM Incoming Power and Transformers table identifies only a "12 MVA" transformer. The 15 MVA forced-air rating is not source-confirmed. | Workbook Packages row 17 (package title) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Incoming Power and Transformers table | Datasheet Attributes (Rating); Specification REQ-015-02-005 | Cite 12 MVA as source-confirmed and carry 15 MVA FA as `ASSUMPTION` until vendor data or detailed electrical source confirms the FA rating. | TBD |
| HRR-015-02-002 | Package title carries "13.8kV/4160/2400V" implying a 2400 V tertiary winding, but the DBM source slice identifies only 4.16 kV as the secondary. | Workbook Packages row 17 (package title) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages and Incoming Power and Transformers tables | Datasheet Attributes (Secondary voltage); Specification REQ-015-02-004, REQ-015-02-005 | Cite 4.16 kV as source-confirmed and carry 2400 V tertiary as `ASSUMPTION` until vendor data or additional source slice confirms a tertiary winding. | TBD |
| HRR-015-02-003 | No package-specific match for `PKG-015` / TXP-8300-1 was confirmed in `26020-Package_Requirements.docx` during this run; detailed transformer requirements (cooling class, BIL, vector group, impedance, taps, NGR) cannot be source-anchored. | `_Sources/26020-Package_Requirements.docx` (no confirmed PKG-015 match identified) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (system-level basis only) | Datasheet Attributes/Construction; Specification REQ-015-02-009 | Mark detailed transformer parameters as `TBD` until a confirmed package-specific source slice or vendor data is provided. | TBD |
