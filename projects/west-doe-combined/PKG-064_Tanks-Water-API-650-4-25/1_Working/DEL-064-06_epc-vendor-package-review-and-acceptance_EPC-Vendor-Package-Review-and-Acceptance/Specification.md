# Specification — EPC Vendor Package Review and Acceptance (DEL-064-06)

## Scope

This specification governs the EPC Integrator's review and acceptance of the Tanks, Water (PKG-064; tag `26020-01-PT-19-002`) vendor package. It covers:

- Review and acceptance of the vendor's engineering deliverables enumerated in `Datasheet.md` (Acceptance Inventory).
- Verification of vendor scope against the EPC Scope of Work (DEL-064-01), Package Datasheet (DEL-064-02), and Construction Work Package (DEL-064-03).
- Acceptance evidence assembly for vendor document turnover (DEL-064-05) and integration into the constructed facility.
- Confirmation that the applicable physical interfaces (per Datasheet "Interfaces Subject to Review") have been engineered, documented, and signed off.

Out of scope:
- Vendor engineering, design, fabrication, and supply themselves (those are DEL-064-04).
- Site civil/foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase, etc., which are explicitly identified as "By others" in the source [SRC1 Scope Notes / Open Items].
- Modifications to source basis or to the vendor's design basis. Discrepancies are routed back to the responsible party for ruling, not corrected here.

## Requirements

R-1. Review-and-acceptance evidence SHALL be assembled against every vendor deliverable listed in the `Datasheet.md` Acceptance Inventory. [Source: SRC1 "Vendor Engineering Deliverables"]

R-2. Each accepted vendor deliverable SHALL show traceability to (a) the EPC Scope of Work (DEL-064-01), (b) the Package Datasheet (DEL-064-02), and (c) the applicable source row in `_Sources/26020-Package_Requirements.docx` heading 19. [ASSUMPTION: traceability convention inferred from EPC Integrator role and Gate 5 anchor framing in DELIVERABLE_REGISTER notes; not an explicit source clause.]

R-3. The package SHALL be evaluated against the source design conditions captured in `Datasheet.md` Attributes: design pressure 32 oz / 1.0 oz vacuum, design temperature -40 deg C to 60 deg C, atmospheric operating pressure, external insulation with heating, and LP fuel gas blanket. Deviations SHALL be documented and routed for human ruling. [Source: SRC1 "Major Included Equipment", "Scope Notes / Open Items"]

R-4. Tank design and fabrication SHALL be verified against modified API 650 as cited in source. [Source: SRC1 "Major Included Equipment"; "API 650 (modified)"] Acceptance shall not waive the modification points; modification points are TBD pending vendor design basis (MEC-001).

R-5. Storage capacity SHALL be verified as Item No. 1: Two (2) 2,000 bbl Process Water Storage Tanks in sweet produced water / process water service. [Source: SRC1 "Basic Scope", "Major Included Equipment"]

R-6. Each applicable interface marked "Yes" in `Datasheet.md` "Interfaces Subject to Review" SHALL have at least one corresponding accepted vendor deliverable from the relevant deliverable group (e.g., Process Piping interface -> PRO-008, PIP-003, PIP-004; Cathodic Protection -> PLN-015, PLN-016; etc.). [Source: SRC1 "Physical Interface Summary" cross-referenced with "Vendor Engineering Deliverables"]

R-7. Interfaces marked "No" in source SHALL NOT be accepted as vendor-in-scope without an explicit human ruling that overrides the source. [Source: SRC1 "Physical Interface Summary"]

R-8. Vendor Document Turnover Package (DEL-064-05) artifacts SHALL be cross-referenced for completeness against the Acceptance Inventory before issuing package acceptance. [ASSUMPTION: based on the package structure where DEL-064-05 owns the turnover record and DEL-064-06 is the acceptance gate.]

R-9. Test and inspection evidence SHALL include, at minimum: ITP (QLT-003) acceptance, Material Test Reports / Certificates (QLT-013), Inspection Release Certificate (QLT-020), and Equipment FAT / Performance Test Report (MEC-022). [Source: SRC1 "Vendor Engineering Deliverables"]

R-10. Open items present in the source (notably "Other throughputs: TBD", "Operating temperature: TBD for Item No. 1", and "Interface Coordination Notes: TBD") SHALL be either resolved with evidence prior to acceptance or recorded as accepted-with-deviation entries with human ruling. [Source: SRC1 "Scope Notes / Open Items", "Interface Coordination Notes"]

R-11. The acceptance record SHALL preserve a stable audit chain: vendor submittal ID -> review disposition (accept / accept-with-comment / reject) -> reviewer -> date -> superseding submittal (if any). [ASSUMPTION: standard vendor-document-review convention; not explicit in source.]

R-12. No item on the "By others" exclusion list SHALL be accepted as vendor-supplied scope: foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase, etc. [Source: SRC1 "Scope Notes / Open Items"]

## Standards

| Standard | Applicability | Location |
|---|---|---|
| API 650 (modified) | Atmospheric storage tank design and fabrication | Cited in SRC1 "Major Included Equipment"; full standard text location TBD (not locally accessible) |
| Modification points to API 650 | Define delta between API 650 and as-built package | location TBD; expected in vendor Mechanical Design Basis (MEC-001) |

Other standards typically governing the deliverable groups in the Acceptance Inventory (e.g., welding, NDE, painting/coating, PSV sizing, structural design, instrumentation loop checking) are not enumerated in the source slice and are TBD until cited in vendor deliverables MEC-001, STR-001, PRO-014, ELE-012, PLN-015, INS-002, or CTL-003.

## Verification

| Requirement | Verification Method | Verification Artifact |
|---|---|---|
| R-1 | Inventory cross-check against `Datasheet.md` Acceptance Inventory | Vendor document review log |
| R-2 | Traceability matrix mapping each accepted item to SOW/Datasheet/source row | Vendor document review log; package acceptance checklist |
| R-3 | Review of vendor MEC-001 Mechanical Design Basis and MEC-014 Mechanical Calculation Package against `Datasheet.md` Attributes | Package acceptance checklist |
| R-4 | Review of MEC-001, MEC-005, MEC-011, MEC-014 for modified API 650 conformance and modification points | Package acceptance checklist |
| R-5 | Review of MEC-002 (Mechanical Equipment List) and MEC-011 (Storage Tank Data Sheets) | Package acceptance checklist |
| R-6 | Interface-to-deliverable matrix completeness check | Package acceptance checklist |
| R-7 | Inspection of any accepted deliverable claiming a "No" interface | Vendor document review log |
| R-8 | Cross-reference DEL-064-05 turnover register to Acceptance Inventory | Turnover evidence pack |
| R-9 | Witness/review of QLT-003 ITP execution, QLT-013, QLT-020, MEC-022 | Test/inspection evidence |
| R-10 | TBD-closure log against source "Open Items" list | Vendor document review log; package acceptance checklist |
| R-11 | Audit of review log entries | Vendor document review log |
| R-12 | Scope-exclusion check during acceptance walkthrough | Package acceptance checklist |

## Documentation

The deliverable produces these artifacts (per `_CONTEXT.md` Anticipated Artifacts):

- Vendor document review log — disposition record for every item in the Acceptance Inventory.
- Package acceptance checklist — per-requirement (R-1 through R-12) pass/fail/deviation record.
- Test/inspection evidence — references to QLT-003, QLT-013, QLT-020, MEC-021, MEC-022, PIP-024.
- Turnover evidence — handoff record to operations; cross-link to DEL-064-05 turnover package.

## Source Key

- SRC1 = `_Sources/26020-Package_Requirements.docx`, heading 19 ("26020-01-PT-19-002 - Tanks, Water"). Sections cited inline.
