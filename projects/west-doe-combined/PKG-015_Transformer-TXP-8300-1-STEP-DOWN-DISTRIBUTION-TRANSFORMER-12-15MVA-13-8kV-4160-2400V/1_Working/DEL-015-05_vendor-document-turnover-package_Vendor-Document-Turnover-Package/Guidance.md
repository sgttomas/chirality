# Guidance: DEL-015-05_vendor-document-turnover-package

## Purpose

This Guidance explains how to interpret and execute the Vendor Document Turnover Package for PKG-015 (Transformer TXP-8300-1, 12/15 MVA step-down distribution transformer) consistently with the decomposition, `_CONTEXT.md`, and accessible source materials. It also surfaces interpretive ambiguities that require human ruling before drafted requirements harden.

Source basis: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-015-05`; `PACKAGE_REGISTER.csv` row `PKG-015`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; `_Sources/26020-Package_Requirements.docx`.

## Principles

1. **Vendor authorship, EPC review.** The Package Vendor produces and owns the vendor document register, submittals, and turnover records. The EPC Integrator reviews these for interface/integration impact rather than re-authoring them. This split mirrors the PKG-015 responsibility model in `PACKAGE_REGISTER.csv`.
2. **Source-row primacy.** Where a vendor document arises directly from a source-material row (DBM, package requirements, applicable standard), the register entry should cite that row. Where it does not, the entry should be labeled as derived from deliverable-type convention rather than asserted as a source-grounded requirement. This is consistent with `_CONTEXT.md` Anticipated Artifacts ("source vendor document table rows as artifacts where available") and with the deliverable's "additional Gate 5" framing.
3. **Artifacts, not decomposition.** Individual source vendor document rows are tracked as artifacts/evidence within this deliverable. They are not promoted to separately decomposed deliverables. This is explicit in `_CONTEXT.md` Notes and `DELIVERABLE_REGISTER.csv`.
4. **Interface fidelity.** The register and turnover records should preserve traceability to the seven applicable interface types declared for PKG-015 (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports).
5. **Project standard core block.** The recurring "Core vendor documents" block in the project package requirements document (PRQ-009 Vendor Document Index; DOC-008 Vendor Document Control Procedure; QLT-006 Supplier Quality) is applied as the baseline document-control framework, even though a PKG-015–specific section was not located in the searched extract.

## Considerations

- **Equipment-class specifics are sparse in available sources.** The PKG-015 transformer is identified by name only in Workbook row 17 and `PACKAGE_REGISTER.csv`. The accessible DBM mentions a "13.8 kV to 4.16 kV, 12 MVA transformer" feeder under "Incoming Power and Transformers" (3-25 DBM, lines 738-745), which plausibly corresponds to TXP-8300-1 but is not explicitly tagged. Treat this correspondence as an ASSUMPTION until confirmed.
- **Package requirements text gap.** `_Sources/26020-Package_Requirements.docx` is structured around process (`26020-01-PT-*`) packages. No PKG-015 / TXP-8300-1 step-down distribution transformer section was located in the searched extract. The "Core vendor documents" block recurs across per-package sections and is applied here by analogy.
- **Transformer-equipment standards.** Specific standards for medium-voltage step-down distribution transformers (e.g., IEEE C57 family, IEC 60076, CSA C88, IEEE/ANSI C57.12 series) are likely applicable but cannot be cited at clause level without accessible source text. Treat as ASSUMPTION; resolve via vendor data and an accepted standards register.
- **Turnover record list depth.** A typical transformer turnover package includes factory acceptance test (FAT) reports, type test certificates, insulation resistance and turns-ratio tests, dielectric and impulse test records, oil quality reports (if oil-filled), nameplate data, as-built drawings, O&M manuals, spare parts list, and warranty documentation. The Specification leaves R-08 as TBD pending source.
- **EPC review scope.** EPC review should focus on cross-package interface integrity (grounding/bonding interconnect, control cabling tie-ins, structural foundation interfaces, area lighting and access) rather than on internal transformer design choices, consistent with the package responsibility model.

## Trade-offs

- **Conservative register vs. completeness.** A narrow, source-grounded register understates real turnover obligations. A broad register risks asserting requirements not warranted by source. The Specification favors a source-grounded register augmented by explicit `TBD`/ASSUMPTION markers, preserving the human's ability to ratify additions.
- **Per-row artifact tracking vs. cross-decomposition.** Treating each source vendor document row as an artifact (not a deliverable) keeps the decomposition flat and aligns with `_CONTEXT.md` Notes; it does mean traceability lives inside the register rather than in the deliverable tree.
- **Project-standard block by analogy.** Adopting the PRQ-009 / DOC-008 / QLT-006 core block by analogy provides immediate document-control coverage but is technically an assumption until a PKG-015–specific section confirms applicability.

## Examples

- A vendor-supplied transformer test report (FAT, dielectric, turns-ratio) should appear as a register entry under turnover records, with source row pointer marked TBD until the PKG-015 package requirements section is located.
- An as-built drawing supplied by the transformer vendor should appear as a register entry and should be cross-checked against the EPC integration package for foundation, grounding, and cable-tray interface fit.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-015-05-001 | The DBM "Incoming Power and Transformers" row "13.8 kV to 4.16 kV, 12 MVA transformer" is plausibly the same equipment as TXP-8300-1 (PKG-015), but the DBM does not carry the TXP-8300-1 tag. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, lines 738-745 | Workbook Packages row 17 / `PACKAGE_REGISTER.csv` row `PKG-015` (package title TXP-8300-1, 12/15 MVA, 13.8 kV / 4160/2400 V) | Datasheet "DBM coupling — Incoming Power and Transformers"; Guidance Considerations | PROPOSAL: treat as the same equipment and use the DBM row as context; record as ASSUMPTION until confirmed. | TBD |
| HRR-015-05-002 | `_Sources/26020-Package_Requirements.docx` contains a recurring "Core vendor documents" block (PRQ-009 / DOC-008 / QLT-006), but no PKG-015–specific section was located in the searched extract; applicability is by analogy. | `_Sources/26020-Package_Requirements.docx`, recurring "Core vendor documents" block | `_Sources/26020-Package_Requirements.docx`, TOC (process-`PT`-keyed only) | Specification R-02, R-07, Standards; Datasheet "Core vendor document references" | PROPOSAL: apply the core block as baseline; mark PKG-015 package-requirements text as `location TBD`. | TBD |
| HRR-015-05-003 | The specific transformer-equipment standards governing this 12/15 MVA, 13.8 kV / 4160/2400 V step-down distribution transformer are not enumerated in any source slice locally accessible to this deliverable. | None located | None located | Specification Standards, R-08; Datasheet Attributes | PROPOSAL: keep the standards row as ASSUMPTION (likely applicable) and resolve via accepted standards register or vendor data. | TBD |
| HRR-015-05-004 | The detailed turnover-record list (FAT reports, dielectric/impulse, turns-ratio, insulation, oil quality, nameplate, as-builts, O&M, spares, warranty, etc.) cannot be enumerated from accessible source text. | None located | Deliverable-type convention | Specification R-08; Procedure Steps | PROPOSAL: leave the detailed list TBD and pull from vendor data and the standards register once available. | TBD |
