# Specification — DEL-072-01 Scope of Work

## Scope

This deliverable is the mandatory EPC Integrator Scope of Work covering the full PKG-072 package scope: tagged equipment, package function, source basis, package boundaries, and the whole-facility integration narrative for the Truck Product Loading Unit 4-25 package (workbook row 99, tracking number 26020-01-23-001). Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 558; PACKAGE_REGISTER.csv row 99.

**In scope (this Scope of Work document):**
- Package identity and tagged equipment list (skid, low-pressure fuel gas heater, low-pressure fuel gas scrubber). Source: SCOPE_LEDGER.csv SOW-0247.
- Package function narrative (skid serves the low-pressure fuel gas system for the West Doe Deep Cut Facility). Source: SCOPE_LEDGER.csv SOW-0246.
- Source basis citations (workbook row 99; 26020-Package_Requirements.docx package heading 26; 4-25_Deepcut_DBM.md). Source: PACKAGE_REGISTER.csv row 99.
- Package boundaries (operating/design conditions, by-others exclusions). Source: SCOPE_LEDGER.csv SOW-0248.
- Whole-facility integration narrative across the applicable interface types listed in PACKAGE_REGISTER.csv row 99.
- Responsibility assignment between Package Vendor and EPC Integrator. Source: PACKAGE_REGISTER.csv row 99 ResponsibilityModel; OBJ-004.

**Out of scope (carried in sibling PKG-072 deliverables, not this document):**
- Package technical datasheet content (handled in DEL-072-02_package-datasheet).
- Construction execution plan and tie-in workface plan (handled in DEL-072-03_construction-work-package).
- Vendor engineering/design/equipment production (handled in DEL-072-04_vendor-engineered-equipment-package).
- Vendor document register and turnover records (handled in DEL-072-05_vendor-document-turnover-package).
- Vendor package review and acceptance evidence (handled in DEL-072-06_epc-vendor-package-review-and-acceptance).

Source: DELIVERABLE_REGISTER.csv rows 558-563.

## Requirements

| ReqID | Requirement | Verification | Source |
|---|---|---|---|
| R-072-01-01 | The Scope of Work shall state package identity using the workbook tracking number `26020-01-23-001` and package name `Truck Product Loading Unit 4-25`. | Inspect document Identification section. | PACKAGE_REGISTER.csv row 99 |
| R-072-01-02 | The Scope of Work shall list the tagged equipment included in the package: skid, fuel gas heater, fuel gas scrubber. | Inspect equipment list. | SCOPE_LEDGER.csv SOW-0247 |
| R-072-01-03 | The Scope of Work shall state the package function as serving the low-pressure fuel gas system for the West Doe Deep Cut Facility. | Inspect function narrative. | SCOPE_LEDGER.csv SOW-0246 |
| R-072-01-04 | The Scope of Work shall cite the source basis: workbook Packages row 99 and `26020-Package_Requirements.docx` package heading 26. | Inspect source-basis citations. | PACKAGE_REGISTER.csv row 99; `_REFERENCES.md` |
| R-072-01-05 | The Scope of Work shall record the package operating and design conditions exactly as carried in SOW-0248 (Design Flow > 8.4 MMSCFD; Operating Pressure 150 psig; Ambient -19 C to 22.2 C; Design Pressure 150 psig; Design Temperature -40 C to 35 C; Final Flow TBD; MAWP TBD). | Inspect Conditions section against SOW-0248. | SCOPE_LEDGER.csv SOW-0248 |
| R-072-01-06 | The Scope of Work shall explicitly identify by-others items (shipping to site, installation, tie-in piping, electrical tie-in) as excluded from the Package Vendor scope. | Inspect Exclusions / By Others section. | SCOPE_LEDGER.csv SOW-0248 |
| R-072-01-07 | The Scope of Work shall list the applicable interface types from PACKAGE_REGISTER.csv row 99 as the integration surface across the facility. | Inspect Interfaces section. | PACKAGE_REGISTER.csv row 99 |
| R-072-01-08 | The Scope of Work shall assign engineering, design, vendor documentation, and physical equipment supply to the Package Vendor, and integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration to the EPC Integrator. | Inspect Responsibility Assignment section. | PACKAGE_REGISTER.csv row 99; OBJ-004 |
| R-072-01-09 | The Scope of Work shall preserve traceability to objectives OBJ-001, OBJ-003 through OBJ-010 as the success conditions the package supports. | Inspect Objectives Traceability section. | DELIVERABLE_REGISTER.csv row 558; OBJECTIVE_REGISTER.csv |
| R-072-01-10 | The Scope of Work shall identify open items and TBD design parameters (Final Flow; MAWP; heater capacity) without inventing values. | Inspect Open Items section. | SCOPE_LEDGER.csv SOW-0247, SOW-0248 |
| R-072-01-11 | ASSUMPTION: Document format and submittal route follow standard EPC project document control practice. | Verify against EPC project document control specification once that specification is locally accessible (location TBD). | Inferred; no source slice presently accessible. |

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| 26020-Package_Requirements.docx (package heading 26) | Authoritative source basis for package scope | `_Sources/26020-Package_Requirements.docx` — relevant slice location TBD (not yet extracted into deliverable folder) |
| 4-25_Deepcut_DBM.md | Facility design basis referenced for SOW-0246 process function and OBJ-001 facility scope | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — relevant slice location TBD |
| Bid Docs/Budgetary/26020-01-PT-RFQ-23-001_FG_Skid_2.docx | Listed as source-basis document for PKG-072 | Referenced by PACKAGE_REGISTER.csv row 99; deliverable-local copy TBD |
| Project codes and standards baseline (CSA, ASME, Provincial regulator) | ASSUMPTION: governing for sour-service mechanical packages per OBJ-009 | location TBD — DBM section SEC-15 referenced by OBJ-009 but not extracted |

## Verification

Each Requirement R-072-01-NN is verified by inspection of the corresponding section of this Scope of Work document and by reconciliation against the cited source (PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, SCOPE_LEDGER.csv, OBJECTIVE_REGISTER.csv rows listed above). Verification ownership rests with the EPC Integrator scope reviewer; final acceptance is recorded in DEL-072-06_epc-vendor-package-review-and-acceptance.

| Requirement | Verification Method | Evidence Location |
|---|---|---|
| R-072-01-01 .. R-072-01-04 | Document inspection vs source row | This deliverable + cited register rows |
| R-072-01-05 | Cross-check Conditions table vs SCOPE_LEDGER SOW-0248 | This deliverable; SCOPE_LEDGER.csv |
| R-072-01-06 | Cross-check Exclusions vs SOW-0248 "By others" clause | This deliverable; SCOPE_LEDGER.csv |
| R-072-01-07 | Cross-check Interfaces list vs PACKAGE_REGISTER row 99 ApplicableInterfaceTypes | This deliverable; PACKAGE_REGISTER.csv |
| R-072-01-08 | Cross-check Responsibility section vs PACKAGE_REGISTER row 99 ResponsibilityModel | This deliverable; PACKAGE_REGISTER.csv |
| R-072-01-09 | Trace objective list against OBJECTIVE_REGISTER rows | This deliverable; OBJECTIVE_REGISTER.csv |
| R-072-01-10 | Open Items section completeness review | This deliverable |
| R-072-01-11 | Review once EPC project document control specification slice is accessible | Source TBD |

## Documentation

Anticipated artifacts produced by this Scope of Work (from `_CONTEXT.md` and DELIVERABLE_REGISTER.csv row 558):

- Package scope of work (this document set)
- Tagged equipment and package identity list (Datasheet.md Identification + Construction sections)
- Package function and integration narrative (Guidance.md; Specification.md Scope)
- Responsibility assignment record (Specification.md Requirements R-072-01-08; Guidance.md)

Downstream consumers per DELIVERABLE_REGISTER.csv rows 559-563:
- DEL-072-02 Package Datasheet (consumes scope and conditions)
- DEL-072-03 Construction Work Package (consumes responsibility split and by-others list)
- DEL-072-04 Vendor Engineered Equipment Package (consumes Package Vendor scope statement)
- DEL-072-05 Vendor Document Turnover Package (consumes documentation expectations)
- DEL-072-06 EPC Vendor Package Review and Acceptance (consumes Requirements as acceptance basis)
