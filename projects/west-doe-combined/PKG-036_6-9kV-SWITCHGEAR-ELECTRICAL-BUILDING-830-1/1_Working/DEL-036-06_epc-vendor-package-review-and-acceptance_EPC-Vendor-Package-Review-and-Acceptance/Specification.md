# Specification — DEL-036-06 EPC Vendor Package Review and Acceptance

## Scope

### In scope

- EPC Integrator review of vendor package documentation, integration interfaces, test/inspection evidence, and turnover records for the PKG-036 6.9 kV Switchgear Electrical Building (830-1) package.
- Acceptance decision and evidence set against the three EPC anchor deliverables for PKG-036: DEL-036-01 Scope of Work, DEL-036-02 Package Datasheet, and DEL-036-03 Construction Work Package.
- Production of: vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence (DELIVERABLE_REGISTER.csv row DEL-036-06).

### Out of scope

- Vendor engineering, design, fabrication, supply, and the physical equipment package itself (these are the responsibility of DEL-036-04, Package Vendor).
- Vendor document register authorship and submittal management (DEL-036-05).
- Authorship of the EPC Scope of Work, Package Datasheet, and Construction Work Package (DEL-036-01, -02, -03).
- Authoring source standards (ELC-QAS-* documents).

## Requirements

| ReqID | Requirement | Source / Basis |
|---|---|---|
| REQ-036-06-001 | The review and acceptance evidence set shall include: vendor document review log, package acceptance checklist, test/inspection evidence, and turnover evidence. | DELIVERABLE_REGISTER.csv row DEL-036-06 (Anticipated artifacts) |
| REQ-036-06-002 | Vendor documents shall be reviewed for compliance with the EPC Scope of Work (DEL-036-01), Package Datasheet (DEL-036-02), and Construction Work Package (DEL-036-03). | DELIVERABLE_REGISTER.csv row DEL-036-06 (Description) |
| REQ-036-06-003 | Electrical equipment supplied with the package shall be third-party certified by CSA, ULc, FM, ETL, or another Nationally Recognized Testing Laboratory acceptable for the application; certification evidence shall be captured in the review log. | DBM-Deepcut/4-25_Deepcut_DBM.md (Governing Codes section, paragraph on third-party certification) |
| REQ-036-06-004 | Vendor package design, fabrication, installation, testing, and inspection shall comply with CSA C22.1-21 Canadian Electrical Code, applicable BC provincial and local electrical codes, and ELC-QAS-000003-001 "Electrical Requirements for Packaged Equipment" Rev 2; medium-voltage switchgear shall additionally comply with ELC-QAS-000007-001 "Medium Voltage Switchgear" Rev 1. Compliance evidence shall be captured. | DBM-Deepcut/4-25_Deepcut_DBM.md (Governing Codes; Table 12-1) |
| REQ-036-06-005 | The acceptance checklist shall verify integration interfaces declared at the package level (Utility Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports). | PACKAGE_REGISTER.csv row PKG-036 (Interface types) |
| REQ-036-06-006 | Acceptance shall confirm that grounding interface meets the project basis: 6.9 kV transformer feeding the package grounded via a 100 A, 10 s neutral grounding resistor operating as a tripping system; building grounded to the plant grid at two points with ground wells. | DBM-Deepcut/4-25_Deepcut_DBM.md (Grounding and Bonding section) |
| REQ-036-06-007 | Acceptance shall confirm building services compliance: prefabricated modular building in a general-purpose area, n+1 HVAC, bottom cable entry on elevated piles, TECK/ACIC cable wiring, equipment doors sized to remove the largest equipment. | DBM-Deepcut/4-25_Deepcut_DBM.md (Electrical Buildings section) |
| REQ-036-06-008 | Test and inspection evidence shall include factory/shop test records appropriate to the supplied equipment classes (e.g., medium-voltage switchgear factory acceptance tests). Detailed FAT acceptance criteria are TBD pending access to ELC-QAS-000003-001 and ELC-QAS-000007-001 source slices. | ARTIFACT_REGISTER.csv ART-2E1BDD099B; location TBD |
| REQ-036-06-009 | Turnover evidence shall enable handoff into the EPC Construction Work Package (DEL-036-03) and downstream facility integration; specific turnover document list is TBD pending project turnover specification. | DELIVERABLE_REGISTER.csv row DEL-036-06; location TBD |
| REQ-036-06-010 | All review/acceptance items shall record source provenance (vendor document ID and revision; project SOW/Datasheet/CWP reference) sufficient for audit. | ASSUMPTION (derived from anticipated-artifact list "Vendor document review log" + DBM third-party certification requirement) |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| CSA C22.1-21 Canadian Electrical Code | General applicability to project electrical equipment and installation | DBM-Deepcut/4-25_Deepcut_DBM.md (Governing Codes) |
| ELC-QAS-000003-001 Electrical Requirements for Packaged Equipment, Rev 2 | Direct: governs vendor packaged-equipment electrical requirements | DBM-Deepcut/4-25_Deepcut_DBM.md Table 12-1; clause-level text — location TBD |
| ELC-QAS-000007-001 Medium Voltage Switchgear, Rev 1 | Direct: governs medium-voltage switchgear supplied with the package | DBM-Deepcut/4-25_Deepcut_DBM.md Table 12-1; clause-level text — location TBD |
| ELC-QAS-000015-001 Instrumentation for Packaged Equipment, Rev 1 | Direct: governs instrumentation supplied with the package | DBM-Deepcut/4-25_Deepcut_DBM.md Table 12-1; clause-level text — location TBD |
| Applicable BC provincial/local electrical codes; Technical Safety BC; BCER | General applicability | DBM-Deepcut/4-25_Deepcut_DBM.md (Governing Codes) |
| CSA, API, IEEE, ISA, NEMA, WorkSafeBC | General applicability per discipline-relevant clauses | DBM-Deepcut/4-25_Deepcut_DBM.md (Governing Codes) |

## Verification

| ReqID | Verification approach |
|---|---|
| REQ-036-06-001 | Inventory check: each required artifact type present in the deliverable's evidence folder. |
| REQ-036-06-002 | Trace each vendor document to a clause/section in DEL-036-01, DEL-036-02, or DEL-036-03; record exceptions. |
| REQ-036-06-003 | Inspection of certification marks/certificates on equipment data sheets and nameplate photos; recorded in review log. |
| REQ-036-06-004 | Cross-reference vendor specification compliance against CSA C22.1-21 and ELC-QAS-000003-001 / -000007-001 clause table; record gaps as comments. |
| REQ-036-06-005 | Interface-by-interface acceptance checklist signed by EPC Integrator with vendor evidence per interface. |
| REQ-036-06-006 | Review of vendor grounding drawings and connection points; field walk-down for two-point ground connections. |
| REQ-036-06-007 | Review of vendor building drawings, HVAC sizing report, cable-entry details, and equipment-door schedule against DBM Electrical Buildings clauses. |
| REQ-036-06-008 | Review of FAT/shop test reports; witness records (if witnessed); non-conformance log closure evidence. |
| REQ-036-06-009 | Turnover checklist closure with construction handover acceptance signature. |
| REQ-036-06-010 | Audit sample of review-log entries for source provenance fields. |

## Documentation

Required artifacts:

- Vendor document review log (ART-FB61C5F7B1)
- Package acceptance and turnover checklist (ART-8F50EF826E)
- Factory/shop test and inspection evidence (ART-2E1BDD099B)
- Turnover evidence package (composition TBD)
