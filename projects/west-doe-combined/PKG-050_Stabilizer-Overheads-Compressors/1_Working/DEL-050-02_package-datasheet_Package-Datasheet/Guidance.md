# Guidance — DEL-050-02 Package Datasheet (Stabilizer Overheads Compressors)

## Purpose

The Package Datasheet is the EPC Integrator's technical handoff to the Package Vendor. It is the consolidated, source-grounded data package required for third-party vendor or discipline package engineering and design (`_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-050-02). It is one of the mandatory Gate 5 EPC anchor deliverables for PKG-050 alongside the EPC Scope of Work (DEL-050-01) and the Construction Work Package (DEL-050-03).

Per `_CONTEXT.md`, interface facts for the package are intentionally carried in this datasheet as evidence rather than as standalone deliverables. The datasheet therefore plays two roles: (i) technical data carrier; (ii) authoritative interface-inventory carrier for downstream vendor handoff.

## Principles

1. **Source fidelity over convention.** Numeric values, equipment selections, and operating limits come from `26020-Package_Requirements.docx` heading 5 (via the gate-snapshot SCOPE_LEDGER rows SOW-0173..SOW-0176) and the workbook Packages row 81 (via PACKAGE_REGISTER / INTERFACE_REGISTER). Where the source does not state a value, the datasheet marks `TBD` rather than inventing one.
2. **Responsibility split is explicit.** Package Vendor owns package engineering, design, vendor documentation, and the physical package; EPC Integrator owns facility-level integration and interfaces (`PACKAGE_REGISTER.csv` Responsibility text). Items "by others" listed in SOW-0176 must be flagged in the datasheet so the vendor does not silently absorb or exclude them.
3. **Two-of-a-kind, 100% each.** The 2x identical 100%-capacity configuration (SOW-0174) is load-sharing redundancy, not 2x50% sparing. Guidance text and procedures should not blur this.
4. **No Toshiba motors.** This exclusion appears twice in source (SOW-0175 and SOW-0176); treat as a hard supply constraint.
5. **Interface inventory completeness.** All 13 PKG-050 interface types in `INTERFACE_REGISTER.csv` are flagged YES; none may be silently dropped from the package interface requirements matrix.

## Considerations

- **Pressure envelope is wide.** 50 psig → 1100 psig final discharge (SOW-0174) implies a four-stage machine with per-stage MAWP varying from 1723 kPag (1st-stage suction) to ≥ 9101 kPag (final-stage discharge at 177 C) (SOW-0176). Vessel and piping code stamping must reflect per-stage envelopes, not a single project-wide value.
- **Truncated source values.** The Stage 3 cooler discharge temperature is truncated in the extracted source slice as "3rd." (SOW-0176). The Stage 4 cooler discharge temperature and several "Other MAWP" values are TBC per source. These are real evidence gaps, not omissions to fix by inference; they should be raised to the source author.
- **Air cooler frame designation "Ap-661 (modified)".** This appears to be a vendor model reference; ASSUMPTION: it is a manufacturer model designation requiring vendor lookup. Not verified in this run.
- **By-others list shapes the construction work package.** Shipping to site, installation on piles, tie-in piping, electrical connections, mounting platform and stairs (SOW-0176) all become EPC-owned scope in DEL-050-03. The datasheet's by-others list must be the single source of truth for that split.
- **Workbook source not opened in this run.** Workbook Packages row 81 and the `.docx` source were not opened directly; this draft is grounded in the gate-snapshot extracts. Verbatim verification before vendor handoff is recommended.

## Trade-offs

- **Carrying interfaces as datasheet evidence vs. separate deliverable.** The decision (`_CONTEXT.md`) to carry interface facts here keeps the vendor handoff package single-headed but means the datasheet must explicitly include an interface requirements matrix with side-of-line responsibility and tie-in detail. The trade-off is concentration of risk in one document.
- **Speed control + 3:1 turndown vs. recycle valve sizing.** Both are specified (SOW-0175, SOW-0176). Operating philosophy guidance for when to use speed control vs. recycle is `TBD` from accessible source — should be settled with the process owner before vendor handoff.
- **Quote TEFC enclosure but enclosure TBD.** The source instructs to quote TEFC but leaves the final enclosure designation open (SOW-0176). The trade-off (TEFC vs. WPII vs. XPFC) hinges on area classification (`TBD` here) and should not be silently resolved by the datasheet.

## Examples

- **Example interface row (Process Piping, IFC-67DA240B8B):** Flagged YES for PKG-050 in `INTERFACE_REGISTER.csv`. The datasheet's matrix entry must capture: tie-in tag, nominal size, rating, side-of-line responsibility, and reference P&ID. All of these are `TBD` in accessible sources for this run.
- **Example exclusion row:** "Installation on piles" (SOW-0176) → recorded as carried by others; flows into DEL-050-03 Construction Work Package work-face plan rather than the vendor package.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-001 | Stage 3 cooler discharge temperature truncated as "3rd." with no value | SCOPE_LEDGER SOW-0176 (Cooler discharge temperatures) | n/a | Datasheet > Operating Conditions; Specification REQ-DS-41 | Retrieve verbatim from `26020-Package_Requirements.docx` heading 5 Operating conditions table | TBD |
| CONF-002 | Final-stage discharge value labeled "compression (7585 kPag)" — unclear whether 7585 kPag is the discharge pressure or a separate compression-pressure datum; also inconsistent with 1100 psig (~7584 kPag) basic-scope figure | SCOPE_LEDGER SOW-0174 (50 psig→1100 psig) | SCOPE_LEDGER SOW-0176 (4th stage: discharge / compression (7585 kPag)) | Datasheet > Operating Conditions; Specification REQ-DS-40, REQ-DS-43 | Treat 7585 kPag ≈ 1100 psig as final-stage discharge; verify verbatim wording with source | TBD |
| CONF-003 | Motor data appears twice with slight wording differences (SOW-0175 lists "2700 HP with speed control and automated recycle valve, 4000V,3PH,60Hz"; SOW-0176 adds "8 Pole", "891 RPM", enclosure "TBD (quote TEFC)") | SCOPE_LEDGER SOW-0175 | SCOPE_LEDGER SOW-0176 | Datasheet > Driver/Motor; Specification REQ-DS-20..25 | Treat SOW-0176 as the more complete instance; both rows are from the same Word heading 5 | TBD |
| CONF-004 | "MAWP is 1723 kPag at 1st stage suction" — is 1723 kPag the MAWP of the 1st-stage suction vessel/piping or a project-floor MAWP? "Other MAWP is TBC." | SCOPE_LEDGER SOW-0176 | n/a | Datasheet > Design Conditions; Specification REQ-DS-43 | Confirm per-stage MAWP table with vendor and source author | TBD |
| CONF-005 | Air cooler "Ap-661 (modified)" — unidentified model reference | SCOPE_LEDGER SOW-0175 / ARTIFACT_REGISTER ART-15F17CEA07 | n/a | Datasheet > Auxiliaries | Verify with vendor catalog (likely a manufacturer model designation) | TBD |
