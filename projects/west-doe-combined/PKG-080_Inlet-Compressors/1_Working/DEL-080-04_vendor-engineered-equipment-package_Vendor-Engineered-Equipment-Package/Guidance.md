# Guidance: DEL-080-04 — PKG-080 Inlet Compressors Vendor Engineered Equipment Package

> Source-grounding note: Rationale draws from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05 and `_Sources/26020-Package_Requirements.docx` package heading 33. Where rationale is inferred and not directly stated, items are labeled `ASSUMPTION`.

## Purpose

This deliverable is the Package Vendor production unit for engineering, design, fabrication/supply, and the physical equipment package developed from the EPC Scope of Work (DEL-080-01) and the EPC Package Datasheet (DEL-080-02). It exists so that a single vendor accountable for the inlet compressor packages can deliver engineered, modularized equipment ready for EPC integration into the West Doe Compressor Station and Liquids Hub facility.
Source: `_CONTEXT.md`; heading 33 "Basic Scope"; DBM SEC-05.

## Principles

1. **Single vendor accountability for a packaged scope.** The inlet compressors are procured as a packaged unit (compressor + auxiliaries + controls + building) rather than as discrete components, so that mechanical integration risk and FAT-level performance accountability stay with the vendor.
   Source: heading 33 "Major Included Equipment" (modular self-framing buildings, piping, instrumentation, electrical, HVAC, package auxiliaries listed together with the compressor).
2. **2 x 50% with no spare.** Capacity is shared across two parallel packages with no installed spare; availability comes from redundancy in operation, not from a dedicated spare machine.
   Source: DBM SEC-05 Compressor Item table; heading 33 "Scope Notes".
3. **Modularize for transport and field install.** Shop assembly minimizes site work; three-piece transport breaks the package down to road/rail-legal sections and supports field reassembly inside self-framing buildings.
   Source: DBM SEC-05 "Inlet Compression Overview".
4. **Source-grounded vendor scope.** The vendor's deliverable set is the heading-33 "Vendor Engineering Deliverables" list, not an abstracted convention. The EPC integration scope (DEL-080-06) operates on those vendor outputs.
   Source: heading 33 "Vendor Engineering Deliverables".
5. **NACE sour service is non-negotiable.** Composition includes H2S (~0.296 mol%), and all materials and seals must be NACE-compliant; this is treated as a hard constraint, not a value-engineering item.
   Source: DBM SEC-05; heading 33 "Scope Notes".

## Considerations

- **Inlet pressure basis discrepancy.** Heading 33 cites ~1275 kPag suction / ~6550 kPag discharge; DBM SEC-05 cites a multi-row pressure table in psig. The DBM table is the more authoritative current basis for compression design conditions, but the heading-33 single-line summary must be reconciled with the DBM table during vendor kickoff. See Conflict-02.
- **Model designation.** Heading 33 uses "Ariel KBZ/6"; DBM SEC-05 uses "Ariel KBC/6 (TBC)". Both are marked TBC, so the final model selection is a vendor-engineering item, but the project must pick a single nominal designation for downstream references. See Conflict-01.
- **VFD start basis.** SCA-001 VE #34 fixes VFD starting; soft starters are explicitly not in the current basis. VFD sizing remains an electrical detailed-design item that must be coordinated with the EPC.
- **Recycle valve failure action.** Recycle valves are "expected to fail open" but final failure action is TBC; this affects depressurization/blowdown logic (PRO-018) and should be ruled before relief sizing is closed.
- **Pressure equipment registration jurisdiction.** Site is BC per DBM SEC-01. Registration body and specific code reference is `location TBD`.
- **Aerial cooler environmental treatment.** Warm-air recirculation, automated louvers, and heating/plenum heat are vendor design items and depend on the SEC-02 ambient conditions; the EPC should not over-specify these in advance of vendor design.

## Trade-offs

| Trade-off | Direction Recommended | Rationale | Source |
|---|---|---|---|
| Installed spare vs 2x50% | No spare (current basis) | Capital cost discipline; operational redundancy through parallel units | DBM SEC-05 |
| TEFC vs WPII motor enclosure | Vendor to choose per environmental and maintainability tradeoff | DBM lists both as acceptable; final by vendor | DBM SEC-05 |
| Soft start vs VFD start | VFD start (fixed by SCA-001 VE #34) | Avoids voltage dip and torque transients; supports inverter-duty operation | DBM SEC-05 |
| Shop assembly vs site assembly | Shop assembly with three-piece transport | Reduces site labor, improves FAT scope | DBM SEC-05 |
| Vendor-supplied buildings vs site-built | Vendor modular self-framing buildings | Maintains single-vendor accountability for the package envelope | heading 33; DBM SEC-05 |

## Examples

- **Example interface boundary — Electrical Power.** Heading 33 flags Electrical Power "Yes": the EPC supplies 4,000 V medium-voltage power to a defined termination on the package; the vendor owns motor cabling, junction boxes, and grounding inside the package. (Detailed boundary location TBD until SLDs ELE-003 are issued.)
- **Example interface boundary — Process Piping.** Heading 33 flags Process Piping "Yes": the vendor terminates package process piping at flanged tie-in points listed in PIP-004 Tie-In List; the EPC pipes from facility headers to those tie-in points.
- **Example excluded interface — Cathodic Protection.** Heading 33 flags Cathodic Protection "No": no in-package CP scope; if buried package piping exists, CP is by EPC.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| Conflict-01 | Preliminary compressor model designation: "Ariel KBC/6" (DBM) vs "Ariel KBZ/6" (heading 33) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05 Compressor Item table | `_Sources/26020-Package_Requirements.docx` heading 33 "Major Included Equipment" | Datasheet Attributes; Specification R-080-04-002 | DBM SEC-05 (KBC/6) as the technical basis pending vendor confirmation | TBD |
| Conflict-02 | Suction/discharge pressure basis: ~1275 kPag / ~6550 kPag (heading 33) vs psig four-point table (DBM) | `_Sources/26020-Package_Requirements.docx` heading 33 "Scope Notes" | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-05 "Compression Design Conditions" | Datasheet Conditions; Specification R-080-04-003 | DBM SEC-05 multi-point table as the controlling basis; heading 33 numbers treated as a summary | TBD |
| Conflict-03 | Recycle valve failure action: "expected fail open" vs "final action TBC" | DBM SEC-05 | DBM SEC-05 (same source, internal TBC) | Specification R-080-04-006; relief / blowdown design | Resolve at vendor kickoff before PRO-014/PRO-018 are closed | TBD |
| Conflict-04 | NACE clause-level requirement (which standard family, which year) | heading 33 "Scope Notes" ("NACE-compliant") | (no clause-level text accessible in current source slices) | Specification R-080-04-004; Standards table | NACE MR0175 / ISO 15156 current edition as nominal basis | TBD |
