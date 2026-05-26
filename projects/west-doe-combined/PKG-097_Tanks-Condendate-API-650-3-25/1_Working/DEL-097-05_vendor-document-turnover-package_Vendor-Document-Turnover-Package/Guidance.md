# Guidance — DEL-097-05 Vendor Document Turnover Package

> Pass 1/2 generation by `TASK + four-documents`. Rationale drawn from accessible sources; otherwise `TBD`.

## Purpose

The Vendor Document Turnover Package exists to consolidate, control, and hand off the full set of Package-Vendor-issued documentation for `PKG-097` Tanks, Condendate (API 650) 3-25, so the EPC Integrator can complete vendor package review and acceptance under `DEL-097-06` and so operations/owner records contain a complete, traceable as-built dossier for the tank field (decomposition register row DEL-097-05; `_CONTEXT.md`).

## Principles

- **Register first, submittals second.** The vendor document register is the controlled index; individual submittals derive their identity, revision, and status from the register. (DBM SEC-09 line 617.)
- **Source-row fidelity.** Where the source documents (Workbook Packages row 88; 26020-Package_Requirements.docx package heading 49) name a specific vendor document, the corresponding register row must trace to that source. (`_CONTEXT.md`; specific row list `TBD`.)
- **Code-of-construction traceability.** Tank documentation must connect physical fabrication evidence to the API 650 / API-650 Modified basis stated in DBM SEC-06 line 421 and in the package name.
- **Cold-climate realism.** Vendor documentation must reflect the -40 deg C minimum ambient governing exposed equipment (DBM SEC-02 line 145); generic-climate vendor templates should be redlined where they conflict.
- **EPC-vendor interface clarity.** The Package Vendor owns issuance; the EPC Integrator owns interface/integration review. Roles must not blur in the transmittal log. (`_CONTEXT.md` ResponsibleParty.)

## Considerations

- The full source list of required vendor documents is anchored in `26020-Package_Requirements.docx` (heading 49) and the Workbook Packages register. Both sources exist in `_Sources/` as binary/spreadsheet and were not text-accessible in this pass; the register and submittal list cannot be enumerated row-for-row until those sources are extracted to text.
- The package mixes condensate-service and produced-water-service tanks (DBM SEC-06 lines 406, 421); vendor documentation should preserve service segregation, especially for materials, coatings (Devchem 253 on produced-water tanks), and sour-service applicability.
- Some tank parameters in the DBM are explicitly `TBC` (e.g., produced-water tank SG 1.25 vs pump basis 1.18, DBM SEC-06 line 421); vendor documentation must not silently resolve these — open items should be flagged in the register and routed to detailed design closure.

## Trade-offs

- **Single comprehensive register vs split sub-registers** (e.g., by tank service or by document type): a single register simplifies turnover and EPC review; sub-registers can ease vendor production. Decision basis: `TBD` (no source guidance located).
- **Submittal granularity** (one transmittal per document vs batched transmittals): finer-grain transmittals improve traceability; coarser transmittals reduce administrative load. Decision basis: `TBD`.

## Examples

- Examples of completed vendor turnover registers or transmittal logs from prior 03-25 / 04-25 packages: none located in accessible sources — `TBD`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 | Package name asserts "API 650" for the tank package, but accessible DBM source explicitly states API-650 Modified only for produced-water tanks; the code basis clause for condensate tanks is not located in any text-accessible source. | Package name "Tanks, Condendate (API 650) 3-25" (`_CONTEXT.md`; decomposition register) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 line 421 (PW only) | Datasheet Attributes; Specification R-05, R-06; Standards table | PROPOSAL: condensate tanks are API 650 (or API-650 Modified) per package naming convention; confirm explicit code basis clause from source still to be located (likely in 26020-Package_Requirements.docx heading 49). | TBD |
| CT-02 | The deliverable scope references "source vendor document table rows as artifacts where available" but the source tables (Workbook Packages row 88; 26020-Package_Requirements.docx package heading 49) are binary/spreadsheet and were not text-accessible this pass, so specific rows cannot be enumerated. | `_CONTEXT.md` Anticipated Artifacts | `_REFERENCES.md` Source Materials | Datasheet Construction; Specification R-03; Guidance Considerations | PROPOSAL: extract `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` to text/CSV, then re-run this skill or update the four documents with the specific row list. | TBD |
| CT-03 | Produced-water tank design SG (1.25) and pump-fluid SG basis (1.18) disagree, per DBM SEC-06 line 421 ("discrepancy shall be closed during detailed design"). Vendor documentation must reflect one of them or both. | DBM SEC-06 line 421 (tank design SG 1.25 TBC) | DBM SEC-06 line 421 (pump basis SG 1.18) | Datasheet Conditions (implicit); Specification R-05 verification | PROPOSAL: vendor documentation flags this as an open item carried to detailed design; closure recorded in register. | TBD |
