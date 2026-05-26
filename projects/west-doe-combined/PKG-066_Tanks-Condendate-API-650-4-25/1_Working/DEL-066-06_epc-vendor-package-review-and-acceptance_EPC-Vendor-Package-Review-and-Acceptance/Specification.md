# Specification: DEL-066-06 — EPC Vendor Package Review and Acceptance (PKG-066)

> Normative requirements for the EPC Integrator review-and-acceptance activity covering the PKG-066 Condensate Storage Tanks (4-25) vendor package. Requirements cite the originating source slice; inferred requirements are labeled `ASSUMPTION`. Where the locally accessible source does not yet establish a normative value, the requirement is marked `TBD` with the verification owner indicated.

## Scope

### In scope
- EPC Integrator-led review of the Package Vendor's engineered equipment package (DEL-066-04) and vendor document turnover package (DEL-066-05) for PKG-066 — Condensate Storage Tanks at 4-25 Deepcut.
- Verification of vendor scope, equipment, design basis, interfaces, and turnover documentation against the EPC Scope of Work (DEL-066-01), Package Datasheet (DEL-066-02), and Construction Work Package (DEL-066-03).
- Issuance of acceptance disposition (accept / accept-with-conditions / reject-and-resubmit) supported by review evidence.
- Compilation of the review-and-acceptance evidence set: vendor document review log, package acceptance checklist, test/inspection evidence, turnover evidence.

### Out of scope
- Authoring of vendor engineering documents (those are vendor production-unit outputs under DEL-066-04 / DEL-066-05).
- Mechanical re-design of the equipment package.
- Acceptance of items outside the PKG-066 package boundary (other packages have their own DEL-NN-06 acceptance deliverables).
- Field installation acceptance and pre-commissioning sign-off (those are construction/commissioning deliverables, not the vendor-package acceptance deliverable).

## Requirements

### REQ-066-06-01 — Coverage of EPC anchor deliverables (R-MUST)
The review-and-acceptance evidence set MUST demonstrate, for each applicable section, that the vendor package satisfies, conflicts with, or has an open item against:
- the EPC Scope of Work (DEL-066-01),
- the Package Datasheet (DEL-066-02), and
- the Construction Work Package (DEL-066-03).

Source: `DELIVERABLE_REGISTER.csv` row 503 ("review, integration acceptance, and handoff readiness against the EPC Scope of Work, Package Datasheet, and Construction Work Package").

### REQ-066-06-02 — Vendor document review log (R-MUST)
The EPC Integrator MUST maintain a vendor document review log capturing, for each vendor document submission, at minimum:
- vendor document ID and revision,
- date received and date reviewed,
- review disposition (Code 1 / Code 2 / Code 3 or equivalent acceptance code — exact coding `TBD`, to be aligned with project document control),
- comment log reference (if applicable),
- final accepted revision.

Source: anticipated artifact list in `_CONTEXT.md`; ASSUMPTION on disposition coding scheme (no source-defined coding found in locally accessible references).

### REQ-066-06-03 — Vendor deliverable coverage (R-MUST)
The review log MUST cover, at minimum, every vendor engineering deliverable enumerated in the package requirements for `26020-01-PT-19-004 - Tanks, Condensate`:
- Core vendor documents: PRQ-009 (Vendor Document Index), DOC-008 (Vendor Document Control Procedure), QLT-006 (Supplier Quality Plan), QLT-003 (ITP), QLT-013 (MTRs/Certificates), QLT-020 (Inspection Release Certificate), QLT-021 (Manufacturing Record Book / Vendor Data Book), PRQ-013 (Logistics/Shipping Plan), PRQ-015 (SPIR), PRQ-016 (Vendor Data Book / Final Supplier Documentation).
- Core package engineering: MEC-001, MEC-002, MEC-003, MEC-006, MEC-014, MEC-016, MEC-017, MEC-018, MEC-021, MEC-022, MEC-023, MEC-024, MEC-025.
- Storage-tank-specific: MEC-005 (Static Equipment Specifications), MEC-011 (Storage Tank Data Sheets).
- Relief / flare / vent design (applicability per Datasheet): PRO-014, PRO-015, PRO-016 (and downstream IDs listed in source).

Source: `26020-Package_Requirements.docx` lines 5060-5119 (extracted from package-requirements text).

### REQ-066-06-04 — Acceptance checklist by interface applicability (R-MUST)
The package acceptance checklist MUST contain explicit acceptance items for every interface marked "Yes" in the package interface summary (see Datasheet "Interface Applicability"). Interfaces marked "No" SHOULD be recorded as "Not applicable per source" rather than omitted, so reviewer scope is auditable.

Source: `26020-Package_Requirements.docx` lines 5014-5055 (package interface summary).

### REQ-066-06-05 — Tank design conformance (R-MUST)
Acceptance evidence MUST verify that the vendor-supplied condensate storage tanks conform to:
- Modified API 650 atmospheric tank design with 16 oz test pressure (`4-25_Deepcut_DBM.md` lines 518, 1646-1647).
- Maximum fill 90% of tank volume with thermal expansion review (`4-25_Deepcut_DBM.md` lines 519, 1648).
- Blanket gas system sized per API 2000 to prevent winter vacuum (`4-25_Deepcut_DBM.md` lines 520, 1663).
- Product condensate tanks non-insulated; slop tank fully insulated (`4-25_Deepcut_DBM.md` lines 1644-1645). NOTE: PKG-066 is the on-spec product tank package (TK-9110-1…-9150-1); slop-tank verification belongs to a different package and is out of scope (ASSUMPTION based on tag set in `4-25_Deepcut_DBM.md` line 2625).

### REQ-066-06-06 — Resolution of DBM open items (R-MUST)
The acceptance package MUST record the status of each Deepcut DBM open item relevant to the condensate tank package, including at minimum:
- confirmation of condensate flow values,
- slop tank SG (TBC),
- truck / vacuum-truck assumptions,
- tank venting and isolation philosophy,
- EPRV sizing,
- thermal expansion,
- transfer-pump operating conditions (where transfer pumps are within or interfacing with the package).

Each item MUST be marked: Resolved (with cite), Deferred to detailed engineering, or Open (with owner). Source: `4-25_Deepcut_DBM.md` lines 1663, 1815.

### REQ-066-06-07 — Test / inspection evidence completeness (R-MUST)
Test and inspection evidence MUST include, at minimum:
- executed ITP (QLT-003) with hold/witness sign-offs,
- Material Test Reports / certificates (QLT-013),
- NDE reports per ITP,
- Equipment FAT / Performance Test Report (MEC-022) where applicable,
- Inspection Release Certificate (QLT-020).

Source: `26020-Package_Requirements.docx` lines 5067-5074, 5099-5102.

### REQ-066-06-08 — Turnover evidence completeness (R-MUST)
Turnover evidence MUST include:
- Manufacturing Record Book / Vendor Data Book (QLT-021) and Final Supplier Documentation (PRQ-016) / Mechanical Final Documentation (MEC-023),
- Equipment IOM Manual (MEC-025),
- Mechanical Spares / Special Tools requirements (MEC-024),
- Spare Parts Interchangeability Record (PRQ-015),
- Logistics / Shipping Plan (PRQ-013).

Source: `26020-Package_Requirements.docx` lines 5074-5107.

### REQ-066-06-09 — Acceptance authority (R-MUST)
Final acceptance signature authority MUST be the EPC Integrator's mechanical discipline lead or designee. No agent or automated tool may sign or issue acceptance for reliance. Source: project governance (CHIRALITY K-AUTH-1, applied as ASSUMPTION to this deliverable's acceptance signature; project-specific signatory roster `TBD`).

### REQ-066-06-10 — Disposition recording (R-MUST)
For each acceptance checklist item, the recorded disposition MUST be one of: ACCEPT, ACCEPT-WITH-CONDITIONS (conditions enumerated), REJECT (rebid/resubmit required), or DEFER (with owner and date). Source: ASSUMPTION; specific project disposition vocabulary `TBD` and should align with the document control procedure referenced by DOC-008.

## Standards

| Standard | Applicability | Source |
|---|---|---|
| API 650 (modified) | Tank design and fabrication basis | `4-25_Deepcut_DBM.md` lines 518, 1646; `26020-Package_Requirements.docx` line 5012 |
| API 2000 | Blanket gas / venting basis | `4-25_Deepcut_DBM.md` lines 520, 1663 |
| Project document control procedure (ID `TBD`) | Vendor document review coding and disposition | Referenced via DOC-008 in `26020-Package_Requirements.docx` line 5064; `TBD` location |

## Verification

| Requirement | Verification Method |
|---|---|
| REQ-066-06-01 | Cross-reference matrix: each section of DEL-066-01 / DEL-066-02 / DEL-066-03 to acceptance-checklist line items. |
| REQ-066-06-02 | Inspection of completed vendor document review log; field presence audit. |
| REQ-066-06-03 | Coverage audit: each enumerated vendor deliverable ID maps to a review-log row. |
| REQ-066-06-04 | Checklist completeness audit against the interface summary table. |
| REQ-066-06-05 | Review of MEC-011 (Storage Tank Data Sheets) and MEC-014 (Mechanical Calculation Package) against the cited DBM values. |
| REQ-066-06-06 | DBM-open-items disposition register included as an annex to the acceptance package. |
| REQ-066-06-07 | Document inventory check against the enumerated artifact list. |
| REQ-066-06-08 | Turnover document inventory check against the enumerated artifact list. |
| REQ-066-06-09 | Signed acceptance record bearing the designated authority's signature. |
| REQ-066-06-10 | Inspection of disposition column in the checklist. |

## Documentation

Required artifacts that constitute this deliverable (anticipated):

- Vendor document review log
- Package acceptance checklist
- Test / inspection evidence binder (or index pointing to vendor-issued evidence)
- Turnover evidence binder (or index pointing to vendor-issued evidence)
- DBM-open-items disposition annex
- Signed acceptance record

Source: `_CONTEXT.md` ("Anticipated Artifacts"); `DELIVERABLE_REGISTER.csv` row 503.
