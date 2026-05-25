# Procedure: DEL-015-05_vendor-document-turnover-package

## Purpose

Steps to **produce** the Vendor Document Turnover Package deliverable for PKG-015 (Transformer TXP-8300-1, 12/15 MVA step-down distribution transformer): assemble the vendor document register, route submittals through EPC Integrator review, and compile turnover records for closeout.

## Prerequisites

**Declared upstream dependencies (from `_DEPENDENCIES.md`):** none declared during PREPARATION.

**Required reference materials:**

- `_CONTEXT.md` — deliverable identity, scope, anticipated artifacts.
- `_REFERENCES.md` — Gate 7 source pointers and shared source root.
- `Datasheet.md`, `Specification.md`, `Guidance.md` — deliverable-local production documents.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` and `PACKAGE_REGISTER.csv` — row `DEL-015-05` and row `PKG-015`.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — incoming-power/transformer context and the package-deliverables sentence.
- `_Sources/26020-Package_Requirements.docx` — recurring "Core vendor documents" block (PRQ-009 / DOC-008 / QLT-006).
- Vendor package data for TXP-8300-1 (provided by the Package Vendor; not part of the current source set).

**Required participants:**

- Package Vendor (vendor documentation lead).
- EPC Integrator (interface/integration reviewer).

## Steps

1. **Confirm scope and identity.** Verify deliverable identity against `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` row `DEL-015-05`. Confirm parent package (`PKG-015`), equipment tag (TXP-8300-1), and the seven applicable interface types in `PACKAGE_REGISTER.csv` row `PKG-015`.
2. **Establish the document-control framework.** Adopt the project "Core vendor documents" block (PRQ-009 Vendor Document Index, DOC-008 Vendor Document Control Procedure, QLT-006 Supplier Quality) as the baseline. Mark any PKG-015–specific package-requirements text as `location TBD` until located. (See Specification R-02, R-07.)
3. **Initialize the vendor document register.** Create the register with at minimum the following columns: register row ID; document title; document type (datasheet, drawing, test report, certification, manual, etc.); source-row pointer (DBM section, package-requirements row, standard clause, or "derived from deliverable type convention"); interface-type tag(s); submittal status; review status; turnover status; provenance notes.
4. **Populate from source materials.** Enumerate register rows from every accessible source row that requires a vendor document for PKG-015: DBM rows that imply documentation (notably the "Incoming Power and Transformers" feeder context — see Guidance Considerations and HRR-015-05-001), the project package-requirements core block, and any standards rows once accepted. Cite source rows in the source-row pointer column.
5. **Populate from deliverable-type convention.** Add register rows for vendor document types typical of a 12/15 MVA, 13.8 kV / 4160/2400 V step-down distribution transformer (e.g., FAT reports, type tests, dielectric/impulse, turns-ratio, insulation resistance, oil quality if applicable, nameplate, as-built drawings, O&M manuals, spare parts list, warranty documentation). Tag these as "derived from deliverable type convention" and mark detail TBD until vendor data confirms (HRR-015-05-004).
6. **Tag interfaces.** For each register row, tag the applicable interface types from the PKG-015 set (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports). Ensure each interface type appears in at least one row. (Specification R-06.)
7. **Submit vendor documents.** Package Vendor executes submittal transmittals per DOC-008 (when accessible) or the equivalent vendor-document control procedure in effect. Each submittal updates the corresponding register row's submittal status.
8. **EPC integrator review.** EPC Integrator reviews each submittal for interface/integration impact across the seven interface types. Review focuses on cross-package interface integrity rather than internal transformer design. Reviews update the register row's review status.
9. **Compile turnover records.** Assemble turnover records (submittals, test reports, certifications, as-built drawings, warranty documentation, and other artifacts indicated by source materials and applicable standards). Update each register row's turnover status. (Specification R-04.)
10. **Final integrity check.** Confirm: (a) every applicable interface type has at least one register row (R-06); (b) every source-driven row carries a source-row pointer (R-03); (c) every convention-derived row is labeled as such; (d) the core block PRQ-009 / DOC-008 / QLT-006 is represented (R-02, R-07); (e) no individual source vendor document row has been promoted to a separately decomposed deliverable (R-09).
11. **Hand off to acceptance.** Provide the completed register and turnover records to `DEL-015-06_epc-vendor-package-review-and-acceptance` as inputs to package acceptance closeout.

## Verification

| Check | Method | Evidence |
|---|---|---|
| Register exists and is PKG-015–scoped | Inspection | `Vendor_Document_Register` artifact (path TBD when produced) |
| Source-row pointers present where applicable | Inspection | Register column "source-row pointer" populated |
| Interface coverage complete | Cross-check against `PACKAGE_REGISTER.csv` row `PKG-015` | Each applicable interface type tagged at least once |
| Core block applied | Inspection | Register includes PRQ-009 / DOC-008 / QLT-006 rows |
| Submittal and review status closed for all required rows | Audit prior to handoff | Register status columns |
| Turnover records complete | Audit prior to handoff | Turnover records artifact set |
| No row promoted to separate deliverable | Decomposition cross-check | `DELIVERABLE_REGISTER.csv` does not contain a deliverable for any individual source vendor document row of PKG-015 |

## Records

Records produced and retained:

- Vendor document register (master register artifact).
- Vendor document submittal transmittals.
- EPC Integrator review records.
- Turnover record set (submittals, FAT/type/dielectric/insulation/turns-ratio test reports, oil quality reports if applicable, nameplate documentation, as-built drawings, O&M manuals, spare parts list, warranty documentation, certifications) — specific list TBD pending vendor data (HRR-015-05-004).
- Source-row pointer table linking register rows back to source rows in the DBM, package requirements, and standards.
- Handoff package to `DEL-015-06_epc-vendor-package-review-and-acceptance`.
