# Specification — DEL-089-05 Vendor Document Turnover Package (PKG-089)

> Normative. Requirements derive from accessible source slices in the GATE-07 PROJECT_DECOMP snapshot (which extracted `26020-Package_Requirements.docx` heading 42 into the registers) and the locally accessible `3-25_Comp_and_Liquids_DBM.md`. Inferred requirements are labeled `ASSUMPTION`; unsupported items are `TBD`.

## Scope

### In Scope

- The vendor document register and submittal flow for PKG-089 (Pig Receivers (Inlet) 3-25) covering all 10 source categories listed in the Datasheet.
  - Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 430; ARTIFACT_REGISTER.csv DEL-089-05 category rows.
- Vendor document submittals against each of the 109 source-listed vendor document artifact rows carried under DEL-089-05.
  - Source: ARTIFACT_REGISTER.csv DEL-089-05 rows.
- Turnover records (Vendor Data Book / Final Supplier Documentation) consolidating accepted submittals at acceptance.
  - Source: ARTIFACT_REGISTER.csv DEL-089-05; DELIVERABLE_REGISTER.csv row 430 (AnticipatedArtifacts).
- EPC Integrator interface/integration review interaction surface with this deliverable.
  - Source: DELIVERABLE_REGISTER.csv row 430 (ResponsibleParty).

### Out of Scope

- Physical equipment package engineering and design — owned by DEL-089-04 Vendor Engineered Equipment Package.
  - Source: DELIVERABLE_REGISTER.csv row 429.
- EPC review log, acceptance checklist, and acceptance evidence — owned by DEL-089-06 EPC Vendor Package Review and Acceptance.
  - Source: DELIVERABLE_REGISTER.csv row 431.
- Construction installation, tie-ins, and turnover field activities — owned by DEL-089-03 Construction Work Package.
  - Source: DELIVERABLE_REGISTER.csv row 428.
- Interconnecting piping, DCS integration, foundations, and electrical supply to MCC — by-others scope (EPC Integrator).
  - Source: SCOPE_LEDGER.csv SOW-0160.
- Promoting any individual source vendor-document row to a standalone deliverable.
  - Source: DELIVERABLE_REGISTER.csv row 430 (Notes).
- Cross-deliverable register aggregation across packages.

## Requirements

### REQ-DEL-089-05-001 — Vendor Document Register Completeness

The Package Vendor SHALL maintain a vendor document register covering every source-listed vendor document carried as an artifact row under DEL-089-05 (109 rows in ARTIFACT_REGISTER.csv of the Gate 7 snapshot).
- Verification: V-001.
- Source: ARTIFACT_REGISTER.csv DEL-089-05 rows; DELIVERABLE_REGISTER.csv row 430 (AnticipatedArtifacts: "Vendor document register").

### REQ-DEL-089-05-002 — Source-Category Coverage

The register SHALL organize documents under the 10 source categories listed in the Datasheet (Core vendor documents; Core package engineering; Process package design; Process piping interfaces; Relief/Flare/Vent interfaces; Drainage/containment interfaces; Electrical; I&C interfaces; Structural; Pipeline/Pigging interfaces).
- Verification: V-002.
- Source: ARTIFACT_REGISTER.csv DEL-089-05 category rows; PACKAGE_REGISTER.csv row 77 (Applicable interface types).

### REQ-DEL-089-05-003 — Authority Anchor

Each register row SHALL identify its source basis (Workbook Packages row 77; `26020-Package_Requirements.docx` heading 42 — Vendor Engineering Deliverables table; or other accepted decomposition source).
- Verification: V-003.
- Source: ARTIFACT_REGISTER.csv DEL-089-05 (Source column).

### REQ-DEL-089-05-004 — Submittal Lifecycle

Each registered document SHALL traverse a defined submittal lifecycle: planned -> submitted -> under EPC review -> accepted (or returned with comments) -> incorporated into turnover.
- Verification: V-004.
- Source: ASSUMPTION — submittal-lifecycle states are inferred from the deliverable role (vendor documentation with EPC review). Source `26020-Package_Requirements.docx` heading 42 detailed lifecycle states are `location TBD` (not extracted into accessible registers).

### REQ-DEL-089-05-005 — Pressure Equipment Registration

The Pressure Equipment Registration Package SHALL be included for PR-1010/1020-2 pig receivers, using the controlling MAWP (635 psig per SOW-0160).
- Verification: V-005.
- Source: SCOPE_LEDGER.csv SOW-0160 (Design pressure normal high = 200 psig; MAWP = 635 psig); ARTIFACT_REGISTER.csv DEL-089-05 (Pressure Equipment Registration Package row).

### REQ-DEL-089-05-006 — Sour-Service Material Certification

Material Test Reports / Certificates and the Inspection and Test Plan SHALL provide evidence of materials suitable for the design sour-service condition (0.1 mol% sour).
- Verification: V-006.
- Source: SCOPE_LEDGER.csv SOW-0159; ARTIFACT_REGISTER.csv DEL-089-05 (MTR/Certificates row; ITP row).

### REQ-DEL-089-05-007 — ESDV Documentation

The vendor document set SHALL include ESDV data sheets and functional requirements for the inlet ESDVs (full-port, piggable, with position transmitters per DBM) installed upstream of each receiver.
- Verification: V-007.
- Source: SCOPE_LEDGER.csv SOW-0159; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 239 (Inlet ESDV: Full-port, piggable, position transmitters).

### REQ-DEL-089-05-008 — Sweet-Gas Purge and HP Flare Vent Provisions

Vendor documentation SHALL describe the sweet-gas purge (downstream of manual isolation valve for sour gas purge prior to opening for pig retrieval) and the vent line to the HP flare system as integrated package provisions.
- Verification: V-008.
- Source: SCOPE_LEDGER.csv SOW-0159; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 230-238.

### REQ-DEL-089-05-009 — FAT/Performance Test Evidence

Equipment FAT / Performance Test Procedure AND the matching FAT / Performance Test Report SHALL both be submitted before the receivers are released for shipment.
- Verification: V-009.
- Source: ARTIFACT_REGISTER.csv DEL-089-05 (Equipment FAT / Performance Test Procedure row; Equipment FAT / Performance Test Report row). The "before shipment" sequencing is `ASSUMPTION` derived from the document-name semantics; explicit gating language is `location TBD`.

### REQ-DEL-089-05-010 — Final Turnover Set

The Vendor Data Book / Final Supplier Documentation SHALL aggregate accepted submittals into a single turnover record set delivered prior to package acceptance under DEL-089-06.
- Verification: V-010.
- Source: ARTIFACT_REGISTER.csv DEL-089-05 (Vendor Data Book / Final Supplier Documentation row); DELIVERABLE_REGISTER.csv row 431 (DEL-089-06 dependency on turnover evidence).

### REQ-DEL-089-05-011 — Interface-Document Set

Interface-discipline documents (Process Piping; Relief/Flare/Vent; Drainage/containment; Electrical Power; EHT; I&C/Control Cabling; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports; Pipeline/Pigging) SHALL be supplied at the level of detail needed for EPC Integrator integration review.
- Verification: V-011.
- Source: PACKAGE_REGISTER.csv row 77 (ApplicableInterfaceTypes); ARTIFACT_REGISTER.csv DEL-089-05 interface-category rows.

### REQ-DEL-089-05-012 — No Cross-Deliverable Scope Bleed

Documents owned by sibling deliverables (DEL-089-01..04, DEL-089-06) SHALL NOT be re-authored under this deliverable; this register references their authoritative locations.
- Verification: V-012.
- Source: DELIVERABLE_REGISTER.csv rows 426-431.

### REQ-DEL-089-05-013 — Document Control Procedure

The Vendor Document Control Procedure SHALL be the earliest-submitted document and SHALL govern revision, distribution, and acceptance handling for all other submittals.
- Verification: V-013.
- Source: ARTIFACT_REGISTER.csv DEL-089-05 (Vendor Document Control Procedure row, ART-F156006A5E). Sequencing as "earliest" is `ASSUMPTION` from document role; explicit sequencing in source is `location TBD`.

### REQ-DEL-089-05-014 — Identical Twin Package Treatment

The vendor document set SHALL describe both PR-1010-2 and PR-1020-2 as identical units; deltas (if any) SHALL be itemized rather than masked.
- Verification: V-014.
- Source: SCOPE_LEDGER.csv SOW-0159 ("(2x) Pig receiver assemblies"); PACKAGE_REGISTER.csv row 77 (Supply 2 identical 610mm OD pig receivers).

## Standards

| Standard / Source | Relevance | Source |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 42 (Vendor Engineering Deliverables table) | Governs the vendor document register content and obligations | `_REFERENCES.md`; PACKAGE_REGISTER.csv row 77 (Source column) |
| Workbook Packages row 77 | Defines package identity, vendor-vs-EPC responsibility split, applicable interface types | PACKAGE_REGISTER.csv row 77 |
| `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Inlet Pipeline Interface and Pigging) | Sets the facility design basis for pig receivers, ESDV, sweet-gas purge, HP flare vent | DBM-Comp_and_Liquids/3-25 lines 226-239 |
| Provincial pressure equipment regulator (ABSA in Alberta, or equivalent jurisdictional authority) | Governs Pressure Equipment Registration Package contents | ASSUMPTION — jurisdictional authority not explicitly named in accessible source slice; location TBD |
| ASME BPVC Section VIII (or equivalent) | Pressure vessel design/fabrication code typically referenced for cylindrical pressure receivers | ASSUMPTION — not explicitly cited in accessible source slice; location TBD |
| Sour-service material standards (e.g., NACE MR0175 / ISO 15156) | Material selection for 0.1 mol% sour service | ASSUMPTION — not explicitly cited in accessible source slice; location TBD |

## Verification

| Verification ID | Requirement | Method | Source |
|---|---|---|---|
| V-001 | REQ-DEL-089-05-001 | Audit of register against ARTIFACT_REGISTER.csv DEL-089-05 rows (109 expected); gap report = empty | ARTIFACT_REGISTER.csv |
| V-002 | REQ-DEL-089-05-002 | Inspection of register structure for all 10 categories | ARTIFACT_REGISTER.csv category rows |
| V-003 | REQ-DEL-089-05-003 | Sample-row inspection: every row carries a source citation | ARTIFACT_REGISTER.csv (Source column convention) |
| V-004 | REQ-DEL-089-05-004 | Review of submittal status field across register; lifecycle states present | ASSUMPTION (lifecycle inferred) |
| V-005 | REQ-DEL-089-05-005 | Confirm Pressure Equipment Registration Package row is registered and submitted | SCOPE_LEDGER.csv SOW-0160 |
| V-006 | REQ-DEL-089-05-006 | Confirm MTRs and ITP evidence sour-service material compliance | SCOPE_LEDGER.csv SOW-0159 |
| V-007 | REQ-DEL-089-05-007 | Confirm ESDV data sheets and functional requirements submitted | SCOPE_LEDGER.csv SOW-0159; DBM-Comp_and_Liquids/3-25 line 239 |
| V-008 | REQ-DEL-089-05-008 | Confirm sweet-gas purge and HP flare vent provisions are documented | SCOPE_LEDGER.csv SOW-0159; DBM lines 230-238 |
| V-009 | REQ-DEL-089-05-009 | Verify both FAT Procedure and FAT Report submitted; pre-shipment release record exists | ARTIFACT_REGISTER.csv DEL-089-05 |
| V-010 | REQ-DEL-089-05-010 | Confirm Vendor Data Book aggregates accepted submittals at turnover time | ARTIFACT_REGISTER.csv DEL-089-05 |
| V-011 | REQ-DEL-089-05-011 | Cross-check interface document set against PACKAGE_REGISTER.csv applicable-interface list | PACKAGE_REGISTER.csv row 77 |
| V-012 | REQ-DEL-089-05-012 | Cross-deliverable boundary audit against DELIVERABLE_REGISTER.csv rows 426-431 | DELIVERABLE_REGISTER.csv |
| V-013 | REQ-DEL-089-05-013 | Confirm Vendor Document Control Procedure submitted and active before subsequent submittals are processed | ASSUMPTION |
| V-014 | REQ-DEL-089-05-014 | Inspect documentation set for identical-twin treatment of PR-1010-2 and PR-1020-2 | SCOPE_LEDGER.csv SOW-0159 |

## Documentation

This deliverable produces the documentation; the artifacts produced are themselves the vendor documents listed in the Datasheet. The required local deliverable-side records are:

- `Datasheet.md` (this folder) — the vendor document register and source-category structure.
- `Specification.md` (this file) — the normative requirements on the register and submittals.
- `Guidance.md` (this folder) — rationale, principles, and Conflict Table.
- `Procedure.md` (this folder) — operational steps for producing and operating the register and turnover.
- Source: DELIVERABLE_REGISTER.csv row 430 (AnticipatedArtifacts); ARTIFACT_REGISTER.csv DEL-089-05 rows.
