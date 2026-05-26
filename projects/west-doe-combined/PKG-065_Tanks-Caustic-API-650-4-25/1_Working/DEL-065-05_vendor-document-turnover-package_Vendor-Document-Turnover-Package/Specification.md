# Specification — DEL-065-05 Vendor Document Turnover Package

## Scope

This specification governs the Vendor Document Turnover Package for `PKG-065` "Tanks, Caustic (API 650) 4-25". The deliverable is a single Package Vendor production unit comprising:

- the vendor document register,
- the vendor document submittals issued against that register,
- source-required vendor document table rows preserved as evidence/artifacts where the source enumerates them, and
- the turnover records required for handover of the package to the EPC Integrator.

EPC Integrator review (interface/integration) is in scope of this deliverable's responsibility split. (Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row DEL-065-05.)

In scope:
- Documentation that evidences the engineering, design, fabrication, inspection, test, and supply of the Spent Caustic Tank (TK-6780-1) and the Fresh Caustic Tank (tag TBD), both per modified API 650, 400 bbl nominal capacity. (Source: SCOPE_LEDGER SOW-0198, SOW-0199; `26020-Package_Requirements.docx` package heading 20 — `location TBD` for vendor-document-specific clauses.)

Out of scope:
- Engineering and physical equipment supply itself (that is DEL-065-04 Vendor Engineered Equipment Package). (Source: DELIVERABLE_REGISTER.csv rows DEL-065-04 and DEL-065-05.)
- EPC Integrator's own facility-level documentation (foundations, civil, E&I install, platforms, staircases). (Source: SCOPE_LEDGER SOW-0200 "By others".)
- Standalone deliverables for individual source-document rows; these remain artifacts/evidence within this package. (Source: `_CONTEXT.md` Notes.)

## Requirements

### R-01 Vendor Document Register
The Package Vendor SHALL produce and maintain a Vendor Document Register that lists every document the Vendor will submit for PKG-065, including document number, title, revision, anticipated submittal date, status, and review responsibility. (Source: `_CONTEXT.md` Anticipated Artifacts — "Vendor document register"; specific column set and numbering convention `location TBD` — `26020-Package_Requirements.docx` package heading 20 not directly read.)

### R-02 Submittals Per Register
For every document listed on the register, the Package Vendor SHALL submit the document to the EPC Integrator at the revision and milestone declared on the register. Revision coding (e.g., A/B/C for IFR/IFA/IFC, or 0/1/2 numerical) is `TBD` and SHALL be agreed with the EPC Integrator before the first submittal. (Source: `_CONTEXT.md` Anticipated Artifacts — "vendor document submittals"; ASSUMPTION on revision convention.)

### R-03 Source-Required Vendor Documents
Where `26020-Package_Requirements.docx` package heading 20 (Workbook Packages row 87) enumerates a specific required vendor document, that document SHALL appear on the register and SHALL be submitted. The exhaustive list of source-required vendor documents is `location TBD` (binary `.docx` not directly read in this run); the Vendor SHALL extract it from the authoritative source before issuing Rev. 0 of the register. (Source: `_CONTEXT.md` Source Reference; `_CONTEXT.md` Anticipated Artifacts — "source vendor document table rows as artifacts where available".)

### R-04 Turnover Records
The Package Vendor SHALL provide turnover records demonstrating mechanical completion of the package, suitable for the EPC Integrator to accept and integrate the package into facility commissioning. Minimum content SHALL include (ASSUMPTION — typical for API 650 atmospheric tanks; not enumerated in available source slice):
- material test reports (MTRs) for plate, structural, and welded components;
- weld maps and NDE records (RT/UT/PT/MT as required by the code of construction);
- hydrostatic test record(s) per modified API 650;
- vendor inspection release / Certificate of Conformance;
- nameplate rubbing or photograph and serial number record;
- as-built drawings;
- operations & maintenance manual including the integral heater (≥ 32.2 °C / 90 °F minimum) for TK-6780-1 (Source: SOW-0199 for heater);
- spare parts list and recommended commissioning spares.

Items beyond the workbook/source statement are labeled ASSUMPTION; the authoritative content list is `location TBD`.

### R-05 EPC Integrator Review
Every submittal SHALL pass through EPC Integrator interface/integration review before being treated as accepted. Acceptance criteria, return cycles, and review timelines are `TBD` and SHALL be defined in the project's document control procedure (procedure reference `TBD`). (Source: `_CONTEXT.md` ResponsibleParty — "EPC Integrator interface/integration review".)

### R-06 Traceability to Scope
Every document on the register SHALL be traceable back to a scope item (`SOW-0197`..`SOW-0200`) or to the underlying equipment identity (TK-6780-1; Fresh Caustic Tank). (Source: SCOPE_LEDGER rows SOW-0197..SOW-0200 explicitly list DEL-065-05 in the covered-deliverables column.)

### R-07 Code Compatibility
Documentation SHALL be sufficient to evidence design and fabrication to modified API 650. Specific modifications to API 650 are `location TBD` (not enumerated in available source slice — see DEL-065-04 R-01); the vendor SHALL document deviations from base API 650. (Source: SOW-0199; cross-ref DEL-065-04 Specification R-01.)

## Standards

| Standard | Applicability | Source |
|---|---|---|
| API 650 (modified) | Code of construction for both tanks; documentation must evidence compliance and deviations | SOW-0199 |
| EPC Integrator document control procedure | Submittal format, transmittal, review/return cycle | `_CONTEXT.md` (review responsibility); document identity `TBD` |
| Project numbering/CAD/document control standards | Document numbering, revision, file formats | `TBD` — not stated in available source slices |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-01 Vendor Document Register | EPC Integrator review of Rev. 0 register; check that every anticipated artifact category in `_CONTEXT.md` is represented |
| R-02 Submittals Per Register | Transmittal log compared against register; status closed-out at acceptance |
| R-03 Source-Required Vendor Documents | Cross-check register against `26020-Package_Requirements.docx` package heading 20 source-required list (extraction `TBD`) |
| R-04 Turnover Records | Turnover record set checklist signed off by EPC Integrator prior to handover |
| R-05 EPC Integrator Review | Review status field on register reaches "Accepted" or equivalent for each document |
| R-06 Traceability | Register includes a SOW-/equipment-reference column populated for every line |
| R-07 Code Compatibility | Documentation set evidences API 650 modified design; deviation list reviewed |

## Documentation

Anticipated artifacts produced by/contained in this deliverable:
- Vendor Document Register (Rev. 0 and subsequent revisions)
- Vendor document submittals (per register)
- Preserved source-required vendor document evidence rows (where available)
- Turnover records package
- EPC Integrator review/acceptance records

(Source: `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER.csv row DEL-065-05.)
