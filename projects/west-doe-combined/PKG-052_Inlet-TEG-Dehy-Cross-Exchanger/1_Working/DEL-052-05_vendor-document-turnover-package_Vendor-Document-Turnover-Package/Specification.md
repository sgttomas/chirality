# Specification — DEL-052-05 Vendor Document Turnover Package (PKG-052)

> Normative. Requirements derive from accessible source slices in the GATE-07 PROJECT_DECOMP snapshot (which extracted `26020-Package_Requirements.docx` heading 7 into the registers). Inferred requirements are labeled `ASSUMPTION`; unsupported items are `TBD`.

## Scope

### In Scope

- The vendor document register and submittal flow for PKG-052 (Inlet / TEG Dehy Cross Exchanger) covering all 9 source categories listed in the Datasheet.
  - Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 340; ARTIFACT_REGISTER.csv DEL-052-05 category rows.
- Vendor document submittals against each source-listed vendor document carried as an artifact row under DEL-052-05.
  - Source: ARTIFACT_REGISTER.csv DEL-052-05 rows.
- Turnover records (Vendor Data Book / Final Supplier Documentation) consolidating accepted submittals at acceptance.
  - Source: ARTIFACT_REGISTER.csv DEL-052-05 (Vendor Data Book / Final Supplier Documentation row); DELIVERABLE_REGISTER.csv row 340 (AnticipatedArtifacts).
- EPC Integrator interface/integration review interaction surface with this deliverable.
  - Source: DELIVERABLE_REGISTER.csv row 340 (ResponsibleParty).

### Out of Scope

- Physical equipment package engineering and design — owned by DEL-052-04 Vendor Engineered Equipment Package.
  - Source: DELIVERABLE_REGISTER.csv row 339.
- EPC review log, acceptance checklist, and acceptance evidence — owned by DEL-052-06 EPC Vendor Package Review and Acceptance.
  - Source: DELIVERABLE_REGISTER.csv row 341.
- Construction installation, tie-ins, and turnover field activities — owned by DEL-052-03 Construction Work Package.
  - Source: DELIVERABLE_REGISTER.csv row 338.
- Promoting any individual source vendor-document row to a standalone deliverable.
  - Source: DELIVERABLE_REGISTER.csv row 340 (Notes).
- Cross-deliverable register aggregation across packages.

## Requirements

### REQ-DEL-052-05-001 — Vendor Document Register Completeness

The Package Vendor SHALL maintain a vendor document register covering every source-listed vendor document carried as an artifact row under DEL-052-05.
- Verification: V-001.
- Source: ARTIFACT_REGISTER.csv DEL-052-05 rows; DELIVERABLE_REGISTER.csv row 340 (AnticipatedArtifacts: "Vendor document register").

### REQ-DEL-052-05-002 — Source-Category Coverage

The register SHALL organize documents under the 9 source categories listed in the Datasheet (Core vendor documents; Core package engineering; Heat transfer equipment; Process package design; Process piping interfaces; Drainage / containment interfaces; Electrical; Instrumentation and controls interfaces; Structural).
- Verification: V-002.
- Source: ARTIFACT_REGISTER.csv DEL-052-05 category rows.

### REQ-DEL-052-05-003 — Authority Anchor

Each register row SHALL identify its source basis (Workbook Packages row 62; `26020-Package_Requirements.docx` heading 7 — Vendor Engineering Deliverables table; or other accepted decomposition source).
- Verification: V-003.
- Source: ARTIFACT_REGISTER.csv DEL-052-05 (Source column).

### REQ-DEL-052-05-004 — Submittal Lifecycle

Each registered document SHALL traverse a defined submittal lifecycle: planned -> submitted -> under EPC review -> accepted (or returned with comments) -> incorporated into turnover.
- Verification: V-004.
- Source: ASSUMPTION — submittal-lifecycle states are inferred from the deliverable role (vendor documentation with EPC review). Source `26020-Package_Requirements.docx` heading 7 detailed lifecycle states are `location TBD` (not extracted into accessible registers).

### REQ-DEL-052-05-005 — Pressure Equipment Registration

The Pressure Equipment Registration Package SHALL be included as a heat-transfer-category submittal for E-5718-1 (design pressure 9,756 kPag / 1,415 psig).
- Verification: V-005.
- Source: SCOPE_LEDGER.csv SOW-0106 (design pressure); ARTIFACT_REGISTER.csv DEL-052-05 (Pressure Equipment Registration Package row).

### REQ-DEL-052-05-006 — FAT/Performance Test Evidence

Equipment FAT / Performance Test Procedure AND the matching FAT / Performance Test Report SHALL both be submitted before the heat exchanger is released for shipment.
- Verification: V-006.
- Source: ARTIFACT_REGISTER.csv DEL-052-05 (Equipment FAT / Performance Test Procedure row; Equipment FAT / Performance Test Report row). The "before shipment" sequencing is `ASSUMPTION` derived from the document-name semantics; explicit gating language is `location TBD`.

### REQ-DEL-052-05-007 — Final Turnover Set

The Vendor Data Book / Final Supplier Documentation SHALL aggregate accepted submittals into a single turnover record set delivered prior to package acceptance under DEL-052-06.
- Verification: V-007.
- Source: ARTIFACT_REGISTER.csv DEL-052-05 (Vendor Data Book / Final Supplier Documentation row); DELIVERABLE_REGISTER.csv row 341 (DEL-052-06 dependency on turnover evidence).

### REQ-DEL-052-05-008 — Interface-Document Set

Interface-discipline documents (Process piping; Drainage/containment; Electrical; I&C; Structural) SHALL be supplied at the level of detail needed for EPC Integrator integration review.
- Verification: V-008.
- Source: PACKAGE_REGISTER.csv row 62 (Applicable interface types: Process Piping; Utility Piping; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports); ARTIFACT_REGISTER.csv DEL-052-05 interface-category rows.

### REQ-DEL-052-05-009 — No Cross-Deliverable Scope Bleed

Documents owned by sibling deliverables (DEL-052-01..04, DEL-052-06) SHALL NOT be re-authored under this deliverable; instead, this register references their authoritative locations.
- Verification: V-009.
- Source: DELIVERABLE_REGISTER.csv rows 336-341.

### REQ-DEL-052-05-010 — Document Control Procedure

The Vendor Document Control Procedure SHALL be the earliest-submitted document and SHALL govern revision, distribution, and acceptance handling for all other submittals.
- Verification: V-010.
- Source: ARTIFACT_REGISTER.csv DEL-052-05 (Vendor Document Control Procedure row, ART-B9AFEA01D9). Sequencing as "earliest" is `ASSUMPTION` from document role; explicit sequencing in source is `location TBD`.

## Standards

| Standard / Source | Relevance | Source |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 7 (Vendor Engineering Deliverables table) | Governs the vendor document register content and obligations | `_REFERENCES.md`; PACKAGE_REGISTER.csv row 62 (Source column) |
| Workbook Packages row 62 | Defines package identity, vendor-vs-EPC responsibility split, applicable interface types | PACKAGE_REGISTER.csv row 62 |
| Provincial pressure equipment regulator (ABSA in Alberta, or equivalent jurisdictional authority) | Governs Pressure Equipment Registration Package contents | ASSUMPTION — jurisdictional authority not explicitly named in accessible source slice; location TBD |
| TEMA (Tubular Exchanger Manufacturers Association) | Heat-exchanger fabrication/inspection conventions applicable to E-5718-1 (TEMA 'R' BEM) | PACKAGE_REGISTER.csv row 62 (Scope); SCOPE_LEDGER.csv SOW-0105 |
| ASME BPVC Section VIII (or equivalent) | Pressure vessel design/fabrication code typically referenced for shell-and-tube exchangers | ASSUMPTION — not explicitly cited in accessible source slice; location TBD |

## Verification

| Verification ID | Requirement | Method | Source |
|---|---|---|---|
| V-001 | REQ-DEL-052-05-001 | Audit of register against ARTIFACT_REGISTER.csv DEL-052-05 rows; gap report = empty | ARTIFACT_REGISTER.csv |
| V-002 | REQ-DEL-052-05-002 | Inspection of register structure for all 9 categories | ARTIFACT_REGISTER.csv category rows |
| V-003 | REQ-DEL-052-05-003 | Sample-row inspection: every row carries a source citation | ARTIFACT_REGISTER.csv (Source column convention) |
| V-004 | REQ-DEL-052-05-004 | Review of submittal status field across register; lifecycle states present | ASSUMPTION (lifecycle inferred) |
| V-005 | REQ-DEL-052-05-005 | Confirm Pressure Equipment Registration Package row is registered and submitted | SCOPE_LEDGER.csv SOW-0106 |
| V-006 | REQ-DEL-052-05-006 | Verify both FAT Procedure and FAT Report submitted; pre-shipment release record exists | ARTIFACT_REGISTER.csv DEL-052-05 |
| V-007 | REQ-DEL-052-05-007 | Confirm Vendor Data Book aggregates accepted submittals at turnover time | ARTIFACT_REGISTER.csv DEL-052-05 |
| V-008 | REQ-DEL-052-05-008 | Cross-check interface document set against PACKAGE_REGISTER.csv applicable-interface list | PACKAGE_REGISTER.csv row 62 |
| V-009 | REQ-DEL-052-05-009 | Cross-deliverable boundary audit against DELIVERABLE_REGISTER.csv rows 336-341 | DELIVERABLE_REGISTER.csv |
| V-010 | REQ-DEL-052-05-010 | Confirm Vendor Document Control Procedure submitted and active before subsequent submittals are processed | ASSUMPTION |

## Documentation

This deliverable produces the documentation; the artifacts produced are themselves the vendor documents listed in the Datasheet. The required local deliverable-side records are:

- `Datasheet.md` (this folder) — the vendor document register and source-category structure.
- `Specification.md` (this file) — the normative requirements on the register and submittals.
- `Guidance.md` (this folder) — rationale, principles, and Conflict Table.
- `Procedure.md` (this folder) — operational steps for producing and operating the register and turnover.
- Source: DELIVERABLE_REGISTER.csv row 340 (AnticipatedArtifacts); ARTIFACT_REGISTER.csv DEL-052-05 rows.
