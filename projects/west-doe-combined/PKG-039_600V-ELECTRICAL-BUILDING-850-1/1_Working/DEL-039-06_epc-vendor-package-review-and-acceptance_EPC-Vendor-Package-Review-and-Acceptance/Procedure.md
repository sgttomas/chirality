# Procedure: DEL-039-06_epc-vendor-package-review-and-acceptance

## Purpose

Define the working procedure for producing EPC Vendor Package Review and Acceptance evidence for `PKG-039 -- 600V ELECTRICAL BUILDING (850-1)`.

This procedure produces or supports the vendor document review log, package acceptance checklist, factory/shop test and inspection evidence record, and turnover evidence record. It does not create binding acceptance; binding acceptance requires authorized human EPC Integrator review and sign-off.

## Prerequisites

- EPC Scope of Work (`DEL-039-01`) for `PKG-039`.
- EPC Package Datasheet (`DEL-039-02`) for `PKG-039`, including interface requirements matrix.
- EPC Construction Work Package (`DEL-039-03`) for `PKG-039`.
- Vendor Engineered Equipment Package (`DEL-039-04`), including vendor design basis, datasheets, drawings, and physical equipment package evidence.
- Vendor Document Turnover Package (`DEL-039-05`), including vendor document register, submittals, source-required vendor documentation, and turnover records.
- Gate 7 accepted registers: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM electrical design basis source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Vendor ITP, factory/shop test records, inspection reports, and authority inspection evidence: `TBD` pending vendor submittal.

## Steps

1. Confirm package identity.
   - Verify package ID `PKG-039`, workbook ID 39, workbook row 41, WBS `01`, CoA tracking number `26020-01-30-030`, and package name `600V ELECTRICAL BUILDING (850-1)` against `PACKAGE_REGISTER.csv`.
   - Record any mismatch in the vendor document review log.

2. Establish acceptance basis.
   - List the active EPC anchor documents: `DEL-039-01`, `DEL-039-02`, and `DEL-039-03`.
   - List the vendor package inputs: `DEL-039-04` and `DEL-039-05`.
   - Record unavailable or superseded documents as `TBD` or review-log comments.

3. Build the vendor document review log.
   - Create review-log entries for each vendor submittal or turnover document received.
   - Tie each comment to one or more basis items: EPC anchor document, Gate 7 register row, DBM electrical basis section, interface row, or vendor ITP criterion.
   - Track each comment through vendor response, EPC disposition, closure evidence, and final reviewer status.

4. Build the acceptance checklist.
   - Include package responsibility checks from `PACKAGE_REGISTER.csv` row `PKG-039`.
   - Include artifact checks for `ART-3910447327`, `ART-AA4BFB86C9`, and `ART-0156F0196A`.
   - Include all twelve `PKG-039` interface rows from `INTERFACE_REGISTER.csv`: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports.

5. Review electrical-building source-basis items.
   - Confirm that the vendor package evidence addresses the prefabricated modular electrical building basis.
   - Confirm bottom-entry cable routing and elevated/pile-supported installation where applicable.
   - Confirm HVAC redundancy basis (`n + 1`) where the vendor package includes building HVAC.
   - Confirm grounding/bonding expectations, including two-point grid connection for major electrical equipment and ground-well provision at electrical buildings.
   - Confirm cable/raceway, communications cable, lighting, and maintenance-access requirements where vendor scope includes those systems.

6. Review compliance and inspection evidence.
   - Check vendor evidence against CSA C22.1-21 Canadian Electrical Code, applicable BC provincial and local electrical codes, Tourmaline-designated electrical inspection authority requirements, and applicable CSA/API/IEEE/ISA/NEMA/WorkSafeBC/Technical Safety BC/BCER requirements identified in the DBM source.
   - Mark detailed clause checks `TBD` unless the governing source clause and vendor evidence are locally available.

7. Review factory/shop test and inspection records.
   - Confirm that factory/shop test and inspection evidence exists for the prefabricated, shop-fabricated electrical building.
   - Compare tests, witness points, hold points, and acceptance criteria to the vendor ITP when available.
   - Record missing vendor ITP or test thresholds as `TBD` in the acceptance checklist and review log.

8. Review turnover readiness.
   - Confirm that vendor turnover records are indexed and traceable to the vendor document register.
   - Confirm that open review comments, rejected submittals, missing tests, or missing inspection evidence are either closed or explicitly carried as human-approved exceptions.
   - Record the turnover index or form number as `TBD` if not yet available.

9. Prepare the human acceptance package.
   - Assemble the review log, acceptance checklist, factory/shop test and inspection evidence, and turnover evidence.
   - Highlight unresolved `TBD`, conflict-table entries, and open review comments.
   - Present the package to the authorized EPC Integrator reviewer for approval, rejection, or conditional acceptance.

10. Record final disposition.
   - Update the acceptance checklist only with the authorized human disposition.
   - Do not treat generated draft content as acceptance.
   - Archive the signed checklist, closed review log, and turnover evidence as the acceptance record.

## Verification

| Check | Acceptance criterion | Record |
|---|---|---|
| Package identity | `PKG-039` identity, WBS, CoA, and package name match `PACKAGE_REGISTER.csv`. | Review log / checklist |
| Anchor-document coverage | `DEL-039-01`, `DEL-039-02`, and `DEL-039-03` are identified as acceptance basis. | Checklist |
| Vendor package coverage | `DEL-039-04` and `DEL-039-05` are reviewed or listed as unavailable/`TBD`. | Review log |
| Interface coverage | All twelve `PKG-039` interface rows are represented in checklist review. | Checklist |
| Electrical basis coverage | DBM-supported electrical-building, power, grounding, HVAC, cable/raceway, lighting, maintenance-access, and compliance checks are represented where applicable. | Checklist / evidence index |
| Factory/shop evidence | `ART-0156F0196A` exists or missing evidence is logged with closure owner. | Test/inspection evidence record |
| Comment closure | Each review-log comment has disposition and closure evidence or an authorized exception. | Review log |
| Human authorization | Final acceptance is signed or otherwise dispositioned by the authorized EPC Integrator reviewer. | Acceptance checklist |

## Records

- Vendor document review and comment log (`ART-3910447327`).
- Vendor package acceptance and turnover checklist (`ART-AA4BFB86C9`).
- Factory/shop test and inspection evidence (`ART-0156F0196A`).
- Turnover evidence record / index (`TBD` pending vendor turnover documentation).
- Open-items list or exception list, if any.
- Human acceptance/sign-off record.
