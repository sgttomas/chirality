# Guidance — DEL-080-05 Vendor Document Turnover Package

## Purpose

The Vendor Document Turnover Package is the single Package-Vendor deliverable that consolidates the vendor document register, all required vendor submittals, and the turnover records for `PKG-080 Inlet Compressors`. It exists so that the EPC Integrator can review and accept the vendor package against the EPC Scope of Work, Package Datasheet, and Construction Work Package, and so the Owner ultimately receives a complete, controlled record of the equipment package as built and tested.

Source authority: `26020-Package_Requirements.docx` heading 33 → Vendor Engineering Deliverables (the document set this turnover package controls); `_CONTEXT.md` (responsibility and scope); `DELIVERABLE_REGISTER.csv` (deliverable identity and downstream consumer).

## Principles

1. **The source vendor deliverables table is the document-scope authority.**
   The 114-row table at heading 33 (Table 133) is what the vendor must produce. The turnover package does not add documents that the source does not require, and does not omit documents the source requires. Additions or omissions must be reconciled against the EPC Scope of Work and Package Datasheet, and recorded as scope changes.

2. **The Vendor Document Index (PRQ-009) is the operational backbone.**
   Every other document in the package is enumerated, revisioned, transmitted, and reviewed through the index. The index is updated continuously, not just at turnover.

3. **The Vendor Document Control Procedure (DOC-008) is the rule book.**
   Numbering, revision states, transmittal mechanics, hold/code/review codes, and acceptance flow all live in DOC-008. When DOC-008 contradicts informal practice, DOC-008 wins. (DOC-008 is not yet locally accessible — see Conflict Table.)

4. **Turnover is staged, not a single event.**
   The vendor data books (PRQ-016 / MEC-023) are the final, consolidated artifact, but FAT/SAT, material certs, as-builts, and regulatory packages are issued at their natural points in the schedule. The turnover package is the running compilation, not only the final book.

5. **Source-required documents stay first-class; they are artifacts of this deliverable, not standalone deliverables.**
   Per `_CONTEXT.md` Notes, individual source document rows are evidence under this deliverable, not separate decomposition deliverables. The decomposition deliberately keeps them aggregated here.

6. **Interface to acceptance lives in DEL-080-06.**
   Vendor turnover (this deliverable) provides the controlled record. The acceptance ruling lives in `DEL-080-06_epc-vendor-package-review-and-acceptance`. Do not co-mingle.

## Considerations

- **Document granularity vs. package granularity.** The source vendor deliverables table is granular (e.g., separate IDs for Foundation Drawings and Anchor Bolt Drawings). Vendors may issue these as a single transmittal or as separate documents. The Vendor Document Index must preserve the source-level granularity in its rows even if a single vendor PDF satisfies multiple rows.

- **NACE compliance evidence is non-trivial.** The package is sour-service (Table 131: "NACE-compliant materials and seals are required"). Material Test Reports (QLT-013) need explicit NACE-compliance flags per item, not just generic certs.

- **Two-unit configuration.** With 2 × 50% identical units (Table 131), expect two sets of unit-specific documents (e.g., compressor data sheets, FAT reports) plus shared design-basis and package-level documents. The index should disambiguate.

- **Budgetary go-by reference is not contract.** Table 130 notes `24292-02-PT-ENR-12-201_Compressors_R2.pdf` as a budgetary pricing/delivery go-by only. It is not the document control basis for turnover; do not propagate its numbering, terms, or quantities into the vendor index without verification.

- **Interfaces file naming discrepancy.** Source heading 33 → Physical Interface Summary cites `26020-Packages_Interfaces.3.xlsx`; the locally accessible file is `26020-Packages_Interfaces_4_export.xlsx`. Treat as a revision/export-naming discrepancy and follow the more recent file unless a human ruling says otherwise (see Conflict Table).

## Trade-offs

- **Comprehensive index vs. transmittal burden.** A finer-grained index (one row per source ID) increases administrative load but makes acceptance verification straightforward. A coarser index (one row per vendor PDF) shifts burden to verification time. Preferred posture: fine-grained index, coarse transmittals — index resolves the mapping.

- **Stage-by-stage submittal vs. final-book-only.** Issuing only the final vendor data books reduces EPC review cycles but produces a one-shot review surge at turnover. Stage-by-stage submittal smooths review load and surfaces defects early; preferred where DOC-008 permits.

- **Native vendor numbering vs. project numbering.** Native numbering preserves vendor configuration management; project numbering eases EPC consumption. PRQ-009 should carry both columns to avoid the trade-off entirely.

## Examples

- The source vendor deliverables table for PKG-080 enumerates ~114 document IDs across 12 functional groups (core vendor docs, core package engineering, rotating equipment, relief/flare, process piping, utility piping, drainage/containment, electrical, instrumentation/controls, building/HVAC, fire/gas, structural). The Vendor Document Index (PRQ-009) must therefore have at least one row per enumerated source ID. See `Datasheet.md` for the full enumeration.

- A Material Test Report (QLT-013) for a sour-service compressor cylinder is included in the turnover package with a NACE compliance flag and a link to the relevant Mechanical Equipment Data Sheet (MEC-003) entry.

- The Equipment FAT Performance Test Report (MEC-022) is issued as soon as FAT is complete; the executed copy is then bound into the Mechanical Final Documentation (MEC-023) at turnover.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-01 | Submittal revision stages not stated in source | heading 33 (no stages defined) | Industry convention (Bid/IFR/IFA/IFC/As-Built) | Specification REQ-13; Datasheet Conditions | PROPOSAL: adopt Bid/IFR/IFA/IFC/As-Built pending DOC-008 issuance | TBD |
| C-02 | Transmittal medium not stated | heading 33 (silent) | Project document-control standard (not locally accessible) | Specification REQ-15; Datasheet Conditions | PROPOSAL: confirm against issued DOC-008 | TBD |
| C-03 | Review turnaround not stated | heading 33 (silent) | Project document-control standard | Specification REQ-14 | PROPOSAL: confirm against project doc-control matrix | TBD |
| C-04 | Interfaces filename mismatch | heading 33 cites `26020-Packages_Interfaces.3.xlsx` | Local file is `26020-Packages_Interfaces_4_export.xlsx` | Datasheet References; Guidance Considerations | PROPOSAL: use the `_4_export` file as the latest revision unless overruled | TBD |
| C-05 | NACE document not cited at clause level | heading 33 Table 131 (calls for "NACE-compliant materials and seals" without document number) | NACE MR0175 / ISO 15156 (ASSUMPTION) | Specification REQ-12, Standards table; Datasheet Conditions | PROPOSAL: adopt NACE MR0175 / ISO 15156 as the controlling reference; confirm with project metallurgy | TBD |
| C-06 | Pressure-equipment registration jurisdiction not cited | heading 33 lists REG-022 without jurisdiction | Provincial regulator (jurisdiction TBD) | Specification Standards table; REQ-10 | PROPOSAL: confirm jurisdiction from project location (3-25 West Doe Compressor Station, Table 130) | TBD |
| C-07 | Fire/building code not cited | heading 33 lists REG-021 without code reference | Provincial fire/building code (TBD) | Specification Standards table; REQ-10 | PROPOSAL: confirm code from project location | TBD |
| C-08 | Objective-to-deliverable mapping is package-grouped | OBJECTIVE_DELIVERABLE_MAP / OBJECTIVE_SCOPE_MAP show OBJ-002..OBJ-010 against PKG-080 | No deliverable-level explicit objective mapping | _CONTEXT.md Supports Objectives | ASSUMPTION (package-heuristic) per skill default | TBD (confirm) |
