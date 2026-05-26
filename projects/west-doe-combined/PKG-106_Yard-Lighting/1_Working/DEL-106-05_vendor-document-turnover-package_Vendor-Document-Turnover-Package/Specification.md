# Specification: DEL-106-05 — Vendor Document Turnover Package

Pass: P1 (initial draft) — Source-grounded against GATE-07 Final Published PROJECT_DECOMP snapshot.

## Scope

**Covers:** A single Package Vendor production unit comprising the vendor document register, vendor document submittals, source-required vendor documentation, and turnover records for PKG-106 (Yard Lighting), with EPC Integrator interface/integration review. (Source: DELIVERABLE_REGISTER.csv row DEL-106-05; `_CONTEXT.md` Scope.)

**Excludes:**
- EPC Integrator package Scope of Work, Datasheet, and Construction Work Package (covered by DEL-106-01, DEL-106-02, DEL-106-03).
- Vendor engineered physical equipment package (covered by DEL-106-04).
- EPC review/acceptance and turnover acceptance evidence (covered by DEL-106-06).
- Treating individual source vendor-document table rows as separate deliverables — they remain artifacts/evidence within this package (Source: `_CONTEXT.md` Notes; DELIVERABLE_REGISTER.csv).
- Other PKG-106 exclusions: TBD; no package-specific exclusions stated in source materials (Source: PACKAGE_REGISTER.csv).

## Requirements

ID format: `REQ-106-05-NN`. Unless otherwise noted, all requirements derive directly from DELIVERABLE_REGISTER.csv (row DEL-106-05), `_CONTEXT.md`, ARTIFACT_REGISTER.csv (PKG-106 vendor-doc rows), and PACKAGE_REGISTER.csv.

| ID | Requirement | Source | Notes |
|---|---|---|---|
| REQ-106-05-01 | The deliverable SHALL provide a Vendor Document Register listing all documents the Package Vendor is obligated to submit for PKG-106. | DELIVERABLE_REGISTER.csv (Anticipated Artifacts); `_CONTEXT.md` | Register entry content TBD; ART-182773E33C records gap. |
| REQ-106-05-02 | The deliverable SHALL include the vendor document submittals themselves as evidence. | DELIVERABLE_REGISTER.csv; `_CONTEXT.md` | Submittal list TBD. |
| REQ-106-05-03 | Where the source workbook lists specific vendor documents as rows, those rows SHALL be carried as artifacts of this deliverable rather than as separate deliverables. | `_CONTEXT.md` Notes; DELIVERABLE_REGISTER.csv | No such rows enumerated in current snapshot (ASSUMPTION: none in source for PKG-106 — confirmed by ART-182773E33C). |
| REQ-106-05-04 | The deliverable SHALL include turnover records evidencing handoff of the vendor document package. | DELIVERABLE_REGISTER.csv; `_CONTEXT.md` | Record formats TBD. |
| REQ-106-05-05 | The Package Vendor SHALL be the responsible producing party; the EPC Integrator SHALL perform interface/integration review of vendor documentation. | DELIVERABLE_REGISTER.csv (ResponsibleParty); PACKAGE_REGISTER.csv | Detailed EPC review/acceptance evidence is in DEL-106-06 (ART-DE7811332B, ART-6A9AFD2292). |
| REQ-106-05-06 | Vendor documentation SHALL be consistent with PKG-106 interface declarations: Electrical Power; Grounding / Bonding; Area / Exterior Lighting. | PACKAGE_REGISTER.csv; INTERFACE_REGISTER.csv (IFC-6FCF1B30D6, IFC-DA0D60681B, IFC-ED86F51087) | Detailed interface acceptance criteria TBD; carried as evidence in DEL-106-02. |
| REQ-106-05-07 | The deliverable SHALL be traceable to scope item `SOW-0011` and to objectives `OBJ-001, OBJ-004, OBJ-005, OBJ-009, OBJ-010`. | DELIVERABLE_REGISTER.csv; `_CONTEXT.md` | Objective association is ASSUMPTION (package-grouping heuristic). |
| REQ-106-05-08 | Detailed vendor-document content requirements (titles, revisions, format) SHALL be defined when source basis becomes available. | ARTIFACT_REGISTER.csv (ART-182773E33C "TBD vendor document register"); `_REFERENCES.md` Missing/Deferred References | TBD — currently flagged as Vendor Documentation Gap Evidence. |

## Standards

| Standard / Reference | Applicability | Location | Status |
|---|---|---|---|
| Workbook Packages row 12 | Authoritative source row for PKG-106 vendor-document expectations | Workbook 26020-Package_Requirements.docx / 26020-Packages_Interfaces_4_export.xlsx (in `_Sources` shared root) | location TBD for clause-level vendor-doc slices |
| Project-level vendor document turnover standard | ASSUMPTION: likely applicable; not enumerated in accessible sources for PKG-106 | location TBD | TBD |
| Electrical discipline codes (e.g., NEC, applicable IEEE/IES area-lighting standards) | ASSUMPTION: likely applicable to yard/area lighting vendor documentation | location TBD | TBD; not derived from accessible sources |

## Verification

| Requirement | Verification Approach | Source |
|---|---|---|
| REQ-106-05-01 | Inspection of submitted Vendor Document Register against package SOW (DEL-106-01) and Datasheet (DEL-106-02). | DELIVERABLE_REGISTER.csv (DEL-106-01, -02) |
| REQ-106-05-02 | Inspection that each register entry has a corresponding submittal of the listed revision. | `_CONTEXT.md` |
| REQ-106-05-03 | Inspection cross-checking source workbook vendor-document rows (if any) against artifact set. | `_CONTEXT.md` Notes |
| REQ-106-05-04 | Inspection of turnover record signatures/transmittals against the register closure list. | `_CONTEXT.md` |
| REQ-106-05-05 | Review by EPC Integrator (executed under DEL-106-06). | DELIVERABLE_REGISTER.csv (DEL-106-06); ART-DE7811332B |
| REQ-106-05-06 | Cross-check vendor documents against PKG-106 interface facts captured in DEL-106-02. | ARTIFACT_REGISTER.csv (ART-51069C3B2D, ART-B670C2963F, ART-0686DF8D13, ART-9F2D1E8063) |
| REQ-106-05-07 | Traceability check from this deliverable to SOW-0011 and listed objectives via decomposition registers. | DELIVERABLE_REGISTER.csv; OBJECTIVE_DELIVERABLE_MAP.csv |
| REQ-106-05-08 | TBD verification step pending availability of detailed vendor-doc requirements. | TBD |

## Documentation

Required artifacts (from `_CONTEXT.md` Anticipated Artifacts and ARTIFACT_REGISTER.csv):

- Vendor document register (ART-182773E33C currently flagged TBD)
- Vendor document submittals
- Source vendor document table rows carried as artifacts where available (none in current source set for PKG-106)
- Turnover records

Outputs that live elsewhere but consume this deliverable:
- Vendor document review and comment log — ART-DE7811332B (DEL-106-06)
- Vendor package acceptance and turnover checklist — ART-6A9AFD2292 (DEL-106-06)
- Factory/shop test and inspection evidence — ART-058F5C9C1C (DEL-106-06)
