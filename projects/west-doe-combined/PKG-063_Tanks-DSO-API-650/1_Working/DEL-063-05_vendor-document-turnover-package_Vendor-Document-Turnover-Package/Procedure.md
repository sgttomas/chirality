# Procedure — DEL-063-05 Vendor Document Turnover Package

> Operational procedure for assembling, reviewing, and turning over the Vendor Document Turnover Package for PKG-063 Tanks, DSO (API 650).

## Purpose

Provide a repeatable sequence to (a) compile the Package Vendor's documentation set, (b) route it through EPC Integrator interface/integration review, and (c) deliver a turnover record set that closes the documentation requirements of PKG-063.

This procedure governs the package's *production* (vendor assembly) and *use* (EPC review and handover acceptance) — both interpretations are in scope per the four-documents skill rule.

## Prerequisites

| Prerequisite | Source / Owner | Notes |
|---|---|---|
| `DEL-063-01_scope-of-work` available at INITIALIZED or later | EPC Integrator (`DEL-063-01`) | Anchor for submittal alignment (R-03) |
| `DEL-063-02_package-datasheet` available at INITIALIZED or later | EPC Integrator (`DEL-063-02`) | Confirms governing tank code, design conditions, service (resolves Guidance Considerations on DSO and API 650) |
| `DEL-063-04_vendor-engineered-equipment-package` actively progressing | Package Vendor (`DEL-063-04`) | Generates the underlying documents |
| 26020-Package_Requirements.docx heading 18 source slice accessible | Project documentation owner | Resolves R-01/R-02 substance (currently TBD per `_REFERENCES.md`) |
| Workbook Packages row 90 accessible | Project documentation owner | Confirms source register row for PKG-063 |
| Governing tank code text (assumed API 650) accessible for R-08 substantiation | EPC Integrator / vendor | Currently `location TBD` |
| Project document numbering and revision-control convention | Project | Resolves R-09 substance |
| `_DEPENDENCIES.md` declared upstream entries (if any) | EPC Integrator | Currently none declared |

## Steps

| Step | Action | Owner | Output |
|---|---|---|---|
| S-01 | Extract and load the heading-18 required-document list from 26020-Package_Requirements.docx (text slice) into the local reference set | Project doc owner | Heading-18 source slice as accessible text |
| S-02 | Build the vendor document register (R-02) populated with all heading-18 required entries (R-01) plus all SOW/Datasheet-driven submittals (R-03) | Package Vendor | Vendor document register (initial revision) |
| S-03 | For each register entry, plan submittal stages (e.g., IFR / IFC / IFU / As-Built / Final — set TBD per source) and revision-control rules (R-09) | Package Vendor | Register submittal-stage plan |
| S-04 | Issue vendor document submittals per the register and the planned stages; capture transmittals | Package Vendor | Submittal files; transmittal log |
| S-05 | Route submittals to EPC Integrator for interface/integration review (R-06) | Package Vendor → EPC Integrator | EPC review log entries (linked from `DEL-063-06`) |
| S-06 | Incorporate EPC review comments; reissue impacted submittals with revised revision; update register | Package Vendor | Revised submittals; updated register |
| S-07 | Capture source-required vendor document table rows as artifacts where available (R-07) | Package Vendor | Source-row artifact set |
| S-08 | Assemble conformance evidence supporting R-08 (mill certs, weld records, NDE reports, hydrotest records, coatings records — specific set TBD per API 650 and project) | Package Vendor | Conformance evidence index (artifact) |
| S-09 | Assemble turnover records (final transmittal log, EPC acceptance records, final handover document set) per R-05 | Package Vendor with EPC Integrator | Turnover record set |
| S-10 | Produce SOW-coverage matrix mapping SOW-0209..0212 to register entries (R-04) | Package Vendor | SOW coverage matrix |
| S-11 | Produce heading-18 coverage matrix mapping each required item to a register entry (R-01) | Package Vendor | Heading-18 coverage matrix |
| S-12 | Hand the consolidated package to EPC Integrator for final review/acceptance (consumed by `DEL-063-06`) | Package Vendor → EPC Integrator | Turnover package handed over |

Notes:
- Steps S-02/S-03/S-11 cannot be substantively completed until prerequisite "heading-18 source slice accessible" is satisfied. Mark register/coverage entries `TBD` for unresolved items rather than inventing them.
- S-08 specific evidence list is `TBD` until governing tank code clauses are confirmed; do not infer NDE/hydrotest acceptance criteria from generic convention.

## Verification

| Check | Closes | Method |
|---|---|---|
| V-01 | R-01 | Heading-18 coverage matrix shows every required item mapped to a register entry; no `TBD` remaining |
| V-02 | R-02 | Register fields inspected against the field set required by source heading 18 (or, until source is accessible, ASSUMPTION baseline: number, title, type, revision, status, transmittal, stage) |
| V-03 | R-03 | Traceability matrix maps each submittal to one or more SOW (`DEL-063-01`) or Datasheet (`DEL-063-02`) line items |
| V-04 | R-04 | SOW-coverage matrix demonstrates each of SOW-0209..0212 is supported by at least one register entry |
| V-05 | R-05 | Each "for handover" register entry has an associated transmittal record and EPC acceptance record |
| V-06 | R-06 | EPC review log entries exist for every submittal routed for review |
| V-07 | R-07 | Source-row artifact set is inventoried; any "not available" rows are explicitly recorded |
| V-08 | R-08 | Conformance evidence index covers tank code clauses applicable to PKG-063 (specific clause set TBD) |
| V-09 | R-09 | Register entries inspected for unique number, current revision, and date |

## Records

The procedure produces the following records, which together constitute the Vendor Document Turnover Package:

| Record | Originating step(s) | Type |
|---|---|---|
| Vendor document register (current revision) | S-02, S-06 | Master index |
| Vendor document submittals (all revisions) | S-04, S-06 | Submittal files |
| Transmittal log | S-04, S-09 | Log |
| EPC review log (linked from `DEL-063-06`) | S-05 | Log |
| Source-row artifact set | S-07 | Evidence |
| Conformance evidence index | S-08 | Evidence index |
| Turnover record set (final transmittal log + acceptance records + final handover set) | S-09 | Turnover records |
| SOW coverage matrix (SOW-0209..0212) | S-10 | Coverage matrix |
| Heading-18 coverage matrix | S-11 | Coverage matrix |
| Hand-over confirmation | S-12 | Acceptance record (consumed by `DEL-063-06`) |
