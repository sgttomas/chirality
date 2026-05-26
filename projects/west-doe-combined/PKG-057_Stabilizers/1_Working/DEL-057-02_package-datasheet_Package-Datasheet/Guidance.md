# Guidance: DEL-057-02_package-datasheet — Package Datasheet (PKG-057 Stabilizers)

> Directional document. Rationale and trade-offs. Inferences are explicitly labeled `ASSUMPTION`. Open conflicts are captured in the Conflict Table.

## Purpose

The Package Datasheet for PKG-057 Stabilizers is the EPC Integrator's mandatory Gate-5 technical handoff. It consolidates the package data a third-party vendor (or a downstream discipline) requires to engineer the package and to integrate it into the 04-25 Deepcut facility. (Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row DEL-057-02.)

The Stabilizers package itself receives raw condensate from the MPFF bottoms and produces stabilized hydrocarbon liquid for downstream product handling (SOW-0178). Three packages are deployed as 3 x 40% trains, supporting the 04-25 sour-gas processing objective (OBJ-001) and related package-set objectives.

## Principles

- **Source-anchored fidelity.** Every non-trivial value on the datasheet should be traceable to a workbook row, SOW item, register row, or document heading. (Authority: `_REFERENCES.md`; deliverable governance.)
- **Vendor / EPC ownership boundary kept explicit.** The Package Vendor owns package engineering and physical equipment; the EPC Integrator owns facility-level integration and interfaces (PACKAGE_REGISTER.csv PKG-057; SOW-0177). The datasheet should never blur this boundary.
- **Interfaces are first-class.** PKG-057 has 13 declared required interfaces. The datasheet carries the matrix because interface facts are intentionally consolidated here rather than created as standalone deliverables (`_CONTEXT.md` Notes).
- **3 x 40% configuration is a design intent, not just a count.** The 40% per-train rating and 3:1 turndown together govern operating flexibility; both must remain visible on the datasheet.
- **`By others` callouts protect scope clarity.** SOW-0180 explicitly carves interconnecting piping (skid edge), DCS integration, foundations, MCC power supply, and installation/erection out of vendor scope. The datasheet must reproduce this explicitly so downstream readers do not misallocate scope.

## Considerations

- **Source binaries not opened in this pass.** The authoritative `.docx` and `.xlsx` source documents (`26020-Package_Requirements.docx`, `26020-Packages_Interfaces_4_export.xlsx`, `26020-01-PT-RFQ-17-005_Inlet Stabilizers_R0.docx`, `4-25_Deepcut_DBM.md`) are listed in `_REFERENCES.md` but are not directly read in this drafting pass. Content here is grounded in the Gate-07 decomposition extracts (SCOPE_LEDGER, PACKAGE_REGISTER, INTERFACE_REGISTER), which are themselves source-attributed. A later pass should open the binary sources and refine any `location TBD` items.
- **Equipment list completeness.** The SOW extracts in SOW-0178 and SOW-0179 do not constitute a full vendor BOM; they identify major included equipment. The datasheet must mark the remainder of the BOM as `TBD` rather than synthesize content.
- **Standards/codes not enumerated.** No specific industry code list (ASME, API, NACE, etc.) is enumerated in the accessible source extracts. ASSUMPTION: such codes typically apply to a Mechanical Process Piping package of this type, but the specific roster must come from source binaries (location TBD) and is left `TBD` here.
- **Sour-gas service context.** OBJ-001 establishes the Deepcut facility as sour-gas processing. ASSUMPTION: NACE MR0175 / ISO 15156 and associated materials-selection considerations are typically applicable to sour service, but this should not appear as a datasheet requirement until source-confirmed.
- **Capacity and product cooler sizing.** The 130% sizing factor on the Stabilizer Product Cooler (SOW-0180) is a design intent that downstream users frequently misread as nameplate; the datasheet should keep "sizing" terminology to preserve the source meaning.

## Trade-offs

- **Verbatim source quoting vs. editorial harmonization.** SOW-0178's narrative ends mid-sentence (`...It.`) in the SCOPE_LEDGER extract. ASSUMPTION: the source `.docx` continues beyond what the ledger captured. The datasheet should preserve the source-accurate facts already cited and leave continuation `TBD` rather than fabricate a smooth narrative.
- **Datasheet vs. specification scope.** Some readers expect a "datasheet" to contain only equipment-line data. Here it is used as the EPC handoff anchor and intentionally carries broader interface and ownership content (`_CONTEXT.md` Notes). The companion `Specification.md` carries the normative requirements that govern the datasheet's content.
- **Granularity of interface matrix.** All 13 interfaces are flagged `Required = YES` in the snapshot. Detailed interface specifics (e.g., tie-in tags, voltages) are not in the source extracts and are `TBD`; a coarse-grained matrix is the right floor until those are sourced.

## Examples

Examples drawn from source extracts (illustrative, not generative):

- **Operating conditions row example.** "Flash Feed Separator — Operating Pressure 345 kPag; Temperature 30.6 °C; Retention Time ~15 min" — quoted from SOW-0180. The datasheet should render this in tabular form alongside the design conditions row for the same equipment.
- **Interface row example.** "Electrical Power — IFC-B993178278 — Required: YES — Source: Workbook Packages row 82" — composed from INTERFACE_REGISTER.csv row for PKG-057.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling |
|---|---|---|---|---|---|---|
| CONF-001 | SOW-0178 narrative truncates mid-sentence (`...It.`); downstream of feed pumps the process flow is not captured in the accessible extract. | SCOPE_LEDGER.csv SOW-0178 | 26020-Package_Requirements.docx package heading 12 (binary, not opened) | Datasheet > Attributes > Package Function; Specification > Scope | PROPOSAL: open the `.docx` source slice and replace the truncated text with the complete process-function paragraph; until then, retain truncated quote and mark continuation `TBD`. | TBD |
| CONF-002 | Sour-service materials/code applicability (e.g., NACE MR0175) is not enumerated in accessible extracts; OBJ-001 establishes sour-gas context. | OBJECTIVE_REGISTER.csv OBJ-001 | 26020-Package_Requirements.docx (binary, not opened) | Specification > Standards; Guidance > Considerations | PROPOSAL: leave standards/codes `TBD`; open source `.docx`/DBM to confirm code list before introducing requirements. | TBD |
| CONF-003 | Full vendor BOM (beyond major included equipment named in SOW-0178/SOW-0179) not enumerated in accessible source extracts. | SCOPE_LEDGER.csv SOW-0178, SOW-0179 | 26020-Package_Requirements.docx package heading 12 (binary, not opened) | Datasheet > Construction; Specification > R-DS-07 | PROPOSAL: keep cited major equipment authoritative; mark remainder of BOM `TBD` until source `.docx` is opened. | TBD |
