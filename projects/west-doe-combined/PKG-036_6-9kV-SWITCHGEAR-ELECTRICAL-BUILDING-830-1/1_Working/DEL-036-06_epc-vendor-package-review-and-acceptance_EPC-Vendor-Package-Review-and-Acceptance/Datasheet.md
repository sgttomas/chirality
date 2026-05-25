# Datasheet — DEL-036-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-036-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-036` |
| Package Name (workbook) | 6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1) |
| Workbook Row | Packages row 38 |
| Discipline | Electrical |
| Type | EPC Vendor Package Acceptance |
| Responsible Party | EPC Integrator (lead); Package Vendor (input) |
| Scope Item | `SOW-0037` |
| Supports Objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable role | EPC Integrator review and acceptance of vendor package against EPC Scope of Work, Package Datasheet, and Construction Work Package | DELIVERABLE_REGISTER.csv row DEL-036-06 |
| Anticipated artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | DELIVERABLE_REGISTER.csv row DEL-036-06; ARTIFACT_REGISTER.csv (ART-FB61C5F7B1, ART-8F50EF826E, ART-2E1BDD099B) |
| Coordination mode | DECLARED (no declared upstream/downstream edges as of PREPARATION) | `_DEPENDENCIES.md` |
| Upstream EPC inputs (peer deliverables in PKG-036) | DEL-036-01 Scope of Work; DEL-036-02 Package Datasheet; DEL-036-03 Construction Work Package | DELIVERABLE_REGISTER.csv (peer rows) |
| Vendor counterpart deliverables (peer in PKG-036) | DEL-036-04 Vendor Engineered Equipment Package; DEL-036-05 Vendor Document Turnover Package | DELIVERABLE_REGISTER.csv (peer rows) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Package classification (workbook) | 6.9 kV medium-voltage switchgear electrical building, building tag 830-1 | PACKAGE_REGISTER.csv row PKG-036 |
| Building-tag classification (DBM) | 830-1 listed as "4.16 kV Acid Gas/Overheads Compressor Electrical Building" | DBM-Deepcut/4-25_Deepcut_DBM.md line 2813 (CONFLICT — see Guidance) |
| Distribution role for 6.9 kV (DBM) | 6.9 kV used as a medium-voltage service for AC inverter-drive motors rated 5,500 hp and above; fed from 13.8 kV via step-down transformer | DBM-Deepcut/4-25_Deepcut_DBM.md lines 2917-2935 |
| Area classification | Electrical buildings located in general-purpose areas | DBM-Deepcut/4-25_Deepcut_DBM.md line 2911 |
| Standby/UPS interfaces inside electrical buildings | 120 V AC UPS and 125 V DC UPS systems housed in electrical buildings | DBM-Deepcut/4-25_Deepcut_DBM.md line 2973 |
| Vendor certification | Electrical equipment to be third-party certified by CSA, ULc, FM, ETL, or another NRTL acceptable for the application | DBM-Deepcut/4-25_Deepcut_DBM.md (Governing Codes section) |

## Construction (review evidence set)

| Item | Value | Source |
|---|---|---|
| Review object 1 | Vendor document submittals against the vendor document register (DEL-036-05) | ARTIFACT_REGISTER.csv ART-FB61C5F7B1 |
| Review object 2 | Vendor engineered equipment package (DEL-036-04) against EPC Scope of Work and Package Datasheet | DELIVERABLE_REGISTER.csv peer rows; SCOPE_LEDGER.csv SOW-0037 |
| Review object 3 | Factory/shop test and inspection evidence | ARTIFACT_REGISTER.csv ART-2E1BDD099B |
| Acceptance evidence | Vendor package acceptance and turnover checklist | ARTIFACT_REGISTER.csv ART-8F50EF826E |
| Quality standards referenced | ELC-QAS-000003-001 Electrical Requirements for Packaged Equipment; ELC-QAS-000007-001 Medium Voltage Switchgear; ELC-QAS-000015-001 Instrumentation for Packaged Equipment | DBM-Deepcut/4-25_Deepcut_DBM.md Table 12-1 |
| Code basis | CSA C22.1-21 Canadian Electrical Code; applicable BC provincial/local codes; CSA, API, IEEE, ISA, NEMA, WorkSafeBC, Technical Safety BC, BCER | DBM-Deepcut/4-25_Deepcut_DBM.md (Governing Codes section) |
| Detailed acceptance criteria | TBD — deliverable-specific acceptance criteria are not stated in accessible sources; to be established from ELC-QAS-000003-001 and ELC-QAS-000007-001 when source slices become accessible | location TBD |

## References

- `_REFERENCES.md`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row DEL-036-06)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (row PKG-036)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv` (rows ART-FB61C5F7B1, ART-8F50EF826E, ART-2E1BDD099B)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv` (row SOW-0037)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Governing Codes; Electrical Buildings; Power System; Building Tags table)
- `_Sources/26020-Package_Requirements.docx` (location TBD — referenced but slice not extracted)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` (location TBD — referenced but slice not extracted)
