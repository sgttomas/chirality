# Specification — DEL-059-05 Vendor Document Turnover Package (PKG-059)

> Normative. Requirements derive from accessible source slices in the GATE-07 PROJECT_DECOMP snapshot (which extracted `26020-Package_Requirements.docx` heading 14 into the registers). Inferred requirements are labeled `ASSUMPTION`; unsupported items are `TBD`.

## Scope

### In Scope

- The vendor document register and submittal flow for PKG-059 (Storage Bullets — two unstable condensate bullets, sixteen LPG product bullets) covering all 10 source categories listed in the Datasheet.
  - Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 466; ARTIFACT_REGISTER.csv DEL-059-05 category rows.
- Vendor document submittals against each source-listed vendor document carried as an artifact row under DEL-059-05.
  - Source: ARTIFACT_REGISTER.csv DEL-059-05 rows.
- Turnover records (Vendor Data Book / Final Supplier Documentation) consolidating accepted submittals at acceptance.
  - Source: ARTIFACT_REGISTER.csv ART-FD677DDDB8; DELIVERABLE_REGISTER.csv row 466 (AnticipatedArtifacts).
- EPC Integrator interface/integration review interaction surface with this deliverable.
  - Source: DELIVERABLE_REGISTER.csv row 466 (ResponsibleParty).

### Out of Scope

- Physical equipment package engineering and design — owned by DEL-059-04 Vendor Engineered Equipment Package.
  - Source: DELIVERABLE_REGISTER.csv row 465.
- EPC review log, acceptance checklist, and acceptance evidence — owned by DEL-059-06 EPC Vendor Package Review and Acceptance.
  - Source: DELIVERABLE_REGISTER.csv row 467.
- Construction installation, tie-ins, and turnover field activities — owned by DEL-059-03 Construction Work Package.
  - Source: DELIVERABLE_REGISTER.csv row 464.
- Promoting any individual source vendor-document row to a standalone deliverable.
  - Source: DELIVERABLE_REGISTER.csv row 466 (Notes).
- Cross-deliverable register aggregation across packages.
- Items declared "by others" in SOW-0184: foundations, DCS integration, electrical supply to MCC.
  - Source: SCOPE_LEDGER.csv SOW-0184.

## Requirements

### REQ-DEL-059-05-001 — Vendor Document Register Completeness

The Package Vendor SHALL maintain a vendor document register covering every source-listed vendor document carried as an artifact row under DEL-059-05.
- Verification: V-001.
- Source: ARTIFACT_REGISTER.csv DEL-059-05 rows (93 rows); DELIVERABLE_REGISTER.csv row 466 (AnticipatedArtifacts: "Vendor document register").

### REQ-DEL-059-05-002 — Source-Category Coverage

The register SHALL organize documents under the 10 source categories listed in the Datasheet (Core vendor documents; Core package engineering; Static pressure equipment; Relief / flare / vent design; Process piping interfaces; Drainage / containment interfaces; Electrical / lighting / EHT / grounding; Instrumentation and controls interfaces; Structural / foundations / supports / access; Civil grading / spill containment interfaces).
- Verification: V-002.
- Source: ARTIFACT_REGISTER.csv DEL-059-05 category rows.

### REQ-DEL-059-05-003 — Authority Anchor

Each register row SHALL identify its source basis (Workbook Packages row 83; `26020-Package_Requirements.docx` heading 14 — Vendor Engineering Deliverables table; or other accepted decomposition source).
- Verification: V-003.
- Source: ARTIFACT_REGISTER.csv DEL-059-05 (Source column convention).

### REQ-DEL-059-05-004 — Submittal Lifecycle

Each registered document SHALL traverse a defined submittal lifecycle: planned -> submitted -> under EPC review -> accepted (or returned with comments) -> incorporated into turnover.
- Verification: V-004.
- Source: ASSUMPTION — submittal-lifecycle states are inferred from the deliverable role (vendor documentation with EPC review). Source `26020-Package_Requirements.docx` heading 14 detailed lifecycle states are `location TBD` (not extracted into accessible registers).

### REQ-DEL-059-05-005 — Pressure Equipment Registration

The Pressure Equipment Registration Package SHALL be included as a static-pressure-equipment-category submittal for each bullet (each designed for 1724 kPag at 66 C and full vacuum).
- Verification: V-005.
- Source: SCOPE_LEDGER.csv SOW-0183 (design pressure/temperature); ARTIFACT_REGISTER.csv ART-01EEC704CB.

### REQ-DEL-059-05-006 — FAT/Performance Test Evidence

Equipment FAT / Performance Test Procedure AND the matching FAT / Performance Test Report SHALL both be submitted before each bullet is released for shipment.
- Verification: V-006.
- Source: ARTIFACT_REGISTER.csv ART-0D1E51ADA7; ART-5098C5E6CC. The "before shipment" sequencing is `ASSUMPTION` derived from the document-name semantics; explicit gating language is `location TBD`.

### REQ-DEL-059-05-007 — Final Turnover Set

The Vendor Data Book / Final Supplier Documentation SHALL aggregate accepted submittals into a single turnover record set delivered prior to package acceptance under DEL-059-06.
- Verification: V-007.
- Source: ARTIFACT_REGISTER.csv ART-FD677DDDB8; DELIVERABLE_REGISTER.csv row 467 (DEL-059-06 dependency on turnover evidence).

### REQ-DEL-059-05-008 — Interface-Document Set

Interface-discipline documents (Process piping; Relief/flare/vent; Drainage/containment; Electrical/EHT/grounding/lighting; I&C; Structural; Civil grading/spill containment) SHALL be supplied at the level of detail needed for EPC Integrator integration review.
- Verification: V-008.
- Source: PACKAGE_REGISTER.csv row 83 (Applicable interface types: Process Piping; Relief / Flare / Vent; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports); ARTIFACT_REGISTER.csv DEL-059-05 interface-category rows.

### REQ-DEL-059-05-009 — No Cross-Deliverable Scope Bleed

Documents owned by sibling deliverables (DEL-059-01..04, DEL-059-06) SHALL NOT be re-authored under this deliverable; instead, this register references their authoritative locations.
- Verification: V-009.
- Source: DELIVERABLE_REGISTER.csv rows 462-467.

### REQ-DEL-059-05-010 — Document Control Procedure

The Vendor Document Control Procedure SHALL be the earliest-submitted document and SHALL govern revision, distribution, and acceptance handling for all other submittals.
- Verification: V-010.
- Source: ARTIFACT_REGISTER.csv ART-D4D95E703A. Sequencing as "earliest" is `ASSUMPTION` from document role; explicit sequencing in source is `location TBD`.

### REQ-DEL-059-05-011 — Relief / Flare / Vent Design Package

The Relief and Flare Design Basis, PSV / Pressure Relief Sizing Calculations, Relief Valve Data Sheets, Flare Load Summary / Flare System Study, and Blowdown / Depressurization Study SHALL be submitted as the relief / flare / vent design package for the bullet farm.
- Verification: V-011.
- Source: ARTIFACT_REGISTER.csv ART-3DDFDEB4CF; ART-FEBD5A09B8; ART-666608E5C5; ART-2387C23874; ART-34A9808598. Driven by full-vacuum design and LPG inventory (SCOPE_LEDGER.csv SOW-0183, SOW-0184).

### REQ-DEL-059-05-012 — LPG Vapour Equalization and Blanket Gas Documentation

Vendor documentation SHALL describe the LPG vapour-equalization arrangement (no pockets) and the blanket-gas arrangement for butane storage.
- Verification: V-012.
- Source: SCOPE_LEDGER.csv SOW-0184. Specific document mapping is `ASSUMPTION` — coverage expected under Process piping interfaces (P&IDs, line list, tie-in list) and Control Narrative / Functional Specification; explicit document-to-feature mapping in source is `location TBD`.

### REQ-DEL-059-05-013 — Civil Grading and Spill Containment Documentation

Grading Plan, Drainage / Stormwater Management Report, Retention Pond / Containment Basin Design, and Civil MTO SHALL be submitted to support secondary-containment and spill-containment requirements for the LPG and condensate inventory.
- Verification: V-013.
- Source: ARTIFACT_REGISTER.csv (DEL-059-05 civil category rows); PACKAGE_REGISTER.csv row 83 (Applicable interface types: Grading / Site Drainage / Spill Containment).

### REQ-DEL-059-05-014 — Scope-By-Others Exclusion

Vendor documentation SHALL NOT purport to include foundation design as a vendor-supplied physical scope, DCS integration as a vendor-supplied physical scope, or MCC-side electrical supply as a vendor-supplied physical scope; the corresponding interface/coordination documents (Foundation Drawings, Anchor Bolt / Embedment Drawings, DCS I/O List, Cause and Effect Matrix, Package Vendor Interface Specification) SHALL be supplied to enable the EPC scope of these items.
- Verification: V-014.
- Source: SCOPE_LEDGER.csv SOW-0184 ("Foundations, DCS integration, and electrical supply to MCC are by others"); ARTIFACT_REGISTER.csv DEL-059-05 (interface rows).

## Standards

| Standard / Source | Relevance | Source |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 14 (Vendor Engineering Deliverables table) | Governs the vendor document register content and obligations | `_REFERENCES.md`; PACKAGE_REGISTER.csv row 83 (Source column) |
| Workbook Packages row 83 | Defines package identity, vendor-vs-EPC responsibility split, applicable interface types | PACKAGE_REGISTER.csv row 83 |
| Provincial pressure equipment regulator (ABSA in Alberta, or equivalent jurisdictional authority) | Governs Pressure Equipment Registration Package contents | ASSUMPTION — jurisdictional authority not explicitly named in accessible source slice; location TBD |
| ASME BPVC Section VIII (or equivalent) | Pressure vessel design/fabrication code typically referenced for horizontal pressure-vessel storage bullets | ASSUMPTION — not explicitly cited in accessible source slice; location TBD |
| API 2510 / API 510 (or equivalent) | LPG storage design / pressure-vessel in-service inspection codes typically referenced for LPG bullets | ASSUMPTION — not explicitly cited in accessible source slice; location TBD |
| Word source basis `26020-01-PT-RFQ-17-007-_Storage_Bullets.docx` | Authoritative RFQ-level scope reference for the package | PACKAGE_REGISTER.csv row 83 (Source column); location TBD for direct slice extraction |

## Verification

| Verification ID | Requirement | Method | Source |
|---|---|---|---|
| V-001 | REQ-DEL-059-05-001 | Audit of register against ARTIFACT_REGISTER.csv DEL-059-05 rows; gap report = empty | ARTIFACT_REGISTER.csv |
| V-002 | REQ-DEL-059-05-002 | Inspection of register structure for all 10 categories | ARTIFACT_REGISTER.csv category rows |
| V-003 | REQ-DEL-059-05-003 | Sample-row inspection: every row carries a source citation | ARTIFACT_REGISTER.csv (Source column convention) |
| V-004 | REQ-DEL-059-05-004 | Review of submittal status field across register; lifecycle states present | ASSUMPTION (lifecycle inferred) |
| V-005 | REQ-DEL-059-05-005 | Confirm Pressure Equipment Registration Package row is registered and submitted per bullet | SCOPE_LEDGER.csv SOW-0183 |
| V-006 | REQ-DEL-059-05-006 | Verify both FAT Procedure and FAT Report submitted per bullet; pre-shipment release record exists | ARTIFACT_REGISTER.csv DEL-059-05 |
| V-007 | REQ-DEL-059-05-007 | Confirm Vendor Data Book aggregates accepted submittals at turnover time | ARTIFACT_REGISTER.csv DEL-059-05 |
| V-008 | REQ-DEL-059-05-008 | Cross-check interface document set against PACKAGE_REGISTER.csv applicable-interface list | PACKAGE_REGISTER.csv row 83 |
| V-009 | REQ-DEL-059-05-009 | Cross-deliverable boundary audit against DELIVERABLE_REGISTER.csv rows 462-467 | DELIVERABLE_REGISTER.csv |
| V-010 | REQ-DEL-059-05-010 | Confirm Vendor Document Control Procedure submitted and active before subsequent submittals are processed | ASSUMPTION |
| V-011 | REQ-DEL-059-05-011 | Confirm all five relief/flare/vent design documents submitted | ARTIFACT_REGISTER.csv (Relief / flare / vent category rows) |
| V-012 | REQ-DEL-059-05-012 | Confirm LPG vapour equalization and butane blanket gas described in P&IDs and Control Narrative | SCOPE_LEDGER.csv SOW-0184 |
| V-013 | REQ-DEL-059-05-013 | Confirm civil grading / containment documents submitted | ARTIFACT_REGISTER.csv (Civil category rows) |
| V-014 | REQ-DEL-059-05-014 | Audit that vendor docs do not claim by-others items as in-scope; confirm interface docs are present | SCOPE_LEDGER.csv SOW-0184 |

## Documentation

This deliverable produces the documentation; the artifacts produced are themselves the vendor documents listed in the Datasheet. The required local deliverable-side records are:

- `Datasheet.md` (this folder) — the vendor document register and source-category structure.
- `Specification.md` (this file) — the normative requirements on the register and submittals.
- `Guidance.md` (this folder) — rationale, principles, and Conflict Table.
- `Procedure.md` (this folder) — operational steps for producing and operating the register and turnover.
- Source: DELIVERABLE_REGISTER.csv row 466 (AnticipatedArtifacts); ARTIFACT_REGISTER.csv DEL-059-05 rows.
