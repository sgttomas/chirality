# Guidance — DEL-065-05 Vendor Document Turnover Package

## Purpose

This deliverable exists so that the EPC Integrator receives a single, auditable evidence package for PKG-065 (Tanks, Caustic, API 650, 4-25) covering what the Package Vendor designed, built, inspected, tested, and shipped — sufficient to integrate the equipment into facility commissioning and to satisfy code-of-construction (modified API 650) traceability. The decomposition explicitly carves this out as a distinct Gate 5 deliverable so that individual source-document table rows can be preserved as artifacts under one accountable package rather than fragmenting into many small deliverables. (Source: `_CONTEXT.md` Scope and Notes; DELIVERABLE_REGISTER.csv row DEL-065-05.)

## Principles

- **Single register, full traceability.** Every document the Vendor will ever submit for PKG-065 lives on one register, traceable to a scope item (`SOW-0197`..`SOW-0200`) and to a tagged piece of equipment (TK-6780-1; Fresh Caustic Tank). (Source: SCOPE_LEDGER rows; `_CONTEXT.md`.)
- **Source-required rows are evidence, not separate deliverables.** When the workbook or `26020-Package_Requirements.docx` package heading 20 enumerates a specific vendor document, it is preserved here as evidence rather than spawning a new deliverable. (Source: `_CONTEXT.md` Notes.)
- **Vendor produces; EPC Integrator accepts.** The responsibility split is binary and explicit: Package Vendor owns production of documentation; EPC Integrator owns interface/integration review. (Source: `_CONTEXT.md` ResponsibleParty.)
- **Code traceability over completeness theatre.** Documentation depth is driven by what modified API 650 and the source materials demand, not by exhaustive bureaucratic templates. Deviations from base API 650 SHALL be documented (cross-ref DEL-065-04 R-01).

## Considerations

- The authoritative enumeration of source-required vendor documents lives in a binary `.docx` (`26020-Package_Requirements.docx` package heading 20) that was not directly read in this drafting run. The Rev. 0 register cannot be considered final until that slice is extracted. Treat `TBD` markers on document line items as load-bearing, not cosmetic.
- "Modified" API 650 implies deviations from the published standard. Capture the deviations in a dedicated document on the register so that downstream operators and inspectors can read them in one place rather than diffing the standard against fabrication records.
- The Fresh Caustic Tank has no asserted tag in the source slices accessed in this run. Until a tag is confirmed, all references to the fresh tank on the register and in turnover records will read as "Fresh Caustic Tank (tag `TBD`)". Avoid inventing a tag.
- Turnover record content beyond what the source explicitly enumerates is labeled ASSUMPTION (industry-typical for atmospheric API 650 tanks). EPC Integrator review should either confirm or trim the assumed list before the Vendor builds against it.

## Trade-offs

- **Granular register vs. shippable register.** A maximally granular register (one line per drawing sheet, one line per MTR) gives perfect traceability but slows review. A coarse register (one line per document family) ships faster but obscures gaps. Default to the granularity stated by the source-required rows when extracted, and group only where the source itself groups.
- **Early Rev. 0 vs. wait-for-source.** Issuing Rev. 0 of the register before the binary source slice is extracted accelerates schedule but locks in an incomplete list. The right call depends on whether EPC Integrator can tolerate revision churn or needs early certainty.
- **Vendor-template turnover records vs. project-template.** Vendor templates are faster and familiar to the fabricator; project templates are uniform across all packages and simpler for the EPC Integrator. Either is acceptable provided traceability requirements are met.

## Examples

No worked examples are available in the locally accessible source slices for PKG-065 vendor document turnover specifically. See sibling deliverable DEL-065-04 (Vendor Engineered Equipment Package) for the engineering-side companion that this documentation package evidences.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|

No conflicts identified across the drafted four documents at Pass 2. All gaps are recorded as `TBD` or `ASSUMPTION` rather than contradictions, because the binary source slice for vendor-document-specific requirements (`26020-Package_Requirements.docx` package heading 20) was not directly read and therefore could not contradict the drafted text.
