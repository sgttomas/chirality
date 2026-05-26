# Guidance — DEL-048-05 Vendor Document Turnover Package

## Purpose

The Vendor Document Turnover Package is the single Package-Vendor deliverable that consolidates the vendor document register, all required vendor submittals, and the turnover records for `PKG-048 Inlet / Sales Compressors`. It exists so that the EPC Integrator can review and accept the vendor package against the EPC Scope of Work, Package Datasheet, and Construction Work Package, and so the Owner ultimately receives a complete, controlled record of the equipment package as built and tested.

Source authority: `26020-Package_Requirements.docx` heading 3 vendor engineering deliverables table (`location TBD`); `_CONTEXT.md` (responsibility and scope); `DELIVERABLE_REGISTER.csv` (deliverable identity and downstream consumer).

## Principles

1. **The source vendor deliverables table is the document-scope authority.**
   The heading 3 table is what the vendor must produce for PKG-048. The turnover package does not add documents that the source does not require, and does not omit documents the source requires. Additions or omissions must be reconciled against the EPC Scope of Work and Package Datasheet, and recorded as scope changes. The expected framework in `Datasheet.md` is a working baseline pending direct extraction of heading 3.

2. **The Vendor Document Index (PRQ-009) is the operational backbone.**
   Every other document in the package is enumerated, revisioned, transmitted, and reviewed through the index. The index is updated continuously, not just at turnover. For PKG-048, the index must also disambiguate inlet-duty vs sales-duty unit documents.

3. **The Vendor Document Control Procedure (DOC-008) is the rule book.**
   Numbering, revision states, transmittal mechanics, hold/code/review codes, and acceptance flow all live in DOC-008. When DOC-008 contradicts informal practice, DOC-008 wins. DOC-008 is not yet locally accessible — see Conflict Table.

4. **Turnover is staged, not a single event.**
   The vendor data books (PRQ-016 / MEC-023) are the final, consolidated artifact, but FAT/SAT, material certs, as-builts, and regulatory packages are issued at their natural points in the schedule. The turnover package is the running compilation, not only the final book.

5. **Source-required documents stay first-class; they are artifacts of this deliverable, not standalone deliverables.**
   Per `_CONTEXT.md` Notes, individual source document rows are evidence under this deliverable, not separate decomposition deliverables. The decomposition deliberately keeps them aggregated here.

6. **Interface to acceptance lives in DEL-048-06.**
   Vendor turnover (this deliverable) provides the controlled record. The acceptance ruling lives in `DEL-048-06_epc-vendor-package-review-and-acceptance`. Do not co-mingle.

## Considerations

- **Combined inlet/sales scope.** The package is "Inlet / Sales Compressors", not inlet-only. Expect at minimum two duty classes (inlet compression and sales compression) with potentially different stage counts, suction/discharge pressures, and materials selection. The Vendor Document Index must preserve duty distinctions per unit.

- **Document granularity vs. package granularity.** Source vendor deliverables tables for compressor packages tend to be granular (e.g., separate IDs for Foundation Drawings and Anchor Bolt Drawings). Vendors may issue these as a single transmittal or as separate documents. PRQ-009 must preserve source-level granularity in its rows even if a single vendor PDF satisfies multiple rows.

- **NACE compliance evidence is non-trivial.** The plant is sour-service per `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`. Material Test Reports (QLT-013) need explicit NACE-compliance flags per item, not just generic certs. Confirm heading 3 NACE callout when extracted.

- **Budgetary references are not contract.** Any budgetary go-by PDFs referenced in source tables are pricing/delivery references only and not the document control basis for turnover.

- **Interfaces workbook naming.** Source heading text may cite an older revision of the interfaces workbook; the locally accessible file is `_Sources/26020-Packages_Interfaces_4_export.xlsx`. Treat any older-revision citation as superseded unless a human ruling says otherwise (see Conflict Table).

- **Heading 3 not yet text-extracted.** Substantive document-set enumeration in `Datasheet.md` and corresponding requirements in `Specification.md` follow a framework derived from the parallel sibling deliverable (PKG-080 heading 33). Re-verification against the heading 3 source slice is required before publication.

## Trade-offs

- **Comprehensive index vs. transmittal burden.** A finer-grained index (one row per source ID) increases administrative load but makes acceptance verification straightforward. Coarser index shifts burden to verification time. Preferred posture: fine-grained index, coarse transmittals — index resolves the mapping.

- **Stage-by-stage submittal vs. final-book-only.** Issuing only the final vendor data books reduces EPC review cycles but produces a one-shot review surge at turnover. Stage-by-stage submittal smooths review load and surfaces defects early; preferred where DOC-008 permits.

- **Native vendor numbering vs. project numbering.** Native numbering preserves vendor configuration management; project numbering eases EPC consumption. PRQ-009 should carry both columns to avoid the trade-off entirely.

- **Unit-duty rollup vs. unit-specific rows.** Rolling up inlet and sales documents under combined "compressor package" rows reduces row count but obscures per-unit verifiability. Recommend per-duty rows with a shared "package design basis" subset.

## Examples

- For a combined inlet/sales compressor package with (assumed) two duty classes, PRQ-009 should carry duty-specific rows for `MEC-008 Compressor Data Sheets`, `MEC-022 Equipment FAT / Performance Test Report`, and `ELE-011 Motor Starting Study`, while sharing rows for `MEC-001 Mechanical Design Basis` and `STR-001 Structural Design Basis`.

- A Material Test Report (QLT-013) for a sour-service compressor cylinder is included in the turnover package with a NACE compliance flag and a link to the relevant Mechanical Equipment Data Sheet (MEC-003) entry.

- The Equipment FAT Performance Test Report (MEC-022) is issued as soon as FAT is complete; the executed copy is then bound into the Mechanical Final Documentation (MEC-023) at turnover.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-01 | Heading 3 source slice not text-extracted; Datasheet/Specification document-set framework derived from sibling PKG-080 heading 33 pattern | `26020-Package_Requirements.docx` heading 3 (binary, not extracted) | Sibling pattern (PKG-080 heading 33) | Datasheet enumerated tables; Specification REQ-01..REQ-12 | PROPOSAL: extract heading 3 to markdown and re-verify enumerated set; remove/add rows as needed and convert `[ASSUMPTION]` REQ-11/REQ-12 to `[SRC]` where heading 3 supports | TBD |
| C-02 | Submittal revision stages not stated in source slice | heading 3 (not extracted; assumed silent) | Industry convention (Bid/IFR/IFA/IFC/As-Built) | Specification REQ-13; Datasheet Conditions | PROPOSAL: adopt Bid/IFR/IFA/IFC/As-Built pending DOC-008 issuance | TBD |
| C-03 | Transmittal medium not stated | heading 3 (silent assumed) | Project document-control standard (not locally accessible) | Specification REQ-15; Datasheet Conditions | PROPOSAL: confirm against issued DOC-008 | TBD |
| C-04 | Review turnaround not stated | heading 3 (silent assumed) | Project document-control standard | Specification REQ-14 | PROPOSAL: confirm against project doc-control matrix | TBD |
| C-05 | Interfaces filename revision | Source likely cites `26020-Packages_Interfaces.3.xlsx` (sibling pattern) | Local file is `26020-Packages_Interfaces_4_export.xlsx` | Datasheet References; Guidance Considerations | PROPOSAL: use the `_4_export` file as the latest revision unless overruled | TBD |
| C-06 | NACE document not cited at clause level | heading 3 (callout details `location TBD`) | NACE MR0175 / ISO 15156 (ASSUMPTION) | Specification REQ-12, Standards table; Datasheet Attributes | PROPOSAL: adopt NACE MR0175 / ISO 15156 as the controlling reference; confirm with project metallurgy | TBD |
| C-07 | Pressure-equipment registration jurisdiction not cited | heading 3 lists REG-022 without jurisdiction (assumed) | Provincial regulator (jurisdiction TBD; BC/AB likely given Doe field) | Specification Standards table; REQ-10 | PROPOSAL: confirm jurisdiction from project location (3-25 / 03-25 West Doe Compressor Station) | TBD |
| C-08 | Fire/building code not cited | heading 3 lists REG-021 without code reference (assumed) | Provincial fire/building code (TBD) | Specification Standards table; REQ-10 | PROPOSAL: confirm code from project location | TBD |
| C-09 | Objective-to-deliverable mapping is package-grouped | `_CONTEXT.md` Supports Objectives lists OBJ-001, OBJ-003..OBJ-010 at PKG-048 level | No deliverable-level explicit objective mapping | `_CONTEXT.md`; Datasheet Identification | ASSUMPTION (PACKAGE_HEURISTIC) per skill default | TBD (confirm) |
| C-10 | Combined inlet/sales scope; per-duty unit count unknown | `_CONTEXT.md` PackageName "Inlet / Sales Compressors" | heading 3 (not extracted) | Datasheet Attributes; Specification REQ-18 | PROPOSAL: confirm number of inlet-duty vs sales-duty units in heading 3; reflect in PRQ-009 unit attribute | TBD |
