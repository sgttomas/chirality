# Guidance: DEL-079-02 — Package Datasheet (Instrument Air Building, PKG-079)

## Purpose

This Package Datasheet exists because the Instrument Air Building is a **Gate-5 EPC anchor** mandatory deliverable: it is the technical handoff that lets a third-party vendor or discipline package take the package from EPC-Integrator-controlled scope into engineered, fabricated, and installed reality. Interface facts (utility, electrical, I&C, structural, fire & gas) are intentionally carried here as **evidence** rather than as standalone deliverables, per the deliverable's `_CONTEXT.md` note.

## Principles

1. **Source-grounded, not narrative-grounded.** Equipment counts, design pressures, dew point, and PSV settings come from the Requirements doc and the Packages interface register — not from generic instrument-air convention. If the source defers to the vendor, this datasheet defers to the vendor (`TBD`), not to convention.
2. **Vendor handoff over EPC redesign.** This datasheet sizes the package envelope (capacity, pressures, temperatures, dew point, motor class, PSV setting); detailed equipment design — including dryer and receiver sizing — is explicitly a vendor activity.
3. **Interfaces are evidence.** The interface matrix (R7) is the authoritative coordination contract with all other disciplines/packages. Any future change to interface applicability must flow back to `26020-Packages_Interfaces_4_export.xlsx` row 69.
4. **By-others boundary is non-negotiable.** Shipping, piling installation, tie-in piping, electrical termination, mounting platform, and stairs are out of vendor scope. Treat these as battery-limit assumptions for both quoting and construction.

## Considerations

- **Shared 4-25 / 3-25 service.** Per the source-basis table, the Instrument Air Building serves both 4-25 and 3-25 facilities. Capacity, availability, and sectionalization should be evaluated against the combined load — not 4-25 alone.
- **Dryer redundancy and "leave".** The dryer is 100% with two towers; sizing must include the leave-air loss for regeneration when both compressors are running. Source uses the phrase "sized for 2 compressors and leave" — vendor must demonstrate compliance.
- **Motor electrical class.** Motors are **non-classified**, which presumes the air compressors are inside a non-hazardous (non-classified) building envelope. The Building HVAC / Services interface applies (R7.1); HVAC and area classification design must preserve this assumption. If site area classification revises this, R3.2 and the motor data sheets change.
- **Compressor count is fixed at 2.** Source does not specify a spare philosophy beyond two units; assess whether 2 × 1113 SCFM (no installed spare beyond N+1 implicit duty/standby) is adequate for site-wide instrument-air demand under loss of one compressor. *(`ASSUMPTION: duty/standby philosophy`; confirm against facility utility summary `PRO-011`.)*
- **PSV vs system pressures.** PSV set at 948 kPag (137.5 psig) sits above maximum compressor discharge / shutdown (1000 kPag) does **not** hold — see CT-03 below; this is a numeric inconsistency in the source that must be ruled on by the human.

## Trade-offs

- **Soft starter vs VFD-ready** (R3.2): VFD-ready allows future capacity modulation and energy savings but adds harmonic and motor-derating concerns; soft starter is simpler and cheaper. Source allows either — vendor proposal should justify selection in the Motor Starting Study (`ELE-011`).
- **Single dry receiver vs 2 × 50%:** Two 50% receivers improve maintainability and redundancy but increase footprint and cost. Source allows either.
- **Building HVAC vs outdoor enclosure:** Package is a building; HVAC service is an applicable interface (R7.1). Outdoor enclosure is not an option in this scope basis.

## Examples

No worked examples are present in the source slices; this section is intentionally minimal. Add examples only when a downstream consumer (e.g., utility summary or facility air balance) produces locally accessible figures.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 | Interface register version: Requirements doc cites `26020-Packages_Interfaces.3.xlsx`; locally accessible file is `26020-Packages_Interfaces_4_export.xlsx` (rev 4). | `26020-Package_Requirements.docx` § Physical Interface Summary | `_Sources/26020-Packages_Interfaces_4_export.xlsx` sheet `Packages` row 69 | Datasheet § Physical Interface Summary; Specification R7 | Use the newer rev-4 export as authoritative; note that the Requirements doc reference is at rev 3. | TBD |
| CT-02 | Motor HP rating: Major Included Equipment states **250 HP**; scope-notes table states **200-250 HP**. | `26020-Package_Requirements.docx` § Major Included Equipment | `26020-Package_Requirements.docx` § scope-notes table | Datasheet § Operating and Design Conditions; Specification R3.1 | Use **250 HP** as the design point (upper bound of the range), allowing vendor to size at 200 HP only with EPC ruling. | TBD |
| CT-03 | PSV set pressure 948 kPag (137.5 psig) is **below** the compressor max discharge / shutdown 1000 kPag and the maximum system design pressure 1034 kPag (150 psig). Conventional practice would set PSV at or near MAWP, above the compressor's high-pressure shutdown. | `26020-Package_Requirements.docx` § Major Included Equipment ("PSVs set at 948 kPag") | `26020-Package_Requirements.docx` § scope-notes table (compressor shutdown 1000 kPag; system design 1034 kPag) | Specification R4.5, R4.2, R4.1; Procedure verification steps | Re-confirm PSV set pressure with process safety / vendor; likely the 948 kPag value is a typo or refers to a specific receiver/PSV rather than all PSVs. Do not proceed to FAT until ruled. | TBD |
| CT-04 | Original RFQ basis `26020-01-PT-RFQ-39-001_Instr_Air_Bldg_R1.docx` is cited as the source basis but is **not locally accessible**. | `26020-Package_Requirements.docx` § source-basis table | (absent) | All sections | Treat the Requirements-doc section as the working authority until the RFQ R1 file is staged in `_Sources`. | TBD |
