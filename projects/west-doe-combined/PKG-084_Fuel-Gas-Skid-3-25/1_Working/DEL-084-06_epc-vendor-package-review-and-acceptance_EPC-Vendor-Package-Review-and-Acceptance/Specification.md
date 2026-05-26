# Specification — DEL-084-06 EPC Vendor Package Review and Acceptance

## Scope

This specification governs the EPC Integrator's review and acceptance of the Fuel Gas Skid 3-25 vendor package (PKG-084). The deliverable produces vendor document review records, an acceptance checklist, test/inspection evidence summaries, and turnover evidence sufficient for integration handoff to commissioning at the 03-25 West Doe Compressor Station (source: _CONTEXT.md; 3-25_Comp_and_Liquids_DBM.md sec. Site/Facility).

**Covers.** Acceptance of vendor scope items SOW-0095, SOW-0096, SOW-0097, SOW-0098 as listed in _CONTEXT.md; review against EPC SOW (DEL-084-01), Package Datasheet (DEL-084-02), and Construction Work Package (DEL-084-03); coordination with Vendor Engineered Equipment Package (DEL-084-04) and Vendor Document Turnover Package (DEL-084-05).

**Excludes.** Vendor engineering, fabrication, or supply (delivered under DEL-084-04). Vendor document production (delivered under DEL-084-05). Downstream commissioning and start-up operations. Modifications to the 04-25 utility supply scope, except to confirm interface compliance at the package boundary.

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| REQ-1 | The acceptance set SHALL evidence vendor conformance with each accepted requirement carried in DEL-084-01 (EPC Scope of Work). | DELIVERABLE_REGISTER.csv row 324 (acceptance basis) |
| REQ-2 | The acceptance set SHALL evidence vendor conformance with the Package Datasheet (DEL-084-02), including tagged equipment list, design conditions, and interface requirements matrix. | DELIVERABLE_REGISTER.csv row 325 |
| REQ-3 | The acceptance set SHALL evidence construction, tie-in, inspection, and turnover steps consistent with DEL-084-03 (Construction Work Package). | DELIVERABLE_REGISTER.csv row 326 |
| REQ-4 | The acceptance set SHALL reconcile vendor document submittals against the Vendor Document Turnover Package (DEL-084-05) register; missing or non-conforming documents SHALL be itemized in the review log. | DELIVERABLE_REGISTER.csv row 328 |
| REQ-5 | Acceptance evidence SHALL confirm the LP fuel-gas service envelope: normal total 1.382 MMSCFD, design >1.5 MMSCFD, supplied from the 04-25 sales-gas splitter (primary) and Alliance (secondary). ASSUMPTION: the vendor skid serves the LP fuel-gas distribution described in the DBM; acceptance applies the DBM service basis unless DEL-084-02 supersedes it. | 3-25_Comp_and_Liquids_DBM.md sec. Fuel Gas |
| REQ-6 | Acceptance evidence SHALL confirm package design for site ambient envelope -40 deg C to +35 deg C and elevation 673 m AMSL unless a stricter package-specific basis is invoked by DEL-084-02. | 3-25_Comp_and_Liquids_DBM.md sec. Site Conditions |
| REQ-7 | Acceptance evidence SHALL include FAT, SAT (where applicable), pressure-test, NDE, and functional-test records for the skid scope. Specific test plan content is TBD pending DEL-084-02 and vendor ITP. | _CONTEXT.md (Anticipated Artifacts); location TBD |
| REQ-8 | Acceptance evidence SHALL include turnover records: mechanical completion certificate, punchlist (open/cleared), system handover sign-off. | _CONTEXT.md (Anticipated Artifacts) |
| REQ-9 | Open items requiring human ruling (e.g., emergency buyback fuel gas applicability per CONFLICT-1) SHALL NOT be silently closed during acceptance; unresolved items SHALL be carried as `TBD` on the acceptance checklist. | 3-25_Comp_and_Liquids_DBM.md sec. Fuel Gas |
| REQ-10 | The acceptance package SHALL cite source slices for every accepted requirement to preserve audit traceability. | K-PROV-1 (governance) — ASSUMPTION as a deliverable-level invariant |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| Project EPC SOW (DEL-084-01) | Primary contractual basis for vendor acceptance | location TBD (DEL-084-01 not yet drafted at run time) |
| Project Package Datasheet (DEL-084-02) | Technical basis for acceptance | location TBD (DEL-084-02 not yet drafted) |
| 26020-Package_Requirements.docx package heading 37 | Source-of-truth package requirement statements | location TBD (binary source not parsed) |
| Applicable Canadian provincial mechanical, pressure equipment, and electrical codes for British Columbia | Acceptance validation of regulatory compliance | location TBD (no clause-level text in accessible source slices) |

## Verification

| Req | Verification Method |
|---|---|
| REQ-1, REQ-2, REQ-3 | Document review against DEL-084-01/02/03; conformance log entries |
| REQ-4 | Cross-check of vendor submittals against DEL-084-05 register |
| REQ-5, REQ-6 | Inspection of vendor design records (datasheets, calculations) confirming service envelope and site basis |
| REQ-7 | Witnessed/reviewed FAT/SAT/test reports; NDE certificates; pressure-test packets |
| REQ-8 | Mechanical completion certificate; punchlist register; signed turnover transmittal |
| REQ-9 | Acceptance checklist entries marked TBD or NEEDS_HUMAN_RULING with traceable references |
| REQ-10 | Audit of acceptance package for source citations |

## Documentation

The acceptance deliverable comprises:

- Vendor document review log (per REQ-4)
- Package acceptance checklist (covering REQ-1 through REQ-9)
- Test/inspection evidence dossier (per REQ-7)
- Turnover evidence dossier (per REQ-8)
- Open-items register (per REQ-9)
