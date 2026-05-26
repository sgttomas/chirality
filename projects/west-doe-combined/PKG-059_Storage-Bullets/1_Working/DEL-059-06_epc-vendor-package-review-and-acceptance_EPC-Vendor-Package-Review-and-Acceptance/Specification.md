# Specification — DEL-059-06 EPC Vendor Package Review and Acceptance

## Scope

This specification governs the EPC Integrator activities required to review, accept, and document the vendor-engineered NGL storage bullet package for PKG-059 (Storage Bullets). Acceptance is evaluated against the EPC Scope of Work (DEL-059-01), Package Datasheet (DEL-059-02), and Construction Work Package (DEL-059-03), with vendor inputs from DEL-059-04 and DEL-059-05.

**In scope:**
- Vendor document review against the EPC basis documents.
- Integration acceptance against package and facility interface requirements.
- Handoff/turnover readiness verification.
- Production of the four anticipated artifacts: vendor document review log, package acceptance checklist, test/inspection evidence, turnover evidence (`_CONTEXT.md` Anticipated Artifacts).

**Out of scope:**
- Vendor engineering and design (DEL-059-04).
- Vendor document register and submittals as a primary deliverable (DEL-059-05).
- Re-issuance of the EPC SOW, Package Datasheet, or CWP (DEL-059-01/02/03).
- Approval authority — acceptance recommendation only; binding approval is reserved to the human owner (per program governance).

## Requirements

### R-01 Acceptance basis documents shall be complete and current
The EPC Integrator shall verify that DEL-059-01, DEL-059-02, and DEL-059-03 are at their accepted snapshot at the time of vendor package review. Source: `_CONTEXT.md` Scope; DELIVERABLE_REGISTER rows 462-464.

### R-02 Vendor document review log
A vendor document review log shall be produced covering all vendor submittals included in DEL-059-05. Each entry shall record document ID, revision, review disposition (accept / accept with comment / reject), reviewer, and date. Source: `_CONTEXT.md` Anticipated Artifacts (vendor document review log); ASSUMPTION on field set (standard EPC acceptance practice).

### R-03 Package acceptance checklist
A package acceptance checklist shall be produced that maps each Scope-of-Work item (SOW-0181, SOW-0182, SOW-0183, SOW-0184) and each Package Datasheet attribute to a verification status: covered / partial / open. Source: `_CONTEXT.md` Covers Scope Items; ASSUMPTION on mapping form.

### R-04 Test and inspection evidence
The EPC Integrator shall collect and verify test and inspection evidence from the vendor package. The acceptable ITP scope and acceptance criteria for the storage bullet package are TBD — not specified in the locally accessible source slices and shall be aligned with the Package Datasheet (DEL-059-02). Source: `_CONTEXT.md` Anticipated Artifacts; `4-25_Deepcut_DBM.md` line 1629 (bullet design parameters TBD).

### R-05 Turnover evidence
Turnover evidence shall demonstrate readiness for facility handoff, including vendor turnover documentation per DEL-059-05 and CWP turnover items per DEL-059-03. Specific turnover record set is TBD pending DEL-059-05 outputs.

### R-06 Spacing and siting verification (API 2510)
The package as installed/planned shall be verified against the pressurized-bullet siting and spacing table reproduced in the design basis: max 6 bullets per cluster; 15.24 m between clusters; 38.1 m to property line; 30.48 m to flare; 15.24 m to fired heater; 30.48 m to atmospheric tanks; 3.05 m to spill containment. Source: `4-25_Deepcut_DBM.md` lines 245-266 (API 2510). Final layout verification depends on plot plan CIV-235633-5002 which is identified as an open external deliverable gap (`4-25_Deepcut_DBM.md` lines 237, 323) — verification is TBD pending receipt of the governing plot plan.

### R-07 Storage capacity verification
The package as accepted shall total 16 x 120,000 USG NGL storage bullets at 04-25, replacing the retired C3/C4 storage scope. Source: `4-25_Deepcut_DBM.md` line 1629; line 492 (Combined-Facility Storage table).

### R-08 Spill control / grading interface
Acceptance shall confirm that grading under the bullets slopes to redirect accidental release away from pipe rack and process areas and that a berm / elevation decline / surface-control feature has been considered for containment, as required by source. Source: `4-25_Deepcut_DBM.md` line 2722.

### R-09 Provenance discipline
All acceptance findings shall cite their evidence (vendor document ID + revision + section, or EPC basis document section). Unsupported items shall be recorded as TBD rather than resolved silently. ASSUMPTION (program governance pattern — K-PROV-1).

## Standards

| Standard | Relevance | Local availability |
|---|---|---|
| API 2510 | Pressurized bullet spacing/siting | Cited by DBM; clause text not locally available (location TBD) |
| Modified API 650 | Adjacent condensate tank spec (interface context only) | `4-25_Deepcut_DBM.md` line 1646 |
| API 2000 | Tank venting/blanket gas (interface context only) | `4-25_Deepcut_DBM.md` line 1663 |
| 26020-Package_Requirements.docx heading 14 | Workbook-level package requirements for PKG-059 | Binary source; slice not extracted (location TBD) |

## Verification

| Req | Verification approach |
|---|---|
| R-01 | Records check against accepted snapshots of DEL-059-01/02/03 |
| R-02 | Inspection of vendor document review log file (presence + completeness audit) |
| R-03 | Inspection of acceptance checklist coverage against SOW-0181..0184 and Package Datasheet attributes |
| R-04 | Inspection of test/inspection evidence package; criteria set TBD |
| R-05 | Inspection of turnover evidence set against DEL-059-03 and DEL-059-05 outputs |
| R-06 | Layout review against API 2510 spacing table; gated by plot plan CIV-235633-5002 (TBD) |
| R-07 | Quantity and capacity reconciliation against DBM 04-25 basis (line 1629) |
| R-08 | Civil grading and containment review against DBM line 2722 |
| R-09 | Sampling audit of acceptance findings for cited evidence |

## Documentation

The deliverable shall produce, at minimum, the four anticipated artifacts (`_CONTEXT.md`):
- vendor document review log,
- package acceptance checklist,
- test/inspection evidence record,
- turnover evidence record.

Format and storage location for each artifact: TBD (to be aligned with program documentation standards).
